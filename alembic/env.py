import os
import sys
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from alembic import context
from logging.config import fileConfig


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# 🔐 Load .env file manually
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# ✅ Use the real values directly
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_USER, DB_PASS, DB_HOST, DB_NAME]):
    raise Exception("Missing database environment variables.")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# Alembic config
config = context.config
fileConfig(config.config_file_name)
config.set_main_option("sqlalchemy.url", DATABASE_URL)

from app.database import Base
from app import models  # Make sure models are imported

target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

