print("Hitung luas ruangan")

panjang= float(input("masukkan panjang ruangan:"))
lebar= float(input("masukkan lebar ruangan:"))
ukuran= (input("masukkan satuan (meter/inci):"))
luas= panjang * lebar

if "meter" in ukuran:
    print("Luas ruangan dengan panjang", panjang, "dan lebar", lebar, "adalah", luas, "meter" )
elif "inci" in ukuran:
    print("luas ruangan dengan panjang", panjang, "dan lebar", lebar, "adalah", luas * 39.3701, "inci")
    
