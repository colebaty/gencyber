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

For example, a very common linux command is `ls`, or "**l**i**s**t directory contents"

## hands-on practice 1
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
