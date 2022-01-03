"""
cowrie/cowrie is a simple honeypot
"""
import re

from honey_robber.honey_robber import HoneyRobber


class Cowrie(HoneyRobber):
    """
    This Class is using cowrie/cowrie
    """
    def parse_log(self, write_pass=True, write_pair=True):
        """
        Parse log line and add user: pass to self.pairs
        """
        fallow_generator = self.fallow_log()
        for line in fallow_generator:
            match = re.search(r"login attempt \[(.*?)\]", line)
            if match:
                find = re.findall("\'(.*?)\'", match.string)
                self.pair.append({find[0]: find[1]})
                if write_pair:
                    self.write_user_password(user=find[0], password=find[1])
                if write_pass:
                    self.write_password(password=find[1])
