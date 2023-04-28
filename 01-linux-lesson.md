# intro

## learning objectives
- learn about linux commands
    - command structure
    - options/flags
    - common commands
        - cd
        - ls
        - cat
- hands-on practice

## what is linux?
- its an operating system
- what's an operating system?
    - phones: iOS, android
    - computers: windows, macOS, UNIX, Linux

Windows and macOS (previously OS X) are the two most popular operating 
systems in use today.  Linux is another type of operating system that 
runs on computers. there are even types of operating systems that allow 
you to run multiple operating systems simultaneously on the same machine.

What are some terms we may have associated with Linux?
- open-source
- Unix
- hackers
- Ubuntu/red hat/kali
- others?

## key differences between linux and windows/macos
*Proprietary vs. open source*.
- proprietary: "intellectual property". a company owns the rights to develop,
  distribute, sell, do all the capitalism with a product
- open source: the source code is freely available. anyone can examine it,
  modify it, republish it (within limits)

*GUI-based vs. terminal-based*
- Graphical User Interface (GUI): point and click
- Terminal, aka command line: 1337 sup3r h4xx0r

Windows, macOS, and Linux each have GUI and command-line capabilities. But
Windows and macOS are typically operated with the GUI, while Linux is typically
associated with the command line/terminal

# the language of the command line
Linux commands have a general structure:

```
$ <command> <options/flags> <file>
```
### Check on learning:

```bash
$ cat -n README.md
```

`cat` is a useful command for printing the contents of a file to to the
terminal.  the word `cat` is short for _con*cat*enation_, which is computer
talk for putting two things together.  in this case, we're concatenating the
contents of the file README.md to the output in the terminal.

the `-n` flag means to print the output with line numbers.  

```bash
$ cat -n README.md                                                                   *[main]
     1  # README
     2
     3  ## Basic git workflow
     4
     5  ```bash
     6  git pull    # beginning of session
     7
     8  # editing
     9  # 1) make some changes
    10  # 2) commit the changes
    11
    12  vim <somefile>  # or nano or notepad++ or whatever
    13  git status      # shows list of files changed since last commit
    14  git add <file or files pertaining to this change>
    15  git commit -m "<commit message>"
    16
    17  # repeat this process as needed
    18
    19  git push    # end of session
    20  ```
```


## hands-on practice 1
another common command is `ls`, or `ls`, or "_**l**_i_**s**_t directory contents"

Take ~5 minutes to try the following different ways of invoking the `ls`
commands: 

```bash
$ ls
$ ls -a
$ ls -l
$ ls -a -l
$ ls -al
$ ls -A
$ ls --help
```

## questions
1. How do the different options change the output of this command?
2. Why isn't there a file included as part of the command?  Why does this still
   work?
3. What do the different options/flags mean?  How do you find out?
4. Why is there no file used with this command?  what information is printed if
   you give it a file name?

>**NOTE**:  Notice how the the lines in the code snippets above begin with a dollar sign.
>This is a *convention*, and denotes that the the commands are to be run in a
>non-privileged terminal/shell.  For this lesson, all you have to do is type
>only what follows after the dollar sign.

```bash
# what's written
$ ls -Al

# what you type
ls -Al <enter>
```

## hands-on practice 2
use the `--help` flag to explore the commands listed below.  what does each
do?

1. `mkdir`
2. `ifconfig`
3. `touch`
4. `cat`
