import os
import io
import h5py
import numpy as np

#store train data
def store_train_data(images, labels):
    """ Stores an array of images to HDF5.
        Parameters:
        ---------------
        images       images array, (N, 128, 128, 3) to be stored
        labels       labels array, (N, 1) to be stored
    """
    num_images = len(images)

    # Create a new HDF5 file
    with h5py.File('../Project DF-AI/DataSet/HDF_Dataset/train_data.h5', "w") as file:
    #file = h5py.File('../Project DF-AI/DataSet/HDF_Dataset/train_data.h5', "w")

        # Create a dataset in the file
        file.create_dataset(
            "train-x-value", np.shape(images), h5py.h5t.STD_U8BE, data=images
            )
        file.create_dataset(
            "train-y-value", np.shape(labels), h5py.h5t.STD_U8BE, data=labels
            )
    #file.close()

def create_train_lables():
    y_values = []

    for i in range(1,11):

        if i in (1,3,5,6):
            for j in range(0,90):
                y_values.append(0)
        else:
            for j in range(0,90):
                y_values.append(1)
    return y_values


#store test data
def store_test_data(images, labels):
    """ Stores an array of images to HDF5.
        Parameters:
        ---------------
        images       images array, (N, 128, 128, 3) to be stored
        labels       labels array, (N, 1) to be stored
    """
    num_images = len(images)

    # Create a new HDF5 file
    with h5py.File('../Project DF-AI/DataSet/HDF_Dataset/test_data.h5', "w") as file:
    #file = h5py.File('../Project DF-AI/DataSet/HDF_Dataset/test_data.h5', "w")

        # Create a dataset in the file
        file.create_dataset(
            "test-x-value", np.shape(images), h5py.h5t.STD_U8BE, data=images
            )
        file.create_dataset(
            "test-y-value", np.shape(labels), h5py.h5t.STD_U8BE, data=labels
            )
    #file.close()


def create_test_lables():
    y_values = []

    for i in range(1,4):

        if i in (2,3):
            for j in range(0,90):
                y_values.append(0)
        else:
            for j in range(0,90):
                y_values.append(1)
    return y_values

