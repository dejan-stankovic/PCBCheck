#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parsing routines for the ODB++ line record text format
according to the ODB++ 7.0 specification:

http://www.odb-sa.com/wp-content/uploads/ODB_Format_Description_v7.pdf
"""
from collections import defaultdict
import os.path
from Utils import readZIPFileLines


def filter_line_record_lines(lines):
    "Remove empty and '#'-only lines from the given line list"
    return [
        line for line in lines
        if line and line != "#"
    ]

def read_raw_linerecords(filename):
    "Read a .Z line record file and return only important lines in order"
    return filter_line_record_lines(
        readZIPFileLines(filename))

def group_by_section(lines):
    "Group a line record file by the section. Returns a dict containing lists."
    groups = defaultdict(list)
    name = None
    for line in lines:
        if line.startswith("#"):
            name = line.strip("#").strip()
        else:
            groups[name].append(line)
    return groups