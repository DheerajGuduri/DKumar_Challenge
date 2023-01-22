import re

credit_numbers = int(input())

num = 0

while num in range(credit_numbers):
    num = num +1
    credit_num = input().strip()
    to_sub = '-'
    remove_hyphen = re.sub(to_sub, '',credit_num)
    
    valid = True
    
    check_length16 = bool(re.match(r'^[4-6]\d{15}$',credit_num))
    check_length19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit_num))    
    repeated_digits = bool(re.findall(r'(?=(\d)\1\1\1)',remove_hyphen))
    
    while check_length16 == True or check_length19 == True:
        if repeated_digits == True:
            valid=False
        break
        
    while check_length16 == False and check_length19 == False:
        valid = False  
        break
         
    if valid == True:
        print('Valid')
    else:
        print('Invalid')
