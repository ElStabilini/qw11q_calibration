
# Single QUA script generated at 2025-02-16 09:13:35.543737
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
        play("-6478061349538789568", "B1/drive")
        wait(11, "B1/flux")
        play("-2113038178258897208", "B1/flux")
        wait(46, "B1/drive")
        play("-5716970720315227699", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-7671505665175289921", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        r1 = declare_stream()
        save(v4, r1)
        play("-7936378860622704143", "B2/drive")
        wait(11, "B2/flux")
        play("-2113038178258897208", "B2/flux")
        wait(46, "B2/drive")
        play("-7175288231399142274", "B2/drive")
        wait(66, "B2/acquisition")
        measure("2550459627823321246", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        r2 = declare_stream()
        save(v7, r2)
        play("766728168029010066", "B3/drive")
        wait(11, "B3/flux")
        play("-2113038178258897208", "B3/flux")
        wait(46, "B3/drive")
        play("1527818797252571935", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-5717604780079032417", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        r3 = declare_stream()
        save(v10, r3)
        play("-4520699063366441565", "B4/drive")
        wait(11, "B4/flux")
        play("-2113038178258897208", "B4/flux")
        wait(46, "B4/drive")
        play("-3759608434142879696", "B4/drive")
        wait(66, "B4/acquisition")
        measure("6741631589795925737", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25536, "B4/flux")
        wait(25536, "B3/flux")
        wait(25536, "B1/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B4/drive")
        wait(25001, "B2/acquisition")
        wait(25001, "B3/acquisition")
        wait(25501, "B3/drive")
        play("-6478061349538789568", "B1/drive")
        wait(11, "B1/flux")
        play("-687000267474756513", "B1/flux")
        wait(46, "B1/drive")
        play("-5716970720315227699", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-7671505665175289921", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9999905092516408)-(v3*-0.004356765617302177))>0.0008494611165541193)))
        save(v4, r1)
        play("-7936378860622704143", "B2/drive")
        wait(11, "B2/flux")
        play("-687000267474756513", "B2/flux")
        wait(46, "B2/drive")
        play("-7175288231399142274", "B2/drive")
        wait(66, "B2/acquisition")
        measure("2550459627823321246", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7824341306964239)-(v6*0.6227333547525229))>0.002499868004267324)))
        save(v7, r2)
        play("766728168029010066", "B3/drive")
        wait(11, "B3/flux")
        play("-687000267474756513", "B3/flux")
        wait(46, "B3/drive")
        play("1527818797252571935", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-5717604780079032417", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8869580095383807)-(v9*-0.4618500723348583))>0.0026927888724794886)))
        save(v10, r3)
        play("-4520699063366441565", "B4/drive")
        wait(11, "B4/flux")
        play("-687000267474756513", "B4/flux")
        wait(46, "B4/drive")
        play("-3759608434142879696", "B4/drive")
        wait(66, "B4/acquisition")
        measure("6741631589795925737", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5498713458254006)-(v12*0.8352493657825564))>-0.0005571645574693968)))
        save(v13, r4)
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25536, "B4/flux")
        wait(25536, "B3/flux")
        wait(25536, "B1/flux")
        wait(25001, "B4/acquisition")
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B4/drive")
        wait(25001, "B2/acquisition")
        wait(25001, "B3/acquisition")
        wait(25501, "B3/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-7671505665175289921_B1|acquisition_shots")
        r2.buffer(2).average().save("2550459627823321246_B2|acquisition_shots")
        r3.buffer(2).average().save("-5717604780079032417_B3|acquisition_shots")
        r4.buffer(2).average().save("6741631589795925737_B4|acquisition_shots")


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
                "7": {
                    "offset": 0.0,
                    "filter": {},
                },
                "8": {
                    "offset": 0.0,
                    "filter": {},
                },
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
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
                "7": {},
                "1": {},
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
                "7": {
                    "offset": 0.0,
                    "filter": {},
                },
                "8": {
                    "offset": 0.0,
                    "filter": {},
                },
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
                "7": {},
                "1": {},
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
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "1": {
                    "LO_frequency": 7370000000.0,
                    "gain": -10.0,
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
                "4": {
                    "LO_frequency": 6700000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "1": {
                    "LO_frequency": 5800000000.0,
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-7936378860622704143": "-7936378860622704143",
                "-7175288231399142274": "-7175288231399142274",
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
                "6741631589795925737": "6741631589795925737_B4/acquisition",
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
                "-6478061349538789568": "-6478061349538789568",
                "-5716970720315227699": "-5716970720315227699",
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
                "-7671505665175289921": "-7671505665175289921_B1/acquisition",
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
                "-4520699063366441565": "-4520699063366441565",
                "-3759608434142879696": "-3759608434142879696",
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
                "2550459627823321246": "2550459627823321246_B2/acquisition",
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
                "-5717604780079032417": "-5717604780079032417_B3/acquisition",
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
                "766728168029010066": "766728168029010066",
                "1527818797252571935": "1527818797252571935",
            },
        },
    },
    "pulses": {
        "-6478061349538789568": {
            "length": 40,
            "waveforms": {
                "I": "-6478061349538789568_i",
                "Q": "-6478061349538789568_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4099488898688587186": {
            "length": 16,
            "waveforms": {
                "single": "4099488898688587186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7671505665175289921_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-3275477200491072273_i",
                "Q": "-3275477200491072273_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-7936378860622704143": {
            "length": 40,
            "waveforms": {
                "I": "-7936378860622704143_i",
                "Q": "-7936378860622704143_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2550459627823321246_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8293068983248237452_i",
                "Q": "-8293068983248237452_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "766728168029010066": {
            "length": 40,
            "waveforms": {
                "I": "766728168029010066_i",
                "Q": "766728168029010066_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5717604780079032417_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1026395656959657328_i",
                "Q": "1026395656959657328_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-4520699063366441565": {
            "length": 40,
            "waveforms": {
                "I": "-4520699063366441565_i",
                "Q": "-4520699063366441565_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6741631589795925737_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-9171981231813389832_i",
                "Q": "-9171981231813389832_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-6141725885793972651": {
            "length": 16,
            "waveforms": {
                "single": "-6141725885793972651",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2730455906908680204": {
            "length": 16,
            "waveforms": {
                "single": "2730455906908680204",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2951949966107395452": {
            "length": 16,
            "waveforms": {
                "single": "2951949966107395452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3722472138592090540": {
            "length": 16,
            "waveforms": {
                "single": "-3722472138592090540",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9178092734956224175": {
            "length": 16,
            "waveforms": {
                "single": "9178092734956224175",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1510737678434673806": {
            "length": 16,
            "waveforms": {
                "single": "1510737678434673806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8063824602572224955": {
            "length": 16,
            "waveforms": {
                "single": "-8063824602572224955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3708497366437840669": {
            "length": 16,
            "waveforms": {
                "single": "3708497366437840669",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3929991425636555917": {
            "length": 16,
            "waveforms": {
                "single": "3929991425636555917",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4263859680175169681": {
            "length": 16,
            "waveforms": {
                "single": "-4263859680175169681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9163201242663320263": {
            "length": 16,
            "waveforms": {
                "single": "9163201242663320263",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6464457375156370946": {
            "length": 16,
            "waveforms": {
                "single": "-6464457375156370946",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7085783143043064490": {
            "length": 16,
            "waveforms": {
                "single": "-7085783143043064490",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1786398649659588365": {
            "length": 16,
            "waveforms": {
                "single": "1786398649659588365",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3388603884053476776": {
            "length": 16,
            "waveforms": {
                "single": "3388603884053476776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1064045801966640323": {
            "length": 20,
            "waveforms": {
                "single": "1064045801966640323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5586363572056643639": {
            "length": 20,
            "waveforms": {
                "single": "5586363572056643639",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6479348867449274858": {
            "length": 20,
            "waveforms": {
                "single": "-6479348867449274858",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6791190308237746125": {
            "length": 20,
            "waveforms": {
                "single": "6791190308237746125",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9108908939627571292": {
            "length": 24,
            "waveforms": {
                "single": "-9108908939627571292",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5429410996622976768": {
            "length": 24,
            "waveforms": {
                "single": "-5429410996622976768",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5207916937424261520": {
            "length": 24,
            "waveforms": {
                "single": "-5207916937424261520",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1400745031181637869": {
            "length": 24,
            "waveforms": {
                "single": "-1400745031181637869",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1677939434597640083": {
            "length": 28,
            "waveforms": {
                "single": "-1677939434597640083",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "797014656821528994": {
            "length": 28,
            "waveforms": {
                "single": "797014656821528994",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2223052567605669689": {
            "length": 28,
            "waveforms": {
                "single": "2223052567605669689",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-129313101156624531": {
            "length": 28,
            "waveforms": {
                "single": "-129313101156624531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7130015654202513824": {
            "length": 32,
            "waveforms": {
                "single": "-7130015654202513824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4977582701788314493": {
            "length": 32,
            "waveforms": {
                "single": "-4977582701788314493",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8449478221050175451": {
            "length": 32,
            "waveforms": {
                "single": "8449478221050175451",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "255627115238449853": {
            "length": 32,
            "waveforms": {
                "single": "255627115238449853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "477121174437165101": {
            "length": 36,
            "waveforms": {
                "single": "477121174437165101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1132291043802291687": {
            "length": 36,
            "waveforms": {
                "single": "-1132291043802291687",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2674880862440331964": {
            "length": 36,
            "waveforms": {
                "single": "2674880862440331964",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2053555094553638420": {
            "length": 36,
            "waveforms": {
                "single": "2053555094553638420",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7908090679467096310": {
            "length": 40,
            "waveforms": {
                "single": "7908090679467096310",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-576004977624658014": {
            "length": 40,
            "waveforms": {
                "single": "-576004977624658014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8340893706239288443": {
            "length": 40,
            "waveforms": {
                "single": "-8340893706239288443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8119399647040573195": {
            "length": 40,
            "waveforms": {
                "single": "-8119399647040573195",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1290673493771844031": {
            "length": 44,
            "waveforms": {
                "single": "1290673493771844031",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-191064761229583630": {
            "length": 44,
            "waveforms": {
                "single": "-191064761229583630",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "30429297969131618": {
            "length": 44,
            "waveforms": {
                "single": "30429297969131618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-688430142010641986": {
            "length": 44,
            "waveforms": {
                "single": "-688430142010641986",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3931421300172441390": {
            "length": 48,
            "waveforms": {
                "single": "3931421300172441390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3317990214188938420": {
            "length": 48,
            "waveforms": {
                "single": "-3317990214188938420",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7461398802999062827": {
            "length": 48,
            "waveforms": {
                "single": "7461398802999062827",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6463027500620485473": {
            "length": 48,
            "waveforms": {
                "single": "-6463027500620485473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7084353268507179017": {
            "length": 52,
            "waveforms": {
                "single": "-7084353268507179017",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4611667753455710251": {
            "length": 52,
            "waveforms": {
                "single": "4611667753455710251",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1686801444389219340": {
            "length": 52,
            "waveforms": {
                "single": "1686801444389219340",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-236601847175979711": {
            "length": 52,
            "waveforms": {
                "single": "-236601847175979711",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1189436063608160984": {
            "length": 56,
            "waveforms": {
                "single": "1189436063608160984",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9051778720874398853": {
            "length": 56,
            "waveforms": {
                "single": "-9051778720874398853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3487487687240969689": {
            "length": 56,
            "waveforms": {
                "single": "-3487487687240969689",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7194367657853951498": {
            "length": 56,
            "waveforms": {
                "single": "7194367657853951498",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6632524973672516742": {
            "length": 60,
            "waveforms": {
                "single": "-6632524973672516742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1620809215844467644": {
            "length": 60,
            "waveforms": {
                "single": "-1620809215844467644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3102547470845895305": {
            "length": 60,
            "waveforms": {
                "single": "-3102547470845895305",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7407084757869577312": {
            "length": 60,
            "waveforms": {
                "single": "-7407084757869577312",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "798444531357414467": {
            "length": 64,
            "waveforms": {
                "single": "798444531357414467",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1019938590556129715": {
            "length": 64,
            "waveforms": {
                "single": "1019938590556129715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1831115540820881967": {
            "length": 64,
            "waveforms": {
                "single": "-1831115540820881967",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4549916093382751152": {
            "length": 64,
            "waveforms": {
                "single": "4549916093382751152",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9072233863472754468": {
            "length": 68,
            "waveforms": {
                "single": "9072233863472754468",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8450908095586060924": {
            "length": 68,
            "waveforms": {
                "single": "8450908095586060924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5599853964209049242": {
            "length": 68,
            "waveforms": {
                "single": "5599853964209049242",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5821348023407764490": {
            "length": 68,
            "waveforms": {
                "single": "5821348023407764490",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1846007033113785879": {
            "length": 72,
            "waveforms": {
                "single": "-1846007033113785879",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2676310736976217437": {
            "length": 72,
            "waveforms": {
                "single": "2676310736976217437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4046604728094987144": {
            "length": 72,
            "waveforms": {
                "single": "-4046604728094987144",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6206288239802838874": {
            "length": 72,
            "waveforms": {
                "single": "6206288239802838874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6427782299001554122": {
            "length": 76,
            "waveforms": {
                "single": "6427782299001554122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8339463831703402970": {
            "length": 76,
            "waveforms": {
                "single": "-8339463831703402970",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8117969772504687722": {
            "length": 76,
            "waveforms": {
                "single": "-8117969772504687722",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8004216219118027441": {
            "length": 76,
            "waveforms": {
                "single": "8004216219118027441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4587992269678066285": {
            "length": 80,
            "waveforms": {
                "single": "-4587992269678066285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2113038178258897208": {
            "length": 80,
            "waveforms": {
                "single": "-2113038178258897208",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-687000267474756513": {
            "length": 80,
            "waveforms": {
                "single": "-687000267474756513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5716970720315227699": {
            "length": 40,
            "waveforms": {
                "I": "-5716970720315227699_i",
                "Q": "-5716970720315227699_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7175288231399142274": {
            "length": 40,
            "waveforms": {
                "I": "-7175288231399142274_i",
                "Q": "-7175288231399142274_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1527818797252571935": {
            "length": 40,
            "waveforms": {
                "I": "1527818797252571935_i",
                "Q": "1527818797252571935_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3759608434142879696": {
            "length": 40,
            "waveforms": {
                "I": "-3759608434142879696_i",
                "Q": "-3759608434142879696_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6478061349538789568_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-6478061349538789568_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "4099488898688587186": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-3275477200491072273_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-3275477200491072273_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7936378860622704143_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-7936378860622704143_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-8293068983248237452_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-8293068983248237452_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "766728168029010066_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "766728168029010066_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "1026395656959657328_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "1026395656959657328_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4520699063366441565_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-4520699063366441565_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-9171981231813389832_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-9171981231813389832_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6141725885793972651": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "2730455906908680204": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "2951949966107395452": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-3722472138592090540": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "9178092734956224175": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "1510737678434673806": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-8063824602572224955": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "3708497366437840669": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "3929991425636555917": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-4263859680175169681": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "9163201242663320263": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-6464457375156370946": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7085783143043064490": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1786398649659588365": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "3388603884053476776": {
            "sample": 0.25,
            "type": "constant",
        },
        "1064045801966640323": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5586363572056643639": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6479348867449274858": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "6791190308237746125": {
            "sample": 0.25,
            "type": "constant",
        },
        "-9108908939627571292": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5429410996622976768": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5207916937424261520": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-1400745031181637869": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1677939434597640083": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "797014656821528994": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2223052567605669689": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-129313101156624531": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7130015654202513824": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4977582701788314493": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8449478221050175451": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "255627115238449853": {
            "sample": 0.25,
            "type": "constant",
        },
        "477121174437165101": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1132291043802291687": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2674880862440331964": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "2053555094553638420": {
            "sample": 0.25,
            "type": "constant",
        },
        "7908090679467096310": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-576004977624658014": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8340893706239288443": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-8119399647040573195": {
            "sample": 0.25,
            "type": "constant",
        },
        "1290673493771844031": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-191064761229583630": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "30429297969131618": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-688430142010641986": {
            "sample": 0.25,
            "type": "constant",
        },
        "3931421300172441390": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3317990214188938420": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7461398802999062827": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-6463027500620485473": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7084353268507179017": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4611667753455710251": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1686801444389219340": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-236601847175979711": {
            "sample": 0.25,
            "type": "constant",
        },
        "1189436063608160984": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9051778720874398853": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3487487687240969689": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "7194367657853951498": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6632524973672516742": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1620809215844467644": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3102547470845895305": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-7407084757869577312": {
            "sample": 0.25,
            "type": "constant",
        },
        "798444531357414467": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1019938590556129715": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1831115540820881967": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "4549916093382751152": {
            "sample": 0.25,
            "type": "constant",
        },
        "9072233863472754468": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8450908095586060924": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5599853964209049242": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "5821348023407764490": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1846007033113785879": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2676310736976217437": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4046604728094987144": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "6206288239802838874": {
            "sample": 0.25,
            "type": "constant",
        },
        "6427782299001554122": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8339463831703402970": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8117969772504687722": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "8004216219118027441": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4587992269678066285": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2113038178258897208": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-687000267474756513": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-5716970720315227699_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-5716970720315227699_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-7175288231399142274_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-7175288231399142274_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "1527818797252571935_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "1527818797252571935_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "-3759608434142879696_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-3759608434142879696_q": {
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
                "7": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "1": {
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
                "7": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "1": {
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-2113038178258897208": "-2113038178258897208",
                "-687000267474756513": "-687000267474756513",
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
                "-7936378860622704143": "-7936378860622704143",
                "-7175288231399142274": "-7175288231399142274",
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
                "mixer": "B2/drive_mixer_a11",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "6741631589795925737": "6741631589795925737_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_67f",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "-6478061349538789568": "-6478061349538789568",
                "-5716970720315227699": "-5716970720315227699",
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
                "mixer": "B1/drive_mixer_6d3",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "-7671505665175289921": "-7671505665175289921_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_24c",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "-4520699063366441565": "-4520699063366441565",
                "-3759608434142879696": "-3759608434142879696",
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
                "mixer": "B4/drive_mixer_07d",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "2550459627823321246": "2550459627823321246_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_c07",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-5717604780079032417": "-5717604780079032417_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_178",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "766728168029010066": "766728168029010066",
                "1527818797252571935": "1527818797252571935",
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
                "mixer": "B3/drive_mixer_fcc",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
        },
    },
    "pulses": {
        "-6478061349538789568": {
            "length": 40,
            "waveforms": {
                "I": "-6478061349538789568_i",
                "Q": "-6478061349538789568_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4099488898688587186": {
            "length": 16,
            "waveforms": {
                "single": "4099488898688587186",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7671505665175289921_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-3275477200491072273_i",
                "Q": "-3275477200491072273_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-7936378860622704143": {
            "length": 40,
            "waveforms": {
                "I": "-7936378860622704143_i",
                "Q": "-7936378860622704143_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2550459627823321246_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8293068983248237452_i",
                "Q": "-8293068983248237452_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "766728168029010066": {
            "length": 40,
            "waveforms": {
                "I": "766728168029010066_i",
                "Q": "766728168029010066_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5717604780079032417_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1026395656959657328_i",
                "Q": "1026395656959657328_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4520699063366441565": {
            "length": 40,
            "waveforms": {
                "I": "-4520699063366441565_i",
                "Q": "-4520699063366441565_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6741631589795925737_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-9171981231813389832_i",
                "Q": "-9171981231813389832_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-6141725885793972651": {
            "length": 16,
            "waveforms": {
                "single": "-6141725885793972651",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2730455906908680204": {
            "length": 16,
            "waveforms": {
                "single": "2730455906908680204",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2951949966107395452": {
            "length": 16,
            "waveforms": {
                "single": "2951949966107395452",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3722472138592090540": {
            "length": 16,
            "waveforms": {
                "single": "-3722472138592090540",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9178092734956224175": {
            "length": 16,
            "waveforms": {
                "single": "9178092734956224175",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1510737678434673806": {
            "length": 16,
            "waveforms": {
                "single": "1510737678434673806",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8063824602572224955": {
            "length": 16,
            "waveforms": {
                "single": "-8063824602572224955",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3708497366437840669": {
            "length": 16,
            "waveforms": {
                "single": "3708497366437840669",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3929991425636555917": {
            "length": 16,
            "waveforms": {
                "single": "3929991425636555917",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4263859680175169681": {
            "length": 16,
            "waveforms": {
                "single": "-4263859680175169681",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9163201242663320263": {
            "length": 16,
            "waveforms": {
                "single": "9163201242663320263",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6464457375156370946": {
            "length": 16,
            "waveforms": {
                "single": "-6464457375156370946",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7085783143043064490": {
            "length": 16,
            "waveforms": {
                "single": "-7085783143043064490",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1786398649659588365": {
            "length": 16,
            "waveforms": {
                "single": "1786398649659588365",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3388603884053476776": {
            "length": 16,
            "waveforms": {
                "single": "3388603884053476776",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1064045801966640323": {
            "length": 20,
            "waveforms": {
                "single": "1064045801966640323",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5586363572056643639": {
            "length": 20,
            "waveforms": {
                "single": "5586363572056643639",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6479348867449274858": {
            "length": 20,
            "waveforms": {
                "single": "-6479348867449274858",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6791190308237746125": {
            "length": 20,
            "waveforms": {
                "single": "6791190308237746125",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9108908939627571292": {
            "length": 24,
            "waveforms": {
                "single": "-9108908939627571292",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5429410996622976768": {
            "length": 24,
            "waveforms": {
                "single": "-5429410996622976768",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5207916937424261520": {
            "length": 24,
            "waveforms": {
                "single": "-5207916937424261520",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1400745031181637869": {
            "length": 24,
            "waveforms": {
                "single": "-1400745031181637869",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1677939434597640083": {
            "length": 28,
            "waveforms": {
                "single": "-1677939434597640083",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "797014656821528994": {
            "length": 28,
            "waveforms": {
                "single": "797014656821528994",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2223052567605669689": {
            "length": 28,
            "waveforms": {
                "single": "2223052567605669689",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-129313101156624531": {
            "length": 28,
            "waveforms": {
                "single": "-129313101156624531",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7130015654202513824": {
            "length": 32,
            "waveforms": {
                "single": "-7130015654202513824",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4977582701788314493": {
            "length": 32,
            "waveforms": {
                "single": "-4977582701788314493",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8449478221050175451": {
            "length": 32,
            "waveforms": {
                "single": "8449478221050175451",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "255627115238449853": {
            "length": 32,
            "waveforms": {
                "single": "255627115238449853",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "477121174437165101": {
            "length": 36,
            "waveforms": {
                "single": "477121174437165101",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1132291043802291687": {
            "length": 36,
            "waveforms": {
                "single": "-1132291043802291687",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2674880862440331964": {
            "length": 36,
            "waveforms": {
                "single": "2674880862440331964",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2053555094553638420": {
            "length": 36,
            "waveforms": {
                "single": "2053555094553638420",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7908090679467096310": {
            "length": 40,
            "waveforms": {
                "single": "7908090679467096310",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-576004977624658014": {
            "length": 40,
            "waveforms": {
                "single": "-576004977624658014",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8340893706239288443": {
            "length": 40,
            "waveforms": {
                "single": "-8340893706239288443",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8119399647040573195": {
            "length": 40,
            "waveforms": {
                "single": "-8119399647040573195",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1290673493771844031": {
            "length": 44,
            "waveforms": {
                "single": "1290673493771844031",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-191064761229583630": {
            "length": 44,
            "waveforms": {
                "single": "-191064761229583630",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "30429297969131618": {
            "length": 44,
            "waveforms": {
                "single": "30429297969131618",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-688430142010641986": {
            "length": 44,
            "waveforms": {
                "single": "-688430142010641986",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3931421300172441390": {
            "length": 48,
            "waveforms": {
                "single": "3931421300172441390",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3317990214188938420": {
            "length": 48,
            "waveforms": {
                "single": "-3317990214188938420",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7461398802999062827": {
            "length": 48,
            "waveforms": {
                "single": "7461398802999062827",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6463027500620485473": {
            "length": 48,
            "waveforms": {
                "single": "-6463027500620485473",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7084353268507179017": {
            "length": 52,
            "waveforms": {
                "single": "-7084353268507179017",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4611667753455710251": {
            "length": 52,
            "waveforms": {
                "single": "4611667753455710251",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1686801444389219340": {
            "length": 52,
            "waveforms": {
                "single": "1686801444389219340",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-236601847175979711": {
            "length": 52,
            "waveforms": {
                "single": "-236601847175979711",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1189436063608160984": {
            "length": 56,
            "waveforms": {
                "single": "1189436063608160984",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9051778720874398853": {
            "length": 56,
            "waveforms": {
                "single": "-9051778720874398853",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3487487687240969689": {
            "length": 56,
            "waveforms": {
                "single": "-3487487687240969689",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7194367657853951498": {
            "length": 56,
            "waveforms": {
                "single": "7194367657853951498",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6632524973672516742": {
            "length": 60,
            "waveforms": {
                "single": "-6632524973672516742",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1620809215844467644": {
            "length": 60,
            "waveforms": {
                "single": "-1620809215844467644",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3102547470845895305": {
            "length": 60,
            "waveforms": {
                "single": "-3102547470845895305",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7407084757869577312": {
            "length": 60,
            "waveforms": {
                "single": "-7407084757869577312",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "798444531357414467": {
            "length": 64,
            "waveforms": {
                "single": "798444531357414467",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1019938590556129715": {
            "length": 64,
            "waveforms": {
                "single": "1019938590556129715",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1831115540820881967": {
            "length": 64,
            "waveforms": {
                "single": "-1831115540820881967",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4549916093382751152": {
            "length": 64,
            "waveforms": {
                "single": "4549916093382751152",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9072233863472754468": {
            "length": 68,
            "waveforms": {
                "single": "9072233863472754468",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8450908095586060924": {
            "length": 68,
            "waveforms": {
                "single": "8450908095586060924",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5599853964209049242": {
            "length": 68,
            "waveforms": {
                "single": "5599853964209049242",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5821348023407764490": {
            "length": 68,
            "waveforms": {
                "single": "5821348023407764490",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1846007033113785879": {
            "length": 72,
            "waveforms": {
                "single": "-1846007033113785879",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2676310736976217437": {
            "length": 72,
            "waveforms": {
                "single": "2676310736976217437",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4046604728094987144": {
            "length": 72,
            "waveforms": {
                "single": "-4046604728094987144",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6206288239802838874": {
            "length": 72,
            "waveforms": {
                "single": "6206288239802838874",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6427782299001554122": {
            "length": 76,
            "waveforms": {
                "single": "6427782299001554122",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8339463831703402970": {
            "length": 76,
            "waveforms": {
                "single": "-8339463831703402970",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8117969772504687722": {
            "length": 76,
            "waveforms": {
                "single": "-8117969772504687722",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8004216219118027441": {
            "length": 76,
            "waveforms": {
                "single": "8004216219118027441",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4587992269678066285": {
            "length": 80,
            "waveforms": {
                "single": "-4587992269678066285",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2113038178258897208": {
            "length": 80,
            "waveforms": {
                "single": "-2113038178258897208",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-687000267474756513": {
            "length": 80,
            "waveforms": {
                "single": "-687000267474756513",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5716970720315227699": {
            "length": 40,
            "waveforms": {
                "I": "-5716970720315227699_i",
                "Q": "-5716970720315227699_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7175288231399142274": {
            "length": 40,
            "waveforms": {
                "I": "-7175288231399142274_i",
                "Q": "-7175288231399142274_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1527818797252571935": {
            "length": 40,
            "waveforms": {
                "I": "1527818797252571935_i",
                "Q": "1527818797252571935_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3759608434142879696": {
            "length": 40,
            "waveforms": {
                "I": "-3759608434142879696_i",
                "Q": "-3759608434142879696_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-6478061349538789568_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6478061349538789568_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4099488898688587186": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3275477200491072273_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-3275477200491072273_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-7936378860622704143_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7936378860622704143_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8293068983248237452_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-8293068983248237452_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "766728168029010066_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "766728168029010066_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1026395656959657328_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "1026395656959657328_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4520699063366441565_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4520699063366441565_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9171981231813389832_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-9171981231813389832_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-6141725885793972651": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2730455906908680204": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2951949966107395452": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3722472138592090540": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9178092734956224175": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1510737678434673806": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8063824602572224955": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3708497366437840669": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3929991425636555917": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4263859680175169681": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9163201242663320263": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6464457375156370946": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7085783143043064490": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1786398649659588365": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3388603884053476776": {
            "type": "constant",
            "sample": 0.25,
        },
        "1064045801966640323": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5586363572056643639": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6479348867449274858": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6791190308237746125": {
            "type": "constant",
            "sample": 0.25,
        },
        "-9108908939627571292": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5429410996622976768": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5207916937424261520": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1400745031181637869": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1677939434597640083": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "797014656821528994": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2223052567605669689": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-129313101156624531": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7130015654202513824": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4977582701788314493": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8449478221050175451": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "255627115238449853": {
            "type": "constant",
            "sample": 0.25,
        },
        "477121174437165101": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1132291043802291687": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2674880862440331964": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2053555094553638420": {
            "type": "constant",
            "sample": 0.25,
        },
        "7908090679467096310": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-576004977624658014": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8340893706239288443": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8119399647040573195": {
            "type": "constant",
            "sample": 0.25,
        },
        "1290673493771844031": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-191064761229583630": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "30429297969131618": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-688430142010641986": {
            "type": "constant",
            "sample": 0.25,
        },
        "3931421300172441390": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3317990214188938420": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7461398802999062827": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6463027500620485473": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7084353268507179017": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4611667753455710251": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1686801444389219340": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-236601847175979711": {
            "type": "constant",
            "sample": 0.25,
        },
        "1189436063608160984": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9051778720874398853": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3487487687240969689": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7194367657853951498": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6632524973672516742": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1620809215844467644": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3102547470845895305": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7407084757869577312": {
            "type": "constant",
            "sample": 0.25,
        },
        "798444531357414467": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1019938590556129715": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1831115540820881967": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4549916093382751152": {
            "type": "constant",
            "sample": 0.25,
        },
        "9072233863472754468": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8450908095586060924": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5599853964209049242": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5821348023407764490": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1846007033113785879": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2676310736976217437": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4046604728094987144": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6206288239802838874": {
            "type": "constant",
            "sample": 0.25,
        },
        "6427782299001554122": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8339463831703402970": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8117969772504687722": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8004216219118027441": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4587992269678066285": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2113038178258897208": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-687000267474756513": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5716970720315227699_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5716970720315227699_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7175288231399142274_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7175288231399142274_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1527818797252571935_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1527818797252571935_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3759608434142879696_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3759608434142879696_q": {
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
        "B2/drive_mixer_a11": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_67f": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_6d3": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_24c": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_07d": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_c07": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_178": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_fcc": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

