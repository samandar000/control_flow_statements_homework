def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    if a > 0:
        x1=1
    else:
        x1=0
    if b > 0:
        x2=1

    else:
        x2=0
    if c > 0:
        x3=1
    else:
        x3=0
        
    if x1+x2+x3 > 1:
        return 'there are a lot of positive numbers'
    else:
        return 'there are a lot of negative numbers'

print(main(-2,-5,2))