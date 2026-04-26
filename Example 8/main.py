# tuble It cannot be changed (immutable)
numbers = (1, 2, 3, 4);
print(numbers);
print(numbers[0]);
print(numbers[3]);

for n in numbers:
    print(n);

point = (10, 20);

x,y = point;

print("x =", x, "y =",y);