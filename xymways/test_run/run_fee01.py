import pytest
import datetime

if __name__ == "__main__":
    pytest.main(['../test_case/', '--html=../report/report.html', '--alluredir', '../report/reportallure'])
    # pytest.main(['../test_case/test_order.py', '--html=../report/report.html'])
