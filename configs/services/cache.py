import os

from App.helpers import env
from config import CACHE_PATH, STATIC_APP_NAME

__CONFIG__ = {
    # Driver for cache accessible
    # Drivers: file, memory, redis
    "default": env("CACHE_DRIVER", "file"),

    "drivers": {
        "file": {
            # Path of cache storage
            "path": os.path.join(CACHE_PATH, "storage.cache"),
        },
        "redis": {
            "host": env("REDIS_HOST", "localhost"),
            "port": env("REDIS_PORT", 6379),
            "password": env("REDIS_PASSWORD"),
        },
    },

    # Prefix for database based cache services
    "prefix": env("CACHE_PREFIX", STATIC_APP_NAME).replace("-", "_") + "_cache_",
}
