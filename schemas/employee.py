from pydantic import BaseModel


class Employee(BaseModel):
    username: str
    name: str
    email: str
    level: int
    gender: str
    city: str
