from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="intern")

class Intern(Base):
    __tablename__ = "interns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    track = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", backref="intern_profile")

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    status = Column(String, default="pending")
    intern_id = Column(Integer, ForeignKey("interns.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    intern = relationship("Intern", backref="submissions")

