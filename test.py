import copy
from colorama import Fore, Style, init


class LevelGame:
    # تعريف المراحل
    #الرقم هو عبارة عن رقم المرحلة الذي اريد حلهت 
    #R: الحجر الاحمر  
    #P:الحجر البنفسجي
    #G:الحجارة الرمادية 
    #W: الاماكن البيضاء التي نريد الوصول اليها 
    #1:المكان المسموح التحرك به ووضع المغناطيس به 
    #0:المكان الممنوع وضع حجر به والتحرك به 
    #WR:ان الخانة التي نريد الوصول اليها تحتوي على مغناطيس احمر
    #WP:ان الخانة التي نريد الوصول الها تحتوي على مغناطيس بنفسجي 
    #WG:ان الخانة التي نريد الوصول اليها تحتوي على حجر رمادي
    levels = {
        1:[
            ["1","1","1","1"],
            ["1","W","G","W"],
            ["P","1","1","1"],
            ["0","0","0","0"],
        ],
        2:[
            ["1","1","W","1","1"],
            ["1","1","G","1","1"],
            ["W","G","W","G","W"],
            ["1","1","G","1","1"],
            ["P","1","W","1","1"],
        ],
        3:[
            ["0","0","0","0"],
            ["0","0","0","W"],
            ["1","1","G","1"],
            ["P","1","1","W"],
            
        ],
        4:[
            ["0","0","W","1","W"],
            ["0","0","0","G","1"],
            ["0","0","P","1","1"],
            ["0","0","0","G","1"],
            ["0","0","1","W","1"],
        ],
        5:[
            ["W","0","W","0"],
            ["WG","0","WG","0"],
            ["G","0","G","0"],
            ["W","P","1","0"],
            
        ],
        6:[
            ["1","1","1","W","1"],
            ["1","G","W","G","1"],
            ["P","1","1","W","1"],
            ["0","0","0","0","0"],
            ["0","0","0","0","0"],
        ],
        7:[
            ["W","1","1","1","0"],
            ["WG","1","1","1","0"],
            ["G","P","1","W","0"],
            ["1","G","WG","1","0"],
            ["0","0","0","W","0"],
        ],
        8:[
            ["W","1","W","1"],
            ["1","G","G","1"],
            ["P","1","W","1"],
            ["0","0","0","0"],
        ],
        9:[
            ["P","W","1","WG","1","G","W"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
        ],
        10:[
            ["P","1","1","1"],
            ["1","W","1","W"],
            ["1","1","G","G"],
            ["W","G","1","W"],
        ],
        11:[
            ["P","W","W","W",'G'],
            ["0","0","R","0",'0'],
            ["0","0","0","0",'0'],
            ["0","0","0","0",'0'],
            ["0","0","0","0",'0'],
        ],
        12:[
            ["G","1","0","0",'0'],
            ["WG","1","0","0",'0'],
            ["W","1","1","1",'0'],
            ["1","R","1","1",'0'],
            ["W","1","W","G",'0'],
        ],
        13:[
            ["G","1","1","W",'WG',"G"],
            ["0","W","1","1",'0',"0"],
            ["0","W","1","R",'0',"0"],
            ["0","0","0","0",'0',"0"],
            ["0","0","0","0",'0',"0"],
            ["0","0","0","0",'0',"0"],
            ],
        14:[
            ["1","1","1","G"],
            ["W","1","W","1"],
            ["G","W","W","1"],
            ["G","1","1","R"],
        ],
        15:[
            ["W","G","1","G",'1'],
            ["1","1","P","1",'W'],
            ["1","1","R","1",'W'],
            ["0","0","0","0",'0'],
            ["0","0","0","0",'0'],
        ],
        16:[
            ["1","1","1","W",'W'],
            ["1","1","G","1",'1'],
            ["R","1","1","1",'P'],
            ["1","1","G","1",'1'],
            ["W","1","1","W",'1'],
        ],


        
    }

    def show_level(self, array):
            for row in array:
                colored_row = []
                for item in row:
                    if item == 'R':
                        colored_row.append(Fore.RED + item)
                    elif item == 'P':
                        colored_row.append(Fore.MAGENTA + item)
                    elif item == 'G':
                        colored_row.append(Fore.LIGHTWHITE_EX + item)
                    elif item == 'W':
                        colored_row.append(Fore.WHITE + item)
                    elif item == '1':
                        colored_row.append(Fore.GREEN + item)
                    elif item == 'WP':
                        colored_row.append(Fore.WHITE + Fore.MAGENTA + item)  # أبيض وبنفسجي
                    elif item == 'WR':
                        colored_row.append(Fore.WHITE + Fore.RED + item)  # أبيض وأحمر
                    elif item == 'WG':
                        colored_row.append(Fore.WHITE + Fore.LIGHTBLACK_EX + item)  # أبيض ورمادي
                    elif item == "0":
                        colored_row.append(Fore.LIGHTYELLOW_EX+item)  # لا لون للمساحات الممنوعة (0) أو أي شيء آخر
            
                # تنسيق عرض الصف 
                print(" | ".join(colored_row))
                # print("-" * (len(row) * 4 - 1))  # خط يفصل بين الصفوف


class GameSolve:
    array=0
    number_of_moves=0
    level_number=0
    w=0

    def __init__(self):
        try:
            number = int(input("Enter the stage number you want to solve: "))
            self.level_number=number
            self.start_solve(number)
        except:
            print("Please enter a valid stage number.")
        
    def start_solve(self,level_number):
        game = LevelGame()
        self.array= copy.deepcopy(game.levels[level_number])
        game.show_level(self.array)
        self.select_magnetes()

    
    def select_magnetes(self):
        
        x=int(input("Enter row magnets :"))-1
        y=int(input("Enter col magnets :"))-1
        type=self.check_magnets(x,y)
        self.move_magntes(x,y,type)

    
    def move_magntes(self,x,y,type):
        new_row=int(input("Enter new Row :"))-1
        new_col=int(input("Enter new Col :"))-1
        new_type=self.check_move(new_row,new_col)
        self.move(x,y,new_row,new_col,type,new_type)


    def move(self,x,y,new_row,new_col,type,new_type):
        if(type=="P" and new_type == '1'):
            self.array[new_row][new_col]="P"
            self.array[x][y]="1"
        elif(type=="P" and new_type == 'W'):
            self.array[new_row][new_col]="WP"
            self.array[x][y]="1"
        elif(type=="WP" and new_type == '1'):
            self.array[new_row][new_col]="P"
            self.array[x][y]="W"
        elif(type=="WP" and new_type == 'W'):
            self.array[new_row][new_col]="WP"
            self.array[x][y]="W"
        elif(type=="R" and new_type == '1'):
            self.array[new_row][new_col]="R"
            self.array[x][y]="1"
        elif(type=="R" and new_type == 'W'):
            self.array[new_row][new_col]="WR"
            self.array[x][y]="1"
        elif(type=="WR" and new_type == '1'):
            self.array[new_row][new_col]="R"
            self.array[x][y]="W"
        elif(type=="WR" and new_type == 'W'):
            self.array[new_row][new_col]="WR"
            self.array[x][y]="W"
        #يقوم بطباعة المصفوفة مرة اخرى بعد نقل المغناطيس 
        self.check_gray(new_row,new_col,type) # يقوم باستدعاء تابع يفحص العناصر G ان وجدت 
        game=LevelGame()
        game.show_level(self.array)
        self.finish_solution(self.array)
    


    def check_move(self,x,y):
        if(self.array[x][y] == "1" or self.array[x][y]== "W"):
            return self.array[x][y]
        else:
            self.move_magntes()

    def check_magnets(self,x,y):
        if(self.array[x][y] == "P" or self.array[x][y] == "R" or self.array[x][y] == "WR" or self.array[x][y] == "WP"):
            self.number_of_moves+=1
            return self.array[x][y]
        else:
            print("You can only move P or R.")
            self.select_magnetes()
    
    
    def check_gray(self,x,y,type):
        len1=len(self.array)
        if type == "P" or type == "WP":
            self.move_gray_row_for_P(x,y,len1)
            self.move_gray_row_for_PR(x,y,len1)
            self.move_gray_col_for_P(x,y,len1)
            self.move_gray_col_for_PR(x,y,len1)
        # elif type == "R":
        #     self.move_gray_row(x,y,len1)
        #     self.move_gray_col(x,y,len1)
        return


    def move_gray_row_for_P(self,x,y,len1):
        should_exit=False
    # فحص الاحجار الرمادية بشكل نظامي افقي
        for i in range(y+1,len1):
            if(self.array[x][i]=="G"):
                for j in range(i+1,len1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W"):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="R"):
                        self.array[x][j]="RG"
                        self.array[x][i]="1" 
                        break        
                    elif(self.array[x][j]=="P"):
                        self.array[x][j]="PG"
                        self.array[x][i]="1"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="R"):
                for j in range(i+1,len1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="R"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WR"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GR"
                        self.array[x][i]="1"
                        break
                if(should_exit):
                        should_exit=False
                        break
                continue
            elif(self.array[x][i]=="GG"):
                for j in range(i+1,len1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        self.array[x][j]="G"
                        self.array[j-1][y]="G"
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="R"):
                        self.array[x][j]="RG"
                        self.array[x][i]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="RG"):
                for j in range(i+1,len1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        self.array[x][i]="R"
                        self.array[j-1][y]="G"
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="R"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="R"
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GR"
                        self.array[x][i]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="GR"):
                for j in range(i+1,len1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                            should_exit=True
                    if(self.array[x][j]=="0"):
                        self.array[x][i]="G"
                        self.array[j-1][y]="R"
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="R"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WR"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="R"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="WG"):
                for j in range(i+1,len1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                            should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="W"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="W"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="W"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="WGG"):
                for j in range(i+1,len1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                            should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="WG"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="WG"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="WG"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
        return
#========================================================
    def move_gray_row_for_PR(self,x,y,len1):
        # فحص الاحجار الرمادية بشكل عكسيي افقي 
        for i in range(y-1,-1,-1):
            if(self.array[x][i]=="G"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="R"):
                        self.array[x][j]="RG"
                        self.array[x][i]="1" 
                        break        
                    elif(self.array[x][j]=="P"):
                        self.array[x][j]="PG"
                        self.array[x][i]="1"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="R"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="R"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WR"
                        self.array[x][i]="1"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GR"
                        self.array[x][i]="1"
                        break
                if(should_exit):
                        should_exit=False
                        break
                continue
            elif(self.array[x][i]=="GG"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        self.array[x][j]="G"
                        self.array[x][j+1]="G"
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="R"):
                        self.array[x][j]="RG"
                        self.array[x][i]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="RG"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                    if(self.array[x][j]=="0"):
                        self.array[x][i]="R"
                        self.array[x][j+1]="G"
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="R"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="R"
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GR"
                        self.array[x][i]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="GR"):
                if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                        should_exit=True
                for j in range(i-1,-1,-1):
                    if(self.array[x][j]=="0"):
                        self.array[x][i]="G"
                        self.array[x][j+1]="R"
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="R"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WR"
                        self.array[x][i]="G"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="R"
                        break
                if(should_exit):
                    should_exit=False
                    break
            elif(self.array[x][i]=="WG"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                            should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="W"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="W"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="W"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[x][i]=="WGG"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j]=="0" or self.array[x][j]=="1" or self.array[x][j]=="W" ):
                            should_exit=True
                    if(self.array[x][j]=="0"):
                        break
                    elif(self.array[x][j]=="1"):
                        self.array[x][j]="G"
                        self.array[x][i]="WG"
                        break
                    elif(self.array[x][j]=="W"):
                        self.array[x][j]="WG"
                        self.array[x][i]="WG"
                        break
                    elif(self.array[x][j]=="G"):
                        self.array[x][j]="GG"
                        self.array[x][i]="WG"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
        return
    


    def move_gray_col_for_P(self,x,y,len1):
        should_exit=False
#فحص الاحجار الرمادية بشكل نظامي عامودي
        for i in range(x+1,len1):
            if(self.array[i][y]=="G"):
                for j in range(i+1,len1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="R"):
                        self.array[j][y]="RG"
                        self.array[i][y]="1" 
                        break        
                    elif(self.array[j][y]=="P"):
                        self.array[j][y]="PG"
                        self.array[i][y]="1"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="R"):
                for j in range(i+1,len1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="R"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WR"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GR"
                        self.array[i][y]="1"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="GG"):
                for j in range(i+1,len1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        self.array[j][y]="G"
                        self.array[j+1][y]="G"
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="R"):
                        self.array[j][y]="RG"
                        self.array[i][y]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="RG"):
                for j in range(i+1,len1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        self.array[i][y]="R"
                        self.array[j-1][y]="G"
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="R"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="R"
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GR"
                        self.array[i][y]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="GR"):
                if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                for j in range(i+1,len1):
                    if(self.array[j][y]=="0"):
                        self.array[i][y]="G"
                        self.array[j-1][y]="R"
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="R"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WR"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="R"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="WG"):
                for j in range(i+1,len1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="W"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="W"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="W"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="WGG"):
                if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="WG"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="WG"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="WG"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
        return
#=================================================================
    def move_gray_col_for_PR(self,x,y,len1):
        for i in range(x-1,-1,-1):
            if(self.array[i][y]=="G"):
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="WG"):
                        self.array[j][y]="WGG"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="R"):
                        self.array[j][y]="RG"
                        self.array[i][y]="1" 
                        break        
                    elif(self.array[j][y]=="P"):
                        self.array[j][y]="PG"
                        self.array[i][y]="1"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="R"):
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="R"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WR"
                        self.array[i][y]="1"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GR"
                        self.array[i][y]="1"
                        break        
                    elif(self.array[j][y]=="P"):
                        self.array[j][y]="PR"
                        self.array[i][y]="1"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="GG"):
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        self.array[j][y]="G"
                        self.array[j+1][y]="G"
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="R"):
                        self.array[j][y]="RG"
                        self.array[i][y]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="RG"):
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                    if(self.array[j][y]=="0"):
                        self.array[i][y]="R"
                        self.array[j+1][y]="G"
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="R"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="R"
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GR"
                        self.array[i][y]="G"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="GR"):
                if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0"):
                        self.array[i][y]="G"
                        self.array[j+1][y]="R"
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="R"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WR"
                        self.array[i][y]="G"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="R"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="WG"):
                if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="W"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="W"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="W"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
            elif(self.array[i][y]=="WGG"):
                if(self.array[j][y]=="0" or self.array[j][y]=="1" or self.array[j][y]=="W" ):
                        should_exit=True
                for j in range(i-1,-1,-1):
                    if(self.array[j][y]=="0"):
                        break
                    elif(self.array[j][y]=="1"):
                        self.array[j][y]="G"
                        self.array[i][y]="WG"
                        break
                    elif(self.array[j][y]=="W"):
                        self.array[j][y]="WG"
                        self.array[i][y]="WG"
                        break
                    elif(self.array[j][y]=="G"):
                        self.array[j][y]="GG"
                        self.array[i][y]="WG"
                        break
                if(should_exit):
                    should_exit=False
                    break
                continue
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
        elif(self.w !=0 and self.number_of_moves>=3):
            self.w=0
            self.number_of_moves=0
            print("If you could not solve the stage with the limited number of trials, the stage will be repeated.")
            print("--------------------------------------------------------------------------------------------------")
            self.start_solve(self.level_number)
        elif(self.w !=0 and self.number_of_moves<3):
            self.w=0
            self.select_magnetes()
        


game=GameSolve()
