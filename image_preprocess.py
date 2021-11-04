from PIL import Image, ImageEnhance, ImageFilter
import os

def preprocess(dataset):
    for root, dirs, files in os.walk(dataset):
        #This goes through the files recursively so it dosen't matter if pictures are in sub-folders
        for x in files:
            if x.endswith(".jpg") or x.endswith(".png"):
                print(x)
                img = Image.open(root + "\\" + x)   #Opens the image
                img.thumbnail((300, 300))           #resizes it to 300x300
                img = img.convert("L")              #Converts it to greyscale
                enhancer = ImageEnhance.Contrast(img)   #Increases contrast
                img = enhancer.enhance(1.75)            #
                img = img.filter(ImageFilter.FIND_EDGES)    #Finds the edges of the elements in the image
                #img = img.filter(ImageFilter.GaussianBlur(0.75))
                img.save("Preprocessed dataset/{}".format(x))   #Saves the preprocessed image

preprocess("Raw dataset")