# Installation and Setup

Here we present the instructions for setting up the project on an [Ubuntu Azure VM](https://azure.microsoft.com/en-us/services/virtual-machines/). The VM we used for the experiment was a NV24 with 4 NVIDIA M60 GPUs. The OS was Ubuntu 16.04. We recommend to use the [Azure Data Science VM](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoft-ads.standard-data-science-vm) which comes with many machine learning tools already installed.

## Setting up the environment 

Clone this repo to your desired location
```bash
git clone https://github.com/Azure/fast_retraining.git
```

Create a conda environment if you haven't already done so. The command below creates a python 3 environment called fast.
```bash
conda create --name fast python=3.5 anaconda
```

Edit [activate_env_vars.sh](environment/activate_env_vars.sh ) and [deactivate_env_vars.sh](environment/deactivate_env_vars.sh )
so that they contain the correct information.

Install command line json parser
```bash
apt-get install jq
```

Activate the conda environment and install the requirements.
```bash
source activate fast
pip install -r requirements.txt
```

Get the currently activated environment and assign it to env_path.
Get info of current env and output to json | look for default_prefix element in JSON | remove all quotes
```bash
env_path=$(conda info --json | jq '.default_prefix' | tr -d '"')
```

Make sure you are in the environment folder of the project and run the following
```bash
activate_script_path=$(readlink -f activate_env_vars.sh)
deactivate_script_path=$(readlink -f deactivate_env_vars.sh)
```

Then we create the activation and deactivation scripts and make sure they point to our now modified activation 
and deactivation scripts in our environment folder
```bash
mkdir -p $env_path/etc/conda/activate.d
mkdir -p $env_path/etc/conda/deactivate.d
echo 'source '$activate_script_path >> $env_path/etc/conda/activate.d/env_vars.sh
echo 'source '$deactivate_script_path >> $env_path/etc/conda/deactivate.d/env_vars.sh
```

Exit the environment
```bash
source deactivate
```

Enter the environment again
```bash
source activate fast
```

Finally, to register the environment in the jupyter notebook:
```bash
python -m ipykernel install --user --name fast --display-name "Python Fast"
```

## Installation of boosted tree libraries

We need to install [XGBoost](https://github.com/dmlc/xgboost) and [LightGBM](https://github.com/microsoft/LightGBM). Even though both libraries have pypi versions, for creating the experiments contained in this repo we compiled from source.

To install XGBoost you can follow the [installation guide](https://xgboost.readthedocs.io/en/latest/build.html). To build in CPU, using the specific commit we used:

    git clone --recursive https://github.com/dmlc/xgboost
    cd xgboost
    git checkout 6776292951565c8cd72e69afd9d94de1474f00c0
    git submodule update --recursive
    make -j$(nproc)

In case you want to use the last version, just skip the commands `git checkout` and `git submodule`.

If you want to build in GPU, the instructions are [here](https://github.com/dmlc/xgboost/tree/master/plugin/updater_gpu). You first need to download and unzip [CUB 1.6.4](https://nvlabs.github.io/cub/).

    git clone --recursive https://github.com/dmlc/xgboost
    cd xgboost
    git checkout 6776292951565c8cd72e69afd9d94de1474f00c0
    git submodule update --recursive
    mkdir build
    cd build
    cmake .. -DPLUGIN_UPDATER_GPU=ON -DCUB_DIRECTORY=/path/to/cub-1.6.4
    make -j$(nproc)

To install LighGBM you can follow the [installation guide](https://github.com/Microsoft/LightGBM/wiki/Installation-Guide). To build on CPU:

    git clone --recursive https://github.com/Microsoft/LightGBM ; cd LightGBM
    git checkout 73968a96829e212b333c88cd44725c8c39c03ad1
    mkdir build ; cd build
    cmake ..
    make -j$(nproc)

To install the GPU version:

    git clone --recursive https://github.com/Microsoft/LightGBM ; cd LightGBM
    git checkout 73968a96829e212b333c88cd44725c8c39c03ad1
    mkdir build ; cd build
    cmake .. -DUSE_GPU=1
    make -j$(nproc)

To install the python biddings you have to compile in the python directory. Both libraries have the exact same name for the python package, so you just need to do the following step in both libraries:

    cd python-package
    python setup.py install

Finally, to check that the libraries are correctly installed, try to load them from python:

    python -c "import xgboost; import lightgbm"


## Installation of bokeh functionality to export plots

To generate png exports with bokeh you have to follow the instructions explained in [this link](http://bokeh.pydata.org/en/0.12.6/docs/user_guide/export.html).

    sudo apt-get install npm
    sudo npm install -g phantomjs-prebuilt
