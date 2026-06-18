import os

import requests
from dotenv import load_dotenv
from langchain.tools import tool

@tool
def getWeather(city: str) -> str:
        """
        查看指定地点的当前天气情况。
        当用户询问某个城市或地点的天气、气温、风力等信息时调用此工具。

        Args:
            city: 城市名称，如"北京"、"成都"

        Returns:
            包含温度、天气、风力等信息的字符串
        """
        gaode_api_key = os.getenv("GAODE_API_KEY")  

        if not gaode_api_key:
            return "错误：未找到高德地图 API Key"

        weather_url = "https://restapi.amap.com/v3/weather/weatherInfo"
        weather_params = {
            "city": city,
            "key": gaode_api_key,
            "extensions": "base"
        }

        try:
            weather_response = requests.get(weather_url, params=weather_params, timeout=5)
            weather_data = weather_response.json()

            if weather_data.get("status") == "1" and weather_data.get("lives"):
                live = weather_data["lives"][0]  # lives 是列表，取第一个
                return (
                    f"{city}当前天气：{live['weather']}，"
                    f"温度{live['temperature']}"
                    f"湿度{live['humidity']}"
                    f"风向{live['winddirection']}，风力{live['windpower']}级，"
                    f"发布时间：{live['reporttime']}"
                )
            else:
                return f"无法获取'{city}'的天气信息"

        except Exception as e:
            return f"查询天气时出错：{str(e)}"

