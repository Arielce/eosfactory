import os
import setup
import eosf

from eosf import Verbosity
import eosf_account
from eosf_wallet import Wallet
from eosf_account import account_create, account_master_create

logger.Logger.verbosity = [Verbosity.TRACE, Verbosity.OUT, Verbosity.DEBUG]
logger.set_throw_error(False)

remote_testnet = "http://88.99.97.30:38888"
_ = logger.Logger()

'''
The following account exists in the blockchain of the testnode. It is used, in
this article, for testing.

Accout Name: dgxo1uyhoytn
Owner Public Key: EOS8AipFftYjovw8xpuqCxsjid57XqNstDyeTVmLtfFYNmFrgY959
Active Public Key: EOS6HDfGKbR79Gcs74LcQfvL6x8eVhZNXMGZ48Ti7u84nDnyq87rv

Owner Private Key: 5JE9XSurh4Bmdw8Ynz72Eh6ZCKrxf63SmQWKrYJSXf1dEnoiKFY
Active Private Key: 5JgLo7jZhmY4huDNXwExmaWQJqyS1hGZrnSjECcpWwGU25Ym8tA 
'''

logger.set_is_testing_errors(False)
logger.set_throw_error(True)

_.SCENARIO('''
Test registering to a remote testnet.
Set-up: 
    * Delete existing, if any, wallet named ``jungle_wallet`` using
        a general procedure as the EOSFactory does not have any.
    * Set KEOSD as the Wallet Manager.
    * Set the URL of a remote testnet.
    * Stop the KEOSD Wallet Manager.
    * Create a wallet named ``jungle_wallet``;
        Expected result is that a password message is printed.
Test:
    Use the ``create_master_account`` factory with the name of the resulting
    account object. 
    
    You can add the second argument that is a desired
    name of the physical account (if not set the name argument is random).
    If the given name is not available, the factory loops.
''')

setup.set_nodeos_address(remote_testnet)
eosf.kill_keosd()

wallet_name = "jungle_wallet"
try:
    os.remove(eosf.wallet_dir() + wallet_name + ".wallet")
except:
    pass

wallet = Wallet(wallet_name)

_.COMMENT('''
Use ``eosf.info()`` to check whether the remote testnet responces: it throws
an exception if the testnode is off. 
''')

eosf.info()

_.COMMENT('''
Use an active account, called ``account_master_test`` to simulate the 
registration procedure: in tests, this account substitutes one that would be
physically registered.
''')
eosf_account.account_master_test = eosf_account.GetAccount(
    "account_master_test",
    "dgxo1uyhoytn", 
    "5JE9XSurh4Bmdw8Ynz72Eh6ZCKrxf63SmQWKrYJSXf1dEnoiKFY",
    "5JgLo7jZhmY4huDNXwExmaWQJqyS1hGZrnSjECcpWwGU25Ym8tA"
)
eosf_account.account_master_test.ERROR()

logger.set_throw_error(False)
logger.set_is_testing_errors()        
######################################################################

_.COMMENT('''
In subsequent tests, you have to change the account object name, here 
``account_master``, or you have to resolve name conflicts, if you are prompted.
''')
account_master_create("account_master")