from typing import Optional

from pydantic import BaseModel


class UsersSchema(BaseModel):
    id: Optional[int] = None
    name: str
    username: str
    password: str
    email: str
