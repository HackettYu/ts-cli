#_*_coding:utf-8_*_
import argparse
import sys
from transla import Transla  # 不支持带 “-”
from pronunc import Pronunc


# def __init__():
#     if len(sys.argv) > 0:
#         for s in sys.argv:
#             s = s.encode('utf-8')

# def encodeCommandArg(bytesstring):
#     utf_string = bytesstring.decode(sys.getfilesystemencoding())
#     return utf_string
# utf_type = lambda s: str(sys.getfilesystemencoding, 'utf-8')


def foo():
    parser = argparse.ArgumentParser(description="输入你要查找的单词或汉字")
    parser.add_argument("-p", "--pronunc", default=1,
                        help="发音，默认发音，参数为：1 发音，其它不发音")
    parser.add_argument("word", help="输入")    # python2 -> python3 : unicode -> str
    parser.add_argument("-n", "--num", type=int, default=1,
                        help="选择音源，默认为音源 1")

    args = parser.parse_args()
    # print(args)
    # args.word.encode()

    if args.word is None:
        # print("请输入：")
        pass
    # elif args.pronunc != 1 and args.num:    # 默认不发音
    elif args.pronunc == 1 and args.num:    # 默认发音, "-p 2" 也表示不发音
        t = Transla().traselator(args.word)
        p = Pronunc().getEnglishPronunciation(args.word, args.num)
    elif args.num is None:
        t = Transla().traselator(args.word)
        p = Pronunc().getEnglishPronunciation(args.word, 1)
    else:
        t = Transla().traselator(args.word)


def main():
    # __init__()
    foo()


if __name__ == '__main__':
    main()
