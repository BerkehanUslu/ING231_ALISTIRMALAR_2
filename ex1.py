import random

sayi = random.randint(10,98)
s_sayi = str(sayi)
#sayi degiskenini stringe donusturduk.

while s_sayi[0] == s_sayi[1]:
    sayi = random.randint(10,98)
#programin dogru bir sayi uretmesi saglanir.

tahmin = input('Bir sayi girin: \n')
while int(tahmin)<10 or int(tahmin)>98 or tahmin[0] == tahmin[1]:
    tahmin = input("Lutfen nizami bir sayi giriniz: \n")

#oyuncunun girdigi sayi kontrol edilir.
#input fonksiyonu girdi argumanlarini string olarak atadıgı icin, if statement
#icinde kullanabilmek icin str ifadeyi int bir ifadeye cast ettik.

counter=0
n_counter=0
#counter dogru yer sayacidir.
#n_counter, yanlis yer sayacidir.

if (tahmin[0] == s_sayi[0]) :
    counter+=1
if (tahmin[1] == s_sayi[1]):
    counter+=1
if (tahmin[0] == s_sayi[1]):
    n_counter-=1
if (tahmin[1] == s_sayi[0]):
    n_counter-=1

print("Dogru yer sayaci: {}".format(counter))
print("Yanlisyer sayaci: {}".format(n_counter))
#kullanicinin soyledigi sayi ile rastgele tutulan sayi karsilastirilir.
    



    
        

