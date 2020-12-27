from typing import Callable, Iterable, List
from time import time


def log(text: str) -> Callable:
    """
    Decorates function to log
    :param text:
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            ret = func(*args, **kwargs)
            end_time = time()
            print(text.format(end_time - start_time))
            return ret

        return wrapper

    return decorator


def splitter(iter: Iterable, char: str = ' ', ) -> List:
    """
    Splits iterable by some split-character char
    :param iter: Some iterable object of strings
    :param char: Split-character
    :return: List
    """
    return [el for el in iter.split(char) if el is not []]


def stripper(iter: Iterable, char: str = ' ', ) -> List:
    """
    Strips iterable by some strip-character char
    :param iter: Some iterable object of strings
    :param char: Strip-character
    :return: List
    """
    return [el.strip(char) for el in iter if el is not []]
