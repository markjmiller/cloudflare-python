# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateway.expression_template import FallthroughCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFallthrough:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        fallthrough = client.api_gateway.expression_template.fallthrough.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["{zone}.domain1.tld", "domain2.tld"],
        )
        assert_matches_type(FallthroughCreateResponse, fallthrough, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.api_gateway.expression_template.fallthrough.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["{zone}.domain1.tld", "domain2.tld"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallthrough = response.parse()
        assert_matches_type(FallthroughCreateResponse, fallthrough, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.api_gateway.expression_template.fallthrough.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["{zone}.domain1.tld", "domain2.tld"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallthrough = response.parse()
            assert_matches_type(FallthroughCreateResponse, fallthrough, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.expression_template.fallthrough.with_raw_response.create(
                zone_id="",
                hosts=["{zone}.domain1.tld", "domain2.tld"],
            )


class TestAsyncFallthrough:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        fallthrough = await async_client.api_gateway.expression_template.fallthrough.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["{zone}.domain1.tld", "domain2.tld"],
        )
        assert_matches_type(FallthroughCreateResponse, fallthrough, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.expression_template.fallthrough.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["{zone}.domain1.tld", "domain2.tld"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallthrough = await response.parse()
        assert_matches_type(FallthroughCreateResponse, fallthrough, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.expression_template.fallthrough.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["{zone}.domain1.tld", "domain2.tld"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallthrough = await response.parse()
            assert_matches_type(FallthroughCreateResponse, fallthrough, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.expression_template.fallthrough.with_raw_response.create(
                zone_id="",
                hosts=["{zone}.domain1.tld", "domain2.tld"],
            )
