import sys
import json
import logging

from lib import osutils
from lib import osinit
from lib import osauth
from lib import osmetrics

NR_OSMON_VERSION = '1.0.6'

# ==========================================
# -----------------------------------------------------------
# -----------------------------------------------------------
# main logic
init = osinit.OpenStackInit()
config = init.getConfig()
logger = osutils.setLogging(config)
logger.log(logging.WARNING, ">>> Starting NR Openstack Monitor %s", NR_OSMON_VERSION)
# logger.log(logging.DEBUG, ">> config: %s", config) # contains user creds

init.prepareEnvironment()
file_handles = init.getFileHandles()
logger.log(logging.DEBUG, ">> file handles: %s", file_handles)
osAuth = osauth.OpenStackAuth(config, init.getServiceTypes())
metrics = osmetrics.ProcessMetrics(osAuth, config, file_handles, init.serviceType)

metrics.getProjectMetrics()

metrics.getSystemMetrics()

metrics.close_output_files()

logger.log(logging.WARNING, ">>> Terminating NR Openstack Monitor")

#################################################################
#################################################################
