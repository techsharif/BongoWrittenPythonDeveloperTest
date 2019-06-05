def is_non_primitive(obj):
    return True

def calculate_depth(data, depth):
	return []


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
