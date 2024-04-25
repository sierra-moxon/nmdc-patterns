# Auto generated from nmdc_patterns.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-16T17:25:37
# Schema: nmdc-patterns
#
# id: https://w3id.org/sierra-moxon/nmdc-patterns
# description: test pattern validation in nmdc
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC_PATTERNS = CurieNamespace('nmdc_patterns', 'https://w3id.org/sierra-moxon/nmdc-patterns/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = NMDC_PATTERNS


# Types

# Class references
class ActivityId(URIorCURIE):
    pass


class WorkflowExecutionActivityId(ActivityId):
    pass


class NamedThingId(URIorCURIE):
    pass


class PlannedProcessId(NamedThingId):
    pass


class OmicsProcessingId(PlannedProcessId):
    pass


@dataclass
class WorkflowExecutionActivityCollection(YAMLRoot):
    """
    A holder for Activity objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_PATTERNS["WorkflowExecutionActivityCollection"]
    class_class_curie: ClassVar[str] = "nmdc_patterns:WorkflowExecutionActivityCollection"
    class_name: ClassVar[str] = "WorkflowExecutionActivityCollection"
    class_model_uri: ClassVar[URIRef] = NMDC_PATTERNS.WorkflowExecutionActivityCollection

    entries: Optional[Union[Dict[Union[str, WorkflowExecutionActivityId], Union[dict, "WorkflowExecutionActivity"]], List[Union[dict, "WorkflowExecutionActivity"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=WorkflowExecutionActivity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Activity(YAMLRoot):
    """
    Something that occurs over a period of time and acts upon or with entities; it may include consuming, processing,
    transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_PATTERNS["Activity"]
    class_class_curie: ClassVar[str] = "nmdc_patterns:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = NMDC_PATTERNS.Activity

    id: Union[str, ActivityId] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        super().__post_init__(**kwargs)


@dataclass
class WorkflowExecutionActivity(Activity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_PATTERNS["WorkflowExecutionActivity"]
    class_class_curie: ClassVar[str] = "nmdc_patterns:WorkflowExecutionActivity"
    class_name: ClassVar[str] = "WorkflowExecutionActivity"
    class_model_uri: ClassVar[URIRef] = NMDC_PATTERNS.WorkflowExecutionActivity

    id: Union[str, WorkflowExecutionActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowExecutionActivityId):
            self.id = WorkflowExecutionActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_PATTERNS["NamedThing"]
    class_class_curie: ClassVar[str] = "nmdc_patterns:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NMDC_PATTERNS.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "OBI:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = NMDC_PATTERNS.PlannedProcess

    id: Union[str, PlannedProcessId] = None

@dataclass
class OmicsProcessing(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_PATTERNS["OmicsProcessing"]
    class_class_curie: ClassVar[str] = "nmdc_patterns:OmicsProcessing"
    class_name: ClassVar[str] = "OmicsProcessing"
    class_model_uri: ClassVar[URIRef] = NMDC_PATTERNS.OmicsProcessing

    id: Union[str, OmicsProcessingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OmicsProcessingId):
            self.id = OmicsProcessingId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=NMDC_PATTERNS.id, name="id", curie=NMDC_PATTERNS.curie('id'),
                   model_uri=NMDC_PATTERNS.id, domain=None, range=URIRef,
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=NMDC_PATTERNS.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NMDC_PATTERNS.description, domain=None, range=Optional[str])

slots.was_informed_by = Slot(uri=NMDC_PATTERNS.was_informed_by, name="was_informed_by", curie=NMDC_PATTERNS.curie('was_informed_by'),
                   model_uri=NMDC_PATTERNS.was_informed_by, domain=Activity, range=Optional[Union[str, ActivityId]], mappings = [PROV["wasInformedBy"]])

slots.workflowExecutionActivityCollection__entries = Slot(uri=NMDC_PATTERNS.entries, name="workflowExecutionActivityCollection__entries", curie=NMDC_PATTERNS.curie('entries'),
                   model_uri=NMDC_PATTERNS.workflowExecutionActivityCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, WorkflowExecutionActivityId], Union[dict, WorkflowExecutionActivity]], List[Union[dict, WorkflowExecutionActivity]]]])

slots.WorkflowExecutionActivity_id = Slot(uri=NMDC_PATTERNS.id, name="WorkflowExecutionActivity_id", curie=NMDC_PATTERNS.curie('id'),
                   model_uri=NMDC_PATTERNS.WorkflowExecutionActivity_id, domain=WorkflowExecutionActivity, range=Union[str, WorkflowExecutionActivityId],
                   pattern=re.compile(r'^nmdc:wf-[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.Activity_id = Slot(uri=NMDC_PATTERNS.id, name="Activity_id", curie=NMDC_PATTERNS.curie('id'),
                   model_uri=NMDC_PATTERNS.Activity_id, domain=Activity, range=Union[str, ActivityId],
                   pattern=re.compile(r'^nmdc:act-[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.Activity_was_informed_by = Slot(uri=NMDC_PATTERNS.was_informed_by, name="Activity_was_informed_by", curie=NMDC_PATTERNS.curie('was_informed_by'),
                   model_uri=NMDC_PATTERNS.Activity_was_informed_by, domain=Activity, range=Optional[Union[str, ActivityId]], mappings = [PROV["wasInformedBy"]],
                   pattern=re.compile(r'^nmdc:act-[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))

slots.OmicsProcessing_id = Slot(uri=NMDC_PATTERNS.id, name="OmicsProcessing_id", curie=NMDC_PATTERNS.curie('id'),
                   model_uri=NMDC_PATTERNS.OmicsProcessing_id, domain=OmicsProcessing, range=Union[str, OmicsProcessingId],
                   pattern=re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$'))