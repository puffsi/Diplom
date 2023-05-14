import cv2
import sys

def face_remove(input_path, output_path):
  #i = 1
  #j = 1
  #k = 1
  #while i <= 2000:
    image = cv2.imread(input_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier("C:/testing/haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30)
    )

    print("Found {0} Faces!".format(len(faces)))
    print(len(faces))
    if(len(faces) == 1):
      for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0,0 ), 150)
        status = cv2.imwrite(output_path, image)
        print ("Image faces_detected.jpg written to filesystem: ",status)
        #j += 1
    #else:
      #status = cv2.imwrite(output_path2 + str(k) + '.jpg', image)
      #print ("Image faces_detected.jpg written to filesystem: ",status)
      #k += 1
    #i += 1
    return 0