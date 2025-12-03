from fastapi import FastAPI,HTTPException
from models import Employee, Promotion
from mongoengine import connect, LongField

connect(
    db="employeedb",
    host="mongodb+srv://admin:admin@cluster0.teul3as.mongodb.net/?appName=Cluster0"
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Microservice fetching"}

@app.get("/employee")
def get_employee():
    em = Employee.objects()
    l = list(em)
    for e in em:
        l.append(e.to_mongo().to_dict())

    return {"status": "success", "employees": l}

@app.get("/promotion")
def get_promotion():
    pro = Promotion.objects()
    l = list(pro)
    for p in pro:
        l.append(p.to_mongo().to_dict())

    return {"status": "success", "promotions": l}

@app.get("/employee/{salary}")
def get_employee(salary:int):
    emp = Employee.objects(SALARY__lt=salary)
    if emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    l = list(emp)
    for e in emp:
        l.append(e.to_mongo().to_dict())

    return {"status": "success", "employees": l}

@app.get("/employee/filter/sd")
def get_employees(salary:int, department:str):
    emp = Employee.objects(SALARY__lt=salary, DEPARTMENT=department)
    if emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    l = list(emp)
    for e in emp:
        l.append(e.to_mongo().to_dict())

    return {"status": "success", "employees": l}

@app.get("/employee/order/fields")
def get_employee2():
    em = Employee.objects().order_by("-SALARY", "-ID")
    l = list(em)
    for e in em:
        l.append(e.to_mongo().to_dict())

    return {"status": "success", "employees": l}




