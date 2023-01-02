#!/usr/bin/env python3
# coding: utf-8


import random


ZODIAC_SIGN = ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座',
               '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座']
JAPANESE_ZODIAC = ['子年', '丑年', '寅年', '卯年', '辰年', '巳年',
                   '午年', '未年', '申年', '酉年', '戌年', '亥年']
BLOOD_TYPE = ['A型', 'B型', 'O型', 'AB型']


def main():
    l = []
    for zs in ZODIAC_SIGN:
        for jz in JAPANESE_ZODIAC:
            for bt in BLOOD_TYPE:
                l.append(zs + ' ✖ ' + jz + ' ✖ ' + bt)

    l_random = random.sample(l, len(l))

    count = 0
    for i in range(len(l_random)):
        count += 1
        print('{0:<6} {1}'.format('第' + str(count) + '位:', l_random[i]))


if __name__ == '__main__':
    main()
