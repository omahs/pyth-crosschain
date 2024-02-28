# coding: utf-8

"""
    auction-server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from openapi_client.models.token_qty import TokenQty
from typing import Optional, Set
from typing_extensions import Self

class OpportunityParamsWithMetadata(BaseModel):
    """
    Similar to OpportunityParams, but with the opportunity id included.
    """ # noqa: E501
    calldata: StrictStr = Field(description="Calldata for the contract call.")
    chain_id: StrictStr = Field(description="The chain id where the liquidation will be executed.")
    contract: StrictStr = Field(description="The contract address to call for execution of the liquidation.")
    permission_key: StrictStr = Field(description="The permission key required for succesful execution of the liquidation.")
    receipt_tokens: List[TokenQty]
    repay_tokens: List[TokenQty]
    value: StrictStr = Field(description="The value to send with the contract call.")
    version: StrictStr
    creation_time: StrictInt = Field(description="Creation time of the opportunity")
    opportunity_id: StrictStr = Field(description="The opportunity unique id")
    __properties: ClassVar[List[str]] = ["calldata", "chain_id", "contract", "permission_key", "receipt_tokens", "repay_tokens", "value", "version", "creation_time", "opportunity_id"]

    @field_validator('version')
    def version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['v1']):
            raise ValueError("must be one of enum values ('v1')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OpportunityParamsWithMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in receipt_tokens (list)
        _items = []
        if self.receipt_tokens:
            for _item in self.receipt_tokens:
                if _item:
                    _items.append(_item.to_dict())
            _dict['receipt_tokens'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in repay_tokens (list)
        _items = []
        if self.repay_tokens:
            for _item in self.repay_tokens:
                if _item:
                    _items.append(_item.to_dict())
            _dict['repay_tokens'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpportunityParamsWithMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "calldata": obj.get("calldata"),
            "chain_id": obj.get("chain_id"),
            "contract": obj.get("contract"),
            "permission_key": obj.get("permission_key"),
            "receipt_tokens": [TokenQty.from_dict(_item) for _item in obj["receipt_tokens"]] if obj.get("receipt_tokens") is not None else None,
            "repay_tokens": [TokenQty.from_dict(_item) for _item in obj["repay_tokens"]] if obj.get("repay_tokens") is not None else None,
            "value": obj.get("value"),
            "version": obj.get("version"),
            "creation_time": obj.get("creation_time"),
            "opportunity_id": obj.get("opportunity_id")
        })
        return _obj


