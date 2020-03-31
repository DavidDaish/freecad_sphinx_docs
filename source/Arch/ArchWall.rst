Arch Wall
=========

.. automodule:: ArchWall

.. autofunction:: Arch.makeWall

.. autofunction:: Arch.joinWalls

.. autofunction:: Arch.areSameWallTypes

.. autoclass:: ArchWall._Wall
    :show-inheritance:

    .. automethod:: getParentHeight

.. 
    The ArchWall._CommandWall can't ever enter it's interactive mode, which is
    a shame. I think a draft module moved. An important example of why
    unit tests should be implemented.

..
    Part::PartFeature = a simple element with a topological shape associated to it that can be displayed in the 3D view. 
    Part::Feature = Old name for Part::PartFeature
    Part::FeaturePython = This is a simple object that by default doesn't have
        many properties, for example, no placement nor topological shape. This
        object is for general purpose use; depending on the properties that are
        assigned to it, it can be used to manage different types of data. 

..
    TODO Come back to ArchWall._Wall
