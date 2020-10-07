---
title: "R"
draft: false
toc: true
---


# Handy Tricks for R

## Progress Bars

Adding a progress bar to a loop is easy enough without any extra libraries required.
```R
loop_length <- 10
pb <- txtProgressBar(min = 0, max = loop_length, style = 3)
for(i in 1:loop_length){
	
	print i
	
	# Update progress bar
	setTxtProgressBar(pb, i)

}

close(pb)
```

Progress bars can also be added to apply functions with the help of a lovely packaged called [pbapply](https://jekyllrb.com/). First lets get the package:
```R
install.packages('pbapply')
```

Then it's just a simple case of loading it and changing your regular `apply` call to `pbapply`:
```R
library('pbapply')
pblapply(1:10, function(x) x+1)
```

## Common Libraries

Handy libraries for all types on situations.

```R
install.packages(c('data.table',
                 'foreach',
                 'RODBC',
                 'ggplot2',
                 'h2o',
                 'doSNOW',
                 'parallel',
                 'gridExtra',
                 'readr'))
```



## R Kernel for Jupyter

One of the niftiest features of Jupyter is its ability to run multiple kernels. The below libraries will install the R kernel.

```R
install.packages(c('repr',
                   'IRdisplay',
                   'evaluate',
                   'crayon',
                   'pbdZMQ',
                   'devtools',
                   'uuid',
                   'digest'))
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()
```