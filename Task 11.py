t=int(input("enter the price"))

if t>250 and t<500:
    print("Recliners")
elif t>200 and t<250:
    print("Platinum")
elif t>150 and t<200:
    print("Gold")
elif t>100 and t<150:
    print("Silver")
else:
    print("Balcony")
