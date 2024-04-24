# Modules
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.exc import NoResultFound

from src import db


class TripsRepository(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destination_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(DateTime, default=datetime.utcnow)
    end_date = db.Column(DateTime, default=datetime.utcnow)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_all(cls, limit=10):
        try:
            return TripsRepository.query.limit(limit).all()
        except NoResultFound:
            return None

    @classmethod
    def update(cls, trip_id, trip_data):
        trip = TripsRepository.query.filter_by(id=trip_id).first()
        if not trip:
            return False

        trip.destination_name = trip_data.destination_name
        trip.start_date = trip_data.start_date
        trip.end_date = trip_data.end_date
        db.session.commit()
        return trip

    @classmethod
    def delete(cls, trip_id):
        TripsRepository.query.filter_by(id=trip_id).delete()
        db.session.commit()
