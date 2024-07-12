from rembg import remove

input_path = "WhatsApp Görsel 2024-07-07 saat 21.15.21_82703dc3.jpg"
output_path = "output.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)