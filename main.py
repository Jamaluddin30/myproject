# This are the import packages which is needed for this project.




import os
from datetime import datetime
import cv2
import sys
import time




#  There are Azure sevice which I used for face detection.


from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person





# create variables for resource's Azure endpoint and key.

KEY = "219e7c810d774cc0a4150d2ac3503b03"


ENDPOINT = "https://faceforazure.cognitiveservices.azure.com/"


face_client = FaceClient(ENDPOINT,CognitiveServicesCredentials(KEY))







#Assign path and create list of images.
path = 'images'
images = []
personNames = []
myList = os.listdir(path)
#print(myList)

for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)




  

#For recording Attendence by face recognization.
def attendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tStr},{dStr}')

#  declare variables that will point to the source and target images for the verification operation.
IMAGE_BASE_URL = path

target_image_file_names = ['Ajay Devgan.jpg']

source_image_file_name1 = 'Akshay Kumar.jpg'
source_image_file_name2 = 'Smit.jpg'


# Detect face(s) from source image 1, returns a list[DetectedFaces]
# We use detection model 3 to get better performance.
detected_faces1 = face_client.face.detect_with_url(IMAGE_BASE_URL + source_image_file_name1, detection_model='detection_03')

# Add the returned face's face ID

source_image1_id = detected_faces1[0].face_id
print('{} face(s) detected from image {}.'.format(len(detected_faces1), source_image_file_name1))


detected_faces2 = face_client.face.detect_with_url(IMAGE_BASE_URL + source_image_file_name2, detection_model='detection_03')

source_image2_id = detected_faces2[0].face_id
print('{} face(s) detected from image {}.'.format(len(detected_faces2), source_image_file_name2))


# List for the target face IDs (uuids)
detected_faces_ids = []

#If face matched then show detected face and saved name to attendence file with time and date.
verify_result_same = face_client.face.verify_face_to_face(source_image1_id, detected_faces_ids[0])
print('Faces from {} & {} are of the same person, with confidence: {}'
    .format(source_image_file_name1, target_image_file_names[0], verify_result_same.confidence)
    if verify_result_same.is_identical

      
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            attendance(name)




    else 'Faces from {} & {} are of a different person, with confidence: {}'
        .format(source_image_file_name1, target_image_file_names[0], verify_result_same.confidence))




    #Showing webcam with detecting image.

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()

