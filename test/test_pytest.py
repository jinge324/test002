import pytest


if __name__ == "__main__":
    # pytest.main(['../test_case/test_fee.py', '../test_case/test_fee_01.py'])
    # pytest.main(['../test_case'])
    pytest.main(['../test_case/test_fee.py', '--html=../report/report.html', '--alluredir', '../report/reportallure'])