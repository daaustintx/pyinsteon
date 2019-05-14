"""Load saved devices to provide quick startup."""

import asyncio
from pyinsteon import async_connect, devices, async_close
from pyinsteon.managers.link_manager import async_link_devices
from . import _LOGGER, set_log_levels, PATH


# DEVICE = '/dev/ttyS5'
DEVICE = 'COM5'
HOST = '192.168.1.136'
USERNAME = 'username'
PASSWORD = 'password'


def state_changed(name, value, group):
    """Capture the state change."""
    _LOGGER.info('State changed to %s', value)


async def do_run():
    """Connect to the PLM and load the ALDB."""
    modem = await async_connect(device=DEVICE)
    # modem = await async_connect(host=HOST,
    #                             username=USERNAME,
    #                             password=PASSWORD)
    _LOGGER.info('Connected')
    _LOGGER.info('Modem Address: %s', modem.address)
    await devices.async_load(workdir=PATH, id_devices=0)
    controller = devices.get('27.C3.87')
    responder = devices.get('13.36.96')
    link_result = await async_link_devices(controller, responder, 1)
    if link_result:
        _LOGGER.info(link_result)
    await async_close()


if __name__ == '__main__':
    set_log_levels(logger='info', logger_pyinsteon='info', logger_messages='info')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_run())