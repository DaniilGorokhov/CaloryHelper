import os
import json
import shutil

productNames = open('meta/classes.txt', 'r')
productNames = productNames.read()
productNames = productNames.split('\n')
productNames.pop()

with open('meta/test.json') as f:
    imagesForTest = json.load(f)

source = 'D:/Programming/intersystemsIRIS/PythonGateway-Template/pythonAI/products/train/'
destination = 'D:/Programming/intersystemsIRIS/PythonGateway-Template/pythonAI/products/test/'

for productName in productNames:
    currentProductImages = imagesForTest[productName]
    for productImage in currentProductImages:
        if not os.path.exists('products/test/' + productName):
            os.makedirs('products/test/' + productName)
        # print(source + productImage + '.jpg')
        # print(destination + productName + '/')
        shutil.move(source + productImage + '.jpg', destination + productName + '/')
