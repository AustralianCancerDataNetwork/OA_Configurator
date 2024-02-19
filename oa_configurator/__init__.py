# grabbing environment variables for path of configuration files - review files .example_dotenv and 
# oa_system_config_demo.yaml to see what items need to be setup in your local environment

from dotenv import load_dotenv
import os

load_dotenv()

message = ""
try:
    os.environ['OA_CONFIG']
except:
    message = 'Please set OA_CONFIG environment variable to allow loading of db configuration details'

# weird way to do this, but necessary if we are to be able to use jupyter - can't handle exiting from
# an exception block for some reason...
if len(message) > 0:
    raise SystemExit(message)

from .config import oa_config, Config, logger

__all__ = [oa_config, Config, logger]