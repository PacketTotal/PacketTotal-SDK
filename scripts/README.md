```
usage: packettotal [-h] [--query QUERY] [--pcap-id PCAP_ID]
                   [--search-id SEARCH_ID] [--path PCAP_PATH]
                   [--name PCAP_NAME]
                   [--sources PCAP_SOURCES [PCAP_SOURCES ...]]
                   [--output OUTPUT]
                   mode

A simple command-line utility for interacting with the PacketTotal API.

positional arguments:
  mode                  The mode to invoke [ analyze|search|deep_search_create
                        |deep_search_get|info|analysis|download|similar ]

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY         Your search query
  --pcap-id PCAP_ID     The MD5 hash of some PCAP file.
  --search-id SEARCH_ID
                        The search identifier corresponding to a deep search
                        task
  --path PCAP_PATH      The path to the pcap file you wish to analyze.
  --name PCAP_NAME      The optional name to assign your pcap analysis.
  --sources PCAP_SOURCES [PCAP_SOURCES ...]
                        Optionally supply URLs to blog posts, articles, or anything else to be included in the References view of your PCAP. Useful for attributing the PCAP to your organization, or providing additional context for the PCAP.
  --output OUTPUT       A path to an output file, defaulted to stdout if
                        not included.
```