import logging.handlers


PUB_ARTICLE_TITLE = None


def log_basic_config():

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ls = logging.StreamHandler()
    lst = logging.handlers.TimedRotatingFileHandler("./log/html_test01.log",
                                                    when='midnight', interval=1, backupCount=2, encoding="utf-8")

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    ls.setFormatter(formatter)
    lst.setFormatter(formatter)

    logger.addHandler(ls)
    logger.addHandler(lst)