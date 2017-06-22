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

In the following table there are sumarized some results of the benckmarks performed in the experiments:

| Dataset | Experiment | Data size | Features | time xgb | time xgb_hist | time lgb | F1 xgb | F1 xgb_hist | F1 lgb | 
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Airline | [link](./experiments/01_airline.ipynb) | 115069017 | 13 | 2180 | 578 | 366 | 0.717 | 0.698 | 0.694 |
| BCI | [link](./experiments/02_BCI.ipynb) | 20497 | 2048 | 15.97 | 52.69 | 6.38 | 0.110 | 0.142 | 0.137 |
| Football | [link](./experiments/03_football.ipynb) | 19673 | 46 | 2.27 | 2.47 | 0.582 | 0.458 | 0.460 | 0.587 |
| Planet Amazon | [link](./experiments/04_PlanetKaggle.ipynb) | 40479 | 2048 | 291.93 | 2238.96 | 78.43 | 0.805 | 0.819 | 0.891 |
| Fraud Detection | [link](./experiments/05_FraudDetection.ipynb) | 284807 | 30 | 4.45 | 1.20 | 0.73 | 0.824 | 0.802 | 0.813 |
| Airline (GPU) | [link](./experiments/06_airline_GPU.ipynb) | 115069017 | 13 | 65.04 | 27.15 | 21.35 | 0.726 | 0.738 | 0.728 |
| HIGGS (GPU) | [link](./experiments/07_HIGGS_GPU.ipynb) | 1000000 | 28 | 107.63 | 51.26 | 28.90 | 0.770 | 0.770 | 0.766 |

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

