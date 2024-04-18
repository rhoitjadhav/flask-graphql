from pydantic import BaseModel


class UsersSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str
