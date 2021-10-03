from PIL import ImageEnhance, ImageFilter, Image
import cv2 as cv

def preprocess(img):
    img = Image.open(img)   #Opens the image
    #img.thumbnail((300, 300))           #resizes it to 300x300
    img = img.convert("L")              #Converts it to greyscale
    enhancer = ImageEnhance.Contrast(img)   #Increases contrast
    img = enhancer.enhance(1.75)            #
    img = img.filter(ImageFilter.FIND_EDGES)    #Finds the edges of the elements in the image
    img = img.filter(ImageFilter.GaussianBlur(0.75))
    #img.save("Images/preprocessed".format(x))   #Saves the preprocessed image
    return img

def count_colonies(img):
    #img = cv.imread(img, cv.IMREAD_GRAYSCALE) #Opens the image in grayscale
    ret, labels = cv.connectedComponents(img)   #Counts the number of elements based on connected pixels
    return ret - 1