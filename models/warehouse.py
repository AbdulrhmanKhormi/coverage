from sqlalchemy import Table, Column
from database import meta
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, CHAR

warehouse = Table(
    "warehouse", meta,
    Column("name", VARCHAR(20), primary_key=True),
    Column("dep", VARCHAR(255)),
    Column("capacity", Integer),
    Column("current_cap", Integer),
    Column("city", VARCHAR(255))
)
