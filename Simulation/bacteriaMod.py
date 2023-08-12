
from cc3d import CompuCellSetup
        

from bacteriaModSteppables import bacteriaModSteppable

CompuCellSetup.register_steppable(steppable=bacteriaModSteppable(frequency=1))


CompuCellSetup.run()
