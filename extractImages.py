import numpy as np
from PIL import Image
import glob

def extract_train_images():
    images = []
    for f in glob.iglob("""Train dataset location"""):
        images.append(np.asarray(Image.open(f)))

    images = np.array(images)

    return images

def extract_test_images():
    images = []
    for f in glob.iglob("""Test dataset location"""):
        images.append(np.asarray(Image.open(f)))

    images = np.array(images)

    return images
