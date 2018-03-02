from pan_scrape.rekognize import identify

answers = {'readable_captchas/readable_captcha_21.jpeg': '737HV', 'readable_captchas/readable_captcha_28.jpeg': '3N5YR', 'readable_captchas/readable_captcha_16.jpeg': '4NYDP', 'readable_captchas/readable_captcha_4.jpeg': 'WHDFL', 'readable_captchas/readable_captcha_11.jpeg': '4KXRK', 'readable_captchas/readable_captcha_14.jpeg': 'JLKIF', 'readable_captchas/readable_captcha_24.jpeg': 'HUQP7', 'readable_captchas/readable_captcha_0.jpeg': 'N4GXD', 'readable_captchas/readable_captcha_2.jpeg': '7XB75', 'readable_captchas/readable_captcha_3.jpeg': 'KD5QG', 'readable_captchas/readable_captcha_9.jpeg': 'NTSQQ', 'readable_captchas/readable_captcha_15.jpeg': '5SLCT', 'readable_captchas/readable_captcha_27.jpeg': 'DEHJY', 'readable_captchas/readable_captcha_6.jpeg': '4L7MD', 'readable_captchas/readable_captcha_18.png': 'JSETL', 'readable_captchas/readable_captcha_20.jpeg': 'MD7WX', 'readable_captchas/readable_captcha_19.jpeg': '5EGEH', 'readable_captchas/readable_captcha_29.jpeg': '6SQEY', 'readable_captchas/readable_captcha_30.png': '7BBC6', 'readable_captchas/readable_captcha_10.jpeg': 'V77EB', 'readable_captchas/readable_captcha_1.jpeg': 'LGB3L', 'readable_captchas/readable_captcha_25.jpeg': 'TMSCT', 'readable_captchas/readable_captcha_12.jpeg': 'CJ5Q6', 'readable_captchas/readable_captcha_23.jpeg': 'MPBQU', 'readable_captchas/readable_captcha_17.jpeg': 'JYJHK', 'readable_captchas/readable_captcha_5.jpeg': 'VXY45', 'readable_captchas/readable_captcha_18.jpeg': 'DFB54', 'readable_captchas/readable_captcha_26.jpeg': 'EP6NN', 'readable_captchas/readable_captcha_22.jpeg': '63ETY', 'readable_captchas/readable_captcha_7.jpeg': 'VFR7C', 'readable_captchas/readable_captcha_13.jpeg': 'VXWSJ', 'readable_captchas/readable_captcha_8.jpeg': 'Y4RTR'}
if __name__=='__main__':
    f = open("answers.csv", "w")
    f.write("File,Answer,Correct,Diff\n")
    count = 0
    for filename in answers:
        ans = identify(filename)
        diff = ""
        if ans == answers[filename]:
            count+=1
        else:
            for i in range(0, len(answers[filename])):
                if i>=len(ans):
                    diff += "broken"
                    break
                if answers[filename][i]!=ans[i]:
                    diff+=str(i)
        f.write(filename+ "," +ans + "," + answers[filename] + "," + diff+"\n")
    f.close()
    print((count/float(len(answers)))*100)

