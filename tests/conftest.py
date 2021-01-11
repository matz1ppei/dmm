import os
import pytest
from dmm import DMM


def pytest_addoption(parser):
    parser.addoption('--local', action='store_true',
                     help='get environment variables by .env')
    parser.addoption('--apiid', action='store',
                     help='APIID: DMM API ID')
    parser.addoption('--affiliateid', action='store',
                     help='AFFILIATEID: DMM Affiliate ID')


@pytest.fixture(scope='session')
def local(pytestconfig):
    return pytestconfig.option.local


@pytest.fixture(scope='session')
def apiid(pytestconfig):
    return pytestconfig.option.apiid


@pytest.fixture(scope='session')
def affiliateid(pytestconfig):
    return pytestconfig.option.affiliateid


@pytest.fixture(scope='session')
def client(local, apiid, affiliateid):
    api_id = os.environ['API_ID'] if local else apiid
    affiliate_id = os.environ['AFFILIATE_ID'] if local else affiliateid
    return DMM(api_id, affiliate_id)
