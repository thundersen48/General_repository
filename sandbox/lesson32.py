import os
tree = os.walk('folder/')
"""
Данный объект это генератор
он не хранит в себе данные
он генерирует их по запросу.
"""
# print(tree)
# for files in tree:
#     print(files)


def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root,dirs, files)
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename((root))}]')
        sub_indent = ' ' * 4 * (level + 1)

        # print(root, files, level, indent, sub_indent)
        for file in files:
            print(f'{sub_indent} {file}' )

read_dir('folder')

