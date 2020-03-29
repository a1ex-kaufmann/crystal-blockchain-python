class CrystalException(Exception):
    """Base class for crystal client exceptions."""
    pass

# TODO разобраться с этим
# class InsufficientFundsException(CrystalException):
#     """Raise when not enough funds to process transaction."""
#
#     def __init__(self, message, acc, amount, fee):
#         """Constructor."""
#         super(InsufficientFundsException, self).__init__(message)
#         self.acc = acc
#         self.amount = amount
#         self.fee = fee
#
#
# class InsufficientFeeException(CrystalException):
#     """Raise when failed process transaction due insufficient fee."""
#
#     def __init__(self, message, fee):
#         """Constructor."""
#         super(InsufficientFeeException, self).__init__(message)
#         self.fee = fee
#
#
# class MinimalTransferLimitException(CrystalException):
#     """Raise when amount (with fee) < MINIMAL_TRANSFER."""
#
#     def __init__(self, message, amount, minimal):
#         """Constructor."""
#         super(MinimalTransferLimitException, self).__init__(message)
#         self.amount = amount
#         self.minimal = minimal
#
#
# class InvalidAddress(CrystalException):
#     """Raises whent address validation fails."""
#     pass
