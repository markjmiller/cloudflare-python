# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.devices.policies.certificate_update_response import CertificateUpdateResponse

from ....._wrappers import ResultWrapper

from typing import Optional

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from .....types.zero_trust.devices.policies.certificate_get_response import CertificateGetResponse

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.devices.policies import certificate_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CertificatesResource", "AsyncCertificatesResource"]


class CertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self)

    def update(
        self,
        zone_tag: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateUpdateResponse]:
        """
        Enable Zero Trust Clients to provision a certificate, containing a x509 subject,
        and referenced by Access device posture policies when the client visits MTLS
        protected domains. This facilitates device posture without a WARP session.

        Args:
          enabled: The current status of the device policy certificate provisioning feature for
              WARP clients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            Optional[CertificateUpdateResponse],
            self._patch(
                f"/zones/{zone_tag}/devices/policy/certificates",
                body=maybe_transform({"enabled": enabled}, certificate_update_params.CertificateUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[CertificateUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        zone_tag: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateGetResponse]:
        """
        Fetches device certificate provisioning

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            Optional[CertificateGetResponse],
            self._get(
                f"/zones/{zone_tag}/devices/policy/certificates",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[CertificateGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self)

    async def update(
        self,
        zone_tag: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateUpdateResponse]:
        """
        Enable Zero Trust Clients to provision a certificate, containing a x509 subject,
        and referenced by Access device posture policies when the client visits MTLS
        protected domains. This facilitates device posture without a WARP session.

        Args:
          enabled: The current status of the device policy certificate provisioning feature for
              WARP clients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            Optional[CertificateUpdateResponse],
            await self._patch(
                f"/zones/{zone_tag}/devices/policy/certificates",
                body=await async_maybe_transform(
                    {"enabled": enabled}, certificate_update_params.CertificateUpdateParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[CertificateUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        zone_tag: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateGetResponse]:
        """
        Fetches device certificate provisioning

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_tag:
            raise ValueError(f"Expected a non-empty value for `zone_tag` but received {zone_tag!r}")
        return cast(
            Optional[CertificateGetResponse],
            await self._get(
                f"/zones/{zone_tag}/devices/policy/certificates",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[CertificateGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificateGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CertificatesResourceWithRawResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.update = to_raw_response_wrapper(
            certificates.update,
        )
        self.get = to_raw_response_wrapper(
            certificates.get,
        )


class AsyncCertificatesResourceWithRawResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.update = async_to_raw_response_wrapper(
            certificates.update,
        )
        self.get = async_to_raw_response_wrapper(
            certificates.get,
        )


class CertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.update = to_streamed_response_wrapper(
            certificates.update,
        )
        self.get = to_streamed_response_wrapper(
            certificates.get,
        )


class AsyncCertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.update = async_to_streamed_response_wrapper(
            certificates.update,
        )
        self.get = async_to_streamed_response_wrapper(
            certificates.get,
        )
