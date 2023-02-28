import pandas as pd
import numpy as np
import json
import requests


def select_parts(df):

    # create the submission dictionary
    submission = {}

    submission["partGuids"] = []
    submission["supplierParts"] = {}

    # iterate over each row in the dataframe
    for _, row in df.iterrows():
        part_guid = row["Part_GUID"]
        supplier_guid = row["Supplier_GUID"]

        # add the part GUID to the list of part GUIDs
        submission["partGuids"].append(part_guid)

        # add the part to the supplier's list of parts
        if supplier_guid in submission["supplierParts"]:
            supplier_parts = submission["supplierParts"][supplier_guid]
            supplier_parts.append({"partGuid": part_guid, "isArticle": False})
            submission["supplierParts"][supplier_guid] = supplier_parts
        else:
            submission["supplierParts"][supplier_guid] = [{"partGuid": part_guid, "isArticle": False}]

    # update each part in the supplier's list of parts with "isArticle"
    for supplier_guid in submission["supplierParts"]:
        supplier_parts = submission["supplierParts"][supplier_guid]
        for i in range(len(supplier_parts)):
            supplier_parts[i]["isArticle"] = False

    return submission