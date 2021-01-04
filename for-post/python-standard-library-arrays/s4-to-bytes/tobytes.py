import array as arr

a = arr.array('i', [255])

print(a.tobytes()) # b'\xff\x00\x00\x00'

