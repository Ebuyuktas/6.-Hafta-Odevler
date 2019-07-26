
#tuttugum sayı=17
import random
pc=random.randint(0,100)
list=[0,100]

while True:
    try:
        print("pc tahmini:",pc,"\n")
        deger=input("tahmin yuksekse '-',alcaksa '+',dogru ise '=' işareti giriniz\ncikmak icin 'q'ya basınız:")
        if deger.lower()=="q":
            print("cıkılıyor...")
            break
        if not deger:
            print("**********bos gecmeyelim aub******************\n")
        if deger=="=":
            print("tebrikler bildiniz")
            break
        elif deger=="+":
            list.sort()
            list.pop(0)
            list.append(pc)
            list.sort()
            pc=random.randint(list[0],list[1])
            continue
        elif deger=="-":
            list.sort()
            list.pop(1)
            list.append(pc)
            list.sort()
            pc=random.randint(list[0],list[1])
            continue
    except:
        print("hata olustu")
        
