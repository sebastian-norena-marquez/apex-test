from typing import List, Optional
from pymongo.collection import Collection
from app.application.ports.output_port import ProductRepositoryPort
from app.domain.entities.product import Product
from app.infrastructure.database.models import MongoDBProductModel


class MongoDBProductRepository(ProductRepositoryPort):
    """Repositorio para gestionar productos en MongoDB."""

    def __init__(self, collection: Collection):
        self.collection = collection

    def create_product(self, product: Product) -> Product:
        try:
            # Convertir de Product a MongoDBProductModel
            model = MongoDBProductModel(**product.dict())
            self.collection.insert_one(model.dict(by_alias=True))
            return product
        except Exception as e:
            raise ValueError(f"Error inserting product into MongoDB: {e}")


    def get_all_products(self) -> List[Product]:
        """Obtiene todos los productos."""
        products = self.collection.find()
        return [Product(**MongoDBProductModel(**product).dict()) for product in products]

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """Obtiene un producto por su ID."""
        product = self.collection.find_one({"product_id": product_id})
        if product:
            model = MongoDBProductModel(**product)
            return Product(**model.dict())
        return None

    def update_product(self, product_id: str, product_data: dict) -> Optional[Product]:
        """Actualiza un producto existente."""
        result = self.collection.find_one_and_update(
            {"product_id": product_id},
            {"$set": product_data},
            return_document=True,
        )
        if result:
            model = MongoDBProductModel(**result)
            return Product(**model.dict())
        return None

    def delete_product(self, product_id: str) -> bool:
        """Elimina un producto por su ID."""
        result = self.collection.delete_one({"product_id": product_id})
        return result.deleted_count > 0
