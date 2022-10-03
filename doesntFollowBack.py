import instaloader

il = instaloader.Instaloader()

##########  VARIABLES TO DEFINE  ##########
username = "lironbiam"  # Check who doesn't follow this user back
il.load_session_from_file("username_of_saved_session")  # Username we used in 'login.py'.
# [!] if target is private, you have to follow it with the account from 'login.py'.
##########    endof VARIABLES    ##########

profile = instaloader.Profile.from_username(il.context, username)

# Get the list of who the user is following
file = open(f"data\\{username}_following.txt", "w")
follow_list = []
count = 0
print(f"Retrieving list of who {username} is following..")
for followers in profile.get_followees():
    follow_list.append(followers.username)
    file.write(follow_list[count])
    file.write("\n")
    # print(follow_list[count])  # uncomment to print each name to console
    count = count + 1
file.close()
print(f"> {username} is following {count} accounts. List saved to data/following_{username}.txt")

# Get the list of who is following the user
file = open(f"data\\{username}_followers.txt", "w")
follow_list = []
count = 0
print(f"Retrieving list of {username}'s followers..")
for followers in profile.get_followers():
    follow_list.append(followers.username)
    file.write(follow_list[count])
    file.write("\n")
    # print(follow_list[count])  # uncomment to print each name to console
    count = count + 1
file.close()
print(f"> {username} is followed by {count} accounts. List saved to data/followers_{username}.txt")


# Function that checks the differences between the files
def checkDifferences(ers, ing, diff):
    count = 0
    for line in ing:
        if line.strip() not in ers:
            unfollowers.write(line)
            count += 1
    file_name = diff.name.split('\\')[-1]  # skipping the 'data\\' prefix for the filename for nicer output
    print(f"\n> {count} accounts don't follow {username} back. List saved to data/{file_name}.")
    ing.close()
    diff.close()


# Provide the checkDifferences() function with arguments of the file paths for comparison
followers = set((line.strip()
                 for line in open(f'data\\{username}_followers.txt', 'r+')))
following = open(f'data\\{username}_following.txt', 'r+')
unfollowers = open('data\\doesntFollowBack.txt', 'w')
checkDifferences(followers, following, unfollowers)
