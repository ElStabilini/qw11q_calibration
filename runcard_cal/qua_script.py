
# Single QUA script generated at 2025-02-16 11:02:04.415644
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
        play("893362008407208259", "B1/drive")
        wait(11, "B1/flux")
        play("-6390759631059822260", "B1/flux")
        wait(46, "B1/drive")
        play("6052810020615138256", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-7179551393946811700", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("3139819825332845701", "B2/drive")
        wait(11, "B2/flux")
        play("-6390759631059822260", "B2/flux")
        wait(46, "B2/drive")
        play("3900910454556407570", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-2684666171741544649", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("2665743071190447074", "B3/drive")
        wait(11, "B3/flux")
        play("-6390759631059822260", "B3/flux")
        wait(46, "B3/drive")
        play("3426833700414008943", "B3/drive")
        wait(66, "B3/acquisition")
        measure("2965268474484884688", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("-4273938645571968219", "B4/drive")
        wait(11, "B4/flux")
        play("-6390759631059822260", "B4/flux")
        wait(46, "B4/drive")
        play("-3512848016348406350", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-64446664885669001", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25001, "B2/acquisition")
        wait(25501, "B1/drive")
        wait(25536, "B3/flux")
        wait(25501, "B2/drive")
        wait(25001, "B1/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B3/drive")
        wait(25001, "B4/acquisition")
        play("893362008407208259", "B1/drive")
        wait(11, "B1/flux")
        play("-1202876549622025446", "B1/flux")
        wait(46, "B1/drive")
        play("6052810020615138256", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-7179551393946811700", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("3139819825332845701", "B2/drive")
        wait(11, "B2/flux")
        play("-1202876549622025446", "B2/flux")
        wait(46, "B2/drive")
        play("3900910454556407570", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-2684666171741544649", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("2665743071190447074", "B3/drive")
        wait(11, "B3/flux")
        play("-1202876549622025446", "B3/flux")
        wait(46, "B3/drive")
        play("3426833700414008943", "B3/drive")
        wait(66, "B3/acquisition")
        measure("2965268474484884688", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("-4273938645571968219", "B4/drive")
        wait(11, "B4/flux")
        play("-1202876549622025446", "B4/flux")
        wait(46, "B4/drive")
        play("-3512848016348406350", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-64446664885669001", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25536, "B4/flux")
        wait(25501, "B4/drive")
        wait(25536, "B1/flux")
        wait(25001, "B3/acquisition")
        wait(25001, "B2/acquisition")
        wait(25501, "B1/drive")
        wait(25536, "B3/flux")
        wait(25501, "B2/drive")
        wait(25001, "B1/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B3/drive")
        wait(25001, "B4/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-7179551393946811700_B1|acquisition_shots")
        r2.buffer(2).average().save("-2684666171741544649_B2|acquisition_shots")
        r3.buffer(2).average().save("2965268474484884688_B3|acquisition_shots")
        r4.buffer(2).average().save("-64446664885669001_B4|acquisition_shots")


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
            },
            "digital_outputs": {
                "1": {},
                "3": {},
                "7": {},
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
        "octave2": {
            "connectivity": "con2",
            "RF_outputs": {
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
                "4": {
                    "LO_frequency": 5900000000.0,
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
    },
    "elements": {
        "B1/flux": {
            "singleInput": {
                "port": ('con4', 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
            "intermediate_frequency": 109615374.0,
            "operations": {
                "-4273938645571968219": "-4273938645571968219",
                "-3512848016348406350": "-3512848016348406350",
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
                "2965268474484884688": "2965268474484884688_B3/acquisition",
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
                "-2684666171741544649": "-2684666171741544649_B2/acquisition",
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
                "893362008407208259": "893362008407208259",
                "6052810020615138256": "6052810020615138256",
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
                "3139819825332845701": "3139819825332845701",
                "3900910454556407570": "3900910454556407570",
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
                "-7179551393946811700": "-7179551393946811700_B1/acquisition",
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
                "2665743071190447074": "2665743071190447074",
                "3426833700414008943": "3426833700414008943",
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
                "-64446664885669001": "-64446664885669001_B4/acquisition",
            },
        },
    },
    "pulses": {
        "893362008407208259": {
            "length": 40,
            "waveforms": {
                "I": "893362008407208259_i",
                "Q": "893362008407208259_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3982715360173977618": {
            "length": 16,
            "waveforms": {
                "single": "-3982715360173977618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7179551393946811700_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1217493754677331738_i",
                "Q": "-1217493754677331738_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "3139819825332845701": {
            "length": 40,
            "waveforms": {
                "I": "3139819825332845701_i",
                "Q": "3139819825332845701_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2684666171741544649_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6970481326205277779_i",
                "Q": "6970481326205277779_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "2665743071190447074": {
            "length": 40,
            "waveforms": {
                "I": "2665743071190447074_i",
                "Q": "2665743071190447074_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2965268474484884688_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5298689474512101963_i",
                "Q": "-5298689474512101963_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-4273938645571968219": {
            "length": 40,
            "waveforms": {
                "I": "-4273938645571968219_i",
                "Q": "-4273938645571968219_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-64446664885669001_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6535355557468310896_i",
                "Q": "6535355557468310896_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4259909763589979832": {
            "length": 16,
            "waveforms": {
                "single": "-4259909763589979832",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6612275432352274052": {
            "length": 16,
            "waveforms": {
                "single": "-6612275432352274052",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4069579912742647135": {
            "length": 16,
            "waveforms": {
                "single": "4069579912742647135",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2711283430148964280": {
            "length": 16,
            "waveforms": {
                "single": "-2711283430148964280",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4193021685150391941": {
            "length": 16,
            "waveforms": {
                "single": "-4193021685150391941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "818694072677657157": {
            "length": 16,
            "waveforms": {
                "single": "818694072677657157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1040188131876372405": {
            "length": 16,
            "waveforms": {
                "single": "1040188131876372405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2326343213753889896": {
            "length": 16,
            "waveforms": {
                "single": "-2326343213753889896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3237947819879539268": {
            "length": 16,
            "waveforms": {
                "single": "3237947819879539268",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3459441879078254516": {
            "length": 16,
            "waveforms": {
                "single": "3459441879078254516",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8471157636906303614": {
            "length": 16,
            "waveforms": {
                "single": "8471157636906303614",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5355734994620164626": {
            "length": 16,
            "waveforms": {
                "single": "-5355734994620164626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5326120350474756561": {
            "length": 16,
            "waveforms": {
                "single": "5326120350474756561",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7556332689601365891": {
            "length": 16,
            "waveforms": {
                "single": "-7556332689601365891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2696560278296460127": {
            "length": 16,
            "waveforms": {
                "single": "2696560278296460127",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4970794778225090242": {
            "length": 20,
            "waveforms": {
                "single": "-4970794778225090242",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5882406416652390234": {
            "length": 20,
            "waveforms": {
                "single": "5882406416652390234",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7171392473206291507": {
            "length": 20,
            "waveforms": {
                "single": "-7171392473206291507",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2551541031023208131": {
            "length": 20,
            "waveforms": {
                "single": "-2551541031023208131",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8097720231184445032": {
            "length": 24,
            "waveforms": {
                "single": "-8097720231184445032",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5622766139765275955": {
            "length": 24,
            "waveforms": {
                "single": "-5622766139765275955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5899960543181278169": {
            "length": 24,
            "waveforms": {
                "single": "-5899960543181278169",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4879428474006723078": {
            "length": 24,
            "waveforms": {
                "single": "4879428474006723078",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2527062805244428858": {
            "length": 28,
            "waveforms": {
                "single": "2527062805244428858",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5237825923370201571": {
            "length": 28,
            "waveforms": {
                "single": "-5237825923370201571",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "326465110263227593": {
            "length": 28,
            "waveforms": {
                "single": "326465110263227593",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1752503021047368288": {
            "length": 28,
            "waveforms": {
                "single": "1752503021047368288",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8488711763435191549": {
            "length": 32,
            "waveforms": {
                "single": "-8488711763435191549",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8267217704236476301": {
            "length": 32,
            "waveforms": {
                "single": "-8267217704236476301",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7757434615293158802": {
            "length": 32,
            "waveforms": {
                "single": "7757434615293158802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6069458016233309438": {
            "length": 32,
            "waveforms": {
                "single": "-6069458016233309438",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-214922431319851548": {
            "length": 36,
            "waveforms": {
                "single": "-214922431319851548",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-836248199206545092": {
            "length": 36,
            "waveforms": {
                "single": "-836248199206545092",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3686069570883458224": {
            "length": 36,
            "waveforms": {
                "single": "3686069570883458224",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5684517799838235054": {
            "length": 36,
            "waveforms": {
                "single": "-5684517799838235054",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1583005547995337019": {
            "length": 40,
            "waveforms": {
                "single": "1583005547995337019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6610845557816388579": {
            "length": 40,
            "waveforms": {
                "single": "-6610845557816388579",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-229813923612755460": {
            "length": 40,
            "waveforms": {
                "single": "-229813923612755460",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8811443252797589844": {
            "length": 40,
            "waveforms": {
                "single": "-8811443252797589844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1967945764390411403": {
            "length": 44,
            "waveforms": {
                "single": "1967945764390411403",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "820123947213542630": {
            "length": 44,
            "waveforms": {
                "single": "820123947213542630",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1041618006412257878": {
            "length": 44,
            "waveforms": {
                "single": "1041618006412257878",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8415582592437955374": {
            "length": 44,
            "waveforms": {
                "single": "8415582592437955374",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3239377694415424741": {
            "length": 48,
            "waveforms": {
                "single": "3239377694415424741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8826334745090493756": {
            "length": 48,
            "waveforms": {
                "single": "-8826334745090493756",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1426558222807332262": {
            "length": 48,
            "waveforms": {
                "single": "1426558222807332262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8800522808833029758": {
            "length": 48,
            "waveforms": {
                "single": "8800522808833029758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3624317910810499125": {
            "length": 52,
            "waveforms": {
                "single": "3624317910810499125",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3845811970009214373": {
            "length": 52,
            "waveforms": {
                "single": "3845811970009214373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3747730908822856767": {
            "length": 52,
            "waveforms": {
                "single": "-3747730908822856767",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6043571658012381236": {
            "length": 52,
            "waveforms": {
                "single": "6043571658012381236",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4567617428608884869": {
            "length": 56,
            "waveforms": {
                "single": "-4567617428608884869",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7169962598670406034": {
            "length": 56,
            "waveforms": {
                "single": "-7169962598670406034",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8924415806276851362": {
            "length": 56,
            "waveforms": {
                "single": "8924415806276851362",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2148363681407002758": {
            "length": 56,
            "waveforms": {
                "single": "-2148363681407002758",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7324568579429533391": {
            "length": 60,
            "waveforms": {
                "single": "-7324568579429533391",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7483203518604129716": {
            "length": 60,
            "waveforms": {
                "single": "7483203518604129716",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2091358762402769045": {
            "length": 60,
            "waveforms": {
                "single": "-2091358762402769045",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1869864703204053797": {
            "length": 60,
            "waveforms": {
                "single": "-1869864703204053797",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7877634304427878713": {
            "length": 64,
            "waveforms": {
                "single": "-7877634304427878713",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "327894984799113066": {
            "length": 64,
            "waveforms": {
                "single": "327894984799113066",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3311076990876775443": {
            "length": 64,
            "waveforms": {
                "single": "-3311076990876775443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5561104801825877412": {
            "length": 64,
            "waveforms": {
                "single": "5561104801825877412",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1113317302873608580": {
            "length": 68,
            "waveforms": {
                "single": "-1113317302873608580",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7758864489829044275": {
            "length": 68,
            "waveforms": {
                "single": "7758864489829044275",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7980358549027759523": {
            "length": 68,
            "waveforms": {
                "single": "7980358549027759523",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5946045018220951796": {
            "length": 68,
            "waveforms": {
                "single": "5946045018220951796",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7160472029241731421": {
            "length": 72,
            "waveforms": {
                "single": "7160472029241731421",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-506883027279818948": {
            "length": 72,
            "waveforms": {
                "single": "-506883027279818948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8365298765422833907": {
            "length": 72,
            "waveforms": {
                "single": "8365298765422833907",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8586792824621549155": {
            "length": 72,
            "waveforms": {
                "single": "8586792824621549155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3855302539437888986": {
            "length": 76,
            "waveforms": {
                "single": "-3855302539437888986",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "764548902745194390": {
            "length": 76,
            "waveforms": {
                "single": "764548902745194390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4571720808987818041": {
            "length": 76,
            "waveforms": {
                "single": "4571720808987818041",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1969375638926296876": {
            "length": 76,
            "waveforms": {
                "single": "1969375638926296876",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1214554733037291627": {
            "length": 80,
            "waveforms": {
                "single": "-1214554733037291627",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6390759631059822260": {
            "length": 80,
            "waveforms": {
                "single": "-6390759631059822260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1202876549622025446": {
            "length": 80,
            "waveforms": {
                "single": "-1202876549622025446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6052810020615138256": {
            "length": 40,
            "waveforms": {
                "I": "6052810020615138256_i",
                "Q": "6052810020615138256_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3900910454556407570": {
            "length": 40,
            "waveforms": {
                "I": "3900910454556407570_i",
                "Q": "3900910454556407570_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3426833700414008943": {
            "length": 40,
            "waveforms": {
                "I": "3426833700414008943_i",
                "Q": "3426833700414008943_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3512848016348406350": {
            "length": 40,
            "waveforms": {
                "I": "-3512848016348406350_i",
                "Q": "-3512848016348406350_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "893362008407208259_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "893362008407208259_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-3982715360173977618": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-1217493754677331738_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-1217493754677331738_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3139819825332845701_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "3139819825332845701_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "6970481326205277779_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "6970481326205277779_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2665743071190447074_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "2665743071190447074_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-5298689474512101963_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-5298689474512101963_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4273938645571968219_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-4273938645571968219_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "6535355557468310896_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "6535355557468310896_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4259909763589979832": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-6612275432352274052": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "4069579912742647135": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-2711283430148964280": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-4193021685150391941": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "818694072677657157": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "1040188131876372405": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-2326343213753889896": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "3237947819879539268": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "3459441879078254516": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "8471157636906303614": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-5355734994620164626": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5326120350474756561": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7556332689601365891": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "2696560278296460127": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4970794778225090242": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5882406416652390234": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7171392473206291507": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-2551541031023208131": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8097720231184445032": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5622766139765275955": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5899960543181278169": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "4879428474006723078": {
            "sample": 0.25,
            "type": "constant",
        },
        "2527062805244428858": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5237825923370201571": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "326465110263227593": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "1752503021047368288": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8488711763435191549": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8267217704236476301": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7757434615293158802": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-6069458016233309438": {
            "sample": 0.25,
            "type": "constant",
        },
        "-214922431319851548": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-836248199206545092": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3686069570883458224": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-5684517799838235054": {
            "sample": 0.25,
            "type": "constant",
        },
        "1583005547995337019": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6610845557816388579": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-229813923612755460": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-8811443252797589844": {
            "sample": 0.25,
            "type": "constant",
        },
        "1967945764390411403": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "820123947213542630": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1041618006412257878": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "8415582592437955374": {
            "sample": 0.25,
            "type": "constant",
        },
        "3239377694415424741": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8826334745090493756": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1426558222807332262": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "8800522808833029758": {
            "sample": 0.25,
            "type": "constant",
        },
        "3624317910810499125": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3845811970009214373": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3747730908822856767": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "6043571658012381236": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4567617428608884869": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7169962598670406034": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8924415806276851362": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-2148363681407002758": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7324568579429533391": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7483203518604129716": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2091358762402769045": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-1869864703204053797": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7877634304427878713": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "327894984799113066": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3311076990876775443": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "5561104801825877412": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1113317302873608580": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7758864489829044275": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7980358549027759523": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "5946045018220951796": {
            "sample": 0.25,
            "type": "constant",
        },
        "7160472029241731421": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-506883027279818948": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8365298765422833907": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "8586792824621549155": {
            "sample": 0.25,
            "type": "constant",
        },
        "-3855302539437888986": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "764548902745194390": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4571720808987818041": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "1969375638926296876": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1214554733037291627": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6390759631059822260": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1202876549622025446": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "6052810020615138256_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "6052810020615138256_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "3900910454556407570_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "3900910454556407570_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "3426833700414008943_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "3426833700414008943_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "-3512848016348406350_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-3512848016348406350_q": {
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
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
                "-6390759631059822260": "-6390759631059822260",
                "-1202876549622025446": "-1202876549622025446",
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
                "-4273938645571968219": "-4273938645571968219",
                "-3512848016348406350": "-3512848016348406350",
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
                "mixer": "B4/drive_mixer_6d1",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "2965268474484884688": "2965268474484884688_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_934",
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
                "-2684666171741544649": "-2684666171741544649_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_422",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "893362008407208259": "893362008407208259",
                "6052810020615138256": "6052810020615138256",
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
                "mixer": "B1/drive_mixer_612",
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
                "3139819825332845701": "3139819825332845701",
                "3900910454556407570": "3900910454556407570",
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
                "mixer": "B2/drive_mixer_9a9",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "-7179551393946811700": "-7179551393946811700_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_5c0",
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
                "2665743071190447074": "2665743071190447074",
                "3426833700414008943": "3426833700414008943",
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
                "mixer": "B3/drive_mixer_d64",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-64446664885669001": "-64446664885669001_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_1ed",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "893362008407208259": {
            "length": 40,
            "waveforms": {
                "I": "893362008407208259_i",
                "Q": "893362008407208259_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3982715360173977618": {
            "length": 16,
            "waveforms": {
                "single": "-3982715360173977618",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7179551393946811700_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1217493754677331738_i",
                "Q": "-1217493754677331738_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3139819825332845701": {
            "length": 40,
            "waveforms": {
                "I": "3139819825332845701_i",
                "Q": "3139819825332845701_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2684666171741544649_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6970481326205277779_i",
                "Q": "6970481326205277779_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "2665743071190447074": {
            "length": 40,
            "waveforms": {
                "I": "2665743071190447074_i",
                "Q": "2665743071190447074_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2965268474484884688_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5298689474512101963_i",
                "Q": "-5298689474512101963_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4273938645571968219": {
            "length": 40,
            "waveforms": {
                "I": "-4273938645571968219_i",
                "Q": "-4273938645571968219_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-64446664885669001_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6535355557468310896_i",
                "Q": "6535355557468310896_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4259909763589979832": {
            "length": 16,
            "waveforms": {
                "single": "-4259909763589979832",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6612275432352274052": {
            "length": 16,
            "waveforms": {
                "single": "-6612275432352274052",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4069579912742647135": {
            "length": 16,
            "waveforms": {
                "single": "4069579912742647135",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2711283430148964280": {
            "length": 16,
            "waveforms": {
                "single": "-2711283430148964280",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4193021685150391941": {
            "length": 16,
            "waveforms": {
                "single": "-4193021685150391941",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "818694072677657157": {
            "length": 16,
            "waveforms": {
                "single": "818694072677657157",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1040188131876372405": {
            "length": 16,
            "waveforms": {
                "single": "1040188131876372405",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2326343213753889896": {
            "length": 16,
            "waveforms": {
                "single": "-2326343213753889896",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3237947819879539268": {
            "length": 16,
            "waveforms": {
                "single": "3237947819879539268",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3459441879078254516": {
            "length": 16,
            "waveforms": {
                "single": "3459441879078254516",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8471157636906303614": {
            "length": 16,
            "waveforms": {
                "single": "8471157636906303614",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5355734994620164626": {
            "length": 16,
            "waveforms": {
                "single": "-5355734994620164626",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5326120350474756561": {
            "length": 16,
            "waveforms": {
                "single": "5326120350474756561",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7556332689601365891": {
            "length": 16,
            "waveforms": {
                "single": "-7556332689601365891",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2696560278296460127": {
            "length": 16,
            "waveforms": {
                "single": "2696560278296460127",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4970794778225090242": {
            "length": 20,
            "waveforms": {
                "single": "-4970794778225090242",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5882406416652390234": {
            "length": 20,
            "waveforms": {
                "single": "5882406416652390234",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7171392473206291507": {
            "length": 20,
            "waveforms": {
                "single": "-7171392473206291507",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2551541031023208131": {
            "length": 20,
            "waveforms": {
                "single": "-2551541031023208131",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8097720231184445032": {
            "length": 24,
            "waveforms": {
                "single": "-8097720231184445032",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5622766139765275955": {
            "length": 24,
            "waveforms": {
                "single": "-5622766139765275955",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5899960543181278169": {
            "length": 24,
            "waveforms": {
                "single": "-5899960543181278169",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4879428474006723078": {
            "length": 24,
            "waveforms": {
                "single": "4879428474006723078",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2527062805244428858": {
            "length": 28,
            "waveforms": {
                "single": "2527062805244428858",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5237825923370201571": {
            "length": 28,
            "waveforms": {
                "single": "-5237825923370201571",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "326465110263227593": {
            "length": 28,
            "waveforms": {
                "single": "326465110263227593",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1752503021047368288": {
            "length": 28,
            "waveforms": {
                "single": "1752503021047368288",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8488711763435191549": {
            "length": 32,
            "waveforms": {
                "single": "-8488711763435191549",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8267217704236476301": {
            "length": 32,
            "waveforms": {
                "single": "-8267217704236476301",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7757434615293158802": {
            "length": 32,
            "waveforms": {
                "single": "7757434615293158802",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6069458016233309438": {
            "length": 32,
            "waveforms": {
                "single": "-6069458016233309438",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-214922431319851548": {
            "length": 36,
            "waveforms": {
                "single": "-214922431319851548",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-836248199206545092": {
            "length": 36,
            "waveforms": {
                "single": "-836248199206545092",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3686069570883458224": {
            "length": 36,
            "waveforms": {
                "single": "3686069570883458224",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5684517799838235054": {
            "length": 36,
            "waveforms": {
                "single": "-5684517799838235054",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1583005547995337019": {
            "length": 40,
            "waveforms": {
                "single": "1583005547995337019",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6610845557816388579": {
            "length": 40,
            "waveforms": {
                "single": "-6610845557816388579",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-229813923612755460": {
            "length": 40,
            "waveforms": {
                "single": "-229813923612755460",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8811443252797589844": {
            "length": 40,
            "waveforms": {
                "single": "-8811443252797589844",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1967945764390411403": {
            "length": 44,
            "waveforms": {
                "single": "1967945764390411403",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "820123947213542630": {
            "length": 44,
            "waveforms": {
                "single": "820123947213542630",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1041618006412257878": {
            "length": 44,
            "waveforms": {
                "single": "1041618006412257878",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8415582592437955374": {
            "length": 44,
            "waveforms": {
                "single": "8415582592437955374",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3239377694415424741": {
            "length": 48,
            "waveforms": {
                "single": "3239377694415424741",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8826334745090493756": {
            "length": 48,
            "waveforms": {
                "single": "-8826334745090493756",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1426558222807332262": {
            "length": 48,
            "waveforms": {
                "single": "1426558222807332262",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8800522808833029758": {
            "length": 48,
            "waveforms": {
                "single": "8800522808833029758",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3624317910810499125": {
            "length": 52,
            "waveforms": {
                "single": "3624317910810499125",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3845811970009214373": {
            "length": 52,
            "waveforms": {
                "single": "3845811970009214373",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3747730908822856767": {
            "length": 52,
            "waveforms": {
                "single": "-3747730908822856767",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6043571658012381236": {
            "length": 52,
            "waveforms": {
                "single": "6043571658012381236",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4567617428608884869": {
            "length": 56,
            "waveforms": {
                "single": "-4567617428608884869",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7169962598670406034": {
            "length": 56,
            "waveforms": {
                "single": "-7169962598670406034",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8924415806276851362": {
            "length": 56,
            "waveforms": {
                "single": "8924415806276851362",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2148363681407002758": {
            "length": 56,
            "waveforms": {
                "single": "-2148363681407002758",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7324568579429533391": {
            "length": 60,
            "waveforms": {
                "single": "-7324568579429533391",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7483203518604129716": {
            "length": 60,
            "waveforms": {
                "single": "7483203518604129716",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2091358762402769045": {
            "length": 60,
            "waveforms": {
                "single": "-2091358762402769045",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1869864703204053797": {
            "length": 60,
            "waveforms": {
                "single": "-1869864703204053797",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7877634304427878713": {
            "length": 64,
            "waveforms": {
                "single": "-7877634304427878713",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "327894984799113066": {
            "length": 64,
            "waveforms": {
                "single": "327894984799113066",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3311076990876775443": {
            "length": 64,
            "waveforms": {
                "single": "-3311076990876775443",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5561104801825877412": {
            "length": 64,
            "waveforms": {
                "single": "5561104801825877412",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1113317302873608580": {
            "length": 68,
            "waveforms": {
                "single": "-1113317302873608580",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7758864489829044275": {
            "length": 68,
            "waveforms": {
                "single": "7758864489829044275",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7980358549027759523": {
            "length": 68,
            "waveforms": {
                "single": "7980358549027759523",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5946045018220951796": {
            "length": 68,
            "waveforms": {
                "single": "5946045018220951796",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7160472029241731421": {
            "length": 72,
            "waveforms": {
                "single": "7160472029241731421",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-506883027279818948": {
            "length": 72,
            "waveforms": {
                "single": "-506883027279818948",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8365298765422833907": {
            "length": 72,
            "waveforms": {
                "single": "8365298765422833907",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8586792824621549155": {
            "length": 72,
            "waveforms": {
                "single": "8586792824621549155",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3855302539437888986": {
            "length": 76,
            "waveforms": {
                "single": "-3855302539437888986",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "764548902745194390": {
            "length": 76,
            "waveforms": {
                "single": "764548902745194390",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4571720808987818041": {
            "length": 76,
            "waveforms": {
                "single": "4571720808987818041",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1969375638926296876": {
            "length": 76,
            "waveforms": {
                "single": "1969375638926296876",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1214554733037291627": {
            "length": 80,
            "waveforms": {
                "single": "-1214554733037291627",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6390759631059822260": {
            "length": 80,
            "waveforms": {
                "single": "-6390759631059822260",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1202876549622025446": {
            "length": 80,
            "waveforms": {
                "single": "-1202876549622025446",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6052810020615138256": {
            "length": 40,
            "waveforms": {
                "I": "6052810020615138256_i",
                "Q": "6052810020615138256_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3900910454556407570": {
            "length": 40,
            "waveforms": {
                "I": "3900910454556407570_i",
                "Q": "3900910454556407570_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3426833700414008943": {
            "length": 40,
            "waveforms": {
                "I": "3426833700414008943_i",
                "Q": "3426833700414008943_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3512848016348406350": {
            "length": 40,
            "waveforms": {
                "I": "-3512848016348406350_i",
                "Q": "-3512848016348406350_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "893362008407208259_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "893362008407208259_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3982715360173977618": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1217493754677331738_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-1217493754677331738_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3139819825332845701_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3139819825332845701_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6970481326205277779_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "6970481326205277779_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2665743071190447074_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2665743071190447074_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5298689474512101963_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-5298689474512101963_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4273938645571968219_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4273938645571968219_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6535355557468310896_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "6535355557468310896_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4259909763589979832": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6612275432352274052": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4069579912742647135": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2711283430148964280": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4193021685150391941": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "818694072677657157": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1040188131876372405": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2326343213753889896": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3237947819879539268": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3459441879078254516": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8471157636906303614": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5355734994620164626": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5326120350474756561": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7556332689601365891": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2696560278296460127": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4970794778225090242": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5882406416652390234": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7171392473206291507": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2551541031023208131": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8097720231184445032": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5622766139765275955": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5899960543181278169": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4879428474006723078": {
            "type": "constant",
            "sample": 0.25,
        },
        "2527062805244428858": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5237825923370201571": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "326465110263227593": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1752503021047368288": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8488711763435191549": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8267217704236476301": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7757434615293158802": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6069458016233309438": {
            "type": "constant",
            "sample": 0.25,
        },
        "-214922431319851548": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-836248199206545092": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3686069570883458224": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5684517799838235054": {
            "type": "constant",
            "sample": 0.25,
        },
        "1583005547995337019": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6610845557816388579": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-229813923612755460": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8811443252797589844": {
            "type": "constant",
            "sample": 0.25,
        },
        "1967945764390411403": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "820123947213542630": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1041618006412257878": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8415582592437955374": {
            "type": "constant",
            "sample": 0.25,
        },
        "3239377694415424741": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8826334745090493756": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1426558222807332262": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8800522808833029758": {
            "type": "constant",
            "sample": 0.25,
        },
        "3624317910810499125": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3845811970009214373": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3747730908822856767": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6043571658012381236": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4567617428608884869": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7169962598670406034": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8924415806276851362": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2148363681407002758": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7324568579429533391": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7483203518604129716": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2091358762402769045": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1869864703204053797": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7877634304427878713": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "327894984799113066": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3311076990876775443": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5561104801825877412": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1113317302873608580": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7758864489829044275": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7980358549027759523": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5946045018220951796": {
            "type": "constant",
            "sample": 0.25,
        },
        "7160472029241731421": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-506883027279818948": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8365298765422833907": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8586792824621549155": {
            "type": "constant",
            "sample": 0.25,
        },
        "-3855302539437888986": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "764548902745194390": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4571720808987818041": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1969375638926296876": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1214554733037291627": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6390759631059822260": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1202876549622025446": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6052810020615138256_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6052810020615138256_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3900910454556407570_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3900910454556407570_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3426833700414008943_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3426833700414008943_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3512848016348406350_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3512848016348406350_q": {
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
        "B4/drive_mixer_6d1": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_934": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_422": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_612": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_9a9": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_5c0": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_d64": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_1ed": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

