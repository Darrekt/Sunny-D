import smbus
import math

# Initialisation
bus = smbus.SMBus(1)
bus.write_byte_data(0x39, 0x0, 0x3)

# Polling loop
while True:
    ch0_lo = bus.read_byte_data(0x39, 0xC) & 0xFF
    ch0_hi = bus.read_byte_data(0x39, 0xD) & 0xFF

    ch1_lo = bus.read_byte_data(0x39, 0xE) & 0xFF
    ch1_hi = bus.read_byte_data(0x39, 0xF) & 0xFF

    ch0 = ch0_lo | (ch0_hi << 8)
    ch1 = ch1_lo | (ch1_hi << 8)
    
    coeff = float(ch1) / float(ch0)
    lux = 0.0
    if 0 < coeff and coeff <= 0.5: 
        lux = 0.0304 * ch0 - 0.062 * ch0 * (pow(ch1/ch0), 1.4)
    elif (0.5 < coeff and coeff <= 0.61):
        lux = 0.0224 * ch0 - 0.031 * ch1
    elif (0.61 < coeff and coeff <= 0.8):
        lux = 0.0128 * ch0 - 0.0153 * ch1
    elif (0.8 < coeff and coeff <= 1.3):
        lux = 0.00146 * ch0 - 0.00112 * ch1

    print(lux)
