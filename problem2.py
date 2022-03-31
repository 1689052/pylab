n = int(input("정수 입력:"))
sum = 0

for i in range(1, n+1):
        if(i % 2 ==0):
            sum += 1

print("입력받은 정수중 짝수의 합은:", sum)