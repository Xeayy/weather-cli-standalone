import os
from pypinyin import lazy_pinyin
from datetime import datetime
from api_client import fetch_weather
from formatter import format_weather

script_dir = os.path.dirname(__file__)
log_file_path = os.path.join(script_dir, 'weather_log.txt')

while True:
    city = input('请输入城市名：')

    # 测试拼音转换
    city_pinyin = ''.join(lazy_pinyin(city))

    try:
        now = datetime.now()
        now_str = now.strftime('%Y-%m-%d %H:%M:%S')
        print(f'当前时间：{now_str}')

        # 1. 从 API 获取原始数据
        data = fetch_weather(city_pinyin)
        # 2. 格式化成好看的字符串
        result = format_weather(data,city)
        # 3. 输出
        print(result)

        with open(log_file_path, 'a', encoding='utf-8') as f:
            f.write(f'{now_str} | {city} | {result}\n')

        choice = input('是否继续查询?(y/n):')
        if choice.lower() != 'y':
            break

    except Exception as e:
        # 任何错误都被捕获，打印提示，程序不崩溃
        print(f'查询失败:{e}')
        choice = input('是否继续查询？(y/n):')
        if choice.lower() != 'y':
            break



