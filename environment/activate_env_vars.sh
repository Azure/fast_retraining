#!/bin/sh

# The location of the repository on the host machine
REPOSPATH=$HOME'/repos/'
export PROJECTPATH=$REPOSPATH'fast_retraining'


# Add custom libraries to the python path
export OLD_PYTHON_PATH=$PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$PROJECTPATH'/experiments' # Adds the repository to the python path

# Add scripts to path
export OLD_PATH=$PATH
export PATH=$PATH:PROJECTPATH

export MOUNT_POINT=/fileshare               # The mounting location for the data
export CACHE_DIR=$MOUNT_POINT'/cache'
export STORAGE_URI=//migonzadldsvm2storage.file.core.windows.net/strata-fileshare

echo Me Gusta!
