from PIL import Image, ImageEnhance, ImageFilter
import os
dataset = "AGAR_representative"
for root, dirs, files in os.walk(dataset):
    for x in files:
        if x.endswith(".jpg"):
            print(x)
            img = Image.open(root + "\\" + x)
            img.thumbnail((300, 300))
            img = img.convert("L")
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.75)
            img = img.filter(ImageFilter.FIND_EDGES)
            #img = img.filter(ImageFilter.GaussianBlur(0.75))
            img.save("Preprocessed dataset/{}.jpg".format(x))