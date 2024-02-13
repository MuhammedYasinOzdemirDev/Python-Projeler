class xox():
     def __init__(self):
        self.tahta=[["","",""],["","",""],["","",""]]
        self.durum=True
        self.x=0
        self.o=0
        self.hamle=1
        self.d=[0,0,0]
        self.e=[0,0,0]
     def menu(self):
        print("""
         1     2     3   
        
   1     {a}   {b}   {c}
        
   2     {d}   {e}   {f}
        
   3     {g}   {h}   {i}
        
        """.format(a=self.tahta[0][0],b=self.tahta[0][1],c=self.tahta[0][2],d=self.tahta[1][0],e=self.tahta[1][1],f=self.tahta[1][2],g=self.tahta[2][0],h=self.tahta[2][1],i=self.tahta[2][2]))
     def secim(self):
         while True:
             print("{}- hamle\n".format(self.hamle))
             satir=int(input("satir numarasini giriniz:"))
             sutun = int(input("sutun numarasini giriniz:"))
             if satir <=3 and sutun<=3:
                if self.hamle%2==0:
                    if self.tahta[satir - 1][sutun - 1] == "":
                       self.tahta[satir-1][sutun-1]="x"
                       self.hamle+=1
                       break
                    else:
                        break
                else:
                    if self.tahta[satir-1][sutun-1]=="":
                     self.tahta[satir-1][sutun-1]="o"
                     self.hamle+=1
                     break
                    else:
                      break

             else:
              print("(1-3) arasinda satir sutun degerleri giriniz lutfen")
     def program(self):
         self.menu()
         self.secim()
         self.kontrol()
     def kontrol(self):
         for i in range(3):
             a=[]
             for j in range(3):
                 a.append(self.tahta[i][j])
             if a[0]==a[1] and a[1]==a[2] and a[0]!="" and self.d[i]!=1:
                 if a[0]=="x":
                     self.x+=1
                     self.d[i]=1
                 else:
                     self.o+=1
                     self.d[i]=1
         for i in range(3):
             a = []
             for j in range(3):
                 a.append(self.tahta[j][i])
             if a[0] == a[1] and a[1] == a[2] and a[0]!="" and self.e[j]!=1:
                 if a[0] == "x":
                     self.x+= 1
                     self.e[j]=1
                 else:
                     self.o += 1
                     self.e[j]=1
         if self.tahta[0][0]==self.tahta[1][1] and self.tahta[1][1]==self.tahta[2][2] and self.tahta[0][0]!="":
             if self.tahta[0][0]=="x":
                 self.x+=1
             else:
                 self.o+=1

         elif self.tahta[0][2]==self.tahta[1][1] and self.tahta[1][1]==self.tahta[2][0] and self.tahta[0][2]!="":
             if self.tahta[0][0]=="x":
                 self.x+=1

             else:
                 self.o+=1

         print("x: {}\no:{}".format(self.x,self.o))
         for i in range(3):
             for j in range(3):
                 if self.tahta[i][j]!="":
                     c=1
                 else:
                     c=0
         if c==1:
             self.durum=False
oyun=xox()
while oyun.durum:
 oyun.program()
