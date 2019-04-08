class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length= length
    def __str__(self):
        return '{0} - {1} from {2} - {3}'.format(self.title, self.artist, self.album, self.length)
    def __repr__(self):
        return self.title + self.artist + self.album + self.length
    def __eq__(self, other):
        if self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length:
            return True
        else:
            return False
    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.length))
    def length_seconds(self):
        current_length = self.length.split(':')
        if len(self.length)<=4:
            return int(current_length[0])*60 + int(current_length[1])
        else:
            return int(current_length[0])*3600 + int(current_length[1])*60 + int(current_length[2])
    def length_minutes(self):
        current_length = self.length.split(':')
        if len(self.length)<=4:
            return int(current_length[0])
        else:
            return int(current_length[0])*60 + int(current_length[1])

    def length_hours(self):
        current_length = self.length.split(':')
        if len(self.length)<=4:
            return 0
        else:
            return int(current_length[0])
    def length_string(self):
        return str(self.length)

class Playlist(Song):
    def __init__(self, name, songs, repeat = False, shuffle = False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = songs
        
    def add_song(self, song):
        lst_title.append(song.title)



def main():
    first = Song('Subversive', 'Stone Sour', 'Hydrograd', '1:33:55')
    print(str(first))
    print(first.length_seconds())
    print(first.length_minutes())
    print(first.length_hours())
    print(first.length_string())
if __name__ == '__main__':
    main()