from pydantic import BaseModel, validator
from datetime import datetime
import pytz
from app.config import TZ, MAX_TARGET_HUMIDITY, MAX_TARGET_TEMP, MIN_TARGET_TEMP, MAX_PUMP_TEMPERATURE_DELTA, \
    MIN_PUMP_TEMPERATURE_DELTA

MIN_TIMESTAMP = 1617216126
timezone = pytz.timezone(TZ)
MIN_TEMPERATURE = -40
MAX_TEMPERATURE = 40
MAX_SPEED = 500


class MeasurementSchema(BaseModel):
    timestamp: int
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

    @validator('timestamp')
    def validate_timestamp(cls, value):
        if value < MIN_TIMESTAMP or value > datetime.now(tz=timezone).timestamp() + 300:
            raise ValueError('Invalid timestamp')
        return value

    @validator('insideHumidity', 'outsideHumidity')
    def validate_humidity(cls, value):
        if value < 0 or value > 100:
            raise ValueError('Humidity must be between 0 and 100')
        return value

    @validator('insideTemperature', 'outsideTemperature')
    def validate_temperature(cls, value):
        if value < MIN_TEMPERATURE or value > MAX_TEMPERATURE:
            raise ValueError(f"Temperature must be between {MIN_TEMPERATURE} and {MAX_TEMPERATURE}")
        return value

    @validator('speed')
    def validate_speed(cls, value):
        if value < 0 or value > MAX_SPEED:
            raise ValueError(f"Speed must be between 0 and {MAX_SPEED}")
        return value

    @validator('pidKp', 'pidKi', 'pidKd')
    def validate_pid(cls, value):
        if value < 0:
            raise ValueError('PID values cannot be negative')
        return value

    @validator('humidityUpperBoundary')
    def validate_humidity_upper_boundary(cls, value):
        if value < 0 or value > MAX_TARGET_HUMIDITY:
            raise ValueError(f"Upper humidity boundary must be between 0 and {MAX_TARGET_HUMIDITY}")
        return value

    @validator('humidityLowerBoundary')
    def validate_humidity_lower_boundary(cls, value, values):
        if 'humidityUpperBoundary' in values:
            if values['humidityUpperBoundary'] < value or value < 0:
                raise ValueError(f"Lower humidity boundary must be positive and less than the upper boundary")
        return value

    @validator('pumpTemperatureDelta')
    def validate_pump_temperature_delta(cls, value):
        if value < MIN_PUMP_TEMPERATURE_DELTA or value > MAX_PUMP_TEMPERATURE_DELTA:
            raise ValueError(
                "Pump temperature delta has to be between "
                f"{MIN_PUMP_TEMPERATURE_DELTA} and {MAX_PUMP_TEMPERATURE_DELTA}"
            )
        return value

    @validator('targetTemperature')
    def target_temperature_in_interval(cls, value: float):
        if value < MIN_TARGET_TEMP or value > MAX_TARGET_TEMP:
            raise ValueError(f"Target temperature has to be between {MIN_TARGET_TEMP} and {MAX_TARGET_TEMP}")
        return value
