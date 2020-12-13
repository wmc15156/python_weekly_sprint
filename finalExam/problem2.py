from urllib.request import urlopen
from urllib.parse import urlencode,unquote,quote_plus
import urllib
import json
import xmltodict

from matplotlib import pyplot as plt
from decouple import config


def returnJson(url:str, 
                ServiceKey:str,
                pageNo:str,
                numOfRows:str, 
                startCreateDt:str,
                endCreateDt:str)->dict:
    """[입력 url과 ServiceKey를 입력받으면 해당 url에서 json으로 변경해주는 코드]

    Args:
        url (str): [서비스url]
        ServiceKey (str): [서비스키]
        pageNo (str): [페이지 번호]
        numOfRows (str): [한 페이지 결과 수]
        startCreateDt (str): [검색할 생성일 범위의 시작]
        endCreateDt (str): [검색할 생성일 범위의 종료]

    Returns:
        dict: [json변화 결과값]
    """
    queryParams = '?' + urlencode({ 
        quote_plus('ServiceKey') : ServiceKey,
        quote_plus('pageNo') : pageNo, 
        quote_plus('numOfRows') : numOfRows,
        quote_plus('startCreateDt') : startCreateDt, 
        quote_plus('endCreateDt') : endCreateDt 
        })

    request = urllib.request.Request(url+unquote(queryParams))
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    decoding = response_body.decode('utf-8')

    jsonString = json.dumps(xmltodict.parse(decoding), indent=4)
    return jsonString


if __name__ == "__main__":
    #URL주소
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
    #서비스키
    servicekey = config('SERVICE_KEY')
    res_json2 = returnJson(url=url,ServiceKey=servicekey,
                          pageNo=4,
                          numOfRows=4, 
                          startCreateDt='20200228',
                          endCreateDt='20200228')
    # '20200228'
    def collect_data(date):
        url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
        # 서비스키
        servicekey = '%2FscxPNvXBeFciJsfwzWT3NFrP9G2IJpzLdaHVsehrql2%2FK2e8%2FIzdzy5HtyArYryZ2WMCuvE2y65x79Aa3tnhw%3D%3D'
        result = returnJson(url=url, ServiceKey=servicekey,
                               pageNo=4,
                               numOfRows=4,
                               startCreateDt=date,
                               endCreateDt=date)
        result = json.loads(result)
        return result['response']['body']['items']['item']

    # 격리해제 수	CLEAR_CNT
    # 사망자 수	DEATH_CNT
    # 치료중 환자 수	CARE_CNT
    # 확진자 수	DECIDE_CNT

    result = {1: {"CLEAR_CNT": 1, "DEATH_CNT": 0, "CARE_CNT": 0, "DECIDE_CNT": 0},}

    def monthly_data(data, month):

        obj = {"CLEAR_CNT": "0","DEATH_CNT": 0, "CARE_CNT": 0, "DECIDE_CNT": 0}
        for value in data:
            if value == "clearCnt":
                obj["CLEAR_CNT"] = data[value]
            if value == "deathCnt":
                obj["DEATH_CNT"] = data[value]

            if value == "careCnt":
                obj["CARE_CNT"] = data[value]
            if value == "decideCnt":
                obj["DECIDE_CNT"] = data[value]

        result[month] = obj

    month_end = ["20200228", "20200331", "20200430", "20200531", "20200630", "20200731", "20200831", "20200930",
             "20201031", "20201130", "20201212"]
    month_start = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # month2 = collect_data('20200228')
    # monthly_data(month2, "02")

    for i, v in enumerate(month_end):
        data = collect_data(v)
        if str(type(data)) == "<class 'list'>":
            data = data[0]
        monthly_data(data, month_start[i])

    final_result = {"CLEAR_CNT": [1], "DEATH_CNT": [0], "CARE_CNT": [0], "DECIDE_CNT": [0]}

    print(result)

    for i, v in enumerate(result):
        if i > 0:

            current_month_clear_cnt = int(result[v]['CLEAR_CNT']) - int(result[v-1]['CLEAR_CNT'])
            final_result['CLEAR_CNT'].append(abs(current_month_clear_cnt))

            current_month_death_cnt = int(result[v]["DEATH_CNT"]) - int(result[v - 1]["DEATH_CNT"])
            final_result['DEATH_CNT'].append(abs(current_month_death_cnt))

            current_month_care_cnt = int(result[v]["CARE_CNT"]) - int(result[v - 1]["CARE_CNT"])
            final_result['CARE_CNT'].append(abs(current_month_care_cnt))

            current_month_decide_cnt = int(result[v]["DECIDE_CNT"]) - int(result[v - 1]["DECIDE_CNT"])
            final_result['DECIDE_CNT'].append(abs(current_month_decide_cnt))

    print(final_result)
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], final_result["CLEAR_CNT"])
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], final_result["DEATH_CNT"])
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], final_result["CARE_CNT"])
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], final_result["DECIDE_CNT"])

    plt.title("monthly covid statics")
    plt.legend(["CLEAR_CNT", "DEATH_CNT", "CARE_CNT", "DECIDE_CNT"])
    plt.show()
