from periphery import I2C

i2c = I2C("/dev/i2c-1")
device_address = 0x50
query = [I2C.Message([0x00, 0x00]), I2C.Message([0x00]*8000, read=True)]
i2c.transfer(device_address, query)
for i in query[1].data:
	print(i)
# ~ pickle.dump(query[1].data, open("eeprom.p", "wb"))
