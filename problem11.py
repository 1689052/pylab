import sys

fileName = input("파일이름 입력")
accessMode = "r"
try:
    myFile = open(fileName, 'r')
except FileNotFoundError as e:
    print(e)
    print('파일이 없습니다.'.center(30, '*'))

line_num = 1
line = myFile.readline()

while line:
    print('%d %s'%(line_num, line))
    line = myFile.readline()
    line_num += 1
myFile.close