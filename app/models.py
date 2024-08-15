from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base  # Import from app.database


class Technology(Base):
    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    classification = Column(String, index=True)
    description = Column(String)
    in_production = Column(Boolean, default=False)
    status = Column(Boolean, default=True)
    license_type = Column(String)
