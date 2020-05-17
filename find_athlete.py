import description_tables as descr_tab
import B4_12main as ma
import datetime


def delta_min(index, date):
    "Нахождение минемального значения из двух соседних от date[index]"
    if (date[index+1]-date[index]) < (date[index]-date[index-1]):
        return date[index+1]
    else:
        return date[index-1]


def find(session, input_id_user=0, tn_user=descr_tab.User, tn_athelete=descr_tab.Athelete):
    """
    session - соединение к базе данных
    input_id_user - номерк id пользователя. По умолчанию значение равно 0.
    tn_user - таблица из которои бурутся данные пользователя. По умолчанию имя таблицы user
    tn_athelete - таблица из которои бурутся данные атлетов. По умолчанию имя таблицы athelete

    если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю; если пользователя с таким идентификатором нет, вывести соответствующее сообщение.
    """

    def convert_to_datetime(date): return datetime.datetime.strptime(
        date, "%Y-%m-%d").date()  # конвертирование strdate в date

    def convert_to_str(date): return str(date).strip("','()")

    def filter_None(date): return date != "None"
    #очистка строковую переменною (времени) от артифактов

    query_user = session.query(tn_user).filter(
        tn_user.id == input_id_user).first()
    #запрос данных пользовотеля по id из табдицы с именем tn_user

    if query_user is None:
        print("Пользователя с таким id нет в базе")
        return None

    birthdate_user = convert_to_datetime(query_user.birthdate)
    height_user = (query_user.height)
    birthdate_athelete_to_str = map(
        convert_to_str, session.query(tn_athelete.birthdate).all())
    athelete_birthdate = list(
        set(map(convert_to_datetime, birthdate_athelete_to_str)))
    athelete_birthdate.sort()
    #запрос birthdate из таблицы с именем tn_athelet. Очистка их от артифактов и преобразование к типу DATE, с последующей сортиповкой.
    index = athelete_birthdate.index(birthdate_user)
    athel_date_delta_min = str(delta_min(index, athelete_birthdate))
    #нахождение birthdate атлета ближайшего по дате рождения к заданному пользователю
    athelete_birthdate = session.query(tn_athelete).filter(
        tn_athelete.birthdate == athel_date_delta_min).first()
    #запрос данных атлета по birthdate из табдицы с именем tn_athelet
    ###---------------------------------------------------
    height_athelete = list(set(map(float, filter(filter_None, map(
        convert_to_str, session.query(tn_athelete.height).all())))))
    height_athelete.sort()
    #запрос height из таблицы с именем tn_athelet. Очистка их от артифактов и преобразование к типу float, с последующей сортиповкой.
    index = height_athelete.index(height_user)
    athel_height_min = delta_min(index, height_athelete)
    #нахождение height атлета ближайшего по height к заданному пользователю

    athelete_height = session.query(tn_athelete).filter(
        tn_athelete.height == athel_height_min).first()
    #запрос данных атлета по height из табдицы с именем tn_athelet

    print("Дата рождения пользователя с заданным id {check_id} - {check_birthdate}. Ближе всего к нему пользователь с id - {birthdate_id} {birthdate_name}. Его дата рождения: {birthdate}.".format(
        check_id=input_id_user, check_birthdate=birthdate_user, birthdate_id=athelete_birthdate.id, birthdate_name=athelete_birthdate.name, birthdate=athelete_birthdate.birthdate))

    print("Рост пользователя с заданным id {check_id} - {check_height} см. Ближе всего к нему пользователь с id - {height_id} {height_name} с ростом {height} см.".format(
        check_id=input_id_user, check_height=height_user, height_id=athelete_height.id, height_name=athelete_height.name, height=athelete_height.height))
