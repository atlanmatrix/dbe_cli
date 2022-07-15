"""
Configure of DBE-cli
"""

# """
# System mode can be lazy 'mode' or 'realtime' mode.
# Lazy mode:
#     Lazy mode can provide high performance if you read more and write less.
#     System will read data from cache(if exists). You can partial flush cache
#     by execute `flush` command.
#     If target not found in cache, it will work like in realtime mode but cache
#     returned data for next use.
# Realtime mode:
#     System will always read data from target third-part system(by hook) and
#     will never use cache.
# """
MODE = 'lazy'

# """
# Path of cache file.
# It will be automatically loaded while a new client created, and be updated
# while client exit.
# """
CACHE_FILE = '/tmp/tfs.cache'