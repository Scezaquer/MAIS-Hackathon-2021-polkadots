from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps
import scipy.ndimage as ndi
import numpy as np
import matplotlib.pyplot as plt

def remove_edges(path):
    img = Image.open(path)
    img = img.convert("L")#turns the image into greyscale
    enhancer = ImageEnhance.Contrast(img)   #Enhances contrast
    img = enhancer.enhance(1.75)            #
    img = img.filter(ImageFilter.FIND_EDGES)    #Finds the edges to only take relevant stuff into account
    cx, cy = ndi.center_of_mass(np.array(img)) #Finds the center of mass of the edges

    #Creates an eliptical mask supposed to englobe the petri dish and remove everything outside centered around the center of mass
    dist_to_side = min(cx, cy, img.size[0]-cx, img.size[1]-cy)
    boundingBox = [0, 0, 0, 0]
    print(dist_to_side)
    boundingBox[0] = round(cx-dist_to_side)
    boundingBox[1] = round(cy-dist_to_side)
    boundingBox[2] = round(cx+dist_to_side)
    boundingBox[3] = round(cy+dist_to_side)
    print(boundingBox)

    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + img.size, fill=255)

    im2 = Image.new('RGB', img.size)

    output = Image.composite(Image.open(path), im2, mask)

    return output