
from app.application.services.product_service import ProductService
from app.domain.entities.product import Product
from unittest.mock import Mock

mock_repository = Mock()
product_service = ProductService(mock_repository)

def test_create_product_service():
    product = Product(
        product_id="123",
        name="Test",
        description="Description",
        price=10.0,
        stock=5
    )
    mock_repository.create_product.return_value = product
    result = product_service.create_product(product)
    assert result.name == "Test"

def test_get_all_products_service():
    mock_repository.get_all_products.return_value = []
    result = product_service.get_all_products()
    assert isinstance(result, list)

def test_get_product_by_id_service():
    mock_repository.get_product_by_id.return_value = None
    result = product_service.get_product_by_id("123")
    assert result is None
