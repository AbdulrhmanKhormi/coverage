from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from database import con

from schemas.warehouse import Warehouse
from schemas.coverage import Coverage
from schemas.admin import Admin
from schemas.employee import Employee

from models.admin import admin
from models.warehouse import warehouse
from models.coverage import coverage
from models.employee import employee as emp

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/test/employee")
async def employees(employee: Employee):
    data = con.execute(emp.insert().values(
        username=employee.username,
        name=employee.name,
        email=employee.email,
        level=employee.level,
        gender=employee.gender,
        city=employee.city
    ))
    return data


@app.post("/test/coverage")
async def coverages(cov: Coverage):
    data = con.execute(coverage.insert().values(
        warehouse=cov.warehouse,
        name=cov.name,
        date=cov.date,
        shift=cov.shift,
    ))
    return data


@app.post("/test/warehouse")
async def warehouses(wh: Warehouse):
    data = con.execute(warehouse.insert().values(
        name=wh.name,
        dep=wh.dep,
        capacity=wh.capacity,
        current_cap=wh.current_cap,
        city=wh.city
    ))
    return data


@app.post("/test/admin")
async def admins(ad: Admin):
    data = con.execute(admin.insert().values(
        username=ad.username,
        name=ad.name,
        email=ad.email,
        level=ad.level,
        gender=ad.gender,
        city=ad.city
    ))
    return data


@app.post("/test/emp")
async def get_employee(req: Request):
    month = await req.json()
    data = con.execute(coverage.select().where(coverage.c.month == month['month'])).fetchall()
    return data


@app.post("/test/generate")
async def generate(req: Request):
    month = await req.json()
    data = con.execute(coverage.insert().values())


