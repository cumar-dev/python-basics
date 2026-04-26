# 🔹 Accessing Items (Index)
fruits = ["apple", "banana", "orange"];

print("fruits: ", fruits);

print(fruits[0]);

print(len(fruits));
print(fruits[::-1]);
# 🔹 Changing Values

fruits[1] = "mongo";
print(fruits);

# 🔹 Adding Items

fruits.append("grape");

print(fruits);

fruits.insert(1, "kiwi")

print(fruits);

print(fruits[0]);

print(len(fruits));

# 🔹 Removing Items

fruits.remove("mongo");
print(fruits);

fruits.pop();
print(fruits);

fruits.pop(2);
print(fruits);

# reverse list

print(fruits[::-1]);
# slicig meesha laga bilaabay iyo meesha dhamaadka
# 1,3,5,7,9
numbers = [1,2,3,4,5,6,7,8,9,10];
print(numbers[::-1]);
print(numbers[0:3]);

print(numbers[0:4]);

print(numbers[1:3]);

# ilaa booska indexka sedexaad  laga gaaraayo soco

print(numbers[:3]);   

#  indexka labaad wixii ka danbeeyo soco

print(numbers[2:]);

print(numbers[3:]);

print(numbers[::2]);

print(numbers[::3]);

print(numbers[::4]);

print('_________');
# list methods

nums = [1,2,3,]

# 🔹 1. append()

nums.append(4);

print(nums);

# 2. insert()

nums.insert(4, 5);

print(nums);

# 🔹 3. remove()

nums.remove(4);

print(nums);

# 🔹 4. pop()

nums.pop()     # remove last
nums.pop(0)    # remove index 0

print(nums);

# 🔹 6. index()


print(nums.index(3));

# 🔹 5. clear()

nums.clear();

print(nums);

# 🔹 7. count()

nums = [1, 2, 2, 3]

print(nums.count(2))

# 🔹 8. sort()

nums = [5, 2, 8, 1]
nums.sort()

print(nums)

# 🔹 9. reverse()

nums = [1, 2, 3]
nums.reverse()

print(nums);

# 🔹 10. copy()

nums = [1, 2, 3]
new_nums = nums.copy()

print(new_nums)