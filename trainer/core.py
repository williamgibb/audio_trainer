import os
import random
import logging

import pydub
import pydub.playback as p_play

log = logging.getLogger(__name__)


class AudioCore:
    def __init__(self, dirn, conf=None):
        self.dirn = dirn
        if conf is None:
            conf = {}
        self.conf = conf

        self.samples = {}

        self._initDirnSamples()

    def _initDirnSamples(self):
        log.info(f'Initializing samples from {self.dirn}')
        for dirn, dirs, fns in os.walk(self.dirn):
            for fn in fns:
                if fn.endswith('wav'):
                    fp = os.path.join(dirn, fn)
                    self.addSample(fp)
        log.info('Done initializing samples.')

    def addSample(self, fp, format='wav'):
        log.debug(f'Adding sample from [{fp}] as {format}')

        self.samples[fp] = pydub.AudioSegment.from_file(fp, format=format)
        # with open(fp, 'rb') as fd:
        #     self.samples[fp] = fd.read()

    def run(self):
        # Simple random shuffle test
        items = list(self.samples.items())
        random.shuffle(items)
        for fp, segment in items:
            log.info(f'Playing: {fp}')
            p_play.play(segment)
