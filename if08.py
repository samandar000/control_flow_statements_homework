def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 9 and a < 100:
        answer ='two-digit '
    if a > 99 and a < 1000:
        answer ='three-digit '  
    
    if a%2 == 0:
        answer += 'even number'
    else:
        answer += 'odd number'
    
    return answer
print(main(445))