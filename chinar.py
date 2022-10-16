def func():

    import cx_Oracle
    import numpy as np, pandas as pd
    connection = cx_Oracle.connect(user="system", password="6969", dsn="localhost/XE")
    cursor = connection.cursor()

    print("Choose any one of the following\
            \n1. Gender you are looking for:\
            \n2. According to City preference:\
            \n3. According to his/her Education Background:\
            \n4. According to the type of Job Profile He/She should have:\
            \n5. According to Age preference:\
            \n6. According to Height preference:\
            \n7. According to type of skin Complexion you like to see(Fair, Dusky, Brown):\
            \n8. According to that person's annual income:\
            \n9. According to his/her family status:\
            \n10. If you want to give Multiple choices:\
            \n11.To Exit.\
            ")
    val = int(input("Make your choice : "))

    if val == 1:
        cursor = connection.cursor()
        a = input("Enter gender you are looking for(MALE/FEMALE): ")
        sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :b"
        cursor.execute(sql1, b=a)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
        print(df1)
        func()

    if val == 2:
        cursor = connection.cursor()
        a = input("Enter your City Preference: ")
        sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND I.CURRENT_PLACE = :b"
        cursor.execute(sql1, b=a)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
        print(df1)
        func()

    if val == 3:
         cursor = connection.cursor()
         a = input("What should be his/her Education background: ")
         sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND DEGREE = :b"
         cursor.execute(sql1, b=a)
         res = cursor.fetchall()
         df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
         print(df1)
         func()
    if val == 4:
         cursor = connection.cursor()
         a = input("Type of Job Profile He/She should have: ")
         sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND P.JOB_PROFILE = :b"
         cursor.execute(sql1, b=a)
         res = cursor.fetchall()
         df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
         print(df1)
         func()

    if val == 5:
         cursor = connection.cursor()
         print("Give your Age preference: ")
         a = input("what is your starting Age preference: ")
         b = input("what is your last Age preference: ")
         sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND D.AGE >= :xx AND D.AGE <= :yy"
         cursor.execute(sql1, xx=a, yy=b)
         res = cursor.fetchall()
         df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
         print(df1)
         func()

    if val == 6:
         cursor = connection.cursor()
         print("What is your Height preference(in cm): ")
         a = input("what is your starting Height preference: ")
         b = input("what is your last Height preference: ")
         sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND D.HEIGHT >= :cc AND D.HEIGHT <= :dd"
         cursor.execute(sql1, cc=a, dd = b)
         res = cursor.fetchall()
         df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
         print(df1)
         func()

    if val == 7:
         cursor = connection.cursor()
         a = input("Which type of Skin Complexion you like to see(Fair, Dusky, Brown): ")
         sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND D.COLOUR >= :b"
         cursor.execute(sql1, b=a)
         res = cursor.fetchall()
         df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
         print(df1)
         func()

    if val == 8:
         cursor = connection.cursor()
         a = input("His/Her Annual Salary should be greater than or equal to: ")
         sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND P.ANNUAL_INCOME >= :n"
         cursor.execute(sql1, n=a)
         res = cursor.fetchall()
         df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
         print(df1)
         func()

    if val == 9:
         cursor = connection.cursor()
         a = input("What should be his/her Family Status(CLASS):")
         sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND F.FAMILY_STATUS = :m"
         cursor.execute(sql1, m=a)
         res = cursor.fetchall()
         df1 = pd.DataFrame(res, columns=['USERID','NAME','DOB','BIRTH_PLACE','CLP','GENDER','AGE','HEIGHT','MOBILE_NO','COLOUR','MAIL_ID','JOB_PROFILE','DEGREE','ANNUAL_INCOME','FATHER_NAME','FAMILY_NAME','FATHER_OCC','FAMILY_STATUS'])
         print(df1)
         func()

    if val == 10:

        cursor = connection.cursor()
        a = input("Enter gender you are looking for(MALE/FEMALE): ")
        sql1 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :b"
        cursor.execute(sql1, b=a)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID', 'NAME', 'DOB', 'BIRTH_PLACE', 'CLP', 'GENDER', 'AGE', 'HEIGHT',
                                         'MOBILE_NO', 'COLOUR', 'MAIL_ID', 'JOB_PROFILE', 'DEGREE', 'ANNUAL_INCOME',
                                         'FATHER_NAME', 'FAMILY_NAME', 'FATHER_OCC', 'FAMILY_STATUS'])

        print(df1)

        cursor = connection.cursor()
        aa = input("Enter your City Preference: ")
        sql2 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :bb AND I.CURRENT_PLACE = :cc"
        cursor.execute(sql2, bb=a,cc=aa)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID', 'NAME', 'DOB', 'BIRTH_PLACE', 'CLP', 'GENDER', 'AGE', 'HEIGHT',
                                         'MOBILE_NO', 'COLOUR', 'MAIL_ID', 'JOB_PROFILE', 'DEGREE', 'ANNUAL_INCOME',
                                         'FATHER_NAME', 'FAMILY_NAME', 'FATHER_OCC', 'FAMILY_STATUS'])
        print(df1)

        cursor = connection.cursor()
        aaa = input("What should be his/her Education background: ")
        sql3 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :bbb AND I.CURRENT_PLACE = :ccc AND P.DEGREE = :ddd"
        cursor.execute(sql3, bbb=a, ccc=aa, ddd=aaa)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID', 'NAME', 'DOB', 'BIRTH_PLACE', 'CLP', 'GENDER', 'AGE', 'HEIGHT',
                                         'MOBILE_NO', 'COLOUR', 'MAIL_ID', 'JOB_PROFILE', 'DEGREE', 'ANNUAL_INCOME',
                                         'FATHER_NAME', 'FAMILY_NAME', 'FATHER_OCC', 'FAMILY_STATUS'])
        print(df1)

        cursor = connection.cursor()
        aaaa = input("Type of Job Profile He/She should have: ")
        sql4 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :bbbb AND I.CURRENT_PLACE = :cccc AND P.DEGREE = :dddd AND P.JOB_PROFILE = :eeee"
        cursor.execute(sql4, bbbb=a, cccc=aa, dddd=aaa, eeee=aaaa)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID', 'NAME', 'DOB', 'BIRTH_PLACE', 'CLP', 'GENDER', 'AGE', 'HEIGHT',
                                         'MOBILE_NO', 'COLOUR', 'MAIL_ID', 'JOB_PROFILE', 'DEGREE', 'ANNUAL_INCOME',
                                         'FATHER_NAME', 'FAMILY_NAME', 'FATHER_OCC', 'FAMILY_STATUS'])
        print(df1)

        cursor = connection.cursor()
        print("Give your Age preference: ")
        a3 = input("what is your starting Age preference: ")
        b3 = input("what is your last Age preference: ")
        sql5 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :h3 AND I.CURRENT_PLACE = :c3 AND P.DEGREE = :d3 AND P.JOB_PROFILE = :e3 AND D.AGE >= :f3 AND D.AGE <= :g3"
        cursor.execute(sql5, h3=a, c3=aa, d3=aaa, e3=aaaa, f3=a3, g3=b3)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID', 'NAME', 'DOB', 'BIRTH_PLACE', 'CLP', 'GENDER', 'AGE', 'HEIGHT',
                                         'MOBILE_NO', 'COLOUR', 'MAIL_ID', 'JOB_PROFILE', 'DEGREE', 'ANNUAL_INCOME',
                                         'FATHER_NAME', 'FAMILY_NAME', 'FATHER_OCC', 'FAMILY_STATUS'])
        print(df1)


        cursor = connection.cursor()
        print("What is your Height preference: ")
        a1 = input("what is your starting Height preference(in cm): ")
        b1 = input("what is your last Height preference: ")
        sql6 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :h1 AND I.CURRENT_PLACE = :c1 AND P.DEGREE = :d1 AND P.JOB_PROFILE = :e1 AND D.AGE >= :f1 AND D.AGE <= :g1 AND D.HEIGHT >= :i1 AND D.HEIGHT <= :j1"
        cursor.execute(sql6, h1=a, c1=aa, d1=aaa, e1=aaaa, f1=a3, g1=b3, i1=a1, j1=b1)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID', 'NAME', 'DOB', 'BIRTH_PLACE', 'CLP', 'GENDER', 'AGE', 'HEIGHT',
                                         'MOBILE_NO', 'COLOUR', 'MAIL_ID', 'JOB_PROFILE', 'DEGREE', 'ANNUAL_INCOME',
                                         'FATHER_NAME', 'FAMILY_NAME', 'FATHER_OCC', 'FAMILY_STATUS'])
        print(df1)

        cursor = connection.cursor()
        a2 = int(input("What should be that person's annual income(greater than or equal to): "))
        sql7 = " select I.USERID,I.NAME,I.DOB,I.BIRTH_PLACE,I.CURRENT_PLACE,I.GENDER,D.AGE,D.HEIGHT,D.MOBILE_NO,D.COLOUR,P.MAIL_ID,P.JOB_PROFILE,P.DEGREE,P.ANNUAL_INCOME,F.FATHER_NAME,F.FAMILY_NAME,F.FATHER_OCC,F.FAMILY_STATUS from INFO I, DETAILS D, PROFILE P, FAMILY_DETAILS F , BASIC A  where I.USERID = A.USERID AND F.FAMILY_ID = A.FAMILY_ID AND P.MAIL_ID = A.MAIL_ID AND D.MOBILE_NO = A.MOBILE_NO AND GENDER = :h2 AND I.CURRENT_PLACE = :c2 AND P.DEGREE = :d2 AND P.JOB_PROFILE = :e2 AND D.AGE >= :f2 AND D.AGE <= :g2 AND D.HEIGHT >= :i2 AND D.HEIGHT <= :j2 AND P.ANNUAL_INCOME >= :n2"
        cursor.execute(sql7, h2=a, c2=aa, d2=aaa, e2=aaaa, f2=a3, g2=b3, i2=a1, j2=b1, n2=a2)
        res = cursor.fetchall()
        df1 = pd.DataFrame(res, columns=['USERID', 'NAME', 'DOB', 'BIRTH_PLACE', 'CLP', 'GENDER', 'AGE', 'HEIGHT',
                                         'MOBILE_NO', 'COLOUR', 'MAIL_ID', 'JOB_PROFILE', 'DEGREE', 'ANNUAL_INCOME',
                                         'FATHER_NAME', 'FAMILY_NAME', 'FATHER_OCC', 'FAMILY_STATUS'])
        print(df1)
        func()



    if val == 11:
        print("Thank you for using our application")
        exit()


func()




