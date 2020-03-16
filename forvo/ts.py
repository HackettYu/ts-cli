# _*_coding:utf-8_*_
import argparse
import sys
import types
from argparse import RawTextHelpFormatter

from color import _Colored
from pronunc import Pronunc
from transla import Transla


def foo():
    """输入你要查找的单词或汉字
    """
    # Red = _wrap_color(_Colored.Red)
    Green = _Colored()._wrap_color(_Colored.Green)
    Yellow = _Colored()._wrap_color(_Colored.Yellow)
    # Blue = _wrap_color(_Colored.Blue)
    # Purple = _wrap_color(_Colored.Purple)
    # LightBlue = _wrap_color(_Colored.LightBlue)
    # Purple2 = _Colored()._wrap_color(_Colored.Purple2)

    parser = argparse.ArgumentParser(
        description=Yellow(foo.__doc__),
        add_help=True,
        formatter_class=RawTextHelpFormatter)
    # parser.add_argument("-p", "--pronunc", default=1,
    #                     help=Green("发音，默认发音，参数为：1 发音，其它不发音"))
    # python2 -> python3 : unicode -> str
    parser.add_argument("word", help=Green("输入"))
    # parser.add_argument("-n", "--num", type=int, default=1,
    #                     help=Purple2("选择音源，默认为音源 1"))

    args = parser.parse_args()

    if args.word is None:
        return
    # 默认发音, "-p 2" 也表示不发音
    Transla().traselator(args.word)
        # Pronunc().getEnglishPronunciation(args.word, args.num)
    # elif args.num is None:
    #     Transla().traselator(args.word)
        # Pronunc().getEnglishPronunciation(args.word, 1)
    # else:
    #     Transla().traselator(args.word)


def main():
    sys.exit(foo())


if __name__ == '__main__':
    main()
