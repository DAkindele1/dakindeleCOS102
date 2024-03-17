p = float(input("Please input your principle amount... "))
r = float(input("Please input your value of rate... "))
t = float(input("Please input your time in number of years... "))
n = float(input("Please input the number of times the interest is compounded annually... ")) 
pmt = float(input("Please input the value of periodic payment... "))
a = float(p * (1 + ((r/100) * t)))
ca = float(p * ((1 + (r/n)))**(n*t))
ap = float(pmt * (((1+(r/t))**(n*t) - 1) / (r/n)))
q = int(input("Please input the calculation you want to make: 1 = Simple Interest, 2 = Compound Interest, 3 = Annuity Plan "))
if q == 1 :
    print("Your Simple Interest is", a)
elif q == 2 :
    print("Your Compound Interest is", ca)
elif q == 3 :
    print("Your Annuity Plan is", ap)
else:
    print("Invalid inpu,! Please enter 1, 2, or 3 for the calculation you want to mak....")