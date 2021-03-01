import logging

logger = logging

logger.basicConfig(level=logging.WARNING,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('lab_final.log'),
                       logging.StreamHandler()
                   ])

