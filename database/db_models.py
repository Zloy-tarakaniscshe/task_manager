from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), Column("name"), nullable=False)
    fullname: Mapped[str] = mapped_column(String(50), Column("fullname"), nullable=False)
    email: Mapped[str] = mapped_column(String(80), Column("email"), nullable=False, unique=True)
    tasks: Mapped[List["Tasks"]] = relationship(back_populates="executor", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}, email={self.email})"

    def __str__(self) -> str:
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}"


class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    title: Mapped[str] = mapped_column(String(250), Column("title"), nullable=False)
    description: Mapped[str] = mapped_column(String(600), Column("description"), nullable=False)
    executor: Mapped["User"] = relationship(back_populates="tasks")

    def __repr__(self) -> str:
        return f"Tasks(id={self.id}, user_id={self.user_id}, title={self.title}, description={self.description})"

    def __str__(self) -> str:
        return f"Tasks(id={self.id}, user_id={self.user_id}, title={self.title}"
