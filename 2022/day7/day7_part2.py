#!/usr/bin/env python
"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is `70000000`. To run the
update, you need unused space of at least `30000000`. You need to find a
directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the
total amount of used space) is `48381165`; this means that the size of the
unused space must currently be `21618835`, which isn't quite the `30000000`
required by the update. Therefore, the update still requires a directory with
total size of at least `8381165` to be deleted before it can run.

To achieve this, you have the following options:

  * Delete directory `e`, which would increase unused space by `584`.
  * Delete directory `a`, which would increase unused space by `94853`.
  * Delete directory `d`, which would increase unused space by `24933642`.
  * Delete directory `/`, which would increase unused space by `48381165`.

Directories `e` and `a` are both too small; deleting them would not free up
enough space. However, directories `d` and `/` are both big enough! Between
these, choose the smallest: `d`, increasing unused space by `24933642`.

Find the smallest directory that, if deleted, would free up enough space on
the filesystem to run the update. What is the total size of that directory?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip()

data = raw_data.splitlines()


class File:
    def __init__(self, filename, filesize):
        self.name = filename
        self.size = filesize

    def __repr__(self):
        return f'<File name="{self.name}" size={self.size}>'


class Dir:
    def __init__(self, dirname, parent=None):
        self.name = dirname
        self.parent = parent
        self.children = []
        self.files = []
        self.size = 0

    def add_file(self, file):
        self.files.append(file)
        self.size += file.size

    def __repr__(self):
        return f'<Dir name="{self.name}" size={self.size} children={len(self.children)} files={len(self.files)}>'


root = Dir('/')
current = root
small_dirs = []

for row in data:
    # COMMAND
    if row.startswith('$'):
        parts = row.split(' ')
        # Change dir
        if parts[1] == 'cd':
            # Move up a directory
            if parts[2] == '..':
                current = current.parent
            # Move down a director
            else:
                for child in current.children:
                    if child.name == parts[2]:
                        current = child
                        break
    # DIR
    elif row.startswith('dir'):
        _, name = row.split(' ')
        new_dir = Dir(name, current)
        current.children.append(new_dir)
    # FILE
    else:
        size, name = row.split(' ')
        new_file = File(name, int(size))
        current.add_file(new_file)


total_size = 70000000
needed_space = 30000000


def get_dir_size(dir):
    if not dir.children:
        result = dir.size
    else:
        result = dir.size + sum(get_dir_size(x) for x in dir.children)
    return result


root_size = get_dir_size(root)
current_free = total_size - root_size
needed = needed_space - current_free

to_delete = []


def get_dir_to_delete(dir):
    if not dir.children:
        result = dir.size
    else:
        result = dir.size + sum(get_dir_to_delete(x) for x in dir.children)
    if result >= needed:
        to_delete.append(result)
    return result


get_dir_to_delete(root)
print(sorted(to_delete)[0])
