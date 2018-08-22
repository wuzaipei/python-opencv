from faceDetection.faceDetector import FaceDetector
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True, help = "Path to where the face cascade resides")
ap.add_argument("-i", "--image", required = True, help = "Path to where the image file resides")
ap.add_argument("-r", "--result", default = "result.jpg", help = "Path to where the result resides")
print (ap.parse_args())
input()
args = vars(ap.parse_args())

image = cv2.imread(args['family_portrait_photograph.jpg'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd = FaceDetector(args["face"])
faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 8, minSize = (30, 30))
print("I found {} face(s)".format(len(faceRects)))

for x, y, w, h in faceRects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.imwrite(args["result"], image)
cv2.waitKey(0)
