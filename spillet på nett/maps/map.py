
#Import statement
from random import randint

class RoomError(Exception):
    pass
#Defining a class which name is room. 
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

#The story. 
start = Room("start",
"""
Velkommen til eventyrland. Bli med paa et kjempe morsomt spill! 
                
Lukk browseren hvis du IKKE har lyst til aa bli med!
				
Trykk fortsett for aa bli med! Kom igjen, ikke vaer kjip naa!
				
Hva velger du?
                 """              
)


rom3 = Room("rom3",
"""
Du kan velge brus eller is!
Liker du ikke brus eller is, gaa til rom2 og velg mellom andre premier!
Hva velger du?
                 
"""
)


magisk_slott = Room("magisk_slott",
"""
Du er inne i det magiske slottet. 
Du maa beseire den onde Styggen, klarer du det faar du premie.
skriv inn rom2 eller rom3 og du kan vinne en fantastisk premie...
""")


rom2 = Room("rom2",
"""
Velkommen til rom2.
Her kan du velge kake eller kaffe!
Liker du ikke kake eler kaffe, gaa til rom3 da!
Hva velger du?

  
""")


kake = Room("kake",
"""Takk for at du spilte, her har du kaka
"""
)


kaffe = Room("kaffe",
"""
Takk for at du spilte, her har du en kopp kaffe
"""
)

isrom = Room("isrom",
""" Takk for at du spilte, her har du en is"""
)

brus = Room("brus",
"""Takk for at du spilte, her har du ei brus """
)
generic_death = Room("death", "You died")


rom3.add_paths({
    'is': isrom,
    'brus': brus,
    'rom2': rom2
})


magisk_slott.add_paths({
    'rom2': rom2,
    'rom3': rom3
})


start.add_paths({
    'fortsett': magisk_slott,
    	
})
rom2.add_paths({
    'kake': kake,
    'kaffe':kaffe,
    'rom3': rom3
})

START = start
