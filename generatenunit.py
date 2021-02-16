from runeatest import nunitresults
from runeatest import pysparkconnect
from runeatest import utils
from runeatest import testreporter
import pytest
import json
from datetime import datetime


def test_convert_to_nunit_results_format(mocker):
    x = '{"tags": {"opId": "ServerBackend-f421e441fa310430","browserUserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","orgId": "1009391617598028","userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","clusterId": "0216-124733-lone970","user": "eter.natus@galar.com","principalIdpObjectId": "71b45910-e7b4-44d8-82f7-bf6fac4630d0","browserHostName": "uksouth.azuredatabricks.net","parentOpId": "RPCClient-bb9b9591c29c01f7","jettyRpcType": "InternalDriverBackendMessages$DriverBackendRequest"},"extraContext":{"notebook_path":"/Users/lorem.ipsum@fake.io/runeatest"}}'
    context = json.loads(x)
    mocker.patch("runeatest.pysparkconnect.get_context", return_value=context)
    t = ("2020-9-13", "13:20:16")
    mocker.patch("runeatest.utils.get_date_and_time", return_value=t)
    results = []
    results.append(testreporter.add_testcase("test name", True))
    results.append(testreporter.add_testcase("test name 2", True))
    actual = nunitresults.convert_to_nunit_results_format(results)
    now = datetime.now()
    now_date = str(now.year) + str(now.month) + str(now.day)
    now_time = str(now.hour) + str(now.minute) + str(now.second)
    fname = "{thisdate}_{thistime}_nunit_test_results.xml".format(
        thisdate=now_date, thistime=now_time
    )
    f = open(fname, "w")
    f.write(actual)
    f.close()
