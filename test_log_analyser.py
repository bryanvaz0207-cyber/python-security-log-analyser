from log_analyser import count_logins


def test_login_counts():
    line_1 = "2026-09-01 09:10 alice SUCCESS 192.168.1.10"
    line_2 = "2026-09-01 09:12 bob FAILED 10.0.0.4"
    line_3 = "2026-09-01 09:13 bob FAILED 10.0.0.4"

    lines = [line_1, line_2, line_3]

    success, failed, failed_ips, invalid_lines = count_logins(lines)

    assert success == 1
    assert failed == 2
    assert failed_ips["10.0.0.4"] == 2
    assert invalid_lines == 0