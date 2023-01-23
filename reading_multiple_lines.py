with open('emails.txt', 'r') as emails:
    emails = emails.readlines()

    for email in emails:
        print(email.rstrip())