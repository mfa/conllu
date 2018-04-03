import gzip
import os.path
import unittest

from conllu.parser import parse_tree


def load_sentence():
    sentence = ''
    filename = os.path.join(os.path.dirname(__file__),
                            'fixtures/UD2.conllu.gz')
    with gzip.open(filename) as fp:
        for line in fp.read().split(b'\n'):
            line = line.decode('utf-8')
            if line.strip() == '':
                yield parse_tree(sentence)
                sentence = ''
            else:
                if not line.startswith('#'):
                    sentence += line + '\n'


class TestUDExamples(unittest.TestCase):

    def test_example1(self):
        # this examples break sent_to_tree
        for _ in load_sentence():
            pass
