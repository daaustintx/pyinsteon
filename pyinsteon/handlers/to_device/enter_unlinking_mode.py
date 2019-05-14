"""Get Device Info command handler."""
from .direct_command import DirectCommandHandlerBase
from ..address import Address
from ..topics import ENTER_UNLINKING_MODE


class EnterUnlinkingModeCommand(DirectCommandHandlerBase):
    """Place a device in linking mode command handler."""

    def __init__(self, address: Address):
        """Init the EnterUnlinkingModeCommand class."""
        super().__init__(address, ENTER_UNLINKING_MODE)

    #pylint: disable=arguments-differ
    async def async_send(self, group: int = 0):
        """Send the ENTER_UNLINKING_MODE request asyncronously."""
        return await super().async_send(address=self._address, group=group)
        