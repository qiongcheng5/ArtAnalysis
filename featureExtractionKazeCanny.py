import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.decomposition import PCA
import cv2
import numpy as np
from scipy.misc import imsave
from scipy import ndimage, misc
import os
import xlsxwriter

# converting a given list or iterator to a string
def get_nice_string(list_or_iterator):
    return ", ".join( str(x) for x in list_or_iterator)

# Canny Edge Extractor
def canny_edge_extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path, 0)
    edges = cv2.Canny(image, 100, 100)
    
    return edges
        
# Kaze Feature Extractor  
def kaze_extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path, 0)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        if dsc is None:
            print(image_path)
            return None
        else:
            dsc = dsc.flatten()
            # Making descriptor of same size
            # Descriptor vector size is 64
            needed_size = (vector_size * 64)
            if dsc.size < needed_size:
                # if we have less the 32 descriptors then just adding zeros at the
                # end of our feature vector
                dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: %s'% e)
        return None

    return dsc

# extracting all images in the given folder (parameter named images_path) and saving extracted features into a file (parameter named filename)
def batch_extract_features(images_path, filename, featuretype):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    # Open the file with writing permission
    myfile = open(filename, 'w')
    
    result = {}
    featuresline = ''
    for f in files:
        print('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = canny_edge_extract_features(f) if featuretype == 1 else kaze_extract_features(f)

        if result[name] is None:
            print(f)
        else:
            featuresline = featuresline + str.format('%s, %s\n' % (name, get_nice_string(result[name])))
            print(len(result[name]))
            myfile.write(str.format('%s, %s\n' % (name, get_nice_string(result[name])))) 
            
    # Close the file
    myfile.close()
    return featuresline

# show image
def show_img(path):
    img = imread(path, mode="RGB")
    plt.imshow(img)
    plt.show()
    
# main entry
def run():
    images_path = './images/'    
    filename = "./imagefvector.txt"
    features = batch_extract_features(images_path, filename, 2)
    
    print('Finished')
    
run()