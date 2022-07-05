def hangman(word):
    wrong = 0
    stages = ["",\
              "|________           ",\
              "|          |        ",\
              "|          |        ",\
              "|          O        ",\
              "|         /|\       ",\
              "|         / \       ",\
              "|                   "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print ("Welcome to game!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Insert the letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "S"
        else:
            wrong += 1
        print ((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You won! Word is: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print(" You lost! Word is: {}.".format(word))

hangman("cat")