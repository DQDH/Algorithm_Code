def min_num(money_used):
    money_now = 1024 - money_used
    num1 = int(money_now/64)
    money_temp1 = money_now % 64
    num2 = int(money_temp1/16)
    money_temp2 = money_temp1 % 16
    num3 = int(money_temp2/4)
    money_temp3 = money_temp2 % 4
    num4 = money_temp3
    num = num1 + num2 + num3 + num4
    return num
if __name__ == "__main__":
    money_used = int(input())
    num = min_num(money_used)
    print(num)