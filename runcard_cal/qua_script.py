
# Single QUA script generated at 2025-01-17 18:20:31.926001
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
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("5436116454423998948", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-2757734651387726650", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-3379060419274420194", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("428111486968203457", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-5191879890882512673", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-5358164055056906211", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("4894728912840919807", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-2772626143680630562", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("8795720915044229579", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-574866455677463699", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-7325589507424126047", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-5899551596639985352", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("2305977692587006427", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-3701791908636818489", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("4503737380590173290", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-1116253997260542840", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-8709796876092613980", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("2524633744807687273", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        play("1609276662556365097", "B4/drive")
        wait(11, "B4/flux")
        play("-5669217361004038325", "B4/flux")
        wait(46, "B4/drive")
        play("2370367291779926966", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2774398681751789420", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.35365058764385754)-(v3*0.9353776038900836))>-0.00036830886943236044)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("2774398681751789420_B4|acquisition_shots")


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
                "5436116454423998948": "5436116454423998948",
                "-2757734651387726650": "-2757734651387726650",
                "-3379060419274420194": "-3379060419274420194",
                "428111486968203457": "428111486968203457",
                "-5191879890882512673": "-5191879890882512673",
                "-5358164055056906211": "-5358164055056906211",
                "4894728912840919807": "4894728912840919807",
                "-2772626143680630562": "-2772626143680630562",
                "8795720915044229579": "8795720915044229579",
                "-574866455677463699": "-574866455677463699",
                "-7325589507424126047": "-7325589507424126047",
                "-5899551596639985352": "-5899551596639985352",
                "2305977692587006427": "2305977692587006427",
                "-3701791908636818489": "-3701791908636818489",
                "4503737380590173290": "4503737380590173290",
                "-1116253997260542840": "-1116253997260542840",
                "-8709796876092613980": "-8709796876092613980",
                "2524633744807687273": "2524633744807687273",
                "-5669217361004038325": "-5669217361004038325",
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
                "2774398681751789420": "2774398681751789420_B4/acquisition",
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
                "1609276662556365097": "1609276662556365097",
                "2370367291779926966": "2370367291779926966",
            },
        },
    },
    "pulses": {
        "1609276662556365097": {
            "length": 40,
            "waveforms": {
                "I": "1609276662556365097_i",
                "Q": "1609276662556365097_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7068344996360817334": {
            "length": 16,
            "waveforms": {
                "single": "-7068344996360817334",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2774398681751789420_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6848263725307004862_i",
                "Q": "6848263725307004862_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "199178351472754739": {
            "length": 16,
            "waveforms": {
                "single": "199178351472754739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3018263807362615146": {
            "length": 16,
            "waveforms": {
                "single": "3018263807362615146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8127513237283744304": {
            "length": 16,
            "waveforms": {
                "single": "8127513237283744304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5796913066335803996": {
            "length": 16,
            "waveforms": {
                "single": "-5796913066335803996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "584118567867829123": {
            "length": 16,
            "waveforms": {
                "single": "584118567867829123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7899977089223925201": {
            "length": 16,
            "waveforms": {
                "single": "-7899977089223925201",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7776016702118290013": {
            "length": 16,
            "waveforms": {
                "single": "-7776016702118290013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8733947512877533936": {
            "length": 16,
            "waveforms": {
                "single": "8733947512877533936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1855550497892842461": {
            "length": 16,
            "waveforms": {
                "single": "1855550497892842461",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7515036872828850817": {
            "length": 16,
            "waveforms": {
                "single": "-7515036872828850817",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8579341532118406579": {
            "length": 16,
            "waveforms": {
                "single": "8579341532118406579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8441364630807004342": {
            "length": 16,
            "waveforms": {
                "single": "-8441364630807004342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8081976151337348223": {
            "length": 16,
            "waveforms": {
                "single": "8081976151337348223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7804781747921346009": {
            "length": 16,
            "waveforms": {
                "single": "7804781747921346009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2436433036561213828": {
            "length": 16,
            "waveforms": {
                "single": "-2436433036561213828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4659744461489798956": {
            "length": 20,
            "waveforms": {
                "single": "4659744461489798956",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2933798417342272184": {
            "length": 20,
            "waveforms": {
                "single": "-2933798417342272184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2712304358143556936": {
            "length": 20,
            "waveforms": {
                "single": "-2712304358143556936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5563358489520568618": {
            "length": 20,
            "waveforms": {
                "single": "-5563358489520568618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5216030527667432629": {
            "length": 24,
            "waveforms": {
                "single": "5216030527667432629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8708395775952115671": {
            "length": 24,
            "waveforms": {
                "single": "-8708395775952115671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2070993241235885576": {
            "length": 24,
            "waveforms": {
                "single": "2070993241235885576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1793798837819883362": {
            "length": 24,
            "waveforms": {
                "single": "1793798837819883362",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5799744041012187778": {
            "length": 28,
            "waveforms": {
                "single": "-5799744041012187778",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5578249981813472530": {
            "length": 28,
            "waveforms": {
                "single": "-5578249981813472530",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1055932211723469214": {
            "length": 28,
            "waveforms": {
                "single": "-1055932211723469214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3380490293810305667": {
            "length": 28,
            "waveforms": {
                "single": "-3380490293810305667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1141827476279697649": {
            "length": 32,
            "waveforms": {
                "single": "1141827476279697649",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5193309765418398146": {
            "length": 32,
            "waveforms": {
                "single": "-5193309765418398146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6375037293306461995": {
            "length": 32,
            "waveforms": {
                "single": "6375037293306461995",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9155087652420149154": {
            "length": 32,
            "waveforms": {
                "single": "-9155087652420149154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2774056018216516035": {
            "length": 36,
            "waveforms": {
                "single": "-2774056018216516035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8794291040508344106": {
            "length": 36,
            "waveforms": {
                "single": "8794291040508344106",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6857511181794616439": {
            "length": 36,
            "waveforms": {
                "single": "6857511181794616439",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1724118147390217945": {
            "length": 36,
            "waveforms": {
                "single": "-1724118147390217945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1502624088191502697": {
            "length": 40,
            "waveforms": {
                "single": "-1502624088191502697",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2304547818051120954": {
            "length": 40,
            "waveforms": {
                "single": "2304547818051120954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3730585728835261649": {
            "length": 40,
            "waveforms": {
                "single": "3730585728835261649",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6205539820254430726": {
            "length": 40,
            "waveforms": {
                "single": "6205539820254430726",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5928345416838428512": {
            "length": 44,
            "waveforms": {
                "single": "5928345416838428512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8711226750628499453": {
            "length": 44,
            "waveforms": {
                "single": "-8711226750628499453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2783308130406881459": {
            "length": 44,
            "waveforms": {
                "single": "2783308130406881459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3967414921339780889": {
            "length": 44,
            "waveforms": {
                "single": "-3967414921339780889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6291973003426617342": {
            "length": 48,
            "waveforms": {
                "single": "-6291973003426617342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6534779692432218144": {
            "length": 48,
            "waveforms": {
                "single": "6534779692432218144",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3339594196584515132": {
            "length": 48,
            "waveforms": {
                "single": "3339594196584515132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7861911966674518448": {
            "length": 48,
            "waveforms": {
                "single": "7861911966674518448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6380173711673090787": {
            "length": 52,
            "waveforms": {
                "single": "6380173711673090787",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7806211622457231482": {
            "length": 52,
            "waveforms": {
                "single": "7806211622457231482",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6833360545009696483": {
            "length": 52,
            "waveforms": {
                "single": "-6833360545009696483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3946028472178304764": {
            "length": 52,
            "waveforms": {
                "single": "3946028472178304764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4635600857006529620": {
            "length": 56,
            "waveforms": {
                "single": "-4635600857006529620",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4414106797807814372": {
            "length": 56,
            "waveforms": {
                "single": "-4414106797807814372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7780638143438076673": {
            "length": 56,
            "waveforms": {
                "single": "-7780638143438076673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5217460402203318102": {
            "length": 56,
            "waveforms": {
                "single": "5217460402203318102",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1994853050605932261": {
            "length": 60,
            "waveforms": {
                "single": "-1994853050605932261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3016862707222116837": {
            "length": 60,
            "waveforms": {
                "single": "3016862707222116837",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3238356766420832085": {
            "length": 60,
            "waveforms": {
                "single": "3238356766420832085",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5798314166476302305": {
            "length": 60,
            "waveforms": {
                "single": "-5798314166476302305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5436116454423998948": {
            "length": 64,
            "waveforms": {
                "single": "5436116454423998948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2757734651387726650": {
            "length": 64,
            "waveforms": {
                "single": "-2757734651387726650",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3379060419274420194": {
            "length": 64,
            "waveforms": {
                "single": "-3379060419274420194",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "428111486968203457": {
            "length": 64,
            "waveforms": {
                "single": "428111486968203457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5191879890882512673": {
            "length": 68,
            "waveforms": {
                "single": "-5191879890882512673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5358164055056906211": {
            "length": 68,
            "waveforms": {
                "single": "-5358164055056906211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4894728912840919807": {
            "length": 68,
            "waveforms": {
                "single": "4894728912840919807",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2772626143680630562": {
            "length": 68,
            "waveforms": {
                "single": "-2772626143680630562",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8795720915044229579": {
            "length": 72,
            "waveforms": {
                "single": "8795720915044229579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-574866455677463699": {
            "length": 72,
            "waveforms": {
                "single": "-574866455677463699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7325589507424126047": {
            "length": 72,
            "waveforms": {
                "single": "-7325589507424126047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5899551596639985352": {
            "length": 72,
            "waveforms": {
                "single": "-5899551596639985352",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2305977692587006427": {
            "length": 76,
            "waveforms": {
                "single": "2305977692587006427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3701791908636818489": {
            "length": 76,
            "waveforms": {
                "single": "-3701791908636818489",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4503737380590173290": {
            "length": 76,
            "waveforms": {
                "single": "4503737380590173290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1116253997260542840": {
            "length": 76,
            "waveforms": {
                "single": "-1116253997260542840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8709796876092613980": {
            "length": 80,
            "waveforms": {
                "single": "-8709796876092613980",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2524633744807687273": {
            "length": 80,
            "waveforms": {
                "single": "2524633744807687273",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5669217361004038325": {
            "length": 80,
            "waveforms": {
                "single": "-5669217361004038325",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2370367291779926966": {
            "length": 40,
            "waveforms": {
                "I": "2370367291779926966_i",
                "Q": "2370367291779926966_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1609276662556365097_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
        },
        "1609276662556365097_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "-7068344996360817334": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
        },
        "6848263725307004862_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "6848263725307004862_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "199178351472754739": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "3018263807362615146": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "8127513237283744304": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-5796913066335803996": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "584118567867829123": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-7899977089223925201": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-7776016702118290013": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "8733947512877533936": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "1855550497892842461": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-7515036872828850817": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "8579341532118406579": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-8441364630807004342": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8081976151337348223": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7804781747921346009": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-2436433036561213828": {
            "sample": 0.175,
            "type": "constant",
        },
        "4659744461489798956": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2933798417342272184": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2712304358143556936": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5563358489520568618": {
            "sample": 0.175,
            "type": "constant",
        },
        "5216030527667432629": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8708395775952115671": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2070993241235885576": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
        },
        "1793798837819883362": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5799744041012187778": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5578249981813472530": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1055932211723469214": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-3380490293810305667": {
            "sample": 0.175,
            "type": "constant",
        },
        "1141827476279697649": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5193309765418398146": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6375037293306461995": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-9155087652420149154": {
            "sample": 0.175,
            "type": "constant",
        },
        "-2774056018216516035": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8794291040508344106": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6857511181794616439": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-1724118147390217945": {
            "sample": 0.175,
            "type": "constant",
        },
        "-1502624088191502697": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2304547818051120954": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3730585728835261649": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
        },
        "6205539820254430726": {
            "sample": 0.175,
            "type": "constant",
        },
        "5928345416838428512": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8711226750628499453": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2783308130406881459": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-3967414921339780889": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6291973003426617342": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6534779692432218144": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3339594196584515132": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
        },
        "7861911966674518448": {
            "sample": 0.175,
            "type": "constant",
        },
        "6380173711673090787": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7806211622457231482": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6833360545009696483": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
        },
        "3946028472178304764": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4635600857006529620": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4414106797807814372": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7780638143438076673": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
        },
        "5217460402203318102": {
            "sample": 0.175,
            "type": "constant",
        },
        "-1994853050605932261": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3016862707222116837": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3238356766420832085": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-5798314166476302305": {
            "sample": 0.175,
            "type": "constant",
        },
        "5436116454423998948": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2757734651387726650": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3379060419274420194": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
        },
        "428111486968203457": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5191879890882512673": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5358164055056906211": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4894728912840919807": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-2772626143680630562": {
            "sample": 0.175,
            "type": "constant",
        },
        "8795720915044229579": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-574866455677463699": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7325589507424126047": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-5899551596639985352": {
            "sample": 0.175,
            "type": "constant",
        },
        "2305977692587006427": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3701791908636818489": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4503737380590173290": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-1116253997260542840": {
            "sample": 0.175,
            "type": "constant",
        },
        "-8709796876092613980": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2524633744807687273": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5669217361004038325": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
        },
        "2370367291779926966_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "2370367291779926966_q": {
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
                "5436116454423998948": "5436116454423998948",
                "-2757734651387726650": "-2757734651387726650",
                "-3379060419274420194": "-3379060419274420194",
                "428111486968203457": "428111486968203457",
                "-5191879890882512673": "-5191879890882512673",
                "-5358164055056906211": "-5358164055056906211",
                "4894728912840919807": "4894728912840919807",
                "-2772626143680630562": "-2772626143680630562",
                "8795720915044229579": "8795720915044229579",
                "-574866455677463699": "-574866455677463699",
                "-7325589507424126047": "-7325589507424126047",
                "-5899551596639985352": "-5899551596639985352",
                "2305977692587006427": "2305977692587006427",
                "-3701791908636818489": "-3701791908636818489",
                "4503737380590173290": "4503737380590173290",
                "-1116253997260542840": "-1116253997260542840",
                "-8709796876092613980": "-8709796876092613980",
                "2524633744807687273": "2524633744807687273",
                "-5669217361004038325": "-5669217361004038325",
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
                "2774398681751789420": "2774398681751789420_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_e3d",
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
                "1609276662556365097": "1609276662556365097",
                "2370367291779926966": "2370367291779926966",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_c89",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "1609276662556365097": {
            "length": 40,
            "waveforms": {
                "I": "1609276662556365097_i",
                "Q": "1609276662556365097_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7068344996360817334": {
            "length": 16,
            "waveforms": {
                "single": "-7068344996360817334",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2774398681751789420_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6848263725307004862_i",
                "Q": "6848263725307004862_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "199178351472754739": {
            "length": 16,
            "waveforms": {
                "single": "199178351472754739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3018263807362615146": {
            "length": 16,
            "waveforms": {
                "single": "3018263807362615146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8127513237283744304": {
            "length": 16,
            "waveforms": {
                "single": "8127513237283744304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5796913066335803996": {
            "length": 16,
            "waveforms": {
                "single": "-5796913066335803996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "584118567867829123": {
            "length": 16,
            "waveforms": {
                "single": "584118567867829123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7899977089223925201": {
            "length": 16,
            "waveforms": {
                "single": "-7899977089223925201",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7776016702118290013": {
            "length": 16,
            "waveforms": {
                "single": "-7776016702118290013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8733947512877533936": {
            "length": 16,
            "waveforms": {
                "single": "8733947512877533936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1855550497892842461": {
            "length": 16,
            "waveforms": {
                "single": "1855550497892842461",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7515036872828850817": {
            "length": 16,
            "waveforms": {
                "single": "-7515036872828850817",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8579341532118406579": {
            "length": 16,
            "waveforms": {
                "single": "8579341532118406579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8441364630807004342": {
            "length": 16,
            "waveforms": {
                "single": "-8441364630807004342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8081976151337348223": {
            "length": 16,
            "waveforms": {
                "single": "8081976151337348223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7804781747921346009": {
            "length": 16,
            "waveforms": {
                "single": "7804781747921346009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2436433036561213828": {
            "length": 16,
            "waveforms": {
                "single": "-2436433036561213828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4659744461489798956": {
            "length": 20,
            "waveforms": {
                "single": "4659744461489798956",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2933798417342272184": {
            "length": 20,
            "waveforms": {
                "single": "-2933798417342272184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2712304358143556936": {
            "length": 20,
            "waveforms": {
                "single": "-2712304358143556936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5563358489520568618": {
            "length": 20,
            "waveforms": {
                "single": "-5563358489520568618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5216030527667432629": {
            "length": 24,
            "waveforms": {
                "single": "5216030527667432629",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8708395775952115671": {
            "length": 24,
            "waveforms": {
                "single": "-8708395775952115671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2070993241235885576": {
            "length": 24,
            "waveforms": {
                "single": "2070993241235885576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1793798837819883362": {
            "length": 24,
            "waveforms": {
                "single": "1793798837819883362",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5799744041012187778": {
            "length": 28,
            "waveforms": {
                "single": "-5799744041012187778",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5578249981813472530": {
            "length": 28,
            "waveforms": {
                "single": "-5578249981813472530",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1055932211723469214": {
            "length": 28,
            "waveforms": {
                "single": "-1055932211723469214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3380490293810305667": {
            "length": 28,
            "waveforms": {
                "single": "-3380490293810305667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1141827476279697649": {
            "length": 32,
            "waveforms": {
                "single": "1141827476279697649",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5193309765418398146": {
            "length": 32,
            "waveforms": {
                "single": "-5193309765418398146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6375037293306461995": {
            "length": 32,
            "waveforms": {
                "single": "6375037293306461995",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9155087652420149154": {
            "length": 32,
            "waveforms": {
                "single": "-9155087652420149154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2774056018216516035": {
            "length": 36,
            "waveforms": {
                "single": "-2774056018216516035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8794291040508344106": {
            "length": 36,
            "waveforms": {
                "single": "8794291040508344106",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6857511181794616439": {
            "length": 36,
            "waveforms": {
                "single": "6857511181794616439",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1724118147390217945": {
            "length": 36,
            "waveforms": {
                "single": "-1724118147390217945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1502624088191502697": {
            "length": 40,
            "waveforms": {
                "single": "-1502624088191502697",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2304547818051120954": {
            "length": 40,
            "waveforms": {
                "single": "2304547818051120954",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3730585728835261649": {
            "length": 40,
            "waveforms": {
                "single": "3730585728835261649",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6205539820254430726": {
            "length": 40,
            "waveforms": {
                "single": "6205539820254430726",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5928345416838428512": {
            "length": 44,
            "waveforms": {
                "single": "5928345416838428512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8711226750628499453": {
            "length": 44,
            "waveforms": {
                "single": "-8711226750628499453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2783308130406881459": {
            "length": 44,
            "waveforms": {
                "single": "2783308130406881459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3967414921339780889": {
            "length": 44,
            "waveforms": {
                "single": "-3967414921339780889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6291973003426617342": {
            "length": 48,
            "waveforms": {
                "single": "-6291973003426617342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6534779692432218144": {
            "length": 48,
            "waveforms": {
                "single": "6534779692432218144",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3339594196584515132": {
            "length": 48,
            "waveforms": {
                "single": "3339594196584515132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7861911966674518448": {
            "length": 48,
            "waveforms": {
                "single": "7861911966674518448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6380173711673090787": {
            "length": 52,
            "waveforms": {
                "single": "6380173711673090787",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7806211622457231482": {
            "length": 52,
            "waveforms": {
                "single": "7806211622457231482",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6833360545009696483": {
            "length": 52,
            "waveforms": {
                "single": "-6833360545009696483",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3946028472178304764": {
            "length": 52,
            "waveforms": {
                "single": "3946028472178304764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4635600857006529620": {
            "length": 56,
            "waveforms": {
                "single": "-4635600857006529620",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4414106797807814372": {
            "length": 56,
            "waveforms": {
                "single": "-4414106797807814372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7780638143438076673": {
            "length": 56,
            "waveforms": {
                "single": "-7780638143438076673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5217460402203318102": {
            "length": 56,
            "waveforms": {
                "single": "5217460402203318102",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1994853050605932261": {
            "length": 60,
            "waveforms": {
                "single": "-1994853050605932261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3016862707222116837": {
            "length": 60,
            "waveforms": {
                "single": "3016862707222116837",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3238356766420832085": {
            "length": 60,
            "waveforms": {
                "single": "3238356766420832085",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5798314166476302305": {
            "length": 60,
            "waveforms": {
                "single": "-5798314166476302305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5436116454423998948": {
            "length": 64,
            "waveforms": {
                "single": "5436116454423998948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2757734651387726650": {
            "length": 64,
            "waveforms": {
                "single": "-2757734651387726650",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3379060419274420194": {
            "length": 64,
            "waveforms": {
                "single": "-3379060419274420194",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "428111486968203457": {
            "length": 64,
            "waveforms": {
                "single": "428111486968203457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5191879890882512673": {
            "length": 68,
            "waveforms": {
                "single": "-5191879890882512673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5358164055056906211": {
            "length": 68,
            "waveforms": {
                "single": "-5358164055056906211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4894728912840919807": {
            "length": 68,
            "waveforms": {
                "single": "4894728912840919807",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2772626143680630562": {
            "length": 68,
            "waveforms": {
                "single": "-2772626143680630562",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8795720915044229579": {
            "length": 72,
            "waveforms": {
                "single": "8795720915044229579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-574866455677463699": {
            "length": 72,
            "waveforms": {
                "single": "-574866455677463699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7325589507424126047": {
            "length": 72,
            "waveforms": {
                "single": "-7325589507424126047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5899551596639985352": {
            "length": 72,
            "waveforms": {
                "single": "-5899551596639985352",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2305977692587006427": {
            "length": 76,
            "waveforms": {
                "single": "2305977692587006427",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3701791908636818489": {
            "length": 76,
            "waveforms": {
                "single": "-3701791908636818489",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4503737380590173290": {
            "length": 76,
            "waveforms": {
                "single": "4503737380590173290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1116253997260542840": {
            "length": 76,
            "waveforms": {
                "single": "-1116253997260542840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8709796876092613980": {
            "length": 80,
            "waveforms": {
                "single": "-8709796876092613980",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2524633744807687273": {
            "length": 80,
            "waveforms": {
                "single": "2524633744807687273",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5669217361004038325": {
            "length": 80,
            "waveforms": {
                "single": "-5669217361004038325",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2370367291779926966": {
            "length": 40,
            "waveforms": {
                "I": "2370367291779926966_i",
                "Q": "2370367291779926966_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1609276662556365097_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1609276662556365097_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7068344996360817334": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6848263725307004862_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "6848263725307004862_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "199178351472754739": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3018263807362615146": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8127513237283744304": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5796913066335803996": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "584118567867829123": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7899977089223925201": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7776016702118290013": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8733947512877533936": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1855550497892842461": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7515036872828850817": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8579341532118406579": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8441364630807004342": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8081976151337348223": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7804781747921346009": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2436433036561213828": {
            "sample": 0.175,
            "type": "constant",
        },
        "4659744461489798956": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2933798417342272184": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2712304358143556936": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5563358489520568618": {
            "sample": 0.175,
            "type": "constant",
        },
        "5216030527667432629": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8708395775952115671": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2070993241235885576": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1793798837819883362": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5799744041012187778": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5578249981813472530": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1055932211723469214": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3380490293810305667": {
            "sample": 0.175,
            "type": "constant",
        },
        "1141827476279697649": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5193309765418398146": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6375037293306461995": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9155087652420149154": {
            "sample": 0.175,
            "type": "constant",
        },
        "-2774056018216516035": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8794291040508344106": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6857511181794616439": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1724118147390217945": {
            "sample": 0.175,
            "type": "constant",
        },
        "-1502624088191502697": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2304547818051120954": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3730585728835261649": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6205539820254430726": {
            "sample": 0.175,
            "type": "constant",
        },
        "5928345416838428512": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8711226750628499453": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2783308130406881459": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3967414921339780889": {
            "sample": 0.175,
            "type": "constant",
        },
        "-6291973003426617342": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6534779692432218144": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3339594196584515132": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7861911966674518448": {
            "sample": 0.175,
            "type": "constant",
        },
        "6380173711673090787": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7806211622457231482": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6833360545009696483": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3946028472178304764": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4635600857006529620": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4414106797807814372": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7780638143438076673": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5217460402203318102": {
            "sample": 0.175,
            "type": "constant",
        },
        "-1994853050605932261": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3016862707222116837": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3238356766420832085": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5798314166476302305": {
            "sample": 0.175,
            "type": "constant",
        },
        "5436116454423998948": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2757734651387726650": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3379060419274420194": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "428111486968203457": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5191879890882512673": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5358164055056906211": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4894728912840919807": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2772626143680630562": {
            "sample": 0.175,
            "type": "constant",
        },
        "8795720915044229579": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-574866455677463699": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7325589507424126047": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5899551596639985352": {
            "sample": 0.175,
            "type": "constant",
        },
        "2305977692587006427": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3701791908636818489": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4503737380590173290": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1116253997260542840": {
            "sample": 0.175,
            "type": "constant",
        },
        "-8709796876092613980": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2524633744807687273": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5669217361004038325": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2370367291779926966_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2370367291779926966_q": {
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
        "B4/acquisition_mixer_e3d": [{'intermediate_frequency': 330298316.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_c89": [{'intermediate_frequency': 109678455.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

