# Fast Retraining

In this repo we compare two of the fastest boosted decision tree libraries: [XGBoost](https://github.com/dmlc/xgboost) and [LightGBM](https://github.com/microsoft/LightGBM). We will evaluate them across datasets of several domains and different sizes.

On July 25, 2017, we published a blog post evaluating both libraries and discussing the benchmark results. The post is [Lessons Learned From Benchmarking Fast Machine Learning Algorithms](https://blogs.technet.microsoft.com/machinelearning/2017/07/25/lessons-learned-benchmarking-fast-machine-learning-algorithms/).

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

In the following table there are summarized the time results (in seconds) and the ratio of the benchmarks performed in the experiments:

| Dataset | Experiment | Data size | Features | xgb time: <br/> CPU (GPU) | xgb_hist time: <br/> CPU (GPU) | lgb time: <br/>CPU (GPU) | ratio xgb/lgb: <br/> CPU (GPU) | ratio xgb_hist/lgb: <br/> CPU <br/> (GPU) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Football | [Link CPU](./experiments/03_football.ipynb)<br/> [Link GPU](./experiments/03_football_GPU.ipynb) | 19673 | 46 | 2.27 (7.09) | 2.47 (4.58) | 0.58 (0.97) | 3.90 <br/> (7.26) | 4.25 <br/>(4.69) |
| Fraud Detection | [Link CPU](./experiments/05_FraudDetection.ipynb)<br/> [Link GPU](./experiments/05_FraudDetection_GPU.ipynb) | 284807 | 30 | 4.34 (5.80) | 2.01 (1.64) | 0.66 (0.29) | 6.58 <br/>(19.74) | 3.04 <br/> (5.58) |
| BCI | [Link CPU](./experiments/02_BCI.ipynb)<br/> [Link GPU](./experiments/02_BCI_GPU.ipynb) | 20497 | 2048 | 11.51 (12.93) | 41.84 (42.69) | 7.31 (2.76)| 1.57 <br/> (4.67) | 5.72 <br/>(15.43) |
| Planet Kaggle | [Link CPU](./experiments/04_PlanetKaggle.ipynb)<br/> [Link GPU](./experiments/04_PlanetKaggle_GPU.ipynb) | 40479 | 2048 | 313.89 (-) | 2115.28 (2028.43) | 194.57 (317.68)| 1.61 <br/> (-) | 10.87 <br/>(6.38) |
| HIGGS | [Link CPU](./experiments/06_HIGGS.ipynb)<br/> [Link GPU](./experiments/06_HIGGS_GPU.ipynb) | 11000000 | 28 | 2996.16 (-) | 121.21 (114.88) | 119.34 (71.87) | 25.10 <br/>(-) | 1.01 <br/> (1.59) |
| Airline | [Link CPU](./experiments/01_airline.ipynb) <br/> [Link GPU](./experiments/01_airline_GPU.ipynb) | 115069017 | 13 | - (-) | 1242.09 (1271.91) | 1056.20 (645.40) | - <br/> (-) | 1.17 <br/>(1.97) |


In the next table we summarize the performance results using the [F1-Score](https://en.wikipedia.org/wiki/F1_score).

| Dataset | Experiment | Data size | Features | xgb F1: <br/> CPU (GPU) | xgb_hist F1: <br/> CPU (GPU) | lgb F1: <br/> CPU (GPU) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Football | [Link](./experiments/03_football.ipynb) <br/> [Link](./experiments/03_football_GPU.ipynb) | 19673 | 46 | 0.458 (0.470) | 0.460 (0.472) | 0.459 (0.470)|
| Fraud Detection | [Link](./experiments/05_FraudDetection.ipynb) <br/> [Link](./experiments/05_FraudDetection_GPU.ipynb)  | 284807 | 30 | 0.824 (0.821) | 0.802 (0.814) | 0.813 (0.811) |
| BCI | [Link](./experiments/02_BCI.ipynb) <br/> [Link](./experiments/02_BCI_GPU.ipynb) | 20497 | 2048 | 0.110 (0.093) | 0.142 (0.120) | 0.137 (0.138) |
| Planet Kaggle | [Link](./experiments/04_PlanetKaggle.ipynb) <br/> [Link](./experiments/04_PlanetKaggle_GPU.ipynb) | 40479 | 2048 | 0.805 (-) | 0.822 (0.822) | 0.822 (0.821)|
| HIGGS | [Link](./experiments/06_HIGGS.ipynb) <br/> [Link](./experiments/06_HIGGS_GPU.ipynb) | 11000000 | 28 | 0.763 (-) | 0.767 (0.767) | 0.768 (0.767) |
| Airline | [Link](./experiments/01_airline.ipynb) <br/> [Link](./experiments/01_airline_GPU.ipynb) | 115069017 | 13 | - (-) | 0.741 (0.745) | 0.732 (0.745) |

The experiments were run on an Azure NV24 VM with 24 cores and 224 GB memory. The machine has 4 NVIDIA M60 GPUs. In both cases we used Ubuntu 16.04.


## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

