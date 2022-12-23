def flatten(list_, level=1):
    for _ in range(level):
        list_ = flatten_once(list_)
    return list_


def flatten_once(list_):
    flat_list = []
    for sublist in list_:
        flat_list.extend(sublist)
    return flat_list
