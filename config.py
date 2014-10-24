### Settings relating to server identity

# Name of the server
ServerName = 'Multicoin.co'

### Settings relating to server scaling/load
# Share hashes must be below this to be valid shares If dynamic targetting is enabled, this is a minimum
ShareTarget = 0x0000ffff00000000000000000000000000000000000000000000000000000000 #Scrypt

# Automatically adjust targets per username 0 = disabled 1 = arbitrary targets 2 = power of two difficulties (zero bit counts)
DynamicTargetting = 3

# How many shares per minute to try to achieve on average
DynamicTargetGoal = 8


# Number of seconds hashrate is measured over
DynamicTargetWindow = 300

# Minimum and maximum of merkle roots to keep queued
WorkQueueSizeRegular = (0x100, 0x1000)
WorkQueueSizeClear = (0x1000, 0x2000)

# Minimum and maximum of BLANK merkle roots to keep queued, one height up
# (used for longpolls)
WorkQueueSizeLongpoll = (0x1000, 0x2000)

# How long to wait between getmemorypool updates normally
MinimumTxnUpdateWait = 5

# How long to wait between retries if getmemorypool fails
TxnUpdateRetryWait = 1

# How long to sleep in idle loops (temporary!)
IdleSleepTime = 0.1

### Settings relating to reward generation

# Address to generate rewards to
TrackerAddr = ''

# Coinbaser command to control reward delegation
# NOTE: This example donates 1% of block rewards to Luke-Jr for Eloipool development
#CoinbaserCmd = 'echo -e "1\\n$((%d / 100))\\n1579aXhdwvKZEMrAKoCZhzGuqMa8EonuXU"'

### Settings relating to upstream data providers

# JSON-RPC server for getmemorypool
UpstreamURI = 'http://username:password@localhost:8002'

# Set to True if you want shares meeting the upstream target to wait for a
# response from the upstream server before logging them. Otherwise, for such
# shares, upstreamResult will always be True and upstreamRejectReason will
# always be None. Note that enabling this may cause shares to be logged out of
# order, or with the wrong timestamp (if your share logger uses the log-time
# rather than share-time).
DelayLogForUpstream = False

# Bitcoin p2p server for announcing blocks found
UpstreamBitcoindNode = ('127.0.0.1', 9333)

# Network ID for the primary blockchain

# Litecoin: b'\xFB\xC0\xB6\xDB'         # 0xfb, 0xc0, 0xb6, 0xdb
UpstreamNetworkId = b'\xFB\xC0\xB6\xDB'

# Secret username allowed to use setworkaux
SecretUser = "ssecreteloipool"

# URI to send gotwork with info for every share submission
GotWorkURI = 'http://mergedproxyuser:mergedproxypass@127.0.0.1:8331/'

# Share hashes must be below this to be submitted to gotwork
GotWorkTarget = 0x0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

# Aim to produce blocks with transaction counts that are a power of two
# This helps avoid any chance of someone abusing CVE-2012-2459 with them
# 1 = cut out feeless transactions; 2 = cut out even fee-included transactions (if possible)
POT = 0

# Avoid mining feeless transactions except to satisfy POT
# Note this only works if POT is in fact enabled in the first place
Greedy = False

### Settings relating to network services

# Addresses to listen on for JSON-RPC getwork server
# Note that Eloipool only supports IPv6 sockets, and if you want to bind to an
# IPv4 address you will need to prepend it with ::ffff: eg ::ffff:192.168.1.2
JSONRPCAddresses = (
	('', 1000),
)

StratumAddresses = (
	('', 2000),
)

# Addresses that are allowed to "spoof" from address with the X-Forwarded-For header
TrustedForwarders = ('::ffff:127.0.0.1',)


# Logging of shares:
ShareLogging = (
	{
		'type': 'sql',
		'engine': 'mysql',
		'dbopts': {
			'host': 'localhost',
			'db': 'multicoin',
			'user': 'root',
		},
		'statement': "insert into shares (user, ip, oresult, uresult, reason, solution, difficulty, time, coin, blkheight) values ({username}, {remoteHost}, {ourResult}, {upstreamResult}, {reason}, unhex({solution}), {difficulty}, {time}, {coin}, {blkheight})",
	},
)

# Authentication
# There currently are 2 modules.
# - allowall will allow every username/password combination
# - simplefile will use the username/passwords from a file, which contains username<tab>password\n with no \n on the last line.
Authentication = (
	{
		'module': 'allowall',
	},
)

