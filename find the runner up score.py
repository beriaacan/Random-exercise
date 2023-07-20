marks = {}
n = int(input()) #ogrenci sayisi

for x in range(n):
    name = input() #ogrenci adi olan sozluk
    mark = float(input()) #ogrenci notu olan sozluk
    
    if mark in marks:
        marks[mark].append(name)  #eger not zaten varsa ogrenciler sozlugunde adı ayni listeye eklenir
    else:
        marks[mark] = [name] #yoksa yeni olusturulur
        
all_marks = list(set(marks.keys())) #tum notlarin oldugu liste olusturuldu
all_marks.sort() #siralama

names_ordered = marks[all_marks[1]] #(x,y) y kismini alir gibi düsün notlara bakiyoruz
names_ordered.sort()

for name in names_ordered:
    print(name)
