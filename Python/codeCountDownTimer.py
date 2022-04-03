import time 
def timer():
    list1=[]
    """insert code here"""
    a=2
    b=2
    c=a+b
    print(c)
    start= time.perf_counter()
    for i in range(10000000):
        list1.append(i**2)
    end = time.perf_counter()
    return f'Code Run Time is {end - start:0.2f} seconds'
if __name__=="__main__":
    print(timer())