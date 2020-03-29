from .crystal_abstract import Crystal


class CrystalBTC(Crystal):
    ENDPOINT = 'https://apibtc.crystalblockchain.com'
    TOKEN_ID = 0


class CrystalUSDT(Crystal):
    ENDPOINT = 'https://apibtc.crystalblockchain.com'
    TOKEN_ID = 1


class CrystalETH(Crystal):
    ENDPOINT = 'https://apieth.crystalblockchain.com'
    TOKEN_ID = 0


class CrystalLTC(Crystal):
    ENDPOINT = 'https://apiltc.crystalblockchain.com'
    TOKEN_ID = 0


class CrystalBCH(Crystal):
    ENDPOINT = 'https://apibch.crystalblockchain.com'
    TOKEN_ID = 0
