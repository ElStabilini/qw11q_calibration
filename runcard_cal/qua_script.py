
# Single QUA script generated at 2025-02-16 13:54:14.149733
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
        play("7318835402014553093", "B1/drive")
        wait(11, "B1/flux")
        play("-57411615864139666", "B1/flux")
        wait(46, "B1/drive")
        play("8079926031238114962", "B1/drive")
        wait(66, "B1/acquisition")
        measure("536844321120771997", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("8434377618891647986", "B2/drive")
        wait(11, "B2/flux")
        play("-57411615864139666", "B2/flux")
        wait(46, "B2/drive")
        play("2149438959480353030", "B2/drive")
        wait(66, "B2/acquisition")
        measure("633372160341670920", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("-3883119154127198889", "B3/drive")
        wait(11, "B3/flux")
        play("-57411615864139666", "B3/flux")
        wait(46, "B3/drive")
        play("8278686260171057771", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-8368801070536299864", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("9004654378015110597", "B4/drive")
        wait(11, "B4/flux")
        play("-57411615864139666", "B4/flux")
        wait(46, "B4/drive")
        play("-8680999066470879150", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6620555947837499112", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25001, "B3/acquisition")
        wait(25501, "B1/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25536, "B1/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B4/drive")
        wait(25501, "B3/drive")
        wait(25536, "B4/flux")
        play("7318835402014553093", "B1/drive")
        wait(11, "B1/flux")
        play("6323620018339493453", "B1/flux")
        wait(46, "B1/drive")
        play("8079926031238114962", "B1/drive")
        wait(66, "B1/acquisition")
        measure("536844321120771997", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("8434377618891647986", "B2/drive")
        wait(11, "B2/flux")
        play("6323620018339493453", "B2/flux")
        wait(46, "B2/drive")
        play("2149438959480353030", "B2/drive")
        wait(66, "B2/acquisition")
        measure("633372160341670920", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("-3883119154127198889", "B3/drive")
        wait(11, "B3/flux")
        play("6323620018339493453", "B3/flux")
        wait(46, "B3/drive")
        play("8278686260171057771", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-8368801070536299864", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("9004654378015110597", "B4/drive")
        wait(11, "B4/flux")
        play("6323620018339493453", "B4/flux")
        wait(46, "B4/drive")
        play("-8680999066470879150", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-6620555947837499112", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25001, "B3/acquisition")
        wait(25501, "B1/drive")
        wait(25001, "B4/acquisition")
        wait(25536, "B2/flux")
        wait(25501, "B2/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25536, "B1/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B4/drive")
        wait(25501, "B3/drive")
        wait(25536, "B4/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("536844321120771997_B1|acquisition_shots")
        r2.buffer(2).average().save("633372160341670920_B2|acquisition_shots")
        r3.buffer(2).average().save("-8368801070536299864_B3|acquisition_shots")
        r4.buffer(2).average().save("-6620555947837499112_B4|acquisition_shots")


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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-8368801070536299864": "-8368801070536299864_B3/acquisition",
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
                "7318835402014553093": "7318835402014553093",
                "8079926031238114962": "8079926031238114962",
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
                "-6620555947837499112": "-6620555947837499112_B4/acquisition",
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
                "8434377618891647986": "8434377618891647986",
                "2149438959480353030": "2149438959480353030",
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
                "633372160341670920": "633372160341670920_B2/acquisition",
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
                "536844321120771997": "536844321120771997_B1/acquisition",
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
                "9004654378015110597": "9004654378015110597",
                "-8680999066470879150": "-8680999066470879150",
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
                "-3883119154127198889": "-3883119154127198889",
                "8278686260171057771": "8278686260171057771",
            },
        },
    },
    "pulses": {
        "7318835402014553093": {
            "length": 40,
            "waveforms": {
                "I": "7318835402014553093_i",
                "Q": "7318835402014553093_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1533892054451501021": {
            "length": 16,
            "waveforms": {
                "single": "1533892054451501021",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "536844321120771997_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6284860524556343935_i",
                "Q": "-6284860524556343935_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "8434377618891647986": {
            "length": 40,
            "waveforms": {
                "I": "8434377618891647986_i",
                "Q": "8434377618891647986_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "633372160341670920_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1903114556326265582_i",
                "Q": "1903114556326265582_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-3883119154127198889": {
            "length": 40,
            "waveforms": {
                "I": "-3883119154127198889_i",
                "Q": "-3883119154127198889_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8368801070536299864_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "1034658540683580631_i",
                "Q": "1034658540683580631_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "9004654378015110597": {
            "length": 40,
            "waveforms": {
                "I": "9004654378015110597_i",
                "Q": "9004654378015110597_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6620555947837499112_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "4884668342635716959_i",
                "Q": "4884668342635716959_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4086099323399215109": {
            "length": 16,
            "waveforms": {
                "single": "-4086099323399215109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-278927417156591458": {
            "length": 16,
            "waveforms": {
                "single": "-278927417156591458",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4164756701416744202": {
            "length": 16,
            "waveforms": {
                "single": "4164756701416744202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6065202959181701126": {
            "length": 16,
            "waveforms": {
                "single": "-6065202959181701126",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2140326330045290653": {
            "length": 16,
            "waveforms": {
                "single": "2140326330045290653",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1421466890065517049": {
            "length": 16,
            "waveforms": {
                "single": "1421466890065517049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7373536147072054999": {
            "length": 16,
            "waveforms": {
                "single": "7373536147072054999",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5764123928832598211": {
            "length": 16,
            "waveforms": {
                "single": "5764123928832598211",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8875448238634329754": {
            "length": 16,
            "waveforms": {
                "single": "-8875448238634329754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7449410327850189059": {
            "length": 16,
            "waveforms": {
                "single": "-7449410327850189059",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4974456236431019982": {
            "length": 16,
            "waveforms": {
                "single": "-4974456236431019982",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6456194491432447643": {
            "length": 16,
            "waveforms": {
                "single": "-6456194491432447643",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7604016308609316416": {
            "length": 16,
            "waveforms": {
                "single": "-7604016308609316416",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1222984674405683297": {
            "length": 16,
            "waveforms": {
                "single": "-1222984674405683297",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3299333095684320019": {
            "length": 16,
            "waveforms": {
                "single": "3299333095684320019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8863624129317749183": {
            "length": 20,
            "waveforms": {
                "single": "8863624129317749183",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7219076092214242032": {
            "length": 20,
            "waveforms": {
                "single": "-7219076092214242032",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6997582033015526784": {
            "length": 20,
            "waveforms": {
                "single": "-6997582033015526784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7618907800902220328": {
            "length": 20,
            "waveforms": {
                "single": "-7618907800902220328",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4799822345012359921": {
            "length": 24,
            "waveforms": {
                "single": "-4799822345012359921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4578328285813644673": {
            "length": 24,
            "waveforms": {
                "single": "-4578328285813644673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "433387472014404425": {
            "length": 24,
            "waveforms": {
                "single": "433387472014404425",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "654881531213119673": {
            "length": 24,
            "waveforms": {
                "single": "654881531213119673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8860410820440111452": {
            "length": 28,
            "waveforms": {
                "single": "8860410820440111452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2852641219216286536": {
            "length": 28,
            "waveforms": {
                "single": "2852641219216286536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3074135278415001784": {
            "length": 28,
            "waveforms": {
                "single": "3074135278415001784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8085851036243050882": {
            "length": 28,
            "waveforms": {
                "single": "8085851036243050882",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2155363748239508955": {
            "length": 32,
            "waveforms": {
                "single": "-2155363748239508955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8163133349463333871": {
            "length": 32,
            "waveforms": {
                "single": "-8163133349463333871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7941639290264618623": {
            "length": 32,
            "waveforms": {
                "single": "-7941639290264618623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "263889998962373156": {
            "length": 32,
            "waveforms": {
                "single": "263889998962373156",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1689927909746513851": {
            "length": 36,
            "waveforms": {
                "single": "1689927909746513851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8096245271023745980": {
            "length": 36,
            "waveforms": {
                "single": "-8096245271023745980",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-510669785234687414": {
            "length": 36,
            "waveforms": {
                "single": "-510669785234687414",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2863035453996981634": {
            "length": 36,
            "waveforms": {
                "single": "-2863035453996981634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8483026831847697764": {
            "length": 40,
            "waveforms": {
                "single": "-8483026831847697764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7711305054628671596": {
            "length": 40,
            "waveforms": {
                "single": "-7711305054628671596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8332630822515365140": {
            "length": 40,
            "waveforms": {
                "single": "-8332630822515365140",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2478095237601907250": {
            "length": 40,
            "waveforms": {
                "single": "-2478095237601907250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2256601178403192002": {
            "length": 44,
            "waveforms": {
                "single": "-2256601178403192002",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3866013396642648790": {
            "length": 44,
            "waveforms": {
                "single": "-3866013396642648790",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-58841490400025139": {
            "length": 44,
            "waveforms": {
                "single": "-58841490400025139",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-680167258286718683": {
            "length": 44,
            "waveforms": {
                "single": "-680167258286718683",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8874018364098444281": {
            "length": 48,
            "waveforms": {
                "single": "-8874018364098444281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8652524304899729033": {
            "length": 48,
            "waveforms": {
                "single": "-8652524304899729033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7372128014629906070": {
            "length": 48,
            "waveforms": {
                "single": "7372128014629906070",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7593622073828621318": {
            "length": 48,
            "waveforms": {
                "single": "7593622073828621318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-600229031983104280": {
            "length": 52,
            "waveforms": {
                "single": "-600229031983104280",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1221554799869797824": {
            "length": 52,
            "waveforms": {
                "single": "-1221554799869797824",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2703293054871225485": {
            "length": 52,
            "waveforms": {
                "single": "-2703293054871225485",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "976204888133369039": {
            "length": 52,
            "waveforms": {
                "single": "976204888133369039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1197698947332084287": {
            "length": 56,
            "waveforms": {
                "single": "1197698947332084287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7052234532245542177": {
            "length": 56,
            "waveforms": {
                "single": "7052234532245542177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1002898747649116978": {
            "length": 56,
            "waveforms": {
                "single": "-1002898747649116978",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9196749853460842576": {
            "length": 56,
            "waveforms": {
                "single": "-9196749853460842576",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1582639163727158671": {
            "length": 60,
            "waveforms": {
                "single": "1582639163727158671",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-769726505035135549": {
            "length": 60,
            "waveforms": {
                "single": "-769726505035135549",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6777496106258960465": {
            "length": 60,
            "waveforms": {
                "single": "-6777496106258960465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2970324200016336814": {
            "length": 60,
            "waveforms": {
                "single": "-2970324200016336814",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1544286289232196119": {
            "length": 64,
            "waveforms": {
                "single": "-1544286289232196119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6661242999994795660": {
            "length": 64,
            "waveforms": {
                "single": "6661242999994795660",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "653473398770970744": {
            "length": 64,
            "waveforms": {
                "single": "653473398770970744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "874967457969685992": {
            "length": 64,
            "waveforms": {
                "single": "874967457969685992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9080496747196677771": {
            "length": 68,
            "waveforms": {
                "single": "9080496747196677771",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3534317547035440870": {
            "length": 68,
            "waveforms": {
                "single": "3534317547035440870",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5836269823686252408": {
            "length": 68,
            "waveforms": {
                "single": "-5836269823686252408",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8305936962999617201": {
            "length": 68,
            "waveforms": {
                "single": "8305936962999617201",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1935277821482942636": {
            "length": 72,
            "waveforms": {
                "single": "-1935277821482942636",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1713783762284227388": {
            "length": 72,
            "waveforms": {
                "single": "-1713783762284227388",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8539109205613598630": {
            "length": 72,
            "waveforms": {
                "single": "8539109205613598630",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6214551123526762177": {
            "length": 72,
            "waveforms": {
                "single": "6214551123526762177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6338511510632397365": {
            "length": 76,
            "waveforms": {
                "single": "6338511510632397365",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5717185742745703821": {
            "length": 76,
            "waveforms": {
                "single": "5717185742745703821",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2476665363066021777": {
            "length": 76,
            "waveforms": {
                "single": "-2476665363066021777",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8757765257834279476": {
            "length": 76,
            "waveforms": {
                "single": "8757765257834279476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4579729385954142982": {
            "length": 80,
            "waveforms": {
                "single": "-4579729385954142982",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-57411615864139666": {
            "length": 80,
            "waveforms": {
                "single": "-57411615864139666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6323620018339493453": {
            "length": 80,
            "waveforms": {
                "single": "6323620018339493453",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8079926031238114962": {
            "length": 40,
            "waveforms": {
                "I": "8079926031238114962_i",
                "Q": "8079926031238114962_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2149438959480353030": {
            "length": 40,
            "waveforms": {
                "I": "2149438959480353030_i",
                "Q": "2149438959480353030_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8278686260171057771": {
            "length": 40,
            "waveforms": {
                "I": "8278686260171057771_i",
                "Q": "8278686260171057771_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8680999066470879150": {
            "length": 40,
            "waveforms": {
                "I": "-8680999066470879150_i",
                "Q": "-8680999066470879150_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "7318835402014553093_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "7318835402014553093_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "1533892054451501021": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-6284860524556343935_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-6284860524556343935_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8434377618891647986_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "8434377618891647986_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "1903114556326265582_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "1903114556326265582_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-3883119154127198889_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-3883119154127198889_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "1034658540683580631_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "1034658540683580631_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "9004654378015110597_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "9004654378015110597_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "4884668342635716959_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "4884668342635716959_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4086099323399215109": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-278927417156591458": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "4164756701416744202": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-6065202959181701126": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "2140326330045290653": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "1421466890065517049": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "7373536147072054999": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "5764123928832598211": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-8875448238634329754": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-7449410327850189059": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-4974456236431019982": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-6456194491432447643": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7604016308609316416": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1222984674405683297": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "3299333095684320019": {
            "sample": 0.25,
            "type": "constant",
        },
        "8863624129317749183": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7219076092214242032": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6997582033015526784": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-7618907800902220328": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4799822345012359921": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4578328285813644673": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "433387472014404425": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "654881531213119673": {
            "sample": 0.25,
            "type": "constant",
        },
        "8860410820440111452": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2852641219216286536": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3074135278415001784": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "8085851036243050882": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2155363748239508955": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8163133349463333871": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7941639290264618623": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "263889998962373156": {
            "sample": 0.25,
            "type": "constant",
        },
        "1689927909746513851": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8096245271023745980": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-510669785234687414": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-2863035453996981634": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8483026831847697764": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7711305054628671596": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8332630822515365140": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-2478095237601907250": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2256601178403192002": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3866013396642648790": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-58841490400025139": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-680167258286718683": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8874018364098444281": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8652524304899729033": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7372128014629906070": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "7593622073828621318": {
            "sample": 0.25,
            "type": "constant",
        },
        "-600229031983104280": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1221554799869797824": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2703293054871225485": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "976204888133369039": {
            "sample": 0.25,
            "type": "constant",
        },
        "1197698947332084287": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7052234532245542177": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1002898747649116978": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-9196749853460842576": {
            "sample": 0.25,
            "type": "constant",
        },
        "1582639163727158671": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-769726505035135549": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6777496106258960465": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-2970324200016336814": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1544286289232196119": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6661242999994795660": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "653473398770970744": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "874967457969685992": {
            "sample": 0.25,
            "type": "constant",
        },
        "9080496747196677771": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3534317547035440870": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5836269823686252408": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "8305936962999617201": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1935277821482942636": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1713783762284227388": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8539109205613598630": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "6214551123526762177": {
            "sample": 0.25,
            "type": "constant",
        },
        "6338511510632397365": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5717185742745703821": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2476665363066021777": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "8757765257834279476": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4579729385954142982": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-57411615864139666": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6323620018339493453": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "8079926031238114962_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "8079926031238114962_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "2149438959480353030_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "2149438959480353030_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "8278686260171057771_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "8278686260171057771_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "-8680999066470879150_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-8680999066470879150_q": {
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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-57411615864139666": "-57411615864139666",
                "6323620018339493453": "6323620018339493453",
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
                "-8368801070536299864": "-8368801070536299864_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_2d6",
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
                "7318835402014553093": "7318835402014553093",
                "8079926031238114962": "8079926031238114962",
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
                "mixer": "B1/drive_mixer_f7a",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "-6620555947837499112": "-6620555947837499112_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_63c",
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
                "8434377618891647986": "8434377618891647986",
                "2149438959480353030": "2149438959480353030",
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
                "mixer": "B2/drive_mixer_4e3",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "633372160341670920": "633372160341670920_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_29a",
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
                "536844321120771997": "536844321120771997_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_7b7",
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
                "9004654378015110597": "9004654378015110597",
                "-8680999066470879150": "-8680999066470879150",
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
                "mixer": "B4/drive_mixer_ef1",
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
                "-3883119154127198889": "-3883119154127198889",
                "8278686260171057771": "8278686260171057771",
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
                "mixer": "B3/drive_mixer_c0b",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
        },
    },
    "pulses": {
        "7318835402014553093": {
            "length": 40,
            "waveforms": {
                "I": "7318835402014553093_i",
                "Q": "7318835402014553093_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1533892054451501021": {
            "length": 16,
            "waveforms": {
                "single": "1533892054451501021",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "536844321120771997_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6284860524556343935_i",
                "Q": "-6284860524556343935_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8434377618891647986": {
            "length": 40,
            "waveforms": {
                "I": "8434377618891647986_i",
                "Q": "8434377618891647986_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "633372160341670920_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1903114556326265582_i",
                "Q": "1903114556326265582_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-3883119154127198889": {
            "length": 40,
            "waveforms": {
                "I": "-3883119154127198889_i",
                "Q": "-3883119154127198889_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8368801070536299864_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "1034658540683580631_i",
                "Q": "1034658540683580631_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "9004654378015110597": {
            "length": 40,
            "waveforms": {
                "I": "9004654378015110597_i",
                "Q": "9004654378015110597_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6620555947837499112_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "4884668342635716959_i",
                "Q": "4884668342635716959_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4086099323399215109": {
            "length": 16,
            "waveforms": {
                "single": "-4086099323399215109",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-278927417156591458": {
            "length": 16,
            "waveforms": {
                "single": "-278927417156591458",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4164756701416744202": {
            "length": 16,
            "waveforms": {
                "single": "4164756701416744202",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6065202959181701126": {
            "length": 16,
            "waveforms": {
                "single": "-6065202959181701126",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2140326330045290653": {
            "length": 16,
            "waveforms": {
                "single": "2140326330045290653",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1421466890065517049": {
            "length": 16,
            "waveforms": {
                "single": "1421466890065517049",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7373536147072054999": {
            "length": 16,
            "waveforms": {
                "single": "7373536147072054999",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5764123928832598211": {
            "length": 16,
            "waveforms": {
                "single": "5764123928832598211",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8875448238634329754": {
            "length": 16,
            "waveforms": {
                "single": "-8875448238634329754",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7449410327850189059": {
            "length": 16,
            "waveforms": {
                "single": "-7449410327850189059",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4974456236431019982": {
            "length": 16,
            "waveforms": {
                "single": "-4974456236431019982",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6456194491432447643": {
            "length": 16,
            "waveforms": {
                "single": "-6456194491432447643",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7604016308609316416": {
            "length": 16,
            "waveforms": {
                "single": "-7604016308609316416",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1222984674405683297": {
            "length": 16,
            "waveforms": {
                "single": "-1222984674405683297",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3299333095684320019": {
            "length": 16,
            "waveforms": {
                "single": "3299333095684320019",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8863624129317749183": {
            "length": 20,
            "waveforms": {
                "single": "8863624129317749183",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7219076092214242032": {
            "length": 20,
            "waveforms": {
                "single": "-7219076092214242032",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6997582033015526784": {
            "length": 20,
            "waveforms": {
                "single": "-6997582033015526784",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7618907800902220328": {
            "length": 20,
            "waveforms": {
                "single": "-7618907800902220328",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4799822345012359921": {
            "length": 24,
            "waveforms": {
                "single": "-4799822345012359921",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4578328285813644673": {
            "length": 24,
            "waveforms": {
                "single": "-4578328285813644673",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "433387472014404425": {
            "length": 24,
            "waveforms": {
                "single": "433387472014404425",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "654881531213119673": {
            "length": 24,
            "waveforms": {
                "single": "654881531213119673",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8860410820440111452": {
            "length": 28,
            "waveforms": {
                "single": "8860410820440111452",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2852641219216286536": {
            "length": 28,
            "waveforms": {
                "single": "2852641219216286536",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3074135278415001784": {
            "length": 28,
            "waveforms": {
                "single": "3074135278415001784",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8085851036243050882": {
            "length": 28,
            "waveforms": {
                "single": "8085851036243050882",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2155363748239508955": {
            "length": 32,
            "waveforms": {
                "single": "-2155363748239508955",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8163133349463333871": {
            "length": 32,
            "waveforms": {
                "single": "-8163133349463333871",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7941639290264618623": {
            "length": 32,
            "waveforms": {
                "single": "-7941639290264618623",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "263889998962373156": {
            "length": 32,
            "waveforms": {
                "single": "263889998962373156",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1689927909746513851": {
            "length": 36,
            "waveforms": {
                "single": "1689927909746513851",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8096245271023745980": {
            "length": 36,
            "waveforms": {
                "single": "-8096245271023745980",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-510669785234687414": {
            "length": 36,
            "waveforms": {
                "single": "-510669785234687414",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2863035453996981634": {
            "length": 36,
            "waveforms": {
                "single": "-2863035453996981634",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8483026831847697764": {
            "length": 40,
            "waveforms": {
                "single": "-8483026831847697764",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7711305054628671596": {
            "length": 40,
            "waveforms": {
                "single": "-7711305054628671596",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8332630822515365140": {
            "length": 40,
            "waveforms": {
                "single": "-8332630822515365140",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2478095237601907250": {
            "length": 40,
            "waveforms": {
                "single": "-2478095237601907250",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2256601178403192002": {
            "length": 44,
            "waveforms": {
                "single": "-2256601178403192002",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3866013396642648790": {
            "length": 44,
            "waveforms": {
                "single": "-3866013396642648790",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-58841490400025139": {
            "length": 44,
            "waveforms": {
                "single": "-58841490400025139",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-680167258286718683": {
            "length": 44,
            "waveforms": {
                "single": "-680167258286718683",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8874018364098444281": {
            "length": 48,
            "waveforms": {
                "single": "-8874018364098444281",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8652524304899729033": {
            "length": 48,
            "waveforms": {
                "single": "-8652524304899729033",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7372128014629906070": {
            "length": 48,
            "waveforms": {
                "single": "7372128014629906070",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7593622073828621318": {
            "length": 48,
            "waveforms": {
                "single": "7593622073828621318",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-600229031983104280": {
            "length": 52,
            "waveforms": {
                "single": "-600229031983104280",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1221554799869797824": {
            "length": 52,
            "waveforms": {
                "single": "-1221554799869797824",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2703293054871225485": {
            "length": 52,
            "waveforms": {
                "single": "-2703293054871225485",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "976204888133369039": {
            "length": 52,
            "waveforms": {
                "single": "976204888133369039",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1197698947332084287": {
            "length": 56,
            "waveforms": {
                "single": "1197698947332084287",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7052234532245542177": {
            "length": 56,
            "waveforms": {
                "single": "7052234532245542177",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1002898747649116978": {
            "length": 56,
            "waveforms": {
                "single": "-1002898747649116978",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9196749853460842576": {
            "length": 56,
            "waveforms": {
                "single": "-9196749853460842576",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1582639163727158671": {
            "length": 60,
            "waveforms": {
                "single": "1582639163727158671",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-769726505035135549": {
            "length": 60,
            "waveforms": {
                "single": "-769726505035135549",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6777496106258960465": {
            "length": 60,
            "waveforms": {
                "single": "-6777496106258960465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2970324200016336814": {
            "length": 60,
            "waveforms": {
                "single": "-2970324200016336814",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1544286289232196119": {
            "length": 64,
            "waveforms": {
                "single": "-1544286289232196119",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6661242999994795660": {
            "length": 64,
            "waveforms": {
                "single": "6661242999994795660",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "653473398770970744": {
            "length": 64,
            "waveforms": {
                "single": "653473398770970744",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "874967457969685992": {
            "length": 64,
            "waveforms": {
                "single": "874967457969685992",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9080496747196677771": {
            "length": 68,
            "waveforms": {
                "single": "9080496747196677771",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3534317547035440870": {
            "length": 68,
            "waveforms": {
                "single": "3534317547035440870",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5836269823686252408": {
            "length": 68,
            "waveforms": {
                "single": "-5836269823686252408",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8305936962999617201": {
            "length": 68,
            "waveforms": {
                "single": "8305936962999617201",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1935277821482942636": {
            "length": 72,
            "waveforms": {
                "single": "-1935277821482942636",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1713783762284227388": {
            "length": 72,
            "waveforms": {
                "single": "-1713783762284227388",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8539109205613598630": {
            "length": 72,
            "waveforms": {
                "single": "8539109205613598630",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6214551123526762177": {
            "length": 72,
            "waveforms": {
                "single": "6214551123526762177",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6338511510632397365": {
            "length": 76,
            "waveforms": {
                "single": "6338511510632397365",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5717185742745703821": {
            "length": 76,
            "waveforms": {
                "single": "5717185742745703821",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2476665363066021777": {
            "length": 76,
            "waveforms": {
                "single": "-2476665363066021777",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8757765257834279476": {
            "length": 76,
            "waveforms": {
                "single": "8757765257834279476",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4579729385954142982": {
            "length": 80,
            "waveforms": {
                "single": "-4579729385954142982",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-57411615864139666": {
            "length": 80,
            "waveforms": {
                "single": "-57411615864139666",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6323620018339493453": {
            "length": 80,
            "waveforms": {
                "single": "6323620018339493453",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8079926031238114962": {
            "length": 40,
            "waveforms": {
                "I": "8079926031238114962_i",
                "Q": "8079926031238114962_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2149438959480353030": {
            "length": 40,
            "waveforms": {
                "I": "2149438959480353030_i",
                "Q": "2149438959480353030_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8278686260171057771": {
            "length": 40,
            "waveforms": {
                "I": "8278686260171057771_i",
                "Q": "8278686260171057771_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8680999066470879150": {
            "length": 40,
            "waveforms": {
                "I": "-8680999066470879150_i",
                "Q": "-8680999066470879150_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "7318835402014553093_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7318835402014553093_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1533892054451501021": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6284860524556343935_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-6284860524556343935_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8434377618891647986_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8434377618891647986_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1903114556326265582_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "1903114556326265582_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-3883119154127198889_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3883119154127198889_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1034658540683580631_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "1034658540683580631_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "9004654378015110597_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9004654378015110597_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4884668342635716959_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "4884668342635716959_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4086099323399215109": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-278927417156591458": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4164756701416744202": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6065202959181701126": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2140326330045290653": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1421466890065517049": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7373536147072054999": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5764123928832598211": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8875448238634329754": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7449410327850189059": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4974456236431019982": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6456194491432447643": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7604016308609316416": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1222984674405683297": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3299333095684320019": {
            "type": "constant",
            "sample": 0.25,
        },
        "8863624129317749183": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7219076092214242032": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6997582033015526784": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7618907800902220328": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4799822345012359921": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4578328285813644673": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "433387472014404425": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "654881531213119673": {
            "type": "constant",
            "sample": 0.25,
        },
        "8860410820440111452": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2852641219216286536": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3074135278415001784": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8085851036243050882": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2155363748239508955": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8163133349463333871": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7941639290264618623": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "263889998962373156": {
            "type": "constant",
            "sample": 0.25,
        },
        "1689927909746513851": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8096245271023745980": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-510669785234687414": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2863035453996981634": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8483026831847697764": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7711305054628671596": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8332630822515365140": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2478095237601907250": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2256601178403192002": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3866013396642648790": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-58841490400025139": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-680167258286718683": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8874018364098444281": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8652524304899729033": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7372128014629906070": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7593622073828621318": {
            "type": "constant",
            "sample": 0.25,
        },
        "-600229031983104280": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1221554799869797824": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2703293054871225485": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "976204888133369039": {
            "type": "constant",
            "sample": 0.25,
        },
        "1197698947332084287": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7052234532245542177": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1002898747649116978": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9196749853460842576": {
            "type": "constant",
            "sample": 0.25,
        },
        "1582639163727158671": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-769726505035135549": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6777496106258960465": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2970324200016336814": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1544286289232196119": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6661242999994795660": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "653473398770970744": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "874967457969685992": {
            "type": "constant",
            "sample": 0.25,
        },
        "9080496747196677771": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3534317547035440870": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5836269823686252408": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8305936962999617201": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1935277821482942636": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1713783762284227388": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8539109205613598630": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6214551123526762177": {
            "type": "constant",
            "sample": 0.25,
        },
        "6338511510632397365": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5717185742745703821": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2476665363066021777": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8757765257834279476": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4579729385954142982": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-57411615864139666": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6323620018339493453": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8079926031238114962_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8079926031238114962_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2149438959480353030_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2149438959480353030_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8278686260171057771_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8278686260171057771_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8680999066470879150_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8680999066470879150_q": {
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
        "B3/acquisition_mixer_2d6": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_f7a": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_63c": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_4e3": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_29a": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_7b7": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_ef1": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_c0b": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

