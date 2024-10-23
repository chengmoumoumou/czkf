import requests
import json
def weather(cityname):
    key='1c9e474cbd03092f5bea1a3199d781fa'
    api='http://apis.juhe.cn/simpleWeather/query'
    params= {
    'key': '1c9e474cbd03092f5bea1a3199d781fa',
    'city': cityname,
}

    response=requests.get(api,params=params)
    json_data = json.loads(response.text)

    print(json_data)
    result=json_data.get('result')
    realtime=result.get('realtime')
    weather_data=dict()
    weather_data['city']=cityname
    weather_data['temperature']=realtime.get('temperature')
    weather_data['info']=realtime.get('info')
    return weather_data
if __name__ == "__main__":

    data = weather('保定')
    print(data)# 确保 weather 函数已经定义或导入

