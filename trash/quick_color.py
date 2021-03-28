import base64

sprite = ["0x"]
for _ in range(8):
    for _ in range(8):
        sprite.append("03A2B1")

sprite = "".join(sprite)
sprite = int(sprite, 16)
sprite = hex(sprite).encode()
print(sprite)

#sprite = base64.b64encode(sprite)
#print(sprite)

#s = 'cafebabe'
b64 = base64.b64encode(sprite).decode()
print('cafebabe in base64:', b64)