from app.configService.schemas import Config, Temperature, Humidity, TopLevelParams
import json

config: Config


def init_config() -> None:
    global config
    with open('/code/app/configService/data_config.json', 'r') as f:
        data = json.load(f)
        config = Config(**data)


def save_config_to_file() -> None:
    global config
    with open('/code/app/configService/data_config.json', 'w') as f:
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
