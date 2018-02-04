from logging import getLogger

from employee.common.constants import LOGGER_NAME


def logger(func):
    def inner(*args, **kwargs):
        log = getLogger(LOGGER_NAME)

        # args[0]：実行されたクラス
        # args[1]：requestオブジェクト
        log.info(str(args[0].__class__) + "開始")

        result = func(*args, **kwargs)

        log.info(str(args[0].__class__) + "終了")

        return result

    return inner
