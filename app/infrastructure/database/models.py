
from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field

class MongoDBProductModel(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    product_id: str
    name: str
    description: str
    price: float
    stock: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
    