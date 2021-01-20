import struct

f = open("/dev/input/event4","rb");
while 1:

    data = f.read(24)
    print struct.unpack('4IHHI',data)

print("")
