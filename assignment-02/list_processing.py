data_list = [33, 26, 17, 29, 56, 45, 77, 88, 42, 31]

multi_dim_list = []
for i in range(0, len(data_list), 4):
    multi_dim_list.append(data_list[i:i+4])


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


prime_cubes = [x**3 for x in data_list if is_prime(x)]

data_list.insert(-1, 100)

start_list = data_list[:4]
end_list = data_list[4:7]
merged_list = start_list + end_list

print("Multi-dimensional list:", multi_dim_list)
print("Cubes of prime numbers:", prime_cubes)
print("Updated data_list:", data_list)
print("Merged list:", merged_list)
