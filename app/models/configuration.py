from sqlalchemy import Integer, SmallInteger, DateTime, Text
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.db.base import Base

class Configuration(Base):
    __tablename__ = "configurations"
    
    configurationID: Mapped[int]    = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str]               = mapped_column(VARCHAR(30), nullable=False)
    value: Mapped[str | None]       = mapped_column(Text, nullable=False)
    remarks: Mapped[str | None]     = mapped_column(Text, nullable=False)
    insertedBy: Mapped[int]         = mapped_column(Integer, nullable=False)
    dateInserted: Mapped[datetime]  = mapped_column(DateTime, nullable=True, default=datetime.now())
    updatedBy: Mapped[int]          = mapped_column(Integer, nullable=False, default=0)
    dateUpdated: Mapped[datetime]   = mapped_column(DateTime, nullable=True)
    status: Mapped[int]             = mapped_column(
        SmallInteger, 
        nullable=False, 
        default=0, 
        comment="0=Hidden, 1=Shown"
    )
