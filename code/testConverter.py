from Converter import Conveter
import pandas as pd

c = Conveter('../video/test_clip', '../video/test_csv')
clip_df = c.convert_video_to_node()
c.write_video_node_to_csv(clip_df, 'test.csv')