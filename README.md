[![tests](https://github.com/boutetnico/ansible-role-percona-release/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-percona-release/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.percona_release-blue.svg)](https://galaxy.ansible.com/boutetnico/percona_release)

ansible-role-percona-release
============================

This role installs and configures [percona-release](https://docs.percona.com/percona-software-repositories/percona-release.html).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Debian - 13 (Trixie)](https://wiki.debian.org/DebianTrixie)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default       | Choices   | Comments                                          |
|------------------------------|----------|---------------|-----------|---------------------------------------------------|
| percona_release_dependencies | true     | `[gnupg]`     | list      |                                                   |
| percona_release_repositories | true     | `[]`          | list      | Repositories to enable.                           |
| percona_release_version      | true     | `latest`      | string    |                                                   |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-percona-release


Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
