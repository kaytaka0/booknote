from booknote.mail import send_bm_mail
from booknote.bookmark import get_chrome_bookmark

def main():
    bms = get_chrome_bookmark()
    if len(bms):
        return
    content = '\n\n'.join([f'・{bm["name"]}:\n {bm["url"]}'for bm in bms])
    send_bm_mail(content=content)

if __name__=='__main__':
    main()
    