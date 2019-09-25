"""
課題A-5:基本統計量の計算
スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
合計値
最大値
最小値
平均値
ただし、組み込み関数やライブラリは使わないこと(sum()やnp.mean()など)
1つの統計量につき、それ専用の関数を実装すること
実行例
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6.75
"""


def main():
    # 入力
    input_data = input("データを入力してください(スペース区切り) >")

    # 計算
    separate_list = input_data.split()
    # 合計
    # 最大値
    # 最小値
    # 平均値
    add_number = 0
    max_number = -99999
    min_number = 99999
    for i in separate_list:
        add_number += int(i)
        if max_number < int(i):
            max_number = int(i)
        if min_number > int(i):
            min_number = int(i)
    average_number = add_number / (len(separate_list))

    # 出力
    print(f'合計値：{add_number}')
    print(f'最大値：{max_number}')
    print(f'最小値：{min_number}')
    print(f'平均値：{average_number}')


if __name__ == '__main__':
    main()
