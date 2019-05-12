```
usage: packettotal [-h] [--query QUERY] [--pcap-id PCAP_ID]
                   [--search-id SEARCH_ID] [--path PCAP_PATH]
                   [--ioc-path IOC_PATH] [--skip-warnings] [--name PCAP_NAME]
                   [--sources PCAP_SOURCES [PCAP_SOURCES ...]]
                   [--output OUTPUT]
                   mode

A simple command-line utility for interacting with the PacketTotal API.

positional arguments:
  mode                  The mode to invoke [ analyze|search|search_by_pcap|ioc
                        _search|deep_search|deep_search_results|info|analysis|
                        download|similar|]

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY         A search query
  --pcap-id PCAP_ID     The MD5 hash of the pcap on PacketTotal.
  --search-id SEARCH_ID
                        The search identifier corresponding to a deep search
                        task
  --path PCAP_PATH      The path to the pcap file you wish to analyze.
  --ioc-path IOC_PATH   The path to a newline delimited text file containing
                        search terms.
  --skip-warnings       Skip pcap analyze warning prompt
  --name PCAP_NAME      The optional name associated with the pcap analysis.
  --sources PCAP_SOURCES [PCAP_SOURCES ...]
                        URLs referencing the original analysis.
  --output OUTPUT       A path to an output file, defaulted to stdout if not
                        included.
```