# Docs!
## Usage
./main.exe convert "print(@a,hello)"

If your using the compile option, you have to include the core module, `core.mclangmodule`.

`./main.exe compile in input.mclang out output.mcfunction`

ALSO, if you want to use the core module in any directory, you have to run `install_module.py`

If your a module developer, you can also edit `install_module.py` to be able to install your module as a global module.

In order to use global modules, don't include the `./` in your import statement
## Commands:
- import(core.mclangmodule)
- give(@s,diamond_shovel)
- summon(zombie,~ ~ ~)
- setblock(stone,0 0 0)
- print(@a,hello)
- fill(~-5 ~ ~-5, ~5 ~ ~5, stone)