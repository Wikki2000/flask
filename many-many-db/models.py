#!/usr/bin/python3
"""This module illustrates a many-to-many relationship."""
from sqlalchemy import create_engine, String, Column, ForeignKey, Table
from sqlalchemy.exc import IntegrityError
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker, relationship
from uuid import uuid4

Base = declarative_base()
engine = create_engine("postgresql://many_user:many_pwd@localhost:5432/many_db")
session = sessionmaker(bind=engine)
session = session()

# Association Table
enrollments = Table("enrollments", Base.metadata,
    Column("studentId", String(50), ForeignKey("students.studentId"), primary_key=True),
    Column("courseId", String(50), ForeignKey("courses.courseId"), primary_key=True)
)

class Student(Base):
    """Defines the student class."""
    __tablename__ = "students"
    studentId = Column(String(50), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    name = Column(String(30), nullable=False)
    regNo = Column(String(30), nullable=False, unique=True)
    courses = relationship("Course", secondary=enrollments, backref="students")

class Course(Base):
    """Define the models for courese offer by student."""
    __tablename__ = "courses"
    courseId = Column(String(50), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    name = Column(String(30), nullable=False, unique=True)
    
Base.metadata.create_all(engine)

def get_session():
    """Retrieve session object to connect with db."""
    return session

def create_student(name, regNo):
    """Create and save student instance in database"""
    student = Student(name=name, regNo=regNo)
    try:
        session.add(student)
        session.commit()
        return student
    except IntegrityError:
        session.rollback()
        return None

def create_course(name):
    """Create and save course instance in database"""
    try:
        course = Course(name=name)
        session.add(course)
        session.commit()
        return course
    except IntegrityError:
        session.rollback()
        return None

def enroll_student(studentId, courseId):
    """Enroll a student in a course."""
    student = session.query(Student).get(studentId)
    course = session.query(Course).get(courseId)

    # Check if the enrollment already exists
    if course in student.courses:
        return False

    # Check if the required student and course instance is present in database
    #if not student or not course:
    #    return False
    try:
        student.courses.append(course)
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False
