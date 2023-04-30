from pprint import pprint, pformat


def print_arg(arg, name=None, indent=' '*4, depth=1):
    prefix = indent * depth
    line = prefix
    if name:
        line += f'{name}='
    if isinstance(arg, dict):
        line += '{'
        print(line)
        for key, val in arg.items():
            print_arg(val, name=key, indent=indent, depth=depth+1)
        print(f'{prefix}}}')
    elif isinstance(arg, list):
        line += '['
        print(line)
        for item in arg:
            print_arg(item, indent=indent, depth=depth+1)
        print(f'{prefix}]')
    else:
        print(f'{line}{arg}')


if __name__ == '__main__':

    print('[1] ---------------- [1]')

    class MetaClass(type):

        def __new__(cls, name, bases, dct, *args, **kwargs):
            print(f'MetaClass::__new__(')
            print_arg(cls, name='cls')
            print_arg(name, name='name')
            print_arg(bases, name='bases')
            print_arg(dct, name='dct')
            for arg in args:
                print_arg(arg)
            for name, kwarg in kwargs.items():
                print_arg(kwarg, name=name)
            print(')')
            return super().__new__(cls, name, bases, dct, *args, **kwargs)

        def __init__(cls, *args, **kwargs):
            print('MetaClass::__init__(')
            print_arg(cls, name='cls')
            for arg in args:
                print_arg(arg)
            for name, kwarg in kwargs.items():
                print_arg(kwarg, name=name)
            print(')')
            super().__init__(*args, **kwargs)

        def __call__(self, *args, **kwargs):
            print('MetaClass::__call__(' + (')' if not args and not kwargs else ''))
            for arg in args:
                print_arg(arg)
            for name, kwarg in kwargs.items():
                print_arg(kwarg, name=name)
            if args or kwargs:
                print(')')
            super().__call__(*args, **kwargs)

    print('[2] ---------------- [2]')

    class ObjClass(metaclass=MetaClass):

        def __new__(cls, *args, **kwargs):
            print(f'ObjClass::__new__(')
            print_arg(cls, name='cls')
            for arg in args:
                print_arg(arg)
            for name, kwarg in kwargs.items():
                print_arg(kwarg, name=name)
            print(')')
            return super().__new__(cls)

        def __init__(self, *args, **kwargs):
            print('ObjClass::__init__(' + (')' if not args and not kwargs else ''))
            for arg in args:
                print_arg(arg)
            for name, kwarg in kwargs.items():
                print_arg(kwarg, name=name)
            if args or kwargs:
                print(')')
            super().__init__()

        def __call__(self, *args, **kwargs):
            print('ObjClass::call(' + (')' if not args and not kwargs else ''))
            for arg in args:
                print_arg(arg)
            for name, kwarg in kwargs.items():
                print_arg(kwarg, name=name)
            if args or kwargs:
                print(')')

    print('[3] ---------------- [3]')

    obj = ObjClass(1, 2, kwarg=3)

    print('[4] ---------------- [4]')
