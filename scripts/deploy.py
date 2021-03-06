from scripts.helpful_scripts import get_account, get_contract
from brownie import AvocadoToken, TokenFarm, network, config
from web3 import Web3
import yaml
import json
import os
import shutil

KEPT_BALANCE = Web3.toWei(100, "ether")


def deploy_token_farm_and_avocado_token(front_end_update=False):
    account = get_account()
    avocado_token = AvocadoToken.deploy({"from": account})
    token_farm = TokenFarm.deploy(
        avocado_token.address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    tx = avocado_token.transfer(
        token_farm.address,
        avocado_token.totalSupply() - KEPT_BALANCE,
        {"from": account},
    )
    tx.wait(1)
    # avocado_token, weth_token, fau_token/dai
    weth_token = get_contract("weth_token")
    fau_token = get_contract("fau_token")
    dict_of_allowed_tokens = {
        avocado_token: get_contract("dai_usd_price_feed"),
        fau_token: get_contract("dai_usd_price_feed"),
        weth_token: get_contract("eth_usd_price_feed"),
    }
    add_allowed_tokens(token_farm, dict_of_allowed_tokens, account)
    if front_end_update:
        update_front_end()
    return token_farm, avocado_token


def add_allowed_tokens(token_farm, dict_of_allowed_tokens, account):
    for token in dict_of_allowed_tokens:
        add_tx = token_farm.addAllowedTokens(token.address, {"from": account})
        add_tx.wait(1)
        set_tx = token_farm.setPriceFeedContract(
            token.address, dict_of_allowed_tokens[token], {"from": account}
        )
        set_tx.wait(1)
    return token_farm


def main():
    deploy_token_farm_and_avocado_token(front_end_update=True)
