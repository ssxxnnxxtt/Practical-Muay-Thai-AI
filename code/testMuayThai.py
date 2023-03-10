import pandas as pd
import numpy as np
from MuayThai import MuayThai as M

### Step 6
true_steps = pd.DataFrame([{'step': 1, 'sub_step': 1, 'main_node': '14', 'true_angle': 90, 'operator': '<'},
{'step': 1, 'sub_step': 2, 'main_node': '13', 'true_angle': 90, 'operator': '<'},
{'step': 2, 'sub_step': 1, 'main_node': '23', 'true_angle': 90, 'operator': '<'},
{'step': 3, 'sub_step': 1, 'main_node': '13', 'true_angle': 125, 'operator': '<='},
{'step': 3, 'sub_step': 2, 'main_node': '11', 'true_angle': 80, 'operator': '>'},
{'step': 3, 'sub_step': 3, 'main_node': '14', 'true_angle': 90, 'operator': '<='},
{'step': 3, 'sub_step': 4, 'main_node': '12', 'true_angle': 90, 'operator': '<'},
{'step': 4, 'sub_step': 1, 'main_node': '14', 'true_angle': 90, 'operator': '>'},
{'step': 4, 'sub_step': 2, 'main_node': '12', 'true_angle': 90, 'operator': '>'}])


cal_steps = pd.DataFrame([{'step': 1, 'sub_step': 1, 'begin_node': '12', 'main_node': '14', 'end_node': '16' , 'axis': 'xy'},
{'step': 1, 'sub_step': 2, 'begin_node': '11', 'main_node': '13', 'end_node': '15' , 'axis': 'xy'},
{'step': 2, 'sub_step': 1, 'begin_node': '24', 'main_node': '23', 'end_node': '25' , 'axis': 'yz'},
{'step': 3, 'sub_step': 1, 'begin_node': '11', 'main_node': '13', 'end_node': '15' , 'axis': 'xy'},
{'step': 3, 'sub_step': 2, 'begin_node': '13', 'main_node': '11', 'end_node': '23' , 'axis': 'yz'},
{'step': 3, 'sub_step': 3, 'begin_node': '12', 'main_node': '14', 'end_node': '22' , 'axis': 'xy'},
{'step': 3, 'sub_step': 4, 'begin_node': '14', 'main_node': '12', 'end_node': '24' , 'axis': 'xy'},
{'step': 4, 'sub_step': 1, 'begin_node': '12', 'main_node': '14', 'end_node': '16' , 'axis': 'xy'},
{'step': 4, 'sub_step': 2, 'begin_node': '14', 'main_node': '12', 'end_node': '24' , 'axis': 'yz'}])

'''
### Step 7
true_steps = pd.DataFrame([{'step': 1, 'sub_step': 1, 'main_node': '14', 'true_angle': 90, 'operator': '<'},
{'step': 1, 'sub_step': 2, 'main_node': '13', 'true_angle': 90, 'operator': '<'},
{'step': 2, 'sub_step': 1, 'main_node': '12', 'true_angle': 75, 'operator': '>'},
{'step': 2, 'sub_step': 2, 'main_node': '14', 'true_angle': 130, 'operator': '>='},
{'step': 3, 'sub_step': 1, 'main_node': '24', 'true_angle': 15, 'operator': '<'},
{'step': 3, 'sub_step': 2, 'main_node': '12', 'true_angle': 80, 'operator': '<'},
{'step': 4, 'sub_step': 1, 'main_node': '24', 'true_angle': 15, 'operator': '<'}])


cal_steps = pd.DataFrame([{'step': 1, 'sub_step': 1, 'begin_node': '12', 'main_node': '14', 'end_node': '16' , 'axis': 'xy'},
{'step': 1, 'sub_step': 2, 'begin_node': '11', 'main_node': '13', 'end_node': '15' , 'axis': 'xy'},
{'step': 2, 'sub_step': 1, 'begin_node': '14', 'main_node': '12', 'end_node': '24' , 'axis': 'yz'},
{'step': 2, 'sub_step': 2, 'begin_node': '12', 'main_node': '14', 'end_node': '16' , 'axis': 'yz'},
{'step': 3, 'sub_step': 1, 'begin_node': '12', 'main_node': '24', 'end_node': '26' , 'axis': 'xy'},
{'step': 3, 'sub_step': 2, 'begin_node': '14', 'main_node': '12', 'end_node': '24' , 'axis': 'yz'},
{'step': 4, 'sub_step': 1, 'begin_node': '12', 'main_node': '24', 'end_node': '26' , 'axis': 'xy'}])
'''

'''
### Step 15
true_steps = pd.DataFrame([{'step': 1, 'sub_step': 1, 'main_node': '14', 'true_angle': 90, 'operator': '<'},
{'step': 1, 'sub_step': 2, 'main_node': '13', 'true_angle': 90, 'operator': '<'},
{'step': 2, 'sub_step': 1, 'main_node': '14', 'true_angle': 90, 'operator': '>'},
{'step': 2, 'sub_step': 2, 'main_node': '12', 'true_angle': 90, 'operator': '>'},
{'step': 2, 'sub_step': 3, 'main_node': '23', 'true_angle': 90, 'operator': '<'},
{'step': 3, 'sub_step': 1, 'main_node': '11', 'true_angle': 90, 'operator': '>'},
{'step': 3, 'sub_step': 2, 'main_node': '13', 'true_angle': 90, 'operator': '>'},
{'step': 4, 'sub_step': 1, 'main_node': '24', 'true_angle': 90, 'operator': '<'},
{'step': 4, 'sub_step': 2, 'main_node': '26', 'true_angle': 90, 'operator': '<'},
{'step': 4, 'sub_step': 3, 'main_node': '12', 'true_angle': 90, 'operator': '<'},
{'step': 4, 'sub_step': 4, 'main_node': '11', 'true_angle': 90, 'operator': '<'},
{'step': 4, 'sub_step': 5, 'main_node': '14', 'true_angle': 100, 'operator': '<'},
{'step': 4, 'sub_step': 6, 'main_node': '13', 'true_angle': 90, 'operator': '<'}])


cal_steps = pd.DataFrame([{'step': 1, 'sub_step': 1, 'begin_node': '12', 'main_node': '14', 'end_node': '16' , 'axis': 'xy'},
{'step': 1, 'sub_step': 2, 'begin_node': '11', 'main_node': '13', 'end_node': '15' , 'axis': 'xy'},
{'step': 2, 'sub_step': 1, 'begin_node': '12', 'main_node': '14', 'end_node': '16' , 'axis': 'yz'},
{'step': 2, 'sub_step': 2, 'begin_node': '14', 'main_node': '12', 'end_node': '24' , 'axis': 'yz'},
{'step': 2, 'sub_step': 3, 'begin_node': '24', 'main_node': '23', 'end_node': '25' , 'axis': 'yz'},
{'step': 3, 'sub_step': 1, 'begin_node': '13', 'main_node': '11', 'end_node': '23' , 'axis': 'yz'},
{'step': 3, 'sub_step': 2, 'begin_node': '11', 'main_node': '13', 'end_node': '15' , 'axis': 'yz'},
{'step': 4, 'sub_step': 1, 'begin_node': '12', 'main_node': '24', 'end_node': '26' , 'axis': 'xy'},
{'step': 4, 'sub_step': 2, 'begin_node': '24', 'main_node': '26', 'end_node': '28' , 'axis': 'yz'},
{'step': 4, 'sub_step': 3, 'begin_node': '14', 'main_node': '12', 'end_node': '24' , 'axis': 'xy'},
{'step': 4, 'sub_step': 4, 'begin_node': '13', 'main_node': '11', 'end_node': '23' , 'axis': 'xy'},
{'step': 4, 'sub_step': 5, 'begin_node': '12', 'main_node': '14', 'end_node': '22' , 'axis': 'xy'},
{'step': 4, 'sub_step': 6, 'begin_node': '11', 'main_node': '13', 'end_node': '15' , 'axis': 'xy'}])
'''

clip_number = 4

df = pd.read_csv('../video/test_csv/test.csv')
del df['Unnamed: 0']

#clip_df = df[df['clip_name'] == '15_{}'.format(clip_number)]
clip_df = df

m = M(clip_df, 4, true_steps, cal_steps)
#print(m.get_data_size())
point, true_step_frame = m.check()
print(point)
print(true_step_frame)
