# Fast Retraining

In this repo we compare two of the fastest boosted decision tree libraries: [XGBoost](https://github.com/dmlc/xgboost) and [LightGBM](https://github.com/microsoft/LightGBM). We will evaluate them across datasets of several domains and different sizes.

## Installation and Setup

The installation instructions can be found [here](./INSTALL.md).

## Project

In the folder [experiments](./experiments) you can find the different experiments of the project. We developed 6 experiments with the CPU and GPU versions of the libraries.

* Airline
* BCI
* Football
* Planet Kaggle
* Fraud Detection
* HIGGS

In the folder [experiment/libs](./experiment/libs) there is the common code for the project.

## Benchmark

In the following table there are summarized the time results of the benchmarks performed in the experiments:

| Dataset | Experiment | Data size | Features | xgb time: <br/> CPU (GPU) | xgb_hist time: <br/>CPU (GPU) | lgb time: <br/>CPU (GPU) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Airline | [Link CPU](./experiments/01_airline.ipynb) <br/> [link GPU](./experiments/01_airline_GPU.ipynb) | 115069017 | 13 | 2180 (-) | 578 (432.14) | 366 (210.92) |
| BCI | [Link CPU](./experiments/02_BCI.ipynb)<br/> [link GPU](./experiments/02_BCI_GPU.ipynb) | 20497 | 2048 | 11.51 (12.93) | 41.84 (42.69) | 7.31 (2.76)|
| Football | [Link CPU](./experiments/03_football.ipynb)<br/> [link GPU](./experiments/03_football_GPU.ipynb) | 19673 | 46 | 1.78 (.09) | 3.57 (4.58) | 0.64 (0.97) |
| Planet Kaggle | [Link CPU](./experiments/04_PlanetKaggle.ipynb)<br/> [link GPU](./experiments/04_PlanetKaggle_GPU.ipynb) | 40479 | 2048 | 313.89 (-) | 2115.28 (2028.43) | 194.57 (317.68)|
| Fraud Detection | [Link CPU](./experiments/05_FraudDetection.ipynb)<br/> [link GPU](./experiments/05_FraudDetection_GPU.ipynb) | 284807 | 30 | 4.34 (5.80) | 2.01 (1.64) | 0.66 (0.29) |
| HIGGS | [Link CPU](./experiments/06_HIGGS.ipynb)<br/> [link GPU](./experiments/06_HIGGS_GPU.ipynb) | 11000000 | 28 | 653.45 (-) | 74.42 (79.26) | 63.32 (55.90) |

In the next table we summarize the performance results using the [F1-Score](https://en.wikipedia.org/wiki/F1_score).

| Dataset | Experiment | Data size | Features | F1 xgb | F1 xgb_hist | F1 lgb |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Airline | [link](./experiments/01_airline.ipynb) | 115069017 | 13 | 0.698 | 0.717 | 0.694 |
| Airline (GPU) | [link](./experiments/01_airline_GPU.ipynb) | 115069017 | 13 | - | 0.718 | 0.717 |
| BCI | [link](./experiments/02_BCI.ipynb) | 20497 | 2048 | 0.110 | 0.142 | 0.137 |
| BCI (GPU) | [link](./experiments/02_BCI_GPU.ipynb) | 20497 | 2048 | 0.093 | 0.120 | 0.138 | 
| Football | [link](./experiments/03_football.ipynb) | 19673 | 46 | 0.458 | 0.460 | 0.459 |
| Football (GPU) | [link](./experiments/03_football_GPU.ipynb) | 19673 | 46 | 0.470 | 0.472 | 0.470 | 
| Planet Kaggle | [link](./experiments/04_PlanetKaggle.ipynb) | 40479 | 2048 | 0.805 | 0.822 | 0.822 |
| Planet Kaggle (GPU) | [link](./experiments/04_PlanetKaggle_GPU.ipynb) | 40479 | 2048 | - | 0.822 | 0.821 | 
| Fraud Detection | [link](./experiments/05_FraudDetection.ipynb) | 284807 | 30 | 0.824 | 0.802 | 0.813 |
| Fraud Detection (GPU) | [link](./experiments/05_FraudDetection_GPU.ipynb) | 284807 | 30 | 0.821 | 0.814 | 0.811 |
| HIGGS | [link](./experiments/06_HIGGS.ipynb) | 11000000 | 28 | 0.756 | 0.761 | 0.761 |  
| HIGGS (GPU) | [link](./experiments/06_HIGGS_GPU.ipynb) | 11000000 | 28 | - | 0.761 | 0.761 |

The experiments were run on an Azure NV24 VM with 24 cores and 224 GB memory. The machine has 4 NVIDIA M60 GPUs. In both cases we used Ubuntu 16.04.


## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

