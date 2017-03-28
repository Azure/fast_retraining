# Fast Retraining

This repo shows how to perform fast retraining with LightGBM in different business cases.

## Project

In the folder [experiments](./experiments) you can find the different experiments of the project.

In the folder [experiment/libs](./experiment/libs) there is the common code for the project.

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


### Setup
Instruction for setting up on a Linux Microsoft DSVM

Clone this repo to your desired location
```bash
git clone https://github.com/Azure/fast_retraining.git
```

Create a conda environment if you haven't already done so. The command below creates a python 3 environment called sbsa.
```bash
conda create --name strata python=3 anaconda
```


Edit [activate_env_vars.sh](environment/activate_env_vars.sh ) and [deactivate_env_vars.sh](environment/deactivate_env_vars.sh )
so that they contain the correct information.

Install command line jason parser
```bash
apt-get install jq
```

Activate the conda environment
```bash
source activate strata
```

Get the currently activated environment and assign it to env_path.
Get info of current env and output to json | look for default_prefix element in JSON | remove all quotes
```bash
env_path=$(conda info --json | jq '.default_prefix' | tr -d '"')
```

Make sure you are in the environemnt folder of the project and run the following
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
source activate strata
```

