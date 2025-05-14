print("Welcome to The Lexical Analyzer! ")
size = input("Enter your DFA : ")
liste = list(size)
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = [':','=']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
if liste[0] == numbers[0] or numbers[1] or numbers [2] or numbers[3] or numbers[4] or numbers[5] or numbers[6] or numbers[7] or numbers [8] or numbers [9]:
    initial_state = 1
    if liste[1] == numbers[0] or numbers[1] or numbers [2] or numbers[3] or numbers[4] or numbers[5] or numbers[6] or numbers[7] or numbers [8] or numbers [9]:
        print("Your DFA is Accepted")
    else:
        print("Your DFA is Rejected")

elif liste[0] == symbols[0] or symbols[1] :
    initial_state = 1
    if liste[1] == symbols[0] or symbols[1] :
        print("Your DFA is Accepted")
    else:
        print("Your DFA is Rejected")

elif liste[0] == letters[0] or letters[1] or letters[2] or letters[3] or letters[4] or letters[5] or letters[6] or letters[7] or letters[8] or letters[9] or letters[10] or letters[11] or letters[12] or letters[13] or letters[14] or letters[15] or letters[16] or letters[17] or letters[18] or letters[19] or letters[20] or letters[21] or letters[22] or letters [23] or letters [24] or letters[25]:
    initial_state = 1
    if liste[1] == numbers[0] or numbers[1] or numbers [2] or numbers[3] or numbers[4] or numbers[5] or numbers[6] or numbers[7] or numbers [8] or numbers [9]:
        print("Your DFA is Accepted")
    elif liste[1] == letters[0] or letters[1] or letters[2] or letters[3] or letters[4] or letters[5] or letters[6] or letters[7] or letters[8] or letters[9] or letters[10] or letters[11] or letters[12] or letters[13] or letters[14] or letters[15] or letters[16] or letters[17] or letters[18] or letters[19] or letters[20] or letters[21] or letters[22] or letters[23] or letters[24] or letters[25]:
        print("Your DFA is Accepted")
    else:
        print("Your DFA is Rejected")
else:
    print("Your DFA is Rejected")

