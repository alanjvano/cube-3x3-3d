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

    # p: [face, num of rotations]
    def turn(self, p):
        if p[0] not in Cube.cycles:
            return False
        
        for i in range(p[1]):
            
            # tmp copy of cube
            tmp = copy.deepcopy(self.cube)
            
            for cycle in Cube.cycles[p[0]]:
                #print('cycle',cycle)
                for ind, val in enumerate(cycle):
                    #print(ind, val)
                    target = cycle[(ind + 1) % 4]
                    #print('cur',self.cube[val[0]][val[1]],'target',target,tmp[target[0]][target[1]])
                    self.cube[val[0]][val[1]] = tmp[target[0]][target[1]]

        return True

    # display array format of cube in shell
    def show(self):
        for layer in self.cube:
            print(layer)
        
cube1 = Cube(3)
print(cube1.cube,'\n')
cube1.turn(['f',4])
cube1.show()
