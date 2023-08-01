import itertools
import os

def generate_permutations(first_name, middle_name, last_name, birth_year):
    permutations = []

    # Common permutations
    permutations.extend([
        f"{first_name}{last_name}",
        f"{first_name}.{last_name}",
        f"{first_name}-{last_name}",
        f"{first_name}_{last_name}",
        f"{last_name}{first_name}",
        f"{last_name}.{first_name}",
        f"{last_name}-{first_name}",
        f"{last_name}_{first_name}"
    ])

    if birth_year:
        permutations.extend([
            f"{first_name}{birth_year}",
            f"{first_name}.{birth_year}",
            f"{first_name}-{birth_year}",
            f"{first_name}_{birth_year}",
            f"{last_name}{birth_year}",
            f"{last_name}.{birth_year}",
            f"{last_name}-{birth_year}",
            f"{last_name}_{birth_year}",
            f"{first_name[0]}{last_name}{birth_year}",
            f"{first_name[0]}{last_name}"
        ])

    if middle_name:
        permutations.extend([
            f"{first_name}{middle_name}",
            f"{first_name}.{middle_name}",
            f"{first_name}-{middle_name}",
            f"{first_name}_{middle_name}",
            f"{first_name}{middle_name}{last_name}",
            f"{first_name}.{middle_name}.{last_name}",
            f"{first_name}-{middle_name}-{last_name}",
            f"{first_name}_{middle_name}_{last_name}",
            f"{middle_name}{first_name}",
            f"{middle_name}-{first_name}",
            f"{middle_name}_{first_name}",
            f"{middle_name}{last_name}",
            f"{middle_name}.{last_name}",
            f"{middle_name}-{last_name}",
            f"{middle_name}_{last_name}",
            f"{first_name}{middle_name[0]}{last_name}",
            f"{first_name[0]}{middle_name[0]}{last_name}",
        ])

    return permutations

def generate_emails(usernames, domains):
    emails = [f"{username}@{domain}" for username, domain in itertools.product(usernames, domains)]
    return emails

def print_intro():
    intro = """
   _   _    _    __  __ _____ ____  
  | \\ | |  / \\  |  \\/  | ____|  _ \\ 
  |  \\| | / _ \\ | |\\/| |  _| | |_) |
  | |\\  |/ ___ \\| |  | | |___|  _ < 
  |_| \\_/_/   \\_\\_|  |_|_____|_| \\_\\
                                   
  This script will generate a list of possible usernames and email addresses based on common permutations. 
  This tool is designed to be paired with username enumeration tools.
    """
    print(intro)

def main():
    print_intro()

    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name (optional, press Enter to skip): ")
    last_name = input("Enter last name: ")
    birth_year = input("Enter birth year (optional, press Enter to skip): ")

    # Generate permutations
    permutations = generate_permutations(first_name, middle_name, last_name, birth_year)

    # Print results to files
    usernames_output_filename = "possible_usernames.txt"
    emails_output_filename = "possible_emails.txt"
    count = 1
    while os.path.exists(usernames_output_filename) or os.path.exists(emails_output_filename):
        usernames_output_filename = f"possible_usernames_{count}.txt"
        emails_output_filename = f"possible_emails_{count}.txt"
        count += 1

    with open(usernames_output_filename, "w") as usernames_file, open(emails_output_filename, "w") as emails_file:
        usernames_file.write("Common Permutations:\n")
        emails_file.write("Possible Emails:\n")

        for username in permutations:
            usernames_file.write(username + "\n")

        common_domains = [
            "gmail.com",
            "outlook.com",
            "yahoo.com",
            "hotmail.com"
            "aol.com",
            "icloud.com",
            "yandex.com",
            "protonmail.com"
        ]
        emails = generate_emails(permutations, common_domains)
        for email in emails:
            emails_file.write(email + "\n")

    print(f"Results saved to '{usernames_output_filename}' and '{emails_output_filename}'")
    
if __name__ == "__main__":
    main()
