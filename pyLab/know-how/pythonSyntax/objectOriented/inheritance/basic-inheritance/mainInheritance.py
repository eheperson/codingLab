import oyuncularInheritance as oyuncular

asker1 = oyuncular.Asker('Ahmet', 'İstihkamcı')

işçi1 = oyuncular.İşçi('Mehmet', 'Usta')
yönetici1 = oyuncular.Yönetici('Selim', 'Müdür')

asker1.hareket_et()
işçi1.puan_kaybet()
yönetici1.puan_kazan()

