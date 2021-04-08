
import numpy as np
import pandas as pd

def sepBot(val = "---------------------------"):
    print("------" + val + "------------")
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------------------------------------")
    
# Create Series From list and Dists

x = [1,2,3,4,5]
print(pd.Series(x))
print("")

x2 = ['london','madrid','barcelona', 'germany', 'egypt']
print(pd.Series(x2))
print("")

x3 = [True, True, False, False, True, True]
print(pd.Series(x3))
print("")

x4 = {"tr":18,
        "ts":20,
        "tp":30}
print(pd.Series(x4))
print("")

print(pd.Series(x2).values)
print(pd.Series(x2).index)

print(pd.Series(x2).dtype)
print(pd.Series(x).dtype)

print(pd.Series(x2).shape)
print(pd.Series(x).shape)

x5 = pd.Series(x2)
x5.name="enivici"

print(x5.head())


## methods, parameters, arguments

years = [2015,2016,1017,2018,2020]
incom=[2,3,4,4,7]

s1 = pd.Series(data=years, index=incom)
print(s1)

s2 = pd.Series(data=incom, index=years)
print(s2)

numbers = [1,2,3,4,5,6,7,8,9]

s3 = pd.Series(numbers)
s3.name="numbers"
print(s3)

print("sum : ", s3.sum())
print("max : ", s3.max())
print("min : ", s3.min())
print("product : ", s3.product())
print("mean : ", s3.mean())

### read_cvs(), head(), tail()

print("\n\n Titanic Data Set : \n")
data1 = pd.read_csv("../data/titanic_csv_data/titanic.csv")
print(data1)

print("\n\n Titanic Data Set (Squezeed) : \n")
data2 = pd.read_csv("../data/titanic_csv_data/titanic.csv", squeeze=True)
print(data2)

print("\n\n milligelir.csv : \n")
data3 = pd.read_csv("../data/other/milligelir.csv")
print(data3)
print(data3.head(10)) #default 5
print(data3.tail(7)) #default 5


############################################
## Built-In Function

ulke = pd.read_csv("../data/other/ülke.csv", squeeze=True)
gelir = pd.read_csv("../data/other/milligelir.csv", squeeze=True)

print(type(ulke))
print(sorted(gelir))
print(list(ulke))
print(dict(ulke))
print(min(gelir))

############################################
## sort_values(), inplace, in

print(ulke.sort_values().head())
print(gelir.sort_values())
print(gelir.sort_values(ascending=True))#kucukten buyuge siralar

gelir.sort_values(ascending=True, inplace=True) #uzerine yazar

print(gelir)

print(gelir.sort_index()) ## index e gore siralar

print("ABD" in ulke) ##eleman icinde mi

#################################################3
### Indexleme ve matematik

ulke = pd.read_csv("../data/other/ülke.csv", squeeze=True)
gelir = pd.read_csv("../data/other/milligelir.csv", squeeze=True)

#indeksleme
print(ulke[0])
print(ulke[0:10])
print(ulke[5:])

print(gelir.count())
print(len(gelir))
print(gelir.sum())
print(gelir.mean())
print(gelir.std())
print(gelir.max())
print(gelir.min())
print(gelir.median())
print(gelir.describe())

#################################################3
### value_counts() apply() idxmax() idxmin()

kita = pd.read_csv("../data/other/kıta.csv", squeeze=True)
gelir = pd.read_csv("../data/other/milligelir.csv", squeeze=True)

print(kita.value_counts())
print(kita.value_counts(ascending= True))

print(gelir.idxmin())
print(gelir.min())
print(gelir.idxmax())
print(gelir.max())

##apply() fonksiyon uygulamaya yariyor, bunun icin fonksiyon tanimlamaliyiz

def sinif(gel):
    if gel<2000000:
        return "orta"
    elif gel >= 2000000 and gel<5000000:
        return "yuksek"
    else:
        return "cok yuksek"    

print(gelir.apply(sinif))

print(gelir.apply(lambda  gelir:gelir*2))

#################################################3
### DATAFRAME

dunya = pd.read_csv("../data/other/dünya.csv", squeeze=True)
gelir = pd.read_csv("../data/other/milligelir.csv", squeeze=True)
ulke = pd.read_csv("../data/other/ülke.csv")


print(dunya)
print(dunya.head())
print(dunya.tail())
print(dunya.shape)
print(dunya.columns)
print(dunya.axes)
print(dunya.info)
print(dunya.info()) #ne kadar hafiza kaplivor bilgileri vs.

print(dunya)
dunya = pd.read_csv("../data/other/dünya.csv", index_col='Ülke')
print(dunya)

#################################################3
### DATAFRAME yeni sutun ekleme cikarma degisiklik yapma

dunya = pd.read_csv("../data/other/dünya.csv", squeeze=True)
print(dunya.head())
print(dunya[["Ülke", "KITA"]].head())

dunya["Sıralama"] = "top 20"
print(dunya)

dunya.insert(2, column = "gelirler", value="yuksek cok")
print(dunya)

dunya["Gelir"] /= 100000
print(dunya)

dunya["gelir_tr"] = dunya["Gelir"] * 4.75
print(dunya)

print(dunya["KITA"].value_counts())
print(dunya["KITA"].value_counts(ascending=True))

#################################################3
### dropna() fillna() astype() rank()

#dropna() NaN degerlerini siler
# any belirtilir ise eger her hangi bir nan degeri var ise butun satiri siler
# all belirtilmis ise silmesi icin butun satirin nan olmasi gerekiyor
# inplace parametresi ile uzerine yazilabilir
nufus = pd.read_csv("../data/other/dünyanüfusu.csv", squeeze=True)

print(nufus.head(50))

print(nufus.dropna(how="all").head(50))

# belirli bir sutun icin nan iceren satirlari silmek ister isek
print(nufus.dropna(subset=["Doğum oranı"]).head(50))

# nan olan elemanlarin yerine baska bir deger yamak icin
# asagidaki kod nan olan butun elemanlarin yerine 1  yazar
print(nufus.fillna(1).head(50))

print(nufus["Doğum oranı"])
print(nufus["Doğum oranı"].fillna(1))

print(nufus.info())

print(nufus["Sıralama"].head(50))

nufus["Sıralama"] = nufus["Sıralama"].fillna(1.0)
print(nufus["Sıralama"].head(50))

#float degerleri int e ceviriyoruz
nufus["Sıralama"] = nufus["Sıralama"].astype('int')
print(nufus["Sıralama"].head(50))

print(nufus.sort_values("Ortalama yaş", ascending=False))

print(nufus.sort_values(["Ortalama yaş", "km2"], ascending=[True, False]))

print(nufus.sort_index())

print(nufus.sort_index(ascending=False))

nufus = pd.read_csv("../data/other/dünyanüfusu.csv", squeeze=True).dropna(how="any")

# rank ??????????????? complicated
nufus["Yas Siralama"] = nufus["Ortalama yaş"].rank(ascending=False).astype("int")

#################################################3
### Dataframe isin() isnull() notnull()

df = pd.read_csv("../data/other/millitakım.csv", squeeze=True)

print(df["Takım"]=="Fenerbahçe")

takim =  df["Takım"]=="Fenerbahçe"

print(takim)

## Filtreleme
print(df[takim])

print(df["Görev"] == "önlibero")

on = df["Görev"] == "önlibero"
print(df[on])

print(df[takim&on])

yas = df["Yaş"] > 25
print(df[yas])

yas2 = df["Yaş"]| on

print(df[yas2])

print(df[yas & on | takim])

m = df["Takım"].isin(["Fenerbahçe","Kayseri"])
print(df[m])

null = (df["Gol"].isnull())
print(df[null])

not_null = (df["Gol"].notnull())
print(df[not_null])

#################################################3
### Dataframe between() duplicate() drop_duplicate() unique()

df = pd.read_csv("../data/other/millitakım.csv", squeeze=True)

df["Milyon Euro"] = df["Milyon Euro"].astype("float")
print(df)

yas = df["Yaş"].between(20,25)
print(df["Yaş"].between(20,25))
print(df[yas])

milyonE = df["Milyon Euro"].between(5.0,20.0)
print(df["Milyon Euro"].between(5.0,20.0))
print(df[milyonE])

num = df["Numara"].between(5,10)
print(df["Numara"].between(5,10))
print(df[num])

print(df["Görev"])
df1 = df["Görev"].duplicated(keep="first")  # tekrar edenlerin hangisini silsin (sadece bastakini ya da sondakini siler)
print(df[df1])

df_drop = df.drop_duplicates(subset="Görev")
print(df_drop)

df_unique = df["Görev"].unique()
print(df_unique)
print(len(df["Görev"].unique()))

print(df["Görev"].nunique())

#################################################3
### Dataframe set_index() loc[] iloc[]
# indeksleri degistirme

df = pd.read_csv("../data/other/millitakım.csv", squeeze=True)
print(df)
df.set_index("İsim", inplace=True)
print(df)

df.reset_index(inplace=True)
print(df)

df = pd.read_csv("../data/other/millitakım.csv",index_col="Numara" )
print(df)

print(df.loc[3])
print(df.set_index("İsim").loc["Harun Tekin":"Kaan Ayhan"])

#iloc indekslere gore alir
#loc ise verilen degere gore
print(df.iloc[0])
print(df.iloc[3])
print(df.iloc[0:5])

print(df.iloc[0,4])

#################################################3
### Dataframe reanme() drop() pop()
## Will be added later

#################################################3
### Dataframe-sample, nsamllest(), nlargest(), where(), query(), apply(), copy()

df = pd.read_csv("../data/other/millitakım.csv", squeeze=True)
print(df)

print(df.sample(5, axis=0)) # rastege 5 ornek aldi (orneklem olusturdu)

print(df["Yaş"].sort_values())

print(df.nsmallest(3,columns="Yaş")) # Yas Sutunundan en kucuk 3 ornegi alip orneklem olusturur

print(df.nlargest(5,columns="Yaş")) # Yas Sutunundan en buyuk 5 ornegi alip orneklem olusturur

fener = df["Takım"]=="Fenerbahçe"
print(df.where(fener)) #Takimi fenerbahce olanlar disindaki butun degerleri nan a evirir

yas = (df["Yaş"]<30)
print(df.where(yas)) #Yasi 30dan kucuk olanlar disindaki butun degerleri nan a evirir

print(df.where(yas&fener))  #takimi fenerbahce olan ve yasi 30dan kucuk olanlar disindaki butun  degerleri nan yapar

print(df.query('Takım=="Fenerbahçe"'))

print(df.query('Görev=="sol bek"'))

print(df.query('Yaş > 25'))

# apply() fonksiyonu yukarida tanitildi

takimlar = df["Takım"].copy()
takimlar["Harun Tekin"] = "Turkiye"
print(takimlar)
print(df)

#################################################3
### Dataframe groupby()

oyun = pd.read_csv("../data/other/wcplayers.csv", index_col="FIFA Popular Name", squeeze=True)
print(oyun)

# grupby() fonksiyonu ile takimlara bolunur

takim = oyun.groupby("Team")
len(oyun)
len(takim)

oyun["Team"].value_counts

print(takim.first()) #first metodu ilk degerleri verdirir

print(takim.last()) #last metodu son degerleri verdirir

print(takim.get_group("Brazil"))


print(takim.get_group("France"))
print(takim.max())
print(takim.min())
print(takim.sum())
print(takim.mean())

takim = oyun.groupby(["Team", "Club"])
takim.size()

# agg takim icinde islem yapmaya yarar,

takim.agg({"Height":"sum",
            "Weight": "mean"})

########################################################################
# Aggregate using one or more operations over the specified axis.
dftest = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [np.nan, np.nan, np.nan]],
                   columns=['A', 'B', 'C'])
dftest.agg(['sum', 'min'])
dftest.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
dftest.agg("mean", axis="columns")
#######################################################################
df2 = pd.DataFrame(columns=oyun.columns)

oyun = pd.read_csv("../data/other/wcplayers.csv", index_col="FIFA Popular Name", squeeze=True)
takim = oyun.groupby("Team")

print(takim.size())

for ulke,data in takim:
    uzun = data.nlargest(1, "Height")
    df = df.append(uzun)
print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
print(df.head(100))


#################################################3
### Dataframe merge() joint() append()  concat()


ondort = pd.read_csv("../data/other/2014 wc.csv")
on = pd.read_csv("../data/other/2010 wc.csv")
alti = pd.read_csv("../data/other/2006 wc.csv")
onyedi = pd.read_csv("../data/other/fifa2017.csv", index_col="Ülke")
onsekiz = pd.read_csv("../data/other/fifa2018.csv", index_col="Ülke")
kon7 = pd.read_csv("../data/other/fifa2017k.csv")
kon8 = pd.read_csv("../data/other/fifa2018k.csv")


print(alti)
print(onyedi)
print(kon7)
print(kon8)

new1 = pd.concat([ondort, on])
print(new1)

new1 = pd.concat([ondort, on], ignore_index=True)
print(new1)

new1 = pd.concat([ondort, on], keys=["2014", "2010"])
print(new1)

print(new1.loc["2014",2])
print("1243256375869756342312`145263475869")
print(on.append(alti,ignore_index=True))

print("1243256375869756342312`145263475869")
print(on.merge(alti, how="inner", on="Futbolcu"))

print("1243256375869756342312`145263475869")
print(on.merge(alti, how="inner", on="Futbolcu", suffixes=(" - 2010", " - 2006")))


print("1243256375869756342312`145263475869")
print(on.merge(alti, how="inner", on="Futbolcu", suffixes=(" - 2010", " - 2006")))



print("1243256375869756342312`145263475869")
print(onyedi.merge(onsekiz, how="outer", on="Ülke", suffixes=(" - 2017", " - 2018")))

### Outer parametresi ile butun kumeyi inner parametresi ile kesisim kumesini merge edebiliriz

print("1243256375869756342312`145263475869")
print("1243256375869756342312`145263475869")
print(onyedi.join(onsekiz, how="outer", on="Ülke", lsuffix='2017', rsuffix='2018'))

print("1243256375869756342312`145263475869")
print("1243256375869756342312`145263475869")
print("1243256375869756342312`145263475869")

print(onyedi.merge(kon7, how="left", on="Ülke"))

#################################################3
### Dataframe birden fazla indeks kullanma

world = pd.read_csv("../data/other/wcplayers.csv")

print(world)

world.set_index(keys=["Team", "Shirt Name"], inplace=True)
print(world)

print(world.index.names)

sepBot()
print(world.index[0])
sepBot()
val = world.index.get_level_values(0)
print(val)
sepBot()
val = world.index.get_level_values(1)
print(val)

sepBot() 
#index isimlerini degistirme 

world.index.set_names(["TAKIM", "TAKMA ISIM"], inplace=True)
sepBot()
print(world)

sepBot()
print(world.sort_index(ascending=["True", "True"]))

sepBot()
print(world.swaplevel()) #indekslerin yani takim ve takma ismin yerlerini degistirir

sepBot("eee")

world2 = world.stack()
print(world2)

sepBot()
world3 = world.stack().to_frame()
print(world3)

sepBot()
world4 = world3.unstack()
print(world4)


futbol = pd.read_csv("../data/other/pivot.csv")
sepBot("pivot")

print(futbol)

piv = futbol.pivot(index="Futbolcu", columns="Mevsim", values="Gol")

print(piv)

sepBot("Pivot Tables")

pivT1 = futbol.pivot_table(values="Gol", index="Futbolcu", aggfunc="sum")
print(pivT1)

pivT2 = futbol.pivot_table(values="Gol", index="Futbolcu", aggfunc="mean")
print(pivT2)

# pivot_table fonksiyonunun tam tersi islem yaptirma
m = pd.read_csv("../data/other/melt.csv")
sepBot()
print(m)
toPivot = pd.melt(m, id_vars="Futbolcu", var_name="Yıl", value_name="Gol")

print(toPivot)

#################################################3
### Dataframe - text verileri

sepBot()
kupa = pd.read_csv("../data/other/wcplayers.csv")
print(kupa)
print(kupa.info())

kupa["Team"] = kupa["Team"].astype("category")
print(kupa)
print(kupa.info())  #team i category e cevirdikten sonra hafizeda kapladigi yeri kontrol et

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print(kupa["Team"].unique())

# Butun string islemlerinden once str yerlestirmek gerekiyour
print(kupa["FIFA Popular Name"].str.lower())

print(kupa["FIFA Popular Name"].str.upper())

print(kupa["FIFA Popular Name"].str.title())

print(kupa["FIFA Popular Name"].str.len())

kupa2 = kupa.copy()

kupa2["Team"] = kupa2["Team"].str.replace("Argentina", "ARGENTINA MF")

print(kupa2["Team"])

kupa["Birth Date"] = kupa["Birth Date"].str.replace(".","/")

print(kupa["Birth Date"])

manuel =kupa["FIFA Popular Name"].str.lower().str.contains("manuel")
print(kupa[manuel])

inaEnd =kupa["Team"].str.lower().str.endswith("ina")
print(kupa[inaEnd])

fStart =kupa["Team"].str.lower().str.startswith("f")
print(kupa[fStart])

# Text operations
eni = "         enivicivokki        "
print(eni.lstrip())
print(eni.rstrip())
print(eni.strip())

kupa["FIFA Popular Name"] = kupa["FIFA Popular Name"].str.strip()
kupa["Team"] = kupa["Team"].str.strip()
kupa["Club"] = kupa["Club"].str.strip()

kupa = pd.read_csv("../data/other/wcplayers.csv", index_col="Team")
kupa.index = kupa.index.str.strip().str.upper()
kupa.columns = kupa.columns.str.upper().str.strip()
print(kupa)

kupa["FIFA POPULAR NAME"] = kupa["FIFA POPULAR NAME"].str.split(" ").str.get(0).str.title()
kupa["CLUB"] = kupa["CLUB"].str.split(" ").str.get(0).str.title()
print(kupa)
print(kupa["FIFA POPULAR NAME"].value_counts())

kupa = pd.read_csv("../data/other/wcplayers.csv", index_col="Team")
print(kupa["FIFA Popular Name"].str.split(" ", expand=True, n=1)) 
#split ettikten sonra spliid edilmis nesneleri indeksleri ile gosterir

kupa[["son isim", "ilk isim"]] = kupa["FIFA Popular Name"].str.split(" ", expand=True, n=1)
print(kupa)

#################################################3
### Dataframe - Input and Output

d = pd.read_csv("https://data.cityofnewyork.us/api/views/jb7j-dtam/rows.csv?accessType=DOWNLOAD")
print(d)

sepBot("Leading Causes")
print(d["Leading Cause"])

d_state_l = d["Leading Cause"].tolist()
d_state_f = d["Leading Cause"].to_frame()
sepBot("Leading Causes List ")
print(d_state_l)
sepBot("Leading Causes Dataframe")
print(d_state_f)

d.to_csv("../data/New_York_City_Leading_Causes_of_Death.csv", index=False)
d["Leading Cause"].to_csv("../data/New_York_City_Leading_Causes_of_Death_Causes.csv", index=False)
d_state_f.to_csv("../data/New_York_City_Leading_Causes_of_Death_Causes_dataframe_version.csv", index=False)

exceltest = pd.read_excel("../data/other/excel.xlsx", sheet_name=["2006", "2010"]) 
print(exceltest)

dtest = pd.read_csv("../data/other/2014 wc.csv")
dtest.to_excel("2014.xlsx",sheet_name="2014")

fromhtml = pd.read_html("https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/List_of_banks_in_Turkey.html")
print(fromhtml)