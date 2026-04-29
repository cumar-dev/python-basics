# function

def greet():
    print("hello");
greet();

def greet(name):
    print("Hello "+name);
greet("omar", );

def add(a,b):
    return a + b;
result = add(3, 4);
print("addition of result: ", result);

def greet(name = "Guest"):
    print("Hello", name);
greet();
greet("adnaan");

def info(name, age):
    print(name, "is", age, "years old");
info("omar", 21);

def calc(a,b):
    return a+b,a*b;
sum_product = calc(2, 3);
print(sum_product);

def total(*numbers):
    return sum(numbers);
print(total(1, 2, 3, 4));

def showInfo(**data):
    for k,v in data.items():
        print(k, ":", v);
showInfo(name="Omar", age=20);


def check_even(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
print(check_even(10)); 

def square(n):
    return n * n;
print(square(7));

def shout(text):
    print(text.upper());
shout("omar");

def power(base, exponent):
    return base ** exponent

print(power(2, 3))
print(power(exponent=3, base=2))

def introduce(first, last):
    print(first, last);
introduce("omar", "abdi");

def is_even(n):
    if n % 2 == 0:
        print("true")
    else:
        print("false");
print(is_even(11));    

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print(max_of_two(7, 10));

def divider(a, b = 1):
    return a / b;
print(divider(10));
print(divider(10, 2));

def total(*numbers):
    s = 0;
    for n in numbers:
        s+=n
    return s
  
print(total(1, 2, 3))