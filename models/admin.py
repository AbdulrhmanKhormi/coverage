from sqlalchemy import Table, Column
from database import meta
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, CHAR

admin = Table(
    "admin", meta,
    Column("username", VARCHAR(20), primary_key=True),
    Column("name", VARCHAR(255)),
    Column("email", VARCHAR(255)),
    Column("level", Integer),
    Column("gender", CHAR),
    Column("city", VARCHAR(255))
)
