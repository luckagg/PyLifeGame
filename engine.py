#!/usr/bin/python
#-*-coding:utf-8 -*

"""
Author: Guillaume Griggo
Last Edited: 19/03/2018
"""

class Engine(object):
    """Class to determine the evolution of the grid of the game of life"""
    def __init__(self):
        super(Engine, self).__init__()

    def next(*grid):
        """
            Function calculating the state of the next generation:
            
            :param grid: grid representing the current generation
            :type grid: List of Lists

            :Example:
            >>> e = Engine()
            >>> e.next([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
            [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

            >>> e = Engine()
            >>> e.next([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
            [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        """

        grid = grid[1]

        ret = list()
        nbNeighbors = 0

        for i, row in enumerate(grid):
            ret.append(list(row))
            startVertIndex = i - 1
            endVertIndex = i + 2

            if i == 0:
                startVertIndex = i
            if i == len(grid) - 1:
                endVertIndex = i + 1

            for j, cell in enumerate(row):
                nbNeighbors = 0
                startHorIndex = j - 1
                endHorIndex = j + 2
                
                if j == 0:
                    startHorIndex = j
                if j == len(grid[i]) - 1:
                    endHorIndex = j + 1

                for k in range(startVertIndex, endVertIndex):
                    for l in range(startHorIndex, endHorIndex):
                        if k != i or l != j:
                            nbNeighbors += grid[k][l]

                ret[i][j] = 1 if nbNeighbors == 3 or ( nbNeighbors == 2 and grid[i][j] ) else 0

        return ret

if __name__ == '__main__':
    import doctest
    doctest.testmod()
