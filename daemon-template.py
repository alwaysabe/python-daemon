#!/usr/bin/env python

import sys, time
from daemon import Daemon
import logging
import logging.handlers
import os
date_fmt = '%m/%d/%Y %H:%M:%S'
log_formatter = logging.Formatter(u'[%(asctime)s] %(levelname)-7s: %(message)s (%(filename)s:%(lineno)d)', datefmt=date_fmt)
log_dir = os.path.join("logs", "ussd_app")
log_name = os.path.join(log_dir, "auto_renewals.log")
bytes = 1024 * 1024   # 1 MB
if not os.path.exists(log_dir):
  os.makedirs(log_dir)
handler = logging.handlers.RotatingFileHandler(log_name, maxBytes=bytes, backupCount=7)
handler.setFormatter(log_formatter)
handler.setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().addHandler(handler)

class MyDaemon(Daemon):
  """
   Add the function here in run. Adjust sleep time as desired.
  """
  def run(self):
    while True:
      time.sleep(1)		
      logging.getLogger(__name__).info("Initialized logging subsystem")

if __name__ == "__main__":
  daemon = MyDaemon('/tmp/daemon-example.pid')
  if len(sys.argv) == 2:
    if 'start' == sys.argv[1]:
      daemon.start()
    elif 'stop' == sys.argv[1]:
      daemon.stop()
    elif 'restart' == sys.argv[1]:
      daemon.restart()
    else:
      print "Unknown command"
      sys.exit(2)
    sys.exit(0)
  else:
    print "usage: %s start|stop|restart" % sys.argv[0]
    sys.exit(2)
