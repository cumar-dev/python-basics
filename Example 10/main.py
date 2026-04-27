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
    