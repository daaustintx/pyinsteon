from binascii import unhexlify
import logging
import unittest
import sys

from pyinsteon.constants import MessageId, AckNak
from pyinsteon.messages.template import reset_im

from .template_base import TestTemplateBase
from ...utils import hex_to_inbound_message

_LOGGER = logging.getLogger(__name__)
_INSTEON_LOGGER = logging.getLogger('pyinsteon')


class TestResetIm(unittest.TestCase, TestTemplateBase):

    def setUp(self):
        self.hex = '0267'
        self.hex_ack = '026706'
        self.message_id = MessageId(0x67)
        self.ack = AckNak(0x06)

        self.msg_in, _ = hex_to_inbound_message(self.hex_ack)
        self.msg = reset_im(self.ack)
        
        stream_handler = logging.StreamHandler(sys.stdout)
        _LOGGER.addHandler(stream_handler)

    def test_ack_nak(self):
        assert self.msg.ack == self.ack


if __name__ == '__main__':
    unittest.main()
