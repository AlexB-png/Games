#This likely will not be finished

lineA= [ " " , " " , " " ]
lineB= [ " " , " " , " " ]
lineC= [ " " , " " , " " ]
print(lineA)
print(lineB)
print(lineC)


player1 = input("Input the slot code for the grid. 1-9 left to right")
def Write():
    match player1:
        case 1:
            if lineA[0] !="O" and lineA !="X":
                lineA.append("X")

        
print(lineA)
print(lineB)
print(lineC)