from Locators.AfterSearchLocators import *
from Locators.homepagelocators import *
from Utilities.CommonPageUtilities import *


class HomePageFunctions:

    def search_song(self, song_name):
        CommonFunctions().click(search_song_clk)
        CommonFunctions().fill_fields(search_song_field, song_name)
        CommonFunctions().wait_for_element(song_album_banner_after_search)

    def play_searched_song(self):
        CommonFunctions().click(play_song)

    def options_for_searched_song(self):
        CommonFunctions().click(options_for_searched_song)

    def add_searched_song_to_entered_playlist(self, playlist_name):
        self.options_for_searched_song()
        CommonFunctions().click(addto_playlist_button)
        CommonFunctions().fill_fields(search_for_playlistTo_add, playlist_name)
        CommonFunctions().click(addto_searched_playlist)

    def play_album(self):
        CommonFunctions().click(album_button)
        CommonFunctions().click(album_open)
        CommonFunctions().click(playAlbum_click)

   # def upgrade_to_premium_button















