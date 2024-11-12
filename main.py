from game_solve import GameSolve

if __name__ == "__main__":
    game = GameSolve()
    try:
        number = int(input("Enter the stage number you want to solve: "))
        game.start_solve(number)
    except ValueError:
        print("Please enter a valid stage number.")