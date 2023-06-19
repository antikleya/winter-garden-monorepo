from pydantic import BaseModel, validator
from app.config import MIN_TARGET_TEMP, MAX_TARGET_TEMP, MIN_PUMP_TEMPERATURE_DELTA, MAX_PUMP_TEMPERATURE_DELTA, \
    MAX_TARGET_HUMIDITY


MAX_SENDING_INTERVAL = 15
MIN_GR_DELTA = 0
MAX_GR_DELTA = 15


class ManualControl(BaseModel):
    allowed: bool
    value: bool


class Pump(BaseModel):
    temperatureDelta: float
    manualControl: ManualControl

    @validator('temperatureDelta')
    def temperature_delta_in_interval(cls, value):
        if value < MIN_PUMP_TEMPERATURE_DELTA or value > MAX_PUMP_TEMPERATURE_DELTA:
            raise ValueError(
                "Pump temperature delta has to be between "
                f"{MIN_PUMP_TEMPERATURE_DELTA} and {MAX_PUMP_TEMPERATURE_DELTA}"
            )
        return value


class PID(BaseModel):
    kp: float
    ki: float
    kd: float

    @validator('*')
    def pid_is_positive(cls, value):
        if value < 0:
            raise ValueError("PID values can't be negative")
        return value


class Interval(BaseModel):
    low: int
    high: int


class TopLevelParams(BaseModel):
    sendingInterval: int
    grDelta: float

    @validator('sendingInterval')
    def sending_interval_in_boundaries(cls, value):
        if value <= 0 or value > MAX_SENDING_INTERVAL:
            raise ValueError(f"Sending interval must be between 0 and {MAX_SENDING_INTERVAL}")
        return value

    @validator('grDelta')
    def gr_delta_in_interval(cls, value):
        if value < MIN_GR_DELTA or value > MAX_GR_DELTA:
            raise ValueError(f"Hysteresis delta value has to be between {MIN_GR_DELTA} and {MAX_GR_DELTA}")
        return value


class Relay(BaseModel):
    manualControl: ManualControl


class Humidity(BaseModel):
    interval: Interval
    relay: Relay

    @validator('interval')
    def correct_interval(cls, value: Interval):
        if value.low >= value.high:
            raise ValueError('Bottom humidity interval value has to be less than the top one')
        if value.low < 0 or value.high < 0 or value.high > MAX_TARGET_HUMIDITY:
            raise ValueError(f"Humidity interval values have to be between 0 and {MAX_TARGET_HUMIDITY}")
        return value


class Temperature(BaseModel):
    targetTemperature: float
    pump: Pump
    pid: PID

    @validator('targetTemperature')
    def target_temperature_in_interval(cls, value: float):
        if value < MIN_TARGET_TEMP or value > MAX_TARGET_TEMP:
            raise ValueError(f"Target temperature has to be between {MIN_TARGET_TEMP} and {MAX_TARGET_TEMP}")
        return value


class Config(BaseModel):
    temperature: Temperature
    topLevelParams: TopLevelParams
    humidity: Humidity
