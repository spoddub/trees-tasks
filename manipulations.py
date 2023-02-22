import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile



def compress_images(tree):
    children = get_children(tree)

    def reduce_image_size(node):
        name = get_name(node)
        if not is_file(node) or not name.endswith('.jpg'):
            return node
        meta = get_meta(node)
        new_meta = copy.deepcopy(meta)
        new_meta['size'] //= 2
        return mkfile(name, new_meta)

    new_children = map(reduce_image_size, children)
    new_meta = copy.deepcopy(get_meta(tree))
    return mkdir(get_name(tree), list(new_children), new_meta)
