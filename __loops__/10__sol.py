# Exponential backoff
import time
# time is in seconds
wait_time = 1
max_retries  = 5
attempts = 0

while attempts<max_retries:
    print("Attempt",attempts+1,"Wait time is ",wait_time,"seconds")
    time.sleep(wait_time)
    # it means system will sleep/delay execution for 1 sec
    wait_time *= 2
    attempts += 1