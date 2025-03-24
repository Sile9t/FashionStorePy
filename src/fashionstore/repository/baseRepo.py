from dependency_injector.wiring import Provide
from ..containers import DatabaseSessionManager
from sqlalchemy.orm import AsyncSession

class BaseRepo():
    dbSession: AsyncSession
    
    def __init__(self,session: Provide[DatabaseSessionManager]):
        self.dbSession = session
    