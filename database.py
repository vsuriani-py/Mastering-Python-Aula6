from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://dev_ops_aula01_user:dnwsQz9txG3mPtzlU4QOTz66z51w2qSf@dpg-cspth3lumphs73dmpgn0-a.oregon-postgres.render.com/dev_ops_aula01"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("conexão feita")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        db.close()
