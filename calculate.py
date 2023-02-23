from hexlet.fs import get_children, get_meta, get_name, is_file


def calculate_entry_size(tree):
    if is_file(tree):
        meta = get_meta(tree)
        return meta['size']
    children = get_children(tree)
    sizes = list(map(calculate_entry_size, children))
    return sum(sizes)


def du(tree):
    children = get_children(tree)
    result = list(map(
        lambda child: (get_name(child), calculate_entry_size(child)),
        children,
    ))
    result.sort(key=lambda entry: entry[1], reverse=True)
    return result
