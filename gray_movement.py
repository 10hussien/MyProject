class GrayMovement:
    def __init__(self, array):
        self.array = array

    def move_gray_row_for_P(self,x,y,len1):
        cc=0
        for i in range(y+1,len1):
            if(self.array[x][i] == "1" or self.array[x][i] == "W" ):
                for j in range(i,y,-1):
                    if(self.array[x][j] == "1"):
                        if(self.array[x][j-1]=="G"):
                            self.array[x][j]="G"
                            self.array[x][j-1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j-1]=="WG"):
                            self.array[x][j]="G"
                            self.array[x][j-1]="W"
                            cc+=1
                            continue
                        elif(self.array[x][j-1]=="R"):
                            self.array[x][j]="R"
                            self.array[x][j-1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j-1]=="WR"):
                            self.array[x][j]="R"
                            self.array[x][j-1]="W"
                            cc+=1
                            continue
                        else:
                            break

                    elif(self.array[x][j] == "W"):
                        if(self.array[x][j-1]=="G"):
                            self.array[x][j]="WG"
                            self.array[x][j-1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j-1]=="WG"):
                            self.array[x][j]="WG"
                            self.array[x][j-1]="W"
                            cc+=1
                            continue
                        elif(self.array[x][j-1]=="R"):
                            self.array[x][j]="WR"
                            self.array[x][j-1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j-1]=="WR"):
                            self.array[x][j]="WR"
                            self.array[x][j-1]="W"
                            cc+=1
                            continue
                        else:
                            
                            break
                if(cc>0):
                    cc=0
                    break
                else:
                    continue
#========================================================
    def move_gray_row_for_PR(self,x,y,len1):
        cc=0
        for i in range(y-1,-1,-1):
            if(self.array[x][i] == "1" or self.array[x][i] == "W" ):
                for j in range(i,y,+1):
                    if(self.array[x][j] == "1"):
                        if(self.array[x][j+1]=="G"):
                            self.array[x][j]="G"
                            self.array[x][j+1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j+1]=="WG"):
                            self.array[x][j]="G"
                            self.array[x][j+1]="W"
                            cc+=1
                            continue
                        elif(self.array[x][j+1]=="R"):
                            self.array[x][j]="R"
                            self.array[x][j+1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j+1]=="WR"):
                            self.array[x][j]="R"
                            self.array[x][j+1]="W"
                            cc+=1
                            continue

                    elif(self.array[x][j] == "W"):
                        if(self.array[x][j+1]=="G"):
                            self.array[x][j]="WG"
                            self.array[x][j+1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j+1]=="WG"):
                            self.array[x][j]="WG"
                            self.array[x][j+1]="W"
                            cc+=1
                            continue
                        elif(self.array[x][j+1]=="R"):
                            self.array[x][j]="WR"
                            self.array[x][j+1]="1"
                            cc+=1
                            continue
                        elif(self.array[x][j+1]=="WR"):
                            self.array[x][j]="WR"
                            self.array[x][j+1]="W"
                            cc+=1
                            continue
                if(cc>0):
                    cc=0
                    break
                else:
                    continue


    def move_gray_col_for_P(self,x,y,len1):
        cc=0
        for i in range(x+1,len1):
            if(self.array[i][y] == "1" or self.array[i][y] == "W" ):
                for j in range(i,x,-1):
                    if(self.array[j][y] == "1"):
                        if(self.array[j-1][y]=="G"):
                            self.array[j][y]="G"
                            self.array[j-1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j-1][y]=="WG"):
                            self.array[j][y]="G"
                            self.array[j-1][y]="W"
                            cc+=1
                            continue
                        elif(self.array[j-1][y]=="R"):
                            self.array[j][y]="R"
                            self.array[j-1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j-1][y]=="WR"):
                            self.array[j][y]="R"
                            self.array[j-1][y]="W"
                            cc+=1
                            continue

                    elif(self.array[j][y] == "W"):
                        if(self.array[j-1][y]=="G"):
                            self.array[j][y]="WG"
                            self.array[j-1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j-1][y]=="WG"):
                            self.array[j][y]="WG"
                            self.array[j-1][y]="W"
                            cc+=1
                            continue
                        elif(self.array[j-1][y]=="R"):
                            self.array[j][y]="WR"
                            self.array[j-1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j-1][y]=="WR"):
                            self.array[j][y]="WR"
                            self.array[j-1][y]="W"
                            cc+=1
                            continue
                if(cc>0):
                    cc=0
                    break
                else:
                    continue
#=================================================================
    def move_gray_col_for_PR(self,x,y,len1):
        cc=0
        for i in range(x-1,-1,-1):
            if(self.array[i][y] == "1" or self.array[i][y] == "W" ):
                for j in range(i,x,+1):
                    if(self.array[j][y] == "1"):
                        if(self.array[j+1][y]=="G"):
                            self.array[j][y]="G"
                            self.array[j+1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j+1][y]=="WG"):
                            self.array[j][y]="G"
                            self.array[j+1][y]="W"
                            cc+=1
                            continue
                        elif(self.array[j+1][y]=="R"):
                            self.array[j][y]="R"
                            self.array[j+1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j+1][y]=="WR"):
                            self.array[j][y]="R"
                            self.array[j+1][y]="W"
                            cc+=1
                            continue

                    elif(self.array[j][y] == "W"):
                        if(self.array[j+1][y]=="G"):
                            self.array[j][y]="WG"
                            self.array[j+1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j+1][y]=="WG"):
                            self.array[j][y]="WG"
                            self.array[j+1][y]="W"
                            cc+=1
                            continue
                        elif(self.array[j+1][y]=="R"):
                            self.array[j][y]="WR"
                            self.array[j+1][y]="1"
                            cc+=1
                            continue
                        elif(self.array[j+1][y]=="WR"):
                            self.array[j][y]="WR"
                            self.array[j+1][y]="W"
                            cc+=1
                            continue
                if(cc>0):
                    cc=0
                    break
                else:
                    continue

    def move_gray_row_for_R(self,x,y,len1):
        cc=0
        for i in range(x+1,len1):
            if (self.array[i][y] == "1"):
                for j in range(i+1,len1):
                    if(self.array[j][y] in ("1","W","0")):
                        break
                    elif(self.array[j][y] in ("G","WG","P","WP")):
                        if(self.array[j][y] == "G"):
                            self.array[j-1][y]="G"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WG"):
                            self.array[j-1][y]="G"
                            self.array[j][y]="W"
                            break
                        elif(self.array[j][y] == "P"):
                            self.array[j-1][y]="P"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WP"):
                            self.array[j-1][y]="P"
                            self.array[j][y]="W"
                            break
                continue

            elif(self.array[i][y] == "W"):
                for j in range(i+1,len1):
                    if(self.array[j][y] in ("1","W","0")):
                        break
                    elif(self.array[j][y] in ("G","WG","P","WP")):
                        if(self.array[j][y] == "G"):
                            self.array[j-1][y]="WG"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WG"):
                            self.array[j-1][y]="WG"
                            self.array[j][y]="W"
                            break
                        elif(self.array[j][y] == "P"):
                            self.array[j-1][y]="WP"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WP"):
                            self.array[j-1][y]="WP"
                            self.array[j][y]="W"
                            break
                continue

    def move_gray_row_for_RR(self,x,y,len1):
        cc=0
        for i in range(x-1,-1,-1):
            if (self.array[i][y] == "1"):
                for j in range(i-1,-1,-1):
                    if(self.array[j][y] in ("1","W","0")):
                        break
                    elif(self.array[j][y] in ("G","WG","P","WP")):
                        if(self.array[j][y] == "G"):
                            self.array[j+1][y]="G"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WG"):
                            self.array[j+1][y]="G"
                            self.array[j][y]="W"
                            break
                        elif(self.array[j][y] == "P"):
                            self.array[j+1][y]="P"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WP"):
                            self.array[j+1][y]="P"
                            self.array[j][y]="W"
                            break
                continue

            elif(self.array[i][y] == "W"):
                for j in range(i-1,-1,-1):
                    if(self.array[j][y] in ("1","W","0")):
                        break
                    elif(self.array[j][y] in ("G","WG","P","WP")):
                        if(self.array[j][y] == "G"):
                            self.array[j+1][y]="WG"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WG"):
                            self.array[j+1][y]="WG"
                            self.array[j][y]="W"
                            break
                        elif(self.array[j][y] == "P"):
                            self.array[j+1][y]="WP"
                            self.array[j][y]="1"
                            break
                        elif(self.array[j][y] == "WP"):
                            self.array[j+1][y]="WP"
                            self.array[j][y]="W"
                            break
                continue
    
    def move_gray_col_for_R(self,x,y,len1):
        cc=0
        for i in range(y+1,len1):
            if (self.array[x][i] == "1"):
                for j in range(i+1,len1):
                    if(self.array[x][j] in ("1","W","0")):
                        break
                    elif(self.array[x][j] in ("G","WG","P","WP")):
                        if(self.array[x][j] == "G"):
                            self.array[x][j-1]="G"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WG"):
                            self.array[x][j-1]="G"
                            self.array[x][j]="W"
                            break
                        elif(self.array[x][j] == "P"):
                            self.array[x][j-1]="P"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WP"):
                            self.array[x][j-1]="P"
                            self.array[x][j]="W"
                            break
                continue

            elif(self.array[x][i] == "W"):
                for j in range(i+1,len1):
                    if(self.array[x][j] in ("1","W","0")):
                        break
                    elif(self.array[x][j] in ("G","WG","P","WP")):
                        if(self.array[x][j] == "G"):
                            self.array[x][j-1]="WG"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WG"):
                            self.array[x][j-1]="WG"
                            self.array[x][j]="W"
                            break
                        elif(self.array[x][j] == "P"):
                            self.array[x][j-1]="WP"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WP"):
                            self.array[x][j-1]="WP"
                            self.array[x][j]="W"
                            break
                continue
    
    def move_gray_col_for_RR(self,x,y,len1):
        cc=0
        for i in range(y-1,-1,-1):
            if (self.array[x][i] == "1"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j] in ("1","W","0")):
                        break
                    elif(self.array[x][j] in ("G","WG","P","WP")):
                        if(self.array[x][j] == "G"):
                            self.array[x][j+1]="G"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WG"):
                            self.array[x][j+1]="G"
                            self.array[x][j]="W"
                            break
                        elif(self.array[x][j] == "P"):
                            self.array[x][j+1]="P"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WP"):
                            self.array[x][j+1]="P"
                            self.array[x][j]="W"
                            break
                continue

            elif(self.array[x][i] == "W"):
                for j in range(i-1,-1,-1):
                    if(self.array[x][j] in ("1","W","0")):
                        break
                    elif(self.array[x][j] in ("G","WG","P","WP")):
                        if(self.array[x][j] == "G"):
                            self.array[x][j+1]="WG"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WG"):
                            self.array[x][j+1]="WG"
                            self.array[x][j]="W"
                            break
                        elif(self.array[x][j] == "P"):
                            self.array[x][j+1]="WP"
                            self.array[x][j]="1"
                            break
                        elif(self.array[x][j] == "WP"):
                            self.array[x][j+1]="WP"
                            self.array[x][j]="W"
                            break
                continue
