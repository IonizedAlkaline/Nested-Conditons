units = int(input("Enter the amount of units:"))
if units < 50:
    print("The per-unit cost for less than 50 units is 2.60 and the tax is 25, so the cost for",units,"will be",units*2.60 + 25)
if units <= 100:
    print("The per-unit cost for less than or equal to 100 units is 3.25 and the tax is 35, so the cost for",units,"will be",(units-50)*3.25 +35+50*2.60)
if units <= 200:
    print("The per-unit cost for less than 200 units is 5.26 and the tax is 45, so the cost for",units,"will be",(units-100)*5.26 + 45+50*2.60+50*3.25)
else:
    print("The per-unit cost for greater than 200 units is 8.454 and the tax is 75, so the cost for",units,"will be",(units-200)*8.45 + 75+50*2.60+50*3.25+100*5.26)