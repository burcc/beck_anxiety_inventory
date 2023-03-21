sorular = ["1. Bedeninizin herhangi bir yerinde uyuşma veya karıncalanma \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"2. Sıcak/ ateş basmaları \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"3. Bacaklarda halsizlik, titreme \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"4. Gevşeyememe \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"5. Çok kötü şeyler olacak korkusu \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"6. Baş dönmesi veya sersemlik \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"7. Kalp çarpıntısı \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"8. Dengeyi kaybetme duygusu \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"9. Dehşete kapılma \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"10. Sinirlilik \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"11. Boğuluyormuş gibi olma duygusu \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"12. Ellerde titreme \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"13. Titreklik \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"14. Kontrolü kaybetme korkusu \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"15. Nefes almada güçlük \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"16. Ölüm korkusu \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"17. Korkuya kapılma \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"18. Midede hazımsızlık ya da rahatsızlık hissi \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"19. Baygınlık \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"20. Yüzün kızarması \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım",
"21. Terleme (sıcaklığa bağlı olmayan) \nHiç \nHafif düzeyde.Beni pek etkilemedi \nOrta düzeyde Hoş değildi ama katlanabildim \nCiddi düzeyde, dayanmakta çok zorlandım"
]

score = 0
sonucListem = []

class Beck_Anxiety:
    
    def soruyuGoster (self, num = 1):
        
        cevaplar = []
        index = 0
        print("Hoşgeldin. Hangi envanteri uygulamak istersin?\n1.Beck Kaygı Envanteri")
        num = input("Lütfen uygulamak istediğin envanter numarasını gir: ")
        
      
        print("Beck Kaygı Envanteri Toplam 22 Sorudan oluşuyor.\nSoruların doğru bir cevabı yok.\nLütfen seni en iyi tanımlayan seçeneği seç.")
        basla = input("Başlamak için E'ye bas: ")
            
    
        if (basla == "E" or "e"):
            while  (index < 22):
            
                print(sorular[index])
                guess = int(input("1, 2, 3 ya da 4ü seçin: "))
                char = [1,2,3,4]
                
                if guess in char:
                    cevaplar.append(guess)
                    index +=1
        
                    if index == 21:
                        print(f"Verdiğin cevaplar {cevaplar}")
                        break
                else:
                    print("Hatalı girdin.")
    
            global score
            for item in cevaplar:
                score = score + item
    
            return print(f"Toplam puanın: {score}")
    def sonucumuKaydet(self, score):
        
        myData = sonucListem.append(score)
        
    def sonucumuGoster(self):
        return print(sonucListem)
        
        
    

yeni = Beck_Anxiety()

yeni.sonucumuKaydet(23)
yeni.sonucumuKaydet(21)
yeni.sonucumuKaydet(34)
yeni.sonucumuKaydet(45)
yeni.sonucumuKaydet(12)
yeni.sonucumuGoster()
yeni.soruyuGoster()






