import os
import pathlib
import sys
from os.path import dirname, abspath

ROOT = dirname(abspath(__file__))
CWD = ROOT
HOME = pathlib.Path.home()
BUILD_TYPE = None
EXECUTABLE = sys.executable
EXECUTABLE_DIR = os.path.dirname(EXECUTABLE)

if getattr(sys, 'frozen', False):
    CWD = EXECUTABLE_DIR
    BUILD_TYPE = "@BUILD_TYPE@"

RCL_PROTOCOL_VERSION = 1

# Versions
VERSION_MAJOR = "0"
VERSION_MINOR = "0"
VERSION_PATH = "0"
VERSION_BRANCH = "Alpha"
VERSION_NUMBER = "0"
VERSION_SHOW = "2024.0 (Alpha 2)"
VERSION_BUILD_DATE = "2024-10-03"
VERSION_DETAILED = f'{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATH} ({VERSION_NUMBER}) {VERSION_BRANCH}'

# StaticData
STATIC_APP_NAME = "MFU Server"
STATIC_LICENSE_NAME = "GNU GPL V3"
STATIC_LICENSE_URL = "https://github.com/mfu-utils/server/blob/master/LICENSE"
STATIC_REPO_NAME = "Github"
STATIC_REPO_URL = "https://github.com/mfu-utils/server"

# Settings files
ENV_NAME = '.env'

# Var paths
VAR = os.path.join(CWD, "var")
ENV_PATH = os.path.join(VAR, ENV_NAME)
CACHE_PATH = os.path.join(VAR, "cache")
SQLITE_PATH = os.path.join(VAR, "db")
LOGS_PATH = os.path.join(VAR, "logs")

# Configs parameters
CONFIGS_PATH = os.path.join(ROOT, "configs")

# Config files
CONFIG_FILES_METADATA = os.path.join(CONFIGS_PATH, "metadata.yml")
CONFIG_FILE_SERVICES = os.path.join(CONFIGS_PATH, "container.yml")

# Models
DB_MODELS_NAMESPACES = [
    # f"App.Models",
]

# Controllers paths
CONTROLLERS_NAMESPACES = {
    'App.Controllers',
}

# Console commands
COMMANDS_NAMESPACES = {
    'App.Commands',
}

# Assets paths
ASSETS = os.path.join(ROOT, "assets")

ICONS_PATH = os.path.join(ASSETS, "icons")
STYPES_PATH = os.path.join(ASSETS, "styles")
LANGS_DIR = os.path.join(ASSETS, "langs")
