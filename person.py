class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def talk(self, phrase):
        print(phrase)
        return 'OK'

    def walk(self):
        print('I am walking')
        return 'OK'