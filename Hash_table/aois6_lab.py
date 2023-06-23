def get_alphabet_indexes(char):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char = char.lower()  # Convert to lowercase for case-insensitive matching

    if char in alphabet:
        for i, c in enumerate(alphabet):
            if c == char:
                return i
    else:
        return 0

def function_of_hashing(str, number_of_elements):
    str = str.lower()
    result = 0
    length = len(str)
    for chri, el in enumerate(str):
        result += get_alphabet_indexes(el) * pow(26, length - 1 - chri)
    return result % number_of_elements

def add_element(key, elem):
     adding = [key, elem]
     hash = function_of_hashing(key, 5)
     table[hash].append(adding)

def del_element(key):
    hash = function_of_hashing(key, 5)
    elems = [pair[0] for pair in table[hash]]
    keyidx = elems.index(key)
    table[hash].pop(keyidx)

def print_our_table():
    col_count = 0
    for i, bucket in enumerate(table):
        print(f"Bucket {i}:")
        if len(bucket) > 1:
            col_count += 1
        if not bucket:
            print("   <empty>")
        else:
            for key, elem in bucket:
                print(f"   Key: {key} - Element: {elem}")
        print("-" * 100)
    print(f"Number of collisions: {col_count} of {TABLE_NUMBER_OF_ELEMENTS}")
    print('|' * 100)

TABLE_NUMBER_OF_ELEMENTS = 5
table = [[] for i in range(TABLE_NUMBER_OF_ELEMENTS)]
add_element('Bulgakov', 'Master and Margaret')
add_element('Orwell', '1984')
add_element('Dostoevsky', 'Crime and punishment')
add_element('Tolstoy', 'War and peace')
add_element('Dadzai', 'Confessions of an "inferior" person')
print_our_table()
del_element('Orwell')
print_our_table()