#!/usr/bin/python3
"""Illustrate the creation of dynamic created table with fix attributes."""
from uuid import uuid4
from sqlalchemy import create_engine, Column, String, Integer, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine and metadata object
engine = create_engine("postgresql://many_user:many_pwd@localhost/many_db")
Base = declarative_base()

table_name = input("Enter table name: ")

class DynamicModel(Base):
    __tablename__ = table_name
    id = Column(String(50), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    courses = Column(ARRAY(String), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of inserting data using ORM
new_entry = DynamicModel(
        name='John Doe',
        email='johdoe@example.com',
        courses=['Math', 'Science']
        )
session.add(new_entry)
session.commit()

# Querying data
results = session.query(DynamicModel).all()
for row in results:
    print(row.id, row.name, row.email, row.courses)

# Close the session
session.close()

