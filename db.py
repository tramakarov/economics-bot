import psycopg2 as pg
from user import User
from status import Status
import datetime
from credentials import DB_HOST, DB_NAME, DB_PORT, DB_PASSWORD, DB_USERNAME


def get_user(userid):
    with pg.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USERNAME,
                    password=DB_PASSWORD) as connect:
        with connect.cursor() as cursor:
            cursor.execute('select * from "economics-bot" where id=\'{}\''.format(userid))
            result = [raw for raw in cursor]

    try:
        userid, status, food, food_last, alco, alco_last, pillow, pillow_last, general, general_last, general_today, last_edit, period_end, transport, transport_last = result[0]
        user = User(userid, status, food, food_last, alco, alco_last, pillow, pillow_last, general, general_last, general_today, last_edit, period_end, transport, transport_last)
    except IndexError:
        user = User(userid, Status.HELLO.value, 0, 0, 0, 0, 0, 0, 0, 0, 0, get_date(), None, 0, 0)
        add_user(user)
    return user


def add_user(user):
    query = ("insert into \"economics-bot\"(id, status, food, food_last, alco, alco_last, pillow, pillow_last, " +
             "general, general_last, general_today, last_edit, transport, transport_last) values(" +
             "{id}, '{status}', {food}, {food_last}, {alco}, {alco_last}, {pillow}, {pillow_last}, {general}, " +
             "{general_last}, {general_today}, '{last_edit}', {transport}, {transport_last})").format(
        id=user.userid, status=user.status, food=user.food, food_last=user.food_last, alco=user.alco,
        alco_last=user.alco_last, pillow=user.pillow, pillow_last=user.pillow_last, general=user.general,
        general_last=user.general_last, general_today=user.general_today, last_edit=get_date(),
        transport=user.transport, transport_last=user.transport_last)

    with pg.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USERNAME,
                    password=DB_PASSWORD) as connect:
        with connect.cursor() as cursor:
            cursor.execute(query)


def update_user(user):
    query = ("update \"economics-bot\" set status='{status}', food={food}, food_last={food_last}, alco={alco}, " +
             "alco_last={alco_last}, pillow={pillow}, pillow_last={pillow_last}, general={general}, " +
             "general_last={general_last}, general_today={general_today}, last_edit='{last_edit}',  " +
             "transport={transport}, transport_last={transport_last} where id={id}").format(
        id=user.userid, status=user.status, food=user.food, food_last=user.food_last, alco=user.alco,
        alco_last=user.alco_last, pillow=user.pillow, pillow_last=user.pillow_last, general=user.general,
        general_last=user.general_last, general_today=user.general_today, last_edit=get_date(),
        transport=user.transport, transport_last=user.transport_last)

    with pg.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USERNAME,
                    password=DB_PASSWORD) as connect:
        with connect.cursor() as cursor:
            cursor.execute(query)

    if user.period_end is not None:
        update_user_period(user)


def update_user_period(user):
    query = ("update \"economics-bot\" set period_end='{period_end}' where id={id}").format(
        period_end=parse_date(user.period_end), id=user.userid)

    with pg.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USERNAME,
                    password=DB_PASSWORD) as connect:
        with connect.cursor() as cursor:
            cursor.execute(query)


def get_date():
    return str(datetime.datetime.now()).split(' ')[0].replace('-', '')


def parse_date(date):
    if date is not None:
        return str(date).split(' ')[0].replace('-', '')
