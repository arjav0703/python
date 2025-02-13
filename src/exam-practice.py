import time
n = int(input('n: ' )) + 1 

time.sleep(1)
print('Thinking .........')
time.sleep(1.5)

for x in range (1, n):
    print(str(x) * x + '.' * x)
    time.sleep(0.5)
    


#    for y in range(0, x):
#        x = x +1
