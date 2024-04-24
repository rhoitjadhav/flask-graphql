# Packages
import graphene

# Modules
from src import db
from src.repositories.trips_repository import TripsRepository


class TripsSchema(graphene.ObjectType):
    id = graphene.String(required=False)
    destination_name = graphene.String()
    start_date = graphene.Date()
    end_date = graphene.Date()


class UpdateTripInput(graphene.InputObjectType):
    id = graphene.ID()
    destination_name = graphene.String()
    start_date = graphene.Date()
    end_date = graphene.Date()


class CreateTrip(graphene.Mutation):
    class Arguments:
        destination_name = graphene.String()
        start_date = graphene.Date()
        end_date = graphene.Date()

    ok = graphene.Boolean()
    trip = graphene.Field(TripsSchema)

    def mutate(root, info, destination_name, start_date, end_date):
        trip = TripsRepository(destination_name=destination_name,
                               start_date=start_date,
                               end_date=end_date)
        db.session.add(trip)
        db.session.commit()
        return CreateTrip(trip=trip, ok=True)


class UpdateTrip(graphene.Mutation):
    class Arguments:
        trip_data = UpdateTripInput(required=True)

    ok = graphene.Boolean()
    trip = graphene.Field(TripsSchema)

    def mutate(root, info, trip_data=None):
        trip = TripsRepository.update(trip_data.id, trip_data)
        return UpdateTrip(trip=trip, ok=True)


class DeleteTrip(graphene.Mutation):
    class Arguments:
        trip_id = graphene.ID()

    ok = graphene.Boolean()
    id = graphene.ID()

    def mutate(root, info, trip_id):
        TripsRepository.delete(trip_id=trip_id)
        return DeleteTrip(id=trip_id, ok=True)


class TripsMutation(graphene.ObjectType):
    create_trip = CreateTrip.Field()
    update_trip = UpdateTrip.Field()
    delete_trip = DeleteTrip.Field()


class Query(graphene.ObjectType):
    trips = graphene.List(TripsSchema)

    def resolve_trips(root, info):
        return [TripsSchema(id=str(trip.id),
                            destination_name=trip.destination_name,
                            start_date=trip.start_date,
                            end_date=trip.end_date)
                for trip in TripsRepository.get_all()]


schema = graphene.Schema(query=Query, mutation=TripsMutation)
