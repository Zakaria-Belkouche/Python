# Zakaria Belkouche 25/10/25

class FileItem:
    def __init__(self, name, permissions, owner, size):
        self.name = name
        self.permissions = permissions
        self.owner = owner
        self.size = size

    def fileDetails(self):
        return f"NAME: {self.name}, PERMISSIONS: {self.permissions}  OWNER: {self.owner}  SIZE: {self.size}"

class CsvFile(FileItem):
    def __init__ (self, name, permissions, owner, size, rows, columns):
        super().__init__(name, permissions, owner, size)
        self.rows = rows
        self.columns = columns

    def fileDetails(self):
        x = super().fileDetails()
        print(f"{x}  ROWS: {self.rows}   COLUMNS: {self.columns}")

class JPG(FileItem):
    def __init__ (self, name, permissions, owner, size, colour_mode, orientation):
        super().__init__(name, permissions, owner, size)
        self.colour_mode = colour_mode
        self.orientation = orientation

    def fileDetails(self):
        x = super().fileDetails()
        print(f"{x}, COLOUR: {self.colour_mode}, ORIENTATION: {self.orientation}")

class MP3(FileItem):
    def __init__ (self, name, permissions, owner, size, artist, duration):
        super().__init__ (name, permissions, owner, size)
        self.artist = artist
        self.duration = duration

    def fileDetails(self):
        x = super().fileDetails()
        print(f"{x}, ARTIST: {self.artist},  DURATION: {self.duration}")


csv1 = CsvFile("hello.csv", "rw-", "Zak", 512, 1000, 6)
csv2 = CsvFile("Iam.csv", "r--", "Zak", 597, 960, 20)
csv3 = CsvFile("happy.csv", "--x", "Zak", 250, 800, 10)

csv1.fileDetails()
csv2.fileDetails()
csv3.fileDetails()

JPG1 = JPG("This.jpg", "rwx", "Zak", 692, "on", "Landscape")
JPG2 = JPG("is.jpg", "rwx", "Zak", 321, "off", "Portrait")
JPG3 = JPG("Picture.jpg", "rw-", "Zak", 642, "on", "Landscape")

JPG1.fileDetails()
JPG2.fileDetails()
JPG3.fileDetails()

MP3_1 = MP3("This.mp3", "r--", "Zak", 321, "Cool Singer", "10 hours :)")
MP3_2 = MP3("Is.mp3", "rw-", "Zak", 211, "Funny Singer", "20 minutes")
MP3_3 = MP3("Song.mp3", "rwx", "Zak", 11174, "Nice Singer", "2 hours")

MP3_1.fileDetails()
MP3_2.fileDetails()
MP3_3.fileDetails()


# Challange has not been done yet. Honestly, It's 00:30, and I'm just happy I understand Inheritance!
