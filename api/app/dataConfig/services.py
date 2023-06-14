from app.dataConfig.schemas import Config, Temperature, Humidity, TopLevelParams
from fastapi import HTTPException
import json

config: Config


def valid_temperature(temperature: Temperature) -> Temperature | None:
    if temperature.targetTemp < 15 or temperature.targetTemp > 25:
        raise HTTPException(status_code=422, detail='Incorrect target temperature value')
    if temperature.pid.ki < 0 or temperature.pid.kp < 0 or temperature.pid.kd < 0:
        raise HTTPException(status_code=422, detail='PID values cannot be negative')
    if temperature.pump.temperatureDelta < -10 or temperature.pump.temperatureDelta > 10:
        raise HTTPException(status_code=422, detail='Pump temperature delta must be between -10 and 10')
    return temperature


def valid_humidity(humidity: Humidity) -> Humidity | None:
    if humidity.interval.low >= humidity.interval.high:
        raise HTTPException(status_code=422, detail='Left interval value has to be lower than the right one')
    if humidity.interval.low < 0 or humidity.interval.high < 0 or humidity.interval.high > 60:
        raise HTTPException(status_code=422, detail='Incorrect interval values')
    return humidity


def valid_top_level_params(top_level_params: TopLevelParams) -> TopLevelParams | None:
    if top_level_params.sendingInterval <= 0 or top_level_params.sendingInterval > 15:
        raise HTTPException(status_code=422, detail='Incorrect sending interval')
    if top_level_params.grDelta < 0 or top_level_params.grDelta > 15:
        raise HTTPException(status_code=422, detail='Incorrect hysteresis delta value')
    return top_level_params


def init_config() -> None:
    global config
    with open('/code/app/dataConfig/data_config.json', 'r') as f:
        data = json.load(f)
        config = Config(**data)


def save_config_to_file() -> None:
    global config
    with open('/code/app/dataConfig/data_config.json', 'w') as f:
        f.write(config.json())
    print('config written to disk')


def get_config() -> Config:
    return config


def update_temperature(temperature: Temperature) -> Temperature:
    global config
    config.temperature = temperature
    return temperature


def update_humidity(humidity: Humidity) -> Humidity:
    global config
    config.humidity = humidity
    return humidity


def update_top_level_props(top_level_params: TopLevelParams) -> TopLevelParams:
    global config
    config.topLevelParams = top_level_params
    return top_level_params
