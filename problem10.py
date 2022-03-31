import random
qt = 0
tr = 0
ans = 0
while (qt != "T"):
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    ans1 = input(" {} X {} 는?" .format (n1, n2))
    ans2 = n1 * n2
    tr += 1
    if int(ans1) == ans2:
        ans += 1
    qt = input("나가려면 T를 입력하시오.")
percent = ans / tr * 100
print("정답률은 {} 입니다.".format(percent))