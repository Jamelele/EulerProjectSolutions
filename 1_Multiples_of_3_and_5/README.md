# Multiples of 3 and 5

## Problem
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Solution

    import time

    start = time.time()

    n = 1000
    k = 0

    for i in range(0, n, 3):
      print(i)
      k += i

    for i in range(0, n, 5):
      print(i)
      k += i

    for i in range(0, n, 15):
      k -= i

    end = time.time()

    print(end - start)

I used two for loops using the each multiple of 3 and 5 under 1000, I then took away the common multiples by finding the multiples of 15 and subtracting those.

## Answer
    233168
