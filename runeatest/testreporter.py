from runeatest import pysparkconnect


def add_testcase(name, issuccess, label="", failurereason=""):
    context = pysparkconnect.get_context()
    return {
        "test": name,
        "issuccess": str(issuccess),
        "label": str(label),
        "fullname": (context["extraContext"]["notebook_path"]),
        "result": (get_result(issuccess)),
        "failurereason": str(failurereason),
    }


def get_result(issuccess):
    if issuccess:
        return str("success")
    else:
        return str("failure")
