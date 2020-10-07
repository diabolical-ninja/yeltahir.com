---
title: "Git"
draft: false
toc:
  auto: false
---

# Handy Tricks for Git

## Global Ignore Settings

This is primarily to avoid accidential upload of keys/config/etc to a git host, ie github.

``` bash
git config --global core.excludesfile

vim <path/to/file>/.gitignore_global
```

Then populate it with the below plus anything that you might want:
```sh
# Config Files
conf.yml
conf.yaml
conf.eyaml

config.yml
config.yaml
config.eyaml

# Keys
key.txt
keys.txt

# Environments Files
.env
```


## Status & Changes

View current changes
``` bash
git status
```

Undo changes on a particular file, aka rollback to previous commit.
```bash
git checkout -- <path/to/file.ext>
```

Blow away all current changes
```bash
git reset --hard
```

## Branches
See local branchs
```bash
git branch
```

List all branchs
```bash
git branch -a
```

Switch branch
```bash
git checkout <branchname>
```

Create a new branch, switch to it & push it to remote
```sh
git checkout -b <branchname>
git push -u origin <branchname>
```

## Deleting A Commit
In the instance a commit is must be deleted, as opposed to reverting, etc.
```sh
git reset --hard HEAD^

# To remove last N commits
git reset --hard HEAD~2

# Push changes to remote. This will overwrite remote!!
git push origin -f
```

