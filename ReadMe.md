# **PyWebCrawler** is an open source project Tyler and I created to help automate the ticket warranty audit process.


## Instructions:

1. Must have python installed 2.7 or greater

      a. If you do not have python installed, goto https://www.python.org/downloads/ and download version 3.8 or higher for your operating system.

      b. When you install python, there is an option to "ADD TO PATH". Make sure that is checked before installing.

2. Make sure that you have Python added to your PATH. If you don't have it added to your PATH, or are not sure, follow the directions [here](https://datatofish.com/add-python-to-windows-path/)
3. Download the chromedriver for selenium.

      a. The chromedriver included in this repository is for chrome version 79. Make sure to update chrome to version 79 for this script to work correctly.

      b. Click [here](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) for instructions on how to update your version of chrome.  
4. Open up command prompt, terminal, or Powershell with administrative rights (or use sudo), and install the selenium library for python. This can be done by typing `pip install selenium`.
5. After installing selenium, type `pip install pynput`, to install the pynput library.
6. Some trial and error may be needed depending on screen resolution and size to get the script to run correctly. Open cmd, terminal or Powershell, goto your folder with the scripts located in it and run the setup script `python pyMouseSetup.py` and follow the directions, only clicking the mouse when necessary. It will create a log file in the folder that tells you the position of all your clicks. This should be a good enough starting point to get proper positions for the mouse.
7. After you have your positions, update them in `pyCrawler-Web.py` for variables p1-p7. Also type your username and password into the appropriate variables, and save the file.
8. Finally you can run the program in cmd, terminal, or Powershell by typing `python .\pyCrawler-Web.py` or by double clicking the file in the repository folder.
9. A new chrome browser will open up to the ticketing site and the program will go through the required steps to get setup. Do not worry if it seems like its stalled or not running, it most likely is waiting for the page to load.
10. The end. It has some built in error handling so if something goes wrong it will try to fix itself. But be wary.
