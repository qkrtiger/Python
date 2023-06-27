import spidev
import time

delay = 0.5

pot_ch = 0

spi = spidev.SpiDev() # spi 통신용 객체

spi.open(0, 0) # spi 통신 회선 열기
spi.max_speed_hz = 100000 # 통신 속도 설정

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

try:
    while True:
        pot_value = readadc(pot_ch)
        print(f'저항값 : {pot_value}')
        time.sleep(delay)
except KeyboardInterrupt:
    pass
finally:
    print('프로그램 종료')
    
