#_*_coding:utf-8_*_
import urllib.request
import json


class Transla:
    # Please use your fanyi.youdao key

    def traselator(self, q):
        # q = 'test'
        keyfrom = 'wufeifei'
        key = '716426270'
        contents = urllib.request.urlopen(
            f"http://fanyi.youdao.com/openapi.do?keyfrom={keyfrom}&key={key}&type=data&doctype=json&version=1.1&q={q}").read()

        jsonc = json.loads(contents.decode('utf-8'))

        errorCode = jsonc['errorCode']
        if errorCode == 20:
            print("要翻译的文本过长")
        elif errorCode == 30:
            print("无法进行有效的翻译")
        elif errorCode == 40:
            print("无法进行有效的翻译")
        elif errorCode == 50:
            print("无效的 key")
        elif errorCode == 60:
            print("无词典结果，仅在获取词典结果生效")
        else:   # it's 0 means succesed
            # print(jsonc['errorCode'])
            print("################################")
            print("#    查询：", jsonc['query'])
            print("#    翻译：", jsonc['translation'][0])
            # print(jsonc['basic'])
            try:
                print("#    发音：", jsonc['basic']['phonetic'])
            except KeyError as identifier:
                pass
            try:
                print("#    英式发音：", jsonc['basic']['uk-phonetic'])
                print("#    美式发音：", jsonc['basic']['us-phonetic'])
            except KeyError as identifier:
                pass

            for be in jsonc['basic']['explains']:
                print("#        ", be)
            for i in range(len(jsonc['web'])):
                print("#    ", jsonc['web'][i]['key'], ":")
                for j in range(len(jsonc['web'][i]['value'])):
                    print("#        ", jsonc['web'][i]['value'][j])
            print("################################")
