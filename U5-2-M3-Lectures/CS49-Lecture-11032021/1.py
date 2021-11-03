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
    65
    for b in str_key:
        hash *= 0xcbf29ce484222325  # FNV Offset Basis
        hash ^= b
        hash &= 0xffffffffffffffff  # 64-bit hash

    return hash


"""
  hash_value = ((hash_value << 5) + hash_value) + b
  ---------------------------------------------------
  5381 = ((5381 << 5) + 5381) + 66
"""

"""
  hash_value &= 0xffffffff
  ----------------------------------------------------
  0000 0000 0000 [0101 0010 1010 1010 1010 1010 1010 1010] 0000 0000 0000 0000

  True and True == True
  True and False == False
  False and True == False
  False and False == False

  1 & 1 == 1
  1 & 0 == 0
  0 & 1 == 0
  0 & 0 == 0

  0011 0110 0111 0111 0101
& 0000 0000 0000 0000 1111
  0000 0000 0000 0000 0101
  0101 1011 1011 1011 1011 1111 1011 1111 0101 1011 1011 1011 1011 1111 1011 1111 0101 1011 1011 1011 1011 1111 1011 1111
  0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 1111 1111 1111 1111 1111 1111 1111 1111
  0xffffffff
"""

"""
  hash ^= b
  ---------
  1 xor 1 == 0
  1 xor 0 == 1
  0 xor 0 == 0
  0 xor 1 == 1

  0110 1011 1011 0111 1111
  0000 0000 1111 1011 1011
  0110 1011 0100 1100 0100

"""
