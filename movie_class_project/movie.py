import webbrowser

class Film():

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_url = poster
        self.trailer_url = trailer        

    def watch_trailer(self):
        webbrowser.open(self.trailer_url)


    def see_poster(self):
        webbrowser.open(self.poster_url)
