from typing import List, Optional
from app.domain.entities.product import Product
from app.application.ports.output_port import ProductRepositoryPort

class ProductService:
    def __init__(self, repository: ProductRepositoryPort):
        self.repository = repository

    def create_product(self, product: Product) -> Product:
        return self.repository.create_product(product)

    def get_all_products(self) -> List[Product]:
        return self.repository.get_all_products()

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        return self.repository.get_product_by_id(product_id)

    def update_product(self, product_id: str, product_data: dict) -> Optional[Product]:
        return self.repository.update_product(product_id, product_data)

    def delete_product(self, product_id: str) -> bool:
        return self.repository.delete_product(product_id)
