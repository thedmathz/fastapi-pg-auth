from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    userID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    password: Mapped[str] = mapped_column(VARCHAR(256), nullable=False)
    fname: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    mname: Mapped[str | None] = mapped_column(VARCHAR(30), nullable=True)
    lname: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    gender: Mapped[str] = mapped_column(VARCHAR(10), nullable=False)
