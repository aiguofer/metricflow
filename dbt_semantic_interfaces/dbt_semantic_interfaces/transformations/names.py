import logging

from dbt_semantic_interfaces.objects.data_source import DataSource
from dbt_semantic_interfaces.objects.user_configured_model import UserConfiguredModel
from dbt_semantic_interfaces.transformations.transform_rule import ModelTransformRule

logger = logging.getLogger(__name__)


class LowerCaseNamesRule(ModelTransformRule):
    """Lowercases the names of both top level objects and data source elements in a model"""

    @staticmethod
    def transform_model(model: UserConfiguredModel) -> UserConfiguredModel:  # noqa: D
        LowerCaseNamesRule._lowercase_top_level_objects(model)
        for data_source in model.data_sources:
            LowerCaseNamesRule._lowercase_data_source_elements(data_source)

        return model

    @staticmethod
    def _lowercase_data_source_elements(data_source: DataSource) -> None:
        """Lowercases the names of data source elements."""
        if data_source.measures:
            for measure in data_source.measures:
                measure.name = measure.name.lower()
        if data_source.identifiers:
            for entity in data_source.identifiers:
                entity.name = entity.name.lower()
        if data_source.dimensions:
            for dimension in data_source.dimensions:
                dimension.name = dimension.name.lower()

    @staticmethod
    def _lowercase_top_level_objects(model: UserConfiguredModel) -> None:
        """Lowercases the names of model objects"""
        if model.data_sources:
            for data_source in model.data_sources:
                data_source.name = data_source.name.lower()
