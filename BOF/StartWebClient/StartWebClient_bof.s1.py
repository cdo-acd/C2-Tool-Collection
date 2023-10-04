from typing import List, Tuple

from outflank_stage1.task.base_bof_task import BaseBOFTask
from outflank_stage1.task.enums import BOFArgumentEncoding


class StartWebClientBOF(BaseBOFTask):
    def __init__(self):
        super().__init__("start_web_client", base_binary_name="StartWebClient")
        self.parser.description = "Starting WebClient Service Programmatically."
