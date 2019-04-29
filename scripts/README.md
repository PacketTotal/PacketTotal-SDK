```python

usage: packettotal [-h] [--query QUERY] [--pcap-id PCAP_ID]
                   [--search-id SEARCH_ID] [--output OUTPUT]
                   mode

A simple commandline utility for interacting with the PacketTotal API.

positional arguments:
  mode                  The mode to invoke [ analyze|search|deep_search_create
                        |deep_search_get|pcap_info|pcap_analysis|pcap_download
                        |pcap_similar ]

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY         A search query
  --pcap-id PCAP_ID     The MD5 hash of some PCAP file.
  --search-id SEARCH_ID
                        The search identifier corresponding to a deep search
                        task
  --output OUTPUT       A path to an output file, defaulted to standard out if
                        not included.

```