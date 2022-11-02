from Locators.loginpagelocators import *
from Utilities.CommonPageUtilities import *



class LoginPageFunctions:

    def perform_login(self, correct_mail, correct_passwor) -> None:

        CommonFunctions().fill_fields(username, correct_mail)
        CommonFunctions().fill_fields(password, correct_passwor)
        CommonFunctions().click(loginclk)



