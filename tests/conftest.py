import os
import pytest
from dmm import DMM


@pytest.fixture(scope='session')
def client():
    api_id = os.environ['API_ID']
    affiliate_id = os.environ['AFFILIATE_ID']
    return DMM(api_id, affiliate_id)
