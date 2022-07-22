import pandas
import datetime
import smtplib

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()

now = datetime.datetime.now()
month = now.month
day = now.day

my_email = "yours@mail.com"
password = "yourpassword"

for number in range(len(data_dict["month"])):
    if month == data_dict["month"][number] and day == data_dict["day"][number]:
        with open("letter.txt", 'r') as letter:
            new_letter = ""
            for lines in letter.readlines():
                new_letter += lines.replace("[name]", data_dict["name"][number])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=data_dict["email"][number],
                                msg=f'Subject:Feliz cumpleanos\n\n{new_letter}')


