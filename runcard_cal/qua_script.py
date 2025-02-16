
# Single QUA script generated at 2025-02-16 11:17:32.198014
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
        play("8616111466517398356", "B1/drive")
        wait(11, "B1/flux")
        play("-1527264955344753330", "B1/flux")
        wait(46, "B1/drive")
        play("2331172807106103400", "B1/drive")
        wait(66, "B1/acquisition")
        measure("8230683819360285798", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("-3235622884554674349", "B2/drive")
        wait(11, "B2/flux")
        play("-1527264955344753330", "B2/flux")
        wait(46, "B2/drive")
        play("-2474532255331112480", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-5721175032143998767", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("-1504732966848337736", "B3/drive")
        wait(11, "B3/flux")
        play("-1527264955344753330", "B3/flux")
        wait(46, "B3/drive")
        play("-743642337624775867", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-71240385917569430", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("-17674219780723041", "B4/drive")
        wait(11, "B4/flux")
        play("-1527264955344753330", "B4/flux")
        wait(46, "B4/drive")
        play("743416409442838828", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1677004736781231322", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25501, "B1/drive")
        wait(25501, "B2/drive")
        wait(25001, "B3/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B1/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25536, "B3/flux")
        play("8616111466517398356", "B1/drive")
        wait(11, "B1/flux")
        play("4853766678858879789", "B1/flux")
        wait(46, "B1/drive")
        play("2331172807106103400", "B1/drive")
        wait(66, "B1/acquisition")
        measure("8230683819360285798", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("-3235622884554674349", "B2/drive")
        wait(11, "B2/flux")
        play("4853766678858879789", "B2/flux")
        wait(46, "B2/drive")
        play("-2474532255331112480", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-5721175032143998767", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("-1504732966848337736", "B3/drive")
        wait(11, "B3/flux")
        play("4853766678858879789", "B3/flux")
        wait(46, "B3/drive")
        play("-743642337624775867", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-71240385917569430", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("-17674219780723041", "B4/drive")
        wait(11, "B4/flux")
        play("4853766678858879789", "B4/flux")
        wait(46, "B4/drive")
        play("743416409442838828", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1677004736781231322", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25501, "B1/drive")
        wait(25501, "B2/drive")
        wait(25001, "B3/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B4/acquisition")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25536, "B1/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25536, "B3/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("8230683819360285798_B1|acquisition_shots")
        r2.buffer(2).average().save("-5721175032143998767_B2|acquisition_shots")
        r3.buffer(2).average().save("-71240385917569430_B3|acquisition_shots")
        r4.buffer(2).average().save("1677004736781231322_B4|acquisition_shots")


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
                "3": {
                    "offset": 0.0,
                    "filter": {},
                },
                "4": {
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
                "3": {},
                "7": {},
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
                "2": {
                    "LO_frequency": 4900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "8616111466517398356": "8616111466517398356",
                "2331172807106103400": "2331172807106103400",
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
                "-3235622884554674349": "-3235622884554674349",
                "-2474532255331112480": "-2474532255331112480",
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
                "-71240385917569430": "-71240385917569430_B3/acquisition",
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
                "1677004736781231322": "1677004736781231322_B4/acquisition",
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
                "-5721175032143998767": "-5721175032143998767_B2/acquisition",
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
                "8230683819360285798": "8230683819360285798_B1/acquisition",
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
                "-1504732966848337736": "-1504732966848337736",
                "-743642337624775867": "-743642337624775867",
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
                "-17674219780723041": "-17674219780723041",
                "743416409442838828": "743416409442838828",
            },
        },
    },
    "pulses": {
        "8616111466517398356": {
            "length": 40,
            "waveforms": {
                "I": "8616111466517398356_i",
                "Q": "8616111466517398356_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4408130845702960000": {
            "length": 16,
            "waveforms": {
                "single": "-4408130845702960000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8230683819360285798_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3646000921037737192_i",
                "Q": "3646000921037737192_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-3235622884554674349": {
            "length": 40,
            "waveforms": {
                "I": "-3235622884554674349_i",
                "Q": "-3235622884554674349_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5721175032143998767_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6612768071789204907_i",
                "Q": "-6612768071789204907_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-1504732966848337736": {
            "length": 40,
            "waveforms": {
                "I": "-1504732966848337736_i",
                "Q": "-1504732966848337736_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-71240385917569430_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-435194798797033033_i",
                "Q": "-435194798797033033_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-17674219780723041": {
            "length": 40,
            "waveforms": {
                "I": "-17674219780723041_i",
                "Q": "-17674219780723041_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1677004736781231322_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3414815003155103295_i",
                "Q": "3414815003155103295_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "7160216213021900141": {
            "length": 16,
            "waveforms": {
                "single": "7160216213021900141",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4905496226484018356": {
            "length": 16,
            "waveforms": {
                "single": "-4905496226484018356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3300033062742973423": {
            "length": 16,
            "waveforms": {
                "single": "3300033062742973423",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3022838659326971209": {
            "length": 16,
            "waveforms": {
                "single": "3022838659326971209",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "670472990564676989": {
            "length": 16,
            "waveforms": {
                "single": "670472990564676989",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7766650488615689773": {
            "length": 16,
            "waveforms": {
                "single": "7766650488615689773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "173107609783618633": {
            "length": 16,
            "waveforms": {
                "single": "173107609783618633",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3089726737766559100": {
            "length": 16,
            "waveforms": {
                "single": "3089726737766559100",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8101442495594608198": {
            "length": 16,
            "waveforms": {
                "single": "8101442495594608198",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8322936554793323446": {
            "length": 16,
            "waveforms": {
                "single": "8322936554793323446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4956405209163061145": {
            "length": 16,
            "waveforms": {
                "single": "4956405209163061145",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7926047830913061307": {
            "length": 16,
            "waveforms": {
                "single": "-7926047830913061307",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3403730060823057991": {
            "length": 16,
            "waveforms": {
                "single": "-3403730060823057991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2692838013886296961": {
            "length": 16,
            "waveforms": {
                "single": "-2692838013886296961",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2471343954687581713": {
            "length": 16,
            "waveforms": {
                "single": "-2471343954687581713",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-495078325883130098": {
            "length": 20,
            "waveforms": {
                "single": "-495078325883130098",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-273584266684414850": {
            "length": 20,
            "waveforms": {
                "single": "-273584266684414850",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4248733503405588466": {
            "length": 20,
            "waveforms": {
                "single": "4248733503405588466",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2086403738292507329": {
            "length": 20,
            "waveforms": {
                "single": "-2086403738292507329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5453560239586690952": {
            "length": 24,
            "waveforms": {
                "single": "5453560239586690952",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "111355949710659534": {
            "length": 24,
            "waveforms": {
                "single": "111355949710659534",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "332850008909374782": {
            "length": 24,
            "waveforms": {
                "single": "332850008909374782",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6545547006075316693": {
            "length": 24,
            "waveforms": {
                "single": "-6545547006075316693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8482326864789044360": {
            "length": 28,
            "waveforms": {
                "single": "-8482326864789044360",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1382787879735672872": {
            "length": 28,
            "waveforms": {
                "single": "1382787879735672872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6284567176785877497": {
            "length": 28,
            "waveforms": {
                "single": "-6284567176785877497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5411453845177011771": {
            "length": 28,
            "waveforms": {
                "single": "5411453845177011771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1540755347497158933": {
            "length": 32,
            "waveforms": {
                "single": "-1540755347497158933",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7609213533180178634": {
            "length": 32,
            "waveforms": {
                "single": "7609213533180178634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9035251443964319329": {
            "length": 32,
            "waveforms": {
                "single": "9035251443964319329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1205963340518240508": {
            "length": 32,
            "waveforms": {
                "single": "-1205963340518240508",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5890214157532772276": {
            "length": 36,
            "waveforms": {
                "single": "5890214157532772276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6992238882543350176": {
            "length": 36,
            "waveforms": {
                "single": "-6992238882543350176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3185066976300726525": {
            "length": 36,
            "waveforms": {
                "single": "-3185066976300726525",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7067825991597099493": {
            "length": 36,
            "waveforms": {
                "single": "7067825991597099493",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6446500223710405949": {
            "length": 40,
            "waveforms": {
                "single": "6446500223710405949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6607298666148275792": {
            "length": 40,
            "waveforms": {
                "single": "-6607298666148275792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8644259911713572812": {
            "length": 40,
            "waveforms": {
                "single": "8644259911713572812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3024268533862856682": {
            "length": 40,
            "waveforms": {
                "single": "3024268533862856682",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3726454517883805666": {
            "length": 44,
            "waveforms": {
                "single": "-3726454517883805666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6665156275931086795": {
            "length": 44,
            "waveforms": {
                "single": "6665156275931086795",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1528694829880638803": {
            "length": 44,
            "waveforms": {
                "single": "-1528694829880638803",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9196049886402189172": {
            "length": 44,
            "waveforms": {
                "single": "-9196049886402189172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4673732116312185856": {
            "length": 48,
            "waveforms": {
                "single": "-4673732116312185856",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8324366429329208919": {
            "length": 48,
            "waveforms": {
                "single": "8324366429329208919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5902274675149292406": {
            "length": 48,
            "waveforms": {
                "single": "5902274675149292406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6123768734348007654": {
            "length": 48,
            "waveforms": {
                "single": "6123768734348007654",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1543586322173542715": {
            "length": 52,
            "waveforms": {
                "single": "-1543586322173542715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2978731447916460601": {
            "length": 52,
            "waveforms": {
                "single": "2978731447916460601",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8543022481549889765": {
            "length": 52,
            "waveforms": {
                "single": "8543022481549889765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7539677739982101450": {
            "length": 52,
            "waveforms": {
                "single": "-7539677739982101450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-272154392148529377": {
            "length": 56,
            "waveforms": {
                "single": "-272154392148529377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3535017514094094274": {
            "length": 56,
            "waveforms": {
                "single": "3535017514094094274",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8927962697944964149": {
            "length": 56,
            "waveforms": {
                "single": "8927962697944964149",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2147099355053352734": {
            "length": 56,
            "waveforms": {
                "single": "2147099355053352734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "112785824246545007": {
            "length": 60,
            "waveforms": {
                "single": "112785824246545007",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2239579844515749213": {
            "length": 60,
            "waveforms": {
                "single": "-2239579844515749213",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8247349445739574129": {
            "length": 60,
            "waveforms": {
                "single": "-8247349445739574129",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2532039571448427118": {
            "length": 60,
            "waveforms": {
                "single": "2532039571448427118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6339211477691050769": {
            "length": 64,
            "waveforms": {
                "single": "6339211477691050769",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5191389660514181996": {
            "length": 64,
            "waveforms": {
                "single": "5191389660514181996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2020923792295068367": {
            "length": 64,
            "waveforms": {
                "single": "-2020923792295068367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-594885881510927672": {
            "length": 64,
            "waveforms": {
                "single": "-594885881510927672",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7610643407716064107": {
            "length": 68,
            "waveforms": {
                "single": "7610643407716064107",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1990652029865347977": {
            "length": 68,
            "waveforms": {
                "single": "1990652029865347977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5602890848966723163": {
            "length": 68,
            "waveforms": {
                "single": "-5602890848966723163",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8416846918791605398": {
            "length": 68,
            "waveforms": {
                "single": "-8416846918791605398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3405131160963556300": {
            "length": 72,
            "waveforms": {
                "single": "-3405131160963556300",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3183637101764841052": {
            "length": 72,
            "waveforms": {
                "single": "-3183637101764841052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7498218243330080135": {
            "length": 72,
            "waveforms": {
                "single": "7498218243330080135",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-985877413761674189": {
            "length": 72,
            "waveforms": {
                "single": "-985877413761674189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-764383354562958941": {
            "length": 76,
            "waveforms": {
                "single": "-764383354562958941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2798696885369766668": {
            "length": 76,
            "waveforms": {
                "single": "-2798696885369766668",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4468826462463805405": {
            "length": 76,
            "waveforms": {
                "single": "4468826462463805405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7287911918353665812": {
            "length": 76,
            "waveforms": {
                "single": "7287911918353665812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-379443138167884557": {
            "length": 80,
            "waveforms": {
                "single": "-379443138167884557",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1527264955344753330": {
            "length": 80,
            "waveforms": {
                "single": "-1527264955344753330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4853766678858879789": {
            "length": 80,
            "waveforms": {
                "single": "4853766678858879789",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2331172807106103400": {
            "length": 40,
            "waveforms": {
                "I": "2331172807106103400_i",
                "Q": "2331172807106103400_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2474532255331112480": {
            "length": 40,
            "waveforms": {
                "I": "-2474532255331112480_i",
                "Q": "-2474532255331112480_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-743642337624775867": {
            "length": 40,
            "waveforms": {
                "I": "-743642337624775867_i",
                "Q": "-743642337624775867_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "743416409442838828": {
            "length": 40,
            "waveforms": {
                "I": "743416409442838828_i",
                "Q": "743416409442838828_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8616111466517398356_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "8616111466517398356_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-4408130845702960000": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "3646000921037737192_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "3646000921037737192_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3235622884554674349_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-3235622884554674349_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-6612768071789204907_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-6612768071789204907_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-1504732966848337736_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-1504732966848337736_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-435194798797033033_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-435194798797033033_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-17674219780723041_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-17674219780723041_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "3414815003155103295_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "3414815003155103295_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7160216213021900141": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-4905496226484018356": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "3300033062742973423": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "3022838659326971209": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "670472990564676989": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "7766650488615689773": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "173107609783618633": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "3089726737766559100": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "8101442495594608198": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "8322936554793323446": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "4956405209163061145": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-7926047830913061307": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3403730060823057991": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2692838013886296961": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-2471343954687581713": {
            "sample": 0.25,
            "type": "constant",
        },
        "-495078325883130098": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-273584266684414850": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4248733503405588466": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-2086403738292507329": {
            "sample": 0.25,
            "type": "constant",
        },
        "5453560239586690952": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "111355949710659534": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "332850008909374782": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-6545547006075316693": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8482326864789044360": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1382787879735672872": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6284567176785877497": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "5411453845177011771": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1540755347497158933": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7609213533180178634": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9035251443964319329": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-1205963340518240508": {
            "sample": 0.25,
            "type": "constant",
        },
        "5890214157532772276": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6992238882543350176": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3185066976300726525": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "7067825991597099493": {
            "sample": 0.25,
            "type": "constant",
        },
        "6446500223710405949": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6607298666148275792": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8644259911713572812": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "3024268533862856682": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3726454517883805666": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6665156275931086795": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1528694829880638803": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-9196049886402189172": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4673732116312185856": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8324366429329208919": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5902274675149292406": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "6123768734348007654": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1543586322173542715": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2978731447916460601": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8543022481549889765": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-7539677739982101450": {
            "sample": 0.25,
            "type": "constant",
        },
        "-272154392148529377": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3535017514094094274": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8927962697944964149": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "2147099355053352734": {
            "sample": 0.25,
            "type": "constant",
        },
        "112785824246545007": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2239579844515749213": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8247349445739574129": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "2532039571448427118": {
            "sample": 0.25,
            "type": "constant",
        },
        "6339211477691050769": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5191389660514181996": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2020923792295068367": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-594885881510927672": {
            "sample": 0.25,
            "type": "constant",
        },
        "7610643407716064107": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1990652029865347977": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5602890848966723163": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-8416846918791605398": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3405131160963556300": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3183637101764841052": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7498218243330080135": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-985877413761674189": {
            "sample": 0.25,
            "type": "constant",
        },
        "-764383354562958941": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2798696885369766668": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4468826462463805405": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "7287911918353665812": {
            "sample": 0.25,
            "type": "constant",
        },
        "-379443138167884557": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1527264955344753330": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4853766678858879789": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "2331172807106103400_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "2331172807106103400_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-2474532255331112480_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-2474532255331112480_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-743642337624775867_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-743642337624775867_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "743416409442838828_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "743416409442838828_q": {
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
                "3": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "-1527264955344753330": "-1527264955344753330",
                "4853766678858879789": "4853766678858879789",
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
                "8616111466517398356": "8616111466517398356",
                "2331172807106103400": "2331172807106103400",
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
                "mixer": "B1/drive_mixer_c58",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "-3235622884554674349": "-3235622884554674349",
                "-2474532255331112480": "-2474532255331112480",
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
                "mixer": "B2/drive_mixer_1a6",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "-71240385917569430": "-71240385917569430_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_fb9",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "1677004736781231322": "1677004736781231322_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_c6d",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "-5721175032143998767": "-5721175032143998767_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_6ec",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "8230683819360285798": "8230683819360285798_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_10f",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "-1504732966848337736": "-1504732966848337736",
                "-743642337624775867": "-743642337624775867",
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
                "mixer": "B3/drive_mixer_3ac",
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
                "-17674219780723041": "-17674219780723041",
                "743416409442838828": "743416409442838828",
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
                "mixer": "B4/drive_mixer_d65",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "8616111466517398356": {
            "length": 40,
            "waveforms": {
                "I": "8616111466517398356_i",
                "Q": "8616111466517398356_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4408130845702960000": {
            "length": 16,
            "waveforms": {
                "single": "-4408130845702960000",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8230683819360285798_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3646000921037737192_i",
                "Q": "3646000921037737192_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-3235622884554674349": {
            "length": 40,
            "waveforms": {
                "I": "-3235622884554674349_i",
                "Q": "-3235622884554674349_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5721175032143998767_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6612768071789204907_i",
                "Q": "-6612768071789204907_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-1504732966848337736": {
            "length": 40,
            "waveforms": {
                "I": "-1504732966848337736_i",
                "Q": "-1504732966848337736_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-71240385917569430_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-435194798797033033_i",
                "Q": "-435194798797033033_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-17674219780723041": {
            "length": 40,
            "waveforms": {
                "I": "-17674219780723041_i",
                "Q": "-17674219780723041_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1677004736781231322_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3414815003155103295_i",
                "Q": "3414815003155103295_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7160216213021900141": {
            "length": 16,
            "waveforms": {
                "single": "7160216213021900141",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4905496226484018356": {
            "length": 16,
            "waveforms": {
                "single": "-4905496226484018356",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3300033062742973423": {
            "length": 16,
            "waveforms": {
                "single": "3300033062742973423",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3022838659326971209": {
            "length": 16,
            "waveforms": {
                "single": "3022838659326971209",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "670472990564676989": {
            "length": 16,
            "waveforms": {
                "single": "670472990564676989",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7766650488615689773": {
            "length": 16,
            "waveforms": {
                "single": "7766650488615689773",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "173107609783618633": {
            "length": 16,
            "waveforms": {
                "single": "173107609783618633",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3089726737766559100": {
            "length": 16,
            "waveforms": {
                "single": "3089726737766559100",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8101442495594608198": {
            "length": 16,
            "waveforms": {
                "single": "8101442495594608198",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8322936554793323446": {
            "length": 16,
            "waveforms": {
                "single": "8322936554793323446",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4956405209163061145": {
            "length": 16,
            "waveforms": {
                "single": "4956405209163061145",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7926047830913061307": {
            "length": 16,
            "waveforms": {
                "single": "-7926047830913061307",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3403730060823057991": {
            "length": 16,
            "waveforms": {
                "single": "-3403730060823057991",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2692838013886296961": {
            "length": 16,
            "waveforms": {
                "single": "-2692838013886296961",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2471343954687581713": {
            "length": 16,
            "waveforms": {
                "single": "-2471343954687581713",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-495078325883130098": {
            "length": 20,
            "waveforms": {
                "single": "-495078325883130098",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-273584266684414850": {
            "length": 20,
            "waveforms": {
                "single": "-273584266684414850",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4248733503405588466": {
            "length": 20,
            "waveforms": {
                "single": "4248733503405588466",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2086403738292507329": {
            "length": 20,
            "waveforms": {
                "single": "-2086403738292507329",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5453560239586690952": {
            "length": 24,
            "waveforms": {
                "single": "5453560239586690952",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "111355949710659534": {
            "length": 24,
            "waveforms": {
                "single": "111355949710659534",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "332850008909374782": {
            "length": 24,
            "waveforms": {
                "single": "332850008909374782",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6545547006075316693": {
            "length": 24,
            "waveforms": {
                "single": "-6545547006075316693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8482326864789044360": {
            "length": 28,
            "waveforms": {
                "single": "-8482326864789044360",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1382787879735672872": {
            "length": 28,
            "waveforms": {
                "single": "1382787879735672872",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6284567176785877497": {
            "length": 28,
            "waveforms": {
                "single": "-6284567176785877497",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5411453845177011771": {
            "length": 28,
            "waveforms": {
                "single": "5411453845177011771",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1540755347497158933": {
            "length": 32,
            "waveforms": {
                "single": "-1540755347497158933",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7609213533180178634": {
            "length": 32,
            "waveforms": {
                "single": "7609213533180178634",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9035251443964319329": {
            "length": 32,
            "waveforms": {
                "single": "9035251443964319329",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1205963340518240508": {
            "length": 32,
            "waveforms": {
                "single": "-1205963340518240508",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5890214157532772276": {
            "length": 36,
            "waveforms": {
                "single": "5890214157532772276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6992238882543350176": {
            "length": 36,
            "waveforms": {
                "single": "-6992238882543350176",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3185066976300726525": {
            "length": 36,
            "waveforms": {
                "single": "-3185066976300726525",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7067825991597099493": {
            "length": 36,
            "waveforms": {
                "single": "7067825991597099493",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6446500223710405949": {
            "length": 40,
            "waveforms": {
                "single": "6446500223710405949",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6607298666148275792": {
            "length": 40,
            "waveforms": {
                "single": "-6607298666148275792",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8644259911713572812": {
            "length": 40,
            "waveforms": {
                "single": "8644259911713572812",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3024268533862856682": {
            "length": 40,
            "waveforms": {
                "single": "3024268533862856682",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3726454517883805666": {
            "length": 44,
            "waveforms": {
                "single": "-3726454517883805666",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6665156275931086795": {
            "length": 44,
            "waveforms": {
                "single": "6665156275931086795",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1528694829880638803": {
            "length": 44,
            "waveforms": {
                "single": "-1528694829880638803",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9196049886402189172": {
            "length": 44,
            "waveforms": {
                "single": "-9196049886402189172",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4673732116312185856": {
            "length": 48,
            "waveforms": {
                "single": "-4673732116312185856",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8324366429329208919": {
            "length": 48,
            "waveforms": {
                "single": "8324366429329208919",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5902274675149292406": {
            "length": 48,
            "waveforms": {
                "single": "5902274675149292406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6123768734348007654": {
            "length": 48,
            "waveforms": {
                "single": "6123768734348007654",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1543586322173542715": {
            "length": 52,
            "waveforms": {
                "single": "-1543586322173542715",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2978731447916460601": {
            "length": 52,
            "waveforms": {
                "single": "2978731447916460601",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8543022481549889765": {
            "length": 52,
            "waveforms": {
                "single": "8543022481549889765",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7539677739982101450": {
            "length": 52,
            "waveforms": {
                "single": "-7539677739982101450",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-272154392148529377": {
            "length": 56,
            "waveforms": {
                "single": "-272154392148529377",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3535017514094094274": {
            "length": 56,
            "waveforms": {
                "single": "3535017514094094274",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8927962697944964149": {
            "length": 56,
            "waveforms": {
                "single": "8927962697944964149",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2147099355053352734": {
            "length": 56,
            "waveforms": {
                "single": "2147099355053352734",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "112785824246545007": {
            "length": 60,
            "waveforms": {
                "single": "112785824246545007",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2239579844515749213": {
            "length": 60,
            "waveforms": {
                "single": "-2239579844515749213",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8247349445739574129": {
            "length": 60,
            "waveforms": {
                "single": "-8247349445739574129",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2532039571448427118": {
            "length": 60,
            "waveforms": {
                "single": "2532039571448427118",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6339211477691050769": {
            "length": 64,
            "waveforms": {
                "single": "6339211477691050769",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5191389660514181996": {
            "length": 64,
            "waveforms": {
                "single": "5191389660514181996",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2020923792295068367": {
            "length": 64,
            "waveforms": {
                "single": "-2020923792295068367",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-594885881510927672": {
            "length": 64,
            "waveforms": {
                "single": "-594885881510927672",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7610643407716064107": {
            "length": 68,
            "waveforms": {
                "single": "7610643407716064107",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1990652029865347977": {
            "length": 68,
            "waveforms": {
                "single": "1990652029865347977",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5602890848966723163": {
            "length": 68,
            "waveforms": {
                "single": "-5602890848966723163",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8416846918791605398": {
            "length": 68,
            "waveforms": {
                "single": "-8416846918791605398",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3405131160963556300": {
            "length": 72,
            "waveforms": {
                "single": "-3405131160963556300",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3183637101764841052": {
            "length": 72,
            "waveforms": {
                "single": "-3183637101764841052",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7498218243330080135": {
            "length": 72,
            "waveforms": {
                "single": "7498218243330080135",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-985877413761674189": {
            "length": 72,
            "waveforms": {
                "single": "-985877413761674189",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-764383354562958941": {
            "length": 76,
            "waveforms": {
                "single": "-764383354562958941",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2798696885369766668": {
            "length": 76,
            "waveforms": {
                "single": "-2798696885369766668",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4468826462463805405": {
            "length": 76,
            "waveforms": {
                "single": "4468826462463805405",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7287911918353665812": {
            "length": 76,
            "waveforms": {
                "single": "7287911918353665812",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-379443138167884557": {
            "length": 80,
            "waveforms": {
                "single": "-379443138167884557",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1527264955344753330": {
            "length": 80,
            "waveforms": {
                "single": "-1527264955344753330",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4853766678858879789": {
            "length": 80,
            "waveforms": {
                "single": "4853766678858879789",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2331172807106103400": {
            "length": 40,
            "waveforms": {
                "I": "2331172807106103400_i",
                "Q": "2331172807106103400_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2474532255331112480": {
            "length": 40,
            "waveforms": {
                "I": "-2474532255331112480_i",
                "Q": "-2474532255331112480_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-743642337624775867": {
            "length": 40,
            "waveforms": {
                "I": "-743642337624775867_i",
                "Q": "-743642337624775867_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "743416409442838828": {
            "length": 40,
            "waveforms": {
                "I": "743416409442838828_i",
                "Q": "743416409442838828_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "8616111466517398356_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8616111466517398356_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4408130845702960000": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3646000921037737192_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "3646000921037737192_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-3235622884554674349_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3235622884554674349_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6612768071789204907_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-6612768071789204907_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-1504732966848337736_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1504732966848337736_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-435194798797033033_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-435194798797033033_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-17674219780723041_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-17674219780723041_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3414815003155103295_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "3414815003155103295_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7160216213021900141": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4905496226484018356": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3300033062742973423": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3022838659326971209": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "670472990564676989": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7766650488615689773": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "173107609783618633": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3089726737766559100": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8101442495594608198": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8322936554793323446": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4956405209163061145": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7926047830913061307": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3403730060823057991": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2692838013886296961": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2471343954687581713": {
            "type": "constant",
            "sample": 0.25,
        },
        "-495078325883130098": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-273584266684414850": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4248733503405588466": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2086403738292507329": {
            "type": "constant",
            "sample": 0.25,
        },
        "5453560239586690952": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "111355949710659534": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "332850008909374782": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6545547006075316693": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8482326864789044360": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1382787879735672872": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6284567176785877497": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5411453845177011771": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1540755347497158933": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7609213533180178634": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9035251443964319329": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1205963340518240508": {
            "type": "constant",
            "sample": 0.25,
        },
        "5890214157532772276": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6992238882543350176": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3185066976300726525": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7067825991597099493": {
            "type": "constant",
            "sample": 0.25,
        },
        "6446500223710405949": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6607298666148275792": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8644259911713572812": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3024268533862856682": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3726454517883805666": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6665156275931086795": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1528694829880638803": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9196049886402189172": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4673732116312185856": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8324366429329208919": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5902274675149292406": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6123768734348007654": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1543586322173542715": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2978731447916460601": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8543022481549889765": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7539677739982101450": {
            "type": "constant",
            "sample": 0.25,
        },
        "-272154392148529377": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3535017514094094274": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8927962697944964149": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2147099355053352734": {
            "type": "constant",
            "sample": 0.25,
        },
        "112785824246545007": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2239579844515749213": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8247349445739574129": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2532039571448427118": {
            "type": "constant",
            "sample": 0.25,
        },
        "6339211477691050769": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5191389660514181996": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2020923792295068367": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-594885881510927672": {
            "type": "constant",
            "sample": 0.25,
        },
        "7610643407716064107": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1990652029865347977": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5602890848966723163": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8416846918791605398": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3405131160963556300": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3183637101764841052": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7498218243330080135": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-985877413761674189": {
            "type": "constant",
            "sample": 0.25,
        },
        "-764383354562958941": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2798696885369766668": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4468826462463805405": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7287911918353665812": {
            "type": "constant",
            "sample": 0.25,
        },
        "-379443138167884557": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1527264955344753330": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4853766678858879789": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2331172807106103400_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2331172807106103400_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2474532255331112480_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2474532255331112480_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-743642337624775867_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-743642337624775867_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "743416409442838828_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "743416409442838828_q": {
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
        "B1/drive_mixer_c58": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_1a6": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_fb9": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_c6d": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_6ec": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_10f": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_3ac": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_d65": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

