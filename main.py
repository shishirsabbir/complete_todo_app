# importing packages
from fastapi import FastAPI
from database import engine, Base

from routers import auth, todos, admin, users

# creating the fastapi instance called app
app = FastAPI()

# create the database using sqlalchemy (initially)
Base.metadata.create_all(bind=engine)

# including routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

