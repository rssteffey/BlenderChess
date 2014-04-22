BlenderChess
============

Will automatically setup and render a chess sequence in Blender

Just open the included .blend file and the setup should be usable.

Modify the chessInput.py text file to point at the right input file (default input.txt)
Click "Run Script", which will set up the board appropriately and animate all pieces
Click "Animation" in the far right panel to render the final video



Example of input file data below:

//--Begin example file--

//pauseFrames: (Number of frames to suspend animation between moves)
20

//moveSpeed:  (Number of frames that each piece move will take)
20



//BoardSetup [do not forget final '|' character per row]

R1|N1|B1|K1|Q1|B1|N1|R1|
P1|P1|P1|P1|P1|P1|P1|P1|
  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |
P2|P2|P2|P2|P2|P2|P2|P2|
R2|N2|B2|Q2|K2|B2|N2|R2|


//MoveList
b1->c3
g1->f3
f3->g1

//-- End Sample--
