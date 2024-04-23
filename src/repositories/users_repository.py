# Packages
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash

# Modules
from src import db
from src.schemas.users_schema import UsersSchema


class UsersRepository(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.set_password(password)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def set_password(self, password):
        self.password = generate_password_hash(password, salt_length=54)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_all(cls):
        try:
            return UsersRepository.query.all()
        except NoResultFound:
            return None

    @classmethod
    def get_by_id(cls, user_id):
        try:
            return UsersRepository.query.filter_by(id=user_id).first()
        except NoResultFound:
            return None

    @classmethod
    def delete(cls, user_id):
        UsersRepository.query.filter_by(id=user_id).delete()
        db.session.commit()

    @classmethod
    def update(self, user_id, users_schema: UsersSchema):
        user = UsersRepository.query.filter_by(id=user_id).first()
        if not user:
            return False

        user.name = users_schema.name
        user.username = users_schema.username
        user.password = users_schema.password
        user.username = users_schema.email
        db.session.commit()
        return True
