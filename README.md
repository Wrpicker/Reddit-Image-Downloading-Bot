# Reddit-Image-Downloading-Bot
This script can take up to 5 subreddits and download images from them, saving them into a file.

## DEPENDENCIES:

-Asyncpraw

-Urllib

-OS

-Asyncio

## HOW TO USE:

There are 4 files necessary:

-The Main Python Script

-A Directory text file

-A Client Information text file

-A Subreddit text file

##### **The Main Python Script:**

For this one, all you have to do is download it. There are no modifications necessary for it to function

##### **Directory Text File:**

This should be a text file called "Directory.txt" and should be saved in the same location as the python script. The contents of this file should be the directory that you want the images from reddit saved to. For example, it should be something like "C:\Users\JohnDoe\Documents"

Note that the document should **only** have that text and nothing more. No spaces, no linebreaks, nothing else.

##### **Client Information Text File:**

This should be a text file called "ClientInfo.txt" and should also be saved in the same location as the python script. This should consist of Client ID, Client Secret, Password, Username, and User Agent, in that order on separate lines. If you do not know what these are, it will be explained later.

#### **Subreddit Text File:**

This should be a text file with a name that consists of a keyword relating all the subreddits and the word "Subs" after. For instance, if you wanted to use thus script for gathering cat pictures, you could use "Cat" as your keyword. The subreddit text file should then be names "CatSubs.txt"

The text file should have the names of the subreddits you want the script to gather images from. The text file ***needs to have 5 lines***. If you have less than 5 subreddits, fill the rest of the lines with line breaks. ***DO NOT WRITE ANYTHING ON THESE LINES***.




Once you have all of these files set up, you should be good to go! To run the script just open the command prompt and enter "python RedditDownloadBot.py" (or whatever you have the script saved as).


#### CLIENT INFORMATION EXTENDED

To get the client information necessary to make the script function, you need to create an application on reddit. You can do so here https://ssl.reddit.com/prefs/apps/

After you name it and create it, the Client ID will appear directly under the name. The Client Secret will be labeled "Secret." The username and password are the username and password to the reddit account you made the application on. And lastly, the User Agent is whatever you named it.

#### OPTIONAL FILES

This script defaults to a limit of 100 posts to search through per subreddit and sorts by the timeframe of "week" (for applicable sorting methods such as top and controversial). If you want to change this, you can change the "Modify" variable in the script to True. You will need a text file called "RDB_Config.txt"

The first line of this text file should be the time filter. This can be any of the following: "all", "year", "month", "week", "day", or "hour"

The second line of the text file should be the limit. Note that this controls the number of posts that the script goes through, NOT the number of images it will download. For instance, the limit can be 100 but the script may only download 60 images because only 60 of those posts had images. This can be any number, however reddit itself may limit the amount you can download due to the rate limit.

