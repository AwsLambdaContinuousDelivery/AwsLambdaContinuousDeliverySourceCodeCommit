# By Janos Potecki
# University College London
# January 2018

from troposphere import Template, Sub, Parameter, Ref
from troposphere.codepipeline import ( Stages
                                     , Actions
                                     , ActionTypeId
                                     , OutputArtifacts
                                     )


def getCodeCommit(t: Template, outputfiles: str) -> Stages:
  repo = t.add_parameter(
    Parameter( "CodeCommitRepo"
             , Description="Name of the CodeCommit Repository"
             , Type="String"
             ) 
    )
  branch = t.add_parameter(
    Parameter( "Branch"
             , Description="Branch triggering the deployment"
             , Type="String"
             ) 
    )
  actionId = ActionTypeId( Category = "Source"
                         , Owner = "AWS"
                         , Version = "1"
                         , Provider = "CodeCommit"
                         )
  action = Actions( Name = Sub("${AWS::StackName}-LambdaSource")
                  , ActionTypeId = actionId
                  , Configuration = {"BranchName" : Ref(branch)
                                    , "RepositoryName" : Ref(repo)
                                    }
                  , OutputArtifacts = [OutputArtifacts( Name = outputfiles)]
                  , RunOrder = "1"
                  )
  return Stages( Name = "Source"
               , Actions = [ action ]
               )
