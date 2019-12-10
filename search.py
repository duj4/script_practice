import argparse
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p03_parsing_command_line_options.html
'''
Hypothetical command-line tool for searching a collection of files for one or more text patterns.
'''
# 为了解析命令行选项，你首先要创建一个 ArgumentParser 实例， 并使用 add_argument() 方法声明你想要支持的选项
parser = argparse.ArgumentParser(description='A Python-MySQL client')

# dest 指定解析结果被指派给属性的名字
# metavar 被用来生成帮助信息
# action 指定跟属性对应的处理逻辑, 通常的值为store, 被用来存储某个值或将多个参数值收集到一个列表中
# nargs 参数的个数，可以是具体的数字，或者是+与*，+表示1个或多个，*表示0个或多个
parser.add_argument('--host', action='store', dest='host', required=True, help='connect to host')
parser.add_argument('-u', '--user', action='store', dest='user', required=True, help='user to login')
parser.add_argument('-p', '--password', action='store', dest='password', required=True, help='password to use when connecting to server')
parser.add_argument('-P', '--port', action='store', dest='port', default=3306, type=int, help='port number to use for connection or 3306 for default')

args = parser.parse_args()

print(args.host)
print(args.user)
print(args.password)
print(args.port)