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
        self.row, self.col =0, col
        self._direction = self.direction(direction)
        self.space = [line.rstrip('\n') for line in open(text, 'r')]
        self.ground()

    def position(self):
        return self.row, self.col, self.trans(self._direction)

    def direction(self,dir):
        return 1 if dir=='>' else -1

    def trans(self, num):
        return '>' if num ==1 else '<'

    def ground(self):
        while self.space[self.row+1][self.col] != "#": #until hit the ground
            self.row +=1

    def __str__(self):
        newrow = self.space[self.row][:self.col]+self.trans(self._direction)+self.space[self.row][self.col+1:]
        return '\n'.join(
            self.space[i] if i != self.row else newrow
            for i in range(len(self.space))
            )

    def step(self):
        if self.space[self.row][self.col+self._direction] == " ": #empty or cliff?
            self.col += self._direction
            self.ground() # if cliff, then change row until ground
        elif self.space[self.row-1][self.col+self._direction] == " ": #small step?
            self.col += self._direction  #it is small step
            self.row -=1
        else: #no wall
            self._direction = -(self._direction)
        return self.position()
    #     #elif self.direction == '<': #to left
    def steps(self, num_step):
         return [self.step() for _ in range(num_step)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
# lemming = Lemming('level.txt', 3, '<')