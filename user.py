import datetime


class User:
    def __init__(self, userid, status, food, food_last, alco, alco_last, pillow, pillow_last, general,
                 general_last, general_today, last_edit, period_end, transport, transport_last):
        self.userid = userid
        self.status = status
        self.food = food
        self.food_last = food_last
        self.alco = alco
        self.alco_last = alco_last
        self.pillow = pillow
        self.pillow_last = pillow_last
        self.general = general
        self.general_last = general_last
        self.general_today = general_today
        self.last_edit = last_edit
        self.period_end = period_end
        self.transport = transport
        self.transport_last = transport_last
