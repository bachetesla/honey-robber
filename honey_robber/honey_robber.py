class HoneyRobber:
    """
    Main Honey robber interface
    """

    def __init__(self):
        pass

    def get_log(self):
        """
        This method will read log live
        """
        pass

    def parse_log(self):
        """
        This method will parse log file on stream
        """
        pass

    def get_password(self):
        """
        This method will read password from parse_log
        """
        pass

    def get_user_pass(self):
        """
        This method will read user:password from parse_log
        """
        pass

    def write_password(self, password_list_file):
        """
        This method will write passwords into a file
        :param password_list_file
        :return:
        """
        pass

    def write_user_password(self, user_pass_file):
        """
        This method will write user_pass into a file
        :param user_pass_file
        :return:
        """
        pass
