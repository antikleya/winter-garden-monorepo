from typing import List
from app.measurements.schemas import MeasurementSchema
from fastapi import APIRouter, Depends
from app.database import get_sync_session
from sqlalchemy.orm import Session
import app.measurements.services as services
from app.dependencies import current_user
from app.measurements.dependencies import authorized_source


measurementsRouter = APIRouter(
    prefix='/measurements',
    tags=['measurements']
)


@measurementsRouter.get('/', response_model=List[MeasurementSchema], dependencies=[Depends(current_user)])
def get_measurements(
        start: int,
        end: int,
        db: Session = Depends(get_sync_session)
):
    return services.get_measurements(start=start, end=end, db=db)


@measurementsRouter.post('/', response_model=MeasurementSchema, dependencies=[Depends(authorized_source)])
def create_measurement(measurement: MeasurementSchema, db: Session = Depends(get_sync_session)):
    return services.create_measurement(measurement=measurement, db=db)
