from sqlalchemy import Column, Integer, Boolean, Float
from app.database import Base


class Measurement(Base):
    __tablename__ = "measurements"

    timestamp = Column(Integer, primary_key=True, autoincrement=False)
    insideHumidity = Column(Float, nullable=False)
    outsideHumidity = Column(Float, nullable=False)
    insideTemperature = Column(Float, nullable=False)
    outsideTemperature = Column(Float, nullable=False)
    speed = Column(Integer, nullable=False)
    pumpRelayState = Column(Boolean, nullable=False)
    humidifierRelayState = Column(Boolean, nullable=False)
    reboot = Column(Boolean, nullable=False)

    pidKp = Column(Float, nullable=False)
    pidKi = Column(Float, nullable=False)
    pidKd = Column(Float, nullable=False)
    humidityUpperBoundary = Column(Integer, nullable=False)
    humidityLowerBoundary = Column(Integer, nullable=False)
    pumpTemperatureDelta = Column(Float, nullable=False)
    targetTemperature = Column(Float, nullable=False)
