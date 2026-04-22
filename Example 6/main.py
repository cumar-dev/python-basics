# controll flow if, elif, and else
asignment = True;
if asignment != True:
    print('your are not clever student');
elif asignment == True:
    print('you are clever student');
else:
    print("just normal");

grade = -10;
if grade > 100:
    print("100 wixii ka badan lama aqbali karo grade kaadu waa in uu u dhexeeya 0-100")
elif grade >= 95 and grade <= 100:
    print('grade kaagu waa A+');
elif grade >= 90 and grade <= 95:
    print("grade kaagu waa A");
elif grade >= 85 and grade <= 90:
    print("grade kaagu waa A-");
elif grade >= 80 and grade <= 85:
    print("grade kaagu waa B+");
elif grade >= 75 and grade <= 80:
    print("grade kaagu waa B");
elif grade >= 70 and grade <= 75:
    print("grade kaagu waa B-");
elif grade < 0:
    print("lambarka aad soo gelinaysid waa in uu u dhexeeyaa 1-100");
else:
    print("waa dhacday");


hungry = input("Are you hungry? (yes/no): ")
money = input("Do you have money? (yes/no): ")

if hungry == "yes" and money == "yes":
    print("Buy food")
elif hungry == "yes" and money == "no":
    print("Go home")
else:
    print("Do nothing")

# nested conditions

is_student = True
has_id = False

if is_student and has_id:
    print("Access granted")
else:
    print("Access denied")

age = 20
has_ticket = False

if age >= 18:
    print("Legend");
    
    if has_ticket:
        print("welcome to the show");
    else:
        print("you need a ticket");
else:
    print("coach waa yar tahay");


