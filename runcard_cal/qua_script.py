
# Single QUA script generated at 2025-01-17 18:54:44.888774
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
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("3796485094611735101", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-4397366011199990497", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("6455835183677489979", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-9074289762049121170", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-2820932091083517178", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("8875088930879372090", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("3255097553028655960", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-1643320257019189961", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("5452857241031822823", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-4788357543450737014", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-4566863484252021766", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("444852273576027332", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("6009143307209456496", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-7915282996410091804", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("2864106020777909443", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("3085600079976624691", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("5061865708781076306", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("6615577582803246128", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        play("-8613502842919136169", "B4/drive")
        wait(11, "B4/flux")
        play("-7308848720816302172", "B4/flux")
        wait(46, "B4/drive")
        play("-3454054830711206172", "B4/drive")
        wait(66, "B4/acquisition")
        measure("7749939089205388608", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.3706887495702447)-(v3*0.9287571539116393))>-0.0002612278861125033)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("7749939089205388608_B4|acquisition_shots")


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
                        "feedforward": [],
                        "feedback": [],
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
                "3796485094611735101": "3796485094611735101",
                "-4397366011199990497": "-4397366011199990497",
                "6455835183677489979": "6455835183677489979",
                "-9074289762049121170": "-9074289762049121170",
                "-2820932091083517178": "-2820932091083517178",
                "8875088930879372090": "8875088930879372090",
                "3255097553028655960": "3255097553028655960",
                "-1643320257019189961": "-1643320257019189961",
                "5452857241031822823": "5452857241031822823",
                "-4788357543450737014": "-4788357543450737014",
                "-4566863484252021766": "-4566863484252021766",
                "444852273576027332": "444852273576027332",
                "6009143307209456496": "6009143307209456496",
                "-7915282996410091804": "-7915282996410091804",
                "2864106020777909443": "2864106020777909443",
                "3085600079976624691": "3085600079976624691",
                "5061865708781076306": "5061865708781076306",
                "6615577582803246128": "6615577582803246128",
                "-7308848720816302172": "-7308848720816302172",
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
                "7749939089205388608": "7749939089205388608_B4/acquisition",
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
                "-8613502842919136169": "-8613502842919136169",
                "-3454054830711206172": "-3454054830711206172",
            },
        },
    },
    "pulses": {
        "-8613502842919136169": {
            "length": 40,
            "waveforms": {
                "I": "-8613502842919136169_i",
                "Q": "-8613502842919136169_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8707976356173081181": {
            "length": 16,
            "waveforms": {
                "single": "-8707976356173081181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7749939089205388608_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "2634772637533731547_i",
                "Q": "2634772637533731547_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "1254672060444716111": {
            "length": 16,
            "waveforms": {
                "single": "1254672060444716111",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6266387818272765209": {
            "length": 16,
            "waveforms": {
                "single": "6266387818272765209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3914022149510470989": {
            "length": 16,
            "waveforms": {
                "single": "3914022149510470989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7436544426148067843": {
            "length": 16,
            "waveforms": {
                "single": "-7436544426148067843",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8685641565474647320": {
            "length": 16,
            "waveforms": {
                "single": "8685641565474647320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6333275896712353100": {
            "length": 16,
            "waveforms": {
                "single": "6333275896712353100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6872822093866554841": {
            "length": 16,
            "waveforms": {
                "single": "6872822093866554841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4520456425104260621": {
            "length": 16,
            "waveforms": {
                "single": "4520456425104260621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1487313176119564295": {
            "length": 16,
            "waveforms": {
                "single": "-1487313176119564295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6718216113107427484": {
            "length": 16,
            "waveforms": {
                "single": "6718216113107427484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6939710172306142732": {
            "length": 16,
            "waveforms": {
                "single": "6939710172306142732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6220850732326369128": {
            "length": 16,
            "waveforms": {
                "single": "6220850732326369128",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9137469860309309595": {
            "length": 16,
            "waveforms": {
                "single": "9137469860309309595",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4297558455572192923": {
            "length": 16,
            "waveforms": {
                "single": "-4297558455572192923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4076064396373477675": {
            "length": 16,
            "waveforms": {
                "single": "-4076064396373477675",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "446253373716525641": {
            "length": 20,
            "waveforms": {
                "single": "446253373716525641",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1878304708370310812": {
            "length": 20,
            "waveforms": {
                "single": "-1878304708370310812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1656810649171595564": {
            "length": 20,
            "waveforms": {
                "single": "-1656810649171595564",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3354905108656453534": {
            "length": 20,
            "waveforms": {
                "single": "3354905108656453534",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3576399167855168782": {
            "length": 24,
            "waveforms": {
                "single": "3576399167855168782",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5005230161329665602": {
            "length": 24,
            "waveforms": {
                "single": "-5005230161329665602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5774158855858335645": {
            "length": 24,
            "waveforms": {
                "single": "5774158855858335645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2419692249953389953": {
            "length": 24,
            "waveforms": {
                "single": "-2419692249953389953",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7439375400824451625": {
            "length": 28,
            "waveforms": {
                "single": "-7439375400824451625",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8655003004122805771": {
            "length": 28,
            "waveforms": {
                "single": "8655003004122805771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-438502751507842": {
            "length": 28,
            "waveforms": {
                "single": "-438502751507842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5020121653622569514": {
            "length": 28,
            "waveforms": {
                "single": "-5020121653622569514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5232771314275256504": {
            "length": 32,
            "waveforms": {
                "single": "5232771314275256504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2434583742246293865": {
            "length": 32,
            "waveforms": {
                "single": "-2434583742246293865",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5174727634381696871": {
            "length": 32,
            "waveforms": {
                "single": "-5174727634381696871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7652025061477138615": {
            "length": 32,
            "waveforms": {
                "single": "7652025061477138615",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6987547105989789350": {
            "length": 36,
            "waveforms": {
                "single": "-6987547105989789350",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5561509195205648655": {
            "length": 36,
            "waveforms": {
                "single": "-5561509195205648655",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4789787417986622487": {
            "length": 36,
            "waveforms": {
                "single": "-4789787417986622487",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3363749507202481792": {
            "length": 36,
            "waveforms": {
                "single": "-3363749507202481792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "443422399040141859": {
            "length": 40,
            "waveforms": {
                "single": "443422399040141859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5063273841223225235": {
            "length": 40,
            "waveforms": {
                "single": "5063273841223225235",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-944495760000599681": {
            "length": 40,
            "waveforms": {
                "single": "-944495760000599681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2862676146242023970": {
            "length": 40,
            "waveforms": {
                "single": "2862676146242023970",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1714854329065155197": {
            "length": 44,
            "waveforms": {
                "single": "1714854329065155197",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5952500727456395172": {
            "length": 44,
            "waveforms": {
                "single": "-5952500727456395172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6486473745029331528": {
            "length": 44,
            "waveforms": {
                "single": "6486473745029331528",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4134108076267037308": {
            "length": 44,
            "waveforms": {
                "single": "4134108076267037308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3533246980254513061": {
            "length": 48,
            "waveforms": {
                "single": "-3533246980254513061",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2321288604658944829": {
            "length": 48,
            "waveforms": {
                "single": "2321288604658944829",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1699962836772251285": {
            "length": 48,
            "waveforms": {
                "single": "1699962836772251285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4519048292662111692": {
            "length": 48,
            "waveforms": {
                "single": "4519048292662111692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4740542351860826940": {
            "length": 52,
            "waveforms": {
                "single": "4740542351860826940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8694485964020675578": {
            "length": 52,
            "waveforms": {
                "single": "-8694485964020675578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8472991904821960330": {
            "length": 52,
            "waveforms": {
                "single": "-8472991904821960330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1489656511795836962": {
            "length": 52,
            "waveforms": {
                "single": "1489656511795836962",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6275232216818793467": {
            "length": 56,
            "waveforms": {
                "single": "-6275232216818793467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6053738157620078219": {
            "length": 56,
            "waveforms": {
                "single": "-6053738157620078219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3356334983192339007": {
            "length": 56,
            "waveforms": {
                "single": "3356334983192339007",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3855978469616911356": {
            "length": 56,
            "waveforms": {
                "single": "-3855978469616911356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4349550819610080423": {
            "length": 60,
            "waveforms": {
                "single": "4349550819610080423",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5775588730394221118": {
            "length": 60,
            "waveforms": {
                "single": "5775588730394221118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8863983437072706847": {
            "length": 60,
            "waveforms": {
                "single": "-8863983437072706847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3574991035413019853": {
            "length": 60,
            "waveforms": {
                "single": "3574991035413019853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3796485094611735101": {
            "length": 64,
            "waveforms": {
                "single": "3796485094611735101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4397366011199990497": {
            "length": 64,
            "waveforms": {
                "single": "-4397366011199990497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6455835183677489979": {
            "length": 64,
            "waveforms": {
                "single": "6455835183677489979",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9074289762049121170": {
            "length": 64,
            "waveforms": {
                "single": "-9074289762049121170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2820932091083517178": {
            "length": 68,
            "waveforms": {
                "single": "-2820932091083517178",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8875088930879372090": {
            "length": 68,
            "waveforms": {
                "single": "8875088930879372090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3255097553028655960": {
            "length": 68,
            "waveforms": {
                "single": "3255097553028655960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1643320257019189961": {
            "length": 68,
            "waveforms": {
                "single": "-1643320257019189961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5452857241031822823": {
            "length": 72,
            "waveforms": {
                "single": "5452857241031822823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4788357543450737014": {
            "length": 72,
            "waveforms": {
                "single": "-4788357543450737014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4566863484252021766": {
            "length": 72,
            "waveforms": {
                "single": "-4566863484252021766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "444852273576027332": {
            "length": 72,
            "waveforms": {
                "single": "444852273576027332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6009143307209456496": {
            "length": 76,
            "waveforms": {
                "single": "6009143307209456496",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7915282996410091804": {
            "length": 76,
            "waveforms": {
                "single": "-7915282996410091804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2864106020777909443": {
            "length": 76,
            "waveforms": {
                "single": "2864106020777909443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3085600079976624691": {
            "length": 76,
            "waveforms": {
                "single": "3085600079976624691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5061865708781076306": {
            "length": 80,
            "waveforms": {
                "single": "5061865708781076306",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6615577582803246128": {
            "length": 80,
            "waveforms": {
                "single": "6615577582803246128",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7308848720816302172": {
            "length": 80,
            "waveforms": {
                "single": "-7308848720816302172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3454054830711206172": {
            "length": 40,
            "waveforms": {
                "I": "-3454054830711206172_i",
                "Q": "-3454054830711206172_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8613502842919136169_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
        },
        "-8613502842919136169_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "-8707976356173081181": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
        },
        "2634772637533731547_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "2634772637533731547_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1254672060444716111": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "6266387818272765209": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "3914022149510470989": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-7436544426148067843": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "8685641565474647320": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "6333275896712353100": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "6872822093866554841": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "4520456425104260621": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-1487313176119564295": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "6718216113107427484": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "6939710172306142732": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "6220850732326369128": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9137469860309309595": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4297558455572192923": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-4076064396373477675": {
            "sample": 0.175,
            "type": "constant",
        },
        "446253373716525641": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1878304708370310812": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1656810649171595564": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
        },
        "3354905108656453534": {
            "sample": 0.175,
            "type": "constant",
        },
        "3576399167855168782": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5005230161329665602": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5774158855858335645": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-2419692249953389953": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7439375400824451625": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8655003004122805771": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-438502751507842": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-5020121653622569514": {
            "sample": 0.175,
            "type": "constant",
        },
        "5232771314275256504": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2434583742246293865": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5174727634381696871": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
        },
        "7652025061477138615": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6987547105989789350": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5561509195205648655": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4789787417986622487": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-3363749507202481792": {
            "sample": 0.175,
            "type": "constant",
        },
        "443422399040141859": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5063273841223225235": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-944495760000599681": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
        },
        "2862676146242023970": {
            "sample": 0.175,
            "type": "constant",
        },
        "1714854329065155197": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5952500727456395172": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6486473745029331528": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
        },
        "4134108076267037308": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3533246980254513061": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2321288604658944829": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1699962836772251285": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
        },
        "4519048292662111692": {
            "sample": 0.175,
            "type": "constant",
        },
        "4740542351860826940": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8694485964020675578": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8472991904821960330": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
        },
        "1489656511795836962": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6275232216818793467": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6053738157620078219": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3356334983192339007": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-3855978469616911356": {
            "sample": 0.175,
            "type": "constant",
        },
        "4349550819610080423": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5775588730394221118": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8863983437072706847": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
        },
        "3574991035413019853": {
            "sample": 0.175,
            "type": "constant",
        },
        "3796485094611735101": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4397366011199990497": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6455835183677489979": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-9074289762049121170": {
            "sample": 0.175,
            "type": "constant",
        },
        "-2820932091083517178": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8875088930879372090": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3255097553028655960": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-1643320257019189961": {
            "sample": 0.175,
            "type": "constant",
        },
        "5452857241031822823": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4788357543450737014": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4566863484252021766": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
        },
        "444852273576027332": {
            "sample": 0.175,
            "type": "constant",
        },
        "6009143307209456496": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7915282996410091804": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2864106020777909443": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
        },
        "3085600079976624691": {
            "sample": 0.175,
            "type": "constant",
        },
        "5061865708781076306": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6615577582803246128": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7308848720816302172": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-3454054830711206172_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "-3454054830711206172_q": {
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
                        "feedforward": [],
                        "feedback": [],
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
                "3796485094611735101": "3796485094611735101",
                "-4397366011199990497": "-4397366011199990497",
                "6455835183677489979": "6455835183677489979",
                "-9074289762049121170": "-9074289762049121170",
                "-2820932091083517178": "-2820932091083517178",
                "8875088930879372090": "8875088930879372090",
                "3255097553028655960": "3255097553028655960",
                "-1643320257019189961": "-1643320257019189961",
                "5452857241031822823": "5452857241031822823",
                "-4788357543450737014": "-4788357543450737014",
                "-4566863484252021766": "-4566863484252021766",
                "444852273576027332": "444852273576027332",
                "6009143307209456496": "6009143307209456496",
                "-7915282996410091804": "-7915282996410091804",
                "2864106020777909443": "2864106020777909443",
                "3085600079976624691": "3085600079976624691",
                "5061865708781076306": "5061865708781076306",
                "6615577582803246128": "6615577582803246128",
                "-7308848720816302172": "-7308848720816302172",
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
                "7749939089205388608": "7749939089205388608_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_f8d",
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
                "-8613502842919136169": "-8613502842919136169",
                "-3454054830711206172": "-3454054830711206172",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_76e",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "-8613502842919136169": {
            "length": 40,
            "waveforms": {
                "I": "-8613502842919136169_i",
                "Q": "-8613502842919136169_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8707976356173081181": {
            "length": 16,
            "waveforms": {
                "single": "-8707976356173081181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7749939089205388608_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "2634772637533731547_i",
                "Q": "2634772637533731547_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "1254672060444716111": {
            "length": 16,
            "waveforms": {
                "single": "1254672060444716111",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6266387818272765209": {
            "length": 16,
            "waveforms": {
                "single": "6266387818272765209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3914022149510470989": {
            "length": 16,
            "waveforms": {
                "single": "3914022149510470989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7436544426148067843": {
            "length": 16,
            "waveforms": {
                "single": "-7436544426148067843",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8685641565474647320": {
            "length": 16,
            "waveforms": {
                "single": "8685641565474647320",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6333275896712353100": {
            "length": 16,
            "waveforms": {
                "single": "6333275896712353100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6872822093866554841": {
            "length": 16,
            "waveforms": {
                "single": "6872822093866554841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4520456425104260621": {
            "length": 16,
            "waveforms": {
                "single": "4520456425104260621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1487313176119564295": {
            "length": 16,
            "waveforms": {
                "single": "-1487313176119564295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6718216113107427484": {
            "length": 16,
            "waveforms": {
                "single": "6718216113107427484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6939710172306142732": {
            "length": 16,
            "waveforms": {
                "single": "6939710172306142732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6220850732326369128": {
            "length": 16,
            "waveforms": {
                "single": "6220850732326369128",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9137469860309309595": {
            "length": 16,
            "waveforms": {
                "single": "9137469860309309595",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4297558455572192923": {
            "length": 16,
            "waveforms": {
                "single": "-4297558455572192923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4076064396373477675": {
            "length": 16,
            "waveforms": {
                "single": "-4076064396373477675",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "446253373716525641": {
            "length": 20,
            "waveforms": {
                "single": "446253373716525641",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1878304708370310812": {
            "length": 20,
            "waveforms": {
                "single": "-1878304708370310812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1656810649171595564": {
            "length": 20,
            "waveforms": {
                "single": "-1656810649171595564",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3354905108656453534": {
            "length": 20,
            "waveforms": {
                "single": "3354905108656453534",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3576399167855168782": {
            "length": 24,
            "waveforms": {
                "single": "3576399167855168782",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5005230161329665602": {
            "length": 24,
            "waveforms": {
                "single": "-5005230161329665602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5774158855858335645": {
            "length": 24,
            "waveforms": {
                "single": "5774158855858335645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2419692249953389953": {
            "length": 24,
            "waveforms": {
                "single": "-2419692249953389953",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7439375400824451625": {
            "length": 28,
            "waveforms": {
                "single": "-7439375400824451625",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8655003004122805771": {
            "length": 28,
            "waveforms": {
                "single": "8655003004122805771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-438502751507842": {
            "length": 28,
            "waveforms": {
                "single": "-438502751507842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5020121653622569514": {
            "length": 28,
            "waveforms": {
                "single": "-5020121653622569514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5232771314275256504": {
            "length": 32,
            "waveforms": {
                "single": "5232771314275256504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2434583742246293865": {
            "length": 32,
            "waveforms": {
                "single": "-2434583742246293865",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5174727634381696871": {
            "length": 32,
            "waveforms": {
                "single": "-5174727634381696871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7652025061477138615": {
            "length": 32,
            "waveforms": {
                "single": "7652025061477138615",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6987547105989789350": {
            "length": 36,
            "waveforms": {
                "single": "-6987547105989789350",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5561509195205648655": {
            "length": 36,
            "waveforms": {
                "single": "-5561509195205648655",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4789787417986622487": {
            "length": 36,
            "waveforms": {
                "single": "-4789787417986622487",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3363749507202481792": {
            "length": 36,
            "waveforms": {
                "single": "-3363749507202481792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "443422399040141859": {
            "length": 40,
            "waveforms": {
                "single": "443422399040141859",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5063273841223225235": {
            "length": 40,
            "waveforms": {
                "single": "5063273841223225235",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-944495760000599681": {
            "length": 40,
            "waveforms": {
                "single": "-944495760000599681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2862676146242023970": {
            "length": 40,
            "waveforms": {
                "single": "2862676146242023970",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1714854329065155197": {
            "length": 44,
            "waveforms": {
                "single": "1714854329065155197",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5952500727456395172": {
            "length": 44,
            "waveforms": {
                "single": "-5952500727456395172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6486473745029331528": {
            "length": 44,
            "waveforms": {
                "single": "6486473745029331528",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4134108076267037308": {
            "length": 44,
            "waveforms": {
                "single": "4134108076267037308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3533246980254513061": {
            "length": 48,
            "waveforms": {
                "single": "-3533246980254513061",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2321288604658944829": {
            "length": 48,
            "waveforms": {
                "single": "2321288604658944829",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1699962836772251285": {
            "length": 48,
            "waveforms": {
                "single": "1699962836772251285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4519048292662111692": {
            "length": 48,
            "waveforms": {
                "single": "4519048292662111692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4740542351860826940": {
            "length": 52,
            "waveforms": {
                "single": "4740542351860826940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8694485964020675578": {
            "length": 52,
            "waveforms": {
                "single": "-8694485964020675578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8472991904821960330": {
            "length": 52,
            "waveforms": {
                "single": "-8472991904821960330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1489656511795836962": {
            "length": 52,
            "waveforms": {
                "single": "1489656511795836962",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6275232216818793467": {
            "length": 56,
            "waveforms": {
                "single": "-6275232216818793467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6053738157620078219": {
            "length": 56,
            "waveforms": {
                "single": "-6053738157620078219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3356334983192339007": {
            "length": 56,
            "waveforms": {
                "single": "3356334983192339007",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3855978469616911356": {
            "length": 56,
            "waveforms": {
                "single": "-3855978469616911356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4349550819610080423": {
            "length": 60,
            "waveforms": {
                "single": "4349550819610080423",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5775588730394221118": {
            "length": 60,
            "waveforms": {
                "single": "5775588730394221118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8863983437072706847": {
            "length": 60,
            "waveforms": {
                "single": "-8863983437072706847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3574991035413019853": {
            "length": 60,
            "waveforms": {
                "single": "3574991035413019853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3796485094611735101": {
            "length": 64,
            "waveforms": {
                "single": "3796485094611735101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4397366011199990497": {
            "length": 64,
            "waveforms": {
                "single": "-4397366011199990497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6455835183677489979": {
            "length": 64,
            "waveforms": {
                "single": "6455835183677489979",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9074289762049121170": {
            "length": 64,
            "waveforms": {
                "single": "-9074289762049121170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2820932091083517178": {
            "length": 68,
            "waveforms": {
                "single": "-2820932091083517178",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8875088930879372090": {
            "length": 68,
            "waveforms": {
                "single": "8875088930879372090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3255097553028655960": {
            "length": 68,
            "waveforms": {
                "single": "3255097553028655960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1643320257019189961": {
            "length": 68,
            "waveforms": {
                "single": "-1643320257019189961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5452857241031822823": {
            "length": 72,
            "waveforms": {
                "single": "5452857241031822823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4788357543450737014": {
            "length": 72,
            "waveforms": {
                "single": "-4788357543450737014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4566863484252021766": {
            "length": 72,
            "waveforms": {
                "single": "-4566863484252021766",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "444852273576027332": {
            "length": 72,
            "waveforms": {
                "single": "444852273576027332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6009143307209456496": {
            "length": 76,
            "waveforms": {
                "single": "6009143307209456496",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7915282996410091804": {
            "length": 76,
            "waveforms": {
                "single": "-7915282996410091804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2864106020777909443": {
            "length": 76,
            "waveforms": {
                "single": "2864106020777909443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3085600079976624691": {
            "length": 76,
            "waveforms": {
                "single": "3085600079976624691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5061865708781076306": {
            "length": 80,
            "waveforms": {
                "single": "5061865708781076306",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6615577582803246128": {
            "length": 80,
            "waveforms": {
                "single": "6615577582803246128",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7308848720816302172": {
            "length": 80,
            "waveforms": {
                "single": "-7308848720816302172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3454054830711206172": {
            "length": 40,
            "waveforms": {
                "I": "-3454054830711206172_i",
                "Q": "-3454054830711206172_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-8613502842919136169_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8613502842919136169_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8707976356173081181": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2634772637533731547_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "2634772637533731547_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "1254672060444716111": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6266387818272765209": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3914022149510470989": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7436544426148067843": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8685641565474647320": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6333275896712353100": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6872822093866554841": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4520456425104260621": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1487313176119564295": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6718216113107427484": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6939710172306142732": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6220850732326369128": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9137469860309309595": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4297558455572192923": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4076064396373477675": {
            "sample": 0.175,
            "type": "constant",
        },
        "446253373716525641": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1878304708370310812": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1656810649171595564": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3354905108656453534": {
            "sample": 0.175,
            "type": "constant",
        },
        "3576399167855168782": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5005230161329665602": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5774158855858335645": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2419692249953389953": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7439375400824451625": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8655003004122805771": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-438502751507842": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5020121653622569514": {
            "sample": 0.175,
            "type": "constant",
        },
        "5232771314275256504": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2434583742246293865": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5174727634381696871": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7652025061477138615": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6987547105989789350": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5561509195205648655": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4789787417986622487": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3363749507202481792": {
            "sample": 0.175,
            "type": "constant",
        },
        "443422399040141859": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5063273841223225235": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-944495760000599681": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2862676146242023970": {
            "sample": 0.175,
            "type": "constant",
        },
        "1714854329065155197": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5952500727456395172": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6486473745029331528": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4134108076267037308": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3533246980254513061": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2321288604658944829": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1699962836772251285": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4519048292662111692": {
            "sample": 0.175,
            "type": "constant",
        },
        "4740542351860826940": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8694485964020675578": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8472991904821960330": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1489656511795836962": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6275232216818793467": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6053738157620078219": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3356334983192339007": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3855978469616911356": {
            "sample": 0.175,
            "type": "constant",
        },
        "4349550819610080423": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5775588730394221118": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8863983437072706847": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3574991035413019853": {
            "sample": 0.175,
            "type": "constant",
        },
        "3796485094611735101": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4397366011199990497": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6455835183677489979": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9074289762049121170": {
            "sample": 0.175,
            "type": "constant",
        },
        "-2820932091083517178": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8875088930879372090": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3255097553028655960": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1643320257019189961": {
            "sample": 0.175,
            "type": "constant",
        },
        "5452857241031822823": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4788357543450737014": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4566863484252021766": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "444852273576027332": {
            "sample": 0.175,
            "type": "constant",
        },
        "6009143307209456496": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7915282996410091804": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2864106020777909443": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3085600079976624691": {
            "sample": 0.175,
            "type": "constant",
        },
        "5061865708781076306": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6615577582803246128": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7308848720816302172": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3454054830711206172_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3454054830711206172_q": {
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
        "B4/acquisition_mixer_f8d": [{'intermediate_frequency': 330298316.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_76e": [{'intermediate_frequency': 109678455.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

