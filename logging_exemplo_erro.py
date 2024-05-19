from loguru import logger

logger.debug('Um aviso para o desenvolvedor no futuro')
logger.info('Informacao importante do processo')
logger.warning('Um aviso que algo vai parar de funcionar no futuro')
logger.error('Aconteceu um falha')
logger.critical('Aconteceu algo que aborta a aplicacao')