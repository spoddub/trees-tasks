def remove_first_level(tree):
    result = []
    for item in tree:
        if type(item) == list:
            for subitem in item:
                result.append(subitem)
    return result
