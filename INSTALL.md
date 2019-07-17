# Installation and Setup

Here we present the instructions for setting up the project on an [Ubuntu Azure VM](https://azure.microsoft.com/en-us/services/virtual-machines/). The VM we used for the experiment was a NV24 with 4 NVIDIA M60 GPUs. The OS was Ubuntu 16.04. We recommend to use the [Azure Data Science VM](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoft-ads.standard-data-science-vm) which comes with many machine learning tools already installed.

## Setting up the environment 

Clone this repo to your desired location
```bash
git clone https://github.com/Azure/fast_retraining.git
```

Next you need to take the .env_template file, edit it and save it as .env. This simply contains the location of where you would like the data to be downloaded to.

 By running the following commands a script is executed that creates the Python 3.6 environment with the required dependecies but also sets up the environment variables.
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

To enter the environment run
```bash
conda activate ./fast_retraining_env
```

To register the environment in the jupyter notebook:
```bash
python -m ipykernel install --user --name fast --display-name "Python Fast"
```

Then from inside the environment to start the Jupyter server
```bash
jupyter notebook --no-browser
```

If you need to specify a different port and accept connections from any location
```bash
jupyter notebook --ip=0.0.0.0 --port=9999 --no-browser
```

Exit the environment
```bash
conda deactivate
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
