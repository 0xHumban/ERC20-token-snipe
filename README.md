# ERC20-token-snipe
 Snipe erc20 tokens sent to one account

## How to run it ?
Configure the "config.py" with your data:
- provider address (like infura by example)
- public address (where tokens will be sent)
- private key of the public address above
- public address to sent tokens
- erc20 contract address (if used as a proxy)
- ABI of the contract
- chain ID (check it on chain list)
- max requests you want to send to the rpc (5000 by default)
- setup gas fees (setup by default but this can cause slow transaction)

Install dependencies

```sh
pip install -r requirements.txt
```

Run `main.py`
```sh
python .\main.py
```

*for Linux*

```sh
python3 main.py
```

## Precautions
If you use infura provider, ensure that the limit of 100k request per day is not exceeded.

Be careful with the use of your private key, **anyone with the key** can **access to your funds**!