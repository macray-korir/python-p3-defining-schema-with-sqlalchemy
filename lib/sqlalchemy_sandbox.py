from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base  # Updated import

# Create an instance of the declarative base class
Base = declarative_base()

# Define the Student class which represents the 'students' table
class Student(Base):
    __tablename__ = 'students'

    # Define columns for the table
    id = Column(Integer(), primary_key=True)
    name = Column(String())

# Define the Course class which represents the 'courses' table
class Course(Base):
    __tablename__ = 'courses'

    # Define columns for the table
    id = Column(Integer(), primary_key=True)
    course_name = Column(String())


if __name__ == '__main__':
    # Create an SQLite engine and point it to the 'students.db' file
    engine = create_engine('sqlite:///students.db')

    # Create all tables associated with our Base class (in this case, the 'students' and 'courses' tables)
    Base.metadata.create_all(engine)