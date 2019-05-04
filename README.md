# PacketTotal SDK

The PacketTotal SDK is a collection of modules that provide access to PacketTotal's REST API interface.

The official API documentation can be found [here](https://www.packettotal.com/api-docs/)

## Getting Started

### Prerequisites

- Python 3.5 or higher.

### Installation

- `pip install -r requirements.txt`
- `python setup.py install`

### Optional Configurations

If you need to override the API base URL or version you can do so with the below environmental variables.

```bash
export PACKETTOTAL_API_BASE_URL="https://api.packettotal.com/"
export PACKETTOTAL_API_VERSION_STRING="v1"
```

## Request an API key

You can request an API key [here](https://packettotal.com/api.html).

## Basic Usage

The SDK ships with a library for interacting with the PacketTotal API, as well as a [script](/scripts) to provide easy access to this library.


### Retrieving API Usage Information

##### Via packettotal commandline

```bash
packettotal usage
```


##### Via packettotal_api module
```python
from packettotal_sdk import packettotal_api

api = packettotal_api.PacketTotalApi('my-api-key')

response = api.usage()

print(response.status_code, response.json())

```

### Analyze a PCAP file

##### Via packettotal commandline

```bash
packettotal analyze --path /path/to/my/pcap.pcap --name my-publicly-shared-pcap-name
```


##### Via packettotal_api module
```python
from packettotal_sdk import packettotal_api

api = packettotal_api.PacketTotalApi('my-api-key')

response = api.analyze(open('/path/to/my/pcap.pcap', 'rb'), pcap_name='my-publicly-shared-pcap-name')

print(response.status_code, response.json())

```

### Run a search

##### Via packettotal commandline

```bash
packettotal search --query google.com
```


##### Via packettotal_api module
```python
from packettotal_sdk import packettotal_api

api = packettotal_api.PacketTotalApi('my-api-key')

response = api.search('google.com')

print(response.status_code, response.json())

```

## Documentation

Static HTML version of the SDK's API Module can be found [here](https://packettotal.github.io/PacketTotal-SDK/packettotal_sdk/packettotal_sdk.html#module-packettotal_sdk.packettotal_api).

The official REST API documentation is available [here](https://www.packettotal.com/api-docs/)

Or ...

Build Sphinx Docs with search by following the seps below:

1. From the root directory run `make html` or `make.bat` if on Windows.
2. Navigate to `_build/html/index.html` in a web-browser.