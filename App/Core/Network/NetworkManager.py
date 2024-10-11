from App.Core.Abstract import AbstractConnectionHandler, AbstractReceiveDataHandler
from App.Core.Network import TcpServer
from App.Core import Config, Platform
from App.Core.Logger import Log
from App.Core.Network.Protocol import RCL

if Platform.system_is('Windows'):
    import msvcrt


class NetworkManager:
    def __init__(self, log: Log, config: Config, rcl: RCL, platform: Platform):
        self.__logger = log
        self.__config = config
        self.__protocol = rcl
        self.__platform = platform

    def __debug(self, message: str):
        self.__logger.debug(message, {'object': self})

    def start_server(self, connection_handler: AbstractConnectionHandler, receive_handler: AbstractReceiveDataHandler):
        debug = self.__config.get('server.debug')

        server = TcpServer(self.__config, self.__logger, connection_handler, receive_handler)

        server.daemon = self.__config.get('server.daemon')

        server.start()

        if debug:
            self.__debug('Server started.')

        try:
            if self.__platform.is_windows():
                while True:
                    # Emulate Ctrl+C
                    if msvcrt.getch() == b'\x03':
                        server.terminate()
                        break

            server.join()
        except (KeyboardInterrupt, SystemExit):
            pass

        if debug:
            message = f"Server stopped{' by timeout' if server.is_alive() else ''}"

            self.__logger.debug(message, {'object': self})

