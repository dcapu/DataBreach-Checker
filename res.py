#This program is to prevent the use of compromised passwords. The website sells stolen data which is illegal, do not search anyones emails but your own.
# Please check if your data has been compromised!

import requests, json
from colorama import Fore, init


init()


def main():
    email_check = input('enter your email: ')
    api_key = 'DPAU-NDYM-KQRT-GRAF'
    url = f'https://api.weleakinfo.to/api?value={email_check}&type=email&key={api_key}'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

    r = requests.post(url, data=email_check, headers=headers)
    jsonResponse = r.json()


#    print(r.json())            #for debugging

    if "error" in r.json():
        rerun = input('The email {} was not in any databreaches! Would you like to check another email?[Y/N]: '.format(email_check))
        if 'Y' or 'y' in rerun:
            main()

    elif "result" in r.json():
        count = jsonResponse['found']
        print('Your information was leaked: ', Fore.RED,'{} time(s)'.format(count))
        print(jsonResponse['result'])
        print("# Note the line is in user:password format and the sources is the website where your info was stolen from")

    else:
        print('something went wrong, please try again.')


if __name__ == '__main__':

    main()