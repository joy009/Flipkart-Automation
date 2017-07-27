# Flipkart-Automation
<b>Installation:</b>
  * Clone the p4p-automation project into the local system.
  * Install the python 27 package. If pip is installed in command prompt then "pip install python" command can be used. Else pip can be installed first.
  * Download and install pycharm. (Community version will be preferred.)
  * Open pycharm and the import the p4p-automation project from where it was cloned.
  * Install the selenium webdriver packages for which notification will be displayed on the pycharm. Or Selenium can also be installed from the command prompt using the command "pip install selenium".
  * Download and install chromedriver.
  * Set the path of the python27 in the local system environment variables.
  * Set the path of the chromedriver in the webdriver.py file. The webdriver.py file will be inside the python package. If the python27 is package is installed in c drive, then the path will be C:\Python27\Lib\site-packages\selenium\webdriver\chrome\webdriver.py
  * The Project is now ready to be worked on.
  
<b> Requirements to execute the tests:</b>
  * Goto the "credentials.json" file which is present on the "resources" folder. Under valid credentials, provide a give a valid email and valid password. Currently it is given as test@test.com(username) and test(pwd).
  * There is a "run_tests" file. Set this file as run configuration in the pycharm editor. The test case should be run using that.

<b> How to see the result</b>
 * On the pycharm console a report will be generated which will display the number of test case run, passed, failed etc.
 * Also, there is a "summary.html" file. Open this file and this would display the results summary.
 * There is a "log" file inside the reports/log folder which shows the log of the recently run test case.
 * There is a "Page source" folder inside "reports" folder. This folder contains the source code of the web page on which the test case was run.
 * There is a "screenshots" folder which contains the screenshot of the page if a particular test was failed on a certain page.
