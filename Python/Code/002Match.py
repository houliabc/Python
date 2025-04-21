# -*- encoding = utf-8 -*-
# author : houliabc

age = 15

match age:
    case x if x < 10:  #age<10时成立，且赋值给x
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:   #匹配多个值
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:  #匹配任意值，类似于c语言中的else
        print('not sure.')
print(x)

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，打印报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:   #表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
