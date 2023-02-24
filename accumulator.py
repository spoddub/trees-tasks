import os

from hexlet.fs import flatten, get_children, get_name, is_file


def find_files_by_name(tree, substr):
    def walk(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if is_file(node):
            return [] if name.find(substr) < 0 else new_ancestry
        children = get_children(node)
        paths = map(lambda child: walk(child, new_ancestry), children)
        return flatten(paths)
    return walk(tree, '')
