count = 0
s = input()
s = s.lower()
for char in s:
    if char in ('a','e','i','o','u','y','ä','ö'):
        count = count + 1

print(f'Number of vowels: {count}')