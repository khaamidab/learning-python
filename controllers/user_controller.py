from typing import List
from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import UserService

router = APIRouter()


@router.get("/users")
async def get_all_users(user_service: UserService) -> List[User]:
    return await user_service.get_all_users()


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int, user_service: UserService) -> User:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users")
async def create_user(user: User, user_service: UserService) -> User:
    return await user_service.create_user(user)


@router.put("/users/{user_id}")
async def update_user(
    user_id: int,
    user: User,
    user_service: UserService
) -> User:
    existing_user = await user_service.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return await user_service.update_user(user_id, user)


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, user_service: UserService) -> None:
    existing_user = await user_service.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    await user_service.delete_user(user_id)
