from fastapi import HTTPException, Depends, APIRouter
from FastApiCourse.db.models import Network
from FastApiCourse.db.schema import NetworkSchema
from FastApiCourse.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

network_router = APIRouter(prefix='/network', tags=['Network'])

@network_router.post('/', response_model=dict)
async def create_network(network: NetworkSchema, db: Session = Depends(get_db)):
    network_db = Network(**network.dict())
    db.add(network_db)
    db.commit()
    db.refresh(network_db)
    return {'message': 'Saved'}


@network_router.delete('/{network_id}/')
async def delete_lesson( network_id: int, db: Session = Depends(get_db)):
    network_db = db.query(Network).filter(Network.id == network_id).first()
    if network_db is None:
        raise HTTPException(status_code=401, detail='Андай маалымат жок')
    db.delete(network_db)
    db.commit()
    return {'message': 'Deleted'}
