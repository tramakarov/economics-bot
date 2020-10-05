from enum import Enum


class Status(Enum):
    HELLO = 'HELLO'
    START_SETUP = 'START_SETUP'
    GET_BALANCE_FOOD = 'GET_BALANCE_FOOD'
    GET_BALANCE_ALCO = 'GET_BALANCE_ALCO'
    GET_BALANCE_TRANSPORT = 'GET_BALANCE_TRANSPORT'
    GET_BALANCE_GENERAL = 'GET_BALANCE_GENERAL'
    GET_BALANCE_FINPILLOW = 'GET_BALANCE_FINPILLOW'
    GET_SUM_FOOD = 'GET_SUM_FOOD'
    GET_SUM_ALCO = 'GET_SUM_ALCO'
    GET_SUM_TRANSPORT = 'GET_SUM_TRANSPORT'
    GET_SUM_GENERAL = 'GET_SUM_GENERAL'
    GET_SUM_FINPILLOW = 'GET_SUM_FINPILLOW'
    GET_PERIOD = 'GET_PERIOD'
    MAIN_MENU = 'MAIN_MENU'

    @staticmethod
    def get_next_balance(status):
        if status == Status.GET_PERIOD.value:
            return Status.GET_BALANCE_FOOD.value
        elif status == Status.GET_BALANCE_FOOD.value:
            return Status.GET_BALANCE_ALCO.value
        elif status == Status.GET_BALANCE_ALCO.value:
            return Status.GET_BALANCE_TRANSPORT.value
        elif status == Status.GET_BALANCE_TRANSPORT.value:
            return Status.GET_BALANCE_GENERAL.value
        elif status == Status.GET_BALANCE_GENERAL.value:
            return Status.GET_BALANCE_FINPILLOW.value
        elif status == Status.GET_BALANCE_FINPILLOW.value:
            return Status.MAIN_MENU.value
