"""
課題A-6: N面サイコロの反復試行
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること
実行例
サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
"""
import random


def main():
    # 入力
    N = input("サイコロの面の数は")
    M = input("何回振りますか")
    # 計算
    dice_line = []
    for i in range(int(M)):
        dice_line.append(random.randint(1, int(N)))
    # 出力
    print(dice_line)



if __name__ == '__main__':
    main()
