### Difference b/w Command Line Arguments & Environment Variables:
When we want to pass sensitive info such as passwords, tokens or API key, we'll use Environment variables (or anything that we feel that the user should not type on the terminal)
<br/>
We already have a lot of environment variables but if we want to create a custom env variable, we can use 
```bash
  export password="Vivek@123"
```
This will create an env variable password with the  specified value.
To read environment variables in our program first we'll import a module
```bash
  import os
```
Now to get the vaule of env variable that we stored:
```bash
  os.getenv("password")
```

Note: Let say we're using CI/CD, so we cannot provide the password directly, so instead we'' use env variable. We'll keep the env variable inside a file let say file1.py, so while doing CICD, we'll 
use that pro and then call the function:
```bash
  python file1.py
  password = os.getenv("password")           # here we stored it in a variable password
```
