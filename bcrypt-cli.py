#!/usr/bin/env python3

import bcrypt
import sys

value = sys.stdin.read()
value2 = bytes(value, 'utf-8')
salt = bcrypt.gensalt(12)
print(bcrypt.hashpw(value2, salt))
