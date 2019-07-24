# FacebookAds API Python connect
This is a project that uses a facebookads lib for python, I customized it to meet my needs

First you need to install FacebookAds lib and set yours informations from facebookads manager. Use this link to get the steps:

https://github.com/facebook/facebook-python-business-sdk?fbclid=IwAR1_lPziqj1dPxYHcji0GGc1TnbUa4TaWIKaMDSYXj136SHxGCcOXSpjZTg

This lib outdated, there are graph API v3.3, but the lib uses v2.1. You need to change on the directory of the lib after install.

Step 1 - change to 3.3 the names on the file apiconfig.py on this directory in your computer:

Lib\site-packages\facebookads

Step 2 - This lib is outdated as I said above, and python received new update, the request assynchronous on python was updated.
Before was async, now is async_

Execute the file ReconfigureAsync.py to change this.

Step 3 - Set yours informations on facebookConfig.py

