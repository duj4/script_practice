import os

# Python可以识别所有的普通换行符并将其转换为单个 \n 字符
# 若不希望这种处理方式，则需要传入newline=''
# 默认输出"Beautiful is better than ugly.\nExplicit is better than implicit.\n"
# 加了newline='', "Beautiful is better than ugly.\r\nExplicit is better than implicit.\r\n"
# 当前被读取的文件的最后一行时西班牙语，所以要指定latin-1的解码方式才可以正确打开
with open('./TheZenOfPython.txt', 'r', encoding='latin-1', newline='') as f:
    for line in f:
        print(line)

# 将内容打印到指定文件中
print('\n')
with open('./test.txt', 'w') as f:
    print("HELLO WORLD!", file=f)

# print中的不同分隔符
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')
print(','.join(('ACME', '50', '91.5'))) #仅能用于字符串
row = ('ACME', 50, 91.5)
print(*row, sep=',') #print(','.join(row))会报错“TypeError: sequence item 1: expected str instance, int found”

# print中禁止换行
for i in range(5):
    print(i, end=' ')
print('\n')

# x模式会在写入的时候检测目标文件是否已经存在，若存在，则抛出异常，而不是像w模式一样直接覆盖已有的文件
with open('./test.txt', 'x') as f:
    f.write('HOLA TOTDOS!\n')