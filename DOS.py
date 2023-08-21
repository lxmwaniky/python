import random
import string

def generate_email(name_list, domains):
    email_list = []
    
    for name in name_list:
        random_number = random.randint(100, 999)
        domain = random.choice(domains)
        email = f"{name.lower()}{random_number}@{domain}"
        email_list.append(email)
    
    return email_list

def generate_random_alphanumeric(length):
    alphanumeric_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

def generate_passwords(count, length):
    passwords = []
    
    for _ in range(count):
        password = generate_random_alphanumeric(length)
        passwords.append(password)
    
    return passwords

your_names = ["alice", "bob", "charlie", "dave", "eve", "emma", "liam", "olivia", "noah", "ava", "william", "sophia", "jackson", "isabella", "jacob", "mia", "ethan", "amelia", "oliver", 
    "harper", "lucas", "evelyn", "lily", "aiden", "avery","Lucas", "Nora", "Carter", "Riley", "Gabriel", "Zara", "John", "Hazel", "Matthew", "Stella",
    "Owen", "Natalie", "Jack", "Zoey", "Levi", "Aurora", "Caleb", "Ruby", "Luke", "Lillian",
    "Isaac", "Hailey", "Nathan", "Eleanor", "Samuel", "Skylar", "Jaxon", "Claire", "Muhammad",
    "Paisley", "Christopher", "Ariana", "Andrew", "Arianna", "Thomas", "Liliana", "Joshua", "Sophie",
    "Eli", "Eliana", "Aaron", "Aubrey", "Wyatt", "Bella", "Hunter", "Savannah", "Christian",
    "Camila", "Adrian", "Maya", "Julian", "Naomi", "Ezra", "Layla", "Anthony", "Alexa", "Isaiah", "Valentina", "Charles", "Lucia",
    "Josiah", "Brooklyn", "Hudson", "Violet", "Grayson", "Aria", "Ezekiel", "Scarlett", "Adam", "Zoe",
    "Lincoln", "Eva", "Asher", "Piper", "Xavier", "Anna", "Theodore", "Mila", "Leo", "Leah",
    "Elias", "Samantha", "Gabriel", "Audrey", "Caleb", "Allison", "Daniel", "Aaliyah", "Maxwell", "Genesis",
    "Bryson", "Brielle", "David", "Eleanor", "Joseph", "Sadie", "Cooper", "Skylar", "Miles",
    "Peyton", "Roman", "Madelyn", "Elliott", "Delilah", "Landon", "Aubree", "Nolan", "Hannah", "Jude", "Lily",
    "Nicholas", "Addison", "Evan", "Eliana", "Jordan", "Ellie", "Tyler", "Nora", "Cole", "Lillian",
    "Sawyer", "Zara", "Ezekiel", "Mila", "Cameron", "Maya", "Axel", "Emilia", "Thomas", "Alice",
    "Gavin", "Rebecca", "Dominic", "Isla", "Wyatt", "Naomi", "Elijah", "Elise", "Oscar", "Gianna",
    "Xander", "Julia", "Carson", "Sarah", "Levi", "Elizabeth", "Jason", "Ariana", "Isaac", "Amelia",
    "Mason", "Penelope"]
email_domains = ["gmail.com", "yahoo.com", "outlook.com"]

num_emails = len(your_names) # Generate email addresses for all names
email_list = generate_email(your_names, email_domains)

num_passwords = len(your_names) # Generate passwords for all names
password_length = 10
password_list = generate_passwords(num_passwords, password_length)

for i in range(num_emails):
    print(f"Email: {email_list[i]} | Password: {password_list[i]}")
