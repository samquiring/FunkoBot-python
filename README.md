# FunkoBot
 A python bot made using selenium to purchase items right when they drop from selected sites
 
 This was orignally made specifically for funkopop drops but it should work for any drop
 
 Currently functional bots: Funko.com, Hottopic.com
 
 How to run: 
 1. Download all files
 2. pip install selenium
 3. install chromedriver
 3. edit the user_information text file to contain
 the contents for the page you want to bot
 4. run the bot_gui
 5. import the user_information

How it works:
It uses Selenium to create a automated brower where it goes to the
desired site to bot and then enters your login information. 
It then goes to the product and refreshes the page until the product
is available and then purchases it and enters all the user information.


Note: It doesn't click the final button to purchase because I never actually
bought anything with it.

Note 2: This bot is purely for testing purposes and you should use at your own risk
