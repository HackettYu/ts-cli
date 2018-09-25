#_*_coding:utf-8_*_
import re
import requests
import json
import base64
import subprocess


class Pronunc:
    # https://github.com/rvfu/forvo-api-free/blob/master/en.py
    def getEnglishPronunciation(self, word, num):
        # 字符串格式化写法
        # 1. "{},{}".format(arg1, arg2)
        # 2. f"{a},{b}"
        # 3. "%s,%d" %str %int
        webPageUrl = f"https://forvo.com/word/{word}/#en"
        webPageText = requests.get(webPageUrl).text
        # 使'.'特殊字符与任何字符匹配，包括换行符; 没有此标志，'.'将匹配除换行符之外的任何内容。对应于内联标志(?s)。
        englishPageTextList = re.findall(
            "<em id=\"en.*?</article>", webPageText, re.DOTALL)  # 「.*？」非贪婪匹配 「.*」贪婪匹配
        if len(englishPageTextList) == 0:
            return '{"status":"error"}'
        englishPageText = englishPageTextList[0]
        pronunciations = re.findall("Play\(\d+,'(.*?)'", englishPageText)
        for l in range(len(pronunciations)):
            pronunciations[l] = base64.b64decode(pronunciations[l]).decode()

        key = json.dumps(pronunciations)
		
        pronunclist = key.split('"')  # get the list of voice
        num = num % len(pronunclist)
        pronunc = pronunclist[num]
        if pronunc == False:  # it could has other pronunciations
            print("no pronunciation")

        # http => httpie : like curl compile by python
        #	-d => download https mpeg to mpg123 play
        # mpg123 => compile by c lang
        # 	-q => quit schema
        if pronunc:
            subprocess.call(
                f"http -d https://forvo.com/mp3/{pronunc} | mpg123 -q -", shell=True)
