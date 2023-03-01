class ang():
    def __init__(self, rawang):
        if isinstance(rawang,str):
            self.ang = rawang.split(";")
            for i in range(3):
                if self.ang[i] == "":
                    self.ang[i] = 0
                else:
                    self.ang[i] = int(self.ang[i])
        else:
            self.ang = rawang
    def __repr__(self):
        return str(self.ang)
    def goodstr(self):
        return str(self.ang[0])+"°"+ str(self.ang[1]) + "'" + str(self.ang[2]) + '"'
    def __str__(self):
        restr = str(self.ang[0])
        return str(self.ang[0])+";"+ str(self.ang[1]) + ";" + str(self.ang[2])
    def __add__(self, another):
        newang = str(self.ang[0] + another.ang[0]) + ";" + str(self.ang[1] + another.ang[1]) + ";" + str(self.ang[2] + another.ang[2])
        return ang(newang)
    def __sub__(self, another):
        newang = str(self.ang[0] - another.ang[0]) + ";" + str(self.ang[1] - another.ang[1]) + ";" + str(self.ang[2] - another.ang[2])
        return ang(newang)
    def abs(self):
        return ang([abs(i) for i in self.ang])
    def __truediv__(self,num):
        return ang([i/num for i in self.ang])
    def reverse(self):
        return ang(-i for i in self.ang)
    def latex(self):
        return r"\ang{" + str(self) + "}"

def measure1():
    phi0 = ["275;38;","95;40;","275;39;","95;40;","275;39;","95;41;"]
    thetay = [["295;54;","115;59;","295;54;","115;58;","295;54;","115;59;"],
    ["255;26;","75;26;","255;26;","75;26;","255;26;","75;26;"],
    ["295;60;","115;65;","295;60;","115;64;","295;60;","115;64;"],
    ["255;20;","75;20;","255;20;","75;20;","255;20;","75;21;"]]
    thetay = [[ang(i) for i in j] for j in thetay]
    phi0 = [ang(i) for i in phi0]
    phiy = [[thetay[i][j] - phi0[j] for j in range(6)] for i in range(4)]

    a = ""
    for i in range(4):
        for j in range(3):
            g1 = thetay[i][2*j] - phi0[2*j]
            g1 = g1.abs()
            g2 = phi0[2*j+1] - thetay[i][2*j+1]
            g2 = g2.abs()
            a += thetay[i][2*j].latex()
            a += "&"
            a += g1.latex()
            
            a += "&"
            a += thetay[i][2*j+1].latex()
            a += "&"
            a += g2.latex()
            a += "&"
            a += ((g1+g2)/2).latex()
            a += "\n"
    
    print(a.replace(".0","").replace(";0}",";}").replace(".5;",";30"))
    
measure1()
#123