import sys
import smtplib
import logging
from logging import getLogger, StreamHandler, ERROR as LOGERROR
from email.mime.text import MIMEText
from email.utils import formatdate


from booknote.bookmark import get_chrome_bookmark
from booknote import config


logger = getLogger(__name__)
handler = StreamHandler(sys.stderr)
logger.addHandler(handler)
logger.setLevel(LOGERROR)


def send_bm_mail(content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = 'Today\'s bookmarks!'
    msg['From'] = config.FROM_ADDR
    msg['To'] = config.TO_ADDR
    msg['Date'] = formatdate()

    logger.error(msg)
    with smtplib.SMTP(host=config.SERVER_NAME, port=int(config.PORT)) as smtp:
        smtp.starttls()
        smtp.login(config.USERNAME, config.PASSWORD) 
        smtp.send_message(msg)
        smtp.quit()


if __name__ == '__main__':
    logger.info('Send bookmark mail')
    send_bm_mail()
    