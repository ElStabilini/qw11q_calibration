
# Single QUA script generated at 2025-02-16 11:09:12.521129
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
        play("-7903266633412411531", "B1/drive")
        wait(11, "B1/flux")
        play("9074650686778671594", "B1/flux")
        wait(46, "B1/drive")
        play("-7142176004188849662", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-6071207714660530047", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("3612751474428664691", "B2/drive")
        wait(11, "B2/flux")
        play("9074650686778671594", "B2/flux")
        wait(46, "B2/drive")
        play("4373842103652226560", "B2/drive")
        wait(66, "B2/acquisition")
        measure("8696344894637235104", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("-9148531778418367681", "B3/drive")
        wait(11, "B3/flux")
        play("9074650686778671594", "B3/flux")
        wait(46, "B3/drive")
        play("-8387441149194805812", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-6764978735214761240", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("2358530578528768642", "B4/drive")
        wait(11, "B4/flux")
        play("9074650686778671594", "B4/flux")
        wait(46, "B4/drive")
        play("3119621207752330511", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2614849469517341495", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B1/flux")
        play("-7903266633412411531", "B1/drive")
        wait(11, "B1/flux")
        play("2400228582079185602", "B1/flux")
        wait(46, "B1/drive")
        play("-7142176004188849662", "B1/drive")
        wait(66, "B1/acquisition")
        measure("-6071207714660530047", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("3612751474428664691", "B2/drive")
        wait(11, "B2/flux")
        play("2400228582079185602", "B2/flux")
        wait(46, "B2/drive")
        play("4373842103652226560", "B2/drive")
        wait(66, "B2/acquisition")
        measure("8696344894637235104", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("-9148531778418367681", "B3/drive")
        wait(11, "B3/flux")
        play("2400228582079185602", "B3/flux")
        wait(46, "B3/drive")
        play("-8387441149194805812", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-6764978735214761240", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("2358530578528768642", "B4/drive")
        wait(11, "B4/flux")
        play("2400228582079185602", "B4/flux")
        wait(46, "B4/drive")
        play("3119621207752330511", "B4/drive")
        wait(66, "B4/acquisition")
        measure("2614849469517341495", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25501, "B1/drive")
        wait(25001, "B1/acquisition")
        wait(25501, "B3/drive")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25536, "B3/flux")
        wait(25001, "B3/acquisition")
        wait(25536, "B4/flux")
        wait(25001, "B2/acquisition")
        wait(25536, "B1/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("-6071207714660530047_B1|acquisition_shots")
        r2.buffer(2).average().save("8696344894637235104_B2|acquisition_shots")
        r3.buffer(2).average().save("-6764978735214761240_B3|acquisition_shots")
        r4.buffer(2).average().save("2614849469517341495_B4|acquisition_shots")


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
                "3": {},
                "1": {},
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "-7903266633412411531": "-7903266633412411531",
                "-7142176004188849662": "-7142176004188849662",
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
                "-6071207714660530047": "-6071207714660530047_B1/acquisition",
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
                "-9148531778418367681": "-9148531778418367681",
                "-8387441149194805812": "-8387441149194805812",
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
                "2358530578528768642": "2358530578528768642",
                "3119621207752330511": "3119621207752330511",
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
                "2614849469517341495": "2614849469517341495_B4/acquisition",
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
                "3612751474428664691": "3612751474428664691",
                "4373842103652226560": "4373842103652226560",
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
                "-6764978735214761240": "-6764978735214761240_B3/acquisition",
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
                "8696344894637235104": "8696344894637235104_B2/acquisition",
            },
        },
    },
    "pulses": {
        "-7903266633412411531": {
            "length": 40,
            "waveforms": {
                "I": "-7903266633412411531_i",
                "Q": "-7903266633412411531_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7780789716615239335": {
            "length": 16,
            "waveforms": {
                "single": "-7780789716615239335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6071207714660530047_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6347785925942048029_i",
                "Q": "-6347785925942048029_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "3612751474428664691": {
            "length": 40,
            "waveforms": {
                "I": "3612751474428664691_i",
                "Q": "3612751474428664691_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8696344894637235104_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3172406969764016062_i",
                "Q": "3172406969764016062_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-9148531778418367681": {
            "length": 40,
            "waveforms": {
                "I": "-9148531778418367681_i",
                "Q": "-9148531778418367681_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6764978735214761240_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2045913068491318428_i",
                "Q": "-2045913068491318428_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "2358530578528768642": {
            "length": 40,
            "waveforms": {
                "I": "2358530578528768642_i",
                "Q": "2358530578528768642_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2614849469517341495_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "961276906375409108_i",
                "Q": "961276906375409108_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "3713745164420141577": {
            "length": 16,
            "waveforms": {
                "single": "3713745164420141577",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2232006909418713916": {
            "length": 16,
            "waveforms": {
                "single": "2232006909418713916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5361535969413357224": {
            "length": 16,
            "waveforms": {
                "single": "-5361535969413357224",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4891356998484468794": {
            "length": 16,
            "waveforms": {
                "single": "4891356998484468794",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2775998058037081575": {
            "length": 16,
            "waveforms": {
                "single": "-2775998058037081575",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4393991617703410438": {
            "length": 16,
            "waveforms": {
                "single": "4393991617703410438",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4976595753018282840": {
            "length": 16,
            "waveforms": {
                "single": "-4976595753018282840",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4755101693819567592": {
            "length": 16,
            "waveforms": {
                "single": "-4755101693819567592",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5902923510996436365": {
            "length": 16,
            "waveforms": {
                "single": "-5902923510996436365",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4876465506191564882": {
            "length": 16,
            "waveforms": {
                "single": "4876465506191564882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3705163822993269502": {
            "length": 16,
            "waveforms": {
                "single": "-3705163822993269502",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7074225194194731745": {
            "length": 16,
            "waveforms": {
                "single": "7074225194194731745",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5517983294601361981": {
            "length": 16,
            "waveforms": {
                "single": "-5517983294601361981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1749540053232210092": {
            "length": 16,
            "waveforms": {
                "single": "1749540053232210092",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8953265132312937760": {
            "length": 16,
            "waveforms": {
                "single": "-8953265132312937760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3947299741235376955": {
            "length": 20,
            "waveforms": {
                "single": "3947299741235376955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3720055315286173414": {
            "length": 20,
            "waveforms": {
                "single": "-3720055315286173414",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6532837652611652604": {
            "length": 20,
            "waveforms": {
                "single": "6532837652611652604",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6366553488437259066": {
            "length": 20,
            "waveforms": {
                "single": "6366553488437259066",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4332239957630451339": {
            "length": 24,
            "waveforms": {
                "single": "4332239957630451339",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4553734016829166587": {
            "length": 24,
            "waveforms": {
                "single": "4553734016829166587",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1358548520981463575": {
            "length": 24,
            "waveforms": {
                "single": "1358548520981463575",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6751493704832333450": {
            "length": 24,
            "waveforms": {
                "single": "6751493704832333450",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6972987764031048698": {
            "length": 28,
            "waveforms": {
                "single": "6972987764031048698",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2063683168866085692": {
            "length": 28,
            "waveforms": {
                "single": "-2063683168866085692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8814406220612748040": {
            "length": 28,
            "waveforms": {
                "single": "-8814406220612748040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2957915748397317584": {
            "length": 28,
            "waveforms": {
                "single": "2957915748397317584",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "355570578335796419": {
            "length": 32,
            "waveforms": {
                "single": "355570578335796419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4162742484578420070": {
            "length": 32,
            "waveforms": {
                "single": "4162742484578420070",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5588780395362560765": {
            "length": 32,
            "waveforms": {
                "single": "5588780395362560765",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3236414726600266545": {
            "length": 32,
            "waveforms": {
                "single": "3236414726600266545",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8629359910451136420": {
            "length": 36,
            "waveforms": {
                "single": "8629359910451136420",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1035817031619065280": {
            "length": 36,
            "waveforms": {
                "single": "1035817031619065280",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6631538024902485089": {
            "length": 36,
            "waveforms": {
                "single": "-6631538024902485089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3621354942995340929": {
            "length": 36,
            "waveforms": {
                "single": "3621354942995340929",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7451424544688513191": {
            "length": 40,
            "waveforms": {
                "single": "-7451424544688513191",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5819114630998507792": {
            "length": 40,
            "waveforms": {
                "single": "5819114630998507792",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5360106094877471751": {
            "length": 40,
            "waveforms": {
                "single": "-5360106094877471751",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7394419625684279478": {
            "length": 40,
            "waveforms": {
                "single": "-7394419625684279478",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8238368378200389903": {
            "length": 44,
            "waveforms": {
                "single": "8238368378200389903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4599396402524501394": {
            "length": 44,
            "waveforms": {
                "single": "4599396402524501394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4975165878482397367": {
            "length": 44,
            "waveforms": {
                "single": "-4975165878482397367",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4753671819283682119": {
            "length": 44,
            "waveforms": {
                "single": "-4753671819283682119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2777406190479230504": {
            "length": 48,
            "waveforms": {
                "single": "-2777406190479230504",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2555912131280515256": {
            "length": 48,
            "waveforms": {
                "single": "-2555912131280515256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8102091331441752157": {
            "length": 48,
            "waveforms": {
                "single": "-8102091331441752157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2677297685746249090": {
            "length": 48,
            "waveforms": {
                "single": "2677297685746249090",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3891724696767028715": {
            "length": 52,
            "waveforms": {
                "single": "3891724696767028715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4875057373749415953": {
            "length": 52,
            "waveforms": {
                "single": "4875057373749415953",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5096551432948131201": {
            "length": 52,
            "waveforms": {
                "single": "5096551432948131201",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3097299672863594397": {
            "length": 52,
            "waveforms": {
                "single": "-3097299672863594397",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7755901522013886079": {
            "length": 56,
            "waveforms": {
                "single": "7755901522013886079",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1081479417314400087": {
            "length": 56,
            "waveforms": {
                "single": "1081479417314400087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5919223135731489206": {
            "length": 56,
            "waveforms": {
                "single": "-5919223135731489206",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8271588804493783426": {
            "length": 56,
            "waveforms": {
                "single": "-8271588804493783426",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4555163891365052060": {
            "length": 60,
            "waveforms": {
                "single": "4555163891365052060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9091475324279811528": {
            "length": 60,
            "waveforms": {
                "single": "-9091475324279811528",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6752923579368218923": {
            "length": 60,
            "waveforms": {
                "single": "6752923579368218923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7886648588098709042": {
            "length": 60,
            "waveforms": {
                "single": "-7886648588098709042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7665154528899993794": {
            "length": 64,
            "waveforms": {
                "single": "-7665154528899993794",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5311711291695497277": {
            "length": 64,
            "waveforms": {
                "single": "5311711291695497277",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2959345622933203057": {
            "length": 64,
            "waveforms": {
                "single": "2959345622933203057",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6615216658073695704": {
            "length": 64,
            "waveforms": {
                "single": "-6615216658073695704",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-234185023870062585": {
            "length": 68,
            "waveforms": {
                "single": "-234185023870062585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1843597242109519373": {
            "length": 68,
            "waveforms": {
                "single": "-1843597242109519373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3344285839328277441": {
            "length": 68,
            "waveforms": {
                "single": "3344285839328277441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7834934886547702102": {
            "length": 68,
            "waveforms": {
                "single": "-7834934886547702102",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1037246906154950753": {
            "length": 72,
            "waveforms": {
                "single": "1037246906154950753",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5763539586530159552": {
            "length": 72,
            "waveforms": {
                "single": "5763539586530159552",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3235006594158117616": {
            "length": 72,
            "waveforms": {
                "single": "3235006594158117616",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7449994670152627718": {
            "length": 72,
            "waveforms": {
                "single": "-7449994670152627718",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7228500610953912470": {
            "length": 76,
            "waveforms": {
                "single": "-7228500610953912470",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5252234982149460855": {
            "length": 76,
            "waveforms": {
                "single": "-5252234982149460855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5030740922950745607": {
            "length": 76,
            "waveforms": {
                "single": "-5030740922950745607",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3841440869751907248": {
            "length": 76,
            "waveforms": {
                "single": "3841440869751907248",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "202468894076018739": {
            "length": 80,
            "waveforms": {
                "single": "202468894076018739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9074650686778671594": {
            "length": 80,
            "waveforms": {
                "single": "9074650686778671594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2400228582079185602": {
            "length": 80,
            "waveforms": {
                "single": "2400228582079185602",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7142176004188849662": {
            "length": 40,
            "waveforms": {
                "I": "-7142176004188849662_i",
                "Q": "-7142176004188849662_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4373842103652226560": {
            "length": 40,
            "waveforms": {
                "I": "4373842103652226560_i",
                "Q": "4373842103652226560_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8387441149194805812": {
            "length": 40,
            "waveforms": {
                "I": "-8387441149194805812_i",
                "Q": "-8387441149194805812_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3119621207752330511": {
            "length": 40,
            "waveforms": {
                "I": "3119621207752330511_i",
                "Q": "3119621207752330511_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-7903266633412411531_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-7903266633412411531_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-7780789716615239335": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-6347785925942048029_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-6347785925942048029_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3612751474428664691_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "3612751474428664691_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "3172406969764016062_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "3172406969764016062_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-9148531778418367681_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-9148531778418367681_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-2045913068491318428_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-2045913068491318428_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2358530578528768642_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "2358530578528768642_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "961276906375409108_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "961276906375409108_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3713745164420141577": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "2232006909418713916": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-5361535969413357224": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "4891356998484468794": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-2775998058037081575": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "4393991617703410438": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-4976595753018282840": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-4755101693819567592": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-5902923510996436365": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "4876465506191564882": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-3705163822993269502": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "7074225194194731745": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5517983294601361981": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1749540053232210092": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-8953265132312937760": {
            "sample": 0.25,
            "type": "constant",
        },
        "3947299741235376955": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3720055315286173414": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6532837652611652604": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "6366553488437259066": {
            "sample": 0.25,
            "type": "constant",
        },
        "4332239957630451339": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4553734016829166587": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1358548520981463575": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "6751493704832333450": {
            "sample": 0.25,
            "type": "constant",
        },
        "6972987764031048698": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2063683168866085692": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8814406220612748040": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "2957915748397317584": {
            "sample": 0.25,
            "type": "constant",
        },
        "355570578335796419": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4162742484578420070": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5588780395362560765": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "3236414726600266545": {
            "sample": 0.25,
            "type": "constant",
        },
        "8629359910451136420": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1035817031619065280": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6631538024902485089": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "3621354942995340929": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7451424544688513191": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5819114630998507792": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5360106094877471751": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-7394419625684279478": {
            "sample": 0.25,
            "type": "constant",
        },
        "8238368378200389903": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4599396402524501394": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4975165878482397367": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-4753671819283682119": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2777406190479230504": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2555912131280515256": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8102091331441752157": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "2677297685746249090": {
            "sample": 0.25,
            "type": "constant",
        },
        "3891724696767028715": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4875057373749415953": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5096551432948131201": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-3097299672863594397": {
            "sample": 0.25,
            "type": "constant",
        },
        "7755901522013886079": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1081479417314400087": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5919223135731489206": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-8271588804493783426": {
            "sample": 0.25,
            "type": "constant",
        },
        "4555163891365052060": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-9091475324279811528": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6752923579368218923": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-7886648588098709042": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7665154528899993794": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5311711291695497277": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2959345622933203057": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "-6615216658073695704": {
            "sample": 0.25,
            "type": "constant",
        },
        "-234185023870062585": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1843597242109519373": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3344285839328277441": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-7834934886547702102": {
            "sample": 0.25,
            "type": "constant",
        },
        "1037246906154950753": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5763539586530159552": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3235006594158117616": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-7449994670152627718": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7228500610953912470": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5252234982149460855": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5030740922950745607": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "3841440869751907248": {
            "sample": 0.25,
            "type": "constant",
        },
        "202468894076018739": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9074650686778671594": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2400228582079185602": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-7142176004188849662_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-7142176004188849662_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "4373842103652226560_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "4373842103652226560_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-8387441149194805812_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-8387441149194805812_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "3119621207752330511_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "3119621207752330511_q": {
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "9074650686778671594": "9074650686778671594",
                "2400228582079185602": "2400228582079185602",
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
                "-7903266633412411531": "-7903266633412411531",
                "-7142176004188849662": "-7142176004188849662",
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
                "mixer": "B1/drive_mixer_8f6",
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
                "-6071207714660530047": "-6071207714660530047_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_720",
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
                "-9148531778418367681": "-9148531778418367681",
                "-8387441149194805812": "-8387441149194805812",
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
                "mixer": "B3/drive_mixer_185",
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
                "2358530578528768642": "2358530578528768642",
                "3119621207752330511": "3119621207752330511",
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
                "mixer": "B4/drive_mixer_856",
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
                "2614849469517341495": "2614849469517341495_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_e71",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "3612751474428664691": "3612751474428664691",
                "4373842103652226560": "4373842103652226560",
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
                "mixer": "B2/drive_mixer_c93",
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
                "-6764978735214761240": "-6764978735214761240_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_69e",
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
                "8696344894637235104": "8696344894637235104_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_8bf",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "-7903266633412411531": {
            "length": 40,
            "waveforms": {
                "I": "-7903266633412411531_i",
                "Q": "-7903266633412411531_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7780789716615239335": {
            "length": 16,
            "waveforms": {
                "single": "-7780789716615239335",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6071207714660530047_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6347785925942048029_i",
                "Q": "-6347785925942048029_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3612751474428664691": {
            "length": 40,
            "waveforms": {
                "I": "3612751474428664691_i",
                "Q": "3612751474428664691_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8696344894637235104_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3172406969764016062_i",
                "Q": "3172406969764016062_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-9148531778418367681": {
            "length": 40,
            "waveforms": {
                "I": "-9148531778418367681_i",
                "Q": "-9148531778418367681_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6764978735214761240_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2045913068491318428_i",
                "Q": "-2045913068491318428_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "2358530578528768642": {
            "length": 40,
            "waveforms": {
                "I": "2358530578528768642_i",
                "Q": "2358530578528768642_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2614849469517341495_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "961276906375409108_i",
                "Q": "961276906375409108_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3713745164420141577": {
            "length": 16,
            "waveforms": {
                "single": "3713745164420141577",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2232006909418713916": {
            "length": 16,
            "waveforms": {
                "single": "2232006909418713916",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5361535969413357224": {
            "length": 16,
            "waveforms": {
                "single": "-5361535969413357224",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4891356998484468794": {
            "length": 16,
            "waveforms": {
                "single": "4891356998484468794",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2775998058037081575": {
            "length": 16,
            "waveforms": {
                "single": "-2775998058037081575",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4393991617703410438": {
            "length": 16,
            "waveforms": {
                "single": "4393991617703410438",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4976595753018282840": {
            "length": 16,
            "waveforms": {
                "single": "-4976595753018282840",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4755101693819567592": {
            "length": 16,
            "waveforms": {
                "single": "-4755101693819567592",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5902923510996436365": {
            "length": 16,
            "waveforms": {
                "single": "-5902923510996436365",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4876465506191564882": {
            "length": 16,
            "waveforms": {
                "single": "4876465506191564882",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3705163822993269502": {
            "length": 16,
            "waveforms": {
                "single": "-3705163822993269502",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7074225194194731745": {
            "length": 16,
            "waveforms": {
                "single": "7074225194194731745",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5517983294601361981": {
            "length": 16,
            "waveforms": {
                "single": "-5517983294601361981",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1749540053232210092": {
            "length": 16,
            "waveforms": {
                "single": "1749540053232210092",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8953265132312937760": {
            "length": 16,
            "waveforms": {
                "single": "-8953265132312937760",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3947299741235376955": {
            "length": 20,
            "waveforms": {
                "single": "3947299741235376955",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3720055315286173414": {
            "length": 20,
            "waveforms": {
                "single": "-3720055315286173414",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6532837652611652604": {
            "length": 20,
            "waveforms": {
                "single": "6532837652611652604",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6366553488437259066": {
            "length": 20,
            "waveforms": {
                "single": "6366553488437259066",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4332239957630451339": {
            "length": 24,
            "waveforms": {
                "single": "4332239957630451339",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4553734016829166587": {
            "length": 24,
            "waveforms": {
                "single": "4553734016829166587",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1358548520981463575": {
            "length": 24,
            "waveforms": {
                "single": "1358548520981463575",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6751493704832333450": {
            "length": 24,
            "waveforms": {
                "single": "6751493704832333450",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6972987764031048698": {
            "length": 28,
            "waveforms": {
                "single": "6972987764031048698",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2063683168866085692": {
            "length": 28,
            "waveforms": {
                "single": "-2063683168866085692",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8814406220612748040": {
            "length": 28,
            "waveforms": {
                "single": "-8814406220612748040",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2957915748397317584": {
            "length": 28,
            "waveforms": {
                "single": "2957915748397317584",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "355570578335796419": {
            "length": 32,
            "waveforms": {
                "single": "355570578335796419",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4162742484578420070": {
            "length": 32,
            "waveforms": {
                "single": "4162742484578420070",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5588780395362560765": {
            "length": 32,
            "waveforms": {
                "single": "5588780395362560765",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3236414726600266545": {
            "length": 32,
            "waveforms": {
                "single": "3236414726600266545",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8629359910451136420": {
            "length": 36,
            "waveforms": {
                "single": "8629359910451136420",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1035817031619065280": {
            "length": 36,
            "waveforms": {
                "single": "1035817031619065280",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6631538024902485089": {
            "length": 36,
            "waveforms": {
                "single": "-6631538024902485089",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3621354942995340929": {
            "length": 36,
            "waveforms": {
                "single": "3621354942995340929",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7451424544688513191": {
            "length": 40,
            "waveforms": {
                "single": "-7451424544688513191",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5819114630998507792": {
            "length": 40,
            "waveforms": {
                "single": "5819114630998507792",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5360106094877471751": {
            "length": 40,
            "waveforms": {
                "single": "-5360106094877471751",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7394419625684279478": {
            "length": 40,
            "waveforms": {
                "single": "-7394419625684279478",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8238368378200389903": {
            "length": 44,
            "waveforms": {
                "single": "8238368378200389903",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4599396402524501394": {
            "length": 44,
            "waveforms": {
                "single": "4599396402524501394",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4975165878482397367": {
            "length": 44,
            "waveforms": {
                "single": "-4975165878482397367",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4753671819283682119": {
            "length": 44,
            "waveforms": {
                "single": "-4753671819283682119",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2777406190479230504": {
            "length": 48,
            "waveforms": {
                "single": "-2777406190479230504",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2555912131280515256": {
            "length": 48,
            "waveforms": {
                "single": "-2555912131280515256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8102091331441752157": {
            "length": 48,
            "waveforms": {
                "single": "-8102091331441752157",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2677297685746249090": {
            "length": 48,
            "waveforms": {
                "single": "2677297685746249090",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3891724696767028715": {
            "length": 52,
            "waveforms": {
                "single": "3891724696767028715",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4875057373749415953": {
            "length": 52,
            "waveforms": {
                "single": "4875057373749415953",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5096551432948131201": {
            "length": 52,
            "waveforms": {
                "single": "5096551432948131201",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3097299672863594397": {
            "length": 52,
            "waveforms": {
                "single": "-3097299672863594397",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7755901522013886079": {
            "length": 56,
            "waveforms": {
                "single": "7755901522013886079",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1081479417314400087": {
            "length": 56,
            "waveforms": {
                "single": "1081479417314400087",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5919223135731489206": {
            "length": 56,
            "waveforms": {
                "single": "-5919223135731489206",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8271588804493783426": {
            "length": 56,
            "waveforms": {
                "single": "-8271588804493783426",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4555163891365052060": {
            "length": 60,
            "waveforms": {
                "single": "4555163891365052060",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9091475324279811528": {
            "length": 60,
            "waveforms": {
                "single": "-9091475324279811528",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6752923579368218923": {
            "length": 60,
            "waveforms": {
                "single": "6752923579368218923",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7886648588098709042": {
            "length": 60,
            "waveforms": {
                "single": "-7886648588098709042",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7665154528899993794": {
            "length": 64,
            "waveforms": {
                "single": "-7665154528899993794",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5311711291695497277": {
            "length": 64,
            "waveforms": {
                "single": "5311711291695497277",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2959345622933203057": {
            "length": 64,
            "waveforms": {
                "single": "2959345622933203057",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6615216658073695704": {
            "length": 64,
            "waveforms": {
                "single": "-6615216658073695704",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-234185023870062585": {
            "length": 68,
            "waveforms": {
                "single": "-234185023870062585",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1843597242109519373": {
            "length": 68,
            "waveforms": {
                "single": "-1843597242109519373",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3344285839328277441": {
            "length": 68,
            "waveforms": {
                "single": "3344285839328277441",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7834934886547702102": {
            "length": 68,
            "waveforms": {
                "single": "-7834934886547702102",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1037246906154950753": {
            "length": 72,
            "waveforms": {
                "single": "1037246906154950753",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5763539586530159552": {
            "length": 72,
            "waveforms": {
                "single": "5763539586530159552",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3235006594158117616": {
            "length": 72,
            "waveforms": {
                "single": "3235006594158117616",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7449994670152627718": {
            "length": 72,
            "waveforms": {
                "single": "-7449994670152627718",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7228500610953912470": {
            "length": 76,
            "waveforms": {
                "single": "-7228500610953912470",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5252234982149460855": {
            "length": 76,
            "waveforms": {
                "single": "-5252234982149460855",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5030740922950745607": {
            "length": 76,
            "waveforms": {
                "single": "-5030740922950745607",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3841440869751907248": {
            "length": 76,
            "waveforms": {
                "single": "3841440869751907248",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "202468894076018739": {
            "length": 80,
            "waveforms": {
                "single": "202468894076018739",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9074650686778671594": {
            "length": 80,
            "waveforms": {
                "single": "9074650686778671594",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2400228582079185602": {
            "length": 80,
            "waveforms": {
                "single": "2400228582079185602",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7142176004188849662": {
            "length": 40,
            "waveforms": {
                "I": "-7142176004188849662_i",
                "Q": "-7142176004188849662_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4373842103652226560": {
            "length": 40,
            "waveforms": {
                "I": "4373842103652226560_i",
                "Q": "4373842103652226560_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8387441149194805812": {
            "length": 40,
            "waveforms": {
                "I": "-8387441149194805812_i",
                "Q": "-8387441149194805812_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3119621207752330511": {
            "length": 40,
            "waveforms": {
                "I": "3119621207752330511_i",
                "Q": "3119621207752330511_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-7903266633412411531_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7903266633412411531_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7780789716615239335": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6347785925942048029_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-6347785925942048029_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3612751474428664691_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3612751474428664691_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3172406969764016062_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "3172406969764016062_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-9148531778418367681_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9148531778418367681_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2045913068491318428_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-2045913068491318428_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2358530578528768642_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2358530578528768642_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "961276906375409108_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "961276906375409108_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3713745164420141577": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2232006909418713916": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5361535969413357224": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4891356998484468794": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2775998058037081575": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4393991617703410438": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4976595753018282840": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4755101693819567592": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5902923510996436365": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4876465506191564882": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3705163822993269502": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7074225194194731745": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5517983294601361981": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1749540053232210092": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8953265132312937760": {
            "type": "constant",
            "sample": 0.25,
        },
        "3947299741235376955": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3720055315286173414": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6532837652611652604": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6366553488437259066": {
            "type": "constant",
            "sample": 0.25,
        },
        "4332239957630451339": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4553734016829166587": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1358548520981463575": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6751493704832333450": {
            "type": "constant",
            "sample": 0.25,
        },
        "6972987764031048698": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2063683168866085692": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8814406220612748040": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2957915748397317584": {
            "type": "constant",
            "sample": 0.25,
        },
        "355570578335796419": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4162742484578420070": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5588780395362560765": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3236414726600266545": {
            "type": "constant",
            "sample": 0.25,
        },
        "8629359910451136420": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1035817031619065280": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6631538024902485089": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3621354942995340929": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7451424544688513191": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5819114630998507792": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5360106094877471751": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7394419625684279478": {
            "type": "constant",
            "sample": 0.25,
        },
        "8238368378200389903": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4599396402524501394": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4975165878482397367": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4753671819283682119": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2777406190479230504": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2555912131280515256": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8102091331441752157": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2677297685746249090": {
            "type": "constant",
            "sample": 0.25,
        },
        "3891724696767028715": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4875057373749415953": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5096551432948131201": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3097299672863594397": {
            "type": "constant",
            "sample": 0.25,
        },
        "7755901522013886079": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1081479417314400087": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5919223135731489206": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8271588804493783426": {
            "type": "constant",
            "sample": 0.25,
        },
        "4555163891365052060": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9091475324279811528": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6752923579368218923": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7886648588098709042": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7665154528899993794": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5311711291695497277": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2959345622933203057": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6615216658073695704": {
            "type": "constant",
            "sample": 0.25,
        },
        "-234185023870062585": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1843597242109519373": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3344285839328277441": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7834934886547702102": {
            "type": "constant",
            "sample": 0.25,
        },
        "1037246906154950753": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5763539586530159552": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3235006594158117616": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7449994670152627718": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7228500610953912470": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5252234982149460855": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5030740922950745607": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3841440869751907248": {
            "type": "constant",
            "sample": 0.25,
        },
        "202468894076018739": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9074650686778671594": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2400228582079185602": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7142176004188849662_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7142176004188849662_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4373842103652226560_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4373842103652226560_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8387441149194805812_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8387441149194805812_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3119621207752330511_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3119621207752330511_q": {
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
        "B1/drive_mixer_8f6": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_720": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_185": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_856": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_e71": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_c93": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_69e": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_8bf": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

