def count_colonies(image):
    img = cv.imread(image, cv.IMREAD_GRAYSCALE) #Opens the image in grayscale
    ret, labels = cv.connectedComponents(img)   #Counts the number of elements based on connected pixels
    return ret - 1