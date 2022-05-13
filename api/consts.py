
# http header
API_URL = 'https://www.okex.com'
CONTENT_TYPE = 'Content-Type'
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'
SIMULATION_KEY = "x-simulated-trading"
SIMULATION_VALUE = 1

ACEEPT = 'Accept'
COOKIE = 'Cookie'
LOCALE = 'Locale='

APPLICATION_JSON = 'application/json'

GET = "GET"
POST = "POST"
DELETE = "DELETE"
PUT ="PUT"

PREFIX = '/api/v5'

# TRADE

## 下单 只有当账户有足够资金才能下单     限速60次/2s   规则 useId + instrumentType + underlying
TRADE_ORDER = PREFIX + '/trade/order'
## 批量下单
TRADE_BATCH_ORDER = PREFIX + '/trade/batch-orders'
## 撤单
TRADE_CANCEL_ORDER = PREFIX + '/trade/cancel-order'
## 批量撤单
TRADE_CANCEL_BATCH_ORDER = PREFIX + '/trade/cancel-batch-orders'
## 修改未完成的挂单
TRADE_AMEND_ORDER = PREFIX + '/trade/amend-order'
## 批量修改未完成的挂单
TRADE_AMEND_BATCH_ORDER = PREFIX + '/trade/amend-batch-orders'

## 市价仓位全平
TRADE_CLOSE_POSITION = PREFIX + '/trade/close-postion'
## 获取订单信息
TRADE_ORDER_INFO = PREFIX + '/trade/order'
## 获取未成交订单列别
TRADE_ORDER_PENDING = PREFIX + '/trade/orders-pending'
## 获取历史订单记录(七天)
TRADE_ORDER_HISTORY = PREFIX + '/trade/order-history'
## 获取历史订单记录(近三个月)
TRADE_ORDER_HISTORY_ARCHIVE = PREFIX + '/trade/order-history-archive'
## 获取成交明细（近三天）
TRADE_ORDER_FILLS = PREFIX + '/trade/fills'
## 获取成交明细（近三个月）
TRADE_ORDER_FILLS_HISTORY = PREFIX + '/trade/fills-history'

## 策略委托下单
TRADE_ALGO = PREFIX + '/trade/order-algo'
## 撤销策略委托下单
TRADE_ORDER_CANCEL_ALGO = PREFIX + '/trade/cancel-algos'
## 撤销高级策略委托订单
TRADE_ORDER_CANCEL_ADVANCE_ALGO = PREFIX + '/trade/cancel-advance-algos'
## 获取未完成策略委托单列表
TRADE_ALGO_PENDING = PREFIX + '/trade/orders-algo-pending'
## 获取历史策略委托单列表
TRADE_ALGO_HISTORY = PREFIX + '/trade/orders-algo-history'

# CURRENCY
## 获取平台所有币种列表
ASSET_CURRENCIES = PREFIX + '/asset/currencies'
## 获取资金账户余额
ASSET_BALANCE = PREFIX + '/asset/balances'
## 获取账户资产估值
ASSET_VALUATION = PREFIX + 'asset/asset-valuation'
## 资金划转
ASSET_TRANSFER = PREFIX + '/asset/transfer'
## 获取资金划转状态
ASSET_TRANSFER_STATE = PREFIX + '/asset/transfer-state'
## 获取资金流水
ASSET_





SERVER_TIMESTAMP_URL = '/api/general/v3/time'

# account
WALLET_INFO = '/api/account/v3/wallet'
CURRENCY_INFO = '/api/account/v3/wallet/'
COIN_TRANSFER = '/api/account/v3/transfer'
COIN_WITHDRAW = '/api/account/v3/withdrawal'
LEDGER_RECORD = '/api/account/v3/ledger'
TOP_UP_ADDRESS = '/api/account/v3/deposit/address'
ASSET_VALUATION = '/api/account/v3/asset-valuation'
SUB_ACCOUNT = '/api/account/v3/sub-account'
COINS_WITHDRAW_RECORD = '/api/account/v3/withdrawal/history'
COIN_WITHDRAW_RECORD = '/api/account/v3/withdrawal/history/'
COIN_TOP_UP_RECORDS = '/api/account/v3/deposit/history'
COIN_TOP_UP_RECORD = '/api/account/v3/deposit/history/'
CURRENCIES_INFO = '/api/account/v3/currencies'
COIN_FEE = '/api/account/v3/withdrawal/fee'

# spot
SPOT_ACCOUNT_INFO = '/api/spot/v3/accounts'
SPOT_COIN_ACCOUNT_INFO = '/api/spot/v3/accounts/'
SPOT_LEDGER_RECORD = '/api/spot/v3/accounts/'
SPOT_ORDER = '/api/spot/v3/orders'
SPOT_ORDERS = '/api/spot/v3/batch_orders'
SPOT_REVOKE_ORDER = '/api/spot/v3/cancel_orders/'
SPOT_REVOKE_ORDERS = '/api/spot/v3/cancel_batch_orders/'
SPOT_ORDERS_LIST = '/api/spot/v3/orders'
SPOT_ORDERS_PENDING = '/api/spot/v3/orders_pending'
SPOT_ORDER_INFO = '/api/spot/v3/orders/'
SPOT_FILLS = '/api/spot/v3/fills'
SPOT_ORDER_ALGO = '/api/spot/v3/order_algo'
SPOT_CANCEL_ALGOS = '/api/spot/v3/cancel_batch_algos'
SPOT_TRADE_FEE = '/api/spot/v3/trade_fee'
SPOT_GET_ORDER_ALGOS = '/api/spot/v3/algo'
SPOT_COIN_INFO = '/api/spot/v3/instruments'
SPOT_DEPTH = '/api/spot/v3/instruments/'
SPOT_TICKER = '/api/spot/v3/instruments/ticker'
SPOT_SPECIFIC_TICKER = '/api/spot/v3/instruments/'
SPOT_DEAL = '/api/spot/v3/instruments/'
SPOT_KLINE = '/api/spot/v3/instruments/'

# lever
LEVER_ACCOUNT = '/api/margin/v3/accounts'
LEVER_COIN_ACCOUNT = '/api/margin/v3/accounts/'
LEVER_LEDGER_RECORD = '/api/margin/v3/accounts/'
LEVER_CONFIG = '/api/margin/v3/accounts/availability'
LEVER_SPECIFIC_CONFIG = '/api/margin/v3/accounts/'
LEVER_BORROW_RECORD = '/api/margin/v3/accounts/borrowed'
LEVER_SPECIFIC_BORROW_RECORD = '/api/margin/v3/accounts/'
LEVER_BORROW_COIN = '/api/margin/v3/accounts/borrow'
LEVER_REPAYMENT_COIN = '/api/margin/v3/accounts/repayment'
LEVER_ORDER = '/api/margin/v3/orders'
LEVER_ORDERS = '/api/margin/v3/batch_orders'
LEVER_REVOKE_ORDER = '/api/margin/v3/cancel_orders/'
LEVER_REVOKE_ORDERS = '/api/margin/v3/cancel_batch_orders'
LEVER_ORDER_LIST = '/api/margin/v3/orders'
LEVEL_ORDERS_PENDING = '/api/margin/v3/orders_pending'
LEVER_ORDER_INFO = '/api/margin/v3/orders/'
LEVER_FILLS = '/api/margin/v3/fills'
LEVER_MARK_PRICE = '/api/margin/v3/instruments/'

# future
FUTURE_POSITION = '/api/futures/v3/position'
FUTURE_SPECIFIC_POSITION = '/api/futures/v3/'
FUTURE_ACCOUNTS = '/api/futures/v3/accounts'
FUTURE_COIN_ACCOUNT = '/api/futures/v3/accounts/'
FUTURE_GET_LEVERAGE = '/api/futures/v3/accounts/'
FUTURE_SET_LEVERAGE = '/api/futures/v3/accounts/'
FUTURE_LEDGER = '/api/futures/v3/accounts/'
FUTURE_ORDER = '/api/futures/v3/order'
FUTURE_ORDERS = '/api/futures/v3/orders'
FUTURE_REVOKE_ORDER = '/api/futures/v3/cancel_order/'
FUTURE_REVOKE_ORDERS = '/api/futures/v3/cancel_batch_orders/'
FUTURE_ORDERS_LIST = '/api/futures/v3/orders/'
FUTURE_ORDER_INFO = '/api/futures/v3/orders/'
FUTURE_FILLS = '/api/futures/v3/fills'
FUTURE_MARGIN_MODE = '/api/futures/v3/accounts/margin_mode'
FUTURE_CLOSE_POSITION = '/api/futures/v3/close_position'
FUTURE_CANCEL_ALL = '/api/futures/v3/cancel_all'
HOLD_AMOUNT = '/api/futures/v3/accounts/'
FUTURE_ORDER_ALGO = '/api/futures/v3/order_algo'
FUTURE_CANCEL_ALGOS = '/api/futures/v3/cancel_algos'
FUTURE_GET_ORDER_ALGOS = '/api/futures/v3/order_algo/'
FUTURE_TRADE_FEE = '/api/futures/v3/trade_fee'
FUTURE_PRODUCTS_INFO = '/api/futures/v3/instruments'
FUTURE_DEPTH = '/api/futures/v3/instruments/'
FUTURE_TICKER = '/api/futures/v3/instruments/ticker'
FUTURE_SPECIFIC_TICKER = '/api/futures/v3/instruments/'
FUTURE_TRADES = '/api/futures/v3/instruments/'
FUTURE_KLINE = '/api/futures/v3/instruments/'
FUTURE_INDEX = '/api/futures/v3/instruments/'
FUTURE_RATE = '/api/futures/v3/rate'
FUTURE_ESTIMAT_PRICE = '/api/futures/v3/instruments/'
FUTURE_HOLDS = '/api/futures/v3/instruments/'
FUTURE_LIMIT = '/api/futures/v3/instruments/'
FUTURE_MARK = '/api/futures/v3/instruments/'
FUTURE_LIQUIDATION = '/api/futures/v3/instruments/'

# swap
SWAP_POSITIONS = '/api/swap/v3/position'
SWAP_POSITION = '/api/swap/v3/'
SWAP_ACCOUNTS = '/api/swap/v3/accounts'
SWAP_ORDER_ALGO = '/api/swap/v3/order_algo'
SWAP_CANCEL_ALGOS = '/api/swap/v3/cancel_algos'
SWAP_GET_ORDER_ALGOS = '/api/swap/v3/order_algo/'
SWAP_GET_TRADE_FEE = '/api/swap/v3/trade_fee'
SWAP_ACCOUNT = '/api/swap/v3/'
SWAP_ORDER = '/api/swap/v3/order'
SWAP_ORDERS = '/api/swap/v3/orders'
SWAP_CANCEL_ORDER = '/api/swap/v3/cancel_order/'
SWAP_CANCEL_ORDERS = '/api/swap/v3/cancel_batch_orders/'
SWAP_FILLS = '/api/swap/v3/fills'
SWAP_INSTRUMENTS = '/api/swap/v3/instruments'
SWAP_TICKETS = '/api/swap/v3/instruments/ticker'
SWAP_RATE = '/api/swap/v3/rate'

# index
INDEX_GET_CONSTITUENTS = '/api/index/v3/'

# option
OPTION_ORDER = '/api/option/v3/order'
OPTION_ORDERS = '/api/option/v3/orders'
OPTION_CANCEL_ORDER = '/api/option/v3/cancel_order/'
OPTION_CANCEL_ORDERS = '/api/option/v3/cancel_batch_orders/'
OPTION_AMEND_ORDER = '/api/option/v3/amend_order/'
OPTION_AMEND_BATCH_ORDERS ='/api/option/v3/amend_batch_orders/'
OPTION_FILLS = '/api/option/v3/fills/'
OPTION_POSITION = '/api/option/v3/'
OPTION_ACCOUNT = '/api/option/v3/accounts/'
OPTION_TRADE_FEE = '/api/option/v3/trade_fee'
OPTION_INDEX = '/api/option/v3/underlying'
OPTION_INSTRUMENTS = '/api/option/v3/instruments/'
