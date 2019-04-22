"""
Copyright 2018 SuperDARN

__init__.py
2018-11-05
Init file to setup the logging configuration and linking pydarn's
module, classes, and functions.
"""
# KEEP THIS FILE AS MINIMAL AS POSSIBLE!

import os
import logging.config
import yaml

# Importing pydarn exception classes
from .exceptions import dmap_exceptions
from .exceptions import superdarn_exceptions

# Importing pydarn pydmap data structure classes
from .io.datastructures import DmapScalar
from .io.datastructures import DmapArray
from .io.datastructures import DmapRecord
from .io import superdarn_formats

# Importing pydarn dmap classes
from .io.dmap import DmapRead
from .io.dmap import DmapWrite

# Importing pydarn superdarn classes
from .io.superdarn import DarnRead
from .io.superdarn import DarnWrite
from .io.superdarn import DarnUtilities

# importing utils
from .utils.conversions import dict2dmap
from .utils.conversions import dmap2dict

# import plotting
from .plotting.superdarn_radars import SuperDARNRadars
from .plotting.rtp import RTP

"""
Pydarn uses yaml for logging configuration because it is the
preferred configuration file format because of its readability.

"""
# real path is needed because path imports from where it is ran and the
# logging config will not be in the users current path.
real_path = os.path.realpath(__file__)
dirname = os.path.dirname(real_path)

# setting the logging configuration.
log_path = dirname + "/logging_config.yaml"
with open(log_path, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
