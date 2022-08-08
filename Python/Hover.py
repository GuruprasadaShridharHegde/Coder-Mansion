
def myaddFunction(a: int, b: int, c=0) -> int:
    '''
    this function adds two numbers

    # syntax
    - def `myaddFunction(a: int, b: int) -> int`:
    - def myaddFunction(a: int, b: int, c=0) -> int:

    ## examples
    - myaddFunction(1, 2)=3
    - myaddFunction(1, 2, 3)=6


    @param a: `first number`
    @param b: second number
    @param c[optional]: third number default =0
    @return: sum of a and b
        '''
    return a+b+c


x = myaddFunction(1, 2)
