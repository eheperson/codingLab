import trial
print("")

c1 = trial.Calisan('Ahmet')
c2 = trial.Calisan('Mehmet')

print("")

print(c1.personel)
print(c2.personel)

print("")

print(c1.isim)
print(c2.isim)

print("")

c1.isim = "Mahmut"
c1.personel[0] = "Mahmut"

print("")

print(c1.isim)
print(c1.personel)

print("")

c1.kabiliyet_ekle("prezantabl")
c1.kabiliyet_ekle('konuskan')
c1.kabiliyetleri_goruntule()

print("")

c2.kabiliyet_ekle('girisken')
c2.kabiliyetleri_goruntule()

print("")

c1.personeli_goruntule()
c2.personeli_goruntule()

print("")
print("-- Harf Ayaci --")
print("")

