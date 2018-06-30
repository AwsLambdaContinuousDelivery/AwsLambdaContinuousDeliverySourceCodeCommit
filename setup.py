#!/usr/bin/env python

from distutils.core import setup

setup( name='AwsLambdaContinuousDeliverySourceCodeCommit'
     , version = '0.0.2'
     , description = 'AwsLambdaContinuousDeliverySourceCodeCommit'
     , author = 'Janos Potecki'
     , url = 'https://github.com/AwsLambdaContinuousDelivery/AwsLambdaContinuousDeliverySourceCodeCommit'
     , packages = ['awslambdacontinuousdelivery.source.codecommit']
     , license='MIT'
     , install_requires = [ 
          'troposphere'
        ]
     )
