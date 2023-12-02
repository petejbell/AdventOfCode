import re
from itertools import chain

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size


class Dir:
  def __init__(self, name, parent=None):
    self.name = name
    self._parent = parent
    self._sub_dirs = []
    self._files = []

  def add_file(self, file_name, file_size):
    if not [file for file in self._files if file.name == file_name]:
      self._files.append(File(file_name, int(file_size)))

  def cd(self, dir_name):
    sub_dir =  next((sub_dir for sub_dir in self._sub_dirs if sub_dir.name == dir_name), None)
    if not sub_dir:
      sub_dir = Dir(dir_name, self)
      self._sub_dirs.append(sub_dir)
    return sub_dir
  
  def up(self):
    if self._parent:
      return self._parent
    raise Exception('Cannot .. from root directory')
  
  @property
  def size(self):
    size = sum([file.size for file in self._files]) + sum([sub_dir.size for sub_dir in self._sub_dirs])
    return size
  
  @property
  def all_sub_dirs(self):
    return self._sub_dirs + list(chain.from_iterable([sub_dir.all_sub_dirs for sub_dir in self._sub_dirs]))

  def sum_size(self, under):
    return sum([sub_dir.size for sub_dir in self.all_sub_dirs if sub_dir.size <= under])
  
  def smallest_sub_dir_size(self, above):
    return min([sub_dir.size for sub_dir in self.all_sub_dirs if sub_dir.size >= above])


class Filesystem:
  @classmethod
  def parse_dir_tree(cls, rows):
    root = cwd = Dir('root')
    for row in rows:
      if row == '$ cd ..':
        cwd = cwd.up()
        continue
      cd_match = re.match('\$ cd (.+)', row)
      if cd_match:
        cwd = cwd.cd(cd_match.group(1))
        continue
      file_match = re.match('(\d+) (.*)', row)
      if file_match:
        cwd.add_file(file_match.group(2), file_match.group(1))
    return root

  def __init__(self, filename):
    with open(filename) as data:
      self.data = data.read()
      self.root = Filesystem.parse_dir_tree(self.data.splitlines())


def main():
  fs = Filesystem('day7.txt')
  print(f"Part 1: {fs.root.sum_size(100_000)}")
  unused = 70_000_000 - fs.root.size
  print(f"Part 2: {fs.root.smallest_sub_dir_size(30_000_000 - unused)}")

main()