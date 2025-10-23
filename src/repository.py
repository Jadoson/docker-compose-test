from fastapi import Depends
from sqlalchemy import insert, select

from database import get_session
from schemas import Dog as DogSchema
from models import Dog as DatabaseDog


class DogRepository:
    def __init__(self, database_session):
        self.database_session = database_session

    async def create_dog(self, data: DogSchema):
        dog_as_dict = data.model_dump(exclude_none=True)
        insert_stmt = insert(DatabaseDog).values(**dog_as_dict)
        await self.database_session.execute(insert_stmt)
        await self.database_session.commit()


    async def get_dog_by_id(self, dog_id: str) -> DogSchema | None:
        dog_stmt = select(DatabaseDog).where(DatabaseDog.id == dog_id)
        dog_data = await self.database_session.execute(
            dog_stmt
        )
        dog = dog_data.scalars().one_or_none()
        if dog is None:
            return None

        validated_dog = DogSchema.model_validate(dog)
        return validated_dog


async def get_dog_repository(db_session = Depends(get_session)):
    return DogRepository(db_session)