from pydantic import BaseModel


class ManualControl(BaseModel):
    allowed: bool
    value: bool


class Pump(BaseModel):
    temperatureDelta: float
    manualControl: ManualControl


class PID(BaseModel):
    kp: float
    ki: float
    kd: float


class Interval(BaseModel):
    low: int
    high: int


class TopLevelParams(BaseModel):
    sendingInterval: int
    grDelta: float


class Relay(BaseModel):
    manualControl: ManualControl


class Humidity(BaseModel):
    interval: Interval
    relay: Relay


class Temperature(BaseModel):
    targetTemperature: float
    pump: Pump
    pid: PID


class Config(BaseModel):
    temperature: Temperature
    topLevelParams: TopLevelParams
    humidity: Humidity
