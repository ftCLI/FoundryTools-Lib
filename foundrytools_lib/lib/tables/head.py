from fontTools.misc.textTools import num2binary
from fontTools.ttLib import TTFont

from foundrytools_lib.lib.constants import HEAD_TABLE_TAG
from foundrytools_lib.lib.tables.default import DefaultTbl
from foundrytools_lib.lib.utils.bits_tools import is_nth_bit_set

BOLD_BIT = 0
ITALIC_BIT = 1


class MacStyle:
    """
    A wrapper class for the ``macStyle`` field of the ``head`` table.
    """

    def __init__(self, head_table: "HeadTable") -> None:
        self.head_table = head_table

    def __repr__(self) -> str:
        return f"macStyle({num2binary(self.head_table.table.macStyle)})"

    @property
    def bold(self) -> bool:
        """
        Returns True if the bit 0 (BOLD_BIT) is set in the ``macStyle`` field of the ``head`` table,
        False otherwise.
        """
        return is_nth_bit_set(self.head_table.table.macStyle, BOLD_BIT)

    @bold.setter
    def bold(self, value: bool) -> None:
        """
        Sets the bit 0 (BOLD_BIT) in the ``head.macStyle`` field.
        """
        self.head_table.set_bit(field_name="macStyle", pos=BOLD_BIT, value=value)

    @property
    def italic(self) -> bool:
        """
        Returns True if the bit 1 (ITALIC) is set in the ``macStyle`` field of the ``head`` table,
        False otherwise.
        """
        return is_nth_bit_set(self.head_table.table.macStyle, ITALIC_BIT)

    @italic.setter
    def italic(self, value: bool) -> None:
        """
        Sets the bit 1 (ITALIC_BIT) in the ``head.macStyle`` field.
        """
        self.head_table.set_bit(field_name="macStyle", pos=ITALIC_BIT, value=value)


class HeadTable(DefaultTbl):
    """
    This class extends the fontTools ``head`` table to add some useful methods.
    """

    def __init__(self, ttfont: TTFont) -> None:
        """
        Initializes the ``head`` table handler.

        Args:
            ttfont (TTFont): The ``TTFont`` object.

        Returns:
            None
        """
        super().__init__(ttfont=ttfont, table_tag=HEAD_TABLE_TAG)
        self.mac_style = MacStyle(head_table=self)
