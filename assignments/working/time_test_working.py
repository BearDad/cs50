import time
from working import convert

start_time = time.time()
convert("9 AM to 10 PM")


end_time = time.time()
elapsed_time = end_time - start_time
print(f"script took {elapsed_time} seconds to run")
