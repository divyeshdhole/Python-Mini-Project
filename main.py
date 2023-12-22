import random
import pandas as pd
import datetime as dt
import smtplib


curr = dt.datetime.now()
print(F'Today : {curr.day}/{curr.month}/{curr.year}')
today = (curr.day, curr.month)

friends_data = pd.read_csv("C:/Users/LENOVO/Desktop/Bday Wisher/birthdays.csv")
# dob = (bday_month , bday_day )
dobs = {
    (data_row.day, data_row.month): data_row
    for (index, data_row) in friends_data.iterrows()
}

def Send_Email(recipient,msg):
    email = "tejyamaharaj@gmail.com"
    password = "rhdyexfrfbntkbvf"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email, to_addrs=recipient, msg=f"Subject:Happy Birthday\n\n{msg}"
            )
    print(f"sent to {recipient}")


if today in dobs :
    info = dobs[today]
    letter = f'C:/Users/LENOVO/Desktop/Bday Wisher/letter_1.txt'
    with open(letter, 'r') as f:
        body = f.read()
        msg = body.replace('[NAME]',info['name'])
    Send_Email(info.email,msg)

    