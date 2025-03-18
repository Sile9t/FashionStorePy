from sqlalchemy.ext.asyncio import AsyncSession
from dao.base import BaseDAO
from models import User

class UserDAO(BaseDAO[User]):
    model = User
    
    # @classmethod
    # async def find_user_by_id(cls, session: AsyncSession, data_id: int):
    #     user = await session.get(cls.model, data_id)
        
    #     return user
    