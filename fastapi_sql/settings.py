TORTOISE_ORM = {
    "connections": {
        "models": {
            "engine": "tortoise.backends.sqlite",
            "credentials": {
                "journal_mode": "WAL",
                "journal_size_limit": 16384,
                "file_path": "data/alex.db",
            },
        }
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "models",
        }
    },
}

OWN_MODEL_URL = "http://localhost:5000"
GEMINI_URL = "http://localhost:6000"
