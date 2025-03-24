from dependency_injector import containers, providers
from dependency_injector.wiring import Provide
from .service.authService import AuthService
from .service.baseService import BaseService
from .dao.database import Database
from .dao.session_maker import DatabaseSessionManager
from config import settings

class Container(containers.DeclarativeContainer):
    
    db = providers.Singleton(
        Database,
        db_url=settings.get_db_url()
        )
    
    sessionManager = providers.Singleton(
        DatabaseSessionManager,
        session_maker=db.provided.session,
        )
    
    session_dependency =  providers.Callable(DatabaseSessionManager.get_session)
    transaction_session_dependency = providers.Callable(DatabaseSessionManager.get_transaction_session)
    
    base_service = providers.Factory(
        BaseService,
        sessionManager=sessionManager,
        )
    # brand_service = providers.Factory(AuthService)
