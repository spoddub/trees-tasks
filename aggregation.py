from hexlet.fs import get_children, get_name, is_file

def get_hidden_files_count(tree):
    name = get_name(tree)
    if is_file(tree):
        return name.startswith('.')
    children = get_children(tree)
    hidden_files = list(map(get_hidden_files_count, children))
    return sum(hidden_files)
