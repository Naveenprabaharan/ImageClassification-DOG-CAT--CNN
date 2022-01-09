from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array
from skimage.io import imread #image read
from skimage.transform import resize #to resize the Image

#Author Naveenprabaharan S - GCT[1918L12] 

def DogCAT_pred(path):
    model = load_model('best_model.h5')
    path = path
    img = imread(path) #read image
    img = resize(img, (256,256)) #resize


    #  preprocessing 
    i = img_to_array(img)
    i = preprocess_input(i)
    input_array = np.array([i])
    input_array.shape
    pred = np.argmax(model.predict(input_array))

    # final solution
    if pred == 0:
        return "The Image is CAT"
    else:
        return "The Image is DOG"

    # # to Show Input Image
    # plt.imshow(img)
    # # plt.imshow(input_array[0])
    # plt.title("Input Image")
    # plt.show()
