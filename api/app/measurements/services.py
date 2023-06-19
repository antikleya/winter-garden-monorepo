from typing import List
from app.measurements.schemas import MeasurementSchema
from sqlalchemy.orm import Session
from app.measurements.models import Measurement


def get_measurements(start: int, end: int, db: Session) -> List[MeasurementSchema]:
    measurements = db\
        .query(Measurement)\
        .filter(Measurement.timestamp >= start, Measurement.timestamp <= end)\
        .order_by(Measurement.timestamp)\
        .all()
    return [MeasurementSchema.from_orm(measurement) for measurement in measurements]


def create_measurement(measurement: MeasurementSchema, db: Session) -> MeasurementSchema:
    measurement_model = Measurement(**measurement.dict())

    db.add(measurement_model)
    db.commit()
    db.refresh(measurement_model)

    return MeasurementSchema.from_orm(measurement_model)