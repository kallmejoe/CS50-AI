import sys;

class Node():
    def __init__(self, state, parent , action ):
        self.parent = parent
        self.state = state
        self.action = action

class StackFrontier():


    def __init__(self):
        self.frontier = [];

    def add(self,node):
        self.frontier.append(node);
    
    def empty(self):
        length = len(self.frontier)
        if(length==0):
            return True;
        else:
            return False;
    def contains_state(self,state):
        return any(node.state == state for node in self.frontier)


    def remove(self):
        if self.empty():
            raise Exception("error: your frontier is empty fromt the inside")
        else:
            # getting the last elem in the array
            mayBeGoal = self.frontier[-1]
            # removing this this means get elements from start to -1 (excluding it)
            self.frontier = self.frontier[:-1]
            return mayBeGoal # it is a node at the end
        
def hasStartEnd(MazeContent):

    # if the maze does not have a start or end
    if MazeContent.count('A') != 1:
        raise Exception("The maze must have exactly one start point")
    if MazeContent.count('B') != 1:
        raise Exception("The maze must have exactly one goal")

    return True;



class Maze : 

    def __init__(self,filename):

        # reading file
        # when reading the file the MazeContent will be ='#####B#\n##### #\n####  #\n#### ##\n     ##\nA######\n'
        with open(filename) as f:
            MazeContent = f.read();
        
        # every maze should has a start and a goal (end)
        hasStartEnd(MazeContent);
        

        # spilting the maze into lines by removing the \n(dh zy el \n el f c)
        MazeContent = MazeContent.splitlines();
        # now the maze content look like this (array of strings)

                # [
                #     '#####B#',
                #     '##### #',
                #     '####  #',
                #     '#### ##',
                #     '     ##',
                #     'A######'
                # ]
        
        #height will be the number of lines 

        self.height = len(MazeContent);
        #width the the line that contains the highest number of chars
        self.width = max(len(line) for line in MazeContent)

        # store the walls
        self.walls = []
        # loop over each cell in the 2d array 
        # if it is not " " or " A " or " b " so it is " # "(wall)
        for i in range(self.height):
            row = [];
            for j in range (self.width):
                try:
                    # we don't have switch case here :(
                    # we don't have restriction over " ",'' it is the same here
                    # false --> not a wall , true --> a wall
                    # we are analyzing the game and turning it into numerical the computer can understand
                    if(MazeContent[i][j] == 'A'):
                        self.start = (i,j);
                        row.append(False);
                    elif(MazeContent[i][j]== 'B'):
                        self.goal = (i,j);
                        row.append(False);
                    elif(MazeContent[i][j]==' '):
                        row.append(False);
                    else:
                        row.append(True)
                # in case an get out of bounds
                except IndexError:
                    row.append(False)
            self.walls.append(row);
        
        #intializion the object with none (no pointing)
        self.solution = None

        def displayMaze(self):
            # if self.solution is not none the code tries to access self.solution[1] else it sets to none
            solution =self.solution[1] if self.solution is not None else None
            # enumerate will parse the values into two the vars i: index of row : row : the value of the row (string)
            for i , row in enumerate(self.walls):
                for j , col in enumerate(row):
                    if col: #true --> wall
                         print("█", end="")
                         # by default the print function in python has end=\n which add new line so making it equal to "" will not make newline
                         # it can take " " for spaces or \t
                    elif (i, j) == self.start:
                        print("A", end="")
                    elif (i, j) == self.goal:
                        print("B", end="")
                    elif solution is not None and (i, j) in solution:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print() # print an empty line
            print() # print an empty line

    def neigbors(self,state):
        # state is represented by row and col as the structure is 2d array
        row,col = state;
        possibleActions = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        
        result = []
        # adding the valid moves
        for action, (r, c) in possibleActions:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result
    
    def displayMaze(self):
            # if self.solution is not none the code tries to access self.solution[1] else it sets to none
            solution =self.solution[1] if self.solution is not None else None
            # enumerate will parse the values into two the vars i: index of row : row : the value of the row (string)
            for i , row in enumerate(self.walls):
                for j , col in enumerate(row):
                    if col: #true --> wall
                         print("█", end="")
                         # by default the print function in python has end=\n which add new line so making it equal to "" will not make newline
                         # it can take " " for spaces or \t
                    elif (i, j) == self.start:
                        print("A", end="")
                    elif (i, j) == self.goal:
                        print("B", end="")
                    elif solution is not None and (i, j) in solution:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print() # print an empty line
            print() # print an empty line
    
    def solve (self):
        
        
        #intialize the intial position
        start = Node(state=self.start , parent=None,action=None)
        #type of frontier
        frontier = StackFrontier();
        frontier.add(start);
        
        # intialize an empty explored set
        self.explored = set();
        self.num_explored =0;

        while True:
    
            if frontier.empty():
                raise Exception("no solution")
            
            # remove a node from the frontier and assign to node to check it
            node = frontier.remove();
            # we explored a node now so

            self.num_explored +=1;

            # if node is the goal , then we have a solution
            if node.state == self.goal :
                actions = [];
                cells = [];
            # we are backtracking now till we reach the start
            # start is when the parent is none like when we specified the intial at first
                while node.parent is not None:
                    actions.append(node.action);
                    cells.append(node.state);
                    # to keep the backtracking
                    node = node.parent;
                # we are getting from the end (when we found the solution) till the start 
                # we reverse for ascending order
                actions.reverse();
                cells.reverse();
                self.solution = (actions,cells);
                return;
            
            self.explored.add(node.state);
            for action,state in self.neigbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state,parent=node,action=action)
                    frontier.add(child); 
            
    def output_image(self,filename , show_solution, show_explored):
        from PIL import Image, ImageDraw # a libary called pillow (pip install pillow)
        cell_size=50 # each square in maze in is 50px
        cell_border=2;

        img = Image.new(
            "RGBA",(self.width*cell_size,self.height*cell_size),"black"
        );

        draw = ImageDraw.Draw(img);

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)
                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename);

# no file provided
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")
# will take the file name from the comand in termainl
m = Maze(sys.argv[1])
print("Maze:")
m.displayMaze()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.displayMaze()
m.output_image("maze.png", show_explored=True)