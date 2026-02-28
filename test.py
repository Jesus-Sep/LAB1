import qrcode
from faker import Faker

fake =Faker()
#variables y constantes
# Hice mas modificaciones para youtube, pero deje el codgio que uso par ael ciclo final
#solo seria cambiar qr.add_data('Some data') por un link  o otra cosa
#usamos csus propiedads para cmabiar color img = qr.make_image(fill_color="black", back_color="white")
for _ in range(10):
    name = fake.name();
    img =qrcode.make(name)
    img.save(name + ".png")
    print(f"QR code for {name} generated and saved as {name}png")