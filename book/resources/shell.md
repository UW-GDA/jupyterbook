# Shell Notes
UW Geospatial Data Analysis
CEE498/CEWA599
David Shean

## Background 
See [01_Shell_Github_prep](../modules/01_Shell_Github/01_Shell_Github_prep.html#reading-and-tutorials-complete-before-first-friday-lab)

Also, https://www.youtube.com/watch?v=VF9-sEbqDvU

Nice cheat sheet: https://devhints.io/bash

## Random tips
A collection of common items

### Batch file renaming
Say you have 1000s of tif files, and you want to replace spaces with underscores:

```
for i in *tif
do 
mv “$i” $(echo $i | sed ‘s/ /_/g’)
done

#One line
for i in *tif; do mv “$i” $(echo "$i" | sed ‘s/ /_/g’); done
```

You can also replace any shared string (e.g., 'initial' to 'final') in the filenames by modifying the `sed` command:
```
sed 's/oldstr/newstr/'
```

For example, to change the extension on all .txt files to .csv:
```
for i in *.txt; do mv “$i” $(echo "$i" | sed ‘s/\.txt$/\.csv$/’); done
```

### Permanently store `ll` alias 
```
echo "alias ll='ls -FGlAhp'" >> ~/.bash_profile
source ~/.bash_profile

#One line
echo "alias ll='ls -FGlAhp'" >> ~/.bash_profile && source ~/.bash_profile
```

Read a bit about `.bash_profile` to understand what's going on here

### Finding files
```
find . -name '*.txt'
```
