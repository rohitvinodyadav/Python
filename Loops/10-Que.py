# Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

maxAttempts = 5
waitTime = 1
attempts = 0

while attempts < maxAttempts:
    print("No. of Attempts :: ",attempts+1, " Wait time :: ", waitTime)
    time.sleep(waitTime)
    waitTime = waitTime * 2
    attempts = attempts + 1
