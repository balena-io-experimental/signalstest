#!/usr/bin/env python3

import time
import signal
import logging


class Example():
  def __init__(self):
    logging.info('initing')
    self.running = True
    signal.signal(signal.SIGINT, self._int)
    signal.signal(signal.SIGTERM, self._term)
    signal.signal(signal.SIGUSR1, self._usr1)

  def _int(self, signum, frame):
    logging.info('SIGINT called')
    logging.debug('signum: %i', signum)
    self.running = False

  def _term(self, signum, frame):
    logging.info('SIGTERM called')
    logging.debug('signum: %i', signum)
    self.running = False

  def _usr1(self, signum, frame):
    logging.info('SIGUSR received')
    logging.debug('signum: %i', signum)

  def run(self):
    while self.running:
      logging.info('running')
      time.sleep(1)

if __name__ == '__main__':
  logFormat = '%(asctime)s [%(levelname)s] %(message)s'
  logging.basicConfig(level=logging.DEBUG, format=logFormat)
  a = Example()
  a.run()
