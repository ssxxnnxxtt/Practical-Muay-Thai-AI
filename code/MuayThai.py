import pandas as pd
import numpy as np
import cv2
import mediapipe as mp

class MuayThai:
    def __init__(self, data, step, true_steps, cal_steps):
        self.data = data
        self.step = step
        self.true_steps = true_steps
        self.cal_steps = cal_steps

    def get_data_size(self):
        return len(self.data)

    def cal_angle_xy(self, threshold, body1, body2, body3):
        a = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_x'.format(body1)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_y'.format(body1)]])
        b = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_x'.format(body2)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_y'.format(body2)]])
        c = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_x'.format(body3)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_y'.format(body3)]])

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = int(np.abs(radians * 180.0 / np.pi))
        if angle > 180:
            angle = 360 - angle

        return angle

    def cal_angle_yz(self, threshold, body1, body2, body3):
        a = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_z'.format(body1)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_y'.format(body1)]])
        b = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_z'.format(body2)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_y'.format(body2)]])
        c = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_z'.format(body3)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_y'.format(body3)]])

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = int(np.abs(radians * 180.0 / np.pi))
        if angle > 180:
            angle = 360 - angle

        return angle

    def cal_angle_xz(self, threshold, body1, body2, body3):
        a = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_x'.format(body1)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_z'.format(body1)]])
        b = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_x'.format(body2)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_z'.format(body2)]])
        c = np.array([self.data.loc[self.data['threshold'] == threshold, '{}_x'.format(body3)],
                      self.data.loc[self.data['threshold'] == threshold, '{}_z'.format(body3)]])

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = int(np.abs(radians * 180.0 / np.pi))
        if angle > 180:
            angle = 360 - angle

        return angle

    def find_angles_sub_step(self, step_data, threshold):
        angles = []
        for sub_step in range(1, len(step_data)+1):
            filt = (step_data['sub_step'] == sub_step)
            axis = step_data.loc[filt, 'axis'].iloc[0]

            if axis == 'xy':
                angles.append(self.cal_angle_xy(threshold, step_data.loc[filt, 'begin_node'].iloc[0],
                                step_data.loc[filt, 'main_node'].iloc[0],
                                step_data.loc[filt, 'end_node'].iloc[0]))
            elif axis == 'yz':
                angles.append(self.cal_angle_yz(threshold, step_data.loc[filt, 'begin_node'].iloc[0],
                                step_data.loc[filt, 'main_node'].iloc[0],
                                step_data.loc[filt, 'end_node'].iloc[0]))
            elif axis == 'xz':
                angles.append(self.cal_angle_xz(threshold, step_data.loc[filt, 'begin_node'].iloc[0],
                                step_data.loc[filt, 'main_node'].iloc[0],
                                step_data.loc[filt, 'end_node'].iloc[0]))
        return angles

    #return boolean
    def check_sub_step(self, ans_step_data, angles):
        checked_sub_step = 0
        for sub_step in range(1, len(ans_step_data)+1):
            filt = (ans_step_data['sub_step'] == sub_step)
            compared = eval('{} {} {}'.format(angles[sub_step-1], ans_step_data.loc[filt, 'operator'].iloc[0],
                                        ans_step_data.loc[filt, 'true_angle'].iloc[0]))
            #print(ans_step_data)
            if compared:
                checked_sub_step += 1
        return checked_sub_step == len(ans_step_data)

    def check(self):
        point = 0
        curr_step = 1
        thresholds = self.data['threshold'].tolist()
        step_correct = []

        for i in range(len(thresholds)):
            threshold = thresholds[i]
            all_angles = []

            #Find angles for every step
            for step in range(curr_step, self.step+1):
                curr_step_data = self.cal_steps[self.cal_steps['step'] == step]
                angle = self.find_angles_sub_step(curr_step_data, threshold)
                #print(angle)
                all_angles.append(angle)

            #print(all_angles)

            step_round = 0
            #Compare angles for every step
            for step in range(curr_step, self.step+1):
                curr_ans_step_data = self.true_steps[self.true_steps['step'] == step]
                if self.check_sub_step(curr_ans_step_data, all_angles[step_round]):
                    step_correct.append(threshold)
                    point += 1
                    curr_step = step+1
                    print('Frame: {}, True angle: {}'.format(int(threshold), all_angles[step_round]))
                    print('Current point: {}'.format(point))
                    break
                step_round += 1

            if point == self.step:
                break

        return point, step_correct

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

                    if threshold % diff == 0:
                        #cv2.imshow('Mediapipe Feed', img)
                        results_list.append(results)

                    if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                        break
                else:
                    break

            cap.release()
            cv2.destroyAllWindows()
            
        return results_list

    def show_true_graph(self, landmarks, true_answer_index):
        for i in range(len(true_answer_index)):
            mp_drawing.plot_landmarks(landmarks[true_answer_index[i]].pose_landmarks, mp_pose.POSE_CONNECTIONS, elevation=0, azimuth=0)
