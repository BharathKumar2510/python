month=str(input("enter the month:"))
day=int(input("enter the day:"))
month1=month.lower()
if month1=="march":
    if day>=20:
        print("season is summer")
    else:
        print("season is spring")
elif month1=="june":
    if day>=21:
        print("season is fall")
    else:
        print("season is summer")
elif month1=="september":
    if day>=22:
        print("winter")
    else:
        print("season is fall")
elif month1=="december":
    if day>=21:
        print("spring")
    else:
        print("season is winter")
else:
    print("invalid input")
