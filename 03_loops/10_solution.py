import time

wait_time = 1
max_retries = 5
attempts = 0

while(max_retries):
    print(f'''
          Attempts: {attempts + 1} 
          wait Time = {wait_time}
          ''')
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

    max_retries -= 1