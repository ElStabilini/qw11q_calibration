
# Single QUA script generated at 2025-02-16 10:49:26.250654
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
        play("7094696613202078498", "B1/drive")
        wait(11, "B1/flux")
        play("6098878911102946384", "B1/flux")
        wait(46, "B1/drive")
        play("7855787242425640367", "B1/drive")
        wait(66, "B1/acquisition")
        measure("1078235932028120661", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("-284868177196146850", "B2/drive")
        wait(11, "B2/flux")
        play("6098878911102946384", "B2/flux")
        wait(46, "B2/drive")
        play("476222452027415019", "B2/drive")
        wait(66, "B2/acquisition")
        measure("4969399967854171079", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("-4985059144666518607", "B3/drive")
        wait(11, "B3/flux")
        play("6098878911102946384", "B3/flux")
        wait(46, "B3/drive")
        play("-4223968515442956738", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-7827409459628951200", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("-8092607650656619608", "B4/drive")
        wait(11, "B4/flux")
        play("6098878911102946384", "B4/flux")
        wait(46, "B4/drive")
        play("4069197763641637052", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6079164336930150448", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B4/flux")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25501, "B2/drive")
        wait(25001, "B4/acquisition")
        wait(25001, "B3/acquisition")
        wait(25001, "B1/acquisition")
        wait(25501, "B1/drive")
        wait(25536, "B1/flux")
        play("7094696613202078498", "B1/drive")
        wait(11, "B1/flux")
        play("6320372970301661632", "B1/flux")
        wait(46, "B1/drive")
        play("7855787242425640367", "B1/drive")
        wait(66, "B1/acquisition")
        measure("1078235932028120661", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("-284868177196146850", "B2/drive")
        wait(11, "B2/flux")
        play("6320372970301661632", "B2/flux")
        wait(46, "B2/drive")
        play("476222452027415019", "B2/drive")
        wait(66, "B2/acquisition")
        measure("4969399967854171079", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("-4985059144666518607", "B3/drive")
        wait(11, "B3/flux")
        play("6320372970301661632", "B3/flux")
        wait(46, "B3/drive")
        play("-4223968515442956738", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-7827409459628951200", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("-8092607650656619608", "B4/drive")
        wait(11, "B4/flux")
        play("6320372970301661632", "B4/flux")
        wait(46, "B4/drive")
        play("4069197763641637052", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6079164336930150448", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B4/flux")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25501, "B2/drive")
        wait(25001, "B4/acquisition")
        wait(25001, "B3/acquisition")
        wait(25001, "B1/acquisition")
        wait(25501, "B1/drive")
        wait(25536, "B1/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("1078235932028120661_B1|acquisition_shots")
        r2.buffer(2).average().save("4969399967854171079_B2|acquisition_shots")
        r3.buffer(2).average().save("-7827409459628951200_B3|acquisition_shots")
        r4.buffer(2).average().save("-6079164336930150448_B4|acquisition_shots")


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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "4969399967854171079": "4969399967854171079_B2/acquisition",
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
                "-4985059144666518607": "-4985059144666518607",
                "-4223968515442956738": "-4223968515442956738",
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
                "-8092607650656619608": "-8092607650656619608",
                "4069197763641637052": "4069197763641637052",
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
                "-284868177196146850": "-284868177196146850",
                "476222452027415019": "476222452027415019",
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
                "-6079164336930150448": "-6079164336930150448_B4/acquisition",
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
                "-7827409459628951200": "-7827409459628951200_B3/acquisition",
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
                "1078235932028120661": "1078235932028120661_B1/acquisition",
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
                "7094696613202078498": "7094696613202078498",
                "7855787242425640367": "7855787242425640367",
            },
        },
    },
    "pulses": {
        "7094696613202078498": {
            "length": 40,
            "waveforms": {
                "I": "7094696613202078498_i",
                "Q": "7094696613202078498_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3934457506082242534": {
            "length": 16,
            "waveforms": {
                "single": "-3934457506082242534",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1078235932028120661_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3731896037285345872_i",
                "Q": "3731896037285345872_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-284868177196146850": {
            "length": 40,
            "waveforms": {
                "I": "-284868177196146850_i",
                "Q": "-284868177196146850_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4969399967854171079_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4873841829533098564_i",
                "Q": "4873841829533098564_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-4985059144666518607": {
            "length": 40,
            "waveforms": {
                "I": "-4985059144666518607_i",
                "Q": "-4985059144666518607_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7827409459628951200_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7395328971184281178_i",
                "Q": "-7395328971184281178_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-8092607650656619608": {
            "length": 40,
            "waveforms": {
                "I": "-8092607650656619608_i",
                "Q": "-8092607650656619608_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6079164336930150448_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-3545319169232144850_i",
                "Q": "-3545319169232144850_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "6918743688795237942": {
            "length": 16,
            "waveforms": {
                "single": "6918743688795237942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6135055201063443799": {
            "length": 16,
            "waveforms": {
                "single": "-6135055201063443799",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9116503376798404805": {
            "length": 16,
            "waveforms": {
                "single": "9116503376798404805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3496511998947688675": {
            "length": 16,
            "waveforms": {
                "single": "3496511998947688675",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4586428867622428247": {
            "length": 16,
            "waveforms": {
                "single": "-4586428867622428247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5694271686950855538": {
            "length": 16,
            "waveforms": {
                "single": "5694271686950855538",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1056451364795806810": {
            "length": 16,
            "waveforms": {
                "single": "-1056451364795806810",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8723806421317357179": {
            "length": 16,
            "waveforms": {
                "single": "-8723806421317357179",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2844540637407502962": {
            "length": 16,
            "waveforms": {
                "single": "2844540637407502962",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1362802382406075301": {
            "length": 16,
            "waveforms": {
                "single": "1362802382406075301",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5100008822530049621": {
            "length": 16,
            "waveforms": {
                "single": "-5100008822530049621",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7452374491292343841": {
            "length": 16,
            "waveforms": {
                "single": "-7452374491292343841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3229480853802577346": {
            "length": 16,
            "waveforms": {
                "single": "3229480853802577346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8793771887436006510": {
            "length": 16,
            "waveforms": {
                "single": "8793771887436006510",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9015265946634721758": {
            "length": 16,
            "waveforms": {
                "single": "9015265946634721758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-21404986262412632": {
            "length": 20,
            "waveforms": {
                "single": "-21404986262412632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "200089072936302616": {
            "length": 20,
            "waveforms": {
                "single": "200089072936302616",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7564799655678327813": {
            "length": 20,
            "waveforms": {
                "single": "-7564799655678327813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2397848760939469479": {
            "length": 20,
            "waveforms": {
                "single": "2397848760939469479",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2619342820138184727": {
            "length": 24,
            "waveforms": {
                "single": "2619342820138184727",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "585029289331377000": {
            "length": 24,
            "waveforms": {
                "single": "585029289331377000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "806523348530092248": {
            "length": 24,
            "waveforms": {
                "single": "806523348530092248",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2782788977334543863": {
            "length": 24,
            "waveforms": {
                "single": "2782788977334543863",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3004283036533259111": {
            "length": 28,
            "waveforms": {
                "single": "3004283036533259111",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1856461219356390338": {
            "length": 28,
            "waveforms": {
                "single": "1856461219356390338",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8237492853560023457": {
            "length": 28,
            "waveforms": {
                "single": "8237492853560023457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8994824209128748534": {
            "length": 28,
            "waveforms": {
                "single": "-8994824209128748534",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8011491532146361296": {
            "length": 32,
            "waveforms": {
                "single": "-8011491532146361296",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8082886872800896100": {
            "length": 32,
            "waveforms": {
                "single": "8082886872800896100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8937819290124514821": {
            "length": 32,
            "waveforms": {
                "single": "-8937819290124514821",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5592237784944479185": {
            "length": 32,
            "waveforms": {
                "single": "-5592237784944479185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6740059602121347958": {
            "length": 36,
            "waveforms": {
                "single": "-6740059602121347958",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-359027967917714839": {
            "length": 36,
            "waveforms": {
                "single": "-359027967917714839",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2711393636680009059": {
            "length": 36,
            "waveforms": {
                "single": "-2711393636680009059",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4320805854919465847": {
            "length": 36,
            "waveforms": {
                "single": "-4320805854919465847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-513633948676842196": {
            "length": 40,
            "waveforms": {
                "single": "-513633948676842196",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6133625326527558326": {
            "length": 40,
            "waveforms": {
                "single": "-6133625326527558326",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4719575868349922150": {
            "length": 40,
            "waveforms": {
                "single": "4719575868349922150",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1112026409264155050": {
            "length": 40,
            "waveforms": {
                "single": "-1112026409264155050",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-128693732281767812": {
            "length": 44,
            "waveforms": {
                "single": "-128693732281767812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7138829615551804261": {
            "length": 44,
            "waveforms": {
                "single": "7138829615551804261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1055021490259921337": {
            "length": 44,
            "waveforms": {
                "single": "-1055021490259921337",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8722376546781471706": {
            "length": 44,
            "waveforms": {
                "single": "-8722376546781471706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1142738197743245526": {
            "length": 48,
            "waveforms": {
                "single": "1142738197743245526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7523769831946878645": {
            "length": 48,
            "waveforms": {
                "single": "7523769831946878645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7745263891145593893": {
            "length": 48,
            "waveforms": {
                "single": "7745263891145593893",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6597442073968725120": {
            "length": 48,
            "waveforms": {
                "single": "6597442073968725120",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-76980030730760872": {
            "length": 52,
            "waveforms": {
                "single": "-76980030730760872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8795201761971891983": {
            "length": 52,
            "waveforms": {
                "single": "8795201761971891983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1127846705450341614": {
            "length": 52,
            "waveforms": {
                "single": "1127846705450341614",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6982382290363799504": {
            "length": 52,
            "waveforms": {
                "single": "6982382290363799504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "307960185664313512": {
            "length": 56,
            "waveforms": {
                "single": "307960185664313512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "529454244863028760": {
            "length": 56,
            "waveforms": {
                "single": "529454244863028760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9045108036143870001": {
            "length": 56,
            "waveforms": {
                "single": "-9045108036143870001",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8780310269678988071": {
            "length": 56,
            "waveforms": {
                "single": "8780310269678988071",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6847348348140703138": {
            "length": 60,
            "waveforms": {
                "single": "-6847348348140703138",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7960423749892959969": {
            "length": 60,
            "waveforms": {
                "single": "7960423749892959969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1614138531113938792": {
            "length": 60,
            "waveforms": {
                "single": "-1614138531113938792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1392644471915223544": {
            "length": 60,
            "waveforms": {
                "single": "-1392644471915223544",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7805817769133832612": {
            "length": 64,
            "waveforms": {
                "single": "7805817769133832612",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "805115216087943319": {
            "length": 64,
            "waveforms": {
                "single": "805115216087943319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5407716487548954658": {
            "length": 64,
            "waveforms": {
                "single": "-5407716487548954658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8010061657610475823": {
            "length": 64,
            "waveforms": {
                "single": "-8010061657610475823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6795634646589696198": {
            "length": 68,
            "waveforms": {
                "single": "-6795634646589696198",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2988462740347072547": {
            "length": 68,
            "waveforms": {
                "single": "-2988462740347072547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5883719052355580308": {
            "length": 68,
            "waveforms": {
                "single": "5883719052355580308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2244747076679691799": {
            "length": 68,
            "waveforms": {
                "single": "2244747076679691799",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2931457821342838834": {
            "length": 72,
            "waveforms": {
                "single": "-2931457821342838834",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4442506764682858662": {
            "length": 72,
            "waveforms": {
                "single": "4442506764682858662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2682981421706746289": {
            "length": 72,
            "waveforms": {
                "single": "2682981421706746289",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4910561457125324851": {
            "length": 72,
            "waveforms": {
                "single": "-4910561457125324851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7249538735257849559": {
            "length": 76,
            "waveforms": {
                "single": "7249538735257849559",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1332090593926984825": {
            "length": 76,
            "waveforms": {
                "single": "-1332090593926984825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5048941040276648294": {
            "length": 76,
            "waveforms": {
                "single": "5048941040276648294",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-127263857745882339": {
            "length": 76,
            "waveforms": {
                "single": "-127263857745882339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "94230201452832909": {
            "length": 80,
            "waveforms": {
                "single": "94230201452832909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6098878911102946384": {
            "length": 80,
            "waveforms": {
                "single": "6098878911102946384",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6320372970301661632": {
            "length": 80,
            "waveforms": {
                "single": "6320372970301661632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7855787242425640367": {
            "length": 40,
            "waveforms": {
                "I": "7855787242425640367_i",
                "Q": "7855787242425640367_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "476222452027415019": {
            "length": 40,
            "waveforms": {
                "I": "476222452027415019_i",
                "Q": "476222452027415019_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4223968515442956738": {
            "length": 40,
            "waveforms": {
                "I": "-4223968515442956738_i",
                "Q": "-4223968515442956738_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4069197763641637052": {
            "length": 40,
            "waveforms": {
                "I": "4069197763641637052_i",
                "Q": "4069197763641637052_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "7094696613202078498_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "7094696613202078498_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-3934457506082242534": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "3731896037285345872_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "3731896037285345872_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-284868177196146850_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-284868177196146850_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "4873841829533098564_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "4873841829533098564_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4985059144666518607_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-4985059144666518607_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-7395328971184281178_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-7395328971184281178_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8092607650656619608_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-8092607650656619608_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-3545319169232144850_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-3545319169232144850_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6918743688795237942": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-6135055201063443799": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "9116503376798404805": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "3496511998947688675": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-4586428867622428247": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "5694271686950855538": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-1056451364795806810": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8723806421317357179": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "2844540637407502962": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "1362802382406075301": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-5100008822530049621": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-7452374491292343841": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3229480853802577346": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8793771887436006510": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "9015265946634721758": {
            "sample": 0.25,
            "type": "constant",
        },
        "-21404986262412632": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "200089072936302616": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7564799655678327813": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "2397848760939469479": {
            "sample": 0.25,
            "type": "constant",
        },
        "2619342820138184727": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "585029289331377000": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "806523348530092248": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "2782788977334543863": {
            "sample": 0.25,
            "type": "constant",
        },
        "3004283036533259111": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1856461219356390338": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8237492853560023457": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-8994824209128748534": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8011491532146361296": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8082886872800896100": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8937819290124514821": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-5592237784944479185": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6740059602121347958": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-359027967917714839": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2711393636680009059": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-4320805854919465847": {
            "sample": 0.25,
            "type": "constant",
        },
        "-513633948676842196": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6133625326527558326": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4719575868349922150": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-1112026409264155050": {
            "sample": 0.25,
            "type": "constant",
        },
        "-128693732281767812": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7138829615551804261": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1055021490259921337": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-8722376546781471706": {
            "sample": 0.25,
            "type": "constant",
        },
        "1142738197743245526": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7523769831946878645": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7745263891145593893": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "6597442073968725120": {
            "sample": 0.25,
            "type": "constant",
        },
        "-76980030730760872": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8795201761971891983": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1127846705450341614": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "6982382290363799504": {
            "sample": 0.25,
            "type": "constant",
        },
        "307960185664313512": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "529454244863028760": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-9045108036143870001": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "8780310269678988071": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6847348348140703138": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7960423749892959969": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1614138531113938792": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-1392644471915223544": {
            "sample": 0.25,
            "type": "constant",
        },
        "7805817769133832612": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "805115216087943319": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5407716487548954658": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-8010061657610475823": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6795634646589696198": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2988462740347072547": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5883719052355580308": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "2244747076679691799": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2931457821342838834": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4442506764682858662": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2682981421706746289": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-4910561457125324851": {
            "sample": 0.25,
            "type": "constant",
        },
        "7249538735257849559": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1332090593926984825": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5048941040276648294": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-127263857745882339": {
            "sample": 0.25,
            "type": "constant",
        },
        "94230201452832909": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6098878911102946384": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6320372970301661632": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "7855787242425640367_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "7855787242425640367_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "476222452027415019_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "476222452027415019_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-4223968515442956738_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-4223968515442956738_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "4069197763641637052_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "4069197763641637052_q": {
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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "6098878911102946384": "6098878911102946384",
                "6320372970301661632": "6320372970301661632",
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
                "4969399967854171079": "4969399967854171079_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_090",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-4985059144666518607": "-4985059144666518607",
                "-4223968515442956738": "-4223968515442956738",
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
                "mixer": "B3/drive_mixer_a98",
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
                "-8092607650656619608": "-8092607650656619608",
                "4069197763641637052": "4069197763641637052",
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
                "mixer": "B4/drive_mixer_dee",
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
                "-284868177196146850": "-284868177196146850",
                "476222452027415019": "476222452027415019",
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
                "mixer": "B2/drive_mixer_41e",
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
                "-6079164336930150448": "-6079164336930150448_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_007",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "-7827409459628951200": "-7827409459628951200_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_81c",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "1078235932028120661": "1078235932028120661_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_6cd",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "7094696613202078498": "7094696613202078498",
                "7855787242425640367": "7855787242425640367",
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
                "mixer": "B1/drive_mixer_631",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
        },
    },
    "pulses": {
        "7094696613202078498": {
            "length": 40,
            "waveforms": {
                "I": "7094696613202078498_i",
                "Q": "7094696613202078498_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3934457506082242534": {
            "length": 16,
            "waveforms": {
                "single": "-3934457506082242534",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1078235932028120661_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3731896037285345872_i",
                "Q": "3731896037285345872_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-284868177196146850": {
            "length": 40,
            "waveforms": {
                "I": "-284868177196146850_i",
                "Q": "-284868177196146850_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4969399967854171079_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4873841829533098564_i",
                "Q": "4873841829533098564_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4985059144666518607": {
            "length": 40,
            "waveforms": {
                "I": "-4985059144666518607_i",
                "Q": "-4985059144666518607_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7827409459628951200_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7395328971184281178_i",
                "Q": "-7395328971184281178_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-8092607650656619608": {
            "length": 40,
            "waveforms": {
                "I": "-8092607650656619608_i",
                "Q": "-8092607650656619608_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6079164336930150448_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-3545319169232144850_i",
                "Q": "-3545319169232144850_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6918743688795237942": {
            "length": 16,
            "waveforms": {
                "single": "6918743688795237942",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6135055201063443799": {
            "length": 16,
            "waveforms": {
                "single": "-6135055201063443799",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9116503376798404805": {
            "length": 16,
            "waveforms": {
                "single": "9116503376798404805",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3496511998947688675": {
            "length": 16,
            "waveforms": {
                "single": "3496511998947688675",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4586428867622428247": {
            "length": 16,
            "waveforms": {
                "single": "-4586428867622428247",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5694271686950855538": {
            "length": 16,
            "waveforms": {
                "single": "5694271686950855538",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1056451364795806810": {
            "length": 16,
            "waveforms": {
                "single": "-1056451364795806810",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8723806421317357179": {
            "length": 16,
            "waveforms": {
                "single": "-8723806421317357179",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2844540637407502962": {
            "length": 16,
            "waveforms": {
                "single": "2844540637407502962",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1362802382406075301": {
            "length": 16,
            "waveforms": {
                "single": "1362802382406075301",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5100008822530049621": {
            "length": 16,
            "waveforms": {
                "single": "-5100008822530049621",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7452374491292343841": {
            "length": 16,
            "waveforms": {
                "single": "-7452374491292343841",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3229480853802577346": {
            "length": 16,
            "waveforms": {
                "single": "3229480853802577346",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8793771887436006510": {
            "length": 16,
            "waveforms": {
                "single": "8793771887436006510",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9015265946634721758": {
            "length": 16,
            "waveforms": {
                "single": "9015265946634721758",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-21404986262412632": {
            "length": 20,
            "waveforms": {
                "single": "-21404986262412632",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "200089072936302616": {
            "length": 20,
            "waveforms": {
                "single": "200089072936302616",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7564799655678327813": {
            "length": 20,
            "waveforms": {
                "single": "-7564799655678327813",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2397848760939469479": {
            "length": 20,
            "waveforms": {
                "single": "2397848760939469479",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2619342820138184727": {
            "length": 24,
            "waveforms": {
                "single": "2619342820138184727",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "585029289331377000": {
            "length": 24,
            "waveforms": {
                "single": "585029289331377000",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "806523348530092248": {
            "length": 24,
            "waveforms": {
                "single": "806523348530092248",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2782788977334543863": {
            "length": 24,
            "waveforms": {
                "single": "2782788977334543863",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3004283036533259111": {
            "length": 28,
            "waveforms": {
                "single": "3004283036533259111",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1856461219356390338": {
            "length": 28,
            "waveforms": {
                "single": "1856461219356390338",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8237492853560023457": {
            "length": 28,
            "waveforms": {
                "single": "8237492853560023457",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8994824209128748534": {
            "length": 28,
            "waveforms": {
                "single": "-8994824209128748534",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8011491532146361296": {
            "length": 32,
            "waveforms": {
                "single": "-8011491532146361296",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8082886872800896100": {
            "length": 32,
            "waveforms": {
                "single": "8082886872800896100",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8937819290124514821": {
            "length": 32,
            "waveforms": {
                "single": "-8937819290124514821",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5592237784944479185": {
            "length": 32,
            "waveforms": {
                "single": "-5592237784944479185",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6740059602121347958": {
            "length": 36,
            "waveforms": {
                "single": "-6740059602121347958",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-359027967917714839": {
            "length": 36,
            "waveforms": {
                "single": "-359027967917714839",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2711393636680009059": {
            "length": 36,
            "waveforms": {
                "single": "-2711393636680009059",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4320805854919465847": {
            "length": 36,
            "waveforms": {
                "single": "-4320805854919465847",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-513633948676842196": {
            "length": 40,
            "waveforms": {
                "single": "-513633948676842196",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6133625326527558326": {
            "length": 40,
            "waveforms": {
                "single": "-6133625326527558326",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4719575868349922150": {
            "length": 40,
            "waveforms": {
                "single": "4719575868349922150",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1112026409264155050": {
            "length": 40,
            "waveforms": {
                "single": "-1112026409264155050",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-128693732281767812": {
            "length": 44,
            "waveforms": {
                "single": "-128693732281767812",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7138829615551804261": {
            "length": 44,
            "waveforms": {
                "single": "7138829615551804261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1055021490259921337": {
            "length": 44,
            "waveforms": {
                "single": "-1055021490259921337",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8722376546781471706": {
            "length": 44,
            "waveforms": {
                "single": "-8722376546781471706",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1142738197743245526": {
            "length": 48,
            "waveforms": {
                "single": "1142738197743245526",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7523769831946878645": {
            "length": 48,
            "waveforms": {
                "single": "7523769831946878645",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7745263891145593893": {
            "length": 48,
            "waveforms": {
                "single": "7745263891145593893",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6597442073968725120": {
            "length": 48,
            "waveforms": {
                "single": "6597442073968725120",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-76980030730760872": {
            "length": 52,
            "waveforms": {
                "single": "-76980030730760872",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8795201761971891983": {
            "length": 52,
            "waveforms": {
                "single": "8795201761971891983",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1127846705450341614": {
            "length": 52,
            "waveforms": {
                "single": "1127846705450341614",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6982382290363799504": {
            "length": 52,
            "waveforms": {
                "single": "6982382290363799504",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "307960185664313512": {
            "length": 56,
            "waveforms": {
                "single": "307960185664313512",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "529454244863028760": {
            "length": 56,
            "waveforms": {
                "single": "529454244863028760",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9045108036143870001": {
            "length": 56,
            "waveforms": {
                "single": "-9045108036143870001",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8780310269678988071": {
            "length": 56,
            "waveforms": {
                "single": "8780310269678988071",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6847348348140703138": {
            "length": 60,
            "waveforms": {
                "single": "-6847348348140703138",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7960423749892959969": {
            "length": 60,
            "waveforms": {
                "single": "7960423749892959969",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1614138531113938792": {
            "length": 60,
            "waveforms": {
                "single": "-1614138531113938792",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1392644471915223544": {
            "length": 60,
            "waveforms": {
                "single": "-1392644471915223544",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7805817769133832612": {
            "length": 64,
            "waveforms": {
                "single": "7805817769133832612",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "805115216087943319": {
            "length": 64,
            "waveforms": {
                "single": "805115216087943319",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5407716487548954658": {
            "length": 64,
            "waveforms": {
                "single": "-5407716487548954658",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8010061657610475823": {
            "length": 64,
            "waveforms": {
                "single": "-8010061657610475823",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6795634646589696198": {
            "length": 68,
            "waveforms": {
                "single": "-6795634646589696198",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2988462740347072547": {
            "length": 68,
            "waveforms": {
                "single": "-2988462740347072547",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5883719052355580308": {
            "length": 68,
            "waveforms": {
                "single": "5883719052355580308",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2244747076679691799": {
            "length": 68,
            "waveforms": {
                "single": "2244747076679691799",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2931457821342838834": {
            "length": 72,
            "waveforms": {
                "single": "-2931457821342838834",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4442506764682858662": {
            "length": 72,
            "waveforms": {
                "single": "4442506764682858662",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2682981421706746289": {
            "length": 72,
            "waveforms": {
                "single": "2682981421706746289",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4910561457125324851": {
            "length": 72,
            "waveforms": {
                "single": "-4910561457125324851",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7249538735257849559": {
            "length": 76,
            "waveforms": {
                "single": "7249538735257849559",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1332090593926984825": {
            "length": 76,
            "waveforms": {
                "single": "-1332090593926984825",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5048941040276648294": {
            "length": 76,
            "waveforms": {
                "single": "5048941040276648294",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-127263857745882339": {
            "length": 76,
            "waveforms": {
                "single": "-127263857745882339",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "94230201452832909": {
            "length": 80,
            "waveforms": {
                "single": "94230201452832909",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6098878911102946384": {
            "length": 80,
            "waveforms": {
                "single": "6098878911102946384",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6320372970301661632": {
            "length": 80,
            "waveforms": {
                "single": "6320372970301661632",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7855787242425640367": {
            "length": 40,
            "waveforms": {
                "I": "7855787242425640367_i",
                "Q": "7855787242425640367_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "476222452027415019": {
            "length": 40,
            "waveforms": {
                "I": "476222452027415019_i",
                "Q": "476222452027415019_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4223968515442956738": {
            "length": 40,
            "waveforms": {
                "I": "-4223968515442956738_i",
                "Q": "-4223968515442956738_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4069197763641637052": {
            "length": 40,
            "waveforms": {
                "I": "4069197763641637052_i",
                "Q": "4069197763641637052_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "7094696613202078498_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7094696613202078498_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3934457506082242534": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3731896037285345872_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "3731896037285345872_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-284868177196146850_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-284868177196146850_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4873841829533098564_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "4873841829533098564_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4985059144666518607_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4985059144666518607_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7395328971184281178_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-7395328971184281178_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-8092607650656619608_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8092607650656619608_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3545319169232144850_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-3545319169232144850_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "6918743688795237942": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6135055201063443799": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9116503376798404805": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3496511998947688675": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4586428867622428247": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5694271686950855538": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1056451364795806810": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8723806421317357179": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2844540637407502962": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1362802382406075301": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5100008822530049621": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7452374491292343841": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3229480853802577346": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8793771887436006510": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9015265946634721758": {
            "type": "constant",
            "sample": 0.25,
        },
        "-21404986262412632": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "200089072936302616": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7564799655678327813": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2397848760939469479": {
            "type": "constant",
            "sample": 0.25,
        },
        "2619342820138184727": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "585029289331377000": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "806523348530092248": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2782788977334543863": {
            "type": "constant",
            "sample": 0.25,
        },
        "3004283036533259111": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1856461219356390338": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8237492853560023457": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8994824209128748534": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8011491532146361296": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8082886872800896100": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8937819290124514821": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5592237784944479185": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6740059602121347958": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-359027967917714839": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2711393636680009059": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4320805854919465847": {
            "type": "constant",
            "sample": 0.25,
        },
        "-513633948676842196": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6133625326527558326": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4719575868349922150": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1112026409264155050": {
            "type": "constant",
            "sample": 0.25,
        },
        "-128693732281767812": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7138829615551804261": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1055021490259921337": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8722376546781471706": {
            "type": "constant",
            "sample": 0.25,
        },
        "1142738197743245526": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7523769831946878645": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7745263891145593893": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6597442073968725120": {
            "type": "constant",
            "sample": 0.25,
        },
        "-76980030730760872": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8795201761971891983": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1127846705450341614": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6982382290363799504": {
            "type": "constant",
            "sample": 0.25,
        },
        "307960185664313512": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "529454244863028760": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9045108036143870001": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8780310269678988071": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6847348348140703138": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7960423749892959969": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1614138531113938792": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1392644471915223544": {
            "type": "constant",
            "sample": 0.25,
        },
        "7805817769133832612": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "805115216087943319": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5407716487548954658": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8010061657610475823": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6795634646589696198": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2988462740347072547": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5883719052355580308": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2244747076679691799": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2931457821342838834": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4442506764682858662": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2682981421706746289": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4910561457125324851": {
            "type": "constant",
            "sample": 0.25,
        },
        "7249538735257849559": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1332090593926984825": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5048941040276648294": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-127263857745882339": {
            "type": "constant",
            "sample": 0.25,
        },
        "94230201452832909": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6098878911102946384": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6320372970301661632": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7855787242425640367_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7855787242425640367_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "476222452027415019_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "476222452027415019_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4223968515442956738_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4223968515442956738_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4069197763641637052_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4069197763641637052_q": {
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
        "B2/acquisition_mixer_090": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_a98": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_dee": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_41e": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_007": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_81c": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_6cd": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_631": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

