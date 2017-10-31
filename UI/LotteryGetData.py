
#python3.5
from urllib import    request, parse
import json
import datetime

class LotteryGetData: 
    def __init__(self, code):
        self.code = code
        

    def getData(self):
        time = datetime.datetime.now()
        showapi_appid="48405"  #替换此值
        showapi_sign="6b0c9a848a88464f90a5171fc1618559"   #替换此值
        url="http://route.showapi.com/44-2"
        send_data = parse.urlencode([
            ('showapi_appid', showapi_appid)
            ,('showapi_sign', showapi_sign)
                            ,('code', self.code)
                            ,('endTime', time)
                            ,('count', "20")
            
        ])
        
        req = request.Request(url)
        try:
            response = request.urlopen(req, data=send_data.encode('utf-8'), timeout = 10) # 10秒超时反馈
        except Exception as e:
            print(e)
        result = response.read().decode('utf-8')
        result_json = json.loads(result)

        result_final = []
        for re in result_json['showapi_res_body']['result']:
            final = [
                re['expect'],
                re['openCode'],
                re['time'],
                                
                
            ]
            result_final.append(final)
        return result_final
        

#result_final = LotteryGetData("dlt").getData()
#print(result_final[2])

