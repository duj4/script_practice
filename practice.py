import os
import glob
from fnmatch import fnmatch
import time


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
# with open('./test.txt', 'x') as f:
#     f.write('HOLA TOTDOS!\n')

# 打印链接的source路径
print(os.path.realpath('/usr/bin/python'))

# glob和fnmatch可以用于文件名匹配
pyfiles_1 = glob.glob('/root/code/*.txt')
print(pyfiles_1)
pyfiles_2 = [name for name in os.listdir('/root/code/') if fnmatch(name, '*.txt')]
print(pyfiles_2)

# get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles_1]
for name, size, mtime in name_sz_date:
    print(name, size, time.ctime(mtime))

# alternative: get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles_1]
for name, meta in file_metadata:
    print(name, meta.st_size, time.ctime(meta.st_mtime))

# 创建匿名临时文件
from tempfile import TemporaryFile
# 创建可命名临时文件
from tempfile import NamedTemporaryFile
with NamedTemporaryFile('w') as f:
    print('temp file name is: ', f.name)
# 创建临时目录
from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is: ', dirname)

# 终止程序并给出错误信息
# raise SystemExit('It failed!')

# 获得终端大小
sz = os.get_terminal_size()
print(sz.columns)
print(sz.lines)

# 执行外部命令并获取它的输出
import subprocess
out_bytes = subprocess.check_output(['netstat', '-tlnp']).decode('utf-8') # 以文本形式返回则需要进行解码
print(out_bytes)

# 接受用户输入，在指定目录下查找指定文件
def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            # os.path.abspath() ,它接受一个路径，可能是相对路径，最后返回绝对路径
            # os.path.normpath() ，用来返回正常路径，可以解决双斜杆、对目录的多重引用的问题等
            print(os.path.normpath(os.path.abspath(full_path)))