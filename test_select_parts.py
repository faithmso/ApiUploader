from unittest import TestCase
from select_parts import select_parts
import pandas as pd


class TestSelectParts(TestCase):
    def test_select_parts(self):
        # create a sample DataFrame
        df1 = pd.DataFrame({
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
        actual = select_parts(df1)

        # compare the actual output to the expected output
        assert actual == expected

if __name__ == "__main__":
    TestSelectParts().test_select_parts()

