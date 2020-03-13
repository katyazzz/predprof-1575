import requests
import cognitive_face as CF

import cv2
import os , os.path
file = open("id"+'.txt',"w")
nam = []
SUBSCRIPTION_KEY = '021eaebbf45a4c6d87e43c8e9ce040b6'   
CF.Key.set(SUBSCRIPTION_KEY)
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0'  
CF.BaseUrl.set(BASE_URL)
PERSON_GROUP_ID = 'persons'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
vidcap = cv2.VideoCapture("forvid.mp4")
print (vidcap.read())
success,image = vidcap.read()
coun = 0
success = True
while success:
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite("frame%d.png" % coun, image)     
    coun += 1
st="C:\\Users\\locadmin\\Desktop\\shrd\\frame"
en=".png"
count = 0
mid= str(count)
print(st+mid+en)

while coun!=count :
    mid= str(count)
    print(mid)
    count +=1
    response = CF.face.detect(st+mid+en)
    print(response)
    if os.path.exists(st+mid+en):
        img_url = st+ mid +en
        print(img_url) 
        os.remove(st+mid+en)
        if response != []:
            face_ids = [d['faceId'] for d in response]
            identified_faces = CF.face.identify(face_ids, PERSON_GROUP_ID)
            for i in range(len(identified_faces)):
                idf= str(identified_faces[i])
                idf= idf.split()
                if len(idf)>4:
                    idfi = idf[4]
                    idfix = idfi[1:37]
                    for m in range(len(massid)):
                        if idfix == massid[m]:
                            idfix= id1[m]
                            if nam.count(str(idfix)) <1:
                                nam.append(idfix)
                                file = open("id"+'.txt',"w")
                                file.write(str(nam))
                                file.close()
                else:
                    break

