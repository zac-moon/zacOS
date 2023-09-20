import logins

def lch():
    print('launching')

def main():
    usern = input('Enter Username: ')
    if usern[:3] == 'dev':
        print('dev mode')
        dev = True
        usern = usern[3:]
    else:
        dev = False

    passw = input('Enter Password: ')
    status = logins.main(usern, passw)

    if status == 'pass-correct':
        print('Correct Details - Logged In')
        lch()
    elif status == 'pass-incorrect':
        print('Incorrect Password - Unable to Login')
    elif status == 'user-notfound':
        print('Incorrect Username - Unable to Login')
    else:
        print('An Error Occurred Logging In - We\'re not sure what?')
        if dev:
            print(status)

