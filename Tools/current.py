#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def main(root):
    path = find_and_create_path(root)
    pathLog = 'Run python file: \033[32m%s\033[0m' % (path)
    divLen = (len(pathLog) - 9)
    print(pathLog)
    print('-' * divLen)
    os.system('python3 %s' % (path))
    print('-' * divLen)

def find_and_create_path(root):
    if is_python_file(root):
        return root
    file_list = filter(is_ignored, sorted(os.listdir(root)))
    path = root + '/' + list(file_list)[-1]
    return find_and_create_path(path)

def is_ignored(filename):
#     ignore_list = ['.DS_Store']
#     for _filename in ignore_list:
#         return not _filename.lower() in filename.lower()
    return filename[:2].isdigit()

def is_python_file(filename):
    return filename[-2:] == 'py'

basic_root = 'Basic'
main(basic_root)