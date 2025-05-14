# Git Setup:
mkdir dir  
cd dir  
touch file{1..10}.py

git init  

git remote add origin HTTPS_URL/SSH_URL  
git remote -v  #.git/config    
git remote set-url origin HTTPS_URL/SSH_URL  
#Authentication HTTPS(username/password<= credential manager), SSH(public,private key)  

git config --global user.name "name"    
git config --global user.email "email"  
git config --global --list  

git branch   
- Git needs at least one commit to create or manage branches properly. If your repo has no commits yet,trying to use git branch will fail because there's no master (or main) branch to base the new one on.

vi file  
git add file  
git commit -m "commit message"  
git status  

# Regular Use Commands:
git log  
git log --oneline  
git log -2  
git log <filename>  

git show commit-id  
git show --pretty='' --name-only commit-id   
- gives only "file names" on that commit  

git branch  
git branch new_branch_name  
git checkout new_branch_name  

git push origin new_branch_name  
git push origin bn1 bn2  
git push origin --all  
git branch -D branch_name  
git push origin :deleted_branch_name  

# Data Hadling:
Working Area:
-------------
git checkout file_name   
git diff      

Staging Area
------------
git diff --cached  
git restore --staged file_name  #SA --> WA  

Commited
--------
git diff commit_id1..commit_id2  
git revert HEAD    #undo the last commit -->  new commit with history  
git reset --hard commit_id    #no history  

Stash
-----
git stash  
git stash list    #stash@{0}  
git stash apply stash@{1}  
git stash drop stash@{1}  
or
git stash pop stash@{1}      #(it will apply and delete)  


#  Tags for semantic version:
 
Format:
-------
Ex. VS Code version: 1.0.1 
- PATCH <- Bug Fixes	  
- MINOR <- New features and Improvements	  
- MAJOR <- Major changes (Backward Incompatible)	  
Ex: 3.1.4  
3 - Major  
1 - Minor  
4 - Patch  

TAG A COMMIT: Simply another name to a commit: 
----------------------------------------------
git tag tag_name commit  
git show tag  

ANNOTATED TAGS:  
git tag -a tag_Name -m"message" [commit]  
git tag -a v2.1.6 -m "Release for something"  

PUSH TAGS  
git push origin tag tag_name  
git push --tags   #All the tags  
