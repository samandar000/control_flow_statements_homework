def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    x1=a//10
    x2=a%10
    x3=x2*10
    x4=x1+x3
    if x3 <= a:
        return 'True'
    else:  
        a < x3
        return 'False'


print(main(22))