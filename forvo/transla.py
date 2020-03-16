#_*_coding:utf-8_*_
import urllib.request
import json
from color import _Colored

class Transla:
    # Please use your fanyi.youdao key

    def traselator(self, q):

        LightBlue = _Colored()._wrap_color(_Colored.LightBlue)
        Purple2 = _Colored()._wrap_color(_Colored.Purple2)

        keyfrom = 'wufeifei'
        key = '716426270'
        # https://github.com/FeeiCN/dict/blob/master/dict/__init__.py
        contents = urllib.request.urlopen(
            f"http://fanyi.youdao.com/openapi.do?keyfrom={keyfrom}&key={key}&type=data&doctype=json&version=1.1&q={q}").read()

        jsonc = json.loads(contents.decode('utf-8'))

        errorCode = jsonc['errorCode']
        if errorCode == 20:
            print(Purple2("要翻译的文本过长"))
        elif errorCode == 30:
            print(Purple2("无法进行有效的翻译"))
        elif errorCode == 40:
            print(Purple2("无法进行有效的翻译"))
        elif errorCode == 50:
            print(Purple2("无效的 key"))
        elif errorCode == 60:
            print(Purple2("无词典结果，仅在获取词典结果生效"))
        else:   # it's 0 means succesed
            # print(jsonc['errorCode'])
            print(LightBlue("+-------------------------------"))
            print(LightBlue("+    查询："), LightBlue(jsonc['query']))
            print(LightBlue("+    翻译："), LightBlue(jsonc['translation'][0]))
            # print(jsonc['basic'])
            try:
                print(LightBlue("+    发音："), LightBlue(jsonc['basic']['phonetic']))
            except KeyError as identifier:
                pass
            try:
                print(LightBlue("+    英式发音："), LightBlue(jsonc['basic']['uk-phonetic']))
                print(LightBlue("+    美式发音："), LightBlue(jsonc['basic']['us-phonetic']))
            except KeyError as identifier:
                pass

            try:
                for be in jsonc['basic']['explains']:
                    print(LightBlue("+        "), LightBlue(be))
            except KeyError as identifier:
                pass
            
            try:
                for i in range(len(jsonc['web'])):
                    print(LightBlue("+    "), LightBlue(jsonc['web'][i]['key'], ":"))
                    for j in range(len(jsonc['web'][i]['value'])):
                        print(LightBlue("+        "), LightBlue(jsonc['web'][i]['value'][j]))
            except KeyError as identifier:
                pass
           
            print(LightBlue("+-------------------------------"))
