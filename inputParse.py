"""
----Chess animator----
This will setup and render a scene on a Chessboard, given certain text parameters
Script to parse text input file
"""

lineList = [];

#BoardRows
A=[];
B=[];
C=[];
D=[];
E=[];
F=[];
G=[];
H=[];
board = [A,B,C,D,E,F,G,H];

#Remove comments and save into list
fh = open('input.txt')
for line in fh.readlines():
	if line[0]!='/':
		lineList.append(line)


pauseFrames = lineList[0];
moveSpeed = lineList[1];

for i in range(2, 9):
	for j in range (0, len(lineList[i])):
		if lineList[i][j]=='|':
			makeObject(currPiece, i, counter)
			currPiece=
			counter++
		else
			currPiece.append(lineList[i][j])
		


#Print for testing
for currLine in lineList:
	print currLine,
wait = input("")



#Create object of the given type at the proper location
def makeObject(type, r, c):
	return type
