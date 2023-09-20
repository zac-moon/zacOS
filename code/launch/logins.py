def main(username,password):
    try:
        with open(f'hd/system/login/{username}') as file:
            cpass = file.read()
            if password == cpass:
                return 'pass-correct'
            else:
                return 'pass-incorrect'
    except FileNotFoundError:
        return 'user-notfound'
    except Exception as e:
        return e
