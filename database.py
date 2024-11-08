from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./livros.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Teste de conexão
if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("conexão feita")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        db.close()
