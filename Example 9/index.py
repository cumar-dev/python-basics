# dictionary

person = {
    "name": "omar",
    "age": "20",
    "city": "mogadisho"
}

print(person);

print(person["name"]);
print(person["city"]);

# 🔹 Add or update values

person["country"] = "somalia";
person["age"] = 21;
print(person);

print(person.keys());
print(person.values());
print(person.items());

person.update({"name": "cumar cade"});
print(person);

person.pop("age");
print(person);

print(person.get("name"));