# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from .a_record import ARecord
from ..._models import BaseModel
from .ds_record import DSRecord
from .mx_record import MXRecord
from .ns_record import NSRecord
from .caa_record import CAARecord
from .loc_record import LOCRecord
from .ptr_record import PTRRecord
from .srv_record import SRVRecord
from .txt_record import TXTRecord
from .uri_record import URIRecord
from .aaaa_record import AAAARecord
from .cert_record import CERTRecord
from .svcb_record import SVCBRecord
from .tlsa_record import TLSARecord
from .cname_record import CNAMERecord
from .https_record import HTTPSRecord
from .naptr_record import NAPTRRecord
from .sshfp_record import SSHFPRecord
from .dnskey_record import DNSKEYRecord
from .smimea_record import SMIMEARecord

__all__ = [
    "RecordBatchResponse",
    "Delete",
    "DeleteOpenpgpkey",
    "Patch",
    "PatchOpenpgpkey",
    "Post",
    "PostOpenpgpkey",
    "Put",
    "PutOpenpgpkey",
]


class DeleteOpenpgpkey(BaseModel):
    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Delete: TypeAlias = Annotated[
    Union[
        ARecord,
        AAAARecord,
        CAARecord,
        CERTRecord,
        CNAMERecord,
        DNSKEYRecord,
        DSRecord,
        HTTPSRecord,
        LOCRecord,
        MXRecord,
        NAPTRRecord,
        NSRecord,
        DeleteOpenpgpkey,
        PTRRecord,
        SMIMEARecord,
        SRVRecord,
        SSHFPRecord,
        SVCBRecord,
        TLSARecord,
        TXTRecord,
        URIRecord,
    ],
    PropertyInfo(discriminator="type"),
]


class PatchOpenpgpkey(BaseModel):
    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Patch: TypeAlias = Annotated[
    Union[
        ARecord,
        AAAARecord,
        CAARecord,
        CERTRecord,
        CNAMERecord,
        DNSKEYRecord,
        DSRecord,
        HTTPSRecord,
        LOCRecord,
        MXRecord,
        NAPTRRecord,
        NSRecord,
        PatchOpenpgpkey,
        PTRRecord,
        SMIMEARecord,
        SRVRecord,
        SSHFPRecord,
        SVCBRecord,
        TLSARecord,
        TXTRecord,
        URIRecord,
    ],
    PropertyInfo(discriminator="type"),
]


class PostOpenpgpkey(BaseModel):
    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Post: TypeAlias = Annotated[
    Union[
        ARecord,
        AAAARecord,
        CAARecord,
        CERTRecord,
        CNAMERecord,
        DNSKEYRecord,
        DSRecord,
        HTTPSRecord,
        LOCRecord,
        MXRecord,
        NAPTRRecord,
        NSRecord,
        PostOpenpgpkey,
        PTRRecord,
        SMIMEARecord,
        SRVRecord,
        SSHFPRecord,
        SVCBRecord,
        TLSARecord,
        TXTRecord,
        URIRecord,
    ],
    PropertyInfo(discriminator="type"),
]


class PutOpenpgpkey(BaseModel):
    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Put: TypeAlias = Annotated[
    Union[
        ARecord,
        AAAARecord,
        CAARecord,
        CERTRecord,
        CNAMERecord,
        DNSKEYRecord,
        DSRecord,
        HTTPSRecord,
        LOCRecord,
        MXRecord,
        NAPTRRecord,
        NSRecord,
        PutOpenpgpkey,
        PTRRecord,
        SMIMEARecord,
        SRVRecord,
        SSHFPRecord,
        SVCBRecord,
        TLSARecord,
        TXTRecord,
        URIRecord,
    ],
    PropertyInfo(discriminator="type"),
]


class RecordBatchResponse(BaseModel):
    deletes: Optional[List[Delete]] = None

    patches: Optional[List[Patch]] = None

    posts: Optional[List[Post]] = None

    puts: Optional[List[Put]] = None
