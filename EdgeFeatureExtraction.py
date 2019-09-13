import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
#from sklearn import datasets
#from sklearn.decomposition import PCA
import cv2
import numpy as np
from scipy.misc import imsave
from scipy import ndimage, misc
import os
import xlsxwriter
import xlrd # Reading an excel file using Python

# Read Momo statistics features from Todd into python
def getMomaImageFeatures(images_path, momafilename, outfile):
    # To open Workbook 
    wb = xlrd.open_workbook(momafilename) 
    sheet = wb.sheet_by_index(0)
    # For row 0 and column 0 
    ##print column names
    #sheet.cell_value(0, 0) 
    #for i in range(sheet.ncols): 
    #    print(sheet.cell_value(0, i)) 
    
    ##print column value
    #for i in range(sheet.nrows): 
    #    if (i>1) :
    #        print(sheet.cell_value(i, 1))
            
    source = sheet.col_values(0)[1:sheet.nrows]
    name = sheet.col_values(1)[1:sheet.nrows]
    nationality = sheet.col_values(2)[1:sheet.nrows]
    title = sheet.col_values(3)[1:sheet.nrows]
    date = sheet.col_values(4)[1:sheet.nrows]
    AccessionNumber = sheet.col_values(5)[1:sheet.nrows]
    ThumbnailURL = sheet.col_values(6)[1:sheet.nrows]
    image_filenames = []
    isDecentArtists = []
    artworksLG5 = []
    artworksLG10 = []
    for i in range(sheet.nrows-1):
        url = sheet.col_values(6)[i+1]
        image_filenames.append(url[url.rfind('/')+1 : url.rfind('.')])  #?
        isDecentArtists.append(int(sheet.col_values(7)[i+1]))
        artworksLG5.append(sheet.col_values(8)[i+1])
        artworksLG10.append(int(sheet.col_values(9)[i+1]))
    
#    ID = sheet.col_values(7)[1:sheet.nrows]
#    SourceID = sheet.col_values(8)[1:sheet.nrows]
#    ArtworkSourceIDKey = sheet.col_values(9)[1:sheet.nrows]
    HueArithmeticAverage = sheet.col_values(10)[1:sheet.nrows]
    HueCircularAverage = sheet.col_values(11)[1:sheet.nrows]
    LightnessArithmeticAverage = sheet.col_values(12)[1:sheet.nrows]
    SaturationArithmeticAverageCylinder = sheet.col_values(13)[1:sheet.nrows]
    SaturationArithmeticAverageBicone = sheet.col_values(14)[1:sheet.nrows]
    BrightnessDimensionAverage = sheet.col_values(15)[1:sheet.nrows]
    #BrightnessLogarithmicAverage = sheet.col_values(16)[1:sheet.nrows]
    #BrightnessIntervalAverage = sheet.col_values(17)[1:sheet.nrows]   
    BrightnessContrast = sheet.col_values(17)[1:sheet.nrows] 
    RedEntropy = sheet.col_values(18)[1:sheet.nrows] 
    GreenEntropy = sheet.col_values(19)[1:sheet.nrows] 
    BlueEntropy = sheet.col_values(20)[1:sheet.nrows] 
    Entropy = sheet.col_values(21)[1:sheet.nrows] 

    edgesV = batch_extract_features_Inorder(images_path, image_filenames, 2)
    #all = zip(source, name, title, date, AccessionNumber, ID, ThumbnailURL, ImagePath, SourceID, ArtworkSourceIDKey, HueArithmeticAverage, HueCircularAverage, LightnessArithmeticAverage, SaturationArithmeticAverageCylinder, SaturationArithmeticAverageBicone,BrightnessDimensionAverage, BrightnessLogarithmicAverage,BrightnessIntervalAverage, edgesV)
    all = zip(source, name, nationality, title, date, AccessionNumber, ThumbnailURL, image_filenames, isDecentArtists, artworksLG5, artworksLG10, HueArithmeticAverage, HueCircularAverage, LightnessArithmeticAverage, SaturationArithmeticAverageCylinder, SaturationArithmeticAverageBicone,BrightnessDimensionAverage, BrightnessContrast,RedEntropy, GreenEntropy, BlueEntropy, Entropy, edgesV)

    myfile = open(outfile, 'w')
    for source, name, nationality, title, date, AccessionNumber, ThumbnailURL, ImagePath, isDecentArtists, artworksLG5, artworksLG10, HueArithmeticAverage, HueCircularAverage, LightnessArithmeticAverage, SaturationArithmeticAverageCylinder, SaturationArithmeticAverageBicone,BrightnessDimensionAverage, BrightnessContrast,RedEntropy, GreenEntropy, BlueEntropy, Entropy, edgesV in all:
        #myfile.write(str.format('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%\t%s\t%s\t%s\t%s\t%s' % (str(source), str(name), str(title), str(date), str(AccessionNumber), str(ID), str(ThumbnailURL), str(ImagePath), str(SourceID), str(ArtworkSourceIDKey), str(HueArithmeticAverage), str(HueCircularAverage), str(LightnessArithmeticAverage), str(SaturationArithmeticAverageCylinder), str(SaturationArithmeticAverageBicone), str(BrightnessDimensionAverage), str(BrightnessLogarithmicAverage), str(BrightnessIntervalAverage), edgesV)))
        myfile.write(str.format('%s\t%d\t%d\t%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (AccessionNumber, isDecentArtists, artworksLG5, artworksLG10,HueArithmeticAverage, HueCircularAverage, LightnessArithmeticAverage, SaturationArithmeticAverageCylinder, SaturationArithmeticAverageBicone,BrightnessDimensionAverage, BrightnessContrast, RedEntropy, GreenEntropy, BlueEntropy, Entropy, edgesV)))
        
    myfile.close()
    return all
    
# converting a given list or iterator to a string
def get_nice_string(list_or_iterator):
    return "\t".join( str(x) for x in list_or_iterator)

# deprecated 
def edge_extract_features(image_path, vector_size=32):
    # W1siZiIsIjc1MTUyIl0sWyJwIiwiY29udmVydCIsIi1yZXNpemUgMzAweDMwMFx1MDAzZSJdXQ.png
    image = cv2.imread(str.format('./images/%s' % image_path), 0)
    edges = cv2.Canny(image, 100, 100)
    #img2 = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    #plt.imshow(img2)
    edgesV = get_nice_string(edges.flatten())
    
    return edgesV

# extracting all images in the given folder (parameter named images_path) and returning a list of extracted features 
def batch_extract_features_Inorder(images_path, image_filenames, featuretype):
    result = [] #'edge detection']
    for f in image_filenames:
        #result.append(edge_extract_features(f, featuretype))
        result.append(image_extract_features(os.path.join(images_path, f + '.png'), featuretype))
        #featuresline = featuresline + str.format('%s\t%s\n' % (name, get_nice_string(result[name].flatten())))

    return result
   
"""
def batch_extract_features(images_path, filename, featuretype):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    # Open the file with writing permission
    myfile = open(filename, 'w')
    
    result = {}
    featuresline = ''
    for f in files:
        print('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = edge_extract_features(f)
        #featuresline = featuresline + str.format('%s, %s\n' % (name, get_nice_string(result[name])))
        myfile.write(str.format('%s\t%s\n' % (name, get_nice_string(result[name].flatten()))))
        
    result = {}
    featuresline = ''
    for f in files:
        print('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = canny_edge_extract_features(f) if featuretype == 1 else kaze_extract_features(f)

        if result[name] is None:
            print(f)
        else:
            #featuresline = featuresline + str.format('%s, %s\n' % (name, get_nice_string(result[name])))
            print(len(result[name]))
            myfile.write(str.format('%s\t%s\n' % (name, get_nice_string(result[name])))) 

    # Close the file
    myfile.close()
    return result
"""

# deprecated. extracting all images in the given folder (parameter named images_path) and saving extracted features into a file (parameter named filename)
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
            featuresline = featuresline + str.format('%s\t%s\n' % (name, get_nice_string(result[name])))
            print(len(result[name]))
            myfile.write(str.format('%s\t%s\n' % (name, get_nice_string(result[name])))) 
            
    # Close the file
    myfile.close()
    return featuresline

# image extraction for individual file
def image_extract_features(filename, featuretype):
    name = filename.split('/')[-1].lower()
    print(str.format('image_extract_features : filename = %s' % filename))
    featureSet = canny_edge_extract_features(filename) if featuretype == 1 else kaze_extract_features(filename)

    return str.format('0\t%s\n' % (name)) if featureSet is None else str.format('1\t%s\t%s\n' % (name, get_nice_string(featureSet)))

# Canny Edge Extractor
def canny_edge_extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path, 0)
    edges = cv2.Canny(image, 100, 100)
    
    return edges

# Kaze Feature extractor for individual file  
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
            print(str.format('kaze_extract_features : none extraction in %s' % image_path))
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


def show_img(path):
    img = imread(path, mode="RGB")
    plt.imshow(img)
    plt.show()
    
def run():
    images_path = './images/'    
    filename = "./imagefvector.txt"
    #features = batch_extract_features(images_path, filename)
    
    momafilename = './MoMAPaintingQArtLearnMetrics_Todd_DecentArtists_0705.xlsx'  #'MoMAPaintingQArtLearnMetricsV1.xls'
    outfile = './MoMAPaintingQArtLearnDecentArtistsMetricsVector_0705.txt'                #'./MoMAPaintingQArtLearnMetricsVector.txt'
    getMomaImageFeatures(images_path, momafilename, outfile)
    
    print('Finished')
    
run()