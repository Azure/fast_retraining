#!/bin/sh

# The location of the repository on the host machine
export PROJECTPATH=$(pwd)

# Add custom libraries to the python path
export OLD_PYTHON_PATH=$PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$PROJECTPATH # Adds the repository to the python path

# Add scripts to path
export OLD_PATH=$PATH
export PATH=$PATH:PROJECTPATH

# The mounting location for the data
source ${PROJECTPATH}/.env             
echo Me Gusta!
