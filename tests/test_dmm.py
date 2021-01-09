import json  # noqa
from dmm import DMM


def test_initialize():
    client = DMM('apiid', 'affiliateid')
    assert client.api_id == 'apiid'
    assert client.affiliate_id == 'affiliateid'


def test_get_items(client):
    items = client.get_items({'site': 'FANZA'})
    assert items.status_code == 200


def test_get_item_by_id_dmm(client):
    item = client.get_item_by_id_dmm('b600ysgk01887')
    assert item.status_code == 200


def test_get_item_by_id_fanza(client):
    item = client.get_item_by_id_fanza('h_1240milk00091')
    assert item.status_code == 200


def test_get_floors(client):
    floors = client.get_floors({})
    assert floors.status_code == 200


def test_get_floors_in_dmm(client):
    floors = client.get_floors_dmm()
    assert floors['code'] == 'DMM.com'


def test_get_floors_in_fanza(client):
    floors = client.get_floors_fanza()
    assert floors['code'] == 'FANZA'


def test_get_actresses(client):
    actresses = client.get_actresses({})
    assert actresses.status_code == 200


def test_get_actress_by_id(client):
    actress = client.get_actress_by_id('1011694')
    assert actress.status_code == 200


def test_get_genres(client):
    genres = client.get_genres({'floor_id': '43'})
    assert genres.status_code == 200


def test_get_makers(client):
    makers = client.get_makers({'floor_id': '43'})
    assert makers.status_code == 200


def test_get_series(client):
    series = client.get_series({'floor_id': '43'})
    assert series.status_code == 200


def test_get_authors(client):
    authors = client.get_authors({'floor_id': '81'})
    assert authors.status_code == 200
