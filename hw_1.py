n = int(input("請輸入數字的個數:"))
number = input("請輸入數字組:").split()
while len(number) > n:
    number = input("請輸入數字組:").split()
number_reverse = number[::-1]
for x in number_reverse:
    print(x, end=" ")