from pydantic import BaseModel


class Dog(BaseModel):
    id: str | None = None
    name: str
    age: int
    breed: str
    owner_name: str

    class Config:
        orm_mode = True
        from_attributes = True