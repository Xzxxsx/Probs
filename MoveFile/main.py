import dirsync
import logging
import datetime
import schedule


save_log = input("Where to save log")
logging.basicConfig(filename=save_log, level=logging.DEBUG)
source = input("What dir to copy ")
target = input("Where to copy")


time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def sinc():
    dirsync.sync(source, target, 'sync', verbose=True)
    logging.info(f"Dir sync om {time}")
    logging.info(dirsync.sync(source, target, 'sync', verbose=True))


schedule.every().hour.do(sinc)
while True:
    schedule.run_pending()
    time.sleep(1)