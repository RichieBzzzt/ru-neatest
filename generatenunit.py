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
    now_time = (
        str(now.hour)
        + str(now.minute)
        + str(now.second)
        + str(now.second)
        + str(now.microsecond)
    )
    fname = "{thisdate}_{thistime}_nunit_test_results.xml".format(
        thisdate=now_date, thistime=now_time
    )
    f = open(fname, "w")
    f.write(actual)
    f.close()


def test_convert_to_nunit_results_format_multiple_results(mocker):
    x = '{"tags": {"opId": "ServerBackend-f421e441fa310430","browserUserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","orgId": "1009391617598028","userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","clusterId": "0216-124733-lone970","user": "eter.natus@galar.com","principalIdpObjectId": "71b45910-e7b4-44d8-82f7-bf6fac4630d0","browserHostName": "uksouth.azuredatabricks.net","parentOpId": "RPCClient-bb9b9591c29c01f7","jettyRpcType": "InternalDriverBackendMessages$DriverBackendRequest"},"extraContext":{"notebook_path":"/Users/lorem.ipsum@fake.io/runeatest"}}'
    context = json.loads(x)
    mocker.patch("runeatest.pysparkconnect.get_context", return_value=context)
    t = ("2020-9-13", "13:20:16")
    mocker.patch("runeatest.utils.get_date_and_time", return_value=t)
    results = []
    results.append(testreporter.add_testcase("test name 3", True))
    results.append(testreporter.add_testcase("test name 4", True))
    y = '{"tags": {"opId": "ServerBackend-f421e441fa310430","browserUserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","orgId": "1009391617598028","userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","clusterId": "0216-124733-lone970","user": "eter.natus@galar.com","principalIdpObjectId": "71b45910-e7b4-44d8-82f7-bf6fac4630d0","browserHostName": "uksouth.azuredatabricks.net","parentOpId": "RPCClient-bb9b9591c29c01f7","jettyRpcType": "InternalDriverBackendMessages$DriverBackendRequest"},"extraContext":{"notebook_path":"/Users/lorem.ipsum@fake.io/runeatest/another/notebook"}}'
    context = json.loads(y)
    mocker.patch("runeatest.pysparkconnect.get_context", return_value=context)
    results2 = []
    results2.append(testreporter.add_testcase("test name 5", True))
    results2.append(testreporter.add_testcase("test name 6", True))

    results3 = results + results2
    actual = nunitresults.convert_to_nunit_results_format(results3)

    now = datetime.now()
    now_date = str(now.year) + str(now.month) + str(now.day)
    now_time = (
        str(now.hour)
        + str(now.minute)
        + str(now.second)
        + str(now.second)
        + str(now.microsecond)
    )
    fname = "{thisdate}_{thistime}_nunit_test_results.xml".format(
        thisdate=now_date, thistime=now_time
    )
    f = open(fname, "w")
    f.write(actual)
    f.close()


def test_convert_to_nunit_results_format_multiple_results_nunit(mocker):
    x = '{"tags": {"opId": "ServerBackend-f421e441fa310430","browserUserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","orgId": "1009391617598028","userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","clusterId": "0216-124733-lone970","user": "eter.natus@galar.com","principalIdpObjectId": "71b45910-e7b4-44d8-82f7-bf6fac4630d0","browserHostName": "uksouth.azuredatabricks.net","parentOpId": "RPCClient-bb9b9591c29c01f7","jettyRpcType": "InternalDriverBackendMessages$DriverBackendRequest"},"extraContext":{"notebook_path":"/Users/lorem.ipsum@fake.io/runeatest"}}'
    context = json.loads(x)
    mocker.patch("runeatest.pysparkconnect.get_context", return_value=context)
    t = ("2020-9-13", "13:20:16")
    mocker.patch("runeatest.utils.get_date_and_time", return_value=t)
    results = []
    results.append(testreporter.add_testcase("test name 3", True))
    results.append(testreporter.add_testcase("test name 4", True))
    results2 = []
    results2.append(testreporter.add_testcase("test name 5", True))
    results2.append(testreporter.add_testcase("test name 6", True))

    context = pysparkconnect.get_context()
    header = nunitresults.get_nunit_header(results, context)
    suite = nunitresults.get_test_suite_results(results, context)
    test_cases = nunitresults.get_test_case_results(results)
    test_cases += nunitresults.get_test_case_results(results)
    footer = nunitresults.get_nunit_footer()
    str_test_cases = "\n".join(test_cases)
    actual = header + "\n" + suite + "\n" + str_test_cases + "\n" + footer

    now = datetime.now()
    now_date = str(now.year) + str(now.month) + str(now.day)
    now_time = (
        str(now.hour)
        + str(now.minute)
        + str(now.second)
        + str(now.second)
        + str(now.microsecond)
    )
    fname = "{thisdate}_{thistime}_nunit_test_results.xml".format(
        thisdate=now_date, thistime=now_time
    )
    f = open(fname, "w")
    f.write(actual)
    f.close()


def test_convert_to_nunit_results_format_multiple_results(mocker):
    x = '{"tags": {"opId": "ServerBackend-f421e441fa310430","browserUserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","orgId": "1009391617598028","userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","clusterId": "0216-124733-lone970","user": "eter.natus@galar.com","principalIdpObjectId": "71b45910-e7b4-44d8-82f7-bf6fac4630d0","browserHostName": "uksouth.azuredatabricks.net","parentOpId": "RPCClient-bb9b9591c29c01f7","jettyRpcType": "InternalDriverBackendMessages$DriverBackendRequest"},"extraContext":{"notebook_path":"/Users/lorem.ipsum@fake.io/runeatest"}}'
    context = json.loads(x)
    mocker.patch("runeatest.pysparkconnect.get_context", return_value=context)
    t = ("2020-9-13", "13:20:16")
    mocker.patch("runeatest.utils.get_date_and_time", return_value=t)
    results = []
    results.append(
        testreporter.add_testcase(
            "test name fail 1",
            False,
            "this test is described here",
            "but the test has sadly failed",
        )
    )
    results.append(
        testreporter.add_testcase(
            "test name fail 2",
            False,
            "this test is intending to do something",
            "but the test failed",
        )
    )
    y = '{"tags": {"opId": "ServerBackend-f421e441fa310430","browserUserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","orgId": "1009391617598028","userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36","clusterId": "0216-124733-lone970","user": "eter.natus@galar.com","principalIdpObjectId": "71b45910-e7b4-44d8-82f7-bf6fac4630d0","browserHostName": "uksouth.azuredatabricks.net","parentOpId": "RPCClient-bb9b9591c29c01f7","jettyRpcType": "InternalDriverBackendMessages$DriverBackendRequest"},"extraContext":{"notebook_path":"/Users/lorem.ipsum@fake.io/runeatest/another/notebook"}}'
    context = json.loads(y)
    mocker.patch("runeatest.pysparkconnect.get_context", return_value=context)
    results2 = []
    results2.append(
        testreporter.add_testcase(
            "test name fail 3",
            False,
            "another test, another description",
            "and another failure",
        )
    )
    results2.append(
        testreporter.add_testcase(
            "test name fail 4",
            False,
            "another test to fail, another description",
            "and another failure on this build",
        )
    )

    results3 = results + results2
    actual = nunitresults.convert_to_nunit_results_format(results3)

    now = datetime.now()
    now_date = str(now.year) + str(now.month) + str(now.day)
    now_time = (
        str(now.hour)
        + str(now.minute)
        + str(now.second)
        + str(now.second)
        + str(now.microsecond)
    )
    fname = "{thisdate}_{thistime}_nunit_test_results.xml".format(
        thisdate=now_date, thistime=now_time
    )
    f = open(fname, "w")
    f.write(actual)
    f.close()
