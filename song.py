class Song:

    _all = []

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        Song._all.append(self) # remember to keep track of all trip instances

# GETTERS
    @property
    def name(self):
        return self._name

    @property
    def artist(self):
        return self._artist

    @property
    def genre(self):
        return self._genre

#  SETTERS

    @name.setter
    def name(self,name):
        self._name = name

    @artist.setter
    def artist(self,artist):
        self._artist = artist

    @genre.setter
    def genre(self,genre):
        self._genre = genre

# CLASS METHODS
    @classmethod
    def all(cls):
        return Song._all
