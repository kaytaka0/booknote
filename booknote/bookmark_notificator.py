from booknote.mail import send_bm_mail
from booknote.bookmark import get_chrome_bookmark

def main():
    content = '\n\n'.join([f'・{bm["name"]}:\n {bm["url"]}'for bm in get_chrome_bookmark()])
    send_bm_mail(content=content)

if __name__=='__main__':
    main()
    