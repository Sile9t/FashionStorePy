from ..containers import Container
from dependency_injector.wiring import Provide
from ..dao.session_maker import DatabaseSessionManager

class BaseService():
    sessionManager: DatabaseSessionManager

    def __init__(
            self,
            sessionManager = Provide[Container.sessionManager]
        ):
        self.sessionManager = sessionManager