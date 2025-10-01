from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=255)

    class Meta:
        table = "users"


class Document(models.Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()


    class Meta:
        table = "documents"
