
# Single QUA script generated at 2025-02-16 09:42:08.882518
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
        play("-509142008191373131", "B1/drive")
        wait(11, "B1/flux")
        play("-1358938236425714257", "B1/flux")
        wait(46, "B1/drive")
        play("251948621032188738", "B1/drive")
        wait(66, "B1/acquisition")
        measure("7598755360110157980", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        r1 = declare_stream()
        save(v4, r1)
        play("8788166571196309563", "B2/drive")
        wait(11, "B2/flux")
        play("-1358938236425714257", "B2/flux")
        wait(46, "B2/drive")
        play("-8897486873289680184", "B2/drive")
        wait(66, "B2/acquisition")
        measure("6980055167868760827", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        r2 = declare_stream()
        save(v7, r2)
        play("-5980521366525302411", "B3/drive")
        wait(11, "B3/flux")
        play("-1358938236425714257", "B3/flux")
        wait(46, "B3/drive")
        play("-5219430737301740542", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-7749198133802554073", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        r3 = declare_stream()
        save(v10, r3)
        play("8420437388926352468", "B4/drive")
        wait(11, "B4/flux")
        play("-1358938236425714257", "B4/flux")
        wait(46, "B4/drive")
        play("2135498729515057512", "B4/drive")
        wait(66, "B4/acquisition")
        measure("147005063594526682", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25501, "B3/drive")
        wait(25001, "B3/acquisition")
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25536, "B2/flux")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25536, "B3/flux")
        wait(25001, "B1/acquisition")
        wait(25536, "B1/flux")
        play("-509142008191373131", "B1/drive")
        wait(11, "B1/flux")
        play("2448233669816909394", "B1/flux")
        wait(46, "B1/drive")
        play("251948621032188738", "B1/drive")
        wait(66, "B1/acquisition")
        measure("7598755360110157980", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        save(v4, r1)
        play("8788166571196309563", "B2/drive")
        wait(11, "B2/flux")
        play("2448233669816909394", "B2/flux")
        wait(46, "B2/drive")
        play("-8897486873289680184", "B2/drive")
        wait(66, "B2/acquisition")
        measure("6980055167868760827", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        save(v7, r2)
        play("-5980521366525302411", "B3/drive")
        wait(11, "B3/flux")
        play("2448233669816909394", "B3/flux")
        wait(46, "B3/drive")
        play("-5219430737301740542", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-7749198133802554073", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        save(v10, r3)
        play("8420437388926352468", "B4/drive")
        wait(11, "B4/flux")
        play("2448233669816909394", "B4/flux")
        wait(46, "B4/drive")
        play("2135498729515057512", "B4/drive")
        wait(66, "B4/acquisition")
        measure("147005063594526682", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        save(v13, r4)
        wait(25001, "B2/acquisition")
        wait(25501, "B2/drive")
        wait(25501, "B3/drive")
        wait(25001, "B3/acquisition")
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25536, "B2/flux")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25536, "B3/flux")
        wait(25001, "B1/acquisition")
        wait(25536, "B1/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("7598755360110157980_B1|acquisition_shots")
        r2.buffer(2).average().save("6980055167868760827_B2|acquisition_shots")
        r3.buffer(2).average().save("-7749198133802554073_B3|acquisition_shots")
        r4.buffer(2).average().save("147005063594526682_B4|acquisition_shots")


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
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "6980055167868760827": "6980055167868760827_B2/acquisition",
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
                "8788166571196309563": "8788166571196309563",
                "-8897486873289680184": "-8897486873289680184",
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
                "-5980521366525302411": "-5980521366525302411",
                "-5219430737301740542": "-5219430737301740542",
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
                "-7749198133802554073": "-7749198133802554073_B3/acquisition",
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
                "-509142008191373131": "-509142008191373131",
                "251948621032188738": "251948621032188738",
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
                "8420437388926352468": "8420437388926352468",
                "2135498729515057512": "2135498729515057512",
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
                "147005063594526682": "147005063594526682_B4/acquisition",
            },
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
                "7598755360110157980": "7598755360110157980_B1/acquisition",
            },
        },
    },
    "pulses": {
        "-509142008191373131": {
            "length": 40,
            "waveforms": {
                "I": "-509142008191373131_i",
                "Q": "-509142008191373131_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6813663854744930395": {
            "length": 16,
            "waveforms": {
                "single": "-6813663854744930395",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7598755360110157980_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3814327639956776265_i",
                "Q": "3814327639956776265_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "8788166571196309563": {
            "length": 40,
            "waveforms": {
                "I": "8788166571196309563_i",
                "Q": "8788166571196309563_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6980055167868760827_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5842765145834467911_i",
                "Q": "5842765145834467911_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-5980521366525302411": {
            "length": 40,
            "waveforms": {
                "I": "-5980521366525302411_i",
                "Q": "-5980521366525302411_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7749198133802554073_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-266868079877993960_i",
                "Q": "-266868079877993960_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "8420437388926352468": {
            "length": 40,
            "waveforms": {
                "I": "8420437388926352468_i",
                "Q": "8420437388926352468_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "147005063594526682_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6679421581380004989_i",
                "Q": "6679421581380004989_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "282513643306082389": {
            "length": 16,
            "waveforms": {
                "single": "282513643306082389",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4089685549548706040": {
            "length": 16,
            "waveforms": {
                "single": "4089685549548706040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5959509940161032232": {
            "length": 16,
            "waveforms": {
                "single": "5959509940161032232",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6287445237551872903": {
            "length": 16,
            "waveforms": {
                "single": "6287445237551872903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "838799709483716062": {
            "length": 16,
            "waveforms": {
                "single": "838799709483716062",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5361117479573719378": {
            "length": 16,
            "waveforms": {
                "single": "5361117479573719378",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2306237576947830991": {
            "length": 16,
            "waveforms": {
                "single": "-2306237576947830991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7558877167576886241": {
            "length": 16,
            "waveforms": {
                "single": "7558877167576886241",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4506835271929032256": {
            "length": 16,
            "waveforms": {
                "single": "-4506835271929032256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8491263273712362519": {
            "length": 16,
            "waveforms": {
                "single": "8491263273712362519",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5433163029907185781": {
            "length": 16,
            "waveforms": {
                "single": "-5433163029907185781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3642993673080672557": {
            "length": 16,
            "waveforms": {
                "single": "3642993673080672557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3235403341904018918": {
            "length": 16,
            "waveforms": {
                "single": "-3235403341904018918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7543985675283982329": {
            "length": 16,
            "waveforms": {
                "single": "7543985675283982329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5048222813512111397": {
            "length": 16,
            "waveforms": {
                "single": "-5048222813512111397",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5669548581398804941": {
            "length": 20,
            "waveforms": {
                "single": "-5669548581398804941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7151286836400232602": {
            "length": 20,
            "waveforms": {
                "single": "-7151286836400232602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2628969066310229286": {
            "length": 20,
            "waveforms": {
                "single": "-2628969066310229286",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5824154562157932298": {
            "length": 20,
            "waveforms": {
                "single": "-5824154562157932298",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7002598133700903188": {
            "length": 24,
            "waveforms": {
                "single": "7002598133700903188",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5879854906375219264": {
            "length": 24,
            "waveforms": {
                "single": "-5879854906375219264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4802000438719701923": {
            "length": 24,
            "waveforms": {
                "single": "4802000438719701923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9024892192806766317": {
            "length": 24,
            "waveforms": {
                "single": "-9024892192806766317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5217720286564142666": {
            "length": 28,
            "waveforms": {
                "single": "-5217720286564142666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5494914689980144880": {
            "length": 28,
            "waveforms": {
                "single": "-5494914689980144880",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5358286504897335596": {
            "length": 28,
            "waveforms": {
                "single": "5358286504897335596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1593922687776835108": {
            "length": 28,
            "waveforms": {
                "single": "-1593922687776835108",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2213249218465788543": {
            "length": 32,
            "waveforms": {
                "single": "2213249218465788543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7777540252099217707": {
            "length": 32,
            "waveforms": {
                "single": "7777540252099217707",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6146886051520330593": {
            "length": 32,
            "waveforms": {
                "single": "-6146886051520330593",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8083665910234058260": {
            "length": 32,
            "waveforms": {
                "single": "-8083665910234058260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3484681148490801881": {
            "length": 36,
            "waveforms": {
                "single": "3484681148490801881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2002942893489374220": {
            "length": 36,
            "waveforms": {
                "single": "2002942893489374220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1284083453509600616": {
            "length": 36,
            "waveforms": {
                "single": "1284083453509600616",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5903934895692683992": {
            "length": 36,
            "waveforms": {
                "single": "5903934895692683992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-431202346005411803": {
            "length": 40,
            "waveforms": {
                "single": "-431202346005411803",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9012831675190246187": {
            "length": 40,
            "waveforms": {
                "single": "-9012831675190246187",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8791337615991530939": {
            "length": 40,
            "waveforms": {
                "single": "-8791337615991530939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6288875112087758376": {
            "length": 40,
            "waveforms": {
                "single": "6288875112087758376",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6510369171286473624": {
            "length": 44,
            "waveforms": {
                "single": "6510369171286473624",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6924659144595028894": {
            "length": 44,
            "waveforms": {
                "single": "-6924659144595028894",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1360368110961599730": {
            "length": 44,
            "waveforms": {
                "single": "-1360368110961599730",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1138874051762884482": {
            "length": 44,
            "waveforms": {
                "single": "-1138874051762884482",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4505405397393146783": {
            "length": 48,
            "waveforms": {
                "single": "-4505405397393146783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4283911338194431535": {
            "length": 48,
            "waveforms": {
                "single": "-4283911338194431535",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-975427894566525346": {
            "length": 48,
            "waveforms": {
                "single": "-975427894566525346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3644423547616558030": {
            "length": 48,
            "waveforms": {
                "single": "3644423547616558030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3233973467368133445": {
            "length": 52,
            "waveforms": {
                "single": "-3233973467368133445",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3147058166835499674": {
            "length": 52,
            "waveforms": {
                "single": "3147058166835499674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-908539816126937455": {
            "length": 52,
            "waveforms": {
                "single": "-908539816126937455",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7371351021063062377": {
            "length": 52,
            "waveforms": {
                "single": "-7371351021063062377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8723027383884195019": {
            "length": 56,
            "waveforms": {
                "single": "8723027383884195019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2627539191774343813": {
            "length": 56,
            "waveforms": {
                "single": "-2627539191774343813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4952097273861180266": {
            "length": 56,
            "waveforms": {
                "single": "-4952097273861180266",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6743923748101709002": {
            "length": 56,
            "waveforms": {
                "single": "6743923748101709002",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8023322382603248090": {
            "length": 60,
            "waveforms": {
                "single": "-8023322382603248090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2071253125596710140": {
            "length": 60,
            "waveforms": {
                "single": "-2071253125596710140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8079022726820535056": {
            "length": 60,
            "waveforms": {
                "single": "-8079022726820535056",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "126506562406456723": {
            "length": 60,
            "waveforms": {
                "single": "126506562406456723",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5493484815444259407": {
            "length": 64,
            "waveforms": {
                "single": "-5493484815444259407",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7416888107009458458": {
            "length": 64,
            "waveforms": {
                "single": "-7416888107009458458",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5581210438631936317": {
            "length": 64,
            "waveforms": {
                "single": "5581210438631936317",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "511446778801531107": {
            "length": 64,
            "waveforms": {
                "single": "511446778801531107",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7778970126635103180": {
            "length": 68,
            "waveforms": {
                "single": "7778970126635103180",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6145456176984445120": {
            "length": 68,
            "waveforms": {
                "single": "-6145456176984445120",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4633932840203556127": {
            "length": 68,
            "waveforms": {
                "single": "4633932840203556127",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2615478674157823683": {
            "length": 68,
            "waveforms": {
                "single": "-2615478674157823683",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8163910343030177564": {
            "length": 72,
            "waveforms": {
                "single": "8163910343030177564",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8385404402228892812": {
            "length": 72,
            "waveforms": {
                "single": "8385404402228892812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1507007387244201337": {
            "length": 72,
            "waveforms": {
                "single": "1507007387244201337",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7863579983477491941": {
            "length": 72,
            "waveforms": {
                "single": "-7863579983477491941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9011401800654360714": {
            "length": 76,
            "waveforms": {
                "single": "-9011401800654360714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2630370166450727595": {
            "length": 76,
            "waveforms": {
                "single": "-2630370166450727595",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4982735835213021815": {
            "length": 76,
            "waveforms": {
                "single": "-4982735835213021815",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7456238637272704885": {
            "length": 76,
            "waveforms": {
                "single": "7456238637272704885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-211116419248845484": {
            "length": 80,
            "waveforms": {
                "single": "-211116419248845484",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1358938236425714257": {
            "length": 80,
            "waveforms": {
                "single": "-1358938236425714257",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2448233669816909394": {
            "length": 80,
            "waveforms": {
                "single": "2448233669816909394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "251948621032188738": {
            "length": 40,
            "waveforms": {
                "I": "251948621032188738_i",
                "Q": "251948621032188738_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8897486873289680184": {
            "length": 40,
            "waveforms": {
                "I": "-8897486873289680184_i",
                "Q": "-8897486873289680184_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5219430737301740542": {
            "length": 40,
            "waveforms": {
                "I": "-5219430737301740542_i",
                "Q": "-5219430737301740542_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2135498729515057512": {
            "length": 40,
            "waveforms": {
                "I": "2135498729515057512_i",
                "Q": "2135498729515057512_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-509142008191373131_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-509142008191373131_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-6813663854744930395": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "3814327639956776265_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "3814327639956776265_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8788166571196309563_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "8788166571196309563_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "5842765145834467911_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5842765145834467911_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5980521366525302411_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-5980521366525302411_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-266868079877993960_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-266868079877993960_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8420437388926352468_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "8420437388926352468_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "6679421581380004989_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "6679421581380004989_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "282513643306082389": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "4089685549548706040": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "5959509940161032232": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "6287445237551872903": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "838799709483716062": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "5361117479573719378": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-2306237576947830991": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "7558877167576886241": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-4506835271929032256": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "8491263273712362519": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-5433163029907185781": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "3642993673080672557": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3235403341904018918": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7543985675283982329": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-5048222813512111397": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5669548581398804941": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7151286836400232602": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2628969066310229286": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5824154562157932298": {
            "sample": 0.25,
            "type": "constant",
        },
        "7002598133700903188": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5879854906375219264": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4802000438719701923": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-9024892192806766317": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5217720286564142666": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5494914689980144880": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5358286504897335596": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-1593922687776835108": {
            "sample": 0.25,
            "type": "constant",
        },
        "2213249218465788543": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7777540252099217707": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6146886051520330593": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-8083665910234058260": {
            "sample": 0.25,
            "type": "constant",
        },
        "3484681148490801881": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2002942893489374220": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1284083453509600616": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "5903934895692683992": {
            "sample": 0.25,
            "type": "constant",
        },
        "-431202346005411803": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9012831675190246187": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8791337615991530939": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "6288875112087758376": {
            "sample": 0.25,
            "type": "constant",
        },
        "6510369171286473624": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6924659144595028894": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1360368110961599730": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-1138874051762884482": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4505405397393146783": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4283911338194431535": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-975427894566525346": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "3644423547616558030": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3233973467368133445": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3147058166835499674": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-908539816126937455": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-7371351021063062377": {
            "sample": 0.25,
            "type": "constant",
        },
        "8723027383884195019": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2627539191774343813": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4952097273861180266": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "6743923748101709002": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8023322382603248090": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2071253125596710140": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8079022726820535056": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "126506562406456723": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5493484815444259407": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7416888107009458458": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5581210438631936317": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "511446778801531107": {
            "sample": 0.25,
            "type": "constant",
        },
        "7778970126635103180": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6145456176984445120": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4633932840203556127": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-2615478674157823683": {
            "sample": 0.25,
            "type": "constant",
        },
        "8163910343030177564": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8385404402228892812": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1507007387244201337": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-7863579983477491941": {
            "sample": 0.25,
            "type": "constant",
        },
        "-9011401800654360714": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2630370166450727595": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4982735835213021815": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "7456238637272704885": {
            "sample": 0.25,
            "type": "constant",
        },
        "-211116419248845484": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1358938236425714257": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2448233669816909394": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "251948621032188738_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "251948621032188738_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-8897486873289680184_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-8897486873289680184_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-5219430737301740542_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-5219430737301740542_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "2135498729515057512_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "2135498729515057512_q": {
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
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "-1358938236425714257": "-1358938236425714257",
                "2448233669816909394": "2448233669816909394",
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
                "6980055167868760827": "6980055167868760827_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_d3d",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "8788166571196309563": "8788166571196309563",
                "-8897486873289680184": "-8897486873289680184",
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
                "mixer": "B2/drive_mixer_642",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "-5980521366525302411": "-5980521366525302411",
                "-5219430737301740542": "-5219430737301740542",
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
                "mixer": "B3/drive_mixer_559",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-7749198133802554073": "-7749198133802554073_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_c55",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "-509142008191373131": "-509142008191373131",
                "251948621032188738": "251948621032188738",
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
                "mixer": "B1/drive_mixer_d6a",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "8420437388926352468": "8420437388926352468",
                "2135498729515057512": "2135498729515057512",
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
                "mixer": "B4/drive_mixer_b19",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "147005063594526682": "147005063594526682_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_ae2",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "7598755360110157980": "7598755360110157980_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_c25",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
        },
    },
    "pulses": {
        "-509142008191373131": {
            "length": 40,
            "waveforms": {
                "I": "-509142008191373131_i",
                "Q": "-509142008191373131_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6813663854744930395": {
            "length": 16,
            "waveforms": {
                "single": "-6813663854744930395",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7598755360110157980_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3814327639956776265_i",
                "Q": "3814327639956776265_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8788166571196309563": {
            "length": 40,
            "waveforms": {
                "I": "8788166571196309563_i",
                "Q": "8788166571196309563_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6980055167868760827_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5842765145834467911_i",
                "Q": "5842765145834467911_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5980521366525302411": {
            "length": 40,
            "waveforms": {
                "I": "-5980521366525302411_i",
                "Q": "-5980521366525302411_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7749198133802554073_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-266868079877993960_i",
                "Q": "-266868079877993960_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8420437388926352468": {
            "length": 40,
            "waveforms": {
                "I": "8420437388926352468_i",
                "Q": "8420437388926352468_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "147005063594526682_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6679421581380004989_i",
                "Q": "6679421581380004989_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "282513643306082389": {
            "length": 16,
            "waveforms": {
                "single": "282513643306082389",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4089685549548706040": {
            "length": 16,
            "waveforms": {
                "single": "4089685549548706040",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5959509940161032232": {
            "length": 16,
            "waveforms": {
                "single": "5959509940161032232",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6287445237551872903": {
            "length": 16,
            "waveforms": {
                "single": "6287445237551872903",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "838799709483716062": {
            "length": 16,
            "waveforms": {
                "single": "838799709483716062",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5361117479573719378": {
            "length": 16,
            "waveforms": {
                "single": "5361117479573719378",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2306237576947830991": {
            "length": 16,
            "waveforms": {
                "single": "-2306237576947830991",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7558877167576886241": {
            "length": 16,
            "waveforms": {
                "single": "7558877167576886241",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4506835271929032256": {
            "length": 16,
            "waveforms": {
                "single": "-4506835271929032256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8491263273712362519": {
            "length": 16,
            "waveforms": {
                "single": "8491263273712362519",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5433163029907185781": {
            "length": 16,
            "waveforms": {
                "single": "-5433163029907185781",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3642993673080672557": {
            "length": 16,
            "waveforms": {
                "single": "3642993673080672557",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3235403341904018918": {
            "length": 16,
            "waveforms": {
                "single": "-3235403341904018918",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7543985675283982329": {
            "length": 16,
            "waveforms": {
                "single": "7543985675283982329",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5048222813512111397": {
            "length": 16,
            "waveforms": {
                "single": "-5048222813512111397",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5669548581398804941": {
            "length": 20,
            "waveforms": {
                "single": "-5669548581398804941",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7151286836400232602": {
            "length": 20,
            "waveforms": {
                "single": "-7151286836400232602",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2628969066310229286": {
            "length": 20,
            "waveforms": {
                "single": "-2628969066310229286",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5824154562157932298": {
            "length": 20,
            "waveforms": {
                "single": "-5824154562157932298",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7002598133700903188": {
            "length": 24,
            "waveforms": {
                "single": "7002598133700903188",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5879854906375219264": {
            "length": 24,
            "waveforms": {
                "single": "-5879854906375219264",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4802000438719701923": {
            "length": 24,
            "waveforms": {
                "single": "4802000438719701923",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9024892192806766317": {
            "length": 24,
            "waveforms": {
                "single": "-9024892192806766317",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5217720286564142666": {
            "length": 28,
            "waveforms": {
                "single": "-5217720286564142666",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5494914689980144880": {
            "length": 28,
            "waveforms": {
                "single": "-5494914689980144880",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5358286504897335596": {
            "length": 28,
            "waveforms": {
                "single": "5358286504897335596",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1593922687776835108": {
            "length": 28,
            "waveforms": {
                "single": "-1593922687776835108",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2213249218465788543": {
            "length": 32,
            "waveforms": {
                "single": "2213249218465788543",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7777540252099217707": {
            "length": 32,
            "waveforms": {
                "single": "7777540252099217707",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6146886051520330593": {
            "length": 32,
            "waveforms": {
                "single": "-6146886051520330593",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8083665910234058260": {
            "length": 32,
            "waveforms": {
                "single": "-8083665910234058260",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3484681148490801881": {
            "length": 36,
            "waveforms": {
                "single": "3484681148490801881",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2002942893489374220": {
            "length": 36,
            "waveforms": {
                "single": "2002942893489374220",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1284083453509600616": {
            "length": 36,
            "waveforms": {
                "single": "1284083453509600616",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5903934895692683992": {
            "length": 36,
            "waveforms": {
                "single": "5903934895692683992",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-431202346005411803": {
            "length": 40,
            "waveforms": {
                "single": "-431202346005411803",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9012831675190246187": {
            "length": 40,
            "waveforms": {
                "single": "-9012831675190246187",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8791337615991530939": {
            "length": 40,
            "waveforms": {
                "single": "-8791337615991530939",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6288875112087758376": {
            "length": 40,
            "waveforms": {
                "single": "6288875112087758376",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6510369171286473624": {
            "length": 44,
            "waveforms": {
                "single": "6510369171286473624",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6924659144595028894": {
            "length": 44,
            "waveforms": {
                "single": "-6924659144595028894",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1360368110961599730": {
            "length": 44,
            "waveforms": {
                "single": "-1360368110961599730",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1138874051762884482": {
            "length": 44,
            "waveforms": {
                "single": "-1138874051762884482",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4505405397393146783": {
            "length": 48,
            "waveforms": {
                "single": "-4505405397393146783",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4283911338194431535": {
            "length": 48,
            "waveforms": {
                "single": "-4283911338194431535",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-975427894566525346": {
            "length": 48,
            "waveforms": {
                "single": "-975427894566525346",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3644423547616558030": {
            "length": 48,
            "waveforms": {
                "single": "3644423547616558030",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3233973467368133445": {
            "length": 52,
            "waveforms": {
                "single": "-3233973467368133445",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3147058166835499674": {
            "length": 52,
            "waveforms": {
                "single": "3147058166835499674",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-908539816126937455": {
            "length": 52,
            "waveforms": {
                "single": "-908539816126937455",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7371351021063062377": {
            "length": 52,
            "waveforms": {
                "single": "-7371351021063062377",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8723027383884195019": {
            "length": 56,
            "waveforms": {
                "single": "8723027383884195019",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2627539191774343813": {
            "length": 56,
            "waveforms": {
                "single": "-2627539191774343813",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4952097273861180266": {
            "length": 56,
            "waveforms": {
                "single": "-4952097273861180266",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6743923748101709002": {
            "length": 56,
            "waveforms": {
                "single": "6743923748101709002",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8023322382603248090": {
            "length": 60,
            "waveforms": {
                "single": "-8023322382603248090",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2071253125596710140": {
            "length": 60,
            "waveforms": {
                "single": "-2071253125596710140",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8079022726820535056": {
            "length": 60,
            "waveforms": {
                "single": "-8079022726820535056",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "126506562406456723": {
            "length": 60,
            "waveforms": {
                "single": "126506562406456723",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5493484815444259407": {
            "length": 64,
            "waveforms": {
                "single": "-5493484815444259407",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7416888107009458458": {
            "length": 64,
            "waveforms": {
                "single": "-7416888107009458458",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5581210438631936317": {
            "length": 64,
            "waveforms": {
                "single": "5581210438631936317",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "511446778801531107": {
            "length": 64,
            "waveforms": {
                "single": "511446778801531107",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7778970126635103180": {
            "length": 68,
            "waveforms": {
                "single": "7778970126635103180",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6145456176984445120": {
            "length": 68,
            "waveforms": {
                "single": "-6145456176984445120",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4633932840203556127": {
            "length": 68,
            "waveforms": {
                "single": "4633932840203556127",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2615478674157823683": {
            "length": 68,
            "waveforms": {
                "single": "-2615478674157823683",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8163910343030177564": {
            "length": 72,
            "waveforms": {
                "single": "8163910343030177564",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8385404402228892812": {
            "length": 72,
            "waveforms": {
                "single": "8385404402228892812",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1507007387244201337": {
            "length": 72,
            "waveforms": {
                "single": "1507007387244201337",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7863579983477491941": {
            "length": 72,
            "waveforms": {
                "single": "-7863579983477491941",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9011401800654360714": {
            "length": 76,
            "waveforms": {
                "single": "-9011401800654360714",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2630370166450727595": {
            "length": 76,
            "waveforms": {
                "single": "-2630370166450727595",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4982735835213021815": {
            "length": 76,
            "waveforms": {
                "single": "-4982735835213021815",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7456238637272704885": {
            "length": 76,
            "waveforms": {
                "single": "7456238637272704885",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-211116419248845484": {
            "length": 80,
            "waveforms": {
                "single": "-211116419248845484",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1358938236425714257": {
            "length": 80,
            "waveforms": {
                "single": "-1358938236425714257",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2448233669816909394": {
            "length": 80,
            "waveforms": {
                "single": "2448233669816909394",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "251948621032188738": {
            "length": 40,
            "waveforms": {
                "I": "251948621032188738_i",
                "Q": "251948621032188738_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8897486873289680184": {
            "length": 40,
            "waveforms": {
                "I": "-8897486873289680184_i",
                "Q": "-8897486873289680184_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5219430737301740542": {
            "length": 40,
            "waveforms": {
                "I": "-5219430737301740542_i",
                "Q": "-5219430737301740542_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2135498729515057512": {
            "length": 40,
            "waveforms": {
                "I": "2135498729515057512_i",
                "Q": "2135498729515057512_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-509142008191373131_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-509142008191373131_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6813663854744930395": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3814327639956776265_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "3814327639956776265_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8788166571196309563_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8788166571196309563_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5842765145834467911_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "5842765145834467911_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-5980521366525302411_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5980521366525302411_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-266868079877993960_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-266868079877993960_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8420437388926352468_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8420437388926352468_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6679421581380004989_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "6679421581380004989_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "282513643306082389": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4089685549548706040": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5959509940161032232": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6287445237551872903": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "838799709483716062": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5361117479573719378": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2306237576947830991": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7558877167576886241": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4506835271929032256": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8491263273712362519": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5433163029907185781": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3642993673080672557": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3235403341904018918": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7543985675283982329": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5048222813512111397": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5669548581398804941": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7151286836400232602": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2628969066310229286": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5824154562157932298": {
            "type": "constant",
            "sample": 0.25,
        },
        "7002598133700903188": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5879854906375219264": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4802000438719701923": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9024892192806766317": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5217720286564142666": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5494914689980144880": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5358286504897335596": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1593922687776835108": {
            "type": "constant",
            "sample": 0.25,
        },
        "2213249218465788543": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7777540252099217707": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6146886051520330593": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8083665910234058260": {
            "type": "constant",
            "sample": 0.25,
        },
        "3484681148490801881": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2002942893489374220": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1284083453509600616": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5903934895692683992": {
            "type": "constant",
            "sample": 0.25,
        },
        "-431202346005411803": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9012831675190246187": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8791337615991530939": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6288875112087758376": {
            "type": "constant",
            "sample": 0.25,
        },
        "6510369171286473624": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6924659144595028894": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1360368110961599730": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1138874051762884482": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4505405397393146783": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4283911338194431535": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-975427894566525346": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3644423547616558030": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3233973467368133445": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3147058166835499674": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-908539816126937455": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7371351021063062377": {
            "type": "constant",
            "sample": 0.25,
        },
        "8723027383884195019": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2627539191774343813": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4952097273861180266": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6743923748101709002": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8023322382603248090": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2071253125596710140": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8079022726820535056": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "126506562406456723": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5493484815444259407": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7416888107009458458": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5581210438631936317": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "511446778801531107": {
            "type": "constant",
            "sample": 0.25,
        },
        "7778970126635103180": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6145456176984445120": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4633932840203556127": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2615478674157823683": {
            "type": "constant",
            "sample": 0.25,
        },
        "8163910343030177564": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8385404402228892812": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1507007387244201337": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7863579983477491941": {
            "type": "constant",
            "sample": 0.25,
        },
        "-9011401800654360714": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2630370166450727595": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4982735835213021815": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7456238637272704885": {
            "type": "constant",
            "sample": 0.25,
        },
        "-211116419248845484": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1358938236425714257": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2448233669816909394": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "251948621032188738_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "251948621032188738_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8897486873289680184_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8897486873289680184_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5219430737301740542_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5219430737301740542_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2135498729515057512_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2135498729515057512_q": {
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
        "B2/acquisition_mixer_d3d": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_642": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_559": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_c55": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_d6a": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_b19": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_ae2": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_c25": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

