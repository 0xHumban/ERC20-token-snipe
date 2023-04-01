from web3 import Web3
import json
import config

# connect to the blockchain with provider address
w3 = Web3(Web3.HTTPProvider(config.provider_address))

# data recovery
public_address_snipe = config.ether_address_to_snipe

private_key = config.private_key

address_to_send_token = config.ether_address_to_send_token

chain_id = config.chain_id

max_requests = config.max_requests

gas_fee_price = config.gas_fee_price

max_gas_fees = config.max_gas_fees

## contract of the ERC20 token
contract_address = config.erc20_token_contract_address

abi_contract_address = json.loads(config.erc20_token_abi_contract_address)


# Main function
def snipe_erc20_token(public_address_snipe:str, address_to_send_token:str, private_key:str, contract_address,
                      abi_contract_address:json, chain_id:int,gas_fee_price:str, max_gas_fees:int,
                      max_requests:int=5000)->None:
    # "Create contract"
    contract = w3.eth.contract(address=contract_address, abi=abi_contract_address)

    # Get token balance of the user
    user_balance = contract.functions.balanceOf(public_address_snipe).call()

    total_requests = 1
    while user_balance == 0 and total_requests < max_requests:
        user_balance = contract.functions.balanceOf(public_address_snipe).call()
        total_requests += 1

    # Create new transaction
    tx = new_transaction(public_address_snipe, address_to_send_token, user_balance, contract, chain_id,
                         gas_fee_price, max_gas_fees)

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print("Number of requests: ", total_requests + 3)
    print('Transaction hash : ', w3.to_hex(tx_hash))


def new_transaction(public_address_snipe, address_to_send_token, user_balance:float, contract, chain_id:int,
                    gas_fee_price:str, max_gas_fees:int):

    nonce = w3.eth.get_transaction_count(public_address_snipe)
    tx = {
        'from': public_address_snipe,
        'to': contract_address,
        'nonce': nonce,
        'gas': max_gas_fees,
        'gasPrice': w3.to_wei(gas_fee_price, 'gwei'),
        'chainId': chain_id,
        'data': contract.encodeABI(fn_name='transfer', args=[address_to_send_token, user_balance])
    }
    return tx


if __name__ == "__main__":
    snipe_erc20_token(
        public_address_snipe, address_to_send_token, private_key, contract_address, abi_contract_address, chain_id,
        gas_fee_price, max_gas_fees, max_requests)
