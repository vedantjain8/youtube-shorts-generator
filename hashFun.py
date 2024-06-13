import hashlib


def check_hash(string):
    # Generate hash for string1
    hash1 = hashlib.sha256(string.encode()).hexdigest()+"\n"

    # Compare the hashes
    with open("hashes.txt", 'r') as hash2:
        hashes = hash2.readlines()
        if hash1 in hashes:
            print("hashcheck")
            return True
        else:
            print("false hashcheck")
            return False


def write_hash(string):
    hash = hashlib.sha256(string.encode()).hexdigest()

    # Compare the hashes
    with open("hashes.txt", 'a') as file:
        file.write(hash + "\n")
