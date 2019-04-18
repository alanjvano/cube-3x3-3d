import copy

# define Rubik's cube using a class structure
class Cube():

    cycles = {
        'u': [[(0,0), (0,2), (0,8), (0,6)], [(0,1), (0,5), (0,7), (0,3)]],
        'l': [[(0,0), (0,6), (2,6), (2,0)], [(0,3), (1,6), (2,3), (1,0)]], 
        'f': [[(0,6), (0,8), (2,8), (2,6)], [(0,7), (1,8), (2,7), (1,6)]],
        'r': [[(0,8), (0,2), (2,2), (2,8)], [(0,5), (1,2), (2,5), (1,8)]],
        'b': [[(0,2), (0,0), (2,0), (2,2)], [(0,1), (1,0), (2,1), (1,2)]],
        'd': [[(2,6), (2,8), (2,2), (2,0)], [(2,3), (2,7), (2,5), (2,1)]]}
    
    def __init__(self, size):

        # define each cubie with [position, twist=0]
        self.cube = [[[9*j + i, 0] for i in range(size ** 2)] for j in range(size)]

    # p: [face, dir, double]
    def turn(self, p):
        if p[0] not in Cube.cycles:
            return False
        
        # tmp copy of cube
        tmp = copy.copy(self.cube)
        print("tmp",tmp,'\n')
        
        for cycle in Cube.cycles[p[0]]:
            print('cycle',cycle)
            for ind, val in enumerate(cycle):
                print(ind, val)
                target = cycle[(ind + 1) % 4]
                print(target)
                self.cube[val[0]][val[1]] = tmp[target[0]][target[1]]
        print(self.cube)

        return True
        
cube1 = Cube(3)
print(cube1.cube,'\n')
print(Cube.cycles,'\n')
print(cube1.turn('f'))
