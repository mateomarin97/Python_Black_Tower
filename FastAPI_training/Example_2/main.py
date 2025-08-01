from fastapi import FastAPI
from FastAPI_training.Example_2.database import engine, Base
from FastAPI_training.Example_2.routers import blog, user, authentication

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

Base.metadata.create_all(bind=engine)
