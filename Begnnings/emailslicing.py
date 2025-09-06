Email = input("Enter the email:")#Maya23@gmail.com 
Index = Email.index("@")

username = Email[:Index] #returns as output Maya23

domain = Email[Index+1:] #retuns as output  gmail.com 

print(f"Your username is {username} and domain is {domain}")