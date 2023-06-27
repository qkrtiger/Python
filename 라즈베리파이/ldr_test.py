import spidev
import time

delay = 0.5
ldr_ch = 0

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def readldr(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

try:
    while True:
        lv = readldr(ldr_ch)
        print(f'밝기 : {lv}')
        time.sleep(delay)
except KeyboardInterrupt:
    pass
finally:
    print('프로그램 종료')