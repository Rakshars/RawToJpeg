#Python file for converting raw files to jpeg
#Code makes it easier than to convert it yourself manually
#Author : Amitrakshar Mukherjee

import rawpy		#import rawpy - if not there use pip/pip3 install rawpy
import imageio		#import imageio - if not there use pip/pip3 install imageio
import os		#import os for file and directory management
import sys		#import sys for getting arguements from the user
from PIL import Image   #import Image sub-library from the PIL library - if not there use pip/pip3 install PIL

if (len(sys.argv) == 1):		#Checking the number of arguements that the user has given, required 3 but if given only 1 then throw error.
    print("Please mention the input parameters as follows: python3 RawToJpeg.py inputPath outputPath.")
    sys.exit()		#exiting the code

if (len(sys.argv) > 3):		#If the amount of arguements is above 3 then give error as the max number of arguements required is 3
    print("Too many input parameters are giev which is not required!")
    sys.exit()		#Exiting the code

if (len(sys.argv) < 3):		#If the number of arguements is less than 3 then throw error to user to give more arguements
    print("Please mention the input parameters as follows: python3 RawToJpeg.py inputPath outputPath!")
    sys.exit()		#Exiting the code

inPath = str(sys.argv[1])		#Getting the inpath from the user
outPath = str(sys.argv[2])		#Getting the outpath from the user
folderContents = os.listdir(inPath)	#Getting all the raw files in the given folder specified by the user

for eachFile in folderContents:		#For each of the files in the given inPath(the folder that contains the raw images)
    try:    # Checks the following lines of code for any error. If there are no errors the except block of code will not execute.
        inputImageFullPath = str(inPath) + str(eachFile)    # joins the image name with its directory path to feed it in Image.open() function.
        img = Image.open(inputImageFullPath) # Opening the image file. Would execute without any errors if the input file is a valid image file. Will throw an error is the input file is not a valid image file.
        modifiedPath = inPath + eachFile		#Modifying the inPath with the name of the raw file
        print ("The value of inPath is: " + modifiedPath)
        outPath1 = outPath + eachFile		#Adding name for the final jpeg image
        outPath2 = outPath1.partition('.')[0]		#Getting the name of the final file till the .raw or .NEF or .CR2
        outPath3 = outPath2 + ".jpeg"		#Adding the .jpeg to make it a valid jpeg file
        print ("The value of outPath is: " + outPath3)
        print("")
        rawImage = rawpy.imread(modifiedPath)		#Reading the original raw file
        rgbImage = rawImage.postprocess()		#Procssing the image to get the final jpeg file
        imageio.imsave(outPath3, rgbImage)		#Saving the jpeg file with the same name as the name of the raw file
    except: # If there are errors in the try block of code which means that the input file is not a valid image file then the following lines of code would be executed.
        print('The input file is not a valid image file')   # Printing this statement to let the user know that the input file is not a valid image file.
        print('') # Printing an empty line that the next lines while are going to be printed do not stick to the line above.
