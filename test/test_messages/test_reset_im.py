from binascii import unhexlify
import logging
import unittest
import sys

from pyinsteon.constants import MessageId, AckNak
from ..utils import hex_to_inbpund_message

_LOGGER = logging.getLogger(__name__)
_INSTEON_LOGGER = logging.getLogger('pyinsteon')


class TestResetIm(unittest.TestCase):

    def setUp(self):
        self.hex = '0267'
        self.hex_ack = '026706'
        self.id = MessageId(0x67)
        self.ack = AckNak(0x06)

        self.msg, self.msg_bytes = hex_to_inbpund_message(self.hex_ack)
        
        stream_handler = logging.StreamHandler(sys.stdout)
        _LOGGER.addHandler(stream_handler)

    def test_id(self):
        assert self.msg.id == self.id

    def test_ack_nak(self):
        assert self.msg.ack == self.ack

    def test_bytes(self):
        assert bytes(self.msg) == unhexlify(self.hex_ack)