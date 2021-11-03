def djb2(key):
    """
    DJB2 hash, 32-bit
    """

    # Cast the key to a string and get bytes
    str_key = str(key).encode()

    # Start from an arbitrary large prime
    hash_value = 5381

    # Bit-shift and sum value for each character
    for b in str_key:
        hash_value = ((hash_value << 5) + hash_value) + b
        hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits

    return hash


def fnv1(key):
    """
    FNV-1 hash, 64-bit
    """

    # Cast the key to a string and get bytes
    str_key = str(key).encode()

    hash = 0x00000100000001B3  # FNV Prime

    for b in str_key:
        hash *= 0xcbf29ce484222325  # FNV Offset Basis
        hash ^= b
        hash &= 0xffffffffffffffff  # 64-bit hash

    return hash
