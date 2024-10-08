from BrowserPackage.OpenBrowser import startBrowser
from BrowserPackage.CloseBrowser import closeBrowser

def test_case():
    startBrowser()
    print("I am executing")
    closeBrowser()

test_case()