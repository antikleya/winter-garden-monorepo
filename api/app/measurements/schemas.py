from pydantic import BaseModel
from datetime import datetime


class MeasurementSchema(BaseModel):
    timestamp: datetime
    insideHumidity: float
    outsideHumidity: float
    insideTemperature: float
    outsideTemperature: float
    speed: int
    pumpRelayState: bool
    humidifierRelayState: bool
    reboot: bool

    pidKp: float
    pidKi: float
    pidKd: float
    humidityUpperBoundary: int
    humidityLowerBoundary: int
    pumpTemperatureDelta: float
    targetTemperature: float

    class Config:
        orm_mode = True
