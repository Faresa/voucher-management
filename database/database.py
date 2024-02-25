from sqlalchemy import create_engine, Column, String, Integer, DateTime ,Boolean
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

# SQLite database URL
DATABASE_URL = "sqlite:///./database/database.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create the Database instance
database = Database(DATABASE_URL)

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the Voucher model
class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    redemption_limit = Column(Integer)
    expiration_date = Column(DateTime)
    redeemed_times = Column(Integer, default=0)
    active = Column(Boolean, default=True)

# Create the database tables
def create_database():
    Base.metadata.create_all(bind=engine)
