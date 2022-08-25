from pydantic import BaseModel


class Admin(BaseModel):
    username: str
    name: str
    email: str
    level: int
    gender: str
    city: str
