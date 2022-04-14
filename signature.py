import os
path = input(" file path : ")
os.chdir(path)

sayi = 0
for i in os.listdir(path): 
	sayi += 1
	with open(i, "rb") as f:
		oku = f.read(10)
		if oku[6:11] in [b"JFIF", b"Exif"]:
			print(i, "=>", "JPEG dosyasıdır")

		elif oku[:8] in b"\x89PNG\r\n\x1a\n":
			print(i, "=>", "PNG dosyasıdır")

		elif oku[:3] in b"GIF":
			print(i, "=>", "GIF dosyasıdır")

		elif oku[:2] in [b'II', b'MM']:
			print(i, "=>", "TIFF dosyasıdır")

		elif oku[:2] in b"MZ":
			print(i, "=>", "EXE dosyasıdır")

		elif oku[:3] in b"PDF":
			print(i, "=>", "PDF dosyasıdır")

		else:
			print("Türü Bilinmeyen Dosya !!! ")
print("\n"*3)

print(" [+] {} dosya tarandı".format(sayi).rjust(30), "\n")
f.close()
