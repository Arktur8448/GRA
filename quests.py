class Quest:
    def __init__(self, name, description,required_level, difficulty, to_complete):
        self.name = name
        self.description = description
        self.required_level = required_level
        self.difficulty = difficulty
        self.to_complete = to_complete
        self.progress = None
        self.is_completed = False

    def complete(self):
        if self.progress == self.to_complete:
            self.is_completed = True
            return True
        else:
            return False

        # dla mirosa
        # self.to_complete to jest zmienna jako liczba lub string
        # działa jak special_effect w perkach
        # czyli to nie musi być np zabij 10 golbinów tylko np może być porozmawiaj z Krisem
        # jedyne co musisz zrobic to aby skończyć questa, to musi byc self.progress == self.to_complete
        # :) ~ Jan
