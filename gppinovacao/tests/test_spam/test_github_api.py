from unittest.mock import Mock

import pytest

# from gppinovacao import github_api


# def test_buscar_avatar(avatar_url):
#    url = github_api.buscar_avatar('ogpgit')
#    assert avatar_url == url


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/67315703?v=4'
    resp_mock.json.return_value = {
        'login': 'ogpgit', 'id': 67315703, 'node_id': 'MDQ6VXNlcjY3MzE1NzAz',
        'avatar_url': url
    }
    get_mock = mocker.patch('gppinovacao.github_api.requests.get')
    get_mock.return_value = resp_mock
    # github_api.requests.get = Mock(return_value=resp_mock)
    return url


# def test_buscar_avatar_integracao():
#    url = github_api.buscar_avatar('ogpgit')
#    assert 'https://avatars1.githubusercontent.com/u/67315703?v=4' == url
