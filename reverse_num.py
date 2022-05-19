def reverseNum(n):
  # function that reverses the digits of a number
    rev_num = 0
    while n > 0:
        rev_num *= rev_num + n%10
        n = n//10
    return rev_num
    
