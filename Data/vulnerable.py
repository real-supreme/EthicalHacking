# from portscanner_4 import portscanner
# import os
from concurrent.futures import ThreadPoolExecutor as executor


class vulnerable:
    def __init__(self, banners: list):
        self.banners = banners

    # Matches with the banners
    def match_banners(self, path="banners.txt"):
        while True:
            try:
                f = open(path, "rt")
            except FileNotFoundError:
                print(f"File in path '{path}' doesn't exist!")
                self.create_banners
            else:
                lines = f.readlines()
                with executor() as exe:
                    res = exe.map(self.look_for_vulnerable, lines)
                    print(next(res))
                break
        return res

    # Creates a banner.txt if not exists.
    @property
    def create_banners(self):

        # Certain Vunerable banner names
        banners = r"""
        SSH-2.0-OpenSSH_5.3
        220 ProFTPD Server (srv.bretz.gmbh FTP Server) [::ffff:10.10.10.119]
        SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3
        220 mail.ybnetworks.synology.me ESMTP Postfix
        220 ProFTPD Server (ProFTPD) [213.175.208.161]
        euk-98524.eukservers.com ESMTP Postfix
        +OK Dovecot ready. <370.1.6137b1c9.LFthJ0iiJJV2aLPtd88G+g==@euk-98524.eukservers.com>
        * OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ STARTTLS AUTH=PLAIN AUTH=LOGIN AUTH=DIGEST-MD5 AUTH=CRAM-MD5] Dovecot ready.
        +OK Dovecot ready.
        OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ STARTTLS LOGINDISABLED UTF8=ACCEPT] Dovecot ready.
        """
        with open("banners.txt", "w") as ban:
            banners = banners.splitlines()
            ban.writelines(banners)
        print(f"Created Banners.txt")

    def look_for_vulnerable(self, lines):
        matched = []
        for line in lines:
            line = line.replace("\n", "")
            if line.strip() in self.banners:
                matched.append(line.strip())
        return matched


if __name__ == "__main__":
    print(vulnerable().match_banners(["1", "<ul>"]))
