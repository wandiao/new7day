from rest_framework.schemas import AutoSchema
import coreapi

def DocParam(
  name="default",
  location="query",
  required=False,
  description=None,
  type="string"):
  return coreapi.Field(
    name=name,
    location=location,
    required=required,
    description=description,
    type=type
  )

def auto_schema(fields):
  return AutoSchema(
    manual_fields = fields
  )
  