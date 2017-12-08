from logging import getLogger

from employee.common.constants import LOGGER_NAME


def logger(func_name):
	def __decorator(func):
		def inner(*args, **kwargs):
			log = getLogger(LOGGER_NAME)

			log.info(func_name + "開始")

			result = func(*args, **kwargs)

			log.info(func_name + "終了")

			return result

		return inner

	return __decorator
