from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me = fund_me.fund({"from": account, "value": entrance_fee})
    fund_me.wait(1)
    print("Funded")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing")
    withdraw = fund_me.withdraw({"from": account})
    withdraw.wait(1)
    print("End")


def main():
    fund()
    withdraw()
