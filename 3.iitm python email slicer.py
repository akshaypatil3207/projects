# written by akshay patil
#Get user email address
email=input("What is your email address? :- ").strip()

#silce out username
username=email[:email.index("@")]



#slice out domain name
domain_name=email[email.index("@")+1:]


#format message
output="your username is {} and your domain name is {}".format(username,domain_name)


#display output mesage
print(output)
