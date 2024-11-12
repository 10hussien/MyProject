class MagnetManager:
    def check_magnets(self, array, x, y, game_solve):
        if array[x][y] in ["P", "R", "WR", "WP"]:
            game_solve.number_of_moves += 1
            return array[x][y]
        else:
            print("You can only move P or R.")
            game_solve.select_magnets()

    def check_move(self, array, x, y, type):
        if array[x][y] in ["1", "W"]:
            return array[x][y]
        else:
            return False

    def move(self, array, x, y, new_row, new_col, type, new_type):
        if(type=="P" and new_type == '1'):
            array[new_row][new_col]="P"
            array[x][y]="1"
        elif(type=="P" and new_type == 'W'):
            array[new_row][new_col]="WP"
            array[x][y]="1"
        elif(type=="WP" and new_type == '1'):
            array[new_row][new_col]="P"
            array[x][y]="W"
        elif(type=="WP" and new_type == 'W'):
            array[new_row][new_col]="WP"
            array[x][y]="W"
        elif(type=="R" and new_type == '1'):
            array[new_row][new_col]="R"
            array[x][y]="1"
        elif(type=="R" and new_type == 'W'):
            array[new_row][new_col]="WR"
            array[x][y]="1"
        elif(type=="WR" and new_type == '1'):
            array[new_row][new_col]="R"
            array[x][y]="W"
        elif(type=="WR" and new_type == 'W'):
            array[new_row][new_col]="WR"
            array[x][y]="W"
        return array[new_row][new_col]
    