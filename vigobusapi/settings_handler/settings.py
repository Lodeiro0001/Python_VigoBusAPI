"""SETTINGS
Settings loader. Load the DotEnv file and provide a function to return all the available settings as a Dict.
"""

# # Native # #
from typing import Dict, Optional
from os import getenv

# # Installed # #
# noinspection PyPackageRequirements
from dotenv import load_dotenv

# # Package # #
from .const import *


def load_settings(dotenv_location: Optional[str] = None) -> Dict:
    if dotenv_location is None:
        dotenv_location = getenv(DOTENV_LOCATION)

    load_dotenv(dotenv_path=dotenv_location)

    return {
        ENDPOINT_TIMEOUT: float(getenv(ENDPOINT_TIMEOUT, DEFAULT_ENDPOINT_TIMEOUT)),
        API_HOST: getenv(API_HOST, DEFAULT_API_HOST),
        API_PORT: int(getenv(API_PORT, DEFAULT_API_PORT)),
        API_NAME: getenv(API_NAME, DEFAULT_API_NAME),
        API_DESCRIPTION: getenv(API_DESCRIPTION),
        API_VERSION: getenv(API_VERSION, DEFAULT_API_VERSION),
        API_LOG_LEVEL: getenv(API_LOG_LEVEL, DEFAULT_API_LOG_LEVEL),
        HTTP_REMOTE_API: getenv(HTTP_REMOTE_API),
        WSDL_REMOTE_API: getenv(WSDL_REMOTE_API),
        HTTP_TIMEOUT: float(getenv(HTTP_TIMEOUT, DEFAULT_HTTP_TIMEOUT)),
        WSDL_TIMEOUT: float(getenv(WSDL_TIMEOUT, DEFAULT_WSDL_TIMEOUT)),
        HTTP_RETRIES: int(getenv(HTTP_RETRIES, DEFAULT_HTTP_RETRIES)),
        STOPS_CACHE_MAXSIZE: int(getenv(STOPS_CACHE_MAXSIZE, DEFAULT_STOPS_CACHE_MAXSIZE)),
        STOPS_CACHE_TTL: float(getenv(STOPS_CACHE_TTL, DEFAULT_STOPS_CACHE_TTL)),
        BUSES_CACHE_MAXSIZE: int(getenv(BUSES_CACHE_MAXSIZE, DEFAULT_BUSES_CACHE_MAXSIZE)),
        BUSES_CACHE_TTL: float(getenv(BUSES_CACHE_TTL, DEFAULT_BUSES_CACHE_TTL)),
        MONGO_URI: getenv(MONGO_URI, DEFAULT_MONGO_URI),
        MONGO_STOPS_DB: getenv(MONGO_STOPS_DB, DEFAULT_MONGO_STOPS_DB),
        MONGO_STOPS_COLLECTION: getenv(MONGO_STOPS_COLLECTION, DEFAULT_MONGO_STOPS_COLLECTION),
    }
