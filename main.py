import time

def store_in_dic_for(dic):
    def wrapper(func, n):
        if n < 0: return 0
        if n not in dic:
            try: dic[n] = func(n)
            except RecursionError:
                if dic: nn = max(dic.keys())
                else: nn = 0
                for i in range(nn+1, n+1):
                    dic[i] = func(i)
        return dic[n]
    return lambda func: lambda n: wrapper(func, n)

def store_in_dic(dic):
    def wrapper(func, n):
        if n < 0: return 0
        if n not in dic:
            try: dic[n] = func(n)
            except RecursionError:
                if dic: nn = max(dic.keys())
                else: nn = 0
                while nn <= n:
                    dic[nn] = func(nn)
                    nn += 1
        return dic[n]
    return lambda func: lambda n: wrapper(func, n)

main_dic = {}
@store_in_dic(main_dic)
def main(n):
    if n < 0: return 0
    elif n == 0: return 1
    return sum(foo(i, main(n-seq(i))) for i in range(n))

def foo(idx, a):
    match idx % 4:
        case 0|1: return a
        case 2|3: return -a

seq_dic = {}
@store_in_dic(seq_dic)
def seq(n):
    if n < 0: return 0
    if n == 0: return 1
    return seq(n-1)+diff(n-1)

def diff(n):
    if n < 0: return 0

    # 1, 2, 3, 4, 5...part
    if n % 2 == 0: return n // 2 + 1
    # 3, 7, 11, 13... part
    elif n % 2 == 1: return n + 2
        
# def assert_main(n, a):
    # assert main(n) == a, f"expect {a}, got {main(n)}."

# li = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135]
# for idx, l in enumerate(li):
#     assert_main(idx, l)
# print(main(500))
# print(main_dic)
# s = time.process_time_ns()
main(6676)
# e = time.process_time_ns()
# print(seq(6678))
# print(seq_dic)
# print(e-s)
#
# assert seq(0) == 1
# assert seq(1) == 2
# assert seq(2) == 5
# assert seq(3) == 7
# assert seq(4) == 12
#
# assert diff(0) == 1
# assert diff(2) == 2
# assert diff(4) == 3
# assert diff(6) == 4
# # print(diff(1))
# assert diff(1) == 3
# assert diff(3) == 5
# assert diff(5) == 7
# assert diff(7) == 9
# assert diff(9) == 11

