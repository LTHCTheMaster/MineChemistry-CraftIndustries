@echo off
rd "%1\saves\MCCI\datapacks\MineChemistry-CraftIndustriesDP"
rd "%1\resourcepacks\MineChemistry-CraftIndustriesRP"
mklink /d "%1\saves\MCCI\datapacks\MineChemistry-CraftIndustriesDP" "%2\Datapack"
mklink /d "%1\resourcepacks\MineChemistry-CraftIndustriesRP" "%2\Resourcepack"