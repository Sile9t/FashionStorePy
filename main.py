from src.fashionstore import create_app
import asyncio

app = create_app()

if __name__ == "__main__":
    asyncio.run(app.run())