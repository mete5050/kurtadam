import os
import random

kurtadam=(
'Kurtadam\n\n'
'Geecleri uyanırsın ve arkadaşlarınla beraber bir kurbanı öldürmeye karar verirsin. '
'Gündüzleri normal bir köylü gibi görünmeye ve kendini öldürtmemeye çalışırsın.    '  
)

gozcu=(
'Gözcü\n\n'
'Her gece başka bir oyuncunun rolünü ortaya çıkartmaya çalışırsın.'  
)

doktor=(
'Doktor \n\n'
'Gece bir oyuncuyu uyandırır ve seçersin,bu oyuncu o geec kurtadam tarafından'
'öldürülmez. Aynı oyuncuyu üstü üste 2 gece kurtaramazsın.  '  
)

avcı=(
'Avcı\n \n'
'Öldüğün zaman seninle birlikte  ölecek kişiyi seçebilirsin.  \n '  
)

cadı=(
'Cadı\n \n'
'Gece boyunca kullanabileceğin iki iksirin var:   \n ' 
'Biri bir oyuncunun kurtadamlar tarafından ölmesini önlüyor,\n'
'diğeri ise bir oyuncuyu öldürüyor.\n' 
)

papaz=(
'Papaz \n\n'
'Kutsal suyu başka bir oyuncu üzerinde kulanabilirsin.Eğer o oyuncu kurt adam ise \n' 'ölür, kurtadam değilsesen ölürsün.Bunu sadece bir defa yapabilirsin.  \n '  
)

auragozcu=(
'Aura Gözcüsü\n\n'
'Her gece kurtadam olup olmadığını anlamak için bir oyuncu seçersin. \n \n '  
)

sarhos=(
'Sarhoş \n\n'
'Çok sarhoşsun ve oyun boyunca konuşamazsın.  \n   '  
)


krktrlr=[kurtadam,gozcu,doktor,avcı,cadı,papaz,auragozcu,sarhos]
kulkrktr=[]

global kullanicilar
kullanicilar=[]

oyuncus=int(input("Oyuncu sayısını girin : "))

def kulekle():
    kullanici = input("Kullanıcı adını giriniz : ")
    kullanicilar.append(kullanici)

x = 1
while (x<=oyuncus):#kullanıcı sayısı kadar kullancı ekliyoruz
    kulekle()
    x+=1


a = 1
while (a<=oyuncus):
    kulkrktr.append(random.choice(krktrlr))
    a+=1

y = 1x

oyun = True
while oyun:
    Dur=input("Cihazı oyuncu "+str(y)+"'e verin")
    os.system("clear")
    print(kulkrktr[y-1])
    y +=1
    if(y > int(len(kulkrktr))):
        oyun = False

    
