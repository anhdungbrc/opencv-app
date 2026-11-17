"""Central registry and factory for all OpenCV image processors."""

from typing import Any
from app.processors.base import BaseProcessor
from app.processors.colorspace import BGR2GrayProcessor, BGR2HSVProcessor, ColorFilterInRangeProcessor
from app.processors.geometric import GeometricTransformProcessor
from app.processors.thresholding import (
    SimpleThresholdProcessor,
    AdaptiveThresholdProcessor,
    OtsuThresholdProcessor,
)
from app.processors.smoothing import (
    GaussianBlurProcessor,
    MedianBlurProcessor,
    BilateralFilterProcessor,
)
from app.processors.edges import (
    CannyEdgeProcessor,
    SobelProcessor,
    LaplacianProcessor,
)
from app.processors.morphology import MorphologyProcessor
from app.processors.contours import ContoursProcessor
from app.processors.histogram import HistogramEqualizationProcessor

# Registry dictionary mapping operation ID string to processor class
_PROCESSOR_CLASSES: dict[str, type[BaseProcessor]] = {
    # 1. Colorspaces
    BGR2GrayProcessor.id: BGR2GrayProcessor,
    BGR2HSVProcessor.id: BGR2HSVProcessor,
    ColorFilterInRangeProcessor.id: ColorFilterInRangeProcessor,
    # 2. Geometric
    GeometricTransformProcessor.id: GeometricTransformProcessor,
    # 3. Thresholding
    SimpleThresholdProcessor.id: SimpleThresholdProcessor,
    AdaptiveThresholdProcessor.id: AdaptiveThresholdProcessor,
    OtsuThresholdProcessor.id: OtsuThresholdProcessor,
    # 4. Smoothing
    GaussianBlurProcessor.id: GaussianBlurProcessor,
    MedianBlurProcessor.id: MedianBlurProcessor,
    BilateralFilterProcessor.id: BilateralFilterProcessor,
    # 5. Edges & Gradients
    CannyEdgeProcessor.id: CannyEdgeProcessor,
    SobelProcessor.id: SobelProcessor,
    LaplacianProcessor.id: LaplacianProcessor,
    # 6. Morphology
    MorphologyProcessor.id: MorphologyProcessor,
    # 7. Contours
    ContoursProcessor.id: ContoursProcessor,
    # 8. Histograms
    HistogramEqualizationProcessor.id: HistogramEqualizationProcessor,
}


def register_processor(processor_cls: type[BaseProcessor]) -> None:
    """Register an additional processor class into the global registry.

    Args:
        processor_cls: Subclass of BaseProcessor.
    """
    _PROCESSOR_CLASSES[processor_cls.id] = processor_cls


def get_processor(operation_id: str) -> BaseProcessor:
    """Instantiate a processor by its unique operation identifier.

    Args:
        operation_id: Unique string ID of the processor (e.g. 'canny_edge').

    Returns:
        Instance of BaseProcessor.

    Raises:
        KeyError: If operation_id is not registered.
    """
    if operation_id not in _PROCESSOR_CLASSES:
        raise KeyError(f"Operation '{operation_id}' not found in registry. Available: {list(_PROCESSOR_CLASSES.keys())}")
    return _PROCESSOR_CLASSES[operation_id]()


def list_operations() -> list[dict[str, Any]]:
    """Return list of all registered operations with their schema metadata.

    Returns:
        List of dictionaries with id, name, category, description, doc_url, and parameters.
    """
    operations = []
    for op_id, cls_type in _PROCESSOR_CLASSES.items():
        instance = cls_type()
        operations.append({
            "id": instance.id,
            "name": instance.name,
            "category": instance.category,
            "description": instance.description,
            "doc_url": instance.doc_url,
            "parameters": instance.get_parameter_schema(),
        })
    return operations
