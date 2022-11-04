from selenium.webdriver import ActionChains, Keys
from Config.configdata import *
from Utilities.LoginPageUtilities import *
from Utilities.HomePageUtilities import *
from Utilities.CommonPageUtilities import *
from Locators.paymentpagelocators import *
import time

class TestLoginPage:

    @pytest.mark.smoke
    @pytest.mark.usefixtures("initiate_Driver")
    def test_verify_login_with_correct_credentials(self, initiate_Driver):

        CommonFunctions().click(signin)
        LoginPageFunctions().perform_login(correct_mail, correct_passwor)
        CommonFunctions().wait_for_element(prof)

        assert driver.find_elements(By.CSS_SELECTOR, prof), "the login was not successfull"

    def test_verify_login_with_incorrect_credentials(self, initiate_Driver):

        CommonFunctions().click(signin)
        LoginPageFunctions().perform_login(correct_mail, incorrect_passwor)
        CommonFunctions().wait_for_element(incorrect_id_or_pass)

        assert driver.find_elements(By.CSS_SELECTOR,incorrect_id_or_pass), "the login was successfull"

    def test_play_entered_song(self, initiate_Driver):

        CommonFunctions().click(signin)
        LoginPageFunctions().perform_login(correct_mail, correct_passwor)
        HomePageFunctions().search_song(song_name)
        HomePageFunctions().play_searched_song()
        CommonFunctions().wait_for_element(pause_button)
        time.sleep(100)
        assert driver.find_elements(By.CSS_SELECTOR, pause_button), "the song did not play"


    def test_add_searched_song_toEntered_playlist(self, initiate_Driver):

        CommonFunctions().click(signin)
        LoginPageFunctions().perform_login(correct_mail, correct_passwor)
        HomePageFunctions().search_song(song_name)
        HomePageFunctions().add_searched_song_to_entered_playlist(playlist_name)
        time.sleep(5)
        CommonFunctions().wait_for_element(added_to_playlist_indicator)
        assert driver.find_elements(By.CSS_SELECTOR, added_to_playlist_indicator), "the song did not play"

    def test_play_entered_album(self, initiate_Driver):

        CommonFunctions().click(signin)
        LoginPageFunctions().perform_login(correct_mail, correct_passwor)
        HomePageFunctions().search_song(album_name)
        HomePageFunctions().play_album()
        CommonFunctions().wait_for_element(pause_button)
        assert driver.find_elements(By.CSS_SELECTOR, pause_button), "the album did not play"

















