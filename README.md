![logo](https://i.imgur.com/UxNRyV6.png)
# Online MCIT Discord channel bots

This is an open-source project and all MCIT students are encouraged to contribute to developing useful and playful bots for the server.
Currently, we have two bots:

**Welcome bot** - greats new members and directs them to the rules section. Also notifies Admins when someone leaves the server

![welcome-bot](https://i.imgur.com/Q6i2UIk.png)

**Kanye West** - Our special guest. Who loves to share his thoughts and tell jokes. He also provides basic information about the Online MCIT program. Our goal is to expend him to be more interactive and answer frequently asked questions regarding the program.

![kanyeWest](https://i.imgur.com/oDSr83i.png)

If you want to contribute to the project:

1. Open the New Issue with a description of what functionality you plan to add to the bot:
![new-issue](https://i.imgur.com/KEmcDxY.png)

2. Fork the project

![fork](https://i.imgur.com/ZGGFHpE.png)

3. Using a terminal, clone the repo to your local git by typing:
```
git clone https://github.com/bexxmodd/OnlineMCIT.git
```
_P.S. Automatically new repo will be named as OnlineMCIT and will be copied where your present working directory is. If you want it to be cloned somewhere else type the path after the GitHub link._

4. Go into the cloned project's directory:
```
cd OnlineMCIT
```

5. Set up the remote  repository, which will allow you to fetch the changes and updates introduced to the project:
```
git remote add upstream https://github.com/bexxmodd/OnlineMCIT.git
```

6. Create a branch which you will use to create the functionality you described in the `New Issue`
```
git checkout -b <branch-name>
```
_P.S._ `checkout -b` _allows us to create a branch and switch to it._

Similarly you can use:
```
git branch <branch-name>
git checkout <branch-name>
```

7. After you are done with the functionality, add and commit changes
```
git add <file-name>
git commit -m "type what you have done"
git push origin <branch-name>
```
8. In your repository on *GitHub*, you'll see the `Compare & pull request` button. Click on it and then click submit.

9. Go to the Issues again and close the issue you opened in the beginning with the note what was pushed on the project

![final](https://i.imgur.com/kNxB8LB.png)
