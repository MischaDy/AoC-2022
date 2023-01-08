from typing import Iterable


def flatten(list_, level=1):
    for _ in range(level):
        list_ = flatten_once(list_)
    return list_


def flatten_once(list_):
    flat_list = []
    for sublist in list_:
        flat_list.extend(sublist)
    return flat_list


def minmax(a, b):
    return (a, b) if a <= b else (b, a)


def const_factory(x):
    def const(*args, **kwargs):
        return x
    return const


def map_rev(nested_iterable: Iterable, to=list):
    """
    Reverse each iterable contained in the nested iterable
    :param nested_iterable:
    :param to:
    :return:
    """
    for iterable in nested_iterable:
        yield to(reversed(iterable))
