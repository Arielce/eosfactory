'''
# Account name conflict

This file can be executed as a python script: 
`python3 account_name_conflict.md`.

## Set-up

The set-up statements are explained at <a href="setup.html">cases/setup</a>.

```md
'''
from eosfactory.eosf import *
'''
```
## Case

The EOSFactory wraps EOSIO accounts with objects. The symbolic name of an 
account object, for example 'account_alice', has to be unique in a program. 
Moreover, it has be unique in a collection of scripts, especially, if they 
execute real transactions.

The EOSFactory uses mapping files that keep the uniqueness.

But, what if the user wants to ascribe a previously used name to another 
physical account: the only way to keep the previous physical account within the 
system is to change its mapping name.

Create two account objects: 'account_alice' and 'account_carrol'.

Then try to create another account object called 'account_alice'. Although
this object is going to refer to a new blockchain account, it cannot accept
the given name: error is issued.

You are prompted to change the blocking name. On acceptance, the 'nano' 
editor opens. CTR+X, to save and exit.

Change 'account_alice' to 'account_alice_b'.

```md
'''
reset()
create_master_account("master")

create_account("alice", master)
create_account("carrol", master)

create_account("alice", master)
'''
```

### Test run

In an linux bash, change directory to where this file exists, that is the 
directory 'docs/source/cases' in the repository, and enter the following 
command:

```md
$ python3 account_name_conflict.md
```
```md
We hope that you get something similar to this one shown in the image below.
```

![account_name_conflict](./img/account_name_conflict.png)

'''
