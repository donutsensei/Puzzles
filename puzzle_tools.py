"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
#set higher recursion limit
#which is needed in PuzzleNode.__str__
#uncomment the next two lines on a unix platform, say CDF
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    path = PuzzleNode(puzzle, puzzle.extensions(),None)

    if path.children:
        for child in path.children:
            childResult = depth_first_solve(child)
            if(childResult != None):
                return childResult

    if puzzle.is_solved():
        return path
    return None



    # get to a node.
    # dequeue the front node,
    # enqueue to the front, the children of that node.
    # continue.
    #
    # queue = a queue
    #
    # 1. put the root node in
    # [root]
    # 2. dequeue the root node,
    # [] , we have a root object
    # 3. append to the queue the root's children.'
    # [root_1, root_2]
    # 4. repeat.
    # 5. traverse to root one.
    # 6. dequeue the front node.
    # [root_2] , root_1
    # 7. engqueue to te font, the children of root_1.
    # [root_1_1, root_1_2, root_2]
    #
    # .....
    #
    # [root_1_1_1, root_1_2, root_2]
    # 8. root_1_1_1 is just dequeued, destoryed, kaboom.
    # [root_1_2, root_2]
    # 9. dequeue root_1_2, and append children etc.
    #

# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """

    path = PuzzleNode(puzzle, puzzle.extensions(),None)
    if path.children:
        for child in path.children:
            childResult = depth_first_solve(child)
            if(childResult != None):
                return childResult

    if puzzle.is_solved():
        return path
    return None


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle =None, children =None, parent =None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
