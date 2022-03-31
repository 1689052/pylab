n = int(input("온도 입력:"))
convert = input("c or f")

tc = (9/5) * n + 32
tf = (5/9) * (n -32)

if (convert == "c"):
    print("화씨온도:%d" % tc)
elif (convert =="f"):
    print("섭씨온도:%d" % tf)