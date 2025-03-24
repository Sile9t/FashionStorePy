from dependency_injector.wiring import Provide, inject
from ..dao.session_maker import DatabaseSessionManager
from sqlalchemy.ext.asyncio import AsyncSession

class BaseService():
    sessionManager: DatabaseSessionManager

    def __init__(
            self,
            sessionManager = DatabaseSessionManager
        ):
        self.sessionManager = sessionManager