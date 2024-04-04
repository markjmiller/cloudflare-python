# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from ...types import shared_params
from ..shared import UnnamedSchemaRef163

__all__ = [
    "IdentityProviderCreateParams",
    "AccessAzureAd",
    "AccessAzureAdConfig",
    "AccessCentrify",
    "AccessCentrifyConfig",
    "AccessFacebook",
    "AccessFacebookConfig",
    "AccessGitHub",
    "AccessGitHubConfig",
    "AccessGoogle",
    "AccessGoogleConfig",
    "AccessGoogleApps",
    "AccessGoogleAppsConfig",
    "AccessLinkedin",
    "AccessLinkedinConfig",
    "AccessOidc",
    "AccessOidcConfig",
    "AccessOkta",
    "AccessOktaConfig",
    "AccessOnelogin",
    "AccessOneloginConfig",
    "AccessPingone",
    "AccessPingoneConfig",
    "AccessSaml",
    "AccessSamlConfig",
    "AccessSamlConfigHeaderAttribute",
    "AccessYandex",
    "AccessYandexConfig",
    "AccessOnetimepin",
]


class AccessAzureAd(TypedDict, total=False):
    config: Required[AccessAzureAdConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessAzureAdConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    conditional_access_enabled: bool
    """Should Cloudflare try to load authentication contexts from your account"""

    directory_id: str
    """Your Azure directory uuid"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    prompt: Literal["login", "select_account", "none"]
    """Indicates the type of user interaction that is required.

    prompt=login forces the user to enter their credentials on that request,
    negating single-sign on. prompt=none is the opposite. It ensures that the user
    isn't presented with any interactive prompt. If the request can't be completed
    silently by using single-sign on, the Microsoft identity platform returns an
    interaction_required error. prompt=select_account interrupts single sign-on
    providing account selection experience listing all the accounts either in
    session or any remembered account or an option to choose to use a different
    account altogether.
    """

    support_groups: bool
    """Should Cloudflare try to load groups from your account"""


class AccessCentrify(TypedDict, total=False):
    config: Required[AccessCentrifyConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessCentrifyConfig(TypedDict, total=False):
    centrify_account: str
    """Your centrify account url"""

    centrify_app_id: str
    """Your centrify app id"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""


class AccessFacebook(TypedDict, total=False):
    config: Required[AccessFacebookConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessFacebookConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessGitHub(TypedDict, total=False):
    config: Required[AccessGitHubConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGitHubConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessGoogle(TypedDict, total=False):
    config: Required[AccessGoogleConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""


class AccessGoogleApps(TypedDict, total=False):
    config: Required[AccessGoogleAppsConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleAppsConfig(TypedDict, total=False):
    apps_domain: str
    """Your companies TLD"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""


class AccessLinkedin(TypedDict, total=False):
    config: Required[AccessLinkedinConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessLinkedinConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessOidc(TypedDict, total=False):
    config: Required[AccessOidcConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOidcConfig(TypedDict, total=False):
    auth_url: str
    """The authorization_endpoint URL of your IdP"""

    certs_url: str
    """The jwks_uri endpoint of your IdP to allow the IdP keys to sign the tokens"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    scopes: List[str]
    """OAuth scopes"""

    token_url: str
    """The token_endpoint URL of your IdP"""


class AccessOkta(TypedDict, total=False):
    config: Required[AccessOktaConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOktaConfig(TypedDict, total=False):
    authorization_server_id: str
    """Your okta authorization server id"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    okta_account: str
    """Your okta account url"""


class AccessOnelogin(TypedDict, total=False):
    config: Required[AccessOneloginConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOneloginConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    onelogin_account: str
    """Your OneLogin account url"""


class AccessPingone(TypedDict, total=False):
    config: Required[AccessPingoneConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessPingoneConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    ping_env_id: str
    """Your PingOne environment identifier"""


class AccessSaml(TypedDict, total=False):
    config: Required[AccessSamlConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessSamlConfigHeaderAttribute(TypedDict, total=False):
    attribute_name: str
    """attribute name from the IDP"""

    header_name: str
    """header that will be added on the request to the origin"""


class AccessSamlConfig(TypedDict, total=False):
    attributes: List[str]
    """
    A list of SAML attribute names that will be added to your signed JWT token and
    can be used in SAML policy rules.
    """

    email_attribute_name: str
    """The attribute name for email in the SAML response."""

    header_attributes: Iterable[AccessSamlConfigHeaderAttribute]
    """
    Add a list of attribute names that will be returned in the response header from
    the Access callback.
    """

    idp_public_certs: List[str]
    """X509 certificate to verify the signature in the SAML authentication response"""

    issuer_url: str
    """IdP Entity ID or Issuer URL"""

    sign_request: bool
    """Sign the SAML authentication request with Access credentials.

    To verify the signature, use the public key from the Access certs endpoints.
    """

    sso_target_url: str
    """URL to send the SAML authentication requests to"""


class AccessYandex(TypedDict, total=False):
    config: Required[AccessYandexConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessYandexConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessOnetimepin(TypedDict, total=False):
    config: Required[object]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[UnnamedSchemaRef163]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: shared_params.UnnamedSchemaRef158
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


IdentityProviderCreateParams = Union[
    AccessAzureAd,
    AccessCentrify,
    AccessFacebook,
    AccessGitHub,
    AccessGoogle,
    AccessGoogleApps,
    AccessLinkedin,
    AccessOidc,
    AccessOkta,
    AccessOnelogin,
    AccessPingone,
    AccessSaml,
    AccessYandex,
    AccessOnetimepin,
]
