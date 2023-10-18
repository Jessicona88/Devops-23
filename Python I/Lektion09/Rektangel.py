class Rektangel:
    def __init__(self):
        self.startpunkt = 0
        self.höjd = 0
        self.bredd = 0

    def area(self):
        return self.höjd * 2 * self.bredd * 2

    def omkrets(self):
        return self.höjd * 2 + self.bredd * 2

    def __str__(self):
        return f"Arean är {self.area()}"