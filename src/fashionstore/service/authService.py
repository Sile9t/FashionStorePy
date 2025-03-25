from pydantic import BaseModel
from ..dao.schemas import UserCreateDto, UserDto
from ..dao.dao import UserDAO
from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import Provide
from .baseService import BaseService

class AuthService(BaseService):
    async def getUser(self, id: int = 0):
        userRecord = await UserDAO.find_one_or_none_by_id(
                self.sessionManager.get_session,
                id
            )

        if userRecord:
            user = UserDto.model_validate(userRecord)
            return user
        
        return None

    async def getAllUsers(self):
        userRecords = await UserDAO.find_all(self.sessionManager.get_session)

        users = UserDto.model_dump(userRecords)

        return users

    async def registerUser(self, values: UserCreateDto):
        userRecord = await UserDAO.add(self.sessionManager.get_session, values)
        user = UserDto.model_validate(userRecord)
        
        return user.id

    async def deleteUser(self, id: int):
        userRecord = await UserDAO.find_one_or_none_by_id(self.sessionManager.get_session, id)
        
        if userRecord:
            await UserDAO.delete(self.sessionManager.get_session, userRecord)
            user = UserDto.model_validate(userRecord)
            return user

        return None