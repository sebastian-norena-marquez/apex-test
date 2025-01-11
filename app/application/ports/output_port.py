from typing import List, Optional
from app.domain.entities.product import Product

class ProductRepositoryPort:
    def create_product(self, product: Product) -> Product:
        pass

    def get_all_products(self) -> List[Product]:
        pass

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        pass

    def update_product(self, product_id: str, product_data: dict) -> Optional[Product]:
        pass

    def delete_product(self, product_id: str) -> bool:
        pass
