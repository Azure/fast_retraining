import os
import numpy as np
import glob


def labels_from(labels_df):
    """ Extracts the unique labels from the labels dataframe
    """
    # Build list with unique labels
    label_list = []
    for tag_str in labels_df.tags.values:
        labels = tag_str.split(' ')
        for label in labels:
            if label not in label_list:
                label_list.append(label)
    return label_list


def enrich_with_feature_encoding(labels_df):
    # Add onehot features for every label
    for label in labels_from(labels_df):
        labels_df[label] = labels_df['tags'].apply(lambda x: 1 if label in x.split(' ') else 0)
    return labels_df


def to_multi_label_dict(enriched_labels_df):
    df = enriched_labels_df.set_index('image_name').drop('tags', axis=1)
    return dict((filename, encoded_array) for filename, encoded_array in zip(df.index, df.values))


def get_file_count(folderpath):
    """ Returns the number of files in a folder
    """
    return len(glob.glob(folderpath))


def threshold_prediction(pred_y, threshold=0.5):# TODO: Needs to be tuned?
    return pred_y > threshold


