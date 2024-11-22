from qibo import Circuit, gates, set_backend
set_backend("qibolab", "qw11q")

c = Circuit(1)
c.add(gates.M(0))

print(c().probabilities())
