class Label:
    def __init__(self, x, y, text=''):
        self.x = x 
        self.y = y 
        self.text = text 

    def draw(self, window):
        window.blit(self.text, (self.x, self.y))

    def __repr__(self):
        return self.text