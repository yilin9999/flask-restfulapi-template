from utils.ma import ma
from marshmallow import validate
from marshmallow import Schema, fields

class UserSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.Str(required=True, validate=[
                      validate.Length(min=6, max=36)],)
    # email = fields.Email(required=True)
    # password = fields.Str(required=True, validate=[
    #                   validate.Length(min=6, max=36)],)