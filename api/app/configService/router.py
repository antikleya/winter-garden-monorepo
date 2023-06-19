from fastapi import APIRouter, Depends
from app.dependecies import current_user
from app.configService.schemas import Config, Temperature, Humidity, TopLevelParams
import app.configService.services as services
from fastapi_utils.tasks import repeat_every


configRouter = APIRouter(
    prefix='/config',
    tags=['config'],
    dependencies=[Depends(current_user)]
)


@configRouter.on_event('startup')
def init_config():
    services.init_config()


@configRouter.on_event('shutdown')
def save_config_to_file_on_shutdown():
    services.save_config_to_file()


@configRouter.on_event('startup')
@repeat_every(seconds=60 * 40, wait_first=True)
def save_config_to_file():
    services.save_config_to_file()


@configRouter.get('/', response_model=Config, status_code=200)
def get_config():
    return services.get_config()


@configRouter.patch('/temperature', status_code=200, response_model=Temperature)
def update_temperature(temperature: Temperature):
    return services.update_temperature(temperature)


@configRouter.patch('/humidity', status_code=200, response_model=Humidity)
def update_humidity(humidity: Humidity):
    return services.update_humidity(humidity)


@configRouter.patch('/top', status_code=200, response_model=TopLevelParams)
def update_top_level_props(top_level_params: TopLevelParams):
    return services.update_top_level_props(top_level_params)
