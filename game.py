## First draft of prisoner's dilemma game

# c is cooperate
# d is defect

class Player:
    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type
        self.coins = 0
        self.moves = []


def game(num):

    player1 = initializePlayer()
    player2 = Player("Bob", "Cooperative")
    
    for i in range(10):
        print("Turn " + str(i + 1))
        print("")
        print("You have " + str(player1.coins) + " coins")
        print(player2.name + " has " + str(player2.coins) + " coins")

        print("Do you choose to defect (d) or cooperate (c)")
        player1Decision = input()
        player2Decision = makeMove(player2, player1)

        outcome(player1, player2, player1Decision, player2Decision)


def initializePlayer() -> Player:
    print("What is your name?")
    name = input()
    return Player(name, "player")

def outcome(player1: Player, player2: Player, decision1, decision2):
    outcome = None

    if decision1 == decision2:
        if decision1 == 'd':
            outcome = (1,1)
        else:
            outcome = (3,3)
    
    elif decision1 == 'c':
        outcome = (0,5)
    
    else:
        outcome = (5,0)

    player1.coins += outcome[0]
    player2.coins += outcome[1]

def makeMove(player: Player, opponent: Player) -> str:
    return 'c'

if __name__ == "__main__":
    game(10)