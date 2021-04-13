#!/usr/bin/env python3
# coding: utf-8

# File: upx-fix.py
# Desc: Fix upx format for unpack malware -> Mozi
# Usage: ./upx-fix.py <your binary>

import sys
import os

fileName = sys.argv[1]

# Recover "p_filesize" from the binary
p_filesize = []
file_size = os.stat(fileName).st_size
#print(file_size)
with open(fileName,'rb') as fh:
    offset = file_size - 12
    fh = open(fileName,'rb')
    fh.seek(offset)
    for c in range(0,4):
        s = fh.read(1)
        hex_value = r"0x%02x" % ord(s)
        p_filesize.append(hex_value)
    print(p_filesize)

# Auto patch the binary
offset_1 = 128 + 4
offset_2 = 128 + 4 + 4

fh = open(fileName,'r+b')

count = 0
for b in p_filesize:
    fh.seek(offset_1 + count)
    fh.write(bytes([int(b,0)]))
    count += 1
count = 0
for b in p_filesize:
    fh.seek(offset_2 + count)
    fh.write(bytes([int(b,0)]))
    count += 1

fh.close()
