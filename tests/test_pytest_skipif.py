import pytest


SYSTEM_VERSION = 'v1.2.0'


@pytest.mark.skipif(
        SYSTEM_VERSION == 'v1.3.0',
        reason='Тестне может быть запущен на версии системы v1.3.0'
    )
def test_system_version_valid():
    ...


@pytest.mark.skipif(
        SYSTEM_VERSION == 'v1.2.0',
        reason='Тестне может быть запущен на версии системы v1.2.0'
    )
def test_system_version_invalid():
    ...
