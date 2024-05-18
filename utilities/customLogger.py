import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        # Create a logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create console handler and set level to INFO
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # Create file handler and set level to DEBUG
        log_dir = os.path.join(os.path.dirname("C:\\Users\\rasul\\PycharmProjects\\pythonProject\\OpencartV1\\pythonProject1\\logs"), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, 'app.log')
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger