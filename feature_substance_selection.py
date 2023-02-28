def substance_selection(substance_name, cas, ec, concentration, article_name):

  """
  Handles the "add Substance field". Needs to be able to handle more than one substance added.
  Arg 1: substance name
  Arg 2: substance CAS
  Arg 3: substance EC
  Arg 4: Concentration
  Arg 5: Article Name

  return: submissionProducts (partial)

  Notes:
  The SubstanceGUID should be pulled from the list in class variable 'self.substances',
  created on startup by get_substance_guids.
  This function needs to be able to add more than one substance!
  Multiple substances come in one string separated by a '#'.
  childProducts": [
    ##### first substance LEAD #####
    # {
    #   "productCategory": None,
    #   "productNumber": None,
    #   "productName": "under the chair",
    #   "productDeclarationAdDsl": None,
    #   "productExemptions": [],
    #   "substanceInputs": [
    #     {
    #       "id": "bd193ce6-832e-4b98-bae8-8c6b05cb55f4",
    #       "name": "Lead",
    #       "exemption": None,
    #       "containedIn": None,
    #       "containedInProductType": None,
    #       "status": "abovethreshold",
    #       "comment": None,
    #       "iaeg": None,
    #       "nominalConcentration": 0.11,
    #       "maxConcentration": None,
    #       "weight": None,
    #       "unitOfMeasure": None,
    #       "processStage": None,
    #       "useDescriptors": [],
    #       "substanceGroupIds": ["00000000-0000-0000-0000-000000000000"],
    #       "cas": "7439-92-1",
    #       "ec": "231-100-4",
    #       "threshold": 0.1,
    #       "inProduct": True,
    #       "inProcess": False,
    #       "articleName": "under the chair",
    #       "treeId": "8b7f64f7-72f3-5efb-a391-92e709ada9ba"
    #     }
    #   ],
    #   "overflowSubstanceInputs": [],
    #   "proprietarySubstanceInputs": [],
    #   "fileUploads": [],
    #   "childProducts": [],
    #   "nominalConcentration": None,
    #   "minConcentration": None,
    #   "maxConcentration": None,
    #   "weight": None,
    #   "isArticle": True,
    #   "isHomogeneousMaterial": False,
    #   "treeId": "7ab8bcf8-7a3c-595a-a227-b1a6f14ea414"
    # },
    ##### second substance CADMIUM #####
    {
        # "productCategory": None,
        # "productNumber": None,
        # "productName": "above the chair",
        # "productDeclarationAdDsl": None,
        # "productExemptions": [],
        "substanceInputs": [
            {
                "id": "52a98f3d-1dea-4c1e-a96c-a2c4e331c3f8",
                # "name": "Cadmium",
                # "exemption": None,
                # "containedIn": None,
                # "containedInProductType": None,
                "status": "abovethreshold",
                # "comment": None,
                # "iaeg": None,
                "nominalConcentration": 0.12,
                # "maxConcentration": None,
                # "weight": None,
                # "unitOfMeasure": None,
                # "processStage": None,
                # "useDescriptors": [],
                # "substanceGroupIds": ["00000000-0000-0000-0000-000000000000"],
                # "cas": "7440-43-9",
                # "ec": "231-152-8",
                # "threshold": 0.1,
                "inProduct": True,
                # "inProcess": False,
                "articleName": "above the chair",
                # "treeId": "1779d40d-1d82-5c01-9d2a-89e1f93eafec"
            }
        ], """

  # Split the substance names on the '#' character
  substance_names = substance_name.split('#')
  # Get the SubstanceGUIDs for each substance
  substance_guids = [self.get_substance_guid(sn) for sn in substance_names]

  # Create the substance inputs for each substance
  substance_inputs = []
  for i, sg in enumerate(substance_guids):
    si = {
      "id": f"{sg}-input-{i}",
      "name": substance_names[i],
      "exemption": None,
      "containedIn": None,
      "containedInProductType": None,
      "status": "abovethreshold",
      "comment": None,
      "iaeg": None,
      "nominalConcentration": concentration,
      "maxConcentration": None,
      "weight": None,
      "unitOfMeasure": None,
      "processStage": None,
      "useDescriptors": [],
      "substanceGroupIds": ["00000000-0000-0000-0000-000000000000"],
      "cas": cas,
      "ec": ec,
      "threshold": 0.1,
      "inProduct": True,
      "inProcess": False,
      "articleName": article_name,
      "treeId": f"{sg}-tree"
    }
    substance_inputs.append(si)

  # Create the child products for each substance
  child_products = []
  for sg in substance_guids:
    cp = {
      "substanceInputs": [si for si in substance_inputs if si['name'] == self.get_substance_name(sg)],
      "childProducts": [],
      "nominalConcentration": None,
      "minConcentration": None,
      "maxConcentration": None,
      "weight": None,
      "isArticle": True,
      "isHomogeneousMaterial": False,
      "treeId": f"{sg}-article-tree"
    }
    child_products.append(cp)

  # Create and return the submissionProducts partial
  submission_products = {
    "childProducts": child_products,
    "overflowSubstanceInputs": [],
    "proprietarySubstanceInputs": [],
    "fileUploads": [],
    "nominalConcentration": None,
    "minConcentration": None,
    "maxConcentration": None,
    "weight": None,
    "isArticle": False,
    "isHomogeneousMaterial": False,
    "treeId": "root-tree"
  }
  return submission_products