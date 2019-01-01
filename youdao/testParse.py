import argparse
from url import Transla
from test import Pronunc    # TODO

parser = argparse.ArgumentParser(description="输入你要查找的单词或汉字")
# group = parser.add_mutually_exclusive_group()
parser.add_argument("-p", "--pronunc",default=1, help="pronunciation word")
parser.add_argument("word", type=str, help="input the word")
try:
    parser.add_argument("-n", "--num", type=int, default=1, help="choice pronunciation")
except Exception as identifier:
    pass

args = parser.parse_args()
# print(args)

if args.word is None:
    print("Please input the word")
elif args.pronunc  and args.num:    # 默认不发音，如果想要发音可以删掉 "!= 1"
    t = Transla().traselator(args.word)
    p = Pronunc().getEnglishPronunciation(args.word, args.num)
elif args.num is None:
    t = Transla().traselator(args.word)
    p = Pronunc().getEnglishPronunciation(args.word, 1)
else:
    t = Transla().traselator(args.word)

# def main():
#     pass

# if __name__ == '__main__':
#     main()