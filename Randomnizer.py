f = open("SpO2.txt","w")

for i in range(100):
    f.write(s.SpO2Generator()+"\n")

f.close()

