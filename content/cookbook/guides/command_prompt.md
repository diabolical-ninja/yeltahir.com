---
title: "Command Prompt"
draft: false
toc:
  auto: false
---

# Command Prompt Tips & Tricks

## Findstr
### Search for string 
```BATCH
findstr "string" *.*
```

### Filter on file types
```BATCH
findstr "string" *.file_type
```

### Filter on file name
```BATCH
findstr "string" *<filename>*.*
```
Add the following flags to modify search conditions:
* /s = recursive search    
* /i = not case sensitive    
* /m = return only file name    


    

## Find files
### List Files & directories
```BATCH
dir
```

### Filter on name
```BATCH
dir *<file/directory name>*
```


### Filter on types
```BATCH
dir *.file_type
```
Add `/s` to recursively list results


## Count Files in folder
```BATCH
dir *.* /w
```


## Start H2O via CMD
```BATCH
cd C:\h2o-3.8.3.2
java -Xmx4g -jar h2o.jar  # Start with 4GB ram
java -Xmx16g -jar h2o.jar -nthreads -1 # Start with 16Gb ram & all threads
java -Xmx4g -jar h2o.jar -port 55555 -ip 000.000.000.000  # Start on port 55555 with IP 000.000.000.000
```


## Outlook not opening
```BATCH
taskkill /F /IM UCMAPI.exe
```

## Jupyter

### Start Notebook
```BATCH
jupyter notebook  # This will startup & run locally in whichever folder you start from
jupyter notebook --no-browser  # Prevents from automatically opening a browser windows
jupyter notebook --ip=* --no-browser # Enables notebook to be accessible over a local network
```


### Host Jupyter Slides
```BATCH
jupyter nbconvert "<...>.ipynb" --to slides --post serve
```