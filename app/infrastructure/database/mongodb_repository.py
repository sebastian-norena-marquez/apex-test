
from typing import List, Optional
from pymongo.collection import Collection
from app.domain.entities.product import Product
from pymongo.errors import PyMongoError

class MongoDBProductRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def create_product(self, product: Product) -> Product:
        try:
            self.collection.insert_one(product.dict(by_alias=True))
            return product
        except PyMongoError as e:
                raise RuntimeError(f"Error creating product: {e}")

    def get_all_products(self) -> List[Product]:
        try:
            products = self.collection.find()
            return [Product(**product) for product in products]
        except PyMongoError as e:
            raise RuntimeError(f"Error retrieving products: {e}")

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        try:
            product = self.collection.find_one({"product_id": product_id})
            return Product(**product) if product else None
        except PyMongoError as e:
            raise RuntimeError(f"Error retrieving product by ID: {e}")

    def update_product(self, product_id: str, product_data: dict) -> Optional[Product]:
        try:
            result = self.collection.find_one_and_update(
                {"product_id": product_id},
                {"$set": product_data},
                return_document=True
            )
            return Product(**result) if result else None
        except PyMongoError as e:
                raise RuntimeError(f"Error update product:  {e}")

    def delete_product(self, product_id: str) -> bool:
        try:
            result = self.collection.delete_one({"product_id": product_id})
            return result.deleted_count > 0
        except PyMongoError as e:
                raise RuntimeError(f"Error delete product:  {e}")
    