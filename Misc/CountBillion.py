import time

start_time = time.time()

# Count to 1 billion
for i in range(1000000000):
    pass

end_time = time.time()
time_taken = (end_time - start_time) * 1000  # Convert to milliseconds

print("Time taken to count to 1 billion: %.2f milliseconds" % time_taken)
