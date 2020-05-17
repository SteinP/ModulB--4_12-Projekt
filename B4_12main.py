# * sqlite3 sochi_athletes.sqlite3
# * .schema
# * SELECT COUNT() FROM athelete WHERE gender = 'Female';
# * SELECT COUNT() FROM athelete WHERE age > 30;
# * SELECT COUNT() FROM athelete WHERE gender = 'Male' and age > 25 and gold_medals>=2;
# * SELECT *  FROM user;
import description_tables as descr_tab
import users
import find_athlete

def main():
    session = descr_tab.connect_db()
    #print(height())

    #user_name = find_athlete.find(session, input_id_user=443, tn_user=Athelete)

    mode = input(
        "Выбери режим.\n1 - ввести нового пользователя\n2 - найти ближайших по дате рождения и росту\n")
    if mode == "1":
        users.request_user_data(session=session)

    elif mode == "2":
        input_id_user = int(input("Введите идентификатор пользователя (челое число): "))
        find_athlete.find(session=session, input_id_user=input_id_user)
    else:
        print("Некорректный режим")


if __name__ == "__main__":
    main()
