import description_tables as descr_tab
import B4_12main as ma

def request_user_data(session, tn_user=descr_tab.User):


    def birthdate():
        """
            ожидает дату в формате YYYY-MM-DD. После трех неудачьных попыток возращает 1999-12-31.
        """

        for i in range(2, -1, -1):
            error_text = "Дата рождения введена неравельно, повторите ввод. Осталось попыток {iter}".format(
                iter=i)

            str_birthdate = input(
                "Введите дату рождения в формате YYYY-MM-DD(1999-12-31): ").strip()
            birthdate_splits = str_birthdate.split("-")

            checking_length = len(birthdate_splits) != 3 or len(birthdate_splits[0]) != 4 or len(
                birthdate_splits[1]) != 2 or len(birthdate_splits[2]) != 2

            if checking_length:
                if i == 0:
                    continue
                print(error_text)
                continue

            checking_not_int = not (birthdate_splits[0].isdigit(
            ) and birthdate_splits[1].isdigit() and birthdate_splits[2].isdigit())

            checking_value_error = int(birthdate_splits[0]) < 0 or (int(birthdate_splits[1]) < 0 or int(
                birthdate_splits[1]) > 12) or (int(birthdate_splits[2]) < 0 or int(birthdate_splits[2]) > 31)

            if checking_not_int or checking_value_error:
                if i == 0:
                    continue
                print(error_text)
                continue
            else:
                return str_birthdate

        else:
            print("Вы исчерпали количество порыток. Дата дня рождения будет установлена по умолчанию 1999-12-31")
            return "1999-12-31"


    def gender():
        """
            ожидает пол в формате Male или Female. После трех неудачьных попыток возращает None.
        """
        for i in range(2, -1, -1):
            error_text = "Пол введен неравельно, повторите ввод. Осталось попыток {iter}".format(
                iter=i)

            gender_str = input(
                "Введите пол формате Male или Female: ").strip().capitalize()

            if gender_str != "Male" and gender_str != "Female":
                if i == 0:
                    continue
                print(error_text)
                continue
            else:
                return gender_str

        else:
            print("Вы исчерпали количество порыток. Пол будет установлена по умолчанию None")
            return "None"


    def height():
        """
            ожидает рост в формате #.##(1.70). После трех неудачьных попыток возращает 0.00 .
        """
        for i in range(2, -1, -1):
            error_text = "Рост введен неравельно, повторите ввод. Осталось попыток {iter}".format(
                iter=i)

            gender_str = input("Введите ваш рост в формате #.##: ").strip()

            gender_splits = gender_str.split(".")

            if len(gender_splits) != 2 or len(gender_splits[0]) != 1 or len(gender_splits[1]) != 2:
                if i == 0:
                    continue
                print(error_text)
                continue

            if not(gender_splits[0].isdigit() and gender_splits[1].isdigit()):
                if i == 0:
                    continue
                print(error_text)
                continue
            else:
                return gender_str

        else:
            print("Вы исчерпали количество порыток. Рост будет установлена по умолчанию 0.00")
            return "0.00"

    user = descr_tab.User(
        first_name=input("Введите имя: "),
        last_name=input("Введите фамилию: "),
        gender=gender(),
        email=input("Введите почту: "),
        birthdate=birthdate(),
        height=height()
        )

    session.add(user)
    session.commit()
    print("Данные сохранены")
