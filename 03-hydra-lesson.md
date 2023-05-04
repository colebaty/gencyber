# intro

## review
- [sql lesson](02-sql-lesson.md)

## learning objectives
- learn about authentication
- learn about "brute forcing"
- learn to use `hydra`

## authentication

when we log into a site like facebook or TikTok or whatever, we usually
use some form of _authentication_ - username/password, or your phone number or
your email address, etc.

this is how we prove we are who we say we are.

## brute forcing

imagine you have a 4-digit PIN.  how many possible combinations are there for
the PIN?  how long would it take you to get through all of those combinations?

imagine now you have an 8-"digit" password using just lowercase letters.  how
many choices are there per "digit"?  how many total passwords?

$$ 26^{8} = 208 * 10^{9} $$

humans live for 3 million seconds, on average

you can see that this number grows very large as add more digits (aka longer
passwords) and we add more choices per digits (aka uppercase, lowercase,
numerals, special symbols).

the process of trying every possible combination is called *brute force*.  it
is the most direct way of attempting to discover username/password combinations,
but hopefully you can see that it's not practical.

computers are super fast and can help speed this up, but even a computer has
limits.

$$2.40 GHz = 416 * 10^6 calculations / second$$

$$72^16 = 5.2 * 10^{30}$$

$$1.25 * 10^{22} seconds $$

$5.2 * 10^{30} / 3 * 10^{6} = 1.7 * 10^{24}$ human lifetimes for a computer
to vist each combination!

this is what we call a "computationally infeasible" calculation, because no one
would be around to even see the result!

## credentials are important!

recall that in the previous lesson we used `sqlmap` to dump the table of users
for the DVWA app. what all can we do with those credentials?

1. can we log in to the app as other users?
2. can we log in to the server with some of those creds?

yes to all!  there is a good chance that one of those users has an account on
the machine hosting the app.  we should at least try.

## `hydra`

remember there were only 5 users on the DVWA app, but real applications have
thousands or millions of users.  it's impossible for a single person to test
each username/password combination.

luckily some very smart nerds created a tool to do this automatically, called
`hydra`.  you can give `hydra` a list of users, a list of passwords, and a
target, and it will automatically attempt each combination and report back if
there are any successes.

## hands-on lesson 

follow the instructor to complete these steps:

1. create a file containing the usernames dumped from the previous lesson
2. in the same directory, create a file containing the passwords from the
   previous lesosn
3. open a terminal and navigate to the directory where those files are saved
4. use the following command; pay attention to uppercase/lowercase

```bash
$ hydra -L <username file> -P <password file> ssh://<ip address of target>
```

    * `-L` looks for a file containing a list of usernames
    * `-P` looks for a file containing a list of passwords
    * `ssh://<ip address of target>`: ssh is a program used for remote login.

`hydra` tests each combination of username and password against the target
machine.

## the end
that's the end of this series of lessons.  feel free to explore and play with
some of the tools we've used.
