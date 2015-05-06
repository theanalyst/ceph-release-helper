# ceph-release-helper

Basic script to make release notes between revisions, 
after cloning the repo (preferably in a virtualenv),
do something like 


```sh 
pip install -r requirements.txt
python setup.py install
```

Now invoke this as

```sh
GITHUB_ACCESS_TOKEN='something' # Generate a gh access token and put it as a var
ceph-release-notes -r tags/v0.87..giant /path/to/ceph/repo 
```
