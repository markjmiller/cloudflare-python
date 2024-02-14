# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = [
    "ThreatCategoryListResponse",
    "Meta",
    "MetaDateRange",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "Summary0",
]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class MetaConfidenceInfoAnnotation(BaseModel):
    data_source: str = FieldInfo(alias="dataSource")

    description: str

    event_type: str = FieldInfo(alias="eventType")

    is_instantaneous: object = FieldInfo(alias="isInstantaneous")

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[MetaConfidenceInfoAnnotation]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    brand_impersonation: str = FieldInfo(alias="BrandImpersonation")

    credential_harvester: str = FieldInfo(alias="CredentialHarvester")

    identity_deception: str = FieldInfo(alias="IdentityDeception")

    link: str = FieldInfo(alias="Link")


class ThreatCategoryListResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
