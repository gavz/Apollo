from CommandBase import *
import json


class DownloadArguments(TaskArguments):

    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        if len(self.command_line) == 0:
            raise Exception("Require a path to download.")


class DownloadCommand(CommandBase):
    cmd = "download"
    needs_admin = False
    help_cmd = "download [path/to/file]"
    description = "Download a file off the target system."
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = True
    is_upload_file = False
    is_remove_file = False
    author = "@djhohnstein"
    argument_class = DownloadArguments
    attackmapping = []
    browser_script = BrowserScript(script_name="download", author="@its_a_feature_")

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass