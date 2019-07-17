#!/bin/sh

env_path=fast_retraining_env
project_path=$(pwd)
conda env create -f environment.yml -p $env_path

activate_script_path=$(readlink -f scripts/activate_env_vars.sh)
deactivate_script_path=$(readlink -f scripts/deactivate_env_vars.sh)

mkdir -p $env_path/etc/conda/activate.d
mkdir -p $env_path/etc/conda/deactivate.d
echo 'source '$activate_script_path >> $env_path/etc/conda/activate.d/env_vars.sh
echo 'source '$deactivate_script_path >> $env_path/etc/conda/deactivate.d/env_vars.sh