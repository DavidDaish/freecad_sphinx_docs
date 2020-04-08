Arch Component
==============

.. automodule:: ArchComponent

.. autofunction:: ArchComponent.addToComponent

.. autofunction:: ArchComponent.removeFromComponent

.. inheritance-diagram:: ArchComponent.Component
.. autoclass:: ArchComponent.Component
    :show-inheritance:

    .. automethod:: __init__
    .. automethod:: setProperties
    .. automethod:: onChanged
    .. automethod:: getMovableChildren
    .. automethod:: getParentHeight
    .. automethod:: clone
    .. automethod:: getSiblings
    .. automethod:: getExtrusionData
    .. automethod:: rebase
    .. automethod:: hideSubobjects
    .. automethod:: processSubShapes
    .. automethod:: spread
    .. automethod:: isIdentity
    .. automethod:: applyShape
    .. automethod:: computeAreas
    .. automethod:: isStandardCase
    
.. autoclass:: ArchComponent.ViewProviderComponent

    .. automethod:: __init__
    .. automethod:: setProperties
    .. automethod:: updateData
    .. automethod:: getIcon
    .. automethod:: onChanged
    .. automethod:: attach
    .. automethod:: getDisplayModes
    .. automethod:: setDisplayMode
    .. automethod:: claimChildren
    .. automethod:: setEdit
    .. automethod:: unsetEdit
    .. automethod:: setupContextMenu
    .. automethod:: areDifferentColors
    .. automethod:: colorize
    .. automethod:: getHosts

.. autoclass:: ArchComponent.ArchSelectionObserver

    .. automethod:: __init__
    .. automethod:: addSelection

.. autoclass:: ArchComponent.SelectionTaskPanel

    .. automethod:: __init__
    .. automethod:: getStandardButtons
    .. automethod:: reject

.. autoclass:: ArchComponent.ComponentTaskPanel

    .. automethod:: __init__
    .. automethod:: isAllowedAlterSelection
    .. automethod:: isAllowedAlterView
    .. automethod:: getStandardButtons
    .. automethod:: check
    .. automethod:: getIcon
    .. automethod:: update
    .. automethod:: addElement
    .. automethod:: removeElement
    .. automethod:: accept
    .. automethod:: editObject
    .. automethod:: retranslateUi
    .. automethod:: editIfcProperties
    .. automethod:: acceptIfcProperties
    .. automethod:: addIfcProperty
    .. automethod:: addIfcPset
    .. automethod:: removeIfcProperty
    .. automethod:: editClass

.. autoclass:: ArchComponent.IfcEditorDelegate
    :show-inheritance:

    .. automethod:: __init__
    .. automethod:: createEditor
    .. automethod:: setEditorData
    .. automethod:: setModelData
