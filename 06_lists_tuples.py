# =====================================================
# TOPIC 6: LISTS AND TUPLES
# Creation, Indexing, Slicing, Methods, Differences
# =====================================================

# =================== LISTS ===================
# A list is an ORDERED, CHANGEABLE (mutable) collection that allows duplicates.

# ---------- 1. CREATING A LIST ----------
fruits = ["apple", "banana", "mango", "apple"]
print(fruits)

mixed_list = [1, "hello", 3.14, True]   # lists can hold different data types
print(mixed_list)


# ---------- 2. INDEXING AND SLICING (same rules as strings) ----------
print(fruits[0])      # apple
print(fruits[-1])     # apple (last item)
print(fruits[1:3])    # ['banana', 'mango']


# ---------- 3. MODIFYING A LIST (lists ARE mutable) ----------
fruits[1] = "orange"
print(fruits)          # banana replaced with orange


# ---------- 4. COMMON LIST METHODS ----------
nums = [5, 3, 8, 1, 9]

nums.append(10)        # adds item at the end
print(nums)

nums.insert(2, 100)    # inserts 100 at index 2
print(nums)

nums.remove(3)         # removes the first occurrence of value 3
print(nums)

nums.pop()             # removes and returns the LAST item
print(nums)

nums.pop(0)            # removes item at given index
print(nums)

nums.sort()            # sorts the list in ascending order
print(nums)

nums.sort(reverse=True)   # sorts in descending order
print(nums)

nums.reverse()         # reverses the order of the list
print(nums)

print(len(nums))       # length of the list
print(nums.count(8))   # counts occurrences of a value
print(nums.index(8))   # finds index of first occurrence

nums.clear()           # removes all elements
print(nums)            # []


# ---------- 5. LIST COMPREHENSION ----------
# A short and elegant way to create lists

squares = [x ** 2 for x in range(1, 6)]
print(squares)          # [1, 4, 9, 16, 25]

even_nums = [x for x in range(1, 11) if x % 2 == 0]
print(even_nums)        # [2, 4, 6, 8, 10]


# ---------- 6. LOOPING THROUGH A LIST ----------
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Looping with index using enumerate()
for index, color in enumerate(colors):
    print(index, color)


# ---------- 7. COPYING A LIST ----------
list1 = [1, 2, 3]
list2 = list1.copy()    # creates a real copy (changes in list2 won't affect list1)
list2.append(4)
print(list1)             # [1, 2, 3]
print(list2)             # [1, 2, 3, 4]


# =================== TUPLES ===================
# A tuple is an ORDERED, UNCHANGEABLE (immutable) collection that allows duplicates.
# Tuples are faster than lists and used when data should NOT change.

# ---------- 8. CREATING A TUPLE ----------
my_tuple = (1, 2, 3, "Python")
print(my_tuple)

single_tuple = (5,)    # NOTE: comma is required to make a single-item tuple
print(type(single_tuple))


# ---------- 9. ACCESSING TUPLE ITEMS ----------
print(my_tuple[0])     # 1
print(my_tuple[-1])    # Python
print(my_tuple[1:3])   # (2, 3)


# ---------- 10. TUPLES ARE IMMUTABLE ----------
# my_tuple[0] = 100   # This will cause an ERROR, tuples cannot be changed


# ---------- 11. TUPLE METHODS ----------
t = (1, 2, 2, 3, 4)
print(t.count(2))      # counts occurrences -> 2
print(t.index(3))      # finds index of value -> 3
print(len(t))           # length of tuple


# ---------- 12. UNPACKING A TUPLE ----------
a, b, c = (10, 20, 30)
print(a, b, c)


# ---------- 13. WHY USE TUPLE OVER LIST? ----------
# - Tuples are faster than lists
# - Tuples protect data from accidental changes
# - Use tuple for FIXED data (like coordinates, days of week)
# - Use list for data that needs to CHANGE (add/remove items)
