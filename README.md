# Python Port Scanner Tool

**Description:**  
A fast and flexible Python port scanner that supports predefined port presets, custom port ranges, adjustable scan speeds, and verbose output to identify open and closed TCP ports with common service names.

---

## Overview

This is a simple but effective port scanning tool written in Python. It allows scanning of TCP ports on a target IP address or domain with customizable port ranges or well-known port presets. It supports three scanning speeds and can show verbose output indicating open and closed ports.

---

## Features

- Scan target IP or domain over a range of ports.
- Use predefined port presets like `top10`, `top20`, `web`, `database`, and more.
- Set scan speed mode: Fast, Normal, or Full (adjusts socket timeout).
- Verbose mode to print both open and closed ports.
- Resolves common service names for well-known ports.

---

## Installation

Make sure you have Python 3 installed. This script uses only standard libraries (`argparse` and `socket`), so no extra packages are needed.

---

## Usage

```bash
python port_scanner.py -target <IP_or_domain> [options]
```

## Fodase
| Argument  | Description                           | Default         |
| :-------- | :---------------------------------- | :-------------- |
| `-target` | Target IP address or domain name to scan | **Required**    |
| `-start`  | Starting port number for scanning    | `1`             |
| `-end`    | Ending port number for scanning      | `5000`          |
| `-mode`   | Scan speed mode: Fast, Normal, Full  | `normal`        |
| `-preset` | Port preset list to scan              | `default`       |
| `-v`      | Enable verbose output (show open and closed ports) | `False` (flag) |

## Presets

Port Presets

You can scan specific well-known port groups using -preset:

- top10: Top 10 commonly used ports.
- top20: Top 20 ports.
- top100: Top 100 ports from nmap's list.
- web: Common web-related ports (80, 443, 8080, etc).
- remote: Remote access ports (SSH, Telnet, RDP, VNC).
- database: Popular database ports (MySQL, PostgreSQL, Oracle, MS SQL).
- file: Ports related to file sharing (FTP, NetBIOS, SMB).
- default: Uses the custom port range from -start to -end.

## Examples

```bash
python portscanner.py -target 192.168.1.1

python portscanner.py -target example.com -preset top10 -v

python portscanner.py -target 10.0.0.5 -start 100 -end 200 -mode fast

python portscanner.py -target 192.168.0.10 -preset web -mode full

```


## Authors

- [@LonfLonf](https://github.com/LonfLonf)

