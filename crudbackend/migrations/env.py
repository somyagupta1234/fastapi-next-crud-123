import asyncio
import os
from logging.config import fileConfig
from alembic import context
from tortoise import Tortoise, exceptions
from dotenv import load_dotenv

# Load environment variables (if .env file exists)
load_dotenv()

# Load Alembic configuration (optional logging setup)
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define the database URL (fetch from Alembic config or fallback to SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./db.sqlite3")

async def run_migrations():
    """Initialize Tortoise-ORM and apply migrations."""
    try:
        await Tortoise.init(
            db_url=DATABASE_URL,
            modules={"models": ["crudbackend.models"]}  # ✅ Ensure your actual model path is correct
        )
        print("✅ Running Tortoise migrations...")
        await Tortoise.generate_schemas(safe=True)  # ✅ Creates tables only if they don't exist
        print("✅ Migrations completed successfully.")
    except exceptions.DBConnectionError as e:
        print(f"❌ Database connection failed: {e}")
    finally:
        await Tortoise.close_connections()

def main():
    """Runs migrations in an async-safe manner."""
    try:
        asyncio.run(run_migrations())
    except RuntimeError:
        # Handle nested event loop issues (happens inside some environments)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_migrations())

if __name__ == "__main__":
    main()  # ✅ Ensures proper execution
