import time
import os


class HoneyRobber:
    """
    Main Honey robber interface
    """

    def __init__(self, log_file_path, password_list_file_path=None, pair_list_file_path=None):
        self.log_file_path = log_file_path
        self.password_list_file_path = password_list_file_path
        self.pair_list_file_path = pair_list_file_path
        self.pair = list()

    def fallow_log(self):
        """
        Fallowing log file stream
        """
        file = self.open_log_file()
        file.seek(0, os.SEEK_END)  # Go to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly
                continue
            yield line

    def open_log_file(self):
        """
        This method will read log live
        """
        try:
            return open(self.log_file_path, "r")
        except FileNotFoundError:
            print("HoneyPot server is not running...")
            exit()

    @classmethod
    def _write_file(cls, file_path, line):
        with open(file_path, "a+") as file:
            file.write(line)

    def parse_log(self, write_pass=True, write_pair=True):
        """
        This method will parse log file on stream
        """
        pass

    def write_password(self, password):
        """
        This method will write passwords into a file
        :param password:
        """
        if self.password_list_file_path:
            _password = f"{password}\n"
            HoneyRobber._write_file(file_path=self.password_list_file_path, line=_password)

    def write_user_password(self, user, password):
        """
        This method will write user_pass into a file
        :param user:
        :param password:
        :return:
        """
        if self.pair_list_file_path:
            _pair = f"{user}:{password}\n"
            HoneyRobber._write_file(file_path=self.password_list_file_path, line=_pair)

