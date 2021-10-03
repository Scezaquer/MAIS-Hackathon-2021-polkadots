import keras
from scipy._lib.six import X
import tensorflow as tf
from keras.models import Sequential, Model, load_model
from keras.preprocessing import image
from keras.callbacks import TensorBoard 
from keras.utils.data_utils import get_file
from keras import utils as np_utils
from keras.applications import ResNet50, DenseNet121
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, Dense, Input, Dropout, Activation, Flatten, BatchNormalization,ZeroPadding2D,concatenate,Lambda,GlobalAveragePooling2D
from keras.optimizers import Adam,SGD,RMSprop, Adadelta

import numpy as np
from numpy.lib.function_base import append
from skimage import io
import cv2 
from sklearn.metrics import auc, roc_curve, confusion_matrix,classification_report 
from scipy import interp
from PIL import Image, ImageChops
from keras.preprocessing import image

from count_colonies import *

def get_useful_segments(img, masked_img):
    imgArray = []
    img = img.resize((1000, 1000))
    masked_img = masked_img.resize((1000, 1000))
    segment_size = 100
    for x in range(0, img.size[0], segment_size):
        for y in range(0, img.size[1], segment_size):
            segment = masked_img.crop((x, y, x+min(img.size[0]-x, segment_size), y+min(img.size[1]-y, segment_size)))

            diff = ImageChops.difference(segment, Image.new("RGB", (segment_size, segment_size)))

            if ( diff.getbbox() ):
                imgArray.append(img.crop((x, y, x+min(img.size[0]-x, segment_size), y+min(img.size[1]-y, segment_size))))
    return imgArray

def img_to_array(img):
    img = np.array(img)#From PIL to cv2
    img = image.img_to_array(img) 
    img = img.reshape((1,) + img.shape)  
    return img

def count_colonies(original_image, model):
    nbr_colonies = 0
    masked_img = remove_edges(original_image)

    useful_segments = get_useful_segments(original_image, masked_img)
    for x in useful_segments:
        nbr_colonies += model.predict(img_to_array(x))
    return nbr_colonies

def loadNN(path):
    model = tf.keras.models.load_model(path)
    return model