
mkdir <dir>
cd <dir>
touch file{1..10}.py

git init

git remote add origin <HTTPS>/<SSH>
git remote -v #.git/config
git remote set-url origin <HTTPS>/<SSH>
#Authentication HTTPS(username/password<= credential manager), SSH(public,private key)

git config --global user.name "<name>"
git config --global user.email "<email>"
git config --global --list

git branch 
#Git needs at least one commit to create or manage branches properly. If your repo has no commits yet,trying to use git branch will fail because there's no master (or main) branch to base the new one on.

vi <file>
git add <file>
git commit -m <commit message>
git status

git log
git log --oneline
git log -2
git log <filename>

git show <commit-id>
git show --pretty='' --name-only <commit-id> #gives only <file names> on that commit

git branch
git branch <new branch name>
git checkout <new branch name>

git push origin <new branch name>
git push origin <bn1> <bn2>
git push origin --all
git branch -D <branch name>
git push origin :<deleted branch name>

#Working Area:
git checkout <filename> #Rollback to last commit changes
git diff  #what changes from current commit

#Staging Area
git diff --cached
git restore --staged <filename>  #SA --> WA

#commited
git diff commit_id1..commit_id2
git revert HEAD  #undo the last commit -->new commit with history
git reset --hard <commit_id>  #no history

#Tags for semantic version:
---------------------------
Ex. VS Code version: 1.0.1
Format:
	PATCH <- Bug Fixes
	MINOR <- New features and Improvements
	MAJOR <- Major changes (Backward Incompatible)
3.1.4
3 - Major
1 - Minor
4 - Patch

TAG A COMMIT: Simply another name to a commit.
-------------
git tag <tagname> commit
git show tag

ANNOTATED TAGS:
git tag -a <tagName> -m"message" [commit]
git tag -a v2.1.6 -m"Release for something"

PUSH TAGS
git push origin tag <tagname>
git push --tags #All the tags
