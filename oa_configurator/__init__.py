# grabbing environment variables for path of configuration files - review files .example_dotenv and 
# oa_system_config_demo.yaml to see what items need to be setup in your local environment

from dotenv import load_dotenv
import os, sys
from nbconvert.preprocessors import CellExecutionError

load_dotenv()

message = ""
try:
    os.environ['OA_CONFIG']
except:
    message = 'Please set OA_CONFIG environment variable to allow loading of db configuration details'
    t, v, tb = sys.exc_info() # store tuple of exception type, value, and trackback object memory address
    raise CellExecutionError(None, v, message)
    # raise custom exception to replace the original exception type KeyError
    # this error type deal with failures on jupyter notebook execution
    # by halting cell execution without causing kernel crash

from .config import oa_config, Config, logger

__all__ = [oa_config, Config, logger]