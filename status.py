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

    def get_next_balance(self, status):
        if status == self.GET_BALANCE_FOOD:
            return self.GET_BALANCE_ALCO
        elif status == self.GET_BALANCE_ALCO:
            return self.GET_BALANCE_TRANSPORT
        elif status == self.GET_BALANCE_TRANSPORT:
            return self.GET_BALANCE_GENERAL
        elif status == self.GET_BALANCE_GENERAL:
            return self.GET_BALANCE_FINPILLOW
        elif status == self.GET_BALANCE_FINPILLOW:
            return None