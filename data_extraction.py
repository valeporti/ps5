import numpy as np

def buildDescriptionsList(resumes: list) -> dict:
  desc = np.array([])
  for res in resumes:
    orgs = res['EmploymentHistory']['EmployerOrg']
    for org in orgs:
      roles = org['PositionHistory']
      for role in roles:
        desc = np.concatenate( (desc, [{
          'employer': org['EmployerOrgName'],
          'role': role['OrgName']['OrganizationName'],
          'description': role['Description'],
        }]))
  return desc