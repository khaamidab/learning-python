from fastapi import FastAPI
from routes.user_route import create_routes
from services.user_service import UserService
from repositories.user_repository import UserRepository
from databases import Database
import os

app = FastAPI()

# Load environment variables
database_url = os.getenv("DATABASE_URL")

# Create database connection
database = Database(database_url)
user_repository = UserRepository(database)
user_service = UserService(user_repository)


@app.on_event("startup")
async def startup() -> None:
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()

create_routes(app)
