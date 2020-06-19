

# Account_Numbers:
#     1__ - DepositAccount
#         11 - Personal DepositAccount
#         12 - Business DepositAccount
#     2__ - CreditAccount
#         211 - Personal CreditAccount
#         212 - Business CreditAccount
#         221 - Personal MortgageAccount
#         222 - Business MortgageAccount

import matplotlib.pyplot as plt
import numpy as np

X = ['05/06', '07/06', '08/06', '11/06', '12/06', '15/06', '16/06', '17/06', '18/06']
Y = [1500, 650, 31800, 5000, 8400, 26820, 18100, 12000, 5000]
Z = [1000, 0, 11300, 5000, 6000, 16000, 18100, 9000, 7000]

_X = np.arange(len(X))

plt.bar(_X - 0.2, Y, 0.4)
plt.bar(_X + 0.2, Z, 0.4)
plt.xticks(_X, X) # set labels manually
plt.show()
