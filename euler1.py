import numpy as np

listnum = np.arange(1,1001)
multiples = []

for num in listnum:
    if num % 3 ==0 or num % 5 == 0: 
        multiples.append(num)

sum(multiples)
