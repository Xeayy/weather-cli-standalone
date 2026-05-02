# 天气查询命令行工具 + Web 界面

一个支持中文/拼音城市名的天气查询工具，提供命令行和 Web 两种使用方式。

## 功能

- 输入城市名（中文或拼音），自动转换为拼音查询实时天气
- 显示：温度、体感温度、湿度、天气描述
- 自动保存查询日志到 `weather_log.txt`
- 支持循环查询（命令行版）
- Web 界面采用两栏布局，查询结果显示在右侧
- Web 版支持查询历史（侧边栏），可清空历史

## 安装依赖

```bash
pip install requests pypinyin streamlit
```

## 使用方式

命令行版本：
bash
python main.py

Web 版本：
bash
streamlit run web/app.py
然后在浏览器中打开 http://localhost:8501



## 技术栈
Python 3.12

requests（HTTP 请求）

pypinyin（中文转拼音）

streamlit（Web 界面）