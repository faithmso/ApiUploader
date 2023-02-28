import pandas as pd
from unittest import TestCase


def test_select_parts(TestCase):
    # create a sample DataFrame
    df = pd.DataFrame({
        "Supplier_GUID": ["S1", "S2", "S1"],
        "Part_GUID": ["P1", "P2", "P3"]
    })

    # create the expected output
    expected = {
        "partGuids": ["P1", "P2", "P3"],
        "supplierParts": {
            "S1": [
                {"partGuid": "P1", "isArticle": False},
                {"partGuid": "P3", "isArticle": False}
            ],
            "S2": [
                {"partGuid": "P2", "isArticle": False}
            ]
        }
    }

    # call the function to test
    actual = select_parts(df)

    # compare the actual output to the expected output
    assert actual == expected


def select_parts(df):
    submission = {}
    submission["partGuids"] = []
    submission["supplierParts"] = {}

    for _, row in df.iterrows():
        part_guid = row["Part_GUID"]
        supplier_guid = row["Supplier_GUID"]

        submission["partGuids"].append(part_guid)

        if supplier_guid in submission["supplierParts"]:
            supplier_parts = submission["supplierParts"][supplier_guid]
            supplier_parts.append({"partGuid": part_guid, "isArticle": False})
            submission["supplierParts"][supplier_guid] = supplier_parts
        else:
            submission["supplierParts"][supplier_guid] = [{"partGuid": part_guid, "isArticle": False}]

    return submission


if __name__ == "__main__":

    test_select_parts()





