# List
coureses = ["HTML", "CSS", "JAVASCRIPT", "REACT"];
print(coureses[0], coureses[3]);
coureses.append("Node.js");
print(coureses);
coureses.remove("CSS");
print(coureses);
coureses.pop();
print(coureses);
print(len(coureses));

# tuple

city = ("mogadisho", "wanlaweyn");
x,y = city;

print("x =", x, "y =", y);

for c in city:
    print(c);

# set

words = ["go", "python", "go", "code", "python"];

unique_words = set(words);
print(unique_words);

if "python" or "css" in unique_words:
    print("one of them get");
else:
    print("no each of them get");


# dictionary

phone_book = {
    "Ali": "0612345678",
    "Amina": "0623456789",
    "Omar": "0634567890"
}

print("looking existing names");

print("Ali: ", phone_book.get("Ali", "unknown"));

print("\nLookup missing name:")

print("Hodan: ", phone_book.get("Hodan", "unknown"));

for keys in phone_book.keys():
    print(keys);

for values in phone_book.values():
    print(values);

for name, number in phone_book.items():
    print(name, "->", number);
    

# loop

num = [1, 2, 3, 4, 5];

for n in num:
    print("n: ", n);

for n in range(4):
    print(n);

for n in range(1, 10):
    print(n);

names = ["Ana", "Bo", "Cy"];

for i, name in enumerate(names):
    print(i, names);


scores = {"Ana": 90, "Bo": 88}
for name in scores:
    print(name, scores[name]);

for name, score in scores.items():
    print(str(name) + ": " + str(score));


# Iterate and slice (for + range + enumerate)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::-1]);

for n in numbers:
    print(n)

for n in range(8):
    print(n)

nums = list(range(10))
print(nums[::2])

nums = list(range(9));
print(nums[::3]);

for n in range(3, 8):
    print(n);

words = ["go", "python", "code"];

for index, word in enumerate(words):
     print(f"{index}: {word}")


profile = {
    "name": "omar",
    "email": "omar@gmail.com",
    "age": 20,
    "location": "mogadisho"
}

for key, value in profile.items():
    print(key, ": ", value);

