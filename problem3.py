def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1

a = int(input("자연수 입력:"))

print("입력받은 자연수까지의 곱은:%d" % factorial(a))