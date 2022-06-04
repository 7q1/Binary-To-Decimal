# Github > 7q1

import os
from colorama import *


print(Fore.CYAN+"\n[+] -0 To Exit"+Fore.RESET)
while 1:
    some = 0

    binary = input(f"[{Fore.YELLOW}?{Fore.RESET}] Enter Binary > ")

    # Exit when input == -0
    if binary == '-0':
        os.system('cls||clear')
        exit(1)
    # Making reversed list to calculate binary input
    binaryReversed = []
    for x in range(len(binary), 0, -1):
        binaryReversed.append(binary[x-1])

    # Generate decimal values based on length of binary input
    bitsList = [1, 2]
    for bits in range(2, len(binaryReversed)):
        bitsList.append(2**bits)

    # Counting 1's. And for each '1' there's its decimal value
    count = 0
    for i, j in zip(bitsList, binaryReversed):
        if j == "1":
            count += i

        # If binary contain other than 0,1. Then return the whole decimal value to '0'
        # (some) is variable to break the code and starting it from the beggining.
        # If there's other than 1,0. (some) will be 1.
        elif j != '1' and j != '0':
            print(f"[{Fore.MAGENTA}-{Fore.RESET}] Decimal Value: None\n")
            some += 1
            break

    # If (some) is 1. it will restart the while loop with Decimal value of zero [Line 35]. 
    if some == 1:
        pass
    # If 
    else:
        if "-" in binaryReversed:
            print(f"[{Fore.MAGENTA}-{Fore.RESET}] Decimal Value: -{count:,}\n")
        elif not "-" in binaryReversed:
            print(f"[{Fore.MAGENTA}-{Fore.RESET}] Decimal Value: {count:,}\n")