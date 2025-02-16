
# Single QUA script generated at 2025-02-16 11:24:34.402258
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
        play("-1789916736408370659", "B1/drive")
        wait(11, "B1/flux")
        play("-5666427096488438176", "B1/flux")
        wait(46, "B1/drive")
        play("-1028826107184808790", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-2957210059722568004", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("3995526173624882861", "B2/drive")
        wait(11, "B2/flux")
        play("-5666427096488438176", "B2/flux")
        wait(46, "B2/drive")
        play("4756616802848444730", "B2/drive")
        wait(66, "B2/acquisition")
        measure("1537675162482699047", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("-8765757079222149511", "B3/drive")
        wait(11, "B3/flux")
        play("-5666427096488438176", "B3/flux")
        wait(46, "B3/drive")
        play("-8004666449998587642", "B3/drive")
        wait(66, "B3/acquisition")
        measure("271254758138122477", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("2741305277724986812", "B4/drive")
        wait(11, "B4/flux")
        play("-5666427096488438176", "B4/flux")
        wait(46, "B4/drive")
        play("7900753289932916809", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1915330136336830998", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25501, "B2/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25536, "B2/flux")
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25501, "B3/drive")
        wait(25001, "B1/acquisition")
        wait(25536, "B1/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        play("-1789916736408370659", "B1/drive")
        wait(11, "B1/flux")
        play("-5444933037289722928", "B1/flux")
        wait(46, "B1/drive")
        play("-1028826107184808790", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-2957210059722568004", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("3995526173624882861", "B2/drive")
        wait(11, "B2/flux")
        play("-5444933037289722928", "B2/flux")
        wait(46, "B2/drive")
        play("4756616802848444730", "B2/drive")
        wait(66, "B2/acquisition")
        measure("1537675162482699047", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("-8765757079222149511", "B3/drive")
        wait(11, "B3/flux")
        play("-5444933037289722928", "B3/flux")
        wait(46, "B3/drive")
        play("-8004666449998587642", "B3/drive")
        wait(66, "B3/acquisition")
        measure("271254758138122477", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("2741305277724986812", "B4/drive")
        wait(11, "B4/flux")
        play("-5444933037289722928", "B4/flux")
        wait(46, "B4/drive")
        play("7900753289932916809", "B4/drive")
        wait(66, "B4/acquisition")
        measure("1915330136336830998", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25501, "B2/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B4/flux")
        wait(25536, "B2/flux")
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25501, "B3/drive")
        wait(25001, "B1/acquisition")
        wait(25536, "B1/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-2957210059722568004_B1|acquisition_shots")
        r2.buffer(2).average().save("1537675162482699047_B2|acquisition_shots")
        r3.buffer(2).average().save("271254758138122477_B3|acquisition_shots")
        r4.buffer(2).average().save("1915330136336830998_B4|acquisition_shots")


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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "3995526173624882861": "3995526173624882861",
                "4756616802848444730": "4756616802848444730",
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
                "1915330136336830998": "1915330136336830998_B4/acquisition",
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
                "-1789916736408370659": "-1789916736408370659",
                "-1028826107184808790": "-1028826107184808790",
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
                "2741305277724986812": "2741305277724986812",
                "7900753289932916809": "7900753289932916809",
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
                "-8765757079222149511": "-8765757079222149511",
                "-8004666449998587642": "-8004666449998587642",
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
                "-2957210059722568004": "-2957210059722568004_B1/acquisition",
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
                "1537675162482699047": "1537675162482699047_B2/acquisition",
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
                "271254758138122477": "271254758138122477_B3/acquisition",
            },
        },
    },
    "pulses": {
        "-1789916736408370659": {
            "length": 40,
            "waveforms": {
                "I": "-1789916736408370659_i",
                "Q": "-1789916736408370659_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9028823673102040211": {
            "length": 16,
            "waveforms": {
                "single": "9028823673102040211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2957210059722568004_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6652698795110865525_i",
                "Q": "-6652698795110865525_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "3995526173624882861": {
            "length": 40,
            "waveforms": {
                "I": "3995526173624882861_i",
                "Q": "3995526173624882861_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1537675162482699047_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1535276285771743992_i",
                "Q": "1535276285771743992_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-8765757079222149511": {
            "length": 40,
            "waveforms": {
                "I": "-8765757079222149511_i",
                "Q": "-8765757079222149511_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "271254758138122477_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-3731537112855309087_i",
                "Q": "-3731537112855309087_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "2741305277724986812": {
            "length": 40,
            "waveforms": {
                "I": "2741305277724986812_i",
                "Q": "2741305277724986812_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1915330136336830998_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3674010244995786577_i",
                "Q": "3674010244995786577_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4024975216756641530": {
            "length": 16,
            "waveforms": {
                "single": "-4024975216756641530",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7220160712604344542": {
            "length": 16,
            "waveforms": {
                "single": "-7220160712604344542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6998666653405629294": {
            "length": 16,
            "waveforms": {
                "single": "-6998666653405629294",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1144131068492171404": {
            "length": 16,
            "waveforms": {
                "single": "-1144131068492171404",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3468689150579007857": {
            "length": 16,
            "waveforms": {
                "single": "-3468689150579007857",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1053628619510995459": {
            "length": 16,
            "waveforms": {
                "single": "1053628619510995459",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6613726437010554910": {
            "length": 16,
            "waveforms": {
                "single": "-6613726437010554910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6286838436537759805": {
            "length": 16,
            "waveforms": {
                "single": "6286838436537759805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9203457564520700272": {
            "length": 16,
            "waveforms": {
                "single": "9203457564520700272",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4183774413649638600": {
            "length": 16,
            "waveforms": {
                "single": "4183774413649638600",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8706092183739641916": {
            "length": 16,
            "waveforms": {
                "single": "8706092183739641916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1038737127218091547": {
            "length": 16,
            "waveforms": {
                "single": "1038737127218091547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1812317004158920135": {
            "length": 16,
            "waveforms": {
                "single": "-1812317004158920135",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1590822944960204887": {
            "length": 16,
            "waveforms": {
                "single": "-1590822944960204887",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2309682384939978491": {
            "length": 16,
            "waveforms": {
                "single": "-2309682384939978491",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2310169057243104885": {
            "length": 20,
            "waveforms": {
                "single": "2310169057243104885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6987968377246595095": {
            "length": 20,
            "waveforms": {
                "single": "6987968377246595095",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5840146560069726322": {
            "length": 20,
            "waveforms": {
                "single": "5840146560069726322",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6061640619268441570": {
            "length": 20,
            "waveforms": {
                "single": "6061640619268441570",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2695109273638179269": {
            "length": 24,
            "waveforms": {
                "single": "2695109273638179269",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2916603332836894517": {
            "length": 24,
            "waveforms": {
                "single": "2916603332836894517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6380171860195319532": {
            "length": 24,
            "waveforms": {
                "single": "-6380171860195319532",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4954133949411178837": {
            "length": 24,
            "waveforms": {
                "single": "-4954133949411178837",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2479179857992009760": {
            "length": 28,
            "waveforms": {
                "single": "-2479179857992009760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8099171235842725890": {
            "length": 28,
            "waveforms": {
                "single": "-8099171235842725890",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5108739930170306194": {
            "length": 28,
            "waveforms": {
                "single": "-5108739930170306194",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5901411547839559027": {
            "length": 28,
            "waveforms": {
                "single": "-5901411547839559027",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8253777216601853247": {
            "length": 32,
            "waveforms": {
                "single": "-8253777216601853247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1872745582398220128": {
            "length": 32,
            "waveforms": {
                "single": "-1872745582398220128",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2149939985814222342": {
            "length": 32,
            "waveforms": {
                "single": "-2149939985814222342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4502305654576516562": {
            "length": 32,
            "waveforms": {
                "single": "-4502305654576516562",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-822807711571922038": {
            "length": 36,
            "waveforms": {
                "single": "-822807711571922038",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-601313652373206790": {
            "length": 36,
            "waveforms": {
                "single": "-601313652373206790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-878508055789209004": {
            "length": 36,
            "waveforms": {
                "single": "-878508055789209004",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2928663850453414647": {
            "length": 36,
            "waveforms": {
                "single": "2928663850453414647",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7548515292636498023": {
            "length": 40,
            "waveforms": {
                "single": "7548515292636498023",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-216373435978132406": {
            "length": 40,
            "waveforms": {
                "single": "-216373435978132406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5347917597655296758": {
            "length": 40,
            "waveforms": {
                "single": "5347917597655296758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3688753335241837632": {
            "length": 40,
            "waveforms": {
                "single": "-3688753335241837632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3467259276043122384": {
            "length": 44,
            "waveforms": {
                "single": "-3467259276043122384",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1055058494046880932": {
            "length": 44,
            "waveforms": {
                "single": "1055058494046880932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5667856971024323649": {
            "length": 44,
            "waveforms": {
                "single": "-5667856971024323649",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1048005528841240273": {
            "length": 44,
            "waveforms": {
                "single": "-1048005528841240273",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3082319059648048000": {
            "length": 48,
            "waveforms": {
                "single": "-3082319059648048000",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4185204288185524073": {
            "length": 48,
            "waveforms": {
                "single": "4185204288185524073",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8707522058275527389": {
            "length": 48,
            "waveforms": {
                "single": "8707522058275527389",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-663065312446165889": {
            "length": 48,
            "waveforms": {
                "single": "-663065312446165889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3015430981208460109": {
            "length": 52,
            "waveforms": {
                "single": "-3015430981208460109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4570144504580598457": {
            "length": 52,
            "waveforms": {
                "single": "4570144504580598457",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3512796361989518465": {
            "length": 52,
            "waveforms": {
                "single": "-3512796361989518465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3789990765405520679": {
            "length": 52,
            "waveforms": {
                "single": "-3789990765405520679",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6989398251782480568": {
            "length": 56,
            "waveforms": {
                "single": "6989398251782480568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6935028051837067732": {
            "length": 56,
            "waveforms": {
                "single": "-6935028051837067732",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3918173143040412744": {
            "length": 56,
            "waveforms": {
                "single": "3918173143040412744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6834792271023353211": {
            "length": 56,
            "waveforms": {
                "single": "6834792271023353211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8260830181807493906": {
            "length": 60,
            "waveforms": {
                "single": "8260830181807493906",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6378741985659434059": {
            "length": 60,
            "waveforms": {
                "single": "-6378741985659434059",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1856424215569430743": {
            "length": 60,
            "waveforms": {
                "single": "-1856424215569430743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4180982297656267196": {
            "length": 60,
            "waveforms": {
                "single": "-4180982297656267196",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8645770398202568290": {
            "length": 64,
            "waveforms": {
                "single": "8645770398202568290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1052227519370497150": {
            "length": 64,
            "waveforms": {
                "single": "1052227519370497150",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1273721578569212398": {
            "length": 64,
            "waveforms": {
                "single": "1273721578569212398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4092807034459072805": {
            "length": 64,
            "waveforms": {
                "single": "4092807034459072805",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3471481266572379261": {
            "length": 68,
            "waveforms": {
                "single": "3471481266572379261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4722369839239346337": {
            "length": 68,
            "waveforms": {
                "single": "-4722369839239346337",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1658661794964286782": {
            "length": 68,
            "waveforms": {
                "single": "1658661794964286782",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5122201547927324633": {
            "length": 68,
            "waveforms": {
                "single": "-5122201547927324633",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2303116092037464226": {
            "length": 72,
            "waveforms": {
                "single": "-2303116092037464226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4077915542166168893": {
            "length": 72,
            "waveforms": {
                "single": "4077915542166168893",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2930093724989300120": {
            "length": 72,
            "waveforms": {
                "single": "2930093724989300120",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4737261331532250249": {
            "length": 72,
            "waveforms": {
                "single": "-4737261331532250249",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5127853412992466983": {
            "length": 76,
            "waveforms": {
                "single": "5127853412992466983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5349347472191182231": {
            "length": 76,
            "waveforms": {
                "single": "5349347472191182231",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9156519378433805882": {
            "length": 76,
            "waveforms": {
                "single": "9156519378433805882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7864186784491605039": {
            "length": 76,
            "waveforms": {
                "single": "-7864186784491605039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7768601219393064342": {
            "length": 80,
            "waveforms": {
                "single": "7768601219393064342",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5666427096488438176": {
            "length": 80,
            "waveforms": {
                "single": "-5666427096488438176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5444933037289722928": {
            "length": 80,
            "waveforms": {
                "single": "-5444933037289722928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1028826107184808790": {
            "length": 40,
            "waveforms": {
                "I": "-1028826107184808790_i",
                "Q": "-1028826107184808790_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4756616802848444730": {
            "length": 40,
            "waveforms": {
                "I": "4756616802848444730_i",
                "Q": "4756616802848444730_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8004666449998587642": {
            "length": 40,
            "waveforms": {
                "I": "-8004666449998587642_i",
                "Q": "-8004666449998587642_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7900753289932916809": {
            "length": 40,
            "waveforms": {
                "I": "7900753289932916809_i",
                "Q": "7900753289932916809_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1789916736408370659_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-1789916736408370659_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "9028823673102040211": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-6652698795110865525_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-6652698795110865525_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3995526173624882861_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "3995526173624882861_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "1535276285771743992_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "1535276285771743992_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8765757079222149511_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-8765757079222149511_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-3731537112855309087_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-3731537112855309087_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2741305277724986812_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "2741305277724986812_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "3674010244995786577_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "3674010244995786577_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4024975216756641530": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-7220160712604344542": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-6998666653405629294": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-1144131068492171404": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-3468689150579007857": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "1053628619510995459": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-6613726437010554910": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "6286838436537759805": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "9203457564520700272": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "4183774413649638600": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "8706092183739641916": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "1038737127218091547": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1812317004158920135": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1590822944960204887": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-2309682384939978491": {
            "sample": 0.25,
            "type": "constant",
        },
        "2310169057243104885": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6987968377246595095": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5840146560069726322": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "6061640619268441570": {
            "sample": 0.25,
            "type": "constant",
        },
        "2695109273638179269": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2916603332836894517": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6380171860195319532": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-4954133949411178837": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2479179857992009760": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8099171235842725890": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5108739930170306194": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-5901411547839559027": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8253777216601853247": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1872745582398220128": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2149939985814222342": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-4502305654576516562": {
            "sample": 0.25,
            "type": "constant",
        },
        "-822807711571922038": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-601313652373206790": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-878508055789209004": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "2928663850453414647": {
            "sample": 0.25,
            "type": "constant",
        },
        "7548515292636498023": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-216373435978132406": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5347917597655296758": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-3688753335241837632": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3467259276043122384": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1055058494046880932": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5667856971024323649": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-1048005528841240273": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3082319059648048000": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4185204288185524073": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8707522058275527389": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-663065312446165889": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3015430981208460109": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4570144504580598457": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3512796361989518465": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-3789990765405520679": {
            "sample": 0.25,
            "type": "constant",
        },
        "6989398251782480568": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6935028051837067732": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3918173143040412744": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "6834792271023353211": {
            "sample": 0.25,
            "type": "constant",
        },
        "8260830181807493906": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6378741985659434059": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1856424215569430743": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-4180982297656267196": {
            "sample": 0.25,
            "type": "constant",
        },
        "8645770398202568290": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1052227519370497150": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1273721578569212398": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "4092807034459072805": {
            "sample": 0.25,
            "type": "constant",
        },
        "3471481266572379261": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4722369839239346337": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1658661794964286782": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-5122201547927324633": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2303116092037464226": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4077915542166168893": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2930093724989300120": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-4737261331532250249": {
            "sample": 0.25,
            "type": "constant",
        },
        "5127853412992466983": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5349347472191182231": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9156519378433805882": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-7864186784491605039": {
            "sample": 0.25,
            "type": "constant",
        },
        "7768601219393064342": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5666427096488438176": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5444933037289722928": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-1028826107184808790_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-1028826107184808790_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "4756616802848444730_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "4756616802848444730_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-8004666449998587642_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-8004666449998587642_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "7900753289932916809_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "7900753289932916809_q": {
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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "-5666427096488438176": "-5666427096488438176",
                "-5444933037289722928": "-5444933037289722928",
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
                "3995526173624882861": "3995526173624882861",
                "4756616802848444730": "4756616802848444730",
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
                "mixer": "B2/drive_mixer_bd3",
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
                "1915330136336830998": "1915330136336830998_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_84c",
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
                "-1789916736408370659": "-1789916736408370659",
                "-1028826107184808790": "-1028826107184808790",
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
                "mixer": "B1/drive_mixer_382",
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
                "2741305277724986812": "2741305277724986812",
                "7900753289932916809": "7900753289932916809",
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
                "mixer": "B4/drive_mixer_fde",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "-8765757079222149511": "-8765757079222149511",
                "-8004666449998587642": "-8004666449998587642",
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
                "mixer": "B3/drive_mixer_47b",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-2957210059722568004": "-2957210059722568004_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_cfd",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "1537675162482699047": "1537675162482699047_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_d49",
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
                "271254758138122477": "271254758138122477_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_924",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
        },
    },
    "pulses": {
        "-1789916736408370659": {
            "length": 40,
            "waveforms": {
                "I": "-1789916736408370659_i",
                "Q": "-1789916736408370659_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9028823673102040211": {
            "length": 16,
            "waveforms": {
                "single": "9028823673102040211",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2957210059722568004_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6652698795110865525_i",
                "Q": "-6652698795110865525_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3995526173624882861": {
            "length": 40,
            "waveforms": {
                "I": "3995526173624882861_i",
                "Q": "3995526173624882861_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1537675162482699047_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1535276285771743992_i",
                "Q": "1535276285771743992_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-8765757079222149511": {
            "length": 40,
            "waveforms": {
                "I": "-8765757079222149511_i",
                "Q": "-8765757079222149511_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "271254758138122477_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-3731537112855309087_i",
                "Q": "-3731537112855309087_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "2741305277724986812": {
            "length": 40,
            "waveforms": {
                "I": "2741305277724986812_i",
                "Q": "2741305277724986812_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1915330136336830998_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3674010244995786577_i",
                "Q": "3674010244995786577_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4024975216756641530": {
            "length": 16,
            "waveforms": {
                "single": "-4024975216756641530",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7220160712604344542": {
            "length": 16,
            "waveforms": {
                "single": "-7220160712604344542",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6998666653405629294": {
            "length": 16,
            "waveforms": {
                "single": "-6998666653405629294",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1144131068492171404": {
            "length": 16,
            "waveforms": {
                "single": "-1144131068492171404",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3468689150579007857": {
            "length": 16,
            "waveforms": {
                "single": "-3468689150579007857",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1053628619510995459": {
            "length": 16,
            "waveforms": {
                "single": "1053628619510995459",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6613726437010554910": {
            "length": 16,
            "waveforms": {
                "single": "-6613726437010554910",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6286838436537759805": {
            "length": 16,
            "waveforms": {
                "single": "6286838436537759805",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9203457564520700272": {
            "length": 16,
            "waveforms": {
                "single": "9203457564520700272",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4183774413649638600": {
            "length": 16,
            "waveforms": {
                "single": "4183774413649638600",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8706092183739641916": {
            "length": 16,
            "waveforms": {
                "single": "8706092183739641916",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1038737127218091547": {
            "length": 16,
            "waveforms": {
                "single": "1038737127218091547",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1812317004158920135": {
            "length": 16,
            "waveforms": {
                "single": "-1812317004158920135",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1590822944960204887": {
            "length": 16,
            "waveforms": {
                "single": "-1590822944960204887",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2309682384939978491": {
            "length": 16,
            "waveforms": {
                "single": "-2309682384939978491",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2310169057243104885": {
            "length": 20,
            "waveforms": {
                "single": "2310169057243104885",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6987968377246595095": {
            "length": 20,
            "waveforms": {
                "single": "6987968377246595095",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5840146560069726322": {
            "length": 20,
            "waveforms": {
                "single": "5840146560069726322",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6061640619268441570": {
            "length": 20,
            "waveforms": {
                "single": "6061640619268441570",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2695109273638179269": {
            "length": 24,
            "waveforms": {
                "single": "2695109273638179269",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2916603332836894517": {
            "length": 24,
            "waveforms": {
                "single": "2916603332836894517",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6380171860195319532": {
            "length": 24,
            "waveforms": {
                "single": "-6380171860195319532",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4954133949411178837": {
            "length": 24,
            "waveforms": {
                "single": "-4954133949411178837",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2479179857992009760": {
            "length": 28,
            "waveforms": {
                "single": "-2479179857992009760",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8099171235842725890": {
            "length": 28,
            "waveforms": {
                "single": "-8099171235842725890",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5108739930170306194": {
            "length": 28,
            "waveforms": {
                "single": "-5108739930170306194",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5901411547839559027": {
            "length": 28,
            "waveforms": {
                "single": "-5901411547839559027",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8253777216601853247": {
            "length": 32,
            "waveforms": {
                "single": "-8253777216601853247",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1872745582398220128": {
            "length": 32,
            "waveforms": {
                "single": "-1872745582398220128",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2149939985814222342": {
            "length": 32,
            "waveforms": {
                "single": "-2149939985814222342",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4502305654576516562": {
            "length": 32,
            "waveforms": {
                "single": "-4502305654576516562",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-822807711571922038": {
            "length": 36,
            "waveforms": {
                "single": "-822807711571922038",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-601313652373206790": {
            "length": 36,
            "waveforms": {
                "single": "-601313652373206790",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-878508055789209004": {
            "length": 36,
            "waveforms": {
                "single": "-878508055789209004",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2928663850453414647": {
            "length": 36,
            "waveforms": {
                "single": "2928663850453414647",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7548515292636498023": {
            "length": 40,
            "waveforms": {
                "single": "7548515292636498023",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-216373435978132406": {
            "length": 40,
            "waveforms": {
                "single": "-216373435978132406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5347917597655296758": {
            "length": 40,
            "waveforms": {
                "single": "5347917597655296758",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3688753335241837632": {
            "length": 40,
            "waveforms": {
                "single": "-3688753335241837632",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3467259276043122384": {
            "length": 44,
            "waveforms": {
                "single": "-3467259276043122384",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1055058494046880932": {
            "length": 44,
            "waveforms": {
                "single": "1055058494046880932",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5667856971024323649": {
            "length": 44,
            "waveforms": {
                "single": "-5667856971024323649",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1048005528841240273": {
            "length": 44,
            "waveforms": {
                "single": "-1048005528841240273",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3082319059648048000": {
            "length": 48,
            "waveforms": {
                "single": "-3082319059648048000",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4185204288185524073": {
            "length": 48,
            "waveforms": {
                "single": "4185204288185524073",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8707522058275527389": {
            "length": 48,
            "waveforms": {
                "single": "8707522058275527389",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-663065312446165889": {
            "length": 48,
            "waveforms": {
                "single": "-663065312446165889",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3015430981208460109": {
            "length": 52,
            "waveforms": {
                "single": "-3015430981208460109",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4570144504580598457": {
            "length": 52,
            "waveforms": {
                "single": "4570144504580598457",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3512796361989518465": {
            "length": 52,
            "waveforms": {
                "single": "-3512796361989518465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3789990765405520679": {
            "length": 52,
            "waveforms": {
                "single": "-3789990765405520679",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6989398251782480568": {
            "length": 56,
            "waveforms": {
                "single": "6989398251782480568",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6935028051837067732": {
            "length": 56,
            "waveforms": {
                "single": "-6935028051837067732",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3918173143040412744": {
            "length": 56,
            "waveforms": {
                "single": "3918173143040412744",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6834792271023353211": {
            "length": 56,
            "waveforms": {
                "single": "6834792271023353211",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8260830181807493906": {
            "length": 60,
            "waveforms": {
                "single": "8260830181807493906",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6378741985659434059": {
            "length": 60,
            "waveforms": {
                "single": "-6378741985659434059",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1856424215569430743": {
            "length": 60,
            "waveforms": {
                "single": "-1856424215569430743",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4180982297656267196": {
            "length": 60,
            "waveforms": {
                "single": "-4180982297656267196",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8645770398202568290": {
            "length": 64,
            "waveforms": {
                "single": "8645770398202568290",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1052227519370497150": {
            "length": 64,
            "waveforms": {
                "single": "1052227519370497150",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1273721578569212398": {
            "length": 64,
            "waveforms": {
                "single": "1273721578569212398",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4092807034459072805": {
            "length": 64,
            "waveforms": {
                "single": "4092807034459072805",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3471481266572379261": {
            "length": 68,
            "waveforms": {
                "single": "3471481266572379261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4722369839239346337": {
            "length": 68,
            "waveforms": {
                "single": "-4722369839239346337",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1658661794964286782": {
            "length": 68,
            "waveforms": {
                "single": "1658661794964286782",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5122201547927324633": {
            "length": 68,
            "waveforms": {
                "single": "-5122201547927324633",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2303116092037464226": {
            "length": 72,
            "waveforms": {
                "single": "-2303116092037464226",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4077915542166168893": {
            "length": 72,
            "waveforms": {
                "single": "4077915542166168893",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2930093724989300120": {
            "length": 72,
            "waveforms": {
                "single": "2930093724989300120",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4737261331532250249": {
            "length": 72,
            "waveforms": {
                "single": "-4737261331532250249",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5127853412992466983": {
            "length": 76,
            "waveforms": {
                "single": "5127853412992466983",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5349347472191182231": {
            "length": 76,
            "waveforms": {
                "single": "5349347472191182231",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9156519378433805882": {
            "length": 76,
            "waveforms": {
                "single": "9156519378433805882",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7864186784491605039": {
            "length": 76,
            "waveforms": {
                "single": "-7864186784491605039",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7768601219393064342": {
            "length": 80,
            "waveforms": {
                "single": "7768601219393064342",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5666427096488438176": {
            "length": 80,
            "waveforms": {
                "single": "-5666427096488438176",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5444933037289722928": {
            "length": 80,
            "waveforms": {
                "single": "-5444933037289722928",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1028826107184808790": {
            "length": 40,
            "waveforms": {
                "I": "-1028826107184808790_i",
                "Q": "-1028826107184808790_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4756616802848444730": {
            "length": 40,
            "waveforms": {
                "I": "4756616802848444730_i",
                "Q": "4756616802848444730_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8004666449998587642": {
            "length": 40,
            "waveforms": {
                "I": "-8004666449998587642_i",
                "Q": "-8004666449998587642_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7900753289932916809": {
            "length": 40,
            "waveforms": {
                "I": "7900753289932916809_i",
                "Q": "7900753289932916809_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-1789916736408370659_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1789916736408370659_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9028823673102040211": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6652698795110865525_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-6652698795110865525_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3995526173624882861_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3995526173624882861_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1535276285771743992_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "1535276285771743992_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-8765757079222149511_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8765757079222149511_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3731537112855309087_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-3731537112855309087_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2741305277724986812_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2741305277724986812_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3674010244995786577_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "3674010244995786577_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4024975216756641530": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7220160712604344542": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6998666653405629294": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1144131068492171404": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3468689150579007857": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1053628619510995459": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6613726437010554910": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6286838436537759805": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9203457564520700272": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4183774413649638600": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8706092183739641916": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1038737127218091547": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1812317004158920135": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1590822944960204887": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2309682384939978491": {
            "type": "constant",
            "sample": 0.25,
        },
        "2310169057243104885": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6987968377246595095": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5840146560069726322": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6061640619268441570": {
            "type": "constant",
            "sample": 0.25,
        },
        "2695109273638179269": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2916603332836894517": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6380171860195319532": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4954133949411178837": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2479179857992009760": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8099171235842725890": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5108739930170306194": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5901411547839559027": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8253777216601853247": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1872745582398220128": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2149939985814222342": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4502305654576516562": {
            "type": "constant",
            "sample": 0.25,
        },
        "-822807711571922038": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-601313652373206790": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-878508055789209004": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2928663850453414647": {
            "type": "constant",
            "sample": 0.25,
        },
        "7548515292636498023": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-216373435978132406": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5347917597655296758": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3688753335241837632": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3467259276043122384": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1055058494046880932": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5667856971024323649": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1048005528841240273": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3082319059648048000": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4185204288185524073": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8707522058275527389": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-663065312446165889": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3015430981208460109": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4570144504580598457": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3512796361989518465": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3789990765405520679": {
            "type": "constant",
            "sample": 0.25,
        },
        "6989398251782480568": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6935028051837067732": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3918173143040412744": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6834792271023353211": {
            "type": "constant",
            "sample": 0.25,
        },
        "8260830181807493906": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6378741985659434059": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1856424215569430743": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4180982297656267196": {
            "type": "constant",
            "sample": 0.25,
        },
        "8645770398202568290": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1052227519370497150": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1273721578569212398": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4092807034459072805": {
            "type": "constant",
            "sample": 0.25,
        },
        "3471481266572379261": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4722369839239346337": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1658661794964286782": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5122201547927324633": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2303116092037464226": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4077915542166168893": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2930093724989300120": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4737261331532250249": {
            "type": "constant",
            "sample": 0.25,
        },
        "5127853412992466983": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5349347472191182231": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9156519378433805882": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7864186784491605039": {
            "type": "constant",
            "sample": 0.25,
        },
        "7768601219393064342": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5666427096488438176": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5444933037289722928": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1028826107184808790_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1028826107184808790_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4756616802848444730_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4756616802848444730_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8004666449998587642_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8004666449998587642_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7900753289932916809_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7900753289932916809_q": {
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
        "B2/drive_mixer_bd3": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_84c": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_382": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_fde": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_47b": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_cfd": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_d49": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_924": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

