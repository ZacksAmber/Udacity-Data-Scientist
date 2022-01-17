#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: index-generator.py                                                #
# File Path: /index-generator.py                                               #
# Created Date: 2022-01-13                                                     #
# -----                                                                        #
# Company: Zacks Shen                                                          #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2022-01-13 4:06:38 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2022 Zacks Shen                                                #
################################################################################

import os


def filter_files():
    """filter_files filter the qualified files.

    Returns:
        list: A list contains all filtered file names.
    """
    files = os.listdir()
    notebooks = []
    # Append all files with .ipynb extension
    for file in files:
        if file.endswith('.ipynb'):
            notebooks.append(file)
    # Remove all files in CN
    en_notebooks = []
    for notebook in notebooks:
        if not notebook.endswith("zh.ipynb"):
            en_notebooks.append(notebook)
    # Remove all solutions
    no_solution_notebooks = []
    for notebook in en_notebooks:
        if not notebook.endswith("solution.ipynb"):
            no_solution_notebooks.append(notebook)

    return no_solution_notebooks


def generate_index(notebooks):
    """generate_index generate file link under Markdown format.

    Args:
        notebooks (list): The list provided by function filter_files.
    """
    notebooks.sort()
    titles = []
    for file in notebooks:
        # Process filelink
        filelink = f'(./{file})'
        # Process filename
        filenames = file.split('.ipynb')[0].split('_')
        filenames = list(map(lambda x: x.capitalize(), filenames))
        filename = ' '.join(filenames)
        filename = f'[{filename}]'
        titles.append(f'### {filename}{filelink}')

    for title in titles:
        print(title)
        print('')
        print('---')
        print('')


notebooks = filter_files()
generate_index(notebooks)
