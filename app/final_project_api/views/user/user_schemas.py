"""_summary_
"""

from marshmallow import Schema, fields, post_load
from app.final_project_api.views.business.business_schemas import BusinessSchemas
from app.final_project_api.views.product.product_schemas import ProductSchema

from .user_data import AuthData, UserUpdateData


class LoginSchemas(Schema):
    __name__ = "user base schemas"
    username = fields.String()
    password = fields.String(required=True)
    email = fields.Email()

    @post_load
    def get_data_login(self, data, **kwargs):
        return AuthData(**data)


class RegisterSchema(Schema):
    """payload to create schemas"""

    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)

    @post_load
    def get_data_register(self, data, **kwargs):
        return AuthData(**data)


class UserUpdateSchema(Schema):
    phone_number = fields.Str()
    address = fields.Str()
    occupation = fields.Str()
    description = fields.Str()
    username = fields.Str()
    email = fields.Str()

    @post_load
    def get_data_register(self, data, **kwargs):
        return UserUpdateData(**data)


class UserModelSchema(RegisterSchema):
    """schemas to response user schemas"""

    user_id = fields.Str()
    create_at = fields.DateTime()
    update_at = fields.DateTime()
    access_token = fields.Str()

    phone_number = fields.Str()
    address = fields.Str()
    occupation = fields.Str()
    description = fields.Str()

    email = fields.Email()
    username = fields.Str()
    user_type = fields.Str()
    profile_url = fields.Str()
    images = fields.List(fields.Str)
    product_amount = fields.Integer()
    business_amount = fields.Integer()
    business = fields.List(fields.Nested(BusinessSchemas), dump_only=True)
    product = fields.List(fields.Nested(ProductSchema), dump_only=True)
