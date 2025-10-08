from tortoise import fields
from tortoise.models import Model


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)


class MyAbstractBaseModel(Model):
    id = fields.UUIDField(primary_key=True)

    class Meta:
        abstract = True


class Chat(TimestampMixin, MyAbstractBaseModel):
    name = fields.CharField(20, null=True)
