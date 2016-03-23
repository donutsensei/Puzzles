from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    # __repr__ is up to you
    def __eq__(self, other):

        return (type(other) == type(self))

    def __str__(self):

        pegs = 0
        empty = 0
        unused = 0
        for i in self._marker:
            for j in i:
                if j == '*':
                    pegs += 1
                if j == '.':
                    empty += 1
                if j == '#':
                    unused += 1

        return ("There are " + str(pegs) + " pegs, " + str(empty) + " empty spaces, and " + unused + " unused spaces on the grid")

    # TODO
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration

    def extensions(self):

        ext = []

        for i in range(0,len(self._marker)):
            for j in range(0, len(self._marker[i])):
                if self._marker[i][j] == ".":

                    if (i-2 >= 0) :
                        if self._marker[i-2][j] == "*" and self._marker[i-1][j] == "*":

                            newlist =[]
                            for item in self._marker:
                                newlist.append(item)

                            #JUMPING THE TOP

                            newlist[i][j] = "*"
                            newlist[i-1][j] = "."
                            newlist[i-2][j]= "."

                            ext.append(GridPegSolitairePuzzle(newlist, self._marker_set))

                            newlist[i][j] = "."
                            newlist[i-1][j] = "*"
                            newlist[i-2][j] = "*"


                    if i+2 <= (len(self._marker)-1):
                        if self._marker[i+2][j] == "*" and self._marker[i+1][j] == "*":

                            newlist =[]
                            for item in self._marker:
                                newlist.append(item)

                            #JUMPING THE BOTTOM

                            newlist[i][j] = "*"
                            newlist[i+1][j] = "."
                            newlist[i+2][j]= "."

                            ext.append(GridPegSolitairePuzzle(newlist, self._marker_set))


                            newlist[i][j] = "."
                            newlist[i+1][j] = "*"
                            newlist[i+2][j] = "*"


                    if j-2 >= 0:
                        if self._marker[i][j-2] == "*" and self._marker[i][j-1] == "*":

                            newlist =[]
                            for item in self._marker:
                                newlist.append(item)

                            #JUMPING THE LEFT

                            newlist[i][j] = "*"
                            newlist[i][j-1] = "."
                            newlist[i][j-2]= "."

                            ext.append(GridPegSolitairePuzzle(newlist, self._marker_set))

                            newlist[i][j] = "."
                            newlist[i][j-1] = "*"
                            newlist[i][j-2]= "*"


                    if j+2 <= (len(self._marker[i])-1):
                        if self._marker[i][j+2] == "*" and self._marker[i][j+1] == "*":

                            newlist =[]
                            for item in self._marker:
                                newlist.append(item)

                            #JUMPING THE RIGHT

                            newlist[i][j] = "*"
                            newlist[i][j+1] = "."
                            newlist[i][j+2]= "."

                            ext.append(GridPegSolitairePuzzle(newlist, self._marker_set))

                            newlist[i][j] = "."
                            newlist[i][j+1] = "*"
                            newlist[i][j+2]= "*"



        return ext



    # TODO
    # override is_solved
    # A configuration is solved when there is exactly one "*" left
    def is_solved(self):
        peg = 0

        for i in range(0,len(self._marker)):
            for j in range(0, len(self._marker[i])):
                if self._marker[i][j] == "*":
                    peg += 1
                if peg > 1:
                    return False
        return True
        '''
        for i in self._marker:
            for char in i:
                if char == "*":
                    peg = peg + 1
        if peg > 1:
            return False
        return True
        '''


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})


    import time

    start = time.time()

    solution = depth_first_solve(gpsp)

    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
