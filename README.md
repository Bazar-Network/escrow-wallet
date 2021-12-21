# README #

This repo allows to:

**stakeTokens: Add any approved token to the farming contract for yeild farming, collateral
**unStakeTokens: Remove your tokens from the contract.
**getUserTotalValue: Get the total value that users have supplied based on calculations from the Chainlink Price Feeds.
**issueTokens: Issue a reward to the users

### Installation ###
- nodejs
- npm
- python
- brownie
- ganache
- web3 infura
- .env data is required as follows 

- export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
- export PRIVATE_KEY=<PRIVATE_KEY>
- export ETHERSCAN_TOKEN=<YOUR_TOKEN>

### Usage ###

brownie run scripts/deploy.py
This will deploy the contracts for testing with Chainlink

brownie run scripts/deploy.py --network kovan
This will do the same thing... but on Kovan.

### Testing ###
brownie test
brownie test -k test_stake_and_issue_correct_amounts --network kovan

