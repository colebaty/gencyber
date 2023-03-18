# notes for instructor
## DVWA setup
recommended to configure DVWA not to require login. this will make things easier when we
run sqlmap. otherwise, you will need to capture a valid PHP user session
cookie, which is more than we need to be getting into for this lab.

## `sqlmap` demonstration
1. set up a listener on your host listening on port 8080 `nc -lvnp 8080`
2. on the DVWA app, navigate to the SQL injection page
3. set your browser's proxy to your localhost, e.g. `localhost:8080`.
   recommended to use 
   [FoxyProxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/) with Firefox
4. with the proxy enabled in the browser, and the proxy listener enabled in the
   terminal, submit a query with any information into the web app
5. check your terminal - the listener should have intercepted the request
6. your students will need the information contained in the `Host` and `Cookie`
   headers

## hands-on practice 3 - using `sqlmap` to dump database contents

### exercise
1. if needed, reconnect to the lab wifi and navigate back to the SQL injection
   page.
2. in a terminal, enter the command shown below.  substitute the information
   from the demonstration in the appropriate places of the command. the
   `--batch` flag makes it so the program doesn't prompt you for certain
   choices; we're using the defaults for each of these
```bash
sqlmap -u "<url of injectible page>" --cookie="<cookie info>" -D <database> --dump --batch
```

### questions
1. does `sqlmap` show us more information from this table than we dumped
   manually in HO2?
2. does `sqlmap` reveal more information about each user than we were able to
   dump manually in HO2? if so what else is included?
3. how can this information be used?
4. what's up with the passwords?
