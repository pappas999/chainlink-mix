from brownie import ERC20Basic, config, accounts, network

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = ERC20Basic[-1]
    print("Total Supply is", erc20.totalSupply())


    tx = erc20.transfer('0x13e8f179F4760984DB9a41c94365ff8b103DeBC4',10,{'from': account})
    tx.wait(1)
    print("New token balance is", erc20.balanceOf(account.address,{'from': account}))