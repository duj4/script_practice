import argparse
'''
Hypothetical command-line tool for searching a collection of files for one or more text patterns.
'''
# 为了解析命令行选项，你首先要创建一个 ArgumentParser 实例， 并使用 add_argument() 方法声明你想要支持的选项
parser = argparse.ArgumentParser(description='Search some files')

# dest 指定解析结果被指派给属性的名字
# metavar 被用来生成帮助信息
# action 指定跟属性对应的处理逻辑, 通常的值为store, 被用来存储某个值或将多个参数值收集到一个列表中
parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-p', '--pat', metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text pattern to search for')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store', help='output file')
parser.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'}, default='slow', help='search speed')

args = parser.parse_args()

print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)