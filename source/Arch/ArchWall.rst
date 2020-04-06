Arch Wall
=========

.. automodule:: ArchWall

.. autofunction:: Arch.makeWall

.. autofunction:: Arch.joinWalls

.. autofunction:: Arch.areSameWallTypes

.. autoclass:: ArchWall._Wall
    :show-inheritance:

    .. automethod:: __init__
    .. automethod:: setProperties
    .. automethod:: onDocumentRestored
    .. automethod:: execute
    .. automethod:: onBeforeChange
    .. automethod:: onChanged
    .. automethod:: getFootprint
    .. automethod:: getExtrusionData

.. autoclass:: ArchWall._ViewProviderWall
    :show-inheritance:

    .. automethod:: __init__
    .. automethod:: getIcon
    .. automethod:: attach
    .. automethod:: updateData
    .. automethod:: getDisplayModes
    .. automethod:: setDisplaymode

.. 
    The ArchWall._CommandWall can't ever enter it's interactive mode, which is
    a shame. I think a draft module moved. An important example of why
    unit tests should be implemented.
