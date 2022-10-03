What differs this repository from random App Store applications?

* FOLLOWING AND FOLLOWERS ARE SAVED IN CHRONOLOGICAL ORDER
(Unlike on Instagram - which shows the users in a scrambled order, this program shows all of them in a descending order from newest to oldest)
(The last account the target user followed, will show first in the log file. Same applies for followers - latest followers are the first in the list)
* You don't provide a stranger with your main Instagram account credentials
* You can scan OTHER users' following and followers lists and see who doesn't follow THEM back
* You don't risk your main account getting restricted because you can use a throwaway account for targetting public profiles 
* No advertisements, free to use


How to use?

1. Use the 'login.py' to connect to an Instagram account and save its' session for later uses.
(You only need to use 'login.py' once, from then on, you can just load the session without reconnecting)
2. Inside 'doesntFollowBack.py', fill in the required variables (username = target account) (session = login.py username)
3. Run the program. Results are saved into data/doesntFollowBack.txt
* Following & Followers are logged into {username}_following/followers.txt files in ./data/
