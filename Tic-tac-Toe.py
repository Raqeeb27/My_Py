position = ['0','1','2','3','4','5','6','7','8']
attempts = 0

def print_board():
    print(f"\n  {position[0]} | {position[1]} | {position[2]} \n ---|---|---")
    print(f"  {position[3]} | {position[4]} | {position[5]} \n ---|---|---")
    print(f"  {position[6]} | {position[7]} | {position[8]} \n")

def winCheck(player):
    winPosition = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in winPosition:
        if all(position[i] == player for i in win):
            print(f'{player} WON the match\n')
            return True
    return False

print_board()
while attempts < 9:
    player = 'X' if attempts % 2 == 0 else 'O'
    try:
        playerPosition = int(input(f"'{player}' chance\nEnter {player} position: "))
        if position[playerPosition] in ['O','X']:
            print(f"\nInvalid Position for '{player}'\n")
            continue
        else:
            position[playerPosition] = f"{player}"
            print_board()
            if winCheck(player):
                break
    except:
        print("\nInvalid Position \nSelect position from 0 - 8\n")
        continue    
    attempts += 1

if attempts >= 9:
    print("It's a DRAW !!!\n!!! GAME OVER !!!\n")