# zimbrasync
Script for synchronization for zimbra

# usage
* For unique account:
  - python3.6 zimbra-sync-imap.py --conta <(SYNC ACCOUNT)> --host1 <(SOURCE SERVER)> --userauth1 <(SOURCE AUTH ACCOUNT)> --passwd1 <(SOURCE ACCOUNT PASSWORD)> --host2 <(DESTINATION SERVER)> --userauth2 <(DESTINATION AUTH ACOUNT)> --passwd2 <(DESTINATION PASSWORD)>
* For mass account sync:
  - python3.6 zimbra-sync-imap.py --arq <FILE SYNC ACCOUNT> --host1 <(SOURCE SERVER)> --userauth1 <(SOURCE AUTH ACCOUNT)> --passwd1 <(SOURCE ACCOUNT PASSWORD)> --host2 <(DESTINATION SERVER)> --userauth2 <(DESTINATION AUTH ACOUNT)> --passwd2 <(DESTINATION PASSWORD)>

Note: For mass synchronization use a .txt file with each account on one line. Example:
account1@server.com.br
account2@server.com.br
...
