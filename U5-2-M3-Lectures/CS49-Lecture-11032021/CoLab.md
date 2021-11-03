# Unit 5.2 M3 Hash Tables II with Tom Tarpey 11/03/2021

Today's notes are so closely related to the notes from 09/08/2021
Therefore, additionally... please go to /CS47-Lecture-09082021/CoLab.md for markdown notes
and /CS47-Lecture-09082021/... for code notes

## BitWise Exlusive Or XOR " ^ " 
The bitwise exclusive OR operator (^) compares each bit of its first operand to the corresponding bit of its second operand. If the bit in one of the operands is 0 and the bit in the other operand is 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.

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