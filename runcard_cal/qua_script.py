
# Single QUA script generated at 2025-01-16 17:56:58.625530
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    set_dc_offset("B1/flux", "single", 0.0)
    set_dc_offset("D1/flux", "single", 0.21674190528643072)
    set_dc_offset("B2/flux", "single", -0.2819)
    set_dc_offset("D2/flux", "single", -0.4253086474672965)
    set_dc_offset("B3/flux", "single", 0.0307)
    set_dc_offset("D3/flux", "single", -0.21477959018116385)
    set_dc_offset("B4/flux", "single", -0.215)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("B5/flux", "single", 0.074)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("6229513721976911160", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("4960253338813950585", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-7999659972201108212", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-5207320266438556453", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25540, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-1986740550323039760", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-7812345432198620892", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("7369768839072374644", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-3642804940720424311", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25539, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-2334567718134617126", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-5351068196054898891", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("1812244951491881188", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-2781105655748076828", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25538, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-7166503369111907852", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("4635180909113655455", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("655064014531186921", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-3155374744727776394", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25537, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-2275761866616897524", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("2696638125017472081", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        play("-7253852440036075769", "B4/drive")
        wait(11, "B4/flux")
        play("-4438671077835938680", "B4/flux")
        wait(46, "B4/drive")
        play("4907952974262180891", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1670041411024546998", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*-0.26143754955026)-(v3*-0.9652203933222481))>0.002215054761521925)))
        save(v4, r1)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("1670041411024546998_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": -0.2819,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
    },
    "octaves": {
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
                "6229513721976911160": "6229513721976911160",
                "4960253338813950585": "4960253338813950585",
                "-7999659972201108212": "-7999659972201108212",
                "-5207320266438556453": "-5207320266438556453",
                "-1986740550323039760": "-1986740550323039760",
                "-7812345432198620892": "-7812345432198620892",
                "7369768839072374644": "7369768839072374644",
                "-3642804940720424311": "-3642804940720424311",
                "-2334567718134617126": "-2334567718134617126",
                "-5351068196054898891": "-5351068196054898891",
                "1812244951491881188": "1812244951491881188",
                "-2781105655748076828": "-2781105655748076828",
                "-7166503369111907852": "-7166503369111907852",
                "4635180909113655455": "4635180909113655455",
                "655064014531186921": "655064014531186921",
                "-3155374744727776394": "-3155374744727776394",
                "-2275761866616897524": "-2275761866616897524",
                "2696638125017472081": "2696638125017472081",
                "-4438671077835938680": "-4438671077835938680",
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
            "intermediate_frequency": 109610828.0,
            "operations": {
                "-7253852440036075769": "-7253852440036075769",
                "4907952974262180891": "4907952974262180891",
            },
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
            "intermediate_frequency": 331181947.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "1670041411024546998": "1670041411024546998_B4/acquisition",
            },
        },
    },
    "pulses": {
        "-7253852440036075769": {
            "length": 40,
            "waveforms": {
                "I": "-7253852440036075769_i",
                "Q": "-7253852440036075769_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7048611249650584269": {
            "length": 16,
            "waveforms": {
                "single": "-7048611249650584269",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1670041411024546998_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "794596430159963831_i",
                "Q": "794596430159963831_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "5000449666134406009": {
            "length": 16,
            "waveforms": {
                "single": "5000449666134406009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3269462994846017225": {
            "length": 16,
            "waveforms": {
                "single": "3269462994846017225",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4092174261413506452": {
            "length": 16,
            "waveforms": {
                "single": "-4092174261413506452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4797386374549013684": {
            "length": 16,
            "waveforms": {
                "single": "-4797386374549013684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8262565215960249394": {
            "length": 16,
            "waveforms": {
                "single": "8262565215960249394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6762592530176872915": {
            "length": 16,
            "waveforms": {
                "single": "-6762592530176872915",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2024374902216614684": {
            "length": 16,
            "waveforms": {
                "single": "-2024374902216614684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5336516813455335780": {
            "length": 16,
            "waveforms": {
                "single": "5336516813455335780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4269672900306413101": {
            "length": 16,
            "waveforms": {
                "single": "4269672900306413101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3559255563006466662": {
            "length": 16,
            "waveforms": {
                "single": "-3559255563006466662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4443799639417175583": {
            "length": 16,
            "waveforms": {
                "single": "4443799639417175583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8535478505242642818": {
            "length": 16,
            "waveforms": {
                "single": "-8535478505242642818",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6168587853471660450": {
            "length": 16,
            "waveforms": {
                "single": "-6168587853471660450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4372668021918618374": {
            "length": 16,
            "waveforms": {
                "single": "-4372668021918618374",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1768934101219315798": {
            "length": 16,
            "waveforms": {
                "single": "-1768934101219315798",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1007920290981747239": {
            "length": 20,
            "waveforms": {
                "single": "1007920290981747239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3659145530055654170": {
            "length": 20,
            "waveforms": {
                "single": "-3659145530055654170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1852677571810992253": {
            "length": 20,
            "waveforms": {
                "single": "1852677571810992253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4164929830135520915": {
            "length": 20,
            "waveforms": {
                "single": "4164929830135520915",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2738775174505236030": {
            "length": 24,
            "waveforms": {
                "single": "2738775174505236030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "796243881809824721": {
            "length": 24,
            "waveforms": {
                "single": "796243881809824721",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2657275991552297861": {
            "length": 24,
            "waveforms": {
                "single": "-2657275991552297861",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1565119907971987264": {
            "length": 24,
            "waveforms": {
                "single": "-1565119907971987264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-442417241216421238": {
            "length": 28,
            "waveforms": {
                "single": "-442417241216421238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1950900815714972089": {
            "length": 28,
            "waveforms": {
                "single": "1950900815714972089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8959449711340192546": {
            "length": 28,
            "waveforms": {
                "single": "-8959449711340192546",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7587033871340468720": {
            "length": 28,
            "waveforms": {
                "single": "7587033871340468720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "667054888532028996": {
            "length": 32,
            "waveforms": {
                "single": "667054888532028996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8243887614369834247": {
            "length": 32,
            "waveforms": {
                "single": "-8243887614369834247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4523632129630318927": {
            "length": 32,
            "waveforms": {
                "single": "-4523632129630318927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8451564972341421082": {
            "length": 32,
            "waveforms": {
                "single": "8451564972341421082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-634394430015124574": {
            "length": 36,
            "waveforms": {
                "single": "-634394430015124574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6142562428598392757": {
            "length": 36,
            "waveforms": {
                "single": "-6142562428598392757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2968467151321584041": {
            "length": 36,
            "waveforms": {
                "single": "-2968467151321584041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4126104739227092966": {
            "length": 36,
            "waveforms": {
                "single": "4126104739227092966",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8607754171489102934": {
            "length": 40,
            "waveforms": {
                "single": "-8607754171489102934",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4498991813046809173": {
            "length": 40,
            "waveforms": {
                "single": "4498991813046809173",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7813572960259763270": {
            "length": 40,
            "waveforms": {
                "single": "-7813572960259763270",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5098547381394365669": {
            "length": 40,
            "waveforms": {
                "single": "5098547381394365669",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6148462244432306872": {
            "length": 44,
            "waveforms": {
                "single": "-6148462244432306872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5313900251465660875": {
            "length": 44,
            "waveforms": {
                "single": "-5313900251465660875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4213377196718075648": {
            "length": 44,
            "waveforms": {
                "single": "4213377196718075648",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2539798980906746099": {
            "length": 44,
            "waveforms": {
                "single": "2539798980906746099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5701366380820456035": {
            "length": 48,
            "waveforms": {
                "single": "-5701366380820456035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3962083170249467359": {
            "length": 48,
            "waveforms": {
                "single": "3962083170249467359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3742838432131924646": {
            "length": 48,
            "waveforms": {
                "single": "-3742838432131924646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9188664055854820498": {
            "length": 48,
            "waveforms": {
                "single": "9188664055854820498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6131035065646694504": {
            "length": 52,
            "waveforms": {
                "single": "-6131035065646694504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4463788321257362095": {
            "length": 52,
            "waveforms": {
                "single": "-4463788321257362095",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3935076538643908498": {
            "length": 52,
            "waveforms": {
                "single": "-3935076538643908498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2000947201739783854": {
            "length": 52,
            "waveforms": {
                "single": "2000947201739783854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5810629384227903829": {
            "length": 56,
            "waveforms": {
                "single": "-5810629384227903829",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3782972769717022779": {
            "length": 56,
            "waveforms": {
                "single": "-3782972769717022779",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "671275450850513623": {
            "length": 56,
            "waveforms": {
                "single": "671275450850513623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5384632254471161609": {
            "length": 56,
            "waveforms": {
                "single": "5384632254471161609",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3384024061188388551": {
            "length": 60,
            "waveforms": {
                "single": "3384024061188388551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4205629783625620000": {
            "length": 60,
            "waveforms": {
                "single": "4205629783625620000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5838554588129352125": {
            "length": 60,
            "waveforms": {
                "single": "-5838554588129352125",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3907169149528134460": {
            "length": 60,
            "waveforms": {
                "single": "-3907169149528134460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6229513721976911160": {
            "length": 64,
            "waveforms": {
                "single": "6229513721976911160",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4960253338813950585": {
            "length": 64,
            "waveforms": {
                "single": "4960253338813950585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7999659972201108212": {
            "length": 64,
            "waveforms": {
                "single": "-7999659972201108212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5207320266438556453": {
            "length": 64,
            "waveforms": {
                "single": "-5207320266438556453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1986740550323039760": {
            "length": 68,
            "waveforms": {
                "single": "-1986740550323039760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7812345432198620892": {
            "length": 68,
            "waveforms": {
                "single": "-7812345432198620892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7369768839072374644": {
            "length": 68,
            "waveforms": {
                "single": "7369768839072374644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3642804940720424311": {
            "length": 68,
            "waveforms": {
                "single": "-3642804940720424311",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2334567718134617126": {
            "length": 72,
            "waveforms": {
                "single": "-2334567718134617126",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5351068196054898891": {
            "length": 72,
            "waveforms": {
                "single": "-5351068196054898891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1812244951491881188": {
            "length": 72,
            "waveforms": {
                "single": "1812244951491881188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2781105655748076828": {
            "length": 72,
            "waveforms": {
                "single": "-2781105655748076828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7166503369111907852": {
            "length": 76,
            "waveforms": {
                "single": "-7166503369111907852",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4635180909113655455": {
            "length": 76,
            "waveforms": {
                "single": "4635180909113655455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "655064014531186921": {
            "length": 76,
            "waveforms": {
                "single": "655064014531186921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3155374744727776394": {
            "length": 76,
            "waveforms": {
                "single": "-3155374744727776394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2275761866616897524": {
            "length": 80,
            "waveforms": {
                "single": "-2275761866616897524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2696638125017472081": {
            "length": 80,
            "waveforms": {
                "single": "2696638125017472081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4438671077835938680": {
            "length": 80,
            "waveforms": {
                "single": "-4438671077835938680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4907952974262180891": {
            "length": 40,
            "waveforms": {
                "I": "4907952974262180891_i",
                "Q": "4907952974262180891_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-7253852440036075769_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
        },
        "-7253852440036075769_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "-7048611249650584269": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "794596430159963831_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "794596430159963831_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5000449666134406009": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "3269462994846017225": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-4092174261413506452": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-4797386374549013684": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8262565215960249394": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6762592530176872915": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-2024374902216614684": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5336516813455335780": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "4269672900306413101": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-3559255563006466662": {
            "samples": [0.0] * 10 + [0.15] + [0.0] * 5,
            "type": "arbitrary",
        },
        "4443799639417175583": {
            "samples": [0.0] * 10 + [0.15] * 2 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-8535478505242642818": {
            "samples": [0.0] * 10 + [0.15] * 3 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6168587853471660450": {
            "samples": [0.0] * 10 + [0.15] * 4 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4372668021918618374": {
            "samples": [0.0] * 10 + [0.15] * 5 + [0.0],
            "type": "arbitrary",
        },
        "-1768934101219315798": {
            "samples": [0.0] * 10 + [0.15] * 6,
            "type": "arbitrary",
        },
        "1007920290981747239": {
            "samples": [0.0] * 10 + [0.15] * 7 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3659145530055654170": {
            "samples": [0.0] * 10 + [0.15] * 8 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1852677571810992253": {
            "samples": [0.0] * 10 + [0.15] * 9 + [0.0],
            "type": "arbitrary",
        },
        "4164929830135520915": {
            "samples": [0.0] * 10 + [0.15] * 10,
            "type": "arbitrary",
        },
        "2738775174505236030": {
            "samples": [0.0] * 10 + [0.15] * 11 + [0.0] * 3,
            "type": "arbitrary",
        },
        "796243881809824721": {
            "samples": [0.0] * 10 + [0.15] * 12 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2657275991552297861": {
            "samples": [0.0] * 10 + [0.15] * 13 + [0.0],
            "type": "arbitrary",
        },
        "-1565119907971987264": {
            "samples": [0.0] * 10 + [0.15] * 14,
            "type": "arbitrary",
        },
        "-442417241216421238": {
            "samples": [0.0] * 10 + [0.15] * 15 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1950900815714972089": {
            "samples": [0.0] * 10 + [0.15] * 16 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8959449711340192546": {
            "samples": [0.0] * 10 + [0.15] * 17 + [0.0],
            "type": "arbitrary",
        },
        "7587033871340468720": {
            "samples": [0.0] * 10 + [0.15] * 18,
            "type": "arbitrary",
        },
        "667054888532028996": {
            "samples": [0.0] * 10 + [0.15] * 19 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8243887614369834247": {
            "samples": [0.0] * 10 + [0.15] * 20 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4523632129630318927": {
            "samples": [0.0] * 10 + [0.15] * 21 + [0.0],
            "type": "arbitrary",
        },
        "8451564972341421082": {
            "samples": [0.0] * 10 + [0.15] * 22,
            "type": "arbitrary",
        },
        "-634394430015124574": {
            "samples": [0.0] * 10 + [0.15] * 23 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6142562428598392757": {
            "samples": [0.0] * 10 + [0.15] * 24 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2968467151321584041": {
            "samples": [0.0] * 10 + [0.15] * 25 + [0.0],
            "type": "arbitrary",
        },
        "4126104739227092966": {
            "samples": [0.0] * 10 + [0.15] * 26,
            "type": "arbitrary",
        },
        "-8607754171489102934": {
            "samples": [0.0] * 10 + [0.15] * 27 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4498991813046809173": {
            "samples": [0.0] * 10 + [0.15] * 28 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7813572960259763270": {
            "samples": [0.0] * 10 + [0.15] * 29 + [0.0],
            "type": "arbitrary",
        },
        "5098547381394365669": {
            "samples": [0.0] * 10 + [0.15] * 30,
            "type": "arbitrary",
        },
        "-6148462244432306872": {
            "samples": [0.0] * 10 + [0.15] * 31 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5313900251465660875": {
            "samples": [0.0] * 10 + [0.15] * 32 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4213377196718075648": {
            "samples": [0.0] * 10 + [0.15] * 33 + [0.0],
            "type": "arbitrary",
        },
        "2539798980906746099": {
            "samples": [0.0] * 10 + [0.15] * 34,
            "type": "arbitrary",
        },
        "-5701366380820456035": {
            "samples": [0.0] * 10 + [0.15] * 35 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3962083170249467359": {
            "samples": [0.0] * 10 + [0.15] * 36 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3742838432131924646": {
            "samples": [0.0] * 10 + [0.15] * 37 + [0.0],
            "type": "arbitrary",
        },
        "9188664055854820498": {
            "samples": [0.0] * 10 + [0.15] * 38,
            "type": "arbitrary",
        },
        "-6131035065646694504": {
            "samples": [0.0] * 10 + [0.15] * 39 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4463788321257362095": {
            "samples": [0.0] * 10 + [0.15] * 40 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3935076538643908498": {
            "samples": [0.0] * 10 + [0.15] * 41 + [0.0],
            "type": "arbitrary",
        },
        "2000947201739783854": {
            "samples": [0.0] * 10 + [0.15] * 42,
            "type": "arbitrary",
        },
        "-5810629384227903829": {
            "samples": [0.0] * 10 + [0.15] * 43 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3782972769717022779": {
            "samples": [0.0] * 10 + [0.15] * 44 + [0.0] * 2,
            "type": "arbitrary",
        },
        "671275450850513623": {
            "samples": [0.0] * 10 + [0.15] * 45 + [0.0],
            "type": "arbitrary",
        },
        "5384632254471161609": {
            "samples": [0.0] * 10 + [0.15] * 46,
            "type": "arbitrary",
        },
        "3384024061188388551": {
            "samples": [0.0] * 10 + [0.15] * 47 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4205629783625620000": {
            "samples": [0.0] * 10 + [0.15] * 48 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5838554588129352125": {
            "samples": [0.0] * 10 + [0.15] * 49 + [0.0],
            "type": "arbitrary",
        },
        "-3907169149528134460": {
            "samples": [0.0] * 10 + [0.15] * 50,
            "type": "arbitrary",
        },
        "6229513721976911160": {
            "samples": [0.0] * 10 + [0.15] * 51 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4960253338813950585": {
            "samples": [0.0] * 10 + [0.15] * 52 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7999659972201108212": {
            "samples": [0.0] * 10 + [0.15] * 53 + [0.0],
            "type": "arbitrary",
        },
        "-5207320266438556453": {
            "samples": [0.0] * 10 + [0.15] * 54,
            "type": "arbitrary",
        },
        "-1986740550323039760": {
            "samples": [0.0] * 10 + [0.15] * 55 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7812345432198620892": {
            "samples": [0.0] * 10 + [0.15] * 56 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7369768839072374644": {
            "samples": [0.0] * 10 + [0.15] * 57 + [0.0],
            "type": "arbitrary",
        },
        "-3642804940720424311": {
            "samples": [0.0] * 10 + [0.15] * 58,
            "type": "arbitrary",
        },
        "-2334567718134617126": {
            "samples": [0.0] * 10 + [0.15] * 59 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5351068196054898891": {
            "samples": [0.0] * 10 + [0.15] * 60 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1812244951491881188": {
            "samples": [0.0] * 10 + [0.15] * 61 + [0.0],
            "type": "arbitrary",
        },
        "-2781105655748076828": {
            "samples": [0.0] * 10 + [0.15] * 62,
            "type": "arbitrary",
        },
        "-7166503369111907852": {
            "samples": [0.0] * 10 + [0.15] * 63 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4635180909113655455": {
            "samples": [0.0] * 10 + [0.15] * 64 + [0.0] * 2,
            "type": "arbitrary",
        },
        "655064014531186921": {
            "samples": [0.0] * 10 + [0.15] * 65 + [0.0],
            "type": "arbitrary",
        },
        "-3155374744727776394": {
            "samples": [0.0] * 10 + [0.15] * 66,
            "type": "arbitrary",
        },
        "-2275761866616897524": {
            "samples": [0.0] * 10 + [0.15] * 67 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2696638125017472081": {
            "samples": [0.0] * 10 + [0.15] * 68 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4438671077835938680": {
            "samples": [0.0] * 10 + [0.15] * 69 + [0.0],
            "type": "arbitrary",
        },
        "4907952974262180891_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
        },
        "4907952974262180891_q": {
            "samples": [-0.00032044811992864225, -0.00040909674052497095, -0.0005126697144394557, -0.0006304389395944795, -0.0007604390389508593, -0.0008992666293019756, -0.0010419722712087032, -0.001182084364398955, -0.0013117966442891453, -0.001422336445450926, -0.0015045102726514768, -0.0015493985291385904, -0.0015491457763035965, -0.0014977707309929602, -0.0013919055932163956, -0.0012313708280977211, -0.0010195013292979825, -0.0007631630140344868, -0.0004724330451463361, -0.00015995759435600705, 0.00015995759435600705, 0.0004724330451463361, 0.0007631630140344868, 0.0010195013292979825, 0.0012313708280977211, 0.0013919055932163956, 0.0014977707309929602, 0.0015491457763035965, 0.0015493985291385904, 0.0015045102726514768, 0.001422336445450926, 0.0013117966442891453, 0.001182084364398955, 0.0010419722712087032, 0.0008992666293019756, 0.0007604390389508593, 0.0006304389395944795, 0.0005126697144394557, 0.00040909674052497095, 0.00032044811992864225],
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
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": -0.2819,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
                "6229513721976911160": "6229513721976911160",
                "4960253338813950585": "4960253338813950585",
                "-7999659972201108212": "-7999659972201108212",
                "-5207320266438556453": "-5207320266438556453",
                "-1986740550323039760": "-1986740550323039760",
                "-7812345432198620892": "-7812345432198620892",
                "7369768839072374644": "7369768839072374644",
                "-3642804940720424311": "-3642804940720424311",
                "-2334567718134617126": "-2334567718134617126",
                "-5351068196054898891": "-5351068196054898891",
                "1812244951491881188": "1812244951491881188",
                "-2781105655748076828": "-2781105655748076828",
                "-7166503369111907852": "-7166503369111907852",
                "4635180909113655455": "4635180909113655455",
                "655064014531186921": "655064014531186921",
                "-3155374744727776394": "-3155374744727776394",
                "-2275761866616897524": "-2275761866616897524",
                "2696638125017472081": "2696638125017472081",
                "-4438671077835938680": "-4438671077835938680",
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
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 109610828.0,
            "operations": {
                "-7253852440036075769": "-7253852440036075769",
                "4907952974262180891": "4907952974262180891",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_96d",
                "lo_frequency": 6700000000.0,
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
            "intermediate_frequency": 331181947.0,
            "operations": {
                "1670041411024546998": "1670041411024546998_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_5da",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "-7253852440036075769": {
            "length": 40,
            "waveforms": {
                "I": "-7253852440036075769_i",
                "Q": "-7253852440036075769_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7048611249650584269": {
            "length": 16,
            "waveforms": {
                "single": "-7048611249650584269",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1670041411024546998_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "794596430159963831_i",
                "Q": "794596430159963831_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "5000449666134406009": {
            "length": 16,
            "waveforms": {
                "single": "5000449666134406009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3269462994846017225": {
            "length": 16,
            "waveforms": {
                "single": "3269462994846017225",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4092174261413506452": {
            "length": 16,
            "waveforms": {
                "single": "-4092174261413506452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4797386374549013684": {
            "length": 16,
            "waveforms": {
                "single": "-4797386374549013684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8262565215960249394": {
            "length": 16,
            "waveforms": {
                "single": "8262565215960249394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6762592530176872915": {
            "length": 16,
            "waveforms": {
                "single": "-6762592530176872915",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2024374902216614684": {
            "length": 16,
            "waveforms": {
                "single": "-2024374902216614684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5336516813455335780": {
            "length": 16,
            "waveforms": {
                "single": "5336516813455335780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4269672900306413101": {
            "length": 16,
            "waveforms": {
                "single": "4269672900306413101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3559255563006466662": {
            "length": 16,
            "waveforms": {
                "single": "-3559255563006466662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4443799639417175583": {
            "length": 16,
            "waveforms": {
                "single": "4443799639417175583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8535478505242642818": {
            "length": 16,
            "waveforms": {
                "single": "-8535478505242642818",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6168587853471660450": {
            "length": 16,
            "waveforms": {
                "single": "-6168587853471660450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4372668021918618374": {
            "length": 16,
            "waveforms": {
                "single": "-4372668021918618374",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1768934101219315798": {
            "length": 16,
            "waveforms": {
                "single": "-1768934101219315798",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1007920290981747239": {
            "length": 20,
            "waveforms": {
                "single": "1007920290981747239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3659145530055654170": {
            "length": 20,
            "waveforms": {
                "single": "-3659145530055654170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1852677571810992253": {
            "length": 20,
            "waveforms": {
                "single": "1852677571810992253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4164929830135520915": {
            "length": 20,
            "waveforms": {
                "single": "4164929830135520915",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2738775174505236030": {
            "length": 24,
            "waveforms": {
                "single": "2738775174505236030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "796243881809824721": {
            "length": 24,
            "waveforms": {
                "single": "796243881809824721",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2657275991552297861": {
            "length": 24,
            "waveforms": {
                "single": "-2657275991552297861",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1565119907971987264": {
            "length": 24,
            "waveforms": {
                "single": "-1565119907971987264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-442417241216421238": {
            "length": 28,
            "waveforms": {
                "single": "-442417241216421238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1950900815714972089": {
            "length": 28,
            "waveforms": {
                "single": "1950900815714972089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8959449711340192546": {
            "length": 28,
            "waveforms": {
                "single": "-8959449711340192546",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7587033871340468720": {
            "length": 28,
            "waveforms": {
                "single": "7587033871340468720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "667054888532028996": {
            "length": 32,
            "waveforms": {
                "single": "667054888532028996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8243887614369834247": {
            "length": 32,
            "waveforms": {
                "single": "-8243887614369834247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4523632129630318927": {
            "length": 32,
            "waveforms": {
                "single": "-4523632129630318927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8451564972341421082": {
            "length": 32,
            "waveforms": {
                "single": "8451564972341421082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-634394430015124574": {
            "length": 36,
            "waveforms": {
                "single": "-634394430015124574",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6142562428598392757": {
            "length": 36,
            "waveforms": {
                "single": "-6142562428598392757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2968467151321584041": {
            "length": 36,
            "waveforms": {
                "single": "-2968467151321584041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4126104739227092966": {
            "length": 36,
            "waveforms": {
                "single": "4126104739227092966",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8607754171489102934": {
            "length": 40,
            "waveforms": {
                "single": "-8607754171489102934",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4498991813046809173": {
            "length": 40,
            "waveforms": {
                "single": "4498991813046809173",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7813572960259763270": {
            "length": 40,
            "waveforms": {
                "single": "-7813572960259763270",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5098547381394365669": {
            "length": 40,
            "waveforms": {
                "single": "5098547381394365669",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6148462244432306872": {
            "length": 44,
            "waveforms": {
                "single": "-6148462244432306872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5313900251465660875": {
            "length": 44,
            "waveforms": {
                "single": "-5313900251465660875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4213377196718075648": {
            "length": 44,
            "waveforms": {
                "single": "4213377196718075648",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2539798980906746099": {
            "length": 44,
            "waveforms": {
                "single": "2539798980906746099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5701366380820456035": {
            "length": 48,
            "waveforms": {
                "single": "-5701366380820456035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3962083170249467359": {
            "length": 48,
            "waveforms": {
                "single": "3962083170249467359",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3742838432131924646": {
            "length": 48,
            "waveforms": {
                "single": "-3742838432131924646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9188664055854820498": {
            "length": 48,
            "waveforms": {
                "single": "9188664055854820498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6131035065646694504": {
            "length": 52,
            "waveforms": {
                "single": "-6131035065646694504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4463788321257362095": {
            "length": 52,
            "waveforms": {
                "single": "-4463788321257362095",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3935076538643908498": {
            "length": 52,
            "waveforms": {
                "single": "-3935076538643908498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2000947201739783854": {
            "length": 52,
            "waveforms": {
                "single": "2000947201739783854",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5810629384227903829": {
            "length": 56,
            "waveforms": {
                "single": "-5810629384227903829",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3782972769717022779": {
            "length": 56,
            "waveforms": {
                "single": "-3782972769717022779",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "671275450850513623": {
            "length": 56,
            "waveforms": {
                "single": "671275450850513623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5384632254471161609": {
            "length": 56,
            "waveforms": {
                "single": "5384632254471161609",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3384024061188388551": {
            "length": 60,
            "waveforms": {
                "single": "3384024061188388551",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4205629783625620000": {
            "length": 60,
            "waveforms": {
                "single": "4205629783625620000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5838554588129352125": {
            "length": 60,
            "waveforms": {
                "single": "-5838554588129352125",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3907169149528134460": {
            "length": 60,
            "waveforms": {
                "single": "-3907169149528134460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6229513721976911160": {
            "length": 64,
            "waveforms": {
                "single": "6229513721976911160",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4960253338813950585": {
            "length": 64,
            "waveforms": {
                "single": "4960253338813950585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7999659972201108212": {
            "length": 64,
            "waveforms": {
                "single": "-7999659972201108212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5207320266438556453": {
            "length": 64,
            "waveforms": {
                "single": "-5207320266438556453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1986740550323039760": {
            "length": 68,
            "waveforms": {
                "single": "-1986740550323039760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7812345432198620892": {
            "length": 68,
            "waveforms": {
                "single": "-7812345432198620892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7369768839072374644": {
            "length": 68,
            "waveforms": {
                "single": "7369768839072374644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3642804940720424311": {
            "length": 68,
            "waveforms": {
                "single": "-3642804940720424311",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2334567718134617126": {
            "length": 72,
            "waveforms": {
                "single": "-2334567718134617126",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5351068196054898891": {
            "length": 72,
            "waveforms": {
                "single": "-5351068196054898891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1812244951491881188": {
            "length": 72,
            "waveforms": {
                "single": "1812244951491881188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2781105655748076828": {
            "length": 72,
            "waveforms": {
                "single": "-2781105655748076828",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7166503369111907852": {
            "length": 76,
            "waveforms": {
                "single": "-7166503369111907852",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4635180909113655455": {
            "length": 76,
            "waveforms": {
                "single": "4635180909113655455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "655064014531186921": {
            "length": 76,
            "waveforms": {
                "single": "655064014531186921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3155374744727776394": {
            "length": 76,
            "waveforms": {
                "single": "-3155374744727776394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2275761866616897524": {
            "length": 80,
            "waveforms": {
                "single": "-2275761866616897524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2696638125017472081": {
            "length": 80,
            "waveforms": {
                "single": "2696638125017472081",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4438671077835938680": {
            "length": 80,
            "waveforms": {
                "single": "-4438671077835938680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4907952974262180891": {
            "length": 40,
            "waveforms": {
                "I": "4907952974262180891_i",
                "Q": "4907952974262180891_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-7253852440036075769_i": {
            "samples": [0.00032044811992864235, 0.0004090967405249711, 0.0005126697144394559, 0.0006304389395944798, 0.0007604390389508596, 0.000899266629301976, 0.0010419722712087039, 0.0011820843643989556, 0.0013117966442891462, 0.001422336445450927, 0.001504510272651478, 0.0015493985291385917, 0.001549145776303598, 0.001497770730992962, 0.0013919055932163974, 0.001231370828097723, 0.0010195013292979846, 0.0007631630140344889, 0.00047243304514633835, 0.00015995759435600933, -0.00015995759435600477, -0.0004724330451463339, -0.0007631630140344846, -0.0010195013292979803, -0.0012313708280977192, -0.001391905593216394, -0.0014977707309929585, -0.001549145776303595, -0.001549398529138589, -0.0015045102726514758, -0.0014223364454509252, -0.0013117966442891444, -0.0011820843643989543, -0.0010419722712087026, -0.0008992666293019751, -0.0007604390389508589, -0.0006304389395944791, -0.0005126697144394555, -0.0004090967405249708, -0.00032044811992864214],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7253852440036075769_q": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7048611249650584269": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "794596430159963831_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "794596430159963831_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5000449666134406009": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3269462994846017225": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4092174261413506452": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4797386374549013684": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8262565215960249394": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6762592530176872915": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2024374902216614684": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5336516813455335780": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4269672900306413101": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3559255563006466662": {
            "samples": [0.0] * 10 + [0.15] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4443799639417175583": {
            "samples": [0.0] * 10 + [0.15] * 2 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8535478505242642818": {
            "samples": [0.0] * 10 + [0.15] * 3 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6168587853471660450": {
            "samples": [0.0] * 10 + [0.15] * 4 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4372668021918618374": {
            "samples": [0.0] * 10 + [0.15] * 5 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1768934101219315798": {
            "samples": [0.0] * 10 + [0.15] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1007920290981747239": {
            "samples": [0.0] * 10 + [0.15] * 7 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3659145530055654170": {
            "samples": [0.0] * 10 + [0.15] * 8 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1852677571810992253": {
            "samples": [0.0] * 10 + [0.15] * 9 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4164929830135520915": {
            "samples": [0.0] * 10 + [0.15] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2738775174505236030": {
            "samples": [0.0] * 10 + [0.15] * 11 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "796243881809824721": {
            "samples": [0.0] * 10 + [0.15] * 12 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2657275991552297861": {
            "samples": [0.0] * 10 + [0.15] * 13 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1565119907971987264": {
            "samples": [0.0] * 10 + [0.15] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-442417241216421238": {
            "samples": [0.0] * 10 + [0.15] * 15 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1950900815714972089": {
            "samples": [0.0] * 10 + [0.15] * 16 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8959449711340192546": {
            "samples": [0.0] * 10 + [0.15] * 17 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7587033871340468720": {
            "samples": [0.0] * 10 + [0.15] * 18,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "667054888532028996": {
            "samples": [0.0] * 10 + [0.15] * 19 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8243887614369834247": {
            "samples": [0.0] * 10 + [0.15] * 20 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4523632129630318927": {
            "samples": [0.0] * 10 + [0.15] * 21 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8451564972341421082": {
            "samples": [0.0] * 10 + [0.15] * 22,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-634394430015124574": {
            "samples": [0.0] * 10 + [0.15] * 23 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6142562428598392757": {
            "samples": [0.0] * 10 + [0.15] * 24 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2968467151321584041": {
            "samples": [0.0] * 10 + [0.15] * 25 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4126104739227092966": {
            "samples": [0.0] * 10 + [0.15] * 26,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8607754171489102934": {
            "samples": [0.0] * 10 + [0.15] * 27 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4498991813046809173": {
            "samples": [0.0] * 10 + [0.15] * 28 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7813572960259763270": {
            "samples": [0.0] * 10 + [0.15] * 29 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5098547381394365669": {
            "samples": [0.0] * 10 + [0.15] * 30,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6148462244432306872": {
            "samples": [0.0] * 10 + [0.15] * 31 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5313900251465660875": {
            "samples": [0.0] * 10 + [0.15] * 32 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4213377196718075648": {
            "samples": [0.0] * 10 + [0.15] * 33 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2539798980906746099": {
            "samples": [0.0] * 10 + [0.15] * 34,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5701366380820456035": {
            "samples": [0.0] * 10 + [0.15] * 35 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3962083170249467359": {
            "samples": [0.0] * 10 + [0.15] * 36 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3742838432131924646": {
            "samples": [0.0] * 10 + [0.15] * 37 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9188664055854820498": {
            "samples": [0.0] * 10 + [0.15] * 38,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6131035065646694504": {
            "samples": [0.0] * 10 + [0.15] * 39 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4463788321257362095": {
            "samples": [0.0] * 10 + [0.15] * 40 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3935076538643908498": {
            "samples": [0.0] * 10 + [0.15] * 41 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2000947201739783854": {
            "samples": [0.0] * 10 + [0.15] * 42,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5810629384227903829": {
            "samples": [0.0] * 10 + [0.15] * 43 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3782972769717022779": {
            "samples": [0.0] * 10 + [0.15] * 44 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "671275450850513623": {
            "samples": [0.0] * 10 + [0.15] * 45 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5384632254471161609": {
            "samples": [0.0] * 10 + [0.15] * 46,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3384024061188388551": {
            "samples": [0.0] * 10 + [0.15] * 47 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4205629783625620000": {
            "samples": [0.0] * 10 + [0.15] * 48 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5838554588129352125": {
            "samples": [0.0] * 10 + [0.15] * 49 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3907169149528134460": {
            "samples": [0.0] * 10 + [0.15] * 50,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6229513721976911160": {
            "samples": [0.0] * 10 + [0.15] * 51 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4960253338813950585": {
            "samples": [0.0] * 10 + [0.15] * 52 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7999659972201108212": {
            "samples": [0.0] * 10 + [0.15] * 53 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5207320266438556453": {
            "samples": [0.0] * 10 + [0.15] * 54,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1986740550323039760": {
            "samples": [0.0] * 10 + [0.15] * 55 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7812345432198620892": {
            "samples": [0.0] * 10 + [0.15] * 56 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7369768839072374644": {
            "samples": [0.0] * 10 + [0.15] * 57 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3642804940720424311": {
            "samples": [0.0] * 10 + [0.15] * 58,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2334567718134617126": {
            "samples": [0.0] * 10 + [0.15] * 59 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5351068196054898891": {
            "samples": [0.0] * 10 + [0.15] * 60 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1812244951491881188": {
            "samples": [0.0] * 10 + [0.15] * 61 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2781105655748076828": {
            "samples": [0.0] * 10 + [0.15] * 62,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7166503369111907852": {
            "samples": [0.0] * 10 + [0.15] * 63 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4635180909113655455": {
            "samples": [0.0] * 10 + [0.15] * 64 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "655064014531186921": {
            "samples": [0.0] * 10 + [0.15] * 65 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3155374744727776394": {
            "samples": [0.0] * 10 + [0.15] * 66,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2275761866616897524": {
            "samples": [0.0] * 10 + [0.15] * 67 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2696638125017472081": {
            "samples": [0.0] * 10 + [0.15] * 68 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4438671077835938680": {
            "samples": [0.0] * 10 + [0.15] * 69 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4907952974262180891_i": {
            "samples": [0.0019122312051685873, 0.0025731883433511684, 0.0034089206986104067, 0.004446070758572637, 0.005708867858399413, 0.007216685175589522, 0.008981309812438653, 0.011004130810404815, 0.013273515452095699, 0.01576268961192368, 0.018428451186544403, 0.021211017297298348, 0.024035231438407318, 0.026813238261132712, 0.029448581145735307, 0.031841508282122885, 0.033895109129906946, 0.03552176938051429, 0.036649351381049106] + [0.03722649468648891] * 2 + [0.036649351381049106, 0.03552176938051429, 0.033895109129906946, 0.031841508282122885, 0.029448581145735307, 0.026813238261132712, 0.024035231438407318, 0.021211017297298348, 0.018428451186544403, 0.01576268961192368, 0.013273515452095699, 0.011004130810404815, 0.008981309812438653, 0.007216685175589522, 0.005708867858399413, 0.004446070758572637, 0.0034089206986104067, 0.0025731883433511684, 0.0019122312051685873],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4907952974262180891_q": {
            "samples": [-0.00032044811992864225, -0.00040909674052497095, -0.0005126697144394557, -0.0006304389395944795, -0.0007604390389508593, -0.0008992666293019756, -0.0010419722712087032, -0.001182084364398955, -0.0013117966442891453, -0.001422336445450926, -0.0015045102726514768, -0.0015493985291385904, -0.0015491457763035965, -0.0014977707309929602, -0.0013919055932163956, -0.0012313708280977211, -0.0010195013292979825, -0.0007631630140344868, -0.0004724330451463361, -0.00015995759435600705, 0.00015995759435600705, 0.0004724330451463361, 0.0007631630140344868, 0.0010195013292979825, 0.0012313708280977211, 0.0013919055932163956, 0.0014977707309929602, 0.0015491457763035965, 0.0015493985291385904, 0.0015045102726514768, 0.001422336445450926, 0.0013117966442891453, 0.001182084364398955, 0.0010419722712087032, 0.0008992666293019756, 0.0007604390389508593, 0.0006304389395944795, 0.0005126697144394557, 0.00040909674052497095, 0.00032044811992864225],
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
        "B4/drive_mixer_96d": [{'intermediate_frequency': 109610828.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/acquisition_mixer_5da": [{'intermediate_frequency': 331181947.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

