hours = input("Hours :")
hrs = float(hours)
rate = input("Rate :")
rt = float(rate)

def computepay(hrs,rt):
    if hrs > 40:
        gt=(hrs-40)*rt*0.5
        lt=hrs*rt
        pay = gt + lt
    else:
        pay = hrs*rt
    return pay

p = computepay(hrs,rt)
print(p)
