import asyncpraw
import urllib
import os
import asyncio
modify = False
counter = 1
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#Gets the directory information from the Directory text file
directoryPure = open("Directory.txt", "r")
directory = directoryPure.read()

async def InitializeClient():
    """
    Gets an instance of the Reddit Class
    
    Inputs:
        None
        
    Outputs:
        None
    """    
    #Gets the client information from the ClientInfo text file
    ClientInfo = open("ClientInfo.txt", "r")
    ClientInfoList = ClientInfo.read().split("\n")
    ClientInfo.close()
    
    #Connects the code to reddit using the information
    reddit = asyncpraw.Reddit(client_id = ClientInfoList[0],
    client_secret = ClientInfoList[1],
    password = ClientInfoList[2],
    username = ClientInfoList[3],
    user_agent = ClientInfoList[4])
    return reddit

async def GenGet(Keyword, SubName, Sort):
    """
    Gets images and gifs from the subreddit and saves them to a folder
    
    Inputs:
        Keyword: [STRING] Word used to relate all subreddits in a group
        SubName: [STRING] Name of a subreddit
        Sort: [STRING] The sorting method used for the subreddit 
        
    Outputs:
        None
    """
    
    if SubName == "": 
        return None
    
    else:
        
        global counter
        global modify
        
        if modify == True:
            Modifications = open("RDB_Config.txt", "r")
            ModificationsList = Modifications.read().split("\n")
            TimeFilter = ModificationsList[0]
            ImageLimit = int(ModificationsList[1])
        
        else:
            TimeFilter = "week"
            ImageLimit = 100

        #Checks if the file it will save the images and gifs to exists
        #Makes the file if it doesn't exist
        if os.path.exists(f"{directory}/{Keyword}s") == False:
            os.mkdir(f"{directory}/{Keyword}s")
        reddit = await InitializeClient()
        #Iterates through the subreddits in the subreddit list, checking top 500 posts of the week
        #Then checks if the post has a jpg, png, or gif and, if it does, saves it
        subreddit = await reddit.subreddit(SubName)
        if Sort == "Top":
            SubmissionList = subreddit.top(time_filter=TimeFilter, limit=ImageLimit)
        elif Sort == "Hot":
            SubmissionList = subreddit.hot(limit=ImageLimit)
        elif Sort == "Rising":
            SubmissionList = subreddit.rising(limit=ImageLimit)
        elif Sort == "Controversial":
            SubmissionList = subreddit.controversial(time_filter=TimeFilter, limit=ImageLimit)
        elif Sort == "New":
            SubmissionList = subreddit.new(limit=ImageLimit)
        async for submission in SubmissionList:
            url = str(submission.url)
            if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
                urllib.request.urlretrieve(url, f"{Keyword}{counter}[JPG].jpg")
                os.rename(f"{directory}/{Keyword}{counter}[JPG].jpg", f"{directory}/{Keyword}s/{Keyword}{counter}[JPG].jpg")
                print(f"Post #{counter} got from {SubName}!")
                counter += 1
            elif url.endswith("gif"):
                urllib.request.urlretrieve(url, f"{Keyword}{counter}[GIF].gif")
                os.rename(f"{directory}/{Keyword}{counter}[GIF].gif", f"{directory}/{Keyword}s/{Keyword}{counter}[GIF].gif")
                print(f"Post #{counter} got from {SubName}!")
                counter += 1
    await asyncpraw.Reddit.close(reddit)
                
async def GenReset(Keyword):
    """
    Resets the folder related to Keyword, deleting all files in it
    
    Inputs:
        Keyword: [STRING] Word used to relate all subreddits in a group
        
    Outputs:
        None
    """
    DirList = os.listdir(f"{directory}/{Keyword}s")
    for a in DirList:
        os.remove(f"{directory}/{Keyword}s/{a}")

#Takes user input to run the related functions so user doesn't have to run the functions manually        
async def main():
    """
    Gets user input to determine what function to use, what folder to save images to,
    what subreddits to search, and what sorting method to use
    
    Inputs:
        None
        
    Outputs:
        None
    """
    print("What would you like to do?\n1. Get images\n2. Reset images")
    Choice = input(">>> ")
    while Choice != "1" and Choice != "2":
        print("Please enter either 1 or 2")
        Choice = input(">>> ")
    Keyword = input("Enter keyword: ")
    if Choice == "1":
        Sort = input("Enter sorting method\n1. Top\n2. Hot\n3. Rising\n4. Controversial\n5. New\n\n>>> ")
        while Sort != "1" and Choice != "2" and Choice != "3" and Choice != "4" and Choice != "5":
            print("Please enter 1, 2, 3, 4, or 5")
            Sort = input(">>> ")
        #Opens the Sub text file related to the keyword and generates a list from its contents
        Subs = open(f"{Keyword}Subs.txt", "r")
        SubList = Subs.read().split("\n")
        Subs.close()
        if Sort == "1":
            SortWord = "Top"
        elif Sort == "2":
            SortWord = "Hot"
        elif Sort == "3":
            SortWord = "Rising"
        elif Sort == "4":
            SortWord = "Controversial"
        elif Sort == "5":
            SortWord = "New"
        await asyncio.gather(GenGet(Keyword, SubList[0], SortWord), GenGet(Keyword, SubList[1], SortWord), GenGet(Keyword, SubList[2], SortWord), GenGet(Keyword, SubList[3], SortWord), GenGet(Keyword, SubList[4], SortWord))
    elif Choice == "2":
        await GenReset(Keyword)

if (__name__ == "__main__"):
    asyncio.run(main())
        