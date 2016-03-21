from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you

    def __eq__(self, other):

        return other == self

    def __str__(self):

        return (self.from_grid + " must turn into " + self.to_grid)

    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"

    def extensions(self):

        ext = []

        for i in range(0, len(self.from_grid) + 1):
            for j in range(0, len(i) + 1):
                if self.from_grid[i][j] == "*":

                    #SWITCHING WITH THE LEFT
                    newlist = self.from_grid
                    store = newlist[i][j]
                    newlist[i][j] = newlist[i][j-1]
                    newlist[i][j-1]= store

                    ext.append(newlist)

                    #SWITCHING WITH THE RIGHT
                    newlist = self.from_grid
                    store = newlist[i][j]
                    newlist[i][j] = newlist[i][j+1]
                    newlist[i][j+1]= store
                    
                    ext.append(newlist)

                    #SWITCHING WITH THE TOP
                    newlist = self.from_grid
                    store = newlist[i][j]
                    newlist[i][j] = newlist[i-1][j]
                    newlist[i-1][j]= store

                    ext.append(newlist)

                    #SWITCHING WITH THE BOTTOM
                    newlist = self.from_grid
                    store = newlist[i][j]
                    newlist[i][j] = newlist[i+1][j]
                    newlist[i+1][j]= store

                    ext.append(newlist)

        return ext



    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid

    def is_solved(self):

        return from_grid == to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
