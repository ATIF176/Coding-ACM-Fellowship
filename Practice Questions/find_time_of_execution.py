import time

n = 5
def FindTime():
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s += 1
    end_time = time.time()
    return s, start_time-end_time


print("\n<--------------------------------------->")
iterations, tim = FindTime()
print("Time of execution for", iterations, "iterations is", tim)
print("<--------------------------------------->")