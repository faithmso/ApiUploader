#################### functions specific to REACH submissions ######################
def product_statement(self, product_statement, is_article):
    """
    Handles selection of SVHC ARE CONTAINED vs. SVHC ARE NOT CONTAINED,
    as well as, optional option Single / Complex article
    Arg 1: product statement
    Arg 2: Single / Complex article

    return: submission products (partial)

    Notes: The key 'isArticle' needs to be optional. If Arg 2 has no value, 'isArticle'
    should not be included. Single article has the value 'True', Complex article 'False'.

      ################ Product statement #####################
      "submissionProducts": [
        {
          #"productCategory": None,
          "productDeclaration": "a788c7e0-8c33-11e8-9c8e-23b0961f5545", ## "statementGuid"
          #"productName": "",
          #"productNumber": "",
          "productDeclarationAdDsl": [],
          #"inProcess": None,
          #"productExemptions": [],
          "substanceInputs": [],
          #"overflowSubstanceInputs": [],
          #"proprietarySubstanceInputs": [],
          #"fileUploads": [],
          "productStatements": [
            {
              "statementGuid": "a788c7e0-8c33-11e8-9c8e-23b0961f5545",
              #"queryListIdentifier": "",
              #"queryListAuthority": None,
              #"statementIdentity": None,
              # "statementAuthority": "IPC",
              # "statementText": "REACH Candidate Substances of Very High Concern ARE CONTAINED in Product Above the Limit per the Definition within REACH",
              # "statementMade": "true"
            }],
    """
# create a list called submission_products which contains a dictionary

    # check whether is article is a single article or mixture (e.g. pure metal spring or adhesive)
    # if it is a single article, then return the product statement
    # if it is a mixture, then return the product statement and the is article
    if is_article == "A single article or mixture (e.g. pure metal spring or adhesive)":
        return {"productStatement": product_statement}
    else:
        return {"productStatement": product_statement, "isArticle": is_article}

    # create a list called submission_products which contains a dictionary



submission_products = [{"productDeclaration": product_statement
                            "productDeclarationAdDsl": [],
                            "substanceInputs": [],
                            "productStatements": [
                                {
                                    "statementGuid": product_statement,
                                }],
                            "isArticle": is_article
                            }]


    if is_article == "A single article or mixture (e.g. pure metal spring or adhesive)":
        return {"productStatement": product_statement}
    else:
        return {"productStatement": product_statement, "isArticle": is_article}

    #create a list called submission_products which contains a dictionary




print(submission_products)
