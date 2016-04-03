# Front-end server encoding tests

See this test here:
[http://www.ncbi.nlm.nih.gov/staff/maloneyc/test-encodings/index.html](http://www.ncbi.nlm.nih.gov/staff/maloneyc/test-encodings/index.html).

The index.html file here tests how UTF-8 characters are interpreted, in various
permutations of the environment.

Each javascript file in the test just writes a string directly into the HTML
document. All of these *should* work. Here's the results I get:

![encoding problems](https://stash.ncbi.nlm.nih.gov/users/maloneyc/repos/test-encodings/browse/results.png?at=dbda17e71ab2f11a68704bece48b2a80d4e7a59e&raw)

There are two factors that cause it to break, and one that doesn't:

## 1. Server running without locale

Apache doesn't have any of the locale environment variables set (see 
[here](http://www.ncbi.nlm.nih.gov/staff/maloneyc/test-encodings/echo-locale.cgi)).
That causes it to read most files as ASCII. The only way to fix it is to use a 
byte order mark (BOM) in the file, which is not reliable, since any number of
build processes can strip that off.

This causes problems when CGI scripts are run, that have unicode characters in
them.

## 2. Responses don't have `charset`

Apache doesn't set `charset` on the `Content-type` header. So, when a file 
is sent that doesn't have BOM, the client interprets it as ASCII.

Here's one without a BOM:

```
$ curl -s -D - -o /dev/null \
  http://www.ncbi.nlm.nih.gov/staff/maloneyc/test-encodings/static.js
HTTP/1.1 200 OK
...
Content-Length: 70
Content-Type: text/javascript
```

And one with:

```
$ curl -s -D - -o /dev/null \
  http://www.ncbi.nlm.nih.gov/staff/maloneyc/test-encodings/static-bom.js
HTTP/1.1 200 OK
...
Content-Length: 73
Content-Type: text/javascript
```

You can see that the content-length differs by three bytes -- that's the BOM.
So for those files, because the client gets the BOM, it can interpret the file
correctly, too.

## 3. No effect: "application/javascript" vs "text/javascript"

For completeness, I'm including this. I thought it might make a difference,
when there is no `charset`, whether the content-type is "application/javascript" 
(which is used by /core) or "text/javascript" (used by futurama). It doen't


