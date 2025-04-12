from web3 import Web3
import json

class DAOGovernance:
    def __init__(self, contract_address, abi, web3_provider):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)

    def propose(self, proposal_data, account):
        tx = self.contract.functions.propose(proposal_data).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key='YOUR_PRIVATE_KEY')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def vote(self, proposal_id, support, account):
        tx = self.contract.functions.vote(proposal_id, support).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key='YOUR_PRIVATE_KEY')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def get_proposals(self):
        return self.contract.functions.getProposals().call()

    def get_votes(self, proposal_id):
        return self.contract.functions.getVotes(proposal_id).call()