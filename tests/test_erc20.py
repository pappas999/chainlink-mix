import time
import pytest
from brownie import ERC20Basic, network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account


@pytest.fixture
def deploy_erc20_exercise():
    # Arrange
    # Arrange / Act
    erc20 = ERC20Basic.deploy(
        10000000,
        {"from": get_account()}
    )
    # Assert
    assert erc20 is not None
    return erc20

def test_erc20_totalSupply(deploy_erc20_exercise):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    erc20 = deploy_erc20_exercise
    # Assert
    assert erc20.totalSupply() > 0



def test_erc20_transfer(deploy_erc20_exercise):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    erc20 = deploy_erc20_exercise
    tokensToTransfer = 100
    receiverAddress = '0x517f7Fe4f8778be9ff2dcFab5A99d434a52B63a7'
    senderCurrentTokenBalance = erc20.balanceOf(get_account())

    # Act
    transaction_receipt = erc20.transfer(receiverAddress,tokensToTransfer, {"from": get_account()})
    newTokenBalance = erc20.balanceOf(get_account())
    # Assert
    assert newTokenBalance < senderCurrentTokenBalance


