```                                                                                                                                                                                    
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
(_____|_____|_____|_____|_____|_____|_____|_____|_____|_____)
     (  ____ )\     /\__   __/\     /(  ___  | (    /|       
     | (    )( \   / )  ) (  | )   ( | (   ) |  \  ( |       
     | (____)|\ (_) /   | |  | (___) | |   | |   \ | |       
     |  _____) \   /    | |  |  ___  | |   | | (\ \) |       
     | (        ) (     | |  | (   ) | |   | | | \   |       
     | )        | |     | |  | )   ( | (___) | )  \  |       
     |/  _______\_/_____)_(  |/     \(_______)/    )_)_______
|\     /(  ___  |  ____ ) \    /\   (  ___  )\     /\__   __/
| )   ( | (   ) | (    )|  \  / /   | (   ) | )   ( |  ) (   
| | _ | | |   | | (____)|  (_/ /____| |   | | |   | |  | |   
| |( )| | |   | |     __)   _ (_____) |   | | |   | |  | |   
| || || | |   | | (\ (  |  ( \ \    | |   | | |   | |  | |   
| () () | (___) | ) \ \_|  /  \ \   | (___) | (___) |  | |   
(_______|_______)/ __\__/_/___ \/___(_______|_______)_ )_(__ 
(_____|_____|_____|_____|_____|_____|_____|_____|_____|_____)
```                                                             
Spandex is not required to participate in these exercises.
                                        (or is it?)
***
***
***
### General Environment Setup
(including steps for those new to github)
This is all optional. It's moreso for the sake of records-keeping on my end..
.....
  __  _    _   _      __ _    
 / /\| |\ \ \_| \    / /\ \_/ 
/_/--\_| \||_| \_\/\/_/--\_|  
.....

Use a terminal to install the following:
XCode-
Developer tools for MACOS.                                                             
```
xcode-select --install
```
***
Brew-
Homebrew is a package manager for MACOS. 
The password prompt is for your current MAC user account. 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
***
VS Code-
Text editor. 
```
brew install visual-studio-code
```
run the following command to make it the editor for git-related operations:
```
git config --global core.editor 'code -w'
```
***
[MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
***
MySQL command line client. 
```
brew install mysql-client
brew link --force mysql-client
```
***
Generate a public-private key pair:
```
ssh-keygen -b 4096 -t rsa -f ~/.ssh/id_rsa -C 'YOUR_NAME@EMAIL'
```
Add public key to github
```
# copies public key to the clipboard
cat ~/.ssh/id_rsa.pub | pbcopy
```
Add the key to your [github account](https://github.com/settings/keys) and click "Add SSH Key".
Then paste into large "Key" text box. 
***
***
### Establishing a Python Environment
##### Anaconda
Python has a very large ecosystem w/ many different libraries. Anaconda is a distribution of Python; "batteries included" package for data science. Automatically gives most needed modules for data science work. 

```
# Run these commands from your terminal. It does not matter what directory you are in.
# install anaconda (this might take a few minutes)
brew install --cask anaconda

# add anaconda's tools to your PATH (this tells your shell how to find all of the anaconda programs)
# Run this command if you are using a Mac w/ an Intel processor
echo 'export PATH=/usr/local/anaconda3/bin:$PATH' >> ~/.zshrc

# Run this command if you are using a Mac w/ an M1 processor
echo 'export PATH=/opt/homebrew/anaconda3/bin:$PATH' >> ~/.zshrc

# reload your configuration
source ~/.zshrc
```
