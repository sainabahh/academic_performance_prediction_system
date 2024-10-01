
from audioop import avg
from glob import glob
from itertools import count
import cv2
import mediapipe as mp
import numpy as np
import os
# place holders and global variables
x = 0                                       # X axis head pose
y = 0                                       # Y axis head pose

X_AXIS_CHEAT = 0
Y_AXIS_CHEAT = 0
import time
import pymysql


class Db:
    def __init__(self):
        self.cnx = pymysql.connect(host="localhost",user="root",password="123456789",database="academic")
        self.cur = self.cnx.cursor()


    def select(self, q):
        self.cur.execute(q)
        return self.cur.fetchall()

    def selectOne(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()


    def insert(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount


# import matplotlib.pyplot as plt

while True:

        ob = Db()
        data=ob.select("SELECT * FROM `acd_app_emotion_table` WHERE `pose`='pending'")
        print(data)
        if len(data)>0:
            for row in data:
                mp_face_mesh = mp.solutions.face_mesh
                face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

                mp_drawing = mp.solutions.drawing_utils

                path=r"C:\Users\sainaba shahanas kk\OneDrive\Desktop\Main project\acdamic (2)\acdamic\media/"+str(row[0])+".png"

                frame = cv2.imread(path)
                image =frame


                height, width = frame.shape[:2]


                # Non-max suppression to remove redundant overlapping boxes



                # Head pose detection started
                # Head pose detection started
                # Head pose detection started
                # Head pose detection started


                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

                # To improve performance
                image.flags.writeable = False

                # Get the result
                results = face_mesh.process(image)

                # To improve performance
                image.flags.writeable = True

                # Convert the color space from RGB to BGR
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                img_h, img_w, img_c = image.shape
                face_3d = []
                face_2d = []

                face_ids = [33, 263, 1, 61, 291, 199]


                try:
                    if results.multi_face_landmarks:
                        for face_landmarks in results.multi_face_landmarks:
                            mp_drawing.draw_landmarks(
                                image=image,
                                landmark_list=face_landmarks,
                                connections=mp_face_mesh.FACEMESH_CONTOURS,
                                landmark_drawing_spec=None)
                            for idx, lm in enumerate(face_landmarks.landmark):
                                # print(lm)
                                if idx in face_ids:
                                    if idx == 1:
                                        nose_2d = (lm.x * img_w, lm.y * img_h)
                                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)

                                    x, y = int(lm.x * img_w), int(lm.y * img_h)

                                    # Get the 2D Coordinates
                                    face_2d.append([x, y])

                                    # Get the 3D Coordinates
                                    face_3d.append([x, y, lm.z])

                                    # Convert it to the NumPy array
                            face_2d = np.array(face_2d, dtype=np.float64)

                            # Convert it to the NumPy array
                            face_3d = np.array(face_3d, dtype=np.float64)

                            # The camera matrix
                            focal_length = 1 * img_w

                            cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                                   [0, focal_length, img_w / 2],
                                                   [0, 0, 1]])

                            # The Distance Matrix
                            dist_matrix = np.zeros((4, 1), dtype=np.float64)

                            # Solve PnP
                            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                            # Get rotational matrix
                            rmat, jac = cv2.Rodrigues(rot_vec)

                            # Get angles
                            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

                            # Get the y rotation degree
                            x = angles[0] * 360
                            y = angles[1] * 360

                            print(x,y)

                            # See where the user's head tilting
                            if y < -15:
                                text = "Looking Left"
                            elif y > 10:
                                text = "Looking Right"
                            elif x < -15:
                                text = "Looking Down"
                            else:
                                text = "Forward"
                            # text = str(int(x)) + "::" + str(int(y)) + text
                            print(text)
                            print(text)
                            print(text)
                            print(text)

                            q="UPDATE `acd_app_emotion_table` SET `pose`='"+text+"' WHERE `id`='"+str(row[0])+"'"
                            #
                            ob.update(q)
                except:
                    pass
            time.sleep(5)