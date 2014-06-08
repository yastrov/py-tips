#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unix epoh time
"""

import time
epoch_time = int(time.time())
print(epoch_time)

import datetome
t = datetime.datetime.now()
epoch_time = time.mktime(t.timetuple())
print(epoch_time)

# UTC
t = datetime.datetime.utcnow()
epoch_time = time.mktime(t.timetuple())
print(epoch_time)
