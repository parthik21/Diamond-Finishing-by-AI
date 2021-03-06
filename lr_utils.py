import numpy as np
import h5py
    
    
def load_dataset():
    train_dataset = h5py.File('../Project DF-AI/DataSet/HDF_Dataset/train_data.h5', "r")
    train_set_x_orig = np.array(train_dataset["train-x-value"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train-y-value"][:]) # your train set labels

    test_dataset = h5py.File('../Project DF-AI/DataSet/HDF_Dataset/test_data.h5', "r")
    test_set_x_orig = np.array(test_dataset["test-x-value"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test-y-value"][:]) # your test set labels

    #labels = np.array([b'not-approved',b'approved']) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig

