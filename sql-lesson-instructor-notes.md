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
