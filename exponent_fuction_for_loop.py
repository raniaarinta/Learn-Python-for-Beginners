def raise_to_power(base_num, power_num):
    temp=1
    for index in range (power_num):
        temp =temp * base_num
    return temp
print(raise_to_power(3.14,2))