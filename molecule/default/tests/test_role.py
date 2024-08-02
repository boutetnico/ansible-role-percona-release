import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("percona-release"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "name",
    [
        ("ps-8x-innovation"),
    ],
)
def test_repositories(host, name):
    command = "/usr/bin/percona-release show"
    repositories_list = host.check_output(command)
    assert name in repositories_list
