from fastapi import FastAPI
from pydantic import BaseModel
from .database import Base, engine
from .routers import router


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(router=router, prefix="/api", tags=["todos"])






class Item(BaseModel):
    name: str
    price: float
    description: str = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def creat_item(item: Item):
    print(f"Received item:{item}")
    return {"message": "Item received","item": item}

