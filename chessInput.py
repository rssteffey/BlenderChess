import bpy #Imports the Blender Python API
import datetime


#  --LOCATION OF INPUT FILE GOES HERE--
# -(The list of initial setup and moves)-

#inputFile = 'saavedra.txt'


inputFile = 'test.txt'
#inputFile = 'input.txt'

#Duplicate Object Method
def duplicateObject(scene, name, copyobj, row, col):
 
	# Create new mesh
	mesh = bpy.data.meshes.new(name)

	# Create new object associated with the mesh
	ob_new = bpy.data.objects.new(name, mesh)

	# Copy data block from the old object into the new object
	ob_new.data = copyobj.data.copy()
	ob_new.scale = copyobj.scale
	ob_new.location = [row,col,0] #copyobj.location

	# Link new object to the given scene and select it
	scene.objects.link(ob_new)
 
	return ob_new

def deleteAllPieces():
	bpy.ops.object.select_pattern(pattern="AA*", case_sensitive=False, extend=False)
	bpy.ops.object.delete()

lineList = [];
currPiece = [];
moveList = [];

#BoardRanks
A=[];
B=[];
C=[];
D=[];
E=[];
F=[];
G=[];
H=[];
board = [A,B,C,D,E,F,G,H];


boardScene = bpy.data.scenes["Scene"];

deleteAllPieces()
#Delete animation frames
#bpy.context.active_object.animation_data_clear()
bpy.ops.anim.keyframe_clear_v3d()

#Remove comments and save into list
fh = open(bpy.path.abspath("//" + inputFile))
for line in fh.readlines():
	if line[0]!='/' and len(line)>1:
		withoutReturn = line.replace('\n', '')
		lineList.append(withoutReturn)


pauseFrames = lineList[0];
moveSpeed = lineList[1];

#----Setup Initial Board---

for i in range(2, 10):
	colCount=0
	for j in range (0, len(lineList[i])):
		if lineList[i][j]=='|':
			for ident in currPiece:
				if ident == '1':
					color='white'
				if ident == '2':
					color='black'
				if ident == 'k' or ident == 'K':
					type='king'
				if ident == 'q' or ident == 'Q':
					type='queen'
				if ident == 'r' or ident == 'R':
					type='rook'
				if ident == 'b' or ident == 'B':
					type='bishop'
				if ident == 'n' or ident == 'N':
					type='knight'
				if ident == 'p' or ident == 'P':
					type='pawn'
				if ident == ' ':
					type='none'
			#Make piece from properties
			if type != 'none':
				name=type+ident
				objCopy = bpy.data.objects[name]
				newName = 'AA' + name + '_' + str(i-1) + '_'+ str(colCount+1)
				colAmount= (colCount-3.5)*2
				rowAmount= (i-5.5)*-2
				duplicateObject(boardScene, newName, objCopy, colAmount, rowAmount)
				board[colCount].insert(0,newName)
				
			else:
				name=' '
				board[i-2].append(name)
			print(name),
			currPiece=[]
			colCount=colCount+1
		else:
			currPiece.append(lineList[i][j])
	
for x in range (10,len(lineList)):
		moveList.append(lineList[x])	



bpy.ops.object.select_pattern(pattern="AA*")
bpy.ops.group.create(name="BoardPieces")

bpy.ops.object.select_all(action='TOGGLE')

#---Animate Move List---

#make animation length appropriate
frameNum = (len(moveList)*(int(pauseFrames)+int(moveSpeed))) + (int(pauseFrames)*2)
bpy.data.scenes["Scene"].frame_end = frameNum

markerLocation=0


for currLine in moveList:
	#provided we aren't promoting a piece
	if currLine[0] != '!':
		fromRow = (ord(currLine[0])-97) #get ASCII value and convert to file
		fromCol = int(currLine[1])-1           #gets rank
		toRow = (ord(currLine[4])-97)   #ASCII converted file of destination
		toCol = int(currLine[5])-1				#Rank of destination
		#increment frame counter for pause
		markerLocation = markerLocation + int(pauseFrames)
		print(fromRow)
		print(fromCol)
		print(board[int(fromRow)][int(fromCol)])
		#Update Board Array List
		retrievedName = board[int(fromRow)][int(fromCol)]
		board[int(toRow)][int(toCol)] = retrievedName
		board[int(fromRow)][int(fromCol)] = ' '
		#keyframe before motion
		if retrievedName != ' ':
			movingPiece = bpy.data.objects[retrievedName]
			bpy.ops.object.select_pattern(pattern=retrievedName)
			print(movingPiece)
			boardScene.frame_set(frame = markerLocation)
			
			bpy.ops.anim.keyframe_insert()
			#move to frame after motion
			markerLocation = markerLocation + int(moveSpeed)
			boardScene.frame_set(frame = markerLocation)
			#change location and insert keyframe
			movingPiece.location = [(toRow-3.5)*2,((8-toCol)-4.5)*-2,0] 
			bpy.ops.anim.keyframe_insert()
			
	#Test print the whole board
	print("Board on move: something")
	for letter in board:
		thisLine=""
		for piece in letter:
			thisLine = thisLine + str(piece + "|")	
		print(thisLine + "\n"),

#---Print for testing---
for currLine in moveList:
	print(currLine),


#---Render to File--
t = datetime.datetime.now()
fileName = (t-datetime.datetime(1970,1,1)).total_seconds()


#bpy.context.scene.render.filepath = str(bpy.path.abspath('//') + str(fileName) + '.png')

#bpy.ops.render.render(write_still=True)