from port_check import *


def test_valid_port_number_zero():
    assert valid_port_number(0) == False


def test_valid_port_number_one():
    assert valid_port_number(1) == True


def test_valid_port_number_max():
    assert valid_port_number(65535) == True


def test_valid_port_number_over():
    assert valid_port_number(65536) == False


def test_get_port_scan_mode_single():
    assert get_port_scan_mode(['123']) == 'single'


def test_get_port_scan_mode_range():
    assert get_port_scan_mode(['123', '234']) == 'range'


def test_get_port_scan_mode_invalid():
    assert get_port_scan_mode(['122', '123', '12']) == 'invalid'


def test_get_port_scan_mode_invalid_order():
    assert get_port_scan_mode(['122', '12']) == 'invalid'
