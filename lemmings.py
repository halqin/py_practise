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
>>> lemming.step()
(3, 1, '<')
>>> lemming.step()
(3, 1, '>')
>>> lemming.step()
(3, 2, '>')
>>> print(lemming)
#################################
#                               #
#         #                     #
# >     ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.steps(5)
[(3, 3, '>'), (3, 4, '>'), (3, 5, '>'), (3, 6, '>'), (3, 7, '>')]
>>> print(lemming)
#################################
#                               #
#         #                     #
#      >###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################

>>> lemming.step()
(2, 8, '>')
>>> print(lemming)
#################################
#                               #
#       > #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.step()
(2, 9, '>')
>>> lemming.step()
(1, 10, '>')
>>> print(lemming)
#################################
#         >                     #
#         #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.step()
(6, 11, '>')
>>> print(lemming)
#################################
#                               #
#         #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########> ##############     #
#################################
>>> lemming.steps(21)
[(6, 12, '>'), (5, 13, '>'), (5, 14, '>'), (4, 15, '>'), (4, 16, '>'), (3, 17, '>'), (3, 18, '>'), (3, 19, '>'), (4, 20, '>'), (4, 21, '>'), (4, 22, '>'), (5, 23, '>'), (5, 24, '>'), (5, 25, '>'), (5, 26, '>'), (6, 27, '>'), (6, 28, '>'), (6, 29, '>'), (6, 30, '>'), (6, 31, '>'), (6, 31, '<')]
>>> lemming.steps(21)
[(6, 30, '<'), (6, 29, '<'), (6, 28, '<'), (6, 27, '<'), (5, 26, '<'), (5, 25, '<'), (5, 24, '<'), (5, 23, '<'), (4, 22, '<'), (4, 21, '<'), (4, 20, '<'), (3, 19, '<'), (3, 18, '<'), (3, 17, '<'), (4, 16, '<'), (4, 15, '<'), (5, 14, '<'), (5, 13, '<'), (6, 12, '<'), (6, 11, '<'), (6, 11, '>')]
>>> print(lemming)
#################################
#                               #
#         #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########> ##############     #
#################################
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
        return self.row, self.col, self.direction

    def ground(self):
        for rownum,i in enumerate(self.space[1:-1],1):
            if i[self.col] != " ":
                return rownum-1

    def __str__(self):
        rowstr = self.space[self.row]
        newrow = ''.join((rowstr[:self.col],self.direction,rowstr[self.col+1:]))
        copy_space = self.space.copy()
        copy_space[self.row] = newrow
        return '\n'.join(i for i in copy_space)

    def step(self):
        if self.direction == '>': #to right
            if self.space[self.row][self.col+1] == "#": #may have wall
                if self.space[self.row-1][self.col+1] =="#": #have big wall
                    self.direction = '<'
                else:
                    self.col +=1 #small wall,let's fo
                    self.row -=1
            elif self.space[self.row+1][self.col+1] == "#": #having ground
                self.col +=1
            elif self.space[self.row+2][self.col+1] == "#": #no wall and no ground , maybe down step
                self.row +=1
                self.col +=1
            else: #real cliff!
                self.row +=5
                self.col +=1
        elif self.direction == '<': #to left
            if self.space[self.row][self.col-1] == "#": #may have wall
                if self.space[self.row-1][self.col-1] =="#": #have big wall
                    self.direction = '>' #changing direction
                else:
                    self.col -=1 #small wall, let's fo
                    self.row -=1
            elif self.space[self.row+1][self.col-1] == "#": #having ground
                self.col -=1 #move forward left
            elif self.space[self.row+2][self.col-1] == "#": #maybe down step
                self.col -=1
                self.row +=1
            else: #real cliff
                self.row +=5  #if cliff, walls minus row
                self.col +=1
        return self.position()
        #elif self.direction == '<': #to left
    def steps(self, num_step):
        return [self.step() for _ in range(num_step)]
if __name__ == '__main__':
    import doctest
    doctest.testmod()
# lemming = Lemming('level.txt', 3, '<')