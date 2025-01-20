
# Single QUA script generated at 2025-01-20 08:01:08.170479
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    set_dc_offset("B1/flux", "single", -0.08233987198571363)
    set_dc_offset("D1/flux", "single", 0.21674190528643072)
    set_dc_offset("B2/flux", "single", 0.30438797397930567)
    set_dc_offset("D2/flux", "single", -0.4253086474672965)
    set_dc_offset("B3/flux", "single", 0.34274625187777014)
    set_dc_offset("D3/flux", "single", -0.21477959018116385)
    set_dc_offset("B4/flux", "single", 0.30347347513189465)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("B5/flux", "single", -0.2839878581260484)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-6856037069631139450", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("1349492219595852329", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-6317862836925698040", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("5250484221799162101", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("5471978280997877349", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("8780461724625783538", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("9001955783824498786", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-4922470519795049514", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("5856918497392951733", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-7025534542683170719", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-2013818784855121621", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-1792324725656406373", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("2729993044433596943", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("405434962346760490", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("4927752732436763806", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("2990972873723036139", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-3759750178023626209", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-5369162396263082997", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        play("2062409625443580896", "B4/drive")
        wait(11, "B4/flux")
        play("-1561990490020459346", "B4/flux")
        wait(46, "B4/drive")
        play("2823500254667142765", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1267399234458798216", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6157064216188595)-(v3*0.7879756356495417))>-0.00045062927002878544)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("1267399234458798216_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.08233987198571363,
                    "filter": {},
                },
                "2": {
                    "offset": 0.30438797397930567,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.30347347513189465,
                    "filter": {
                        "feedforward": [1.078098681992251, -0.923066404629278],
                        "feedback": [0.9999990463256836, -0.8449677226370271],
                    },
                },
                "5": {
                    "offset": -0.2839878581260484,
                    "filter": {},
                },
            },
            "digital_outputs": {},
            "analog_inputs": {
                "1": {
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
            },
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.21674190528643072,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "filter": {},
                },
                "7": {
                    "offset": -0.04,
                    "filter": {},
                },
            },
            "digital_outputs": {},
            "analog_inputs": {
                "1": {
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
            },
        },
        "con2": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {
                "1": {},
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                },
            },
        },
        "con3": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": 0.0,
                    "filter": {},
                },
                "8": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {
                "7": {},
            },
            "analog_inputs": {
                "1": {
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
            },
        },
    },
    "octaves": {
        "octave2": {
            "connectivity": "con2",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7370000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7370000000.0,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
        "octave3": {
            "connectivity": "con3",
            "RF_outputs": {
                "4": {
                    "LO_frequency": 6700000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "RF_inputs": {},
        },
    },
    "elements": {
        "B1/flux": {
            "singleInput": {
                "port": ('con4', 1),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D1/flux": {
            "singleInput": {
                "port": ('con9', 3),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B2/flux": {
            "singleInput": {
                "port": ('con4', 2),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D2/flux": {
            "singleInput": {
                "port": ('con9', 4),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B3/flux": {
            "singleInput": {
                "port": ('con4', 3),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D3/flux": {
            "singleInput": {
                "port": ('con9', 5),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B4/flux": {
            "singleInput": {
                "port": ('con4', 4),
            },
            "intermediate_frequency": 0,
            "operations": {
                "-6856037069631139450": "-6856037069631139450",
                "1349492219595852329": "1349492219595852329",
                "-6317862836925698040": "-6317862836925698040",
                "5250484221799162101": "5250484221799162101",
                "5471978280997877349": "5471978280997877349",
                "8780461724625783538": "8780461724625783538",
                "9001955783824498786": "9001955783824498786",
                "-4922470519795049514": "-4922470519795049514",
                "5856918497392951733": "5856918497392951733",
                "-7025534542683170719": "-7025534542683170719",
                "-2013818784855121621": "-2013818784855121621",
                "-1792324725656406373": "-1792324725656406373",
                "2729993044433596943": "2729993044433596943",
                "405434962346760490": "405434962346760490",
                "4927752732436763806": "4927752732436763806",
                "2990972873723036139": "2990972873723036139",
                "-3759750178023626209": "-3759750178023626209",
                "-5369162396263082997": "-5369162396263082997",
                "-1561990490020459346": "-1561990490020459346",
            },
        },
        "D4/flux": {
            "singleInput": {
                "port": ('con9', 6),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B5/flux": {
            "singleInput": {
                "port": ('con4', 5),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D5/flux": {
            "singleInput": {
                "port": ('con9', 7),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "B4/acquisition": {
            "RF_inputs": {
                "port": ('octave2', 1),
            },
            "RF_outputs": {
                "port": ('octave2', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con2', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 330298316.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "1267399234458798216": "1267399234458798216_B4/acquisition",
            },
        },
        "B4/drive": {
            "RF_inputs": {
                "port": ('octave3', 4),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con3', 7),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 109678455.0,
            "operations": {
                "2062409625443580896": "2062409625443580896",
                "2823500254667142765": "2823500254667142765",
            },
        },
    },
    "pulses": {
        "2062409625443580896": {
            "length": 40,
            "waveforms": {
                "I": "2062409625443580896_i",
                "Q": "2062409625443580896_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4927730990343027262": {
            "length": 16,
            "waveforms": {
                "single": "4927730990343027262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1267399234458798216_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7491253477418967775_i",
                "Q": "-7491253477418967775_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "5911063667325414500": {
            "length": 16,
            "waveforms": {
                "single": "5911063667325414500",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7125490678346194125": {
            "length": 16,
            "waveforms": {
                "single": "7125490678346194125",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4523145508284672960": {
            "length": 16,
            "waveforms": {
                "single": "4523145508284672960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8330317414527296611": {
            "length": 16,
            "waveforms": {
                "single": "8330317414527296611",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2881671886459139770": {
            "length": 16,
            "waveforms": {
                "single": "2881671886459139770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3890283890333426282": {
            "length": 16,
            "waveforms": {
                "single": "-3890283890333426282",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "729567551849657094": {
            "length": 16,
            "waveforms": {
                "single": "729567551849657094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8844994729157241667": {
            "length": 16,
            "waveforms": {
                "single": "-8844994729157241667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2463963094953608548": {
            "length": 16,
            "waveforms": {
                "single": "-2463963094953608548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8781862824766281847": {
            "length": 16,
            "waveforms": {
                "single": "8781862824766281847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1114507768244731478": {
            "length": 16,
            "waveforms": {
                "single": "1114507768244731478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8382031116078303551": {
            "length": 16,
            "waveforms": {
                "single": "8382031116078303551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1192531164928595210": {
            "length": 16,
            "waveforms": {
                "single": "-1192531164928595210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8859886221450145579": {
            "length": 16,
            "waveforms": {
                "single": "-8859886221450145579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6735803720882394355": {
            "length": 16,
            "waveforms": {
                "single": "6735803720882394355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8766971332473377935": {
            "length": 20,
            "waveforms": {
                "single": "8766971332473377935",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6414605663711083715": {
            "length": 20,
            "waveforms": {
                "single": "6414605663711083715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-586096889334805578": {
            "length": 20,
            "waveforms": {
                "single": "-586096889334805578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5516085492408387957": {
            "length": 20,
            "waveforms": {
                "single": "5516085492408387957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4058476788598510804": {
            "length": 24,
            "waveforms": {
                "single": "-4058476788598510804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4601168904968536692": {
            "length": 24,
            "waveforms": {
                "single": "-4601168904968536692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6844872615695125631": {
            "length": 24,
            "waveforms": {
                "single": "6844872615695125631",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4656869249185823658": {
            "length": 24,
            "waveforms": {
                "single": "-4656869249185823658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3548660040041168121": {
            "length": 28,
            "waveforms": {
                "single": "3548660040041168121",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6690266634935998274": {
            "length": 28,
            "waveforms": {
                "single": "6690266634935998274",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3051294659260109765": {
            "length": 28,
            "waveforms": {
                "single": "3051294659260109765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2774100255844107551": {
            "length": 28,
            "waveforms": {
                "single": "2774100255844107551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5249054347263276628": {
            "length": 32,
            "waveforms": {
                "single": "5249054347263276628",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2646709177201755463": {
            "length": 32,
            "waveforms": {
                "single": "2646709177201755463",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4104013874544906885": {
            "length": 32,
            "waveforms": {
                "single": "-4104013874544906885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5047860781436570175": {
            "length": 32,
            "waveforms": {
                "single": "-5047860781436570175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-525543011346566859": {
            "length": 36,
            "waveforms": {
                "single": "-525543011346566859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5855488622857066260": {
            "length": 36,
            "waveforms": {
                "single": "5855488622857066260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3326955630485024324": {
            "length": 36,
            "waveforms": {
                "single": "3326955630485024324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3225928550678769826": {
            "length": 36,
            "waveforms": {
                "single": "3225928550678769826",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2604602782792076282": {
            "length": 40,
            "waveforms": {
                "single": "2604602782792076282",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7126920552882079598": {
            "length": 40,
            "waveforms": {
                "single": "7126920552882079598",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-540434503639470771": {
            "length": 40,
            "waveforms": {
                "single": "-540434503639470771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8331747289063182084": {
            "length": 40,
            "waveforms": {
                "single": "8331747289063182084",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7568351958802135333": {
            "length": 44,
            "waveforms": {
                "single": "-7568351958802135333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3888854015797540809": {
            "length": 44,
            "waveforms": {
                "single": "-3888854015797540809",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3667359956598825561": {
            "length": 44,
            "waveforms": {
                "single": "-3667359956598825561",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "139811949643798090": {
            "length": 44,
            "waveforms": {
                "single": "139811949643798090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4260974929212164004": {
            "length": 48,
            "waveforms": {
                "single": "4260974929212164004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4482468988410879252": {
            "length": 48,
            "waveforms": {
                "single": "4482468988410879252",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3282419740203751177": {
            "length": 48,
            "waveforms": {
                "single": "-3282419740203751177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6477605236051454189": {
            "length": 48,
            "waveforms": {
                "single": "-6477605236051454189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1084660052200584314": {
            "length": 52,
            "waveforms": {
                "single": "-1084660052200584314",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6533305580268741155": {
            "length": 52,
            "waveforms": {
                "single": "-6533305580268741155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2726133674026117504": {
            "length": 52,
            "waveforms": {
                "single": "-2726133674026117504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4370043824024895280": {
            "length": 52,
            "waveforms": {
                "single": "4370043824024895280",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7360475129697314976": {
            "length": 56,
            "waveforms": {
                "single": "7360475129697314976",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6148365363873666771": {
            "length": 56,
            "waveforms": {
                "single": "-6148365363873666771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4215437843265767923": {
            "length": 56,
            "waveforms": {
                "single": "4215437843265767923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1613092673204246758": {
            "length": 56,
            "waveforms": {
                "single": "1613092673204246758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3729111616671784660": {
            "length": 60,
            "waveforms": {
                "single": "-3729111616671784660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7124089578205695816": {
            "length": 60,
            "waveforms": {
                "single": "7124089578205695816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6800336725413852484": {
            "length": 60,
            "waveforms": {
                "single": "-6800336725413852484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6578842666215137236": {
            "length": 60,
            "waveforms": {
                "single": "-6578842666215137236",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6856037069631139450": {
            "length": 64,
            "waveforms": {
                "single": "-6856037069631139450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1349492219595852329": {
            "length": 64,
            "waveforms": {
                "single": "1349492219595852329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6317862836925698040": {
            "length": 64,
            "waveforms": {
                "single": "-6317862836925698040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5250484221799162101": {
            "length": 64,
            "waveforms": {
                "single": "5250484221799162101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5471978280997877349": {
            "length": 68,
            "waveforms": {
                "single": "5471978280997877349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8780461724625783538": {
            "length": 68,
            "waveforms": {
                "single": "8780461724625783538",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9001955783824498786": {
            "length": 68,
            "waveforms": {
                "single": "9001955783824498786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4922470519795049514": {
            "length": 68,
            "waveforms": {
                "single": "-4922470519795049514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5856918497392951733": {
            "length": 72,
            "waveforms": {
                "single": "5856918497392951733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7025534542683170719": {
            "length": 72,
            "waveforms": {
                "single": "-7025534542683170719",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2013818784855121621": {
            "length": 72,
            "waveforms": {
                "single": "-2013818784855121621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1792324725656406373": {
            "length": 72,
            "waveforms": {
                "single": "-1792324725656406373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2729993044433596943": {
            "length": 76,
            "waveforms": {
                "single": "2729993044433596943",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "405434962346760490": {
            "length": 76,
            "waveforms": {
                "single": "405434962346760490",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4927752732436763806": {
            "length": 76,
            "waveforms": {
                "single": "4927752732436763806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2990972873723036139": {
            "length": 76,
            "waveforms": {
                "single": "2990972873723036139",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3759750178023626209": {
            "length": 80,
            "waveforms": {
                "single": "-3759750178023626209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5369162396263082997": {
            "length": 80,
            "waveforms": {
                "single": "-5369162396263082997",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1561990490020459346": {
            "length": 80,
            "waveforms": {
                "single": "-1561990490020459346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2823500254667142765": {
            "length": 40,
            "waveforms": {
                "I": "2823500254667142765_i",
                "Q": "2823500254667142765_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "2062409625443580896_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
        },
        "2062409625443580896_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "4927730990343027262": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-7491253477418967775_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-7491253477418967775_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5911063667325414500": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "7125490678346194125": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "4523145508284672960": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "8330317414527296611": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "2881671886459139770": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-3890283890333426282": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "729567551849657094": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8844994729157241667": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-2463963094953608548": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "8781862824766281847": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "1114507768244731478": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "8382031116078303551": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1192531164928595210": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8859886221450145579": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
        },
        "6735803720882394355": {
            "sample": 0.175,
            "type": "constant",
        },
        "8766971332473377935": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6414605663711083715": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-586096889334805578": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
        },
        "5516085492408387957": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4058476788598510804": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4601168904968536692": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6844872615695125631": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-4656869249185823658": {
            "sample": 0.175,
            "type": "constant",
        },
        "3548660040041168121": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6690266634935998274": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3051294659260109765": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
        },
        "2774100255844107551": {
            "sample": 0.175,
            "type": "constant",
        },
        "5249054347263276628": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2646709177201755463": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4104013874544906885": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-5047860781436570175": {
            "sample": 0.175,
            "type": "constant",
        },
        "-525543011346566859": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5855488622857066260": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3326955630485024324": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
        },
        "3225928550678769826": {
            "sample": 0.175,
            "type": "constant",
        },
        "2604602782792076282": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7126920552882079598": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-540434503639470771": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
        },
        "8331747289063182084": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7568351958802135333": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3888854015797540809": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3667359956598825561": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
        },
        "139811949643798090": {
            "sample": 0.175,
            "type": "constant",
        },
        "4260974929212164004": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4482468988410879252": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3282419740203751177": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-6477605236051454189": {
            "sample": 0.175,
            "type": "constant",
        },
        "-1084660052200584314": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6533305580268741155": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2726133674026117504": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
        },
        "4370043824024895280": {
            "sample": 0.175,
            "type": "constant",
        },
        "7360475129697314976": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6148365363873666771": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4215437843265767923": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
        },
        "1613092673204246758": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3729111616671784660": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7124089578205695816": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6800336725413852484": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-6578842666215137236": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6856037069631139450": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1349492219595852329": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6317862836925698040": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
        },
        "5250484221799162101": {
            "sample": 0.175,
            "type": "constant",
        },
        "5471978280997877349": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8780461724625783538": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9001955783824498786": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-4922470519795049514": {
            "sample": 0.175,
            "type": "constant",
        },
        "5856918497392951733": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7025534542683170719": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2013818784855121621": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-1792324725656406373": {
            "sample": 0.175,
            "type": "constant",
        },
        "2729993044433596943": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "405434962346760490": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4927752732436763806": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
        },
        "2990972873723036139": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3759750178023626209": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5369162396263082997": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1561990490020459346": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
        },
        "2823500254667142765_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "2823500254667142765_q": {
            "samples": [-0.00032311264588480903, -0.00041249837971684626, -0.0005169325628573798, -0.000635681039060383, -0.0007667620891775804, -0.000906744030872699, -0.0010506362701201647, -0.0011919133952948808, -0.0013227042327271718, -0.0014341631722800618, -0.0015170202748124885, -0.0015622817771297343, -0.0015620269226550444, -0.0015102246938684684, -0.0014034792875244936, -0.0012416096759145334, -0.0010279784823387492, -0.0007695087141126592, -0.0004763613256793087, -0.00016128764167269125, 0.00016128764167269125, 0.0004763613256793087, 0.0007695087141126592, 0.0010279784823387492, 0.0012416096759145334, 0.0014034792875244936, 0.0015102246938684684, 0.0015620269226550444, 0.0015622817771297343, 0.0015170202748124885, 0.0014341631722800618, 0.0013227042327271718, 0.0011919133952948808, 0.0010506362701201647, 0.000906744030872699, 0.0007667620891775804, 0.000635681039060383, 0.0005169325628573798, 0.00041249837971684626, 0.00032311264588480903],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.08233987198571363,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": 0.30438797397930567,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.30347347513189465,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.078098681992251, -0.923066404629278],
                        "feedback": [0.9999990463256836, -0.8449677226370271],
                    },
                },
                "5": {
                    "offset": -0.2839878581260484,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.21674190528643072,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "7": {
                    "offset": -0.04,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
        },
        "con2": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
        "con3": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "8": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 1),
            },
        },
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
            },
        },
        "B2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 2),
            },
        },
        "D2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 4),
            },
        },
        "B3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 3),
            },
        },
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 5),
            },
        },
        "B4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "operations": {
                "-6856037069631139450": "-6856037069631139450",
                "1349492219595852329": "1349492219595852329",
                "-6317862836925698040": "-6317862836925698040",
                "5250484221799162101": "5250484221799162101",
                "5471978280997877349": "5471978280997877349",
                "8780461724625783538": "8780461724625783538",
                "9001955783824498786": "9001955783824498786",
                "-4922470519795049514": "-4922470519795049514",
                "5856918497392951733": "5856918497392951733",
                "-7025534542683170719": "-7025534542683170719",
                "-2013818784855121621": "-2013818784855121621",
                "-1792324725656406373": "-1792324725656406373",
                "2729993044433596943": "2729993044433596943",
                "405434962346760490": "405434962346760490",
                "4927752732436763806": "4927752732436763806",
                "2990972873723036139": "2990972873723036139",
                "-3759750178023626209": "-3759750178023626209",
                "-5369162396263082997": "-5369162396263082997",
                "-1561990490020459346": "-1561990490020459346",
            },
            "singleInput": {
                "port": ('con4', 4),
            },
        },
        "D4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 6),
            },
        },
        "B5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 5),
            },
        },
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 7),
            },
        },
        "B4/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1),
                "out2": ('con2', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": 330298316.0,
            "operations": {
                "1267399234458798216": "1267399234458798216_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_ba7",
                "lo_frequency": 7370000000.0,
            },
        },
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 109678455.0,
            "operations": {
                "2062409625443580896": "2062409625443580896",
                "2823500254667142765": "2823500254667142765",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_386",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "2062409625443580896": {
            "length": 40,
            "waveforms": {
                "I": "2062409625443580896_i",
                "Q": "2062409625443580896_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4927730990343027262": {
            "length": 16,
            "waveforms": {
                "single": "4927730990343027262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1267399234458798216_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7491253477418967775_i",
                "Q": "-7491253477418967775_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "5911063667325414500": {
            "length": 16,
            "waveforms": {
                "single": "5911063667325414500",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7125490678346194125": {
            "length": 16,
            "waveforms": {
                "single": "7125490678346194125",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4523145508284672960": {
            "length": 16,
            "waveforms": {
                "single": "4523145508284672960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8330317414527296611": {
            "length": 16,
            "waveforms": {
                "single": "8330317414527296611",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2881671886459139770": {
            "length": 16,
            "waveforms": {
                "single": "2881671886459139770",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3890283890333426282": {
            "length": 16,
            "waveforms": {
                "single": "-3890283890333426282",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "729567551849657094": {
            "length": 16,
            "waveforms": {
                "single": "729567551849657094",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8844994729157241667": {
            "length": 16,
            "waveforms": {
                "single": "-8844994729157241667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2463963094953608548": {
            "length": 16,
            "waveforms": {
                "single": "-2463963094953608548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8781862824766281847": {
            "length": 16,
            "waveforms": {
                "single": "8781862824766281847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1114507768244731478": {
            "length": 16,
            "waveforms": {
                "single": "1114507768244731478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8382031116078303551": {
            "length": 16,
            "waveforms": {
                "single": "8382031116078303551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1192531164928595210": {
            "length": 16,
            "waveforms": {
                "single": "-1192531164928595210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8859886221450145579": {
            "length": 16,
            "waveforms": {
                "single": "-8859886221450145579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6735803720882394355": {
            "length": 16,
            "waveforms": {
                "single": "6735803720882394355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8766971332473377935": {
            "length": 20,
            "waveforms": {
                "single": "8766971332473377935",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6414605663711083715": {
            "length": 20,
            "waveforms": {
                "single": "6414605663711083715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-586096889334805578": {
            "length": 20,
            "waveforms": {
                "single": "-586096889334805578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5516085492408387957": {
            "length": 20,
            "waveforms": {
                "single": "5516085492408387957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4058476788598510804": {
            "length": 24,
            "waveforms": {
                "single": "-4058476788598510804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4601168904968536692": {
            "length": 24,
            "waveforms": {
                "single": "-4601168904968536692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6844872615695125631": {
            "length": 24,
            "waveforms": {
                "single": "6844872615695125631",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4656869249185823658": {
            "length": 24,
            "waveforms": {
                "single": "-4656869249185823658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3548660040041168121": {
            "length": 28,
            "waveforms": {
                "single": "3548660040041168121",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6690266634935998274": {
            "length": 28,
            "waveforms": {
                "single": "6690266634935998274",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3051294659260109765": {
            "length": 28,
            "waveforms": {
                "single": "3051294659260109765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2774100255844107551": {
            "length": 28,
            "waveforms": {
                "single": "2774100255844107551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5249054347263276628": {
            "length": 32,
            "waveforms": {
                "single": "5249054347263276628",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2646709177201755463": {
            "length": 32,
            "waveforms": {
                "single": "2646709177201755463",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4104013874544906885": {
            "length": 32,
            "waveforms": {
                "single": "-4104013874544906885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5047860781436570175": {
            "length": 32,
            "waveforms": {
                "single": "-5047860781436570175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-525543011346566859": {
            "length": 36,
            "waveforms": {
                "single": "-525543011346566859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5855488622857066260": {
            "length": 36,
            "waveforms": {
                "single": "5855488622857066260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3326955630485024324": {
            "length": 36,
            "waveforms": {
                "single": "3326955630485024324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3225928550678769826": {
            "length": 36,
            "waveforms": {
                "single": "3225928550678769826",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2604602782792076282": {
            "length": 40,
            "waveforms": {
                "single": "2604602782792076282",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7126920552882079598": {
            "length": 40,
            "waveforms": {
                "single": "7126920552882079598",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-540434503639470771": {
            "length": 40,
            "waveforms": {
                "single": "-540434503639470771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8331747289063182084": {
            "length": 40,
            "waveforms": {
                "single": "8331747289063182084",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7568351958802135333": {
            "length": 44,
            "waveforms": {
                "single": "-7568351958802135333",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3888854015797540809": {
            "length": 44,
            "waveforms": {
                "single": "-3888854015797540809",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3667359956598825561": {
            "length": 44,
            "waveforms": {
                "single": "-3667359956598825561",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "139811949643798090": {
            "length": 44,
            "waveforms": {
                "single": "139811949643798090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4260974929212164004": {
            "length": 48,
            "waveforms": {
                "single": "4260974929212164004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4482468988410879252": {
            "length": 48,
            "waveforms": {
                "single": "4482468988410879252",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3282419740203751177": {
            "length": 48,
            "waveforms": {
                "single": "-3282419740203751177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6477605236051454189": {
            "length": 48,
            "waveforms": {
                "single": "-6477605236051454189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1084660052200584314": {
            "length": 52,
            "waveforms": {
                "single": "-1084660052200584314",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6533305580268741155": {
            "length": 52,
            "waveforms": {
                "single": "-6533305580268741155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2726133674026117504": {
            "length": 52,
            "waveforms": {
                "single": "-2726133674026117504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4370043824024895280": {
            "length": 52,
            "waveforms": {
                "single": "4370043824024895280",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7360475129697314976": {
            "length": 56,
            "waveforms": {
                "single": "7360475129697314976",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6148365363873666771": {
            "length": 56,
            "waveforms": {
                "single": "-6148365363873666771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4215437843265767923": {
            "length": 56,
            "waveforms": {
                "single": "4215437843265767923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1613092673204246758": {
            "length": 56,
            "waveforms": {
                "single": "1613092673204246758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3729111616671784660": {
            "length": 60,
            "waveforms": {
                "single": "-3729111616671784660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7124089578205695816": {
            "length": 60,
            "waveforms": {
                "single": "7124089578205695816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6800336725413852484": {
            "length": 60,
            "waveforms": {
                "single": "-6800336725413852484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6578842666215137236": {
            "length": 60,
            "waveforms": {
                "single": "-6578842666215137236",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6856037069631139450": {
            "length": 64,
            "waveforms": {
                "single": "-6856037069631139450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1349492219595852329": {
            "length": 64,
            "waveforms": {
                "single": "1349492219595852329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6317862836925698040": {
            "length": 64,
            "waveforms": {
                "single": "-6317862836925698040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5250484221799162101": {
            "length": 64,
            "waveforms": {
                "single": "5250484221799162101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5471978280997877349": {
            "length": 68,
            "waveforms": {
                "single": "5471978280997877349",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8780461724625783538": {
            "length": 68,
            "waveforms": {
                "single": "8780461724625783538",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9001955783824498786": {
            "length": 68,
            "waveforms": {
                "single": "9001955783824498786",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4922470519795049514": {
            "length": 68,
            "waveforms": {
                "single": "-4922470519795049514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5856918497392951733": {
            "length": 72,
            "waveforms": {
                "single": "5856918497392951733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7025534542683170719": {
            "length": 72,
            "waveforms": {
                "single": "-7025534542683170719",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2013818784855121621": {
            "length": 72,
            "waveforms": {
                "single": "-2013818784855121621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1792324725656406373": {
            "length": 72,
            "waveforms": {
                "single": "-1792324725656406373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2729993044433596943": {
            "length": 76,
            "waveforms": {
                "single": "2729993044433596943",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "405434962346760490": {
            "length": 76,
            "waveforms": {
                "single": "405434962346760490",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4927752732436763806": {
            "length": 76,
            "waveforms": {
                "single": "4927752732436763806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2990972873723036139": {
            "length": 76,
            "waveforms": {
                "single": "2990972873723036139",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3759750178023626209": {
            "length": 80,
            "waveforms": {
                "single": "-3759750178023626209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5369162396263082997": {
            "length": 80,
            "waveforms": {
                "single": "-5369162396263082997",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1561990490020459346": {
            "length": 80,
            "waveforms": {
                "single": "-1561990490020459346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2823500254667142765": {
            "length": 40,
            "waveforms": {
                "I": "2823500254667142765_i",
                "Q": "2823500254667142765_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "2062409625443580896_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2062409625443580896_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4927730990343027262": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7491253477418967775_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-7491253477418967775_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5911063667325414500": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7125490678346194125": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4523145508284672960": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8330317414527296611": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2881671886459139770": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3890283890333426282": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "729567551849657094": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8844994729157241667": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2463963094953608548": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8781862824766281847": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1114507768244731478": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8382031116078303551": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1192531164928595210": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8859886221450145579": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6735803720882394355": {
            "sample": 0.175,
            "type": "constant",
        },
        "8766971332473377935": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6414605663711083715": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-586096889334805578": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5516085492408387957": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4058476788598510804": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4601168904968536692": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6844872615695125631": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4656869249185823658": {
            "sample": 0.175,
            "type": "constant",
        },
        "3548660040041168121": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6690266634935998274": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3051294659260109765": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2774100255844107551": {
            "sample": 0.175,
            "type": "constant",
        },
        "5249054347263276628": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2646709177201755463": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4104013874544906885": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5047860781436570175": {
            "sample": 0.175,
            "type": "constant",
        },
        "-525543011346566859": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5855488622857066260": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3326955630485024324": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3225928550678769826": {
            "sample": 0.175,
            "type": "constant",
        },
        "2604602782792076282": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7126920552882079598": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-540434503639470771": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8331747289063182084": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7568351958802135333": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3888854015797540809": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3667359956598825561": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "139811949643798090": {
            "sample": 0.175,
            "type": "constant",
        },
        "4260974929212164004": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4482468988410879252": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3282419740203751177": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6477605236051454189": {
            "sample": 0.175,
            "type": "constant",
        },
        "-1084660052200584314": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6533305580268741155": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2726133674026117504": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4370043824024895280": {
            "sample": 0.175,
            "type": "constant",
        },
        "7360475129697314976": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6148365363873666771": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4215437843265767923": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1613092673204246758": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3729111616671784660": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7124089578205695816": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6800336725413852484": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6578842666215137236": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6856037069631139450": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1349492219595852329": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6317862836925698040": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5250484221799162101": {
            "sample": 0.175,
            "type": "constant",
        },
        "5471978280997877349": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8780461724625783538": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9001955783824498786": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4922470519795049514": {
            "sample": 0.175,
            "type": "constant",
        },
        "5856918497392951733": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7025534542683170719": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2013818784855121621": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1792324725656406373": {
            "sample": 0.175,
            "type": "constant",
        },
        "2729993044433596943": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "405434962346760490": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4927752732436763806": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2990972873723036139": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3759750178023626209": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5369162396263082997": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1561990490020459346": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2823500254667142765_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2823500254667142765_q": {
            "samples": [-0.00032311264588480903, -0.00041249837971684626, -0.0005169325628573798, -0.000635681039060383, -0.0007667620891775804, -0.000906744030872699, -0.0010506362701201647, -0.0011919133952948808, -0.0013227042327271718, -0.0014341631722800618, -0.0015170202748124885, -0.0015622817771297343, -0.0015620269226550444, -0.0015102246938684684, -0.0014034792875244936, -0.0012416096759145334, -0.0010279784823387492, -0.0007695087141126592, -0.0004763613256793087, -0.00016128764167269125, 0.00016128764167269125, 0.0004763613256793087, 0.0007695087141126592, 0.0010279784823387492, 0.0012416096759145334, 0.0014034792875244936, 0.0015102246938684684, 0.0015620269226550444, 0.0015622817771297343, 0.0015170202748124885, 0.0014341631722800618, 0.0013227042327271718, 0.0011919133952948808, 0.0010506362701201647, 0.000906744030872699, 0.0007667620891775804, 0.000635681039060383, 0.0005169325628573798, 0.00041249837971684626, 0.00032311264588480903],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B4/acquisition_mixer_ba7": [{'intermediate_frequency': 330298316.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_386": [{'intermediate_frequency': 109678455.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

