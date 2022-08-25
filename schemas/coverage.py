from pydantic import BaseModel


class Coverage(BaseModel):
    warehouse: str
    name: str
    year: int
    month: str
    day: int
    shift: str
