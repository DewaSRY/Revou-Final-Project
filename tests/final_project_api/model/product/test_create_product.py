"""_summary_
"""

from tests.mock_database_connection import MockDatabaseConnection

from app.final_project_api.model.user import UserModel
from app.final_project_api.model.business import BusinessModel, BusinessTypeModel
from app.final_project_api.model.product import ProductModel, ProductImageModel
from pprint import pprint
from unittest import skip
from uuid import uuid4


class TestCreateProduct(MockDatabaseConnection):

    def setup_class(self):
        super().setup_class(self)
        self.product_name = "some product name"
        self.product_price = 1_000
        self.product_description = "some description"

    def setUp(self) -> None:
        self.user_create = UserModel.add_model(
            username="business user name",
            email="business@email.com",
            password="some password",
        )
        self.business_type = BusinessTypeModel.add_model(name="business type")
        self.business = BusinessModel.add_model(
            user_id=self.user_create.id,
            business_name="some business name",
            business_type_name=self.business_type.name,
            description="some business description ",
        )

    def tearDown(self) -> None:
        UserModel.clean_all_model()
        BusinessTypeModel.clean_all_model()
        BusinessModel.clean_all_model()
        ProductImageModel.clean_all_model()
        ProductModel.clean_all_model()

    def test_create_product_image(self):
        first_url = "first ulr"
        second_url = "second ulr"
        create_product = ProductModel.add_model(
            business_id=self.business.id,
            product_name=self.product_name,
            product_price=self.product_price,
            description=self.product_description,
        )
        default_profile_url = create_product.profile_url
        ProductImageModel.add_model(
            public_id=str(uuid4()), secure_url=first_url, product_id=create_product.id
        )
        profile_url_after_first_image = create_product.profile_url
        ProductImageModel.add_model(
            public_id=str(uuid4()), secure_url=second_url, product_id=create_product.id
        )
        profile_url_after_second_image = create_product.profile_url
        assert default_profile_url == ""
        assert profile_url_after_first_image == first_url
        assert profile_url_after_second_image == first_url

    # @skip("just skip")
    def test_create_product(self):
        create_product = ProductModel.add_model(
            business_id=self.business.id,
            product_name=self.product_name,
            product_price=self.product_price,
            description=self.product_description,
        )
        assert create_product.product_price == self.product_price
        assert create_product.product_name == self.product_name
        assert create_product.business_id == self.business.id

    def test_create_product_ten(self):
        for _ in range(10):
            create_product = ProductModel.add_model(
                business_id=self.business.id,
                product_name=self.product_name,
                product_price=self.product_price,
                description=self.product_description,
            )
        modelList = ProductModel.get_all_model()
        assert len(modelList) == 10

    def test_get_public_model(self):
        for _ in range(100):
            create_product = ProductModel.add_model(
                business_id=self.business.id,
                product_name=self.product_name,
                product_price=self.product_price,
                description=self.product_description,
            )
        modelList = ProductModel.get_all_public_model()
        assert len(modelList) == 10
