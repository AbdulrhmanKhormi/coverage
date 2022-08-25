from sqlalchemy import Table, Column, ForeignKey
from database import meta
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, CHAR, DATE
from models.warehouse import warehouse
from models.employee import employee

coverage = Table(
    "coverage", meta,
    Column("warehouse", VARCHAR(20), ForeignKey(warehouse.c.name)),
    Column("name", VARCHAR(255), ForeignKey(employee.c.username)),
    Column("year", Integer),
    Column("month", VARCHAR(10)),
    Column("day", Integer),
    Column("shift", CHAR)
)
