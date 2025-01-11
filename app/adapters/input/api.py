
from fastapi import APIRouter, HTTPException
from typing import List
from app.domain.entities.product import Product
from app.application.services.product_service import ProductService
from app.infrastructure.database.database import db
from app.infrastructure.database.mongodb_repository import MongoDBProductRepository

router = APIRouter()

# Centralized MongoDB connection via database.py
collection = db["products"]
repository = MongoDBProductRepository(collection)
service = ProductService(repository)

@router.post("/products", response_model=Product)
async def create_product(product: Product):
    try:
        return service.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/products", response_model=List[Product])
async def get_all_products():
    return service.get_all_products()

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: str, product_data: dict):
    if not product_data:
        raise HTTPException(status_code=400, detail="At least one field must be provided for update.")
    
    product = service.update_product(product_id, product_data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/products/{product_id}")
async def delete_product(product_id: str):
    if not service.delete_product(product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}
    