# Python Challenge 2 - not my bank

```
I wanted to call my repo "python-challenge-2" but the assignment wanted "customer_banking"
git remote add origin https://github.com/yourusername/customer_banking.git
then 
git push -u origin main 

I did this my way.
edit .git/config
change the name that defaults to the directory name
[remote "origin"]
	url = https://github.com/ehxewri/customer_banking.git
	fetch = +refs/heads/*:refs/remotes/origin/*

Then use this to create the remote repo and push. 

curl -X POST \
  -H "Authorization: token "the repo key" \
  -H "Content-Type: application/json" \
  -d '{"name": "reponame", "description": "Case study for Cisco IBN", "private": false}' \
  https://api.github.com/user/repos
# git remote add origin https://github.com/ehxewri/"repo-Name"
# git push -u origin main
