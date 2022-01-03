# honey-robber
Password List creator (robber) using honeypots 

### Idea
the idea is to run a honeyPot server and let other try to attack to it.
then we analyze the log and saving passwords or user:password which attackers tried.
so we can create a great (I say best) password list. 

### Usage

#### 1. Run your favorite HoneyPot server and write the log to a file
````bash
    docker run -p 2222:2222 cowrie/cowrie > log.hp
````
#### 2. In ``main.py`` import your HoneyPot and call ``parse_log`` 
````python
from cowrie.cowrie import Cowrie

c = Cowrie(log_file_path="./log.hp", password_list_file_path="./passwords.txt", pair_list_file_path="./pair.txt")
c.parse_log()
````
#### 3. Wait... 
Wait to attack and download(save) your password and pair file :)

## Contribute
Feel free and know this repo to yourself.

###### Enjoy :)