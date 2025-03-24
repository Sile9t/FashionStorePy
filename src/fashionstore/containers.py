from dependency_injector import containers, providers
from dependency_injector.wiring import Provide
from .service.authService import AuthService
from .dao.database import async_session_maker
from .dao.session_maker import DatabaseSessionManager

class Container(containers.DeclarativeContainer):
    sessionManager = providers.Singleton(DatabaseSessionManager, async_session_maker)
    
    session_dependency =  providers.Callable(DatabaseSessionManager.get_session)
    transaction_session_dependency = providers.Callable(DatabaseSessionManager.get_transaction_session)
    
    brand_service = providers.Factory(AuthService)
