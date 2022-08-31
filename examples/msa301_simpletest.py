# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_msa3xx import MSA301

i2c = board.I2C()  # uses board.SCL and board.SDA
msa = MSA301(i2c)

while True:
    print("%f %f %f" % msa.acceleration)
    time.sleep(0.5)
