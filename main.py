from src.fashionstore import create_app
import asyncio

application = create_app()

if __name__ == "__main__":
    asyncio.run(application.run())