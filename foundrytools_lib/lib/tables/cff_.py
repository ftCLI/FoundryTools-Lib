from fontTools.cffLib import TopDict
from fontTools.ttLib import TTFont

from foundrytools_lib.lib.constants import CFF_TABLE_TAG
from foundrytools_lib.lib.tables.default import DefaultTbl


class CFFTable(DefaultTbl):  # pylint: disable=too-few-public-methods
    """
    This class extends the fontTools ``CFF `` table to add some useful methods.
    """

    def __init__(self, ttfont: TTFont) -> None:
        """
        Initializes the ``CFF `` table handler.
        """
        super().__init__(ttfont=ttfont, table_tag=CFF_TABLE_TAG)

    @property
    def top_dict(self) -> TopDict:
        """
        Returns the topDictIndex field of the 'CFF ' table.
        """
        return self.table.cff.topDictIndex[0]
