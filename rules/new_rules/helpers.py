import re
import xmltodict
from .input_data import InputData


def get_data(path):
    with open(path) as fd:
        return InputData(xmltodict.parse(fd.read()))


def starts_with(data, pattern, message):
    """ Check if data starts with pattern e.g. ["http://", "https://"] """
    for p in pattern:
        if data.startswith(p):
            return 'ok'

    return message


def in_range(data, pattern, message):
    if len(data) == 0:
        return message

    for d in data:
        if str(d) not in pattern:
            return message

    return 'ok'


def not_empty(data, message):
    if len(data) == 0:
        return message

    for d in data:
        if len(d) == 0:
            return message

    return 'ok'


def contain(data, attr, value, element, message):
    for d in data:
        if d[attr] == value:
            for key in d.keys():
                element_name = re.sub(r'^\w+:([\s\S]+)', r'\1', key)

                if element_name == element:
                    return 'ok'

    return message


def not_contain(data, attr, message):
    if len(data.get_element(attr, ignore_namespaces=False)) != 0:
        return message

    return 'ok'


def contain_attr(data, attr, value, message):
    for d in data:
        print(d)

        if d[attr] == value:
            return 'ok'

    return message
