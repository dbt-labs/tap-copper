from tap_copper.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class OpportunitiesStream(BaseStream):
    API_METHOD = 'POST'
    TABLE = 'opportunities'
    KEY_PROPERTIES = ['id']

        
    @property
    def path(self):
        return '/opportunities/search'