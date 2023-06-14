from pydantic import BaseModel


class ManualControl(BaseModel):
    allowed: bool
    value: bool


class Pump(BaseModel):
    temperatureDelta: int
    manualControl: ManualControl


class PID(BaseModel):
    kp: int
    ki: int
    kd: int


class Interval(BaseModel):
    low: int
    high: int


class TopLevelParams(BaseModel):
    sendingInterval: int
    grDelta: int


class Relay(BaseModel):
    manualControl: ManualControl


class Humidity(BaseModel):
    interval: Interval
    relay: Relay


class Temperature(BaseModel):
    targetTemp: int
    pump: Pump
    pid: PID


class Config(BaseModel):
    temperature: Temperature
    topLevelParams: TopLevelParams
    humidity: Humidity
