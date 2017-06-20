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

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

