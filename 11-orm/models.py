
class Actor:
    def __init__(self, aid, lname, middle, fname, upd):
        self.id = aid
        self.last_name = lname
        self.first_name = fname
        self.last_update = upd
        self.middle_name = middle

    def __str__(self):
        return self.last_name + ", " + self.first_name
