def is_non_primitive(obj):
    return hasattr(obj, '__dict__')

def calculate_depth(data, depth):
    if not data:
        return []

    if is_non_primitive(data):
        return calculate_depth(data.__dict__, depth)

    if type(data) == dict and len(data)==1:
        key = list(data.keys())[0]
        value = data[key]
        if type(value) == dict or is_non_primitive(value):
            return [[key, depth]] + calculate_depth(value, depth+1)
        else:
            return [[key, depth]]
    else:
        first_key = list(data.keys())[0]
        first_value = data.pop(first_key)
        first_data = {first_key:first_value}
        return calculate_depth(first_data, depth) + calculate_depth(data, depth)


def print_depth(data):
    result_data = calculate_depth(data, 1)
    print('\n'.join([ f'{datam[0]} {datam[1]}' for datam in result_data]))

if __name__ == '__main__':
    data = {
            "key1": {
                "key2": {
                    "key3": 4
                }
            }
        }

    print_depth(data)
