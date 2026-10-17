from httpie import __version__
from httpie.version_info import version_tuple


def test_feat_2_version_tuple_parses_release():
    assert version_tuple('3.2.4') == (3, 2, 4)


def test_feat_2_version_tuple_matches_package_version():
    assert version_tuple() == tuple(int(p) for p in __version__.split('.'))
