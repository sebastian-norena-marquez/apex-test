from datetime import datetime, timezone
from pydantic import BaseModel, Field
from bson import ObjectId

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    product_id: str
    name: str
    description: str
    price: float
    stock: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
