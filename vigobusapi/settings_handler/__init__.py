"""SETTINGS HANDLER
Declaration of the Settings class and instance that can be used to get any setting required,
using dotenv-settings-handler and python-dotenv.
"""

# # Native # #
from typing import Optional

# # Installed # #
# noinspection PyPackageRequirements
from dotenv import load_dotenv
from dotenv_settings_handler import BaseSettingsHandler

__all__ = ("settings",)

load_dotenv()


class Settings(BaseSettingsHandler):
    html_remote_api: str
    wsdl_remote_api: str
    endpoint_timeout = 30
    http_timeout = 5
    wsdl_timeout = 10
    http_retries = 2
    stops_cache_maxsize = 500
    stops_cache_ttl = 3600
    buses_cache_maxsize = 300
    buses_cache_ttl = 15
    mongo_uri = "mongodb://localhost:27017"
    mongo_stops_db = "vigobusapi"
    mongo_stops_collection = "stops"
    api_host = "0.0.0.0"
    api_port = 5000
    api_name = "VigoBusAPI"
    api_version = "0.0.1"
    api_log_level = "info"
    api_description: Optional[str]


settings = Settings()
