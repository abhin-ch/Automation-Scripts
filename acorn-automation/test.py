import time 
import datetime

def time_sec(tim):
    tim = tim.strip()
    # Get the current Time 
    current_time = datetime.datetime.now()
    # Get the entered Time 
    entered_time = datetime.datetime.strptime(tim, '%b %d %Y %I:%M%p')
    print(entered_time)

    time_diff = entered_time - current_time
    seconds = time_diff.total_seconds()
    print(seconds)
    return seconds

a = time_sec(' Jul 27 2020 11:13PM ')
time.sleep(a)
print("OKay time done now ")