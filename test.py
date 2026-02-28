import qrcode
from faker import Faker

fake =Faker()
#variables y constantes#
for _ in range(10):
    name = fake.name();
    img =qrcode.make(name)
    img.save(name + ".png")
    print(f"QR code for {name} generated and saved as {name}png")