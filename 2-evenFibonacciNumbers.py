#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
a, b = 0,1
evenSum = 0;
while b < 4000000:
    if b%2==0:
      evenSum+=b
    a, b = b, a + b
print(evenSum) #4613732
