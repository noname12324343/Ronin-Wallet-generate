from web3 import Web3
from eth_account import Account
from colorama import init, Fore, Back, Style
import webbrowser

init()

print(Fore.GREEN + """                      Bản quyền thuộc về https://t.me/Justice0210
            Ngoài ra mình bán tool check live Twitter (X), Tool đọc mail,
                            ae nào cần có thể ủng hộ mình :3""" + Style.RESET_ALL)

webbrowser.open('https://youtu.be/eYEZZ5huOBo') 

w3 = Web3(Web3.HTTPProvider('https://proxy.roninchain.com/free-gas-rpc'))
def create_ronin_wallet():
    Account.enable_unaudited_hdwallet_features()
    acct, mnemonic = Account.create_with_mnemonic()
    address = acct.address
    return mnemonic, address
quantity = int(input('Nhập số acc cần tạo: '))
f = open('Ronin.txt','a')
for i in range(quantity):
    mnemonic, address = create_ronin_wallet()
    print(f"""
    {i + 1}
    Mnemonic: {mnemonic}
    Address: {address}

    """)
    f.write(f'{address} | {mnemonic}\n')


