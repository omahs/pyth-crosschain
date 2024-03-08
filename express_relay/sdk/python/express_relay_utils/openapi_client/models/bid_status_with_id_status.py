# coding: utf-8

"""
    auction-server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.bid_status_one_of import BidStatusOneOf
from openapi_client.models.bid_status_one_of1 import BidStatusOneOf1
from openapi_client.models.bid_status_one_of2 import BidStatusOneOf2
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

BIDSTATUSWITHIDSTATUS_ONE_OF_SCHEMAS = ["BidStatusOneOf", "BidStatusOneOf1", "BidStatusOneOf2"]

class BidStatusWithIdStatus(BaseModel):
    """
    BidStatusWithIdStatus
    """
    # data type: BidStatusOneOf
    oneof_schema_1_validator: Optional[BidStatusOneOf] = None
    # data type: BidStatusOneOf1
    oneof_schema_2_validator: Optional[BidStatusOneOf1] = None
    # data type: BidStatusOneOf2
    oneof_schema_3_validator: Optional[BidStatusOneOf2] = None
    actual_instance: Optional[Union[BidStatusOneOf, BidStatusOneOf1, BidStatusOneOf2]] = None
    one_of_schemas: List[str] = Field(default=Literal["BidStatusOneOf", "BidStatusOneOf1", "BidStatusOneOf2"])

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = BidStatusWithIdStatus.model_construct()
        error_messages = []
        match = 0
        # validate data type: BidStatusOneOf
        if not isinstance(v, BidStatusOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BidStatusOneOf`")
        else:
            match += 1
        # validate data type: BidStatusOneOf1
        if not isinstance(v, BidStatusOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BidStatusOneOf1`")
        else:
            match += 1
        # validate data type: BidStatusOneOf2
        if not isinstance(v, BidStatusOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BidStatusOneOf2`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BidStatusWithIdStatus with oneOf schemas: BidStatusOneOf, BidStatusOneOf1, BidStatusOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BidStatusWithIdStatus with oneOf schemas: BidStatusOneOf, BidStatusOneOf1, BidStatusOneOf2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BidStatusOneOf
        try:
            instance.actual_instance = BidStatusOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BidStatusOneOf1
        try:
            instance.actual_instance = BidStatusOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BidStatusOneOf2
        try:
            instance.actual_instance = BidStatusOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BidStatusWithIdStatus with oneOf schemas: BidStatusOneOf, BidStatusOneOf1, BidStatusOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BidStatusWithIdStatus with oneOf schemas: BidStatusOneOf, BidStatusOneOf1, BidStatusOneOf2. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BidStatusOneOf, BidStatusOneOf1, BidStatusOneOf2]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


