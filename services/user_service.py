from typing import List
from models.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_all_users(self) -> List[User]:
        return await self.user_repository.get_all_users()

    async def get_user_by_id(self, user_id: int) -> User:
        return await self.user_repository.get_user_by_id(user_id)

    async def create_user(self, user: User) -> User:
        return await self.user_repository.create_user(user)

    async def update_user(self, user_id: int, user: User) -> User:
        return await self.user_repository.update_user(user_id, user)

    async def delete_user(self, user_id: int) -> None:
        await self.user_repository.delete_user(user_id)
