from tortoise import fields, models


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)


class MyAbstractBaseModel(models.Model):
    id = fields.UUIDField(primary_key=True)

    class Meta:
        abstract = True


class User(TimestampMixin, MyAbstractBaseModel):
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=255)

    class Meta:
        table = "users"


class Document(TimestampMixin, MyAbstractBaseModel):
    content = fields.TextField()

    class Meta:
        table = "documents"
