import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "vahaan.official@gmail.com"
#you = "arun.dakua@gmail.com"


def email_register(user_name,email):
    global me
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Thank You for Registering with Vahaan"
    msg['From'] = me
    msg['To'] = email

    # Create the body of the message (a plain-text and an HTML version).
    #text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi! """+ str(user_name) + """ <br>
           Kindly Book your Bike.<br>
           For Any Queries Call us on 09892777091 or mail us on vahaan.official@gmail.com.

           Regards,
           Vahaan
        </p>
      </body>
    </html> 
    """  + str(user_name)

    # Record the MIME types of both parts - text/plain and text/html.
    #part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    #msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('vahaan.official', 'new@123456')
    
    mail.sendmail(me, email, msg.as_string())
    
    mail.quit()


def email_transaction(user_name,email,start_date,end_date,tariff_value,vehicle_no):
    global me
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Thank You for Booking Bike with Vahaan"
    msg['From'] = me
    msg['To'] = email

    # Create the body of the message (a plain-text and an HTML version).
    #text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi! """+ str(user_name) + """ <br>
            You have booked a Honda Activa from """+ str(start_date) + """ to """ + str(end_date) + """.<br>
            The tariff calculated is """ + str(tariff_value) + """.<br>
            The vehicle number is """ + str(vehicle_no)+ """.<br>
            Pick Up Point : Yash Westeria,Behind Sayaji Hotel,Wakad,Pune - 411057.<br>
            Original Document to be Submitted while pick up Pan Card/Driving License/Aadhar Card.<br>
            Deposit Refund on return : 500.<br>
            Kindly enjoy your ride.<br>

            Regards,<br>
            Vahaan<br>

            Points to remember:</br>
            1.On not submission of orginal documents ,will lead to cancellation of booking.<br>
            2.On Cancellation of booking ,50% of booking fee will be taken as compensation.<br>
            3.Call us at 09892777091 for further details.</br>
        </p>
      </body>
    </html> 
    """  

    # Record the MIME types of both parts - text/plain and text/html.
    #part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    #msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('vahaan.official', 'new@123456')
    mail.sendmail(me, email, msg.as_string())
    mail.quit()


def email_query(firstname,lastname,email,phone,message):
    global me

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Query from Customer"
    msg['From'] = me
    msg['To'] = me
    
    
    html = """\
    <html>
      <head></head>
      <body>
        <p>First Name """+ str(firstname) + """ <br>
           LastName """ + str(lastname) + """ <br>
           message """ + str(message)+ """ <br> 
        </p>
      </body>
    </html> 
    """  


    part2 = MIMEText(html, 'html')


    msg.attach(part2)

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('vahaan.official', 'new@123456')
    
    mail.sendmail(me, email, msg.as_string())
    
    mail.quit()
