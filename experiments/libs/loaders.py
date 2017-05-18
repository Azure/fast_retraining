import os
import pandas as pd
import arff
import numpy as np
from libs.bci_loader import dataset_epoch_generator, test_dataset_epoch_generator, features_and_labels_from
from functools import reduce


_FRAUD_PATH = 'fraud_detection', 'credit_card_fraud_kaggle', 'creditcard.csv'


def _get_datapath():
    return os.environ['MOUNT_POINT']


def load_fraud():
    """ Loads the credit card fraud data

    The datasets contains transactions made by credit cards in September 2013 by european cardholders.
    This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions.
    The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.
    It contains only numerical input variables which are the result of a PCA transformation.

    Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data.
    Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed
    with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset.
    The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is
    the response variable and it takes value 1 in case of fraud and 0 otherwise.
    Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC).
    Confusion matrix accuracy is not meaningful for unbalanced classification.

    The dataset has been collected and analysed during a research collaboration of Worldline and the Machine Learning Group
    (http://mlg.ulb.ac.be) of ULB (Universite Libre de Bruxelles) on big data mining and fraud detection. More details on current
    and past projects on related topics are available on http://mlg.ulb.ac.be/BruFence and http://mlg.ulb.ac.be/ARTML
    Please cite: Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling
    for Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015

    Returns
    -------
    pandas DataFrame

    """
    return pd.read_csv(reduce(os.path.join, _FRAUD_PATH, _get_datapath()))


def load_iot():
    """ Loads iot data

    Sensor stream contains information (temperature, humidity, light, and sensor voltage) collected from 54 sensors deployed
    in Intel Berkeley Research Lab. The whole stream contains consecutive information recorded over a 2 months
    period (1 reading per 1-3 minutes). I used the sensor ID as the class label, so the learning task of the stream is
    to correctly identify the sensor ID (1 out of 54 sensors) purely based on the sensor data and the corresponding recording time.

    While the data stream flow over time, so does the concepts underlying the stream. For example, the lighting during
    the working hours is generally stronger than the night, and the temperature of specific sensors (conference room)
    may regularly rise during the meetings.


    Returns
    -------
    pandas DataFrame
    """
    iot_path = 'iot', 'sensor_stream_berkeley', 'sensor.arff'

    dataset = arff.load(open(reduce(os.path.join, iot_path, _get_datapath())))
    columns = [i[0] for i in dataset['attributes']]
    return pd.DataFrame(dataset['data'], columns=columns)


def load_bci():
    """ Loads BCI data

    Contains measurements from 64 EEG sensors on the scalp of a single participant. 
    The purpose of the recording is to determine from the electrical brain activity when the participant is paying attention.

    Returns
    -------
    A tuple containing four numpy arrays
        train features
        trai labels
        test features
        test lalels
    """
    train_data_path = 'bci', 'train.mat'
    test_data_path = 'bci', 'test.mat'
    test_labels_path = 'bci', 'labels.txt'

    train_gen = dataset_epoch_generator(reduce(os.path.join, train_data_path, _get_datapath()))
    test_gen = test_dataset_epoch_generator(reduce(os.path.join, test_data_path, _get_datapath()),
                                 reduce(os.path.join, test_labels_path, _get_datapath()))

    train_X, train_y = features_and_labels_from(train_gen)    
    test_X, test_y = features_and_labels_from(test_gen)                          
    return train_X, train_y, test_X, test_y
