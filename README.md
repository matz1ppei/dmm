# dmm
[![CircleCI](https://circleci.com/gh/matz1ppei/dmm.svg?style=svg)](https://circleci.com/gh/matz1ppei/dmm)  

DMM API Client for Python

## Dependencies
requests

## Install
```bash
pip intsall dmm
```

## Usage
```python
from dmm import DMM

dmm = DMM('<API_ID>', '<AFFILIATE_ID>')
```

## Function
### get_floors
```python
floors = dmm.get_floors()
```