def format_weather(data,city):
    """从天气JSON中提取温度和描述，返回可读字符串"""
    # wttr.in 返回的 JSON 结构：
    # { "current_condition": [ { "temp_C": "22", "weatherDesc": [{"value": "Sunny"}] } ] }
    current = data['current_condition'][0]
    temp = current['temp_C']                  # 温度（摄氏度）
    humidity = current['humidity']            # 湿度百分比（字符串）
    feels_like = current['FeelsLikeC']
    desc = current['weatherDesc'][0]['value'] # 天气描述（英文）
    return f'{city}当前温度：{temp}℃ ，体感：{feels_like}℃ ，湿度：{humidity}% ，天气：{desc}'