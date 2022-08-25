from pydantic import BaseModel


class Warehouse(BaseModel):
    name: str
    dep: str
    capacity: int
    current_cap: int
    city: str
