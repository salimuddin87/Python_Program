import datetime
import time


unixtimestamp = 1507126064
dt = datetime.datetime.fromtimestamp(unixtimestamp).strftime('%Y-%m-%d %H:%M:%S')
print(dt)  # '2017-10-04 07:07:44'

timestamp = datetime.datetime(2017, 12, 1, 0, 0).strftime('%s')
print(timestamp)  # 1512115200

date_time = '29.08.2011 11:05:02'
pattern = '%d.%m.%Y %H:%M:%S'
epoch = int(time.mktime(time.strptime(date_time, pattern)))
print(epoch)  # 1314641102
