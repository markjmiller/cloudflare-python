# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..shared import UnnamedSchemaRef107
from ..._models import BaseModel

__all__ = ["FirewallFilterRule"]


class FirewallFilterRule(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the firewall rule."""

    action: Optional[
        Literal["block", "challenge", "js_challenge", "managed_challenge", "allow", "log", "bypass"]
    ] = None
    """The action to apply to a matched request.

    The `log` action is only available on an Enterprise plan.
    """

    description: Optional[str] = None
    """An informative summary of the firewall rule."""

    filter: Optional[UnnamedSchemaRef107] = None

    paused: Optional[bool] = None
    """When true, indicates that the firewall rule is currently paused."""

    priority: Optional[float] = None
    """The priority of the rule.

    Optional value used to define the processing order. A lower number indicates a
    higher priority. If not provided, rules with a defined priority will be
    processed before rules without a priority.
    """

    products: Optional[
        List[Literal["zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf"]]
    ] = None

    ref: Optional[str] = None
    """A short reference tag. Allows you to select related firewall rules."""
