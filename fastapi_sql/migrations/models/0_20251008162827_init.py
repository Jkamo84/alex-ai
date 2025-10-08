from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "documents" (
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "content" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "users" (
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "password_hash" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
