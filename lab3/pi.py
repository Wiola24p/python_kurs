import matplotlib.pyplot as plt
import random
import math

def approximate_pi():
    times = 100
    counter=0
    for _ in range(times):
        x =random.uniform(-1,1)
        y =random.uniform(-1,1)

        if math.sqrt(x**2+y**2)<=1:
            counter+=1
`plt.show()
    return 4*(counter/times)