import copy
from level_game import LevelGame
from magnet import MagnetManager
from gray_movement import GrayMovement
class GameSolve:

    def __init__(self):

        self.array = []

        self.number_of_moves = 0

        self.level_number = 0

        self.w = 0

        self.magnet_manager = MagnetManager()

        # self.gray_movement = GrayMovement(self.array)


    def start_solve(self, level_number):

        self.level_number=level_number

        game = LevelGame()

        self.array = copy.deepcopy(game.levels[level_number])

        game.show_level(self.array)

        self.select_magnets()


    def select_magnets(self):

        x = int(input("Enter row magnets: ")) - 1

        y = int(input("Enter col magnets: ")) - 1

        type = self.magnet_manager.check_magnets(self.array, x, y, self)

        self.move_magnets(x, y, type)


    def move_magnets(self, x, y, type):

        new_row = int(input("Enter new Row: ")) - 1

        new_col = int(input("Enter new Col: ")) - 1

        new_type = self.magnet_manager.check_move(self.array, new_row, new_col, type)
        if(new_type):
            new_type=self.magnet_manager.move(self.array, x, y, new_row, new_col, type, new_type)
            self.check_gray(new_row,new_col,new_type)
            game = LevelGame()
            game.show_level(self.array)
            self.finish_solution(self.array)
        else:
            print("You can't do this move because the place is not moveable. ")
            self.move_magnets(x,y,type)
    

    def check_gray(self,x,y,type):
        len1=len(self.array)
        gray_movement=GrayMovement(self.array)
        if type == "P" or type == "WP":
            gray_movement.move_gray_row_for_P(x,y,len1)
            gray_movement.move_gray_row_for_PR(x,y,len1)
            gray_movement.move_gray_col_for_P(x,y,len1)
            gray_movement.move_gray_col_for_PR(x,y,len1)
        elif type == "R" or type == "WR":
            gray_movement.move_gray_row_for_R(x,y,len1)
            gray_movement.move_gray_row_for_RR(x,y,len1)
            gray_movement.move_gray_col_for_R(x,y,len1)
            gray_movement.move_gray_col_for_RR(x,y,len1)
        return

    
    def finish_solution(self,array):
        len1=len(array)
        for row in array:
            for element in row:
                if element == "W":
                    self.w+=1
                    break
        if(self.w == 0):
            print("Congratulations, the stage has been solved.")
        elif(self.w !=0 and self.number_of_moves>=4):
            self.w=0
            self.number_of_moves=0
            print("If you could not solve the stage with the limited number of trials, the stage will be repeated.")
            print("--------------------------------------------------------------------------------------------------")
            self.start_solve(self.level_number)
        elif(self.w !=0 and self.number_of_moves<4):
            self.w=0
            self.select_magnets()
