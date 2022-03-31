a = list(map(int,input("띄워쓰기를 하여 숫자 3개를 입력:").split()))
b = list(map(int,input("띄워쓰기를 하여 숫자 3개를 입력:").split()))

multi_list = [a[i] * b[i] for i in range(len(a))]
result = sum(multi_list)

print(a)
print(b)
print(result)