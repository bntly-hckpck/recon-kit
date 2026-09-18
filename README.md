# recon-kit

Minimal personal cybersecurity toolkit to explore the fundamentals of TCP reconnaissance.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

## Features

- [X] Parallel test servers for local testing
- [X] Single port connectivity check
- [X] Port range scanning
- [X] Banner grabbing from open ports
- [X] JSON report
- [X] main.py
- [X] CLI arguments (argparse)
- [X] Input validation
- [ ] Error handling
- [ ] *TBD*

## Overview

| Module | Purpose |
|--------|---------|
| [`port_scanner.py`](port_scanner.py) | scan TCP port ranges, return list of open ports |
| [`banner_grabber.py`](banner_grabber.py) | connect to open ports and retrieve service banners |
| [`test_servers.py`](test_servers.py) | parallel test servers for validation |
| [`report.py`](report.py) | write results to JSON file |
| [`main.py`](main.py) | manages scanner, grabber, and report |

## How to use

1. **Start test servers** (terminal 1):
   ```bash
   python test_servers.py
   ```

2. **Run reconnaissance** (terminal 2):
   ```bash
   python main.py 127.0.0.1 9990 9999
   ```

3. **Check JSON report**
   ```bash
   cat recon_report.json
   ```
  
#### Report example:
```json
[
    {
        "port": 9999,
        "banner": "[testbanner]"
    },
    {
        "port": 9998,
        "banner": null
    }
]
