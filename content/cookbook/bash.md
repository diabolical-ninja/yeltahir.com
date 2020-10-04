---
title: "Bash"
draft: false
---

# File Sizes {#file-sizes}
Size of all files in a directory
```bash
du -h
```

Size of current directory
```bash
du -h -s
```

Size of top-level directories within current directory
```bash
du -h -d 1
```


# Find files {#find-files}
## List Files & directories
```bash
ls
```

Add the following flags to modify search conditions:
* -R = recursive list    
* -a = list all
* -s = show file size
* -l = show with details


## Filter on name
```bash
ls | grep "<file/directory name>"
```



# Find String   {#find-string}
## All files containing a string
```bash
grep "<search string">
```
Add the following flags to modify search conditions:
* -r = recursive list  
* -w = only match whole words
* \| = use in search string as an OR

  
## For a specific directory or file
```bash
grep "<search string>" my/directory/
grep "<search string>" my/directory/myfile.txt
```


# Assign Environment Variables  {#assign-env-vars}

If you've got a list of environment variables in a `.env` file, this will assign them all to your existing environment:
```bash
export $(grep -v '^#' .env | xargs)
```