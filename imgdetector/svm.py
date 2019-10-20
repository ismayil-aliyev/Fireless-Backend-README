import numpy as np
from PIL import Image
from skimage.color import rgb2grey
from resizeimage import resizeimage
import pickle
import os


def check_fire(image_url):
    image_reduce_shape = 144
    # Open file and preprocess
    img = Image.open(image_url)
    img_resized = np.array(img)
    img_grey = rgb2grey(img_resized)
    img_shape = np.shape(img_grey)
    img_shape = img_shape == (image_reduce_shape, image_reduce_shape)

    if not img_shape:
        img = Image.open(image_url)
        img_resized = resizeimage.resize_contain(img, [image_reduce_shape, image_reduce_shape])
        img_resized = np.array(img_resized)
        img_grey = rgb2grey(img_resized)

    img_grey = img_grey.reshape(1, image_reduce_shape * image_reduce_shape)

    # load model
    #pkl_filename = 'fire_predictor_model.pkl'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    IMG_DETECTOR = os.path.join(BASE_DIR, 'imgdetector')
    pkl_filename = IMG_DETECTOR + '/fire_predictor_model.pkl'
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)

    prediction = model.predict(img_grey)

    if prediction[0] == 1.0:
        return True
    else:
        return False
