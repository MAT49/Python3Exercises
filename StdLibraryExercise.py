# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:04:17 2020

@author: Motoko
"""


from os import getcwd, environ
import sys
import os
import datetime
import time
import html


# current = getcwd()
# # print(current)
# print(sys.platform)

# print(os.environ)
# print(os.getenv('HOME'))

# # print(os.getenv('HOME'))

# print(datetime.date.today())
# print(datetime.date.today().day)
# print(datetime.date.today().month)
# print(datetime.date.today().year)

# str = datetime.date.isoformat(datetime.date.today())
# print(str)

# print(time.strftime("%H:%M:%S"))

# print(time.strftime("%A %p"))

print(html.escape("This HTML fragment contains a <script>script</script> tag."))

print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))