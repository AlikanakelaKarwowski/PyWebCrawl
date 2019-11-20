# **PyWebCrawler** is an open source project Tyler and I created to help automate the ticket warranty audit process.


## Instructions:

1. Must have python installed 2.7 or greater

      a. If you do not have python installed, goto https://www.python.org/downloads/ and download version 3.8 or higher for your operating system.

      b. When you install python, there is an option to "ADD TO PATH". Make sure that is checked before installing.

2. Make sure that you have Python added to your PATH. If you don't have it added to your PATH, or are not sure, follow the directions [here](https://datatofish.com/add-python-to-windows-path/)
3. Download the chromedriver for selenium. The chromedriver included in this git is for chrome version 79. Make sure to update chrome to version 79 for this script to work correctly. Click [here](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) for instructions on how to update your version of chrome.  
4. Open up command prompt, terminal, or Powershell with administrative rights (or use sudo), and install the selenium library for python. Type `pip install selenium`.
5. After installing selenium, type `pip install pynput`, to install the pynput library.
6.
6. Some trial and error may be needed depending on screen resolution and size. run the setup script `python pyMouseSetup.py` and type in the numbers accordingly.
7. Run the program in cmd/powershell/terminal by typing `python .\pyCrawler-Web.py`
8. A new chrome browser will open up to the ticketing site and the program will ask you for your username and password. DONT F*CK THIS UP
9. Do not move the mouse while it is working, Or you'll F*CK  it up.
10. Watch as my little program does the tedious shit for you, sit back, relax and watch netflix or hulu on your phone.
11. This only does 25 entries at a time to reduce the risk of F*CK UPS. Do more at your own risk.
12. Start from the end so no one else works on the same ticket number as you. Its even in the setup.
