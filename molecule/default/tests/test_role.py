import pytest


@pytest.mark.parametrize("name", ["gnupg", "lsb-release"])
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_percona_release_package_installed(host):
    package = host.package("percona-release")
    assert package.is_installed


def test_percona_release_binary_exists(host):
    """Test that percona-release binary exists and is executable."""
    f = host.file("/usr/bin/percona-release")
    assert f.exists
    assert f.is_file
    assert f.mode & 0o111  # Check executable bit


def test_percona_release_show_command(host):
    """Test that percona-release show command works."""
    cmd = host.run("/usr/bin/percona-release show")
    assert cmd.rc == 0


@pytest.mark.parametrize(
    "name",
    [
        ("ps-8x-innovation"),
    ],
)
def test_repositories_enabled(host, name):
    command = "/usr/bin/percona-release show"
    repositories_list = host.check_output(command)
    assert name in repositories_list
    # Verify it's enabled (has asterisk or enabled marker)
    assert "release" in repositories_list
