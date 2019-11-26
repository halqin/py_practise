'''
>>> lemming = Lemming('level.txt', 3, '<')
#>>> lemming.position()
#(3, 3, '<')
'''
class Lemming(object):
    def __init__(self, text, col, direction):
        #super(Lemming, self).__init__()
        #self.text = text
        self.col = col
        self.direction = direction
        self.space = [list(line.rstrip('\n')for line in open(text, 'r'))]
        #self.row = 0
        self.row = self.ground()

    def postion(self):
        return "({}, {}, {})".format(self.row, self.col, self.direction)

    def ground(self):
        for rownum,i in enumerate(self.space[1:-1]):
            if i[self.col] != " ":
                self.row = rownum-1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
