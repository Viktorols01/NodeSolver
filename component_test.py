from classes.components.Resistance import Resistance
from classes.components.Source import Source
from classes.components.Diode import Diode

# Source
source_function = Source(1).function()
value = source_function([0, 1, 1])
assert value == 0, "source equation not fulfilled"

# Diode
diode_function = Diode(1).function()
value = diode_function([1, 0, 0])
assert value > 0, "diode current should be positive when applying positive voltage"
value = diode_function([0, 1, 0])
assert value <= 0, "diode current should be negative when applying negative voltage"