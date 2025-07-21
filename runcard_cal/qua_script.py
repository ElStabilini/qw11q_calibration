
# Single QUA script generated at 2025-07-17 16:53:19.697055
# QUA library version: 1.2.2

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "B2/acquisition")
    wait((4+(0*(Cast.to_int(v4)+Cast.to_int(v5)))), "B3/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        play("7833776220146976447", "B2/drive")
        play("7918862048613692235", "B3/drive")
        wait(11, "B2/acquisition")
        wait(11, "B3/acquisition")
        measure("-5305991367920849411", "B2/acquisition", dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        measure("-124567342191548221", "B3/acquisition", dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
        r3 = declare_stream()
        save(v4, r3)
        r4 = declare_stream()
        save(v5, r4)
        wait(37500, )
    with stream_processing():
        r1.buffer(5000).save("-5305991367920849411_B2|acquisition_I")
        r2.buffer(5000).save("-5305991367920849411_B2|acquisition_Q")
        r3.buffer(5000).save("-124567342191548221_B3|acquisition_I")
        r4.buffer(5000).save("-124567342191548221_B3|acquisition_Q")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.15000000731389826,
                    "filter": {},
                },
                "2": {
                    "offset": 0.458500065210235,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.04400651410975173,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": -0.47493809361156486,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
                    },
                },
                "5": {
                    "offset": -0.32707319268293555,
                    "filter": {},
                },
            },
            "digital_outputs": {},
            "analog_inputs": {},
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.0,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": 0.0,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": 0.0,
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
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {},
            "analog_inputs": {},
        },
        "con2": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
                "7": {
                    "offset": 0,
                },
                "8": {
                    "offset": 0,
                },
            },
            "digital_outputs": {
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
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
            },
            "digital_outputs": {
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
                    "LO_frequency": 7400000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7400000000.0,
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
                    "output_mode": "always_on",
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
            "operations": {},
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
            "intermediate_frequency": -30481453.0,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "-5305991367920849411": "-5305991367920849411_B2/acquisition",
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
            "intermediate_frequency": 72572210.0,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "-124567342191548221": "-124567342191548221_B3/acquisition",
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
            "intermediate_frequency": -114750228.0,
            "operations": {
                "7918862048613692235": "7918862048613692235",
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
            "intermediate_frequency": 70924893.0,
            "operations": {
                "7833776220146976447": "7833776220146976447",
            },
        },
    },
    "pulses": {
        "-5305991367920849411_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1066446658394806835_i",
                "Q": "-1066446658394806835_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "1799058403373297276_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5841866836181928257_i",
                "Q": "5841866836181928257_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "7833776220146976447": {
            "length": 40,
            "waveforms": {
                "I": "7833776220146976447_i",
                "Q": "7833776220146976447_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7918862048613692235": {
            "length": 40,
            "waveforms": {
                "I": "7918862048613692235_i",
                "Q": "7918862048613692235_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-124567342191548221_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2351073665895932391_i",
                "Q": "-2351073665895932391_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
    },
    "waveforms": {
        "-1066446658394806835_i": {
            "sample": 0.004,
            "type": "constant",
        },
        "-1066446658394806835_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5841866836181928257_i": {
            "sample": 0.00365,
            "type": "constant",
        },
        "5841866836181928257_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7833776220146976447_i": {
            "samples": [0.002510969195218765, 0.0033788783731730568, 0.00447628657037825, 0.00583817829369361, 0.007496369316257264, 0.009476298743853848, 0.011793444333924702, 0.01444963005017386, 0.017429580859462113, 0.020698139399856597, 0.02419857657376014, 0.027852390907967102, 0.03156089367157546, 0.035208721160802134, 0.03866921526015069, 0.04181139090796548, 0.044507993941177826, 0.04664397716816516, 0.04812461594279307] + [0.048882468370506346] * 2 + [0.04812461594279307, 0.04664397716816516, 0.044507993941177826, 0.04181139090796548, 0.03866921526015069, 0.035208721160802134, 0.03156089367157546, 0.027852390907967102, 0.02419857657376014, 0.020698139399856597, 0.017429580859462113, 0.01444963005017386, 0.011793444333924702, 0.009476298743853848, 0.007496369316257264, 0.00583817829369361, 0.00447628657037825, 0.0033788783731730568, 0.002510969195218765],
            "type": "arbitrary",
        },
        "7833776220146976447_q": {
            "samples": [-0.0003713888810590395, -0.0004741297303984871, -0.0005941674166817557, -0.0007306580934354656, -0.0008813239530082447, -0.0010422205856741034, -0.0012076117531440622, -0.0013699970825520017, -0.0015203293687852993, -0.001648441379787593, -0.0017436781555350907, -0.0017957021753769065, -0.0017954092431150678, -0.0017358672473732184, -0.0016131730182082772, -0.001427118480575862, -0.0011815686670606624, -0.0008844809509602576, -0.0005475344341270696, -0.0001853856156122929, 0.0001853856156122929, 0.0005475344341270696, 0.0008844809509602576, 0.0011815686670606624, 0.001427118480575862, 0.0016131730182082772, 0.0017358672473732184, 0.0017954092431150678, 0.0017957021753769065, 0.0017436781555350907, 0.001648441379787593, 0.0015203293687852993, 0.0013699970825520017, 0.0012076117531440622, 0.0010422205856741034, 0.0008813239530082447, 0.0007306580934354656, 0.0005941674166817557, 0.0004741297303984871, 0.0003713888810590395],
            "type": "arbitrary",
        },
        "7918862048613692235_i": {
            "samples": [0.0033175604518554344, 0.004464265544879349, 0.005914190952774576, 0.007713559152744327, 0.009904406005248076, 0.012520342345274308, 0.015581817804809186, 0.01909124225405806, 0.023028433905868822, 0.02734694190223726, 0.031971814224231336, 0.03679933260106726, 0.041699106810790997, 0.04651871520602468, 0.05109081365698861, 0.055242341155542954, 0.0588051660577255, 0.06162728490059022, 0.06358354491825295] + [0.06458484005453405] * 2 + [0.06358354491825295, 0.06162728490059022, 0.0588051660577255, 0.055242341155542954, 0.05109081365698861, 0.04651871520602468, 0.041699106810790997, 0.03679933260106726, 0.031971814224231336, 0.02734694190223726, 0.023028433905868822, 0.01909124225405806, 0.015581817804809186, 0.012520342345274308, 0.009904406005248076, 0.007713559152744327, 0.005914190952774576, 0.004464265544879349, 0.0033175604518554344],
            "type": "arbitrary",
        },
        "7918862048613692235_q": {
            "samples": [-0.0006099909761758264, -0.0007787385994299012, -0.0009758955666094829, -0.001200075894557048, -0.00144753837780398, -0.0017118044854574517, -0.0019834526818390276, -0.0022501639127184346, -0.002497078515462332, -0.0027074972292059837, -0.0028639197199396777, -0.002949367034779604, -0.002948885905576589, -0.0028510906242465227, -0.002649570394545393, -0.0023439834617629404, -0.0019406779830991407, -0.0014527236172140617, -0.0008993028089873149, -0.00030448825585147835, 0.00030448825585147835, 0.0008993028089873149, 0.0014527236172140617, 0.0019406779830991407, 0.0023439834617629404, 0.002649570394545393, 0.0028510906242465227, 0.002948885905576589, 0.002949367034779604, 0.0028639197199396777, 0.0027074972292059837, 0.002497078515462332, 0.0022501639127184346, 0.0019834526818390276, 0.0017118044854574517, 0.00144753837780398, 0.001200075894557048, 0.0009758955666094829, 0.0007787385994299012, 0.0006099909761758264],
            "type": "arbitrary",
        },
        "-2351073665895932391_i": {
            "sample": 0.0023750000000000004,
            "type": "constant",
        },
        "-2351073665895932391_q": {
            "sample": 0.0,
            "type": "constant",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B2/acquisition": {
            "cosine": [(np.float64(1.0), 2000.0)],
            "sine": [(np.float64(-0.0), 2000.0)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(np.float64(0.0), 2000.0)],
            "sine": [(np.float64(1.0), 2000.0)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(np.float64(-0.0), 2000.0)],
            "sine": [(np.float64(-1.0), 2000.0)],
        },
        "cosine_weights_B3/acquisition": {
            "cosine": [(np.float64(1.0), 2000.0)],
            "sine": [(np.float64(-0.0), 2000.0)],
        },
        "sine_weights_B3/acquisition": {
            "cosine": [(np.float64(0.0), 2000.0)],
            "sine": [(np.float64(1.0), 2000.0)],
        },
        "minus_sine_weights_B3/acquisition": {
            "cosine": [(np.float64(-0.0), 2000.0)],
            "sine": [(np.float64(-1.0), 2000.0)],
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
                    "offset": 0.15000000731389826,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.458500065210235,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.04400651410975173,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": -0.47493809361156486,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": -0.32707319268293555,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {},
            "digital_outputs": {},
            "digital_inputs": {},
        },
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                    "crosstalk": {},
                },
                "6": {
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
            },
            "analog_inputs": {},
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
            "operations": {},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
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
            "singleInput": {
                "port": ('con9', 1, 3),
            },
            "intermediate_frequency": 0,
        },
        "B2/flux": {
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
            "singleInput": {
                "port": ('con9', 1, 4),
            },
            "intermediate_frequency": 0,
        },
        "B3/flux": {
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
            "singleInput": {
                "port": ('con9', 1, 5),
            },
            "intermediate_frequency": 0,
        },
        "B4/flux": {
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
                "-5305991367920849411": "-5305991367920849411_B2/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B2/acquisition_mixer_d70",
                "lo_frequency": 7400000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": -30481453.0,
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
                "-124567342191548221": "-124567342191548221_B3/acquisition",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con2', 1, 1),
                "Q": ('con2', 1, 2),
                "mixer": "B3/acquisition_mixer_547",
                "lo_frequency": 7400000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": 72572210.0,
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
                "7918862048613692235": "7918862048613692235",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con3', 1, 1),
                "Q": ('con3', 1, 2),
                "mixer": "B3/drive_mixer_a92",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -114750228.0,
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
                "7833776220146976447": "7833776220146976447",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con2', 1, 7),
                "Q": ('con2', 1, 8),
                "mixer": "B2/drive_mixer_d43",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 70924893.0,
        },
    },
    "pulses": {
        "-5305991367920849411_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1066446658394806835_i",
                "Q": "-1066446658394806835_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "1799058403373297276_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5841866836181928257_i",
                "Q": "5841866836181928257_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7833776220146976447": {
            "length": 40,
            "waveforms": {
                "I": "7833776220146976447_i",
                "Q": "7833776220146976447_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7918862048613692235": {
            "length": 40,
            "waveforms": {
                "I": "7918862048613692235_i",
                "Q": "7918862048613692235_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-124567342191548221_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2351073665895932391_i",
                "Q": "-2351073665895932391_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-1066446658394806835_i": {
            "type": "constant",
            "sample": 0.004,
        },
        "-1066446658394806835_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "5841866836181928257_i": {
            "type": "constant",
            "sample": 0.00365,
        },
        "5841866836181928257_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7833776220146976447_i": {
            "type": "arbitrary",
            "samples": [0.002510969195218765, 0.0033788783731730568, 0.00447628657037825, 0.00583817829369361, 0.007496369316257264, 0.009476298743853848, 0.011793444333924702, 0.01444963005017386, 0.017429580859462113, 0.020698139399856597, 0.02419857657376014, 0.027852390907967102, 0.03156089367157546, 0.035208721160802134, 0.03866921526015069, 0.04181139090796548, 0.044507993941177826, 0.04664397716816516, 0.04812461594279307] + [0.048882468370506346] * 2 + [0.04812461594279307, 0.04664397716816516, 0.044507993941177826, 0.04181139090796548, 0.03866921526015069, 0.035208721160802134, 0.03156089367157546, 0.027852390907967102, 0.02419857657376014, 0.020698139399856597, 0.017429580859462113, 0.01444963005017386, 0.011793444333924702, 0.009476298743853848, 0.007496369316257264, 0.00583817829369361, 0.00447628657037825, 0.0033788783731730568, 0.002510969195218765],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7833776220146976447_q": {
            "type": "arbitrary",
            "samples": [-0.0003713888810590395, -0.0004741297303984871, -0.0005941674166817557, -0.0007306580934354656, -0.0008813239530082447, -0.0010422205856741034, -0.0012076117531440622, -0.0013699970825520017, -0.0015203293687852993, -0.001648441379787593, -0.0017436781555350907, -0.0017957021753769065, -0.0017954092431150678, -0.0017358672473732184, -0.0016131730182082772, -0.001427118480575862, -0.0011815686670606624, -0.0008844809509602576, -0.0005475344341270696, -0.0001853856156122929, 0.0001853856156122929, 0.0005475344341270696, 0.0008844809509602576, 0.0011815686670606624, 0.001427118480575862, 0.0016131730182082772, 0.0017358672473732184, 0.0017954092431150678, 0.0017957021753769065, 0.0017436781555350907, 0.001648441379787593, 0.0015203293687852993, 0.0013699970825520017, 0.0012076117531440622, 0.0010422205856741034, 0.0008813239530082447, 0.0007306580934354656, 0.0005941674166817557, 0.0004741297303984871, 0.0003713888810590395],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7918862048613692235_i": {
            "type": "arbitrary",
            "samples": [0.0033175604518554344, 0.004464265544879349, 0.005914190952774576, 0.007713559152744327, 0.009904406005248076, 0.012520342345274308, 0.015581817804809186, 0.01909124225405806, 0.023028433905868822, 0.02734694190223726, 0.031971814224231336, 0.03679933260106726, 0.041699106810790997, 0.04651871520602468, 0.05109081365698861, 0.055242341155542954, 0.0588051660577255, 0.06162728490059022, 0.06358354491825295] + [0.06458484005453405] * 2 + [0.06358354491825295, 0.06162728490059022, 0.0588051660577255, 0.055242341155542954, 0.05109081365698861, 0.04651871520602468, 0.041699106810790997, 0.03679933260106726, 0.031971814224231336, 0.02734694190223726, 0.023028433905868822, 0.01909124225405806, 0.015581817804809186, 0.012520342345274308, 0.009904406005248076, 0.007713559152744327, 0.005914190952774576, 0.004464265544879349, 0.0033175604518554344],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7918862048613692235_q": {
            "type": "arbitrary",
            "samples": [-0.0006099909761758264, -0.0007787385994299012, -0.0009758955666094829, -0.001200075894557048, -0.00144753837780398, -0.0017118044854574517, -0.0019834526818390276, -0.0022501639127184346, -0.002497078515462332, -0.0027074972292059837, -0.0028639197199396777, -0.002949367034779604, -0.002948885905576589, -0.0028510906242465227, -0.002649570394545393, -0.0023439834617629404, -0.0019406779830991407, -0.0014527236172140617, -0.0008993028089873149, -0.00030448825585147835, 0.00030448825585147835, 0.0008993028089873149, 0.0014527236172140617, 0.0019406779830991407, 0.0023439834617629404, 0.002649570394545393, 0.0028510906242465227, 0.002948885905576589, 0.002949367034779604, 0.0028639197199396777, 0.0027074972292059837, 0.002497078515462332, 0.0022501639127184346, 0.0019834526818390276, 0.0017118044854574517, 0.00144753837780398, 0.001200075894557048, 0.0009758955666094829, 0.0007787385994299012, 0.0006099909761758264],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2351073665895932391_i": {
            "type": "constant",
            "sample": 0.0023750000000000004,
        },
        "-2351073665895932391_q": {
            "type": "constant",
            "sample": 0.0,
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
    },
    "mixers": {
        "B2/acquisition_mixer_d70": [{'intermediate_frequency': -30481453.0, 'lo_frequency': 7400000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_547": [{'intermediate_frequency': 72572210.0, 'lo_frequency': 7400000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_a92": [{'intermediate_frequency': -114750228.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_d43": [{'intermediate_frequency': 70924893.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

