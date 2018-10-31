# from driver import Driver
# daniel = Driver("Daniel", "fast and furious")
# alice = Driver("Alice", "faster and furiouser")
# jeff = Driver("Jeff", "defensive")
#
# from passenger import Passenger
# jake = Passenger("Jake", 29)
# anna = Passenger("Anna", 25)
# katie = Passenger("Katie", 20)
#
# from trip import Trip
# # create trip instances here using the above passenger and driver instance objects
# trip_one = Trip(daniel, jake)
# trip_two = Trip (alice, anna)
# trip_three = Trip (jeff, katie)
# trip_four = Trip(daniel, katie)


from artist import Artist
lady_gaga = Artist("Lady Gaga")
lcd_soundsystem = Artist("LCD Soundsystem")
vulfpeck = Artist("Vulfpeck")

from genre import Genre
pop = Genre("Pop")
rock = Genre("Rock")
alt = Genre("Alternative")
indie = Genre("Indie")
folk = Genre("Folk")
country = Genre("Country")
funk = Genre("Funk")
jam = Genre("Jam")

from song import Song
bad_romance = Song('Bad Romance', lady_gaga, pop)
dance_yrself_clean = Song('Dance Yrself Clean', lcd_soundsystem, alt)
back_pack = Song('Back Pocket', vulfpeck, funk)
