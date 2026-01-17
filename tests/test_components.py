from circuit_simulator.core.advanced_components import Diode, BJT

def test_diode_forward_bias():
    d = Diode(Is=1e-12, Vt=0.026)
    current = d.current(0.7)
    assert current > 0

def test_bjt_gain():
    bjt = BJT(beta=100)
    ic = bjt.collector_current(ib=0.001)
    assert ic == 0.1
