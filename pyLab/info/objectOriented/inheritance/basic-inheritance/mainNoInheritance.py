import oyuncularNoInheritance as oyuncular
asker1 = oyuncular.Asker('Mehmet', 'er')

print(dir(asker1))

print("")

print(asker1.isim)
print(asker1.rütbe)
print(asker1.güç)

print("")

asker1.hareket_et()
asker1.puan_kazan()
asker1.puan_kaybet()

# Aynı şekilde öteki İşçi() ve Yönetici() sınıflarını da örnekleyip kullanabiliriz.