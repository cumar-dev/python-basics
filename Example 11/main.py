for n in range(1, 6):
    if n == 3:
        break
    print(n);

for n in [1, 2, 3, 4, 5]:
    if n == 4:
        print("stopping at 4")
        break
    print(n)


for n in range(6):
    if n % 2 == 0:
        continue
    print("odd:", n)


number = (1,2,3,4,5,6);

for n in number:
   if n %2 == 0:
       print("even: ", n)
   else:
       print("odd: ", n)    


for n in range(1, 6):
    if n == 3:
        break
    print(n)

for n in range(1, 6):
    if n == 3:
        continue
    print(n)    


for n in range(1, 4):
    if n == 2:
        pass
    print(n)   


while True:
    text = input("Enter something (type 'exit' to stop): ")
    
    if text == "":
        continue   # skip empty input
    
    if text == "exit":
        break      # stop loop
    
    pass           # placeholder (not needed here)
    print("You said:", text)

for n in range(20):
    if n == 5:
        print("stopping 5")
        break
    print(n);    

for n in range(10):
    if n == 3:
        continue
    print(n);
if False:
    pass

print("Program still runs fine")