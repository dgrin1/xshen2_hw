#exec(open("./ev.py").read())

#### code to ask user energy level, and out put folating output point values
n=input("what energy level n you would like to?")
n=int(n)
energy=-13.6/n**2
print("the energy of this level is", energy)
