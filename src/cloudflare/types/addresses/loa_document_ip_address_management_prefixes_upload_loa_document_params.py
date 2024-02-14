# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentParams"]


class LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentParams(TypedDict, total=False):
    loa_document: Required[str]
    """LOA document to upload."""
