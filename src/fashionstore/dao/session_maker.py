from functools import wraps
from typing import Optional
from sqlalchemy import text
from database import async_session_maker
from loguru import logger

def connection(self, isolation_level: Optional[str] = None, commit: bool = True):
    def decorator(method):
        @wraps(method)
        async def wrapper(*args, **kwargs):
            async with self.async_session_maker() as session:
                try:
                    if isolation_level:
                        # await session.connection(execution_options=dict(isolation_level=isolation_level.value)) #alternative way to set transaction isolation
                        await session.execute(text(f"SET TRANSACTION ISOLATION LEVEL {isolation_level}"))
                    
                    result = await method(*args, session= session, **kwargs)

                    if commit:
                        await session.commit()
                    return result
                except Exception as e:
                    await session.rollback()
                    raise e
                finally:
                    await session.close()
            
        return wrapper
    return decorator