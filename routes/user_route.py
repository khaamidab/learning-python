from fastapi import FastAPI
from controllers.user_controller import router as user_router


def create_routes(app: FastAPI) -> None:
    app.include_router(user_router)
