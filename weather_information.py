"""
課題A-4: 天気情報の分析
要件
3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
このデータを使って3つの問を満たす実装をしてください
def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)


if __name__ == '__main__':
    main()
"""


def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # 出力
    temperature_add = 0
    i = 0

    # for weather_list in weather_information:
    #     #     temperature_add += weather_list['temperature']
    #     #     i += 1
    #     #
    #     # print(temperature_add / i)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # 出力
    # list_osaka_station = []
    #
    # for weather_list2 in weather_information:
    #     if weather_list2['prefecture'] == '大阪府':
    #         list_osaka_station.append(weather_list2['station'])
    #
    # stationlist_join = ",".join(list_osaka_station)
    #
    # print(stationlist_join)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)

    # 計算
    hukuoka_temperature = 0
    i = 0
    for weather_list3 in weather_information:
        if weather_list3['prefecture'] == '福岡県':
            i += 1
            hukuoka_temperature += weather_list3['temperature']

    # 出力
    print(hukuoka_temperature / i)


if __name__ == '__main__':
    main()
