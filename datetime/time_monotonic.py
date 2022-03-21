import time


start_time = time.monotonic()

time.sleep(5)

print(f'{time.monotonic() - start_time} seconds left')
