# grabbing environment variables for path of configuration files - review files .example_dotenv and 
# oa_system_config_demo.yaml to see what items need to be setup in your local environment

from dotenv import load_dotenv
import os
from nbconvert.preprocessors import CellExecutionError
from IPython import get_ipython

load_dotenv()

try:
    os.environ['OA_CONFIG']
except Exception as e:
    message = 'Please set OA_CONFIG environment variable to allow loading of db configuration details'
    shell = get_ipython().__class__.__name__
    if shell == 'ZMQInteractiveShell':
    # check if execution was done on Jupyter notebook or terminal
        raise CellExecutionError(None, e.args[0], message)
        # raise custom exception to replace the original exception type KeyError
        # this error type deal with failures on jupyter notebook execution
        # by halting cell execution without causing kernel crash
    else:
        raise SystemExit(message)

from .config import oa_config, Config, logger

__all__ = [oa_config, Config, logger]