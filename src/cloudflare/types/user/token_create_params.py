# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .cidr_list_item import CIDRListItem
from .policy_with_permission_groups_param import PolicyWithPermissionGroupsParam

__all__ = ["TokenCreateParams", "Condition", "ConditionRequestIP"]


class TokenCreateParams(TypedDict, total=False):
    name: Required[str]
    """Token name."""

    policies: Required[Iterable[PolicyWithPermissionGroupsParam]]
    """List of access policies assigned to the token."""

    condition: Condition

    expires_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The expiration time on or after which the JWT MUST NOT be accepted for
    processing.
    """

    not_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time before which the token MUST NOT be accepted for processing."""


_ConditionRequestIPReservedKeywords = TypedDict(
    "_ConditionRequestIPReservedKeywords",
    {
        "in": List[CIDRListItem],
    },
    total=False,
)


class ConditionRequestIP(_ConditionRequestIPReservedKeywords, total=False):
    not_in: List[CIDRListItem]
    """List of IPv4/IPv6 CIDR addresses."""


class Condition(TypedDict, total=False):
    request_ip: ConditionRequestIP
    """Client IP restrictions."""
