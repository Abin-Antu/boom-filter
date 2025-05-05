from bitarray import bitarray
import hashlib

def create_bloom_filter(size):
    bit_array = bitarray(size)
    bit_array.setall(0)
    return bit_array

def generate_hashes(item, size, hash_count):
    hashes = []
    for i in range(hash_count):
        hash_result = hashlib.md5((item + str(i)).encode()).hexdigest()
        hashes.append(int(hash_result, 16) % size)
    return hashes

def add_to_bloom_filter(bit_array, item, size, hash_count):
    for hash_value in generate_hashes(item, size, hash_count):
        bit_array[hash_value] = 1

def check_bloom_filter(bit_array, item, size, hash_count):
    return all(bit_array[hash_value] for hash_value in generate_hashes(item, size, hash_count))

size = 100
hash_count = 3

bloom_filter = create_bloom_filter(size)

add_to_bloom_filter(bloom_filter, "apple", size, hash_count)
add_to_bloom_filter(bloom_filter, "banana", size, hash_count)

print(check_bloom_filter(bloom_filter, "apple", size, hash_count))
print(check_bloom_filter(bloom_filter, "banana", size, hash_count))
print(check_bloom_filter(bloom_filter, "cherry", size, hash_count))