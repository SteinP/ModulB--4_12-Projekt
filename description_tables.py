import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения  с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"


# базовый класс моделей таблиц
Base = declarative_base()


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


class Athelete(Base):
    """
        athelete(
            "id" integer primary key autoincrement,
            "age" integer,
            "birthdate" text,
            "gender" text,
            "height" real,
            "name" text,
            "weight" integer,
            "gold_medals" integer,
            "silver_medals" integer,
            "bronze_medals" integer,
            "total_medals" integer,
            "sport" text,
            "country" text
            )
    """

    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key=True)
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)


class User(Base):
    __tablename__ = "user"
    """
        user(
            "id" integer primary key autoincrement,
            "first_name" text,
            "last_name" text,
            "gender" text,
            "email" text,
            "birthdate" text,
            "height" real
            )
    """
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
