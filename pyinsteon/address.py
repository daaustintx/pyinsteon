"""Insteon device address class."""
import logging
import binascii


_LOGGER = logging.getLogger(__name__)


def _normalize(addr):
    """Take any format of address and turn it into a hex string."""
    normalize = None
    if isinstance(addr, Address):
        normalize = bytes(addr)

    elif isinstance(addr, bytearray):
        normalize = bytes(addr)

    elif isinstance(addr, bytes):
        normalize = addr

    elif isinstance(addr, str):
        addr_clean = addr.replace('.', '')
        try:
            if len(addr_clean) != 6:
                raise ValueError('Improper address value: {}'.format(addr))
            else:
                normalize = binascii.unhexlify(addr_clean.lower())
        except binascii.Error:
            raise ValueError('Improper address value: {}'.format(addr))

    elif addr is None:
        normalize = None

    else:
        _LOGGER.warning('Address class init with unknown type %s: %r',
                        type(addr), addr)
    return normalize


class Address():
    """Datatype definition for INSTEON device address handling."""

    def __init__(self, addr):
        """Create an Address object."""
        self._addr = _normalize(addr)

    def __repr__(self):
        """Representation of the Address object."""
        return self._addr.hex()

    def __str__(self):
        """Emit the address in human-readible format (AA.BB.CC)."""
        return '{}.{}.{}'.format(self.__repr__()[0:2],
                                 self.__repr__()[2:4],
                                 self.__repr__()[4:6]).upper()

    def __bytes__(self):
        """Return the bytes representation of the address."""
        return self._addr

    def __eq__(self, other):
        """Test for equality."""
        if isinstance(other, Address):
            return bytes(self) == bytes(other)
        return False

    def __ne__(self, other):
        """Test for not equals."""
        if isinstance(other, Address):
            return bytes(self) != bytes(other)
        return True

    def __lt__(self, other):
        """Test for less than."""
        if isinstance(other, Address):
            return bytes(self) < bytes(other)
        raise TypeError

    def __gt__(self, other):
        """Test for greater than."""
        if isinstance(other, Address):
            return bytes(self) > bytes(other)
        raise TypeError

    def __hash__(self):
        """Create a hash code for the Address object."""
        return hash(str(self))

    def __getitem__(self, byte):
        """Return a btye within the Address object."""
        if byte in [0, 1, 2]:
            return self._addr[byte]
        raise ValueError('Item index must be 0, 1 or 2')

    @property
    def id(self):
        """Return the address id."""
        return repr(self)
