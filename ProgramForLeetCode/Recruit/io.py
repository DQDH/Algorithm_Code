'''
company：Huawei
date: 2019/8/29
title: 输入接口
details: 未知输入行数时的接口
intro: io装饰器（try except实现）io2 读取所有输入
'''


def io(func):
    def wrapper():
        while True:
            try:
                line = list(map(int, input().split(' ')))
                print(func(line))
            except:
                exit(0)
    return wrapper


def io2():
    line = input()
    lines = []
    while line:
        lines.append(line)
        line = input()
    return lines


@io
def test(line):
    print('test')
    return line


if __name__ == '__main__':
    test()