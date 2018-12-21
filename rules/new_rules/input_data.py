import re
from collections import OrderedDict


class InputData():
    def __init__(self, data):
        self._doc = data

    def get_element(self, name, root=None, ignore_namespaces=True, as_list=False):
        if root is None:
            root = self._doc

        if not isinstance(root, OrderedDict):
            return InputData(None)

        for element_name in root:
            if ignore_namespaces:
                raw_element_name = re.sub(r'^\w+:([\s\S]+)', r'\1', element_name)
            else:
                raw_element_name = element_name

            if raw_element_name == name:
                if not isinstance(root[element_name], list) and as_list:
                    return InputData([root[element_name]])
                else:
                    return InputData(root[element_name])

            if isinstance(root[element_name], OrderedDict):
                result = self.get_element(name, root[element_name], ignore_namespaces=ignore_namespaces, as_list=as_list)

                if len(result) != 0:
                    return result

        return InputData(OrderedDict())

    def __getitem__(self, index):
        return self._doc[index]

    def __len__(self):
        return len(self._doc)

    def __str__(self):
        return str(self._doc)

    def __iter__(self):
        return self._doc.__iter__()
