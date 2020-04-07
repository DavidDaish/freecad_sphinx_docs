Arch Floor
==========

.. automodule:: ArchFloor

.. autofunction:: ArchFloor.makeFloor

.. autoclass:: ArchFloor._CommandFloor
    
    .. automethod:: GetResources
    .. automethod:: IsActive
    .. automethod:: Activated

.. autoclass:: ArchFloor._Floor
    :show-inheritance:

    .. automethod:: __init__
    .. automethod:: setProperties
    .. automethod:: onDocumentRestored
    .. automethod:: onChanged
    .. automethod:: execute
    .. automethod:: addObject
    .. automethod:: removeObject

.. autoclass:: ArchFloor._ViewProviderFloor

    .. automethod:: __init__
    .. automethod:: getIcon
    .. automethod:: attach
    .. automethod:: claimChildren
    .. automethod:: setupContextMenu
    .. automethod:: convertToBuildingPart
