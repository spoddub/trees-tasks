
from hexlet import fs

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])

def get_nodes_count(tree):
    if fs.is_file(tree):
        return 1
    children = fs.get_children(tree)
    counter = list(map(get_nodes_count, children))
    return 1 + sum(counter)

