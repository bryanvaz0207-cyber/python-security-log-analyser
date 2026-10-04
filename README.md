# Security Log Analyser

This is a small Python project I made to practise reading files and working with data.

It reads a fictional login log file and counts how many logins were successful and how many failed.

It also counts failed logins by IP address. If an IP address has three or more failed logins, the program reports it as suspicious.

The main file is `log_analyser.py`.

The login data is in `login_events.txt`.

There is also a simple test in `test_log_analyser.py`.

To run it:

```bash
python log_analyser.py
```

To run the test:

```bash
pytest
```

A normal line in the log file looks like this:

```text
2026-09-01 09:10 alice SUCCESS 192.168.1.10
```

The program reads the login result and IP address from each line.

The data is fictional.

The suspicious-IP rule is simple: three or more failed logins.

This is a beginner project, not a full cybersecurity monitoring system.
