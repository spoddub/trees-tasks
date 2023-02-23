import copy
from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile

def downcase_file_names(tree):
    name = get_name(tree)
    new_meta = copy.deepcopy(get_meta(tree))
    if is_file(tree):
        return mkfile(name.lower(), new_meta)
    children = get_children(tree)
    new_children = list(map(downcase_file_names, children))
    return mkdir(name, new_children, new_meta)
