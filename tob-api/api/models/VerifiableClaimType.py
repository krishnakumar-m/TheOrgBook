"""
    REST API Documentation for TheOrgBook

    TheOrgBook is a repository for Verifiable Claims made about Organizations related to a known foundational Verifiable Claim. See https://github.com/bcgov/VON

    OpenAPI spec version: v1
        

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import datetime

from django.db import models
from django.utils import timezone
from .IssuerService import IssuerService

from auditable.models import Auditable

class VerifiableClaimType(Auditable):	    
    claimType = models.CharField(max_length=255)   
    base64Logo = models.CharField(max_length=255, blank=True, null=True)   
    issuerServiceId = models.ForeignKey('IssuerService', related_name='issuerServices')   
    issuerURL = models.CharField(max_length=255)   
    effectiveDate = models.DateField(default=timezone.now)   
    schemaName = models.CharField(max_length=255, blank=True, null=True)   
    schemaVersion = models.CharField(max_length=255, blank=True, null=True)   
    endDate = models.DateField(blank=True, null=True)   
    class Meta:
        db_table = 'VERIFIABLE_CLAIM_TYPE'

