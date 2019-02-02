from binascii import unhexlify
import logging
import unittest

from pyinsteon.address import Address
from pyinsteon.messages.message_flags import MessageFlags
from pyinsteon.messages.inbound import Inbound, create
from pyinsteon.constants import MessageId, MESSAGE_ACK, MESSAGE_NAK
from pyinsteon.messages.user_data import UserData
from pyinsteon.messages.template import send_extended

from .template_base import TestTemplateBase
from ...utils import hex_to_inbound_message


_LOGGER = logging.getLogger(__name__)
_INSTEON_LOGGER = logging.getLogger('pyinsteon')


class TestSendExtended(unittest.TestCase, TestTemplateBase):

    def setUp(self):
        self.buffer = True
        self.hex_data = '0262010203140506a1a2a3a4a5a6a7a8a9aaabacadae06'
        self.bytes_data = bytearray(unhexlify(self.hex_data))
        self.message_id = MessageId.SEND_EXTENDED.value
        self.address = Address('010203')
        self.flags = MessageFlags(0x14)
        self.cmd1 = int(0x05)
        self.cmd2 = int(0x06)
        self.user_data = UserData(unhexlify('a1a2a3a4a5a6a7a8a9aaabacadae'))
        self.ack = MESSAGE_ACK

        self.msg_in, _ = hex_to_inbound_message(self.hex_data)
        self.msg = send_extended(self.address, self.flags,
                                 self.cmd1, self.cmd2, self.user_data, self.ack)

    def test_address(self):
        assert self.msg.address == self.address

    def test_flags(self):
        assert self.msg.flags == self.flags

    def test_cmd1(self):
        assert self.msg.cmd1 == self.cmd1

    def test_cmd2(self):
        assert self.msg.cmd2 == self.cmd2

    def test_user_data(self):
        assert self.msg.user_data == self.user_data

    def test_ack(self):
        _LOGGER.debug(self.msg.ack)
        _LOGGER.debug(self.ack)
        assert self.msg.ack == self.ack


if __name__ == '__main__':
    unittest.main()
