from datetime import datetime


def module_and_user_info():
    """
    Prepares part of the final payload.

    Arg 1: module name
    Arg 2: module version
    Arg 3: user email (taken from class variable)
    Arg 4: shareable (bool: taken from class variable)

    return: dict "declarationInfo"

    Notes: This function should work for REACH and ROHS.

     "declarationInfo": {
    "moduleGuid": "0f810f60-8cac-11e8-acad-d9542266e7fe",
    "declarationName": "EU REACH SVHC",
    "responseDateUtc": "2022-11-28T13:40:03.801Z",
    "isManualOverride": True,
    "bypassGating": False,
    "bypassArticleConfigs": True,
    "contactEmail": "nikolas.guttler@assentcompliance.com",
    "substanceListVersionGuid": "556a4081-ed3d-4b0c-8c54-d02acd4cd625",
    "dslGuid": "867eb651-20c0-4e0d-8783-c90c0856a732",
    #"sendoutToken": None,
    "isShareable": True,
    #"isAssentDeclaration": False,
    "surveyVersion": 2,
    "moduleVersion": 15,
    #"supplierOrgViewWid": 0,
    #"dataSource": None,
    #"evaluationOutcome": None,
    #"evidenceDate": None,
    #"evidenceType": None,
    #"statusSource": None,
    #"proprietaryLimitPercent": 10,
    #"rollupWeightTolerance": 0,
    ######### Not important ################
    # "previousSubmissionData": {
    #   "contactEmail": "",
    #   "declaredDate": "2022-11-28T13:40:03.801Z",
    #   "isRoot": False
    # }
  },

     p1 :moduleGuid(string)
     p2 : declaration name (string)
     p3 : Datetime (datetime)
     p4 : isManualOverride (bool)
     p5 : bypassGating (bool)
     p6 : bypassArticleConfigs (bool)
     p7 : contactEmail (string)
     p8 : substanceListVersionGuid (string)
     p9 : dslGuid (string)
     p10 : isShareable (bool)
     p11 : surveyVersion (int)
     p12 : moduleVersion (int)

    """

    # providing accurate time now
    current_time = datetime.now()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    declarationInfo = {}
    declarationInfo["moduleGuid"] = "moduleGuid"
    declarationInfo["declarationName"] = "Reach SVHC"
    declarationInfo["responseDateUtc"] = current_time
    declarationInfo["isManualOverride"] = True
    declarationInfo["bypassGating"] = False
    declarationInfo["bypassArticleConfigs"] = True
    declarationInfo["contactEmail"] = input("Please enter your email address: ")
    declarationInfo["substanceListVersionGuid"] = "substanceListVersionGuid"
    declarationInfo["dslGuid"] = "dslGuid"
    declarationInfo["isShareable"] = True
    declarationInfo["surveyVersion"] = 2
    declarationInfo["moduleVersion"] = 15

    return declarationInfo


declare1 = module_and_user_info()
print(declare1)
