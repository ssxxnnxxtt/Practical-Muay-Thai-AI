import cv2
import mediapipe as mp

def get_landmarks(self, path_name):
    cap = cv2.VideoCapture(path_name)
    frameTime = 1
    threshold = 0
    results_list = []
    diff = 4
 
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            threshold += 1
 
            showed, frame = cap.read()
            if showed:
                frame = cv2.resize(frame, (1920, 1080))
 
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img.flags.writeable = False
 
                results = holistic.process(img)
 
                try:
                    landmarks = results.pose_landmarks.landmark
                except:
                    pass
 
                img.flags.writeable = True
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
 
                mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
 
                 
                #Important
                if threshold % diff == 0:
                    cv2.imshow('Mediapipe Feed', img)
                    results_list.append(results)
 
                if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                    break
            else:
                break
 
        cap.release()
        cv2.destroyAllWindows()