# https://hyunmin1906.tistory.com/276
import encodings
import smtplib, ssl
import random
import string


# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)


def send_email(to):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "service.center.12342@gmail.com"
    password = "pkbtcfowxykxclcz"
    receiver_email = to

    message = "<h1>"
    letters_set = string.ascii_letters
    random_list = random.sample(letters_set, 10)
    code = "".join(random_list)
    message += f"비밀번호 변경 코드입니다.{code}<h1>"


    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode("utf-8"))
    return code

