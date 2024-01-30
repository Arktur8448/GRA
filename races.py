class Race:
    def __init__(self, name,description, health, mana,strength, defence, agility,stamina,):
        self.name = name
        self.description = description
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defence = defence
        self.agility = agility
        self.stamina = stamina


class NonPlayableRace():
    def __init__(self,name,description,health,mana,strength,agility,stamina):
        self.name = name
        self.description = description
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.stamina = stamina


Human = Race("Human", "Wszechstronne istoty zdolne do różnych profesji i umiejętności.", 25, 10, 10, 10, 5, 10)
Elf = Race("Elf", "Długowieczne istoty o zwinności i smukłej budowie, często utalentowane w magii i sztukach walki.", 20, 15, 3, 5, 10, 15)
Dwarf = Race("Dwarf", "Mocne i wytrzymałe istoty o umiejętnościach rzemieślniczych, często mieszkające w górach.", 20, 5, 8, 5, 5, 5)
Orc = Race("Orc", "Silne i agresywne istoty, znane ze swojej siły fizycznej i zdolności do walki.", 40, 20, 15, 10, 3, 15)
Vampire = Race("Vampire", "Nieumarłe istoty, które żywią się krwią, posiadające różnorodne zdolności nadnaturalne.", 25, 10, 5, 5, 10, 5)
Drakonid = Race("Drakonid", "Pół-człowiek, pół-smok, posiadający zdolności związane z ogniem, lodem lub innymi elementami, w zależności od rodzaju smoka.", 40, 20, 10, 10, 10, 15)
Titan = NonPlayableRace("Titan", "Ogromne istoty, które kiedyś rządziły światem, obecnie uwięzione w odległych zakątkach świata.", 100, 50, 30, 20, 20)
Skeleton = NonPlayableRace("Skeleton", "Słabe istoty.", 15, 10, 5, 5, 5)
Griffin = Race("Griffin", "Potomkowie gryfonów, dobrzy łucznicy.", 30, 5, 5, 15, 3, 10)
Ghost = NonPlayableRace("Ghost", "Potrafią zniknąć.", 20, 20, 2, 15, 10)
Friend = NonPlayableRace("Friend","git ziut",25,10,10,10,10)


# races = [Human, Elf, itp...]
