
# Single QUA script generated at 2025-01-15 08:10:48.883103
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B2/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("-2801073836668835517", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25538, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("2311282418937059119", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25538, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("3829277842256503851", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25537, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("2564262673674617626", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25537, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("4120133706958745881", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25537, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("7628130959065082885", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25537, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("-359567569393755981", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("5840379374230123497", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25001, "B2/acquisition")
        play("-3332521264670444456", "B2/drive")
        wait(11, "B2/flux")
        play("9108247510106471675", "B2/flux")
        wait(51, "B2/drive")
        play("-2571430635446882587", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-6075873721288486511", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25001, "B2/acquisition")
        wait(25000, )
    with stream_processing():
        r1.buffer(9).average().save("-6075873721288486511_B2|acquisition_shots")


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
                        "feedforward": [],
                        "feedback": [],
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
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
            },
            "digital_outputs": {
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
    },
    "octaves": {
        "octave2": {
            "connectivity": "con2",
            "RF_outputs": {
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
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
            "operations": {
                "-2801073836668835517": "-2801073836668835517",
                "2311282418937059119": "2311282418937059119",
                "3829277842256503851": "3829277842256503851",
                "2564262673674617626": "2564262673674617626",
                "4120133706958745881": "4120133706958745881",
                "7628130959065082885": "7628130959065082885",
                "-359567569393755981": "-359567569393755981",
                "5840379374230123497": "5840379374230123497",
                "9108247510106471675": "9108247510106471675",
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
            "operations": {},
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
            "intermediate_frequency": 63692382.0,
            "operations": {
                "-3332521264670444456": "-3332521264670444456",
                "-2571430635446882587": "-2571430635446882587",
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
            "intermediate_frequency": 10073341.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-6075873721288486511": "-6075873721288486511_B2/acquisition",
            },
        },
    },
    "pulses": {
        "-3332521264670444456": {
            "length": 40,
            "waveforms": {
                "I": "-3332521264670444456_i",
                "Q": "-3332521264670444456_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1704241017162025905": {
            "length": 16,
            "waveforms": {
                "single": "1704241017162025905",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6075873721288486511_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5718180174158414151_i",
                "Q": "5718180174158414151_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "2802114369396815230": {
            "length": 16,
            "waveforms": {
                "single": "2802114369396815230",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9047198142888685439": {
            "length": 16,
            "waveforms": {
                "single": "-9047198142888685439",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1825196803110087578": {
            "length": 16,
            "waveforms": {
                "single": "1825196803110087578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6758482513566410310": {
            "length": 16,
            "waveforms": {
                "single": "-6758482513566410310",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6717969064441660087": {
            "length": 16,
            "waveforms": {
                "single": "-6717969064441660087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4569127546996993184": {
            "length": 16,
            "waveforms": {
                "single": "4569127546996993184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5306740759061562458": {
            "length": 16,
            "waveforms": {
                "single": "-5306740759061562458",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7615469105139747265": {
            "length": 16,
            "waveforms": {
                "single": "-7615469105139747265",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5524110644092771715": {
            "length": 16,
            "waveforms": {
                "single": "5524110644092771715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3999602345587742064": {
            "length": 16,
            "waveforms": {
                "single": "3999602345587742064",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1555981769347584681": {
            "length": 16,
            "waveforms": {
                "single": "1555981769347584681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6418360257920614941": {
            "length": 16,
            "waveforms": {
                "single": "6418360257920614941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "330872487648109266": {
            "length": 16,
            "waveforms": {
                "single": "330872487648109266",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8328357440840024066": {
            "length": 16,
            "waveforms": {
                "single": "8328357440840024066",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2161590570169744332": {
            "length": 16,
            "waveforms": {
                "single": "-2161590570169744332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "190617315125354155": {
            "length": 20,
            "waveforms": {
                "single": "190617315125354155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2147595816468150264": {
            "length": 20,
            "waveforms": {
                "single": "2147595816468150264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3110316504597299977": {
            "length": 20,
            "waveforms": {
                "single": "3110316504597299977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4729370284937384535": {
            "length": 20,
            "waveforms": {
                "single": "4729370284937384535",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3210617165699259524": {
            "length": 24,
            "waveforms": {
                "single": "-3210617165699259524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1831259996938650474": {
            "length": 24,
            "waveforms": {
                "single": "1831259996938650474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2611385654996695909": {
            "length": 24,
            "waveforms": {
                "single": "2611385654996695909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7249789689960713619": {
            "length": 24,
            "waveforms": {
                "single": "-7249789689960713619",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6904657848459233734": {
            "length": 28,
            "waveforms": {
                "single": "6904657848459233734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5650792673788335441": {
            "length": 28,
            "waveforms": {
                "single": "-5650792673788335441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5829480971401185754": {
            "length": 28,
            "waveforms": {
                "single": "-5829480971401185754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3838649956939590170": {
            "length": 28,
            "waveforms": {
                "single": "3838649956939590170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5525544834179664944": {
            "length": 32,
            "waveforms": {
                "single": "5525544834179664944",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7736230695892046517": {
            "length": 32,
            "waveforms": {
                "single": "-7736230695892046517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4448577315411839511": {
            "length": 32,
            "waveforms": {
                "single": "4448577315411839511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7855372710141128832": {
            "length": 32,
            "waveforms": {
                "single": "-7855372710141128832",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-702786633209392637": {
            "length": 36,
            "waveforms": {
                "single": "-702786633209392637",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3740424521480665318": {
            "length": 36,
            "waveforms": {
                "single": "3740424521480665318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3347751435961884104": {
            "length": 36,
            "waveforms": {
                "single": "-3347751435961884104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3358498769067318639": {
            "length": 36,
            "waveforms": {
                "single": "3358498769067318639",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7098698821348156696": {
            "length": 40,
            "waveforms": {
                "single": "7098698821348156696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6889819111268589912": {
            "length": 40,
            "waveforms": {
                "single": "6889819111268589912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8878241034758525118": {
            "length": 40,
            "waveforms": {
                "single": "-8878241034758525118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8250694619980911454": {
            "length": 40,
            "waveforms": {
                "single": "-8250694619980911454",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1775479318234511072": {
            "length": 44,
            "waveforms": {
                "single": "1775479318234511072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5651503384411128783": {
            "length": 44,
            "waveforms": {
                "single": "-5651503384411128783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3315660622103041398": {
            "length": 44,
            "waveforms": {
                "single": "-3315660622103041398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5860774496334740329": {
            "length": 44,
            "waveforms": {
                "single": "5860774496334740329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7283091532369879927": {
            "length": 48,
            "waveforms": {
                "single": "7283091532369879927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "432856893697269677": {
            "length": 48,
            "waveforms": {
                "single": "432856893697269677",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9142454174609802680": {
            "length": 48,
            "waveforms": {
                "single": "9142454174609802680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8762711298788080627": {
            "length": 48,
            "waveforms": {
                "single": "-8762711298788080627",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1330300575148032181": {
            "length": 52,
            "waveforms": {
                "single": "1330300575148032181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4943713453491619264": {
            "length": 52,
            "waveforms": {
                "single": "4943713453491619264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5532566609725663212": {
            "length": 52,
            "waveforms": {
                "single": "5532566609725663212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1022622965938373093": {
            "length": 52,
            "waveforms": {
                "single": "-1022622965938373093",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1238688829285665072": {
            "length": 56,
            "waveforms": {
                "single": "1238688829285665072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4143912412909575159": {
            "length": 56,
            "waveforms": {
                "single": "-4143912412909575159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7137335903495984281": {
            "length": 56,
            "waveforms": {
                "single": "7137335903495984281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1845007090635826632": {
            "length": 56,
            "waveforms": {
                "single": "1845007090635826632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6611196219619889944": {
            "length": 60,
            "waveforms": {
                "single": "-6611196219619889944",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4203276962985013985": {
            "length": 60,
            "waveforms": {
                "single": "4203276962985013985",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4520929682105593823": {
            "length": 60,
            "waveforms": {
                "single": "-4520929682105593823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "741475174713494960": {
            "length": 60,
            "waveforms": {
                "single": "741475174713494960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6003762211673235044": {
            "length": 64,
            "waveforms": {
                "single": "-6003762211673235044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-546607530483258957": {
            "length": 64,
            "waveforms": {
                "single": "-546607530483258957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3465480353078342405": {
            "length": 64,
            "waveforms": {
                "single": "3465480353078342405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8471319341955583097": {
            "length": 64,
            "waveforms": {
                "single": "8471319341955583097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8431207786713116744": {
            "length": 68,
            "waveforms": {
                "single": "8431207786713116744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4594584212515581860": {
            "length": 68,
            "waveforms": {
                "single": "4594584212515581860",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1022738293237895902": {
            "length": 68,
            "waveforms": {
                "single": "1022738293237895902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8511364120326059691": {
            "length": 68,
            "waveforms": {
                "single": "-8511364120326059691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7417876328975355008": {
            "length": 72,
            "waveforms": {
                "single": "-7417876328975355008",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2848825808249665226": {
            "length": 72,
            "waveforms": {
                "single": "-2848825808249665226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6536588363730818606": {
            "length": 72,
            "waveforms": {
                "single": "-6536588363730818606",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8322607088264232875": {
            "length": 72,
            "waveforms": {
                "single": "-8322607088264232875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6403984813049691902": {
            "length": 76,
            "waveforms": {
                "single": "-6403984813049691902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6529888274398628136": {
            "length": 76,
            "waveforms": {
                "single": "6529888274398628136",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6756698918981049807": {
            "length": 76,
            "waveforms": {
                "single": "6756698918981049807",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5018324660403355833": {
            "length": 76,
            "waveforms": {
                "single": "5018324660403355833",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2559314455126043254": {
            "length": 80,
            "waveforms": {
                "single": "2559314455126043254",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6214994506865613938": {
            "length": 80,
            "waveforms": {
                "single": "6214994506865613938",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3371302464723107165": {
            "length": 80,
            "waveforms": {
                "single": "3371302464723107165",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1011437984785195405": {
            "length": 80,
            "waveforms": {
                "single": "1011437984785195405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3831822971627865329": {
            "length": 84,
            "waveforms": {
                "single": "-3831822971627865329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2407693383014787308": {
            "length": 84,
            "waveforms": {
                "single": "-2407693383014787308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7075070304125205528": {
            "length": 84,
            "waveforms": {
                "single": "-7075070304125205528",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7752565779924463191": {
            "length": 84,
            "waveforms": {
                "single": "7752565779924463191",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2462222529362097928": {
            "length": 88,
            "waveforms": {
                "single": "-2462222529362097928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4602148255541601755": {
            "length": 88,
            "waveforms": {
                "single": "-4602148255541601755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4910979138670939": {
            "length": 88,
            "waveforms": {
                "single": "-4910979138670939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8492994852230459258": {
            "length": 88,
            "waveforms": {
                "single": "-8492994852230459258",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2299301430927542816": {
            "length": 92,
            "waveforms": {
                "single": "-2299301430927542816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7263800527968564030": {
            "length": 92,
            "waveforms": {
                "single": "-7263800527968564030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2801073836668835517": {
            "length": 92,
            "waveforms": {
                "single": "-2801073836668835517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2311282418937059119": {
            "length": 92,
            "waveforms": {
                "single": "2311282418937059119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3829277842256503851": {
            "length": 96,
            "waveforms": {
                "single": "3829277842256503851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2564262673674617626": {
            "length": 96,
            "waveforms": {
                "single": "2564262673674617626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4120133706958745881": {
            "length": 96,
            "waveforms": {
                "single": "4120133706958745881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7628130959065082885": {
            "length": 96,
            "waveforms": {
                "single": "7628130959065082885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-359567569393755981": {
            "length": 100,
            "waveforms": {
                "single": "-359567569393755981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5840379374230123497": {
            "length": 100,
            "waveforms": {
                "single": "5840379374230123497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9108247510106471675": {
            "length": 100,
            "waveforms": {
                "single": "9108247510106471675",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2571430635446882587": {
            "length": 40,
            "waveforms": {
                "I": "-2571430635446882587_i",
                "Q": "-2571430635446882587_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-3332521264670444456_i": {
            "samples": [0.00020272710178481995, 0.0002588094340347883, 0.0003243334534286107, 0.0003988385361872125, 0.00048108131352079836, 0.0005689086817884582, 0.0006591894461085467, 0.0007478294374550071, 0.0008298901297564485, 0.0008998216167203549, 0.00095180775985842, 0.0009802056987941597, 0.0009800457981846084, 0.0009475440813943577, 0.0008805699560155827, 0.0007790098417747416, 0.0006449735133424266, 0.00048280459894422726, 0.00029887827724257344, 0.00010119497508516105, -0.00010119497508515806, -0.0002988782772425705, -0.00048280459894422444, -0.000644973513342424, -0.000779009841774739, -0.0008805699560155803, -0.0009475440813943555, -0.0009800457981846067, -0.000980205698794158, -0.0009518077598584185, -0.0008998216167203536, -0.0008298901297564475, -0.0007478294374550062, -0.0006591894461085461, -0.0005689086817884575, -0.00048108131352079793, -0.0003988385361872122, -0.00032433345342861036, -0.00025880943403478807, -0.0002027271017848198],
            "type": "arbitrary",
        },
        "-3332521264670444456_q": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
        },
        "1704241017162025905": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5718180174158414151_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5718180174158414151_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2802114369396815230": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-9047198142888685439": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "1825196803110087578": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6758482513566410310": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6717969064441660087": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "4569127546996993184": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5306740759061562458": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-7615469105139747265": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5524110644092771715": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "3999602345587742064": {
            "samples": [0.0] * 10 + [0.25] + [0.0] * 5,
            "type": "arbitrary",
        },
        "1555981769347584681": {
            "samples": [0.0] * 10 + [0.25] * 2 + [0.0] * 4,
            "type": "arbitrary",
        },
        "6418360257920614941": {
            "samples": [0.0] * 10 + [0.25] * 3 + [0.0] * 3,
            "type": "arbitrary",
        },
        "330872487648109266": {
            "samples": [0.0] * 10 + [0.25] * 4 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8328357440840024066": {
            "samples": [0.0] * 10 + [0.25] * 5 + [0.0],
            "type": "arbitrary",
        },
        "-2161590570169744332": {
            "samples": [0.0] * 10 + [0.25] * 6,
            "type": "arbitrary",
        },
        "190617315125354155": {
            "samples": [0.0] * 10 + [0.25] * 7 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2147595816468150264": {
            "samples": [0.0] * 10 + [0.25] * 8 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3110316504597299977": {
            "samples": [0.0] * 10 + [0.25] * 9 + [0.0],
            "type": "arbitrary",
        },
        "4729370284937384535": {
            "samples": [0.0] * 10 + [0.25] * 10,
            "type": "arbitrary",
        },
        "-3210617165699259524": {
            "samples": [0.0] * 10 + [0.25] * 11 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1831259996938650474": {
            "samples": [0.0] * 10 + [0.25] * 12 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2611385654996695909": {
            "samples": [0.0] * 10 + [0.25] * 13 + [0.0],
            "type": "arbitrary",
        },
        "-7249789689960713619": {
            "samples": [0.0] * 10 + [0.25] * 14,
            "type": "arbitrary",
        },
        "6904657848459233734": {
            "samples": [0.0] * 10 + [0.25] * 15 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5650792673788335441": {
            "samples": [0.0] * 10 + [0.25] * 16 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5829480971401185754": {
            "samples": [0.0] * 10 + [0.25] * 17 + [0.0],
            "type": "arbitrary",
        },
        "3838649956939590170": {
            "samples": [0.0] * 10 + [0.25] * 18,
            "type": "arbitrary",
        },
        "5525544834179664944": {
            "samples": [0.0] * 10 + [0.25] * 19 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7736230695892046517": {
            "samples": [0.0] * 10 + [0.25] * 20 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4448577315411839511": {
            "samples": [0.0] * 10 + [0.25] * 21 + [0.0],
            "type": "arbitrary",
        },
        "-7855372710141128832": {
            "samples": [0.0] * 10 + [0.25] * 22,
            "type": "arbitrary",
        },
        "-702786633209392637": {
            "samples": [0.0] * 10 + [0.25] * 23 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3740424521480665318": {
            "samples": [0.0] * 10 + [0.25] * 24 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3347751435961884104": {
            "samples": [0.0] * 10 + [0.25] * 25 + [0.0],
            "type": "arbitrary",
        },
        "3358498769067318639": {
            "samples": [0.0] * 10 + [0.25] * 26,
            "type": "arbitrary",
        },
        "7098698821348156696": {
            "samples": [0.0] * 10 + [0.25] * 27 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6889819111268589912": {
            "samples": [0.0] * 10 + [0.25] * 28 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8878241034758525118": {
            "samples": [0.0] * 10 + [0.25] * 29 + [0.0],
            "type": "arbitrary",
        },
        "-8250694619980911454": {
            "samples": [0.0] * 10 + [0.25] * 30,
            "type": "arbitrary",
        },
        "1775479318234511072": {
            "samples": [0.0] * 10 + [0.25] * 31 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5651503384411128783": {
            "samples": [0.0] * 10 + [0.25] * 32 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3315660622103041398": {
            "samples": [0.0] * 10 + [0.25] * 33 + [0.0],
            "type": "arbitrary",
        },
        "5860774496334740329": {
            "samples": [0.0] * 10 + [0.25] * 34,
            "type": "arbitrary",
        },
        "7283091532369879927": {
            "samples": [0.0] * 10 + [0.25] * 35 + [0.0] * 3,
            "type": "arbitrary",
        },
        "432856893697269677": {
            "samples": [0.0] * 10 + [0.25] * 36 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9142454174609802680": {
            "samples": [0.0] * 10 + [0.25] * 37 + [0.0],
            "type": "arbitrary",
        },
        "-8762711298788080627": {
            "samples": [0.0] * 10 + [0.25] * 38,
            "type": "arbitrary",
        },
        "1330300575148032181": {
            "samples": [0.0] * 10 + [0.25] * 39 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4943713453491619264": {
            "samples": [0.0] * 10 + [0.25] * 40 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5532566609725663212": {
            "samples": [0.0] * 10 + [0.25] * 41 + [0.0],
            "type": "arbitrary",
        },
        "-1022622965938373093": {
            "samples": [0.0] * 10 + [0.25] * 42,
            "type": "arbitrary",
        },
        "1238688829285665072": {
            "samples": [0.0] * 10 + [0.25] * 43 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4143912412909575159": {
            "samples": [0.0] * 10 + [0.25] * 44 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7137335903495984281": {
            "samples": [0.0] * 10 + [0.25] * 45 + [0.0],
            "type": "arbitrary",
        },
        "1845007090635826632": {
            "samples": [0.0] * 10 + [0.25] * 46,
            "type": "arbitrary",
        },
        "-6611196219619889944": {
            "samples": [0.0] * 10 + [0.25] * 47 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4203276962985013985": {
            "samples": [0.0] * 10 + [0.25] * 48 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4520929682105593823": {
            "samples": [0.0] * 10 + [0.25] * 49 + [0.0],
            "type": "arbitrary",
        },
        "741475174713494960": {
            "samples": [0.0] * 10 + [0.25] * 50,
            "type": "arbitrary",
        },
        "-6003762211673235044": {
            "samples": [0.0] * 10 + [0.25] * 51 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-546607530483258957": {
            "samples": [0.0] * 10 + [0.25] * 52 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3465480353078342405": {
            "samples": [0.0] * 10 + [0.25] * 53 + [0.0],
            "type": "arbitrary",
        },
        "8471319341955583097": {
            "samples": [0.0] * 10 + [0.25] * 54,
            "type": "arbitrary",
        },
        "8431207786713116744": {
            "samples": [0.0] * 10 + [0.25] * 55 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4594584212515581860": {
            "samples": [0.0] * 10 + [0.25] * 56 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1022738293237895902": {
            "samples": [0.0] * 10 + [0.25] * 57 + [0.0],
            "type": "arbitrary",
        },
        "-8511364120326059691": {
            "samples": [0.0] * 10 + [0.25] * 58,
            "type": "arbitrary",
        },
        "-7417876328975355008": {
            "samples": [0.0] * 10 + [0.25] * 59 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2848825808249665226": {
            "samples": [0.0] * 10 + [0.25] * 60 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6536588363730818606": {
            "samples": [0.0] * 10 + [0.25] * 61 + [0.0],
            "type": "arbitrary",
        },
        "-8322607088264232875": {
            "samples": [0.0] * 10 + [0.25] * 62,
            "type": "arbitrary",
        },
        "-6403984813049691902": {
            "samples": [0.0] * 10 + [0.25] * 63 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6529888274398628136": {
            "samples": [0.0] * 10 + [0.25] * 64 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6756698918981049807": {
            "samples": [0.0] * 10 + [0.25] * 65 + [0.0],
            "type": "arbitrary",
        },
        "5018324660403355833": {
            "samples": [0.0] * 10 + [0.25] * 66,
            "type": "arbitrary",
        },
        "2559314455126043254": {
            "samples": [0.0] * 10 + [0.25] * 67 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6214994506865613938": {
            "samples": [0.0] * 10 + [0.25] * 68 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3371302464723107165": {
            "samples": [0.0] * 10 + [0.25] * 69 + [0.0],
            "type": "arbitrary",
        },
        "1011437984785195405": {
            "samples": [0.0] * 10 + [0.25] * 70,
            "type": "arbitrary",
        },
        "-3831822971627865329": {
            "samples": [0.0] * 10 + [0.25] * 71 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2407693383014787308": {
            "samples": [0.0] * 10 + [0.25] * 72 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7075070304125205528": {
            "samples": [0.0] * 10 + [0.25] * 73 + [0.0],
            "type": "arbitrary",
        },
        "7752565779924463191": {
            "samples": [0.0] * 10 + [0.25] * 74,
            "type": "arbitrary",
        },
        "-2462222529362097928": {
            "samples": [0.0] * 10 + [0.25] * 75 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4602148255541601755": {
            "samples": [0.0] * 10 + [0.25] * 76 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4910979138670939": {
            "samples": [0.0] * 10 + [0.25] * 77 + [0.0],
            "type": "arbitrary",
        },
        "-8492994852230459258": {
            "samples": [0.0] * 10 + [0.25] * 78,
            "type": "arbitrary",
        },
        "-2299301430927542816": {
            "samples": [0.0] * 10 + [0.25] * 79 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7263800527968564030": {
            "samples": [0.0] * 10 + [0.25] * 80 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2801073836668835517": {
            "samples": [0.0] * 10 + [0.25] * 81 + [0.0],
            "type": "arbitrary",
        },
        "2311282418937059119": {
            "samples": [0.0] * 10 + [0.25] * 82,
            "type": "arbitrary",
        },
        "3829277842256503851": {
            "samples": [0.0] * 10 + [0.25] * 83 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2564262673674617626": {
            "samples": [0.0] * 10 + [0.25] * 84 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4120133706958745881": {
            "samples": [0.0] * 10 + [0.25] * 85 + [0.0],
            "type": "arbitrary",
        },
        "7628130959065082885": {
            "samples": [0.0] * 10 + [0.25] * 86,
            "type": "arbitrary",
        },
        "-359567569393755981": {
            "samples": [0.0] * 10 + [0.25] * 87 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5840379374230123497": {
            "samples": [0.0] * 10 + [0.25] * 88 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9108247510106471675": {
            "samples": [0.0] * 10 + [0.25] * 89 + [0.0],
            "type": "arbitrary",
        },
        "-2571430635446882587_i": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
        },
        "-2571430635446882587_q": {
            "samples": [-0.00020272710178481987, -0.0002588094340347882, -0.0003243334534286105, -0.00039883853618721235, -0.00048108131352079815, -0.0005689086817884579, -0.0006591894461085464, -0.0007478294374550067, -0.000829890129756448, -0.0008998216167203542, -0.0009518077598584193, -0.0009802056987941589, -0.0009800457981846075, -0.0009475440813943566, -0.0008805699560155815, -0.0007790098417747403, -0.0006449735133424253, -0.00048280459894422585, -0.000298878277242572, -0.00010119497508515956, 0.00010119497508515956, 0.000298878277242572, 0.00048280459894422585, 0.0006449735133424253, 0.0007790098417747403, 0.0008805699560155815, 0.0009475440813943566, 0.0009800457981846075, 0.0009802056987941589, 0.0009518077598584193, 0.0008998216167203542, 0.000829890129756448, 0.0007478294374550067, 0.0006591894461085464, 0.0005689086817884579, 0.00048108131352079815, 0.00039883853618721235, 0.0003243334534286105, 0.0002588094340347882, 0.00020272710178481987],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
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
                        "feedforward": [],
                        "feedback": [],
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
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
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
            "operations": {
                "-2801073836668835517": "-2801073836668835517",
                "2311282418937059119": "2311282418937059119",
                "3829277842256503851": "3829277842256503851",
                "2564262673674617626": "2564262673674617626",
                "4120133706958745881": "4120133706958745881",
                "7628130959065082885": "7628130959065082885",
                "-359567569393755981": "-359567569393755981",
                "5840379374230123497": "5840379374230123497",
                "9108247510106471675": "9108247510106471675",
            },
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
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 63692382.0,
            "operations": {
                "-3332521264670444456": "-3332521264670444456",
                "-2571430635446882587": "-2571430635446882587",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_5eb",
                "lo_frequency": 5900000000.0,
            },
        },
        "B2/acquisition": {
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
            "intermediate_frequency": 10073341.0,
            "operations": {
                "-6075873721288486511": "-6075873721288486511_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_b02",
                "lo_frequency": 7370000000.0,
            },
        },
    },
    "pulses": {
        "-3332521264670444456": {
            "length": 40,
            "waveforms": {
                "I": "-3332521264670444456_i",
                "Q": "-3332521264670444456_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1704241017162025905": {
            "length": 16,
            "waveforms": {
                "single": "1704241017162025905",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6075873721288486511_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5718180174158414151_i",
                "Q": "5718180174158414151_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "2802114369396815230": {
            "length": 16,
            "waveforms": {
                "single": "2802114369396815230",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9047198142888685439": {
            "length": 16,
            "waveforms": {
                "single": "-9047198142888685439",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1825196803110087578": {
            "length": 16,
            "waveforms": {
                "single": "1825196803110087578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6758482513566410310": {
            "length": 16,
            "waveforms": {
                "single": "-6758482513566410310",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6717969064441660087": {
            "length": 16,
            "waveforms": {
                "single": "-6717969064441660087",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4569127546996993184": {
            "length": 16,
            "waveforms": {
                "single": "4569127546996993184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5306740759061562458": {
            "length": 16,
            "waveforms": {
                "single": "-5306740759061562458",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7615469105139747265": {
            "length": 16,
            "waveforms": {
                "single": "-7615469105139747265",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5524110644092771715": {
            "length": 16,
            "waveforms": {
                "single": "5524110644092771715",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3999602345587742064": {
            "length": 16,
            "waveforms": {
                "single": "3999602345587742064",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1555981769347584681": {
            "length": 16,
            "waveforms": {
                "single": "1555981769347584681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6418360257920614941": {
            "length": 16,
            "waveforms": {
                "single": "6418360257920614941",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "330872487648109266": {
            "length": 16,
            "waveforms": {
                "single": "330872487648109266",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8328357440840024066": {
            "length": 16,
            "waveforms": {
                "single": "8328357440840024066",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2161590570169744332": {
            "length": 16,
            "waveforms": {
                "single": "-2161590570169744332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "190617315125354155": {
            "length": 20,
            "waveforms": {
                "single": "190617315125354155",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2147595816468150264": {
            "length": 20,
            "waveforms": {
                "single": "2147595816468150264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3110316504597299977": {
            "length": 20,
            "waveforms": {
                "single": "3110316504597299977",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4729370284937384535": {
            "length": 20,
            "waveforms": {
                "single": "4729370284937384535",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3210617165699259524": {
            "length": 24,
            "waveforms": {
                "single": "-3210617165699259524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1831259996938650474": {
            "length": 24,
            "waveforms": {
                "single": "1831259996938650474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2611385654996695909": {
            "length": 24,
            "waveforms": {
                "single": "2611385654996695909",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7249789689960713619": {
            "length": 24,
            "waveforms": {
                "single": "-7249789689960713619",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6904657848459233734": {
            "length": 28,
            "waveforms": {
                "single": "6904657848459233734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5650792673788335441": {
            "length": 28,
            "waveforms": {
                "single": "-5650792673788335441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5829480971401185754": {
            "length": 28,
            "waveforms": {
                "single": "-5829480971401185754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3838649956939590170": {
            "length": 28,
            "waveforms": {
                "single": "3838649956939590170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5525544834179664944": {
            "length": 32,
            "waveforms": {
                "single": "5525544834179664944",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7736230695892046517": {
            "length": 32,
            "waveforms": {
                "single": "-7736230695892046517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4448577315411839511": {
            "length": 32,
            "waveforms": {
                "single": "4448577315411839511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7855372710141128832": {
            "length": 32,
            "waveforms": {
                "single": "-7855372710141128832",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-702786633209392637": {
            "length": 36,
            "waveforms": {
                "single": "-702786633209392637",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3740424521480665318": {
            "length": 36,
            "waveforms": {
                "single": "3740424521480665318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3347751435961884104": {
            "length": 36,
            "waveforms": {
                "single": "-3347751435961884104",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3358498769067318639": {
            "length": 36,
            "waveforms": {
                "single": "3358498769067318639",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7098698821348156696": {
            "length": 40,
            "waveforms": {
                "single": "7098698821348156696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6889819111268589912": {
            "length": 40,
            "waveforms": {
                "single": "6889819111268589912",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8878241034758525118": {
            "length": 40,
            "waveforms": {
                "single": "-8878241034758525118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8250694619980911454": {
            "length": 40,
            "waveforms": {
                "single": "-8250694619980911454",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1775479318234511072": {
            "length": 44,
            "waveforms": {
                "single": "1775479318234511072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5651503384411128783": {
            "length": 44,
            "waveforms": {
                "single": "-5651503384411128783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3315660622103041398": {
            "length": 44,
            "waveforms": {
                "single": "-3315660622103041398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5860774496334740329": {
            "length": 44,
            "waveforms": {
                "single": "5860774496334740329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7283091532369879927": {
            "length": 48,
            "waveforms": {
                "single": "7283091532369879927",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "432856893697269677": {
            "length": 48,
            "waveforms": {
                "single": "432856893697269677",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9142454174609802680": {
            "length": 48,
            "waveforms": {
                "single": "9142454174609802680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8762711298788080627": {
            "length": 48,
            "waveforms": {
                "single": "-8762711298788080627",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1330300575148032181": {
            "length": 52,
            "waveforms": {
                "single": "1330300575148032181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4943713453491619264": {
            "length": 52,
            "waveforms": {
                "single": "4943713453491619264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5532566609725663212": {
            "length": 52,
            "waveforms": {
                "single": "5532566609725663212",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1022622965938373093": {
            "length": 52,
            "waveforms": {
                "single": "-1022622965938373093",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1238688829285665072": {
            "length": 56,
            "waveforms": {
                "single": "1238688829285665072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4143912412909575159": {
            "length": 56,
            "waveforms": {
                "single": "-4143912412909575159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7137335903495984281": {
            "length": 56,
            "waveforms": {
                "single": "7137335903495984281",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1845007090635826632": {
            "length": 56,
            "waveforms": {
                "single": "1845007090635826632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6611196219619889944": {
            "length": 60,
            "waveforms": {
                "single": "-6611196219619889944",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4203276962985013985": {
            "length": 60,
            "waveforms": {
                "single": "4203276962985013985",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4520929682105593823": {
            "length": 60,
            "waveforms": {
                "single": "-4520929682105593823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "741475174713494960": {
            "length": 60,
            "waveforms": {
                "single": "741475174713494960",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6003762211673235044": {
            "length": 64,
            "waveforms": {
                "single": "-6003762211673235044",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-546607530483258957": {
            "length": 64,
            "waveforms": {
                "single": "-546607530483258957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3465480353078342405": {
            "length": 64,
            "waveforms": {
                "single": "3465480353078342405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8471319341955583097": {
            "length": 64,
            "waveforms": {
                "single": "8471319341955583097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8431207786713116744": {
            "length": 68,
            "waveforms": {
                "single": "8431207786713116744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4594584212515581860": {
            "length": 68,
            "waveforms": {
                "single": "4594584212515581860",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1022738293237895902": {
            "length": 68,
            "waveforms": {
                "single": "1022738293237895902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8511364120326059691": {
            "length": 68,
            "waveforms": {
                "single": "-8511364120326059691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7417876328975355008": {
            "length": 72,
            "waveforms": {
                "single": "-7417876328975355008",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2848825808249665226": {
            "length": 72,
            "waveforms": {
                "single": "-2848825808249665226",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6536588363730818606": {
            "length": 72,
            "waveforms": {
                "single": "-6536588363730818606",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8322607088264232875": {
            "length": 72,
            "waveforms": {
                "single": "-8322607088264232875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6403984813049691902": {
            "length": 76,
            "waveforms": {
                "single": "-6403984813049691902",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6529888274398628136": {
            "length": 76,
            "waveforms": {
                "single": "6529888274398628136",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6756698918981049807": {
            "length": 76,
            "waveforms": {
                "single": "6756698918981049807",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5018324660403355833": {
            "length": 76,
            "waveforms": {
                "single": "5018324660403355833",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2559314455126043254": {
            "length": 80,
            "waveforms": {
                "single": "2559314455126043254",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6214994506865613938": {
            "length": 80,
            "waveforms": {
                "single": "6214994506865613938",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3371302464723107165": {
            "length": 80,
            "waveforms": {
                "single": "3371302464723107165",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1011437984785195405": {
            "length": 80,
            "waveforms": {
                "single": "1011437984785195405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3831822971627865329": {
            "length": 84,
            "waveforms": {
                "single": "-3831822971627865329",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2407693383014787308": {
            "length": 84,
            "waveforms": {
                "single": "-2407693383014787308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7075070304125205528": {
            "length": 84,
            "waveforms": {
                "single": "-7075070304125205528",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7752565779924463191": {
            "length": 84,
            "waveforms": {
                "single": "7752565779924463191",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2462222529362097928": {
            "length": 88,
            "waveforms": {
                "single": "-2462222529362097928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4602148255541601755": {
            "length": 88,
            "waveforms": {
                "single": "-4602148255541601755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4910979138670939": {
            "length": 88,
            "waveforms": {
                "single": "-4910979138670939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8492994852230459258": {
            "length": 88,
            "waveforms": {
                "single": "-8492994852230459258",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2299301430927542816": {
            "length": 92,
            "waveforms": {
                "single": "-2299301430927542816",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7263800527968564030": {
            "length": 92,
            "waveforms": {
                "single": "-7263800527968564030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2801073836668835517": {
            "length": 92,
            "waveforms": {
                "single": "-2801073836668835517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2311282418937059119": {
            "length": 92,
            "waveforms": {
                "single": "2311282418937059119",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3829277842256503851": {
            "length": 96,
            "waveforms": {
                "single": "3829277842256503851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2564262673674617626": {
            "length": 96,
            "waveforms": {
                "single": "2564262673674617626",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4120133706958745881": {
            "length": 96,
            "waveforms": {
                "single": "4120133706958745881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7628130959065082885": {
            "length": 96,
            "waveforms": {
                "single": "7628130959065082885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-359567569393755981": {
            "length": 100,
            "waveforms": {
                "single": "-359567569393755981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5840379374230123497": {
            "length": 100,
            "waveforms": {
                "single": "5840379374230123497",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9108247510106471675": {
            "length": 100,
            "waveforms": {
                "single": "9108247510106471675",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2571430635446882587": {
            "length": 40,
            "waveforms": {
                "I": "-2571430635446882587_i",
                "Q": "-2571430635446882587_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-3332521264670444456_i": {
            "samples": [0.00020272710178481995, 0.0002588094340347883, 0.0003243334534286107, 0.0003988385361872125, 0.00048108131352079836, 0.0005689086817884582, 0.0006591894461085467, 0.0007478294374550071, 0.0008298901297564485, 0.0008998216167203549, 0.00095180775985842, 0.0009802056987941597, 0.0009800457981846084, 0.0009475440813943577, 0.0008805699560155827, 0.0007790098417747416, 0.0006449735133424266, 0.00048280459894422726, 0.00029887827724257344, 0.00010119497508516105, -0.00010119497508515806, -0.0002988782772425705, -0.00048280459894422444, -0.000644973513342424, -0.000779009841774739, -0.0008805699560155803, -0.0009475440813943555, -0.0009800457981846067, -0.000980205698794158, -0.0009518077598584185, -0.0008998216167203536, -0.0008298901297564475, -0.0007478294374550062, -0.0006591894461085461, -0.0005689086817884575, -0.00048108131352079793, -0.0003988385361872122, -0.00032433345342861036, -0.00025880943403478807, -0.0002027271017848198],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3332521264670444456_q": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1704241017162025905": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5718180174158414151_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5718180174158414151_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2802114369396815230": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9047198142888685439": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1825196803110087578": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6758482513566410310": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6717969064441660087": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4569127546996993184": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5306740759061562458": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7615469105139747265": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5524110644092771715": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3999602345587742064": {
            "samples": [0.0] * 10 + [0.25] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1555981769347584681": {
            "samples": [0.0] * 10 + [0.25] * 2 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6418360257920614941": {
            "samples": [0.0] * 10 + [0.25] * 3 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "330872487648109266": {
            "samples": [0.0] * 10 + [0.25] * 4 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8328357440840024066": {
            "samples": [0.0] * 10 + [0.25] * 5 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2161590570169744332": {
            "samples": [0.0] * 10 + [0.25] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "190617315125354155": {
            "samples": [0.0] * 10 + [0.25] * 7 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2147595816468150264": {
            "samples": [0.0] * 10 + [0.25] * 8 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3110316504597299977": {
            "samples": [0.0] * 10 + [0.25] * 9 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4729370284937384535": {
            "samples": [0.0] * 10 + [0.25] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3210617165699259524": {
            "samples": [0.0] * 10 + [0.25] * 11 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1831259996938650474": {
            "samples": [0.0] * 10 + [0.25] * 12 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2611385654996695909": {
            "samples": [0.0] * 10 + [0.25] * 13 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7249789689960713619": {
            "samples": [0.0] * 10 + [0.25] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6904657848459233734": {
            "samples": [0.0] * 10 + [0.25] * 15 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5650792673788335441": {
            "samples": [0.0] * 10 + [0.25] * 16 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5829480971401185754": {
            "samples": [0.0] * 10 + [0.25] * 17 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3838649956939590170": {
            "samples": [0.0] * 10 + [0.25] * 18,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5525544834179664944": {
            "samples": [0.0] * 10 + [0.25] * 19 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7736230695892046517": {
            "samples": [0.0] * 10 + [0.25] * 20 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4448577315411839511": {
            "samples": [0.0] * 10 + [0.25] * 21 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7855372710141128832": {
            "samples": [0.0] * 10 + [0.25] * 22,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-702786633209392637": {
            "samples": [0.0] * 10 + [0.25] * 23 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3740424521480665318": {
            "samples": [0.0] * 10 + [0.25] * 24 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3347751435961884104": {
            "samples": [0.0] * 10 + [0.25] * 25 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3358498769067318639": {
            "samples": [0.0] * 10 + [0.25] * 26,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7098698821348156696": {
            "samples": [0.0] * 10 + [0.25] * 27 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6889819111268589912": {
            "samples": [0.0] * 10 + [0.25] * 28 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8878241034758525118": {
            "samples": [0.0] * 10 + [0.25] * 29 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8250694619980911454": {
            "samples": [0.0] * 10 + [0.25] * 30,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1775479318234511072": {
            "samples": [0.0] * 10 + [0.25] * 31 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5651503384411128783": {
            "samples": [0.0] * 10 + [0.25] * 32 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3315660622103041398": {
            "samples": [0.0] * 10 + [0.25] * 33 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5860774496334740329": {
            "samples": [0.0] * 10 + [0.25] * 34,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7283091532369879927": {
            "samples": [0.0] * 10 + [0.25] * 35 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "432856893697269677": {
            "samples": [0.0] * 10 + [0.25] * 36 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9142454174609802680": {
            "samples": [0.0] * 10 + [0.25] * 37 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8762711298788080627": {
            "samples": [0.0] * 10 + [0.25] * 38,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1330300575148032181": {
            "samples": [0.0] * 10 + [0.25] * 39 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4943713453491619264": {
            "samples": [0.0] * 10 + [0.25] * 40 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5532566609725663212": {
            "samples": [0.0] * 10 + [0.25] * 41 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1022622965938373093": {
            "samples": [0.0] * 10 + [0.25] * 42,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1238688829285665072": {
            "samples": [0.0] * 10 + [0.25] * 43 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4143912412909575159": {
            "samples": [0.0] * 10 + [0.25] * 44 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7137335903495984281": {
            "samples": [0.0] * 10 + [0.25] * 45 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1845007090635826632": {
            "samples": [0.0] * 10 + [0.25] * 46,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6611196219619889944": {
            "samples": [0.0] * 10 + [0.25] * 47 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4203276962985013985": {
            "samples": [0.0] * 10 + [0.25] * 48 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4520929682105593823": {
            "samples": [0.0] * 10 + [0.25] * 49 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "741475174713494960": {
            "samples": [0.0] * 10 + [0.25] * 50,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6003762211673235044": {
            "samples": [0.0] * 10 + [0.25] * 51 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-546607530483258957": {
            "samples": [0.0] * 10 + [0.25] * 52 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3465480353078342405": {
            "samples": [0.0] * 10 + [0.25] * 53 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8471319341955583097": {
            "samples": [0.0] * 10 + [0.25] * 54,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8431207786713116744": {
            "samples": [0.0] * 10 + [0.25] * 55 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4594584212515581860": {
            "samples": [0.0] * 10 + [0.25] * 56 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1022738293237895902": {
            "samples": [0.0] * 10 + [0.25] * 57 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8511364120326059691": {
            "samples": [0.0] * 10 + [0.25] * 58,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7417876328975355008": {
            "samples": [0.0] * 10 + [0.25] * 59 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2848825808249665226": {
            "samples": [0.0] * 10 + [0.25] * 60 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6536588363730818606": {
            "samples": [0.0] * 10 + [0.25] * 61 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8322607088264232875": {
            "samples": [0.0] * 10 + [0.25] * 62,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6403984813049691902": {
            "samples": [0.0] * 10 + [0.25] * 63 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6529888274398628136": {
            "samples": [0.0] * 10 + [0.25] * 64 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6756698918981049807": {
            "samples": [0.0] * 10 + [0.25] * 65 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5018324660403355833": {
            "samples": [0.0] * 10 + [0.25] * 66,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2559314455126043254": {
            "samples": [0.0] * 10 + [0.25] * 67 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6214994506865613938": {
            "samples": [0.0] * 10 + [0.25] * 68 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3371302464723107165": {
            "samples": [0.0] * 10 + [0.25] * 69 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1011437984785195405": {
            "samples": [0.0] * 10 + [0.25] * 70,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3831822971627865329": {
            "samples": [0.0] * 10 + [0.25] * 71 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2407693383014787308": {
            "samples": [0.0] * 10 + [0.25] * 72 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7075070304125205528": {
            "samples": [0.0] * 10 + [0.25] * 73 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7752565779924463191": {
            "samples": [0.0] * 10 + [0.25] * 74,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2462222529362097928": {
            "samples": [0.0] * 10 + [0.25] * 75 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4602148255541601755": {
            "samples": [0.0] * 10 + [0.25] * 76 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4910979138670939": {
            "samples": [0.0] * 10 + [0.25] * 77 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8492994852230459258": {
            "samples": [0.0] * 10 + [0.25] * 78,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2299301430927542816": {
            "samples": [0.0] * 10 + [0.25] * 79 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7263800527968564030": {
            "samples": [0.0] * 10 + [0.25] * 80 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2801073836668835517": {
            "samples": [0.0] * 10 + [0.25] * 81 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2311282418937059119": {
            "samples": [0.0] * 10 + [0.25] * 82,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3829277842256503851": {
            "samples": [0.0] * 10 + [0.25] * 83 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2564262673674617626": {
            "samples": [0.0] * 10 + [0.25] * 84 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4120133706958745881": {
            "samples": [0.0] * 10 + [0.25] * 85 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7628130959065082885": {
            "samples": [0.0] * 10 + [0.25] * 86,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-359567569393755981": {
            "samples": [0.0] * 10 + [0.25] * 87 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5840379374230123497": {
            "samples": [0.0] * 10 + [0.25] * 88 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9108247510106471675": {
            "samples": [0.0] * 10 + [0.25] * 89 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2571430635446882587_i": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2571430635446882587_q": {
            "samples": [-0.00020272710178481987, -0.0002588094340347882, -0.0003243334534286105, -0.00039883853618721235, -0.00048108131352079815, -0.0005689086817884579, -0.0006591894461085464, -0.0007478294374550067, -0.000829890129756448, -0.0008998216167203542, -0.0009518077598584193, -0.0009802056987941589, -0.0009800457981846075, -0.0009475440813943566, -0.0008805699560155815, -0.0007790098417747403, -0.0006449735133424253, -0.00048280459894422585, -0.000298878277242572, -0.00010119497508515956, 0.00010119497508515956, 0.000298878277242572, 0.00048280459894422585, 0.0006449735133424253, 0.0007790098417747403, 0.0008805699560155815, 0.0009475440813943566, 0.0009800457981846075, 0.0009802056987941589, 0.0009518077598584193, 0.0008998216167203542, 0.000829890129756448, 0.0007478294374550067, 0.0006591894461085464, 0.0005689086817884579, 0.00048108131352079815, 0.00039883853618721235, 0.0003243334534286105, 0.0002588094340347882, 0.00020272710178481987],
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
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B2/drive_mixer_5eb": [{'intermediate_frequency': 63692382.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/acquisition_mixer_b02": [{'intermediate_frequency': 10073341.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

