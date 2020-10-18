#first 200 units 8ps per units
#for next 100 units 90ps per units
#beyond 300 units 1ru per units
#all users are chrged for a minimum of 100ru as metre charge. if total ammount is more than 400ru additional charge of 15% of total ammount is charged

name = input("Enter your name here: ")
units = int(input("Enter the number off units consumed: "))

if units < 200:
    a = 80*units+100
    print(f"Total bill of {name} is {a}")
elif units < 300:
    a = (80*200)+(units-200)*90+100
    print(f"Total bill of {name} is {a}")
elif units > 300:
    a = (80*200)+(units-200)*90+(units-300)*100+100
    print(f"Total bill of {name} is {a}")
print("Thank you")    

