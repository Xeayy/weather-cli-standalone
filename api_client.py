import requests
import json

def fetch_weather(city):
    # 根据城市名返回天气数据（JSON解析后的字典）
    url = f'https://wttr.in/{city}?format=j1'   # j1 表示返回 JSON格式
    try:
        # 发送 GET 请求，最多等10秒
        response = requests.get(url, timeout=10)
        # 如果状态码不是 200 （如 404），会抛出HTTPError
        response.raise_for_status()
        # 把返回的 JSON 字符串转成 Python 字典/列表
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        raise Exception('网络超时，请检查连接后重试')
    except requests.exceptions.HTTPError as e:
        # e.response.status_code 是具体的错误码 （如404）
        raise Exception(f'HTTP错误 {e.response.status_code}: 城市名可能无效')
    except json.JSONDecodeError:
        raise Exception('服务器返回了非JSON数据，请稍后重试')
    except requests.exceptions.RequestException as e:
        raise Exception(f'网络请求失败：{e}')
