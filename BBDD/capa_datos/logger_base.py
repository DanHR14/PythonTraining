import logging

logger = logging

#Indicamos que solo apareceran los logs de nivel info para arriba (INFO, WARNING, ERROR, CRITICAL)
logger.basicConfig(level=logging.INFO,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%d/%m/%Y %I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),
                       logging.StreamHandler()
                   ])

if __name__ == '__main__':
    logging.warning('mensaje a nivel de warning')
    logging.info('mensaje a nivel de info')
    logging.debug('mensaje a nivel debug')
    logging.error('Ocurrió un error en la base de datos')
    logging.debug('Se realizo la conexion a la BBDD')

