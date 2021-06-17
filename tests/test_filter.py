"""Test file for filter File"""
from rawsec_cli.filter import filter_projects

rawsec_projects = [
    {
        "name": "test",
        "description": "a",
        "language": "Python",
        "price": "Paid",
        "online": "True",
        "blackarch": "test",
    },
    {
        "name": "test2",
        "description": "ab",
        "language": "Go",
        "price": "Free",
        "online": "False",
        "blackarch": "test",
    },
]


def test_filter_projects():
    """test filter_projects function"""
    projects = filter_projects(
        rawsec_projects,
        lang="Python",
        paid=True,
        online=True,
        blackarch=True,
    )
    assert projects == [rawsec_projects[0]]

    projects = filter_projects(
        rawsec_projects,
        lang="Go",
        free=True,
        offline=True,
        blackarch=True,
    )
    assert projects == [rawsec_projects[1]]
