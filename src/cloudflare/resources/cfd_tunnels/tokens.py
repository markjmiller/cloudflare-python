# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.cfd_tunnels import TokenCloudflareTunnelGetACloudflareTunnelTokenResponse

__all__ = ["Tokens", "AsyncTokens"]


class Tokens(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self)

    def cloudflare_tunnel_get_a_cloudflare_tunnel_token(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenCloudflareTunnelGetACloudflareTunnelTokenResponse:
        """
        Gets the token used to associate cloudflared with a specific tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            TokenCloudflareTunnelGetACloudflareTunnelTokenResponse,
            self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/token",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenCloudflareTunnelGetACloudflareTunnelTokenResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncTokens(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self)

    async def cloudflare_tunnel_get_a_cloudflare_tunnel_token(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenCloudflareTunnelGetACloudflareTunnelTokenResponse:
        """
        Gets the token used to associate cloudflared with a specific tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            TokenCloudflareTunnelGetACloudflareTunnelTokenResponse,
            await self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/token",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenCloudflareTunnelGetACloudflareTunnelTokenResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TokensWithRawResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.cloudflare_tunnel_get_a_cloudflare_tunnel_token = to_raw_response_wrapper(
            tokens.cloudflare_tunnel_get_a_cloudflare_tunnel_token,
        )


class AsyncTokensWithRawResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.cloudflare_tunnel_get_a_cloudflare_tunnel_token = async_to_raw_response_wrapper(
            tokens.cloudflare_tunnel_get_a_cloudflare_tunnel_token,
        )


class TokensWithStreamingResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.cloudflare_tunnel_get_a_cloudflare_tunnel_token = to_streamed_response_wrapper(
            tokens.cloudflare_tunnel_get_a_cloudflare_tunnel_token,
        )


class AsyncTokensWithStreamingResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.cloudflare_tunnel_get_a_cloudflare_tunnel_token = async_to_streamed_response_wrapper(
            tokens.cloudflare_tunnel_get_a_cloudflare_tunnel_token,
        )
