'''
>>> lemming = Lemming('level.txt', 3, '<')
>>> lemming.position()
(3, 3, '<')
>>> print(lemming)
#################################
#                               #
#         #                     #
#  <    ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.step()
(3, 2, '<')
>>> print(lemming)
'''
class Lemming(object):
    def __init__(self, text, col, direction):
        #super(Lemming, self).__init__()
        #self.text = text
        self.col = col
        self.direction = direction
        self.space = [line.rstrip('\n') for line in open(text, 'r')]
        self.row = self.ground()

    def position(self):
        return self.row-1, self.col, self.direction

    def ground(self):
        for rownum,i in enumerate(self.space[1:-1],1):
            if i[self.col] != " ":
                return rownum

    def __str__(self):
        rowstr = self.space[self.row-1]
        newrow = ''.join((rowstr[:self.col],self.direction,rowstr[self.col+1:]))
        copy_space = self.space
        copy_space[self.row-1] = newrow
        return '\n'.join(i for i in copy_space)

    def step(self):
        if self.direction == '>': #to right
            if self.space[self.row][self.col+1] == "#": #may have wall
                if self.space[self.row-1][self.col+1] =="#": #have big wall
                    self.direction = '<'
                else:
                    self.col +=1
            elif self.space[self.row+1][self.col+1] == "#": #having ground
                self.col +=1
            else: #no wall and no ground == cliff
                self.row -=1
        elif self.direction == '<': #to left
            if self.space[self.row][self.col-1] == "#": #may have wall
                if self.space[self.row-1][self.col-1] =="#": #have big wall
                    self.direction = '<'
                else:
                    self.col -=1 #move forward left
            elif self.space[self.row+1][self.col-1] == "#": #having ground
                self.col -=1 #move forward left
            else: #no wall and no ground == cliff
                self.row -=1  #if cliff, walls minus row
        return self.position()
        #elif self.direction == '<': #to left

if __name__ == '__main__':
    import doctest
    doctest.testmod()
# lemming = Lemming('level.txt', 3, '<')