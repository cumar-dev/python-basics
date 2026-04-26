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


# set

nums = {1, 2, 2, 3, 4};
print(nums);

# No index (important!)
nums = {10, 20, 30}

print(nums[0])  # ❌ ERROR

# 🔹 Add items

nums.add(10);

tags = {"python", "code", "python", "learn"}
print(tags);

tags.add("fun");
print(tags);

tags.remove("learn");
print(tags);

a = {1, 2, 3, 3};
b = {4, 5, 6};

print(a | b);

print("intersection", a & b);

letters = ["a", "b", "a", "c", "b"]

unique_letters = set(letters)
print(unique_letters)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


print(a & b)

print(a - b)