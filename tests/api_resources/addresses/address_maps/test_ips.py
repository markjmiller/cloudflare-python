# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addresses.address_maps import IPDeleteResponse, IPUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ip = client.addresses.address_maps.ips.update(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPUpdateResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.ips.with_raw_response.update(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(Optional[IPUpdateResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.ips.with_streaming_response.update(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(Optional[IPUpdateResponse], ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.ips.with_raw_response.update(
                "192.0.2.1",
                account_identifier="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            client.addresses.address_maps.ips.with_raw_response.update(
                "192.0.2.1",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            client.addresses.address_maps.ips.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ip = client.addresses.address_maps.ips.delete(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPDeleteResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.ips.with_raw_response.delete(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(Optional[IPDeleteResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.ips.with_streaming_response.delete(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(Optional[IPDeleteResponse], ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.ips.with_raw_response.delete(
                "192.0.2.1",
                account_identifier="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            client.addresses.address_maps.ips.with_raw_response.delete(
                "192.0.2.1",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            client.addresses.address_maps.ips.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncIPs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.addresses.address_maps.ips.update(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPUpdateResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.ips.with_raw_response.update(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(Optional[IPUpdateResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.ips.with_streaming_response.update(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(Optional[IPUpdateResponse], ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.ips.with_raw_response.update(
                "192.0.2.1",
                account_identifier="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            await async_client.addresses.address_maps.ips.with_raw_response.update(
                "192.0.2.1",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            await async_client.addresses.address_maps.ips.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.addresses.address_maps.ips.delete(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPDeleteResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.ips.with_raw_response.delete(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(Optional[IPDeleteResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.ips.with_streaming_response.delete(
            "192.0.2.1",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(Optional[IPDeleteResponse], ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.ips.with_raw_response.delete(
                "192.0.2.1",
                account_identifier="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            await async_client.addresses.address_maps.ips.with_raw_response.delete(
                "192.0.2.1",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            await async_client.addresses.address_maps.ips.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
