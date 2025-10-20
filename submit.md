## Submission
## Security Report

### What I Sent
I accessed the application through:
http://127.0.0.1:8000/

Then I submitted a request (via the form or the address bar) using the following query string:

?name=<script>alert(1)</script>

The complete request URL was:
http://127.0.0.1:8000/vulnerable_echo?name=<script>alert(1)</script>

### What Happened in the Browser
After the request was processed, the page rendered the injected script. As a result, the browser displayed a pop-up alert box with the number `1`.

### Why the Server Was Vulnerable
The server directly embedded unvalidated user input into the HTML response without escaping or encoding it.
For example:

<h1>Hello, <script>alert(1)</script>!</h1>

Because the raw `<script>` tag appeared in the HTML, the browser executed it as JavaScript.

Additionally:
- No Content-Security-Policy header was set to block inline scripts, allowing the injected code to run freely.
- This is a textbook **reflected XSS** vulnerability where attacker-controlled input is reflected back in the response and executed in the browser.

### Impact
An attacker could execute arbitrary JavaScript in the site’s context for any user who visits the crafted URL. This could lead to:
- Theft of session cookies
- Unauthorized actions on behalf of the user
- Phishing or deceptive interface overlays

### How to Fix / Mitigate
- Properly escape or encode user-supplied data before inserting it into HTML (e.g., `markupsafe.escape(name)` or a templating engine that auto-escapes).
- Implement a strong Content Security Policy (CSP) to block inline JavaScript. Example:

Content-Security-Policy: default-src 'self'; script-src 'self'

## Pytest
![pytest](https://github.com/anwitabandaru-gif/anything/actions/workflows/pytest.yml/badge.svg)

![Console Output](pytest.png)
