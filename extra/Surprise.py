import youtube_dl
import pafy
import vlc

class Surprise():
    '''
        Proxy class to create a popup window that streams a video
            from YouTube
        Code adapted from https://stackoverflow.com/questions/49354232/stream-youtube-audio-from-python-using-url-without-downloading-python
    '''

    def __init__(self):

        # Sets up YouTube stream    
        youtube_url = "https://www.youtube.com/watch?v=Gg6fjUm9xLs"
        video = pafy.new(youtube_url)
        best_video = video.getbest()
        self.url = best_video.url
        self.vlc_player = None

    def getVideo(self):
        '''
            Opens VLC Player and streams video
            args: none
            return: none
        '''

        vlc_popup = vlc.Instance()
        self.vlc_player = vlc_popup.media_player_new()
        surprise_video = vlc_popup.media_new(self.url)
        surprise_video.get_mrl()
        self.vlc_player.set_media(surprise_video)
        self.vlc_player.play()

    def endVideo(self):
        '''
            Stops video stream
            args: none
            return: none
        '''
        self.vlc_player.stop()



def test():

    surprise = Surprise()
    surprise.getVideo()

test()
