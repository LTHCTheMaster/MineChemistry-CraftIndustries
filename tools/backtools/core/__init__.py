"""
Core of a sort of toolbox
"""
from .images import *
from .elements import elements
from .periodic import PeriodicTableBuilder
# Remove useless things after importing * from .images because of "runtime" generated class that cannot be simply imported
del filecutter
del define_drawBaseForm
del define_colorInside
del define_imageClass
del listdir
del POS_FILE_PATH
del AFCIMGPATH
del makeColorTuple
del makeColorDarker
del colorMixer
del BLACK
del NATOCC_DECAY
del NATOCC_SYNTHETIC
del STOPPER_LIGHT_BLUE
del STOPPER_LIGHT_BLUE_DECAY
del STOPPER_LIGHT_BLUE_SYNTHETIC
del STOPPER_DARK_BLUE
del BLANK_IMAGE
del SIZE
del Image
del PALETTE_GOLDEN_INGOT
del GOLDEN_INGOT
del PALETTE_COPPER_INGOT
del COPPER_INGOT
del PALETTE_IRON_INGOT
del IRON_INGOT
del PALETTE_SPECIAL_INGOT
del SPECIAL_INGOT
del PALETTE_SPECIALL_INGOT
del SPECIALL_INGOT
del PALETTE_DUST
del DUST
del PALETTE_DUST_BLOCK
del DUST_BLOCK
del PALETTE_COPPER_BLOCK
del COPPER_BLOCK
del PALETTE_IRON_BLOCK
del IRON_BLOCK
del PALETTE_GOLDEN_BLOCK
del GOLDEN_BLOCK
del TemplateImg
del colorEditionIngot
