class _Colored:
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    Blue = '\033[34m'
    Purple = '\033[35m'
    LightBlue = '\033[36m'
    Clear = '\033[39m'
    Purple2 = '\033[95m'

    def _wrap_color(self, colored: str):
        """ 
        color warp 
        """
        def func(*strings: str, sep=''):
            strings = map(lambda each: '{}{}'.format(colored, each), strings)
            return '{}{}'.format(sep.join(strings), _Colored.Clear)
        return func
