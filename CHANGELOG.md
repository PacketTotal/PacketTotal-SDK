## 0.1.0

- API Wrapper via the `packettotal_sdk/packettotal_api.py` wrapper module
- packettotal cmdline added

## 0.2.0
- Bug fixes:
  - `packettotal_sdk/packettotal_api.PacketTotalAPI.deep_search` now returns a proper `request.Response` obj
 
- Added `packettotal_sdk/packettotal_api.search_tools` module
  - provides the ability to search by a list of IOCs
