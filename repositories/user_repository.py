from typing import List
from models.user import User
from databases import Database
from sqlalchemy import select


class UserRepository:
    def __init__(self, database: Database):
        self.database = database

    async def get_all_users(self) -> List[User]:
        query = select([User])
        return await self.database.fetch_all(query)

    async def get_user_by_id(self, user_id: int) -> User:
        query = select([User]).where(User.id == user_id)
        return await self.database.fetch_one(query)

    async def create_user(self, user: User) -> User:
        query = User.insert().values(**user.dict())
        user.id = await self.database.execute(query)
        return user

    async def update_user(self, user_id: int, user: User) -> User:
        query = User.update().where(User.id == user_id).values(**user.dict())
        await self.database.execute(query)
        return user

    async def delete_user(self, user_id: int) -> None:
        query = User.delete().where(User.id == user_id)
        await self.database.execute(query)
