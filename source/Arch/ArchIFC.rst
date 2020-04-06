Arch IFC
========

.. automodule:: ArchIFC

.. autoclass:: ArchIFC.IfcRoot
    
    .. automethod:: setProperties
    .. automethod:: onChanged
    .. automethod:: setupIfcAttributes
    .. automethod:: setupIfcComplexAttributes
    .. automethod:: getIfcTypeSchema
    .. automethod:: getIfcSchema
    .. automethod:: getCanonicalisedIfcTypes
    .. automethod:: getIfcAttributeSchema
    .. automethod:: addIfcAttributes
    .. automethod:: addIfcAttribute
    .. automethod:: addIfcAttributeValueExpressions
    .. automethod:: setObjIfcAttributeValue
    .. automethod:: setObjIfcComplexAttributeValue
    .. automethod:: getObjIfcComplexAttribute
    .. automethod:: purgeUnusedIfcAttributesFromPropertiesList
    .. automethod:: migrateDeprecatedAttributes

.. autoclass:: ArchIFC.IfcProduct
    :show-inheritance:

    .. automethod:: getIfcSchema


.. autoclass:: ArchIFC.IfcContext
    :show-inheritance:

    .. automethod:: getIfcSchema

.. autoclass:: ArchIFCView.IfcContextView
    
    .. automethod:: setEdit

.. autoclass:: ArchIFCView.IfcContextUI

    .. automethod:: __init__
    .. automethod:: accept
    .. automethod:: createBaseLayout
    .. automethod:: createMapConversionFormLayout
    .. automethod:: prefillMapConversionForm
    .. automethod:: createFormEntry
    .. automethod:: createLabel
    .. automethod:: createLineEdit
