from typing import List, Tuple

from outflank_stage1.task.base_bof_task import BaseBOFTask
from outflank_stage1.task.enums import BOFArgumentEncoding


class SmbinfoBOF(BaseBOFTask):
    def __init__(self):
        super().__init__("smbinfo", base_binary_name="Smbinfo")

        self.parser.description = (
            "Use NetWkstaGetInfo API to gather remote system version info."
        )

        self.parser.add_argument("hostname", help="Target")

    def _encode_arguments_bof(
        self, arguments: List[str]
    ) -> List[Tuple[BOFArgumentEncoding, str]]:
        parser_arguments = self.parser.parse_args(arguments)

        return [(BOFArgumentEncoding.WSTR, parser_arguments.hostname)]
