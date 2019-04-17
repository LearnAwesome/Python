#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def main(root):
    path = find_and_create_path(root)
    os.system('python3 %s' % (path))

def find_and_create_path(root):
    if is_python_file(root):
        return root
    file_list = filter(is_ignored, sorted(os.listdir(root)))
    path = root + '/' + list(file_list)[-1]
    return find_and_create_path(path)

def is_ignored(filename):
    ignore_list = ['.DS_Store']
    for _filename in ignore_list:
        if filename.lower() != _filename.lower():
            return True

def is_python_file(filename):
    return filename[-2:] == 'py'

basic_root = 'Basic'
main(basic_root)