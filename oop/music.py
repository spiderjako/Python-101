class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length= length
    def __str__(self):
        return '{0} - {1} from {2} - {3}'.format(self.title, self.artist, self.album, self.length)
    def __eq__(self, other):
        if self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length:
            return True
        else:
            return False
    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.length))
    def length(self):
        
        if len(self.length)<=5:
            self.length.pop(self.length.find(':'))
            current_length = self.length

def main():
    first = Song('Subversive', 'Stone Sour', 'Hydrograd', '3:55')
    print(str(first))

if __name__ == '__main__':
    main()