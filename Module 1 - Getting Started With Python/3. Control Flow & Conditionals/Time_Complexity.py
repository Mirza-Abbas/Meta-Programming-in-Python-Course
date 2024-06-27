#Time Complexity of Nested Loops:

import time

start_time = time.time()

for i in range(100):  # Outer loop

    for j in range(100):  # Inner loop
        print(0, end=" ")
    print()

print("Time:", round(time.time() - start_time, 2), "seconds")