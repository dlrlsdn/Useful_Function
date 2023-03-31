# 연속적인 숫자 list를 만들 때 사용하는 함수

print('function == mkf, mki')
print('list = [] \ninterval == float 또는 int')
print('### function(start, interval, list, width) ###')
import math


def mkf(start, interval, list_f, width):
    for k in range(0, width):
        list_f = list_f + [start + (interval * k)]

    if format(interval, 'f')[-2] == 1:
        for kk in range(0, width):
            list_f = list_f + [round(list_f[0], int(-math.log10(interval)))]
            list_f.pop(0)
    else:
        for kk in range(0, width):
            list_f = list_f + [round(list_f[0], int(-math.log10(interval)) + 1)]
            list_f.pop(0)

    return list_f


def mki(start, interval, list_i, width):
    for k in range(0, width):
        list_i = list_i + [start + (interval * k)]

    for kk in range(0, width):
        list_i = list_i + [round(list_i[0])]
        list_i.pop(0)

    return list_i
