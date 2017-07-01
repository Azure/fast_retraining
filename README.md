# Fast Retraining

This repo shows how to perform fast retraining with LightGBM in different business cases.

In this repo we show we compare two of the fastest boosted decision tree libraries: [XGBoost](https://github.com/dmlc/xgboost) and [LightGBM](https://github.com/microsoft/LightGBM). We will evaluate them across datasets of several domains and different sizes. 

## Installation and Setup

The installation instructions can be found [here](./INSTALL.md).

## Project

In the folder [experiments](./experiments) you can find the different experiments of the project. We developed 5 experiments with the CPU versions of the libraries and 2 experiments with the GPU version.

* Airline
* BCI
* Football
* Planet Amazon
* Fraud Detection
* Airline (GPU version)
* HIGGS (GPU version)

In the folder [experiment/libs](./experiment/libs) there is the common code for the project.

## Benchmark

In the following table there are sumarized the time results of the benckmarks performed in the experiments:

| Dataset | Experiment | Data size | Features | time xgb | time xgb_hist | time lgb | 
| --- | :---: | :---: | :---: | :---: | :---: | :---: | 
| Airline | [link](./experiments/01_airline.ipynb) | 115069017 | 13 | 2180 | 578 | 366 | 
| Airline (GPU) | [link](./experiments/01_airline_GPU.ipynb) | 115069017 | 13 | 65.04 | 27.15 | 21.35 | 
| BCI | [link](./experiments/02_BCI.ipynb) | 20497 | 2048 | 15.97 | 52.69 | 6.38 |
| BCI (GPU) | [link](./experiments/02_BCI_GPU.ipynb) | 20497 | 2048 | 12.93 | 42.69 | 2.76 |  
| Football | [link](./experiments/03_football.ipynb) | 19673 | 46 | 2.27 | 2.47 | 0.582 | 
| Football (GPU) | [link](./experiments/03_football_GPU.ipynb) | 19673 | 46 | 7.09 | 4.58 | 0.97 | 
| Planet Amazon | [link](./experiments/04_PlanetKaggle.ipynb) | 40479 | 2048 | 306.51 | 1990.16 | 204.21 | 
| Planet Amazon (GPU) | [link](./experiments/04_PlanetKaggle_GPU.ipynb) | 40479 | 2048 | - | 2028.43 | 317.68 | 
| Fraud Detection | [link](./experiments/05_FraudDetection.ipynb) | 284807 | 30 | 4.45 | 1.20 | 0.73 |
| Fraud Detection (GPU) | [link](./experiments/05_FraudDetection_GPU.ipynb) | 284807 | 30 | 5.80 | 1.64 | 0.29 |
| HIGGS | [link](./experiments/06_HIGGS.ipynb) | 11000000 | 28 | 336.80 | 102.01 | 77.36 |  
| HIGGS (GPU) | [link](./experiments/06_HIGGS_GPU.ipynb) | 11000000 | 28 | - | 79.26 | 55.90 | 

In the next table we summarize the performance results.

| Dataset | Experiment | Data size | Features | F1 xgb | F1 xgb_hist | F1 lgb | 
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Airline | [link](./experiments/01_airline.ipynb) | 115069017 | 13 | 0.698 | 0.717 | 0.694 |
| BCI | [link](./experiments/02_BCI.ipynb) | 20497 | 2048 | 0. | 0. |  |
| Football | [link](./experiments/03_football.ipynb) | 19673 | 46 | 0. |  |  |
| Planet Amazon | [link](./experiments/04_PlanetKaggle.ipynb) | 40479 | 2048 | 0. | 0. | 0. |
| Fraud Detection | [link](./experiments/05_FraudDetection.ipynb) | 284807 | 30 | 0. | 0. | 0. |
| HIGGS | [link](./experiments/06_HIGGS.ipynb) | 11000000 | 28 |  |  |  |  
| Airline (GPU) | [link](./experiments/01_airline_GPU.ipynb) | 115069017 | 13 | 0.726 | 0.738 | 0.728 |
| BCI (GPU) | [link](./experiments/02_BCI_GPU.ipynb) | 20497 | 2048 |  |  |  | 
| Football (GPU) | [link](./experiments/03_football_GPU.ipynb) | 19673 | 46 |  |  |  | 
| Planet Amazon (GPU) | [link](./experiments/04_PlanetKaggle_GPU.ipynb) | 40479 | 2048 |  |  |  | 
| Fraud Detection (GPU) | [link](./experiments/05_FraudDetection_GPU.ipynb) | 284807 | 30 |  |  |  |
| HIGGS (GPU) | [link](./experiments/06_HIGGS_GPU.ipynb) | 1000000 | 28 | 0.770 | 0.770 | 0.766 |

The CPU experiments were run on an Azure VM Standard DS15 v2 with 20 cores and 140 GB memory. The GPU experiments were run on an Azure NV24 VM with 24 cores and 224 GB memory. The machine has 4 NVIDIA M60 GPUs. In both cases we used Ubuntu 16.04.


## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

