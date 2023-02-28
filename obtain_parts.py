import pandas as pd
import numpy as np
import json
import requests

def select_parts():
    """
    Provides info about which parts are going to be submitted for
    Arg 1: PartGUID(s) (list)

    return: dict "submission"

    How the "submission" dict looks like in the preview:

    ################# Part information ##############
    "submission": {
      #"parts": None,
      "partGuids": [
        "7a489293-abd6-432e-a710-310d8c2ac235", # list of all PartGUIDs in this submission
      ],
      "supplierParts": {
        "5b013261-cebb-43bc-9d30-5a40456862aa" # dictionary key for each SupplierGUID in this submission (one dictionary key if only one supplier)
        : [ # list of parts per supplier
          { # dictionary for each part
            "partGuid":
            "7a489293-abd6-432e-a710-310d8c2ac235",
            # "partNumber": "0003-034-000",
            # "supplierPartNumber": "0003-034-000",
            # "containedIn": "",
            "isArticle": False,
            #"isFSD": False,
            #"lastDeclaredDate": "",
            #"unitOfMeasurement": "",
            #"weight": 0
          },
        ]
      }

    """
    # TODO: WORK ON DATAFRAME

    # create a pandas data frame from a csv file
    df = pd.read_csv("C:/Users/FaithMu/Downloads/test.csv", dtype=str)
    # TODO: You will get the dataframe as an input argument. The dataframe will contain two columns: "Supplier_GUID" and "Part_GUID". Make sure to rework the function to work with this input.

    # create the submission dictionary
    submission = {}
    submission["partGuids"] = []
    submission["supplierParts"] = {}

    # filter dataframe to get the partGuid and supplierGuid
    for part in df['partGuid'].unique():
        df_filtered = df[df['partGuid'] == part]
        supplierGuid = df_filtered['supplierGuid'].unique()[0]
        submission["partGuids"].append(part)
        if supplierGuid not in submission["supplierParts"]:
            submission["supplierParts"][supplierGuid] = []
        part = {}
        part["partGuid"] = part
        part["isArticle"] = False
        submission["supplierParts"][supplierGuid].append(part)

    print(submission)
    return submission


select_parts()