
# Single QUA script generated at 2025-02-16 11:31:19.558454
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(int, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(int, )
    v11 = declare(fixed, )
    v12 = declare(fixed, )
    v13 = declare(int, )
    set_dc_offset("B1/flux", "single", -0.25498290735703955)
    set_dc_offset("D1/flux", "single", -0.4530870218982913)
    set_dc_offset("B2/flux", "single", 0.10729465913983083)
    set_dc_offset("D2/flux", "single", -0.2224873138863394)
    set_dc_offset("B3/flux", "single", 0.2226188560782865)
    set_dc_offset("D3/flux", "single", 0.05128942239382605)
    set_dc_offset("B4/flux", "single", 0.114743772754262)
    set_dc_offset("D4/flux", "single", -0.08416990010352905)
    set_dc_offset("B5/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", 0.05418914676504196)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B1/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B2/acquisition")
    wait((4+(0*((Cast.to_int(v8)+Cast.to_int(v9))+Cast.to_int(v10)))), "B3/acquisition")
    wait((4+(0*((Cast.to_int(v11)+Cast.to_int(v12))+Cast.to_int(v13)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("1370236233548375909", "B1/drive")
        wait(11, "B1/flux")
        play("5104555003540826429", "B1/flux")
        wait(46, "B1/drive")
        play("2131326862771937778", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-3129629664977179120", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("-5205339532812483545", "B2/drive")
        wait(11, "B2/flux")
        play("5104555003540826429", "B2/flux")
        wait(46, "B2/drive")
        play("-4444248903588921676", "B2/drive")
        wait(66, "B2/acquisition")
        measure("1365255557228087931", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("5597379543326980578", "B3/drive")
        wait(11, "B3/flux")
        play("5104555003540826429", "B3/flux")
        wait(46, "B3/drive")
        play("6358470172550542447", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-1453236510719896437", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("-1987390868038532237", "B4/drive")
        wait(11, "B4/flux")
        play("5104555003540826429", "B4/flux")
        wait(46, "B4/drive")
        play("-1226300238814970368", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-998436112298849707", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25001, "B1/acquisition")
        wait(25001, "B4/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25501, "B2/drive")
        wait(25501, "B1/drive")
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B1/flux")
        play("1370236233548375909", "B1/drive")
        wait(11, "B1/flux")
        play("5326049062739541677", "B1/flux")
        wait(46, "B1/drive")
        play("2131326862771937778", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-3129629664977179120", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("-5205339532812483545", "B2/drive")
        wait(11, "B2/flux")
        play("5326049062739541677", "B2/flux")
        wait(46, "B2/drive")
        play("-4444248903588921676", "B2/drive")
        wait(66, "B2/acquisition")
        measure("1365255557228087931", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("5597379543326980578", "B3/drive")
        wait(11, "B3/flux")
        play("5326049062739541677", "B3/flux")
        wait(46, "B3/drive")
        play("6358470172550542447", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-1453236510719896437", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("-1987390868038532237", "B4/drive")
        wait(11, "B4/flux")
        play("5326049062739541677", "B4/flux")
        wait(46, "B4/drive")
        play("-1226300238814970368", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-998436112298849707", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25001, "B1/acquisition")
        wait(25001, "B4/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25501, "B2/drive")
        wait(25501, "B1/drive")
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B1/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-3129629664977179120_B1|acquisition_shots")
        r2.buffer(2).average().save("1365255557228087931_B2|acquisition_shots")
        r3.buffer(2).average().save("-1453236510719896437_B3|acquisition_shots")
        r4.buffer(2).average().save("-998436112298849707_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.25498290735703955,
                    "filter": {},
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.0,
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
                    "offset": -0.4530870218982913,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "6": {
                    "offset": -0.08416990010352905,
                    "filter": {},
                },
                "7": {
                    "offset": 0.05418914676504196,
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
                "7": {
                    "offset": 0.0,
                    "filter": {},
                },
                "8": {
                    "offset": 0.0,
                    "filter": {},
                },
                "3": {
                    "offset": 0.0,
                    "filter": {},
                },
                "4": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {
                "1": {},
                "7": {},
                "3": {},
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
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": 0.0,
                    "filter": {},
                },
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
                "1": {},
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
                    "output_mode": "triggered",
                },
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "2": {
                    "LO_frequency": 4900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
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
                "1": {
                    "LO_frequency": 5800000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "4": {
                    "LO_frequency": 6700000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
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
            "operations": {
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
            },
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
            "operations": {
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
            },
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
            "operations": {
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
            },
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
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
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
        "B1/acquisition": {
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
            "intermediate_frequency": -237451236.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-3129629664977179120": "-3129629664977179120_B1/acquisition",
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
            "intermediate_frequency": 330300527.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-998436112298849707": "-998436112298849707_B4/acquisition",
            },
        },
        "B3/drive": {
            "RF_inputs": {
                "port": ('octave3', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con3', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -115376210.0,
            "operations": {
                "5597379543326980578": "5597379543326980578",
                "6358470172550542447": "6358470172550542447",
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
            "intermediate_frequency": 109615374.0,
            "operations": {
                "-1987390868038532237": "-1987390868038532237",
                "-1226300238814970368": "-1226300238814970368",
            },
        },
        "B2/drive": {
            "RF_inputs": {
                "port": ('octave2', 4),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con2', 7),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 63761228.0,
            "operations": {
                "-5205339532812483545": "-5205339532812483545",
                "-4444248903588921676": "-4444248903588921676",
            },
        },
        "B1/drive": {
            "RF_inputs": {
                "port": ('octave2', 2),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con2', 3),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 100388701.0,
            "operations": {
                "1370236233548375909": "1370236233548375909",
                "2131326862771937778": "2131326862771937778",
            },
        },
        "B3/acquisition": {
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
            "intermediate_frequency": 110622376.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-1453236510719896437": "-1453236510719896437_B3/acquisition",
            },
        },
        "B2/acquisition": {
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
            "intermediate_frequency": 10040944.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "1365255557228087931": "1365255557228087931_B2/acquisition",
            },
        },
    },
    "pulses": {
        "1370236233548375909": {
            "length": 40,
            "waveforms": {
                "I": "1370236233548375909_i",
                "Q": "1370236233548375909_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3400425378092587439": {
            "length": 16,
            "waveforms": {
                "single": "3400425378092587439",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3129629664977179120_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7453777329938855000_i",
                "Q": "-7453777329938855000_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-5205339532812483545": {
            "length": 40,
            "waveforms": {
                "I": "-5205339532812483545_i",
                "Q": "-5205339532812483545_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1365255557228087931_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "734197750943754517_i",
                "Q": "734197750943754517_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "5597379543326980578": {
            "length": 40,
            "waveforms": {
                "I": "5597379543326980578_i",
                "Q": "5597379543326980578_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1453236510719896437_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-60446087009451205_i",
                "Q": "-60446087009451205_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-1987390868038532237": {
            "length": 40,
            "waveforms": {
                "I": "-1987390868038532237_i",
                "Q": "-1987390868038532237_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-998436112298849707_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1141891809292196426_i",
                "Q": "1141891809292196426_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4266929678428962930": {
            "length": 16,
            "waveforms": {
                "single": "-4266929678428962930",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4393641214510328855": {
            "length": 16,
            "waveforms": {
                "single": "4393641214510328855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2069169990425796067": {
            "length": 16,
            "waveforms": {
                "single": "-2069169990425796067",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4421535659188090287": {
            "length": 16,
            "waveforms": {
                "single": "-4421535659188090287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2995497748403949592": {
            "length": 16,
            "waveforms": {
                "single": "-2995497748403949592",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "350083756776086044": {
            "length": 16,
            "waveforms": {
                "single": "350083756776086044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5196095443385150857": {
            "length": 16,
            "waveforms": {
                "single": "-5196095443385150857",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3009433845841840922": {
            "length": 16,
            "waveforms": {
                "single": "3009433845841840922",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3230927905040556170": {
            "length": 16,
            "waveforms": {
                "single": "3230927905040556170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2776841696183268746": {
            "length": 16,
            "waveforms": {
                "single": "-2776841696183268746",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5428687593043723033": {
            "length": 16,
            "waveforms": {
                "single": "5428687593043723033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7163520895752370693": {
            "length": 16,
            "waveforms": {
                "single": "-7163520895752370693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7784846663639064237": {
            "length": 16,
            "waveforms": {
                "single": "-7784846663639064237",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9180159155069059718": {
            "length": 16,
            "waveforms": {
                "single": "9180159155069059718",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5587086975635897374": {
            "length": 16,
            "waveforms": {
                "single": "-5587086975635897374",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5365592916437182126": {
            "length": 20,
            "waveforms": {
                "single": "-5365592916437182126",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4887300051460643892": {
            "length": 20,
            "waveforms": {
                "single": "4887300051460643892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7178412388045274605": {
            "length": 20,
            "waveforms": {
                "single": "-7178412388045274605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2686702356479442627": {
            "length": 20,
            "waveforms": {
                "single": "2686702356479442627",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4980652700042107742": {
            "length": 24,
            "waveforms": {
                "single": "-4980652700042107742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4759158640843392494": {
            "length": 24,
            "waveforms": {
                "single": "-4759158640843392494",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5906980458020261267": {
            "length": 24,
            "waveforms": {
                "single": "-5906980458020261267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8231538540107097720": {
            "length": 24,
            "waveforms": {
                "single": "-8231538540107097720",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3709220770017094404": {
            "length": 28,
            "waveforms": {
                "single": "-3709220770017094404",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2671810864186538715": {
            "length": 28,
            "waveforms": {
                "single": "2671810864186538715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1523989047009669942": {
            "length": 28,
            "waveforms": {
                "single": "1523989047009669942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1289967022815212293": {
            "length": 28,
            "waveforms": {
                "single": "-1289967022815212293",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2517204883427411358": {
            "length": 32,
            "waveforms": {
                "single": "2517204883427411358",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3943242794211552053": {
            "length": 32,
            "waveforms": {
                "single": "3943242794211552053",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7750414700454175704": {
            "length": 32,
            "waveforms": {
                "single": "7750414700454175704",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6141002482214718916": {
            "length": 32,
            "waveforms": {
                "single": "6141002482214718916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6362496541413434164": {
            "length": 36,
            "waveforms": {
                "single": "6362496541413434164",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8277075626053493801": {
            "length": 36,
            "waveforms": {
                "single": "-8277075626053493801",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1975817341844332217": {
            "length": 36,
            "waveforms": {
                "single": "1975817341844332217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-348740740242504236": {
            "length": 36,
            "waveforms": {
                "single": "-348740740242504236",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6747436757808508548": {
            "length": 40,
            "waveforms": {
                "single": "6747436757808508548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-846106121023562592": {
            "length": 40,
            "waveforms": {
                "single": "-846106121023562592",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6466097498874278722": {
            "length": 40,
            "waveforms": {
                "single": "-6466097498874278722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6592830777049381191": {
            "length": 40,
            "waveforms": {
                "single": "6592830777049381191",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7303722823986142221": {
            "length": 44,
            "waveforms": {
                "single": "7303722823986142221",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6620703479633406079": {
            "length": 44,
            "waveforms": {
                "single": "-6620703479633406079",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4158685537554595168": {
            "length": 44,
            "waveforms": {
                "single": "4158685537554595168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1387493662606641733": {
            "length": 44,
            "waveforms": {
                "single": "-1387493662606641733",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4201449732431523968": {
            "length": 48,
            "waveforms": {
                "single": "-4201449732431523968",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "810266025396525130": {
            "length": 48,
            "waveforms": {
                "single": "810266025396525130",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1031760084595240378": {
            "length": 48,
            "waveforms": {
                "single": "1031760084595240378",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6635594971926309991": {
            "length": 48,
            "waveforms": {
                "single": "-6635594971926309991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3229519772598407241": {
            "length": 52,
            "waveforms": {
                "single": "3229519772598407241",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9181589029604945191": {
            "length": 52,
            "waveforms": {
                "single": "9181589029604945191",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8462729589625171587": {
            "length": 52,
            "waveforms": {
                "single": "8462729589625171587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8684223648823886835": {
            "length": 52,
            "waveforms": {
                "single": "8684223648823886835",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2545077586011436246": {
            "length": 56,
            "waveforms": {
                "single": "-2545077586011436246",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7564760736882497918": {
            "length": 56,
            "waveforms": {
                "single": "-7564760736882497918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1612691479875959968": {
            "length": 56,
            "waveforms": {
                "single": "-1612691479875959968",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4979222825506222269": {
            "length": 56,
            "waveforms": {
                "single": "-4979222825506222269",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "585068208127206895": {
            "length": 60,
            "waveforms": {
                "single": "585068208127206895",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5107385978217210211": {
            "length": 60,
            "waveforms": {
                "single": "5107385978217210211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2559969078304340158": {
            "length": 60,
            "waveforms": {
                "single": "-2559969078304340158",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8293232116573140318": {
            "length": 60,
            "waveforms": {
                "single": "8293232116573140318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8016037713157138104": {
            "length": 64,
            "waveforms": {
                "single": "8016037713157138104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1382357244240012941": {
            "length": 64,
            "waveforms": {
                "single": "-1382357244240012941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5686894531263694948": {
            "length": 64,
            "waveforms": {
                "single": "-5686894531263694948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1879722625021071297": {
            "length": 64,
            "waveforms": {
                "single": "-1879722625021071297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2241440354547294617": {
            "length": 68,
            "waveforms": {
                "single": "2241440354547294617",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "318037062982095566": {
            "length": 68,
            "waveforms": {
                "single": "318037062982095566",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6270106319988633516": {
            "length": 68,
            "waveforms": {
                "single": "6270106319988633516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8497139810716323576": {
            "length": 68,
            "waveforms": {
                "single": "-8497139810716323576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8275645751517608328": {
            "length": 72,
            "waveforms": {
                "single": "-8275645751517608328",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8552840154933610542": {
            "length": 72,
            "waveforms": {
                "single": "-8552840154933610542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6077886063514441465": {
            "length": 72,
            "waveforms": {
                "single": "-6077886063514441465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-223350478600983575": {
            "length": 72,
            "waveforms": {
                "single": "-223350478600983575",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7890705535122533944": {
            "length": 76,
            "waveforms": {
                "single": "-7890705535122533944",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2326414501489104780": {
            "length": 76,
            "waveforms": {
                "single": "-2326414501489104780",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2195903268600898536": {
            "length": 76,
            "waveforms": {
                "single": "2195903268600898536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7305152698522027694": {
            "length": 76,
            "waveforms": {
                "single": "7305152698522027694",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7429113085627662882": {
            "length": 80,
            "waveforms": {
                "single": "7429113085627662882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5104555003540826429": {
            "length": 80,
            "waveforms": {
                "single": "5104555003540826429",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5326049062739541677": {
            "length": 80,
            "waveforms": {
                "single": "5326049062739541677",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2131326862771937778": {
            "length": 40,
            "waveforms": {
                "I": "2131326862771937778_i",
                "Q": "2131326862771937778_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4444248903588921676": {
            "length": 40,
            "waveforms": {
                "I": "-4444248903588921676_i",
                "Q": "-4444248903588921676_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6358470172550542447": {
            "length": 40,
            "waveforms": {
                "I": "6358470172550542447_i",
                "Q": "6358470172550542447_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1226300238814970368": {
            "length": 40,
            "waveforms": {
                "I": "-1226300238814970368_i",
                "Q": "-1226300238814970368_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1370236233548375909_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "1370236233548375909_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "3400425378092587439": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-7453777329938855000_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-7453777329938855000_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5205339532812483545_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-5205339532812483545_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "734197750943754517_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "734197750943754517_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5597379543326980578_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "5597379543326980578_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-60446087009451205_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-60446087009451205_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1987390868038532237_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-1987390868038532237_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "1141891809292196426_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "1141891809292196426_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4266929678428962930": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "4393641214510328855": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-2069169990425796067": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-4421535659188090287": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-2995497748403949592": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "350083756776086044": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-5196095443385150857": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "3009433845841840922": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "3230927905040556170": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-2776841696183268746": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "5428687593043723033": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-7163520895752370693": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7784846663639064237": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9180159155069059718": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-5587086975635897374": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5365592916437182126": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4887300051460643892": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7178412388045274605": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "2686702356479442627": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4980652700042107742": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4759158640843392494": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5906980458020261267": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-8231538540107097720": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3709220770017094404": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2671810864186538715": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1523989047009669942": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-1289967022815212293": {
            "sample": 0.25,
            "type": "constant",
        },
        "2517204883427411358": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3943242794211552053": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7750414700454175704": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "6141002482214718916": {
            "sample": 0.25,
            "type": "constant",
        },
        "6362496541413434164": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8277075626053493801": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1975817341844332217": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-348740740242504236": {
            "sample": 0.25,
            "type": "constant",
        },
        "6747436757808508548": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-846106121023562592": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6466097498874278722": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "6592830777049381191": {
            "sample": 0.25,
            "type": "constant",
        },
        "7303722823986142221": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6620703479633406079": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4158685537554595168": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-1387493662606641733": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4201449732431523968": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "810266025396525130": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1031760084595240378": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-6635594971926309991": {
            "sample": 0.25,
            "type": "constant",
        },
        "3229519772598407241": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9181589029604945191": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8462729589625171587": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "8684223648823886835": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2545077586011436246": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7564760736882497918": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1612691479875959968": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-4979222825506222269": {
            "sample": 0.25,
            "type": "constant",
        },
        "585068208127206895": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5107385978217210211": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2559969078304340158": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "8293232116573140318": {
            "sample": 0.25,
            "type": "constant",
        },
        "8016037713157138104": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1382357244240012941": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5686894531263694948": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-1879722625021071297": {
            "sample": 0.25,
            "type": "constant",
        },
        "2241440354547294617": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "318037062982095566": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6270106319988633516": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-8497139810716323576": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8275645751517608328": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8552840154933610542": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6077886063514441465": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-223350478600983575": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7890705535122533944": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2326414501489104780": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2195903268600898536": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "7305152698522027694": {
            "sample": 0.25,
            "type": "constant",
        },
        "7429113085627662882": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5104555003540826429": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5326049062739541677": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "2131326862771937778_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "2131326862771937778_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-4444248903588921676_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-4444248903588921676_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "6358470172550542447_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "6358470172550542447_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "-1226300238814970368_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-1226300238814970368_q": {
            "samples": [-0.0003245581697577896, -0.0004143437926495826, -0.0005192451877881842, -0.0006385249144990759, -0.0007701923879260787, -0.0009108005732581567, -0.0010553365498202029, -0.0011972457129536525, -0.0013286216753579413, -0.0014405792538840587, -0.0015238070380387684, -0.0015692710288161837, -0.001569015034187334, -0.0015169810553923994, -0.0014097580972250387, -0.0012471643221046982, -0.001032577396853722, -0.0007729513005631845, -0.0004784924452043538, -0.00016200920159745424, 0.00016200920159745424, 0.0004784924452043538, 0.0007729513005631845, 0.001032577396853722, 0.0012471643221046982, 0.0014097580972250387, 0.0015169810553923994, 0.001569015034187334, 0.0015692710288161837, 0.0015238070380387684, 0.0014405792538840587, 0.0013286216753579413, 0.0011972457129536525, 0.0010553365498202029, 0.0009108005732581567, 0.0007701923879260787, 0.0006385249144990759, 0.0005192451877881842, 0.0004143437926495826, 0.0003245581697577896],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B1/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B1/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B1/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
        "cosine_weights_B3/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B3/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
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
                    "offset": -0.25498290735703955,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {},
            "digital_inputs": {},
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": -0.4530870218982913,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": -0.2224873138863394,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": -0.08416990010352905,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "7": {
                    "offset": 0.05418914676504196,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {},
            "digital_inputs": {},
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
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "7": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "7": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "3": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
            },
            "digital_inputs": {},
        },
        "con3": {
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
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "7": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "7": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
            },
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 1),
            },
            "intermediate_frequency": 0,
        },
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 3),
            },
            "intermediate_frequency": 0,
        },
        "B2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 2),
            },
            "intermediate_frequency": 0,
        },
        "D2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 4),
            },
            "intermediate_frequency": 0,
        },
        "B3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 3),
            },
            "intermediate_frequency": 0,
        },
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 5),
            },
            "intermediate_frequency": 0,
        },
        "B4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "5104555003540826429": "5104555003540826429",
                "5326049062739541677": "5326049062739541677",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 4),
            },
            "intermediate_frequency": 0,
        },
        "D4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 6),
            },
            "intermediate_frequency": 0,
        },
        "B5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con4', 1, 5),
            },
            "intermediate_frequency": 0,
        },
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con9', 1, 7),
            },
            "intermediate_frequency": 0,
        },
        "B1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "-3129629664977179120": "-3129629664977179120_B1/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B1/acquisition_mixer_e01",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
        },
        "B4/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "-998436112298849707": "-998436112298849707_B4/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B4/acquisition_mixer_c90",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
        "B3/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "5597379543326980578": "5597379543326980578",
                "6358470172550542447": "6358470172550542447",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con3', 1, 1),
                "Q": ('con3', 1, 2),
                "mixer": "B3/drive_mixer_cb8",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
        },
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-1987390868038532237": "-1987390868038532237",
                "-1226300238814970368": "-1226300238814970368",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con3', 1, 7),
                "Q": ('con3', 1, 8),
                "mixer": "B4/drive_mixer_dc3",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-5205339532812483545": "-5205339532812483545",
                "-4444248903588921676": "-4444248903588921676",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 7),
                "Q": ('con2', 1, 8),
                "mixer": "B2/drive_mixer_e2d",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
        },
        "B1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "1370236233548375909": "1370236233548375909",
                "2131326862771937778": "2131326862771937778",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 3),
                "Q": ('con2', 1, 4),
                "mixer": "B1/drive_mixer_109",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
        },
        "B3/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "-1453236510719896437": "-1453236510719896437_B3/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B3/acquisition_mixer_9b6",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
        },
        "B2/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1, 1),
                "out2": ('con2', 1, 2),
            },
            "operations": {
                "1365255557228087931": "1365255557228087931_B2/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B2/acquisition_mixer_283",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "1370236233548375909": {
            "length": 40,
            "waveforms": {
                "I": "1370236233548375909_i",
                "Q": "1370236233548375909_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3400425378092587439": {
            "length": 16,
            "waveforms": {
                "single": "3400425378092587439",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3129629664977179120_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7453777329938855000_i",
                "Q": "-7453777329938855000_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5205339532812483545": {
            "length": 40,
            "waveforms": {
                "I": "-5205339532812483545_i",
                "Q": "-5205339532812483545_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1365255557228087931_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "734197750943754517_i",
                "Q": "734197750943754517_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "5597379543326980578": {
            "length": 40,
            "waveforms": {
                "I": "5597379543326980578_i",
                "Q": "5597379543326980578_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1453236510719896437_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-60446087009451205_i",
                "Q": "-60446087009451205_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-1987390868038532237": {
            "length": 40,
            "waveforms": {
                "I": "-1987390868038532237_i",
                "Q": "-1987390868038532237_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-998436112298849707_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1141891809292196426_i",
                "Q": "1141891809292196426_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4266929678428962930": {
            "length": 16,
            "waveforms": {
                "single": "-4266929678428962930",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4393641214510328855": {
            "length": 16,
            "waveforms": {
                "single": "4393641214510328855",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2069169990425796067": {
            "length": 16,
            "waveforms": {
                "single": "-2069169990425796067",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4421535659188090287": {
            "length": 16,
            "waveforms": {
                "single": "-4421535659188090287",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2995497748403949592": {
            "length": 16,
            "waveforms": {
                "single": "-2995497748403949592",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "350083756776086044": {
            "length": 16,
            "waveforms": {
                "single": "350083756776086044",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5196095443385150857": {
            "length": 16,
            "waveforms": {
                "single": "-5196095443385150857",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3009433845841840922": {
            "length": 16,
            "waveforms": {
                "single": "3009433845841840922",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3230927905040556170": {
            "length": 16,
            "waveforms": {
                "single": "3230927905040556170",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2776841696183268746": {
            "length": 16,
            "waveforms": {
                "single": "-2776841696183268746",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5428687593043723033": {
            "length": 16,
            "waveforms": {
                "single": "5428687593043723033",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7163520895752370693": {
            "length": 16,
            "waveforms": {
                "single": "-7163520895752370693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7784846663639064237": {
            "length": 16,
            "waveforms": {
                "single": "-7784846663639064237",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9180159155069059718": {
            "length": 16,
            "waveforms": {
                "single": "9180159155069059718",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5587086975635897374": {
            "length": 16,
            "waveforms": {
                "single": "-5587086975635897374",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5365592916437182126": {
            "length": 20,
            "waveforms": {
                "single": "-5365592916437182126",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4887300051460643892": {
            "length": 20,
            "waveforms": {
                "single": "4887300051460643892",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7178412388045274605": {
            "length": 20,
            "waveforms": {
                "single": "-7178412388045274605",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2686702356479442627": {
            "length": 20,
            "waveforms": {
                "single": "2686702356479442627",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4980652700042107742": {
            "length": 24,
            "waveforms": {
                "single": "-4980652700042107742",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4759158640843392494": {
            "length": 24,
            "waveforms": {
                "single": "-4759158640843392494",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5906980458020261267": {
            "length": 24,
            "waveforms": {
                "single": "-5906980458020261267",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8231538540107097720": {
            "length": 24,
            "waveforms": {
                "single": "-8231538540107097720",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3709220770017094404": {
            "length": 28,
            "waveforms": {
                "single": "-3709220770017094404",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2671810864186538715": {
            "length": 28,
            "waveforms": {
                "single": "2671810864186538715",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1523989047009669942": {
            "length": 28,
            "waveforms": {
                "single": "1523989047009669942",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1289967022815212293": {
            "length": 28,
            "waveforms": {
                "single": "-1289967022815212293",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2517204883427411358": {
            "length": 32,
            "waveforms": {
                "single": "2517204883427411358",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3943242794211552053": {
            "length": 32,
            "waveforms": {
                "single": "3943242794211552053",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7750414700454175704": {
            "length": 32,
            "waveforms": {
                "single": "7750414700454175704",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6141002482214718916": {
            "length": 32,
            "waveforms": {
                "single": "6141002482214718916",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6362496541413434164": {
            "length": 36,
            "waveforms": {
                "single": "6362496541413434164",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8277075626053493801": {
            "length": 36,
            "waveforms": {
                "single": "-8277075626053493801",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1975817341844332217": {
            "length": 36,
            "waveforms": {
                "single": "1975817341844332217",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-348740740242504236": {
            "length": 36,
            "waveforms": {
                "single": "-348740740242504236",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6747436757808508548": {
            "length": 40,
            "waveforms": {
                "single": "6747436757808508548",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-846106121023562592": {
            "length": 40,
            "waveforms": {
                "single": "-846106121023562592",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6466097498874278722": {
            "length": 40,
            "waveforms": {
                "single": "-6466097498874278722",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6592830777049381191": {
            "length": 40,
            "waveforms": {
                "single": "6592830777049381191",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7303722823986142221": {
            "length": 44,
            "waveforms": {
                "single": "7303722823986142221",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6620703479633406079": {
            "length": 44,
            "waveforms": {
                "single": "-6620703479633406079",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4158685537554595168": {
            "length": 44,
            "waveforms": {
                "single": "4158685537554595168",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1387493662606641733": {
            "length": 44,
            "waveforms": {
                "single": "-1387493662606641733",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4201449732431523968": {
            "length": 48,
            "waveforms": {
                "single": "-4201449732431523968",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "810266025396525130": {
            "length": 48,
            "waveforms": {
                "single": "810266025396525130",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1031760084595240378": {
            "length": 48,
            "waveforms": {
                "single": "1031760084595240378",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6635594971926309991": {
            "length": 48,
            "waveforms": {
                "single": "-6635594971926309991",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3229519772598407241": {
            "length": 52,
            "waveforms": {
                "single": "3229519772598407241",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9181589029604945191": {
            "length": 52,
            "waveforms": {
                "single": "9181589029604945191",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8462729589625171587": {
            "length": 52,
            "waveforms": {
                "single": "8462729589625171587",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8684223648823886835": {
            "length": 52,
            "waveforms": {
                "single": "8684223648823886835",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2545077586011436246": {
            "length": 56,
            "waveforms": {
                "single": "-2545077586011436246",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7564760736882497918": {
            "length": 56,
            "waveforms": {
                "single": "-7564760736882497918",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1612691479875959968": {
            "length": 56,
            "waveforms": {
                "single": "-1612691479875959968",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4979222825506222269": {
            "length": 56,
            "waveforms": {
                "single": "-4979222825506222269",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "585068208127206895": {
            "length": 60,
            "waveforms": {
                "single": "585068208127206895",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5107385978217210211": {
            "length": 60,
            "waveforms": {
                "single": "5107385978217210211",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2559969078304340158": {
            "length": 60,
            "waveforms": {
                "single": "-2559969078304340158",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8293232116573140318": {
            "length": 60,
            "waveforms": {
                "single": "8293232116573140318",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8016037713157138104": {
            "length": 64,
            "waveforms": {
                "single": "8016037713157138104",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1382357244240012941": {
            "length": 64,
            "waveforms": {
                "single": "-1382357244240012941",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5686894531263694948": {
            "length": 64,
            "waveforms": {
                "single": "-5686894531263694948",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1879722625021071297": {
            "length": 64,
            "waveforms": {
                "single": "-1879722625021071297",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2241440354547294617": {
            "length": 68,
            "waveforms": {
                "single": "2241440354547294617",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "318037062982095566": {
            "length": 68,
            "waveforms": {
                "single": "318037062982095566",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6270106319988633516": {
            "length": 68,
            "waveforms": {
                "single": "6270106319988633516",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8497139810716323576": {
            "length": 68,
            "waveforms": {
                "single": "-8497139810716323576",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8275645751517608328": {
            "length": 72,
            "waveforms": {
                "single": "-8275645751517608328",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8552840154933610542": {
            "length": 72,
            "waveforms": {
                "single": "-8552840154933610542",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6077886063514441465": {
            "length": 72,
            "waveforms": {
                "single": "-6077886063514441465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-223350478600983575": {
            "length": 72,
            "waveforms": {
                "single": "-223350478600983575",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7890705535122533944": {
            "length": 76,
            "waveforms": {
                "single": "-7890705535122533944",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2326414501489104780": {
            "length": 76,
            "waveforms": {
                "single": "-2326414501489104780",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2195903268600898536": {
            "length": 76,
            "waveforms": {
                "single": "2195903268600898536",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7305152698522027694": {
            "length": 76,
            "waveforms": {
                "single": "7305152698522027694",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7429113085627662882": {
            "length": 80,
            "waveforms": {
                "single": "7429113085627662882",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5104555003540826429": {
            "length": 80,
            "waveforms": {
                "single": "5104555003540826429",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5326049062739541677": {
            "length": 80,
            "waveforms": {
                "single": "5326049062739541677",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2131326862771937778": {
            "length": 40,
            "waveforms": {
                "I": "2131326862771937778_i",
                "Q": "2131326862771937778_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4444248903588921676": {
            "length": 40,
            "waveforms": {
                "I": "-4444248903588921676_i",
                "Q": "-4444248903588921676_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6358470172550542447": {
            "length": 40,
            "waveforms": {
                "I": "6358470172550542447_i",
                "Q": "6358470172550542447_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1226300238814970368": {
            "length": 40,
            "waveforms": {
                "I": "-1226300238814970368_i",
                "Q": "-1226300238814970368_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "1370236233548375909_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1370236233548375909_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3400425378092587439": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7453777329938855000_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-7453777329938855000_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-5205339532812483545_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5205339532812483545_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "734197750943754517_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "734197750943754517_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "5597379543326980578_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5597379543326980578_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-60446087009451205_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-60446087009451205_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-1987390868038532237_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1987390868038532237_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1141891809292196426_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "1141891809292196426_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4266929678428962930": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4393641214510328855": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2069169990425796067": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4421535659188090287": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2995497748403949592": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "350083756776086044": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5196095443385150857": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3009433845841840922": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3230927905040556170": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2776841696183268746": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5428687593043723033": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7163520895752370693": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7784846663639064237": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9180159155069059718": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5587086975635897374": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5365592916437182126": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4887300051460643892": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7178412388045274605": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2686702356479442627": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4980652700042107742": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4759158640843392494": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5906980458020261267": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8231538540107097720": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3709220770017094404": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2671810864186538715": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1523989047009669942": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1289967022815212293": {
            "type": "constant",
            "sample": 0.25,
        },
        "2517204883427411358": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3943242794211552053": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7750414700454175704": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6141002482214718916": {
            "type": "constant",
            "sample": 0.25,
        },
        "6362496541413434164": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8277075626053493801": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1975817341844332217": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-348740740242504236": {
            "type": "constant",
            "sample": 0.25,
        },
        "6747436757808508548": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-846106121023562592": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6466097498874278722": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6592830777049381191": {
            "type": "constant",
            "sample": 0.25,
        },
        "7303722823986142221": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6620703479633406079": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4158685537554595168": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1387493662606641733": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4201449732431523968": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "810266025396525130": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1031760084595240378": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6635594971926309991": {
            "type": "constant",
            "sample": 0.25,
        },
        "3229519772598407241": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9181589029604945191": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8462729589625171587": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8684223648823886835": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2545077586011436246": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7564760736882497918": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1612691479875959968": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4979222825506222269": {
            "type": "constant",
            "sample": 0.25,
        },
        "585068208127206895": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5107385978217210211": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2559969078304340158": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8293232116573140318": {
            "type": "constant",
            "sample": 0.25,
        },
        "8016037713157138104": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1382357244240012941": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5686894531263694948": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1879722625021071297": {
            "type": "constant",
            "sample": 0.25,
        },
        "2241440354547294617": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "318037062982095566": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6270106319988633516": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8497139810716323576": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8275645751517608328": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8552840154933610542": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6077886063514441465": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-223350478600983575": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7890705535122533944": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2326414501489104780": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2195903268600898536": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7305152698522027694": {
            "type": "constant",
            "sample": 0.25,
        },
        "7429113085627662882": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5104555003540826429": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5326049062739541677": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2131326862771937778_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2131326862771937778_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4444248903588921676_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4444248903588921676_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6358470172550542447_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6358470172550542447_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1226300238814970368_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1226300238814970368_q": {
            "type": "arbitrary",
            "samples": [-0.0003245581697577896, -0.0004143437926495826, -0.0005192451877881842, -0.0006385249144990759, -0.0007701923879260787, -0.0009108005732581567, -0.0010553365498202029, -0.0011972457129536525, -0.0013286216753579413, -0.0014405792538840587, -0.0015238070380387684, -0.0015692710288161837, -0.001569015034187334, -0.0015169810553923994, -0.0014097580972250387, -0.0012471643221046982, -0.001032577396853722, -0.0007729513005631845, -0.0004784924452043538, -0.00016200920159745424, 0.00016200920159745424, 0.0004784924452043538, 0.0007729513005631845, 0.001032577396853722, 0.0012471643221046982, 0.0014097580972250387, 0.0015169810553923994, 0.001569015034187334, 0.0015692710288161837, 0.0015238070380387684, 0.0014405792538840587, 0.0013286216753579413, 0.0011972457129536525, 0.0010553365498202029, 0.0009108005732581567, 0.0007701923879260787, 0.0006385249144990759, 0.0005192451877881842, 0.0004143437926495826, 0.0003245581697577896],
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
        "cosine_weights_B1/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B1/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B3/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B3/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B1/acquisition_mixer_e01": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_c90": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_cb8": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_dc3": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_e2d": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_109": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_9b6": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_283": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

