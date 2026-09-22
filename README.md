Reflected XSS Flask Lab

A small educational Flask application designed to demonstrate Reflected Cross-Site Scripting (XSS) in a controlled local environment.

The lab compares a deliberately vulnerable implementation with a secure implementation using HTML escaping. It allows learners to understand how user-controlled input can become part of an HTML response and how proper output encoding prevents the browser from interpreting the input as executable HTML/JavaScript.

Educational project — for local laboratory use only.

1. Project Overview

This project demonstrates a classic Reflected XSS scenario using a Flask web application.

The application receives a user-controlled q parameter through a GET request:

/search?q=USER_INPUT

The input is then displayed in the generated HTML page.

The lab provides two implementations:

Vulnerable: user input is inserted into HTML without proper escaping.
Secure: user input is escaped before being inserted into the HTML response.

This makes it possible to visually compare the behavior of unsafe and properly handled input.

2. Learning Objectives

After completing this lab, the learner should be able to:

Understand what Reflected XSS is.
Identify user-controlled input in a web application.
Understand how GET parameters reach the server.
Understand how server-side HTML generation works.
Observe how a browser interprets injected HTML/JavaScript.
Understand the difference between vulnerable and secure output handling.
Understand the role of HTML escaping.
Recognize why untrusted input should not be directly inserted into HTML.
3. Request Flow

The vulnerable scenario follows this basic flow:

User
  │
  │ GET /search?q=INPUT
  ▼
Flask Application
  │
  │ Read q parameter
  ▼
Server-side HTML generation
  │
  │ User input inserted without escaping
  ▼
HTTP Response
  │
  ▼
Browser
  │
  │ HTML is interpreted
  ▼
Potential XSS execution

The secure implementation changes the flow by escaping the user-controlled value before inserting it into the HTML response.

4. Project Structure
reflected-xss-flask-lab/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── base.html
    ├── index.html
    ├── search.html
    └── lab.html
Main files
File	Description
app.py	Flask application, routes and lab logic
requirements.txt	Python dependencies
base.html	Common page layout
index.html	Lab homepage
search.html	XSS demonstration and comparison
lab.html	Visual explanation of the attack flow
style.css	Application styling
5. Requirements
Python 3.9+
Flask
A modern web browser
Windows, Linux or macOS

The project is designed to run locally.

6. Installation

Clone or copy the project:

cd C:\TP\reflected-xss-flask-lab

Create a virtual environment:

python -m venv venv

Activate it:

venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt
7. Run the Lab

Start the Flask application:

python app.py

Then open:

http://127.0.0.1:5000/
8. Available Pages
Homepage
/

Provides an introduction to the laboratory.

Search / XSS Lab
/search?q=...

Contains:

User input
Vulnerable implementation
Secure implementation
Generated HTML comparison
"Try it yourself" section
Explanation of what happened
Mitigation guidance
Lab Explanation
/lab

Provides a visual explanation of:

User Input
     ↓
q Parameter
     ↓
Flask Server
     ↓
HTML Response
     ↓
Browser
9. Test Inputs

The following examples can be used inside the local laboratory.

Normal text
Bonjour tout le monde

Expected behavior:

The browser displays the text normally.
HTML input
<b>Texte en gras</b>

This demonstrates the difference between displaying input as text and allowing the browser to interpret it as HTML.

Local JavaScript test
<script>alert('XSS Lab local')</script>

In the vulnerable implementation, the browser can interpret the injected script.

In the secure implementation, the input is escaped and treated as text.

10. Vulnerable Implementation

The vulnerable concept can be represented as:

f"<p>Resultats pour : {q}</p>"

The value of q is inserted directly into the generated HTML.

If the value contains HTML or JavaScript, the browser may interpret it as part of the page rather than ordinary text.

11. Secure Implementation

The secure concept uses HTML escaping:

f"<p>Resultats pour : {escape(q)}</p>"

Special HTML characters such as:

<
>
"
'
&

are converted into safe HTML entities before being inserted into the page.

The browser therefore displays the input as text instead of interpreting it as HTML markup.

12. Vulnerable vs Secure
Aspect	Vulnerable	Secure
User input	Trusted directly	Treated as untrusted
HTML escaping	Not applied	Applied
<script> input	Can be interpreted	Displayed as text
Risk	Reflected XSS	Reduced XSS risk
Main protection	None	Output encoding
13. Security Concept
Reflected XSS

Reflected Cross-Site Scripting occurs when attacker-controlled input is immediately reflected by a web application in its HTTP response without appropriate output encoding.

The browser receives the response and may interpret the injected content as HTML or JavaScript.

The important security principle demonstrated by this lab is:

Never trust user-controlled input.

Input received through parameters such as:

?q=

should be treated as untrusted data.

14. Mitigation

The main mitigation demonstrated by this laboratory is context-appropriate output encoding.

For HTML content, special characters should be escaped before inserting untrusted data into the HTML document.

Additional protections commonly used in real applications include:

Context-aware output encoding
Safe templating practices
Avoiding unsafe HTML rendering
Content Security Policy (CSP)
Input validation where appropriate
Secure application design
15. Security Scope

This project is intentionally limited to a local educational environment.

It does not contain:

Real user accounts
Real credentials
Real personal information
Production data
External targets
External attack infrastructure

The examples are designed to run on the learner's own machine.

16. Safety

Do not deploy this intentionally vulnerable application to a public server or expose it to the Internet.

Run the laboratory locally:

127.0.0.1

The vulnerable functionality exists intentionally for educational purposes.

17. Recommended Learning Workflow

Use the following workflow when studying the lab:

1. Understand
      ↓
2. Run the application
      ↓
3. Test normal input
      ↓
4. Test HTML input
      ↓
5. Observe vulnerable behavior
      ↓
6. Compare secure behavior
      ↓
7. Analyze the source code
      ↓
8. Identify the security weakness
      ↓
9. Apply the mitigation
      ↓
10. Test again
18. Lab Goal

The goal of this project is not simply to execute an XSS payload.

The main objective is to understand the complete chain:

User Input
     ↓
HTTP Request
     ↓
Server-side Processing
     ↓
HTML Generation
     ↓
HTTP Response
     ↓
Browser Interpretation
     ↓
Security Impact

Understanding this flow makes it easier to identify and prevent similar vulnerabilities in real web applications.

19. Technologies
Python
Flask
HTML
CSS
Jinja2 / MarkupSafe
HTTP
Web Browser
20. Project Type
Educational Cybersecurity Laboratory

Focus:

Web Application Security
        │
        └── Cross-Site Scripting
                │
                └── Reflected XSS
21. Disclaimer

This project is created strictly for cybersecurity education, experimentation, and local laboratory practice.

Use it only in environments where you have explicit authorization.

Do not use the techniques demonstrated by this laboratory against systems, applications, or users without permission.

22. Author

Cybersecurity learning project by Bilal.

Part of a practical cybersecurity laboratory focused on understanding web application vulnerabilities through controlled exercises.