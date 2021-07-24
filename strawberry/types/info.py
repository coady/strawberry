import dataclasses
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from graphql import OperationDefinitionNode
from graphql.language import FieldNode
from graphql.pyutils.path import Path

from strawberry.type import StrawberryType

from .nodes import SelectionField


ContextType = TypeVar("ContextType")
RootValueType = TypeVar("RootValueType")


@dataclasses.dataclass
class Info(Generic[ContextType, RootValueType]):
    field_name: str
    field_nodes: List[FieldNode]  # deprecated
    field: SelectionField
    context: ContextType
    root_value: RootValueType
    variable_values: Dict[str, Any]
    # TODO: merge type with StrawberryType when StrawberryObject is implemented
    return_type: Optional[Union[type, StrawberryType]]
    # TODO: create an abstraction on these fields
    operation: OperationDefinitionNode
    path: Path
    # TODO: parent_type as strawberry types
