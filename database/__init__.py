from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Ссылку для БД
SQLALCHEMY_DATABASE_URI = "sqlite:///pay.db"

# Подключения к БД
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Генерация сессий
SessionLocal = sessionmaker(bind=engine)

# Общий класс для моделей что бы использовать внутри models.py
Base = declarative_base()

from database import models

# Функция для генерации связей к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()