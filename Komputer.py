import time

class Komputer():
    def __init__(self,cmp_veziyyeti = "sonulu",cmp_ses = 20,ram = 16,ssd = 512):
        self.cmp_veziyyeti = cmp_veziyyeti
        self.cmp_ses = cmp_ses
        self.ram = ram
        self.ssd = ssd

    def komp_ac(self):
        if self.cmp_veziyyeti == "aciq":
            print("Komputer Onsuzda Aciqdir!")
        else:
            print("Komputer acilir...")
            time.sleep(2)
            print("Xos Geldiniz!")
            self.cmp_veziyyeti = "aciq"
    def komp_sondur(self):
        if self.cmp_veziyyeti == "sonulu":
            print("Komputer Onsuzda sonuludur!")
        else:
            print("Komputer Sondurulur...")
            time.sleep(3)
            self.cmp_veziyyeti = "sonulu"
    def __str__(self):
        return "Komputer Veziyyeti: {}\nSes Seviyyesi: {}\nRam: {}\nSSD: {}".format(self.cmp_veziyyeti,self.cmp_ses, self.ram,self.ssd)

    def ses_ayarlari(self):
        while True:
            ses = input("Sesi azalt: <\nSesi artir: >\nMenyuya donmek ucun 'q'\nEmeliniz: ")
            if ses == "<":
                if self.cmp_ses > 0:
                   self.cmp_ses -= 2
                print("Ses: ", self.cmp_ses)
            if ses == ">":
                 if self.cmp_ses < 100:
                    self.cmp_ses += 2
                 print("Ses: ", self.cmp_ses)
            else:
                 print("Cixilir...")
                 break
    def menyu (self):
        while True:
            print("""Programlar:
        
        Qalereya
        
        Chrome
        
        Cixmaq ucun 'q'
        """)
            m = input("Hansi programa girmek isdeyirsiniz?: ")
            if m == "Qalereya":
                print("Qalereyaya girilir...")
                time.sleep(2)
                print("""Qalereya
            
                Sekiller:
            
                *********
                //****///
                *********
            
                ==++++==
                ***+++** 
                ********
                
                
                
                """)
            elif m == "Chrome":
                print("Chrome'a girilir...")
                time.sleep(3)
                print("""Chrome
                Youtube
                Translate
                Wikipedia
                """)
            elif m == "q":
                print("Cixilir...")
                time.sleep(2)
                break
            else:
                print("Mumkun Olmadi...")

komp1 = Komputer()

print("""

1. Komp Yandir

2. Komp Sondur

3. Ses Seviyyesi

4. Komp Hakkinda

5. Menyu

q. Cixmaq
""")

while True:
    emel = input("Emeliniz: ")

    if emel == "1":
       komp1.komp_ac()

    elif emel == "2":
       komp1.komp_sondur()

    elif emel == "3":
        komp1.ses_ayarlari()

    elif emel == "4":
        print(komp1)

    elif emel == "5":
        komp1.menyu()

    elif emel == "q":
        print("Cixilir...")
        break