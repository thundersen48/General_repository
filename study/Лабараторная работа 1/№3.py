import math

V= int(input())
H= int(input())

if H <= 350:
    Z = 0.85*V**0.1
else:
    Z = 0.925 * V**0.05
print(Z)
