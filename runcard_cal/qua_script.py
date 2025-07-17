
# Single QUA script generated at 2025-07-17 13:02:57.666647
# QUA library version: 1.2.2

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(fixed, )
    v11 = declare(fixed, )
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "B1/acquisition")
    wait((4+(0*(Cast.to_int(v4)+Cast.to_int(v5)))), "B2/acquisition")
    wait((4+(0*(Cast.to_int(v6)+Cast.to_int(v7)))), "B3/acquisition")
    wait((4+(0*(Cast.to_int(v8)+Cast.to_int(v9)))), "B4/acquisition")
    wait((4+(0*(Cast.to_int(v10)+Cast.to_int(v11)))), "B5/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        play("4227437304698026270", "B1/drive")
        play("-1622640846851456587", "B2/drive")
        play("-936764638743741469", "B3/drive")
        play("5029432767767575771", "B4/drive")
        play("-7649439895581956161", "B5/drive")
        wait(11, "B4/acquisition")
        wait(11, "B1/acquisition")
        wait(11, "B3/acquisition")
        wait(11, "B5/acquisition")
        wait(11, "B2/acquisition")
        measure("5075140133721825083", "B1/acquisition", dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        measure("5042097768281963375", "B2/acquisition", dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
        r3 = declare_stream()
        save(v4, r3)
        r4 = declare_stream()
        save(v5, r4)
        measure("6375682183705686214", "B3/acquisition", dual_demod.full("cos", "sin", v6), dual_demod.full("minus_sin", "cos", v7))
        r5 = declare_stream()
        save(v6, r5)
        r6 = declare_stream()
        save(v7, r6)
        measure("-2492957474530439685", "B4/acquisition", dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        r7 = declare_stream()
        save(v8, r7)
        r8 = declare_stream()
        save(v9, r8)
        measure("5042097768281963375", "B5/acquisition", dual_demod.full("cos", "sin", v10), dual_demod.full("minus_sin", "cos", v11))
        r9 = declare_stream()
        save(v10, r9)
        r10 = declare_stream()
        save(v11, r10)
        wait(25000, )
    with stream_processing():
        r1.buffer(5000).save("5075140133721825083_B1|acquisition_I")
        r2.buffer(5000).save("5075140133721825083_B1|acquisition_Q")
        r3.buffer(5000).save("5042097768281963375_B2|acquisition_I")
        r4.buffer(5000).save("5042097768281963375_B2|acquisition_Q")
        r5.buffer(5000).save("6375682183705686214_B3|acquisition_I")
        r6.buffer(5000).save("6375682183705686214_B3|acquisition_Q")
        r7.buffer(5000).save("-2492957474530439685_B4|acquisition_I")
        r8.buffer(5000).save("-2492957474530439685_B4|acquisition_Q")
        r9.buffer(5000).save("5042097768281963375_B5|acquisition_I")
        r10.buffer(5000).save("5042097768281963375_B5|acquisition_Q")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.09223860900254983,
                    "filter": {},
                },
                "2": {
                    "offset": 0.4395472244576253,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.11719021104861632,
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
                    "offset": -0.3270396460963957,
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
                "3": {
                    "offset": 0,
                },
                "4": {
                    "offset": 0,
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
                    "offset": 0,
                },
                "2": {
                    "offset": 0,
                },
                "5": {
                    "offset": 0,
                },
                "6": {
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
                "5": {},
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
                    "LO_frequency": 7400000000.0,
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
                    "output_mode": "triggered",
                },
                "3": {
                    "LO_frequency": 5900000000.0,
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
            "intermediate_frequency": 295786067.3723173,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "-2492957474530439685": "-2492957474530439685_B4/acquisition",
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
            "intermediate_frequency": -276815005.25032425,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "5075140133721825083": "5075140133721825083_B1/acquisition",
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
            "intermediate_frequency": 72723357.48168659,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "6375682183705686214": "6375682183705686214_B3/acquisition",
            },
        },
        "B5/acquisition": {
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
            "intermediate_frequency": 237546952.22525024,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "5042097768281963375": "5042097768281963375_B5/acquisition",
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
            "intermediate_frequency": -29903654.919409752,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "5042097768281963375": "5042097768281963375_B2/acquisition",
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
            "intermediate_frequency": -114699359.50313663,
            "operations": {
                "-936764638743741469": "-936764638743741469",
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
            "intermediate_frequency": 71116855.56381321,
            "operations": {
                "-1622640846851456587": "-1622640846851456587",
            },
        },
        "B5/drive": {
            "RF_inputs": {
                "port": ('octave3', 3),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con3', 5),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -158164268.59013176,
            "operations": {
                "-7649439895581956161": "-7649439895581956161",
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
            "intermediate_frequency": 100165524.99305248,
            "operations": {
                "4227437304698026270": "4227437304698026270",
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
            "intermediate_frequency": 111771407.14482498,
            "operations": {
                "5029432767767575771": "5029432767767575771",
            },
        },
    },
    "pulses": {
        "5075140133721825083_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6697118023121392728_i",
                "Q": "-6697118023121392728_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "5042097768281963375_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2665187753934918941_i",
                "Q": "-2665187753934918941_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "6375682183705686214_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "2862414565446642988_i",
                "Q": "2862414565446642988_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-2492957474530439685_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6365607154033099368_i",
                "Q": "6365607154033099368_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "5042097768281963375_B5/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2665187753934918941_i",
                "Q": "-2665187753934918941_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
        },
        "4227437304698026270": {
            "length": 40,
            "waveforms": {
                "I": "4227437304698026270_i",
                "Q": "4227437304698026270_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1622640846851456587": {
            "length": 40,
            "waveforms": {
                "I": "-1622640846851456587_i",
                "Q": "-1622640846851456587_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-936764638743741469": {
            "length": 40,
            "waveforms": {
                "I": "-936764638743741469_i",
                "Q": "-936764638743741469_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5029432767767575771": {
            "length": 40,
            "waveforms": {
                "I": "5029432767767575771_i",
                "Q": "5029432767767575771_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7649439895581956161": {
            "length": 40,
            "waveforms": {
                "I": "-7649439895581956161_i",
                "Q": "-7649439895581956161_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6697118023121392728_i": {
            "sample": 0.0045,
            "type": "constant",
        },
        "-6697118023121392728_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2665187753934918941_i": {
            "sample": 0.004,
            "type": "constant",
        },
        "-2665187753934918941_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2862414565446642988_i": {
            "sample": 0.00365,
            "type": "constant",
        },
        "2862414565446642988_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6365607154033099368_i": {
            "sample": 0.003,
            "type": "constant",
        },
        "6365607154033099368_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "4227437304698026270_i": {
            "samples": [0.0023932862492013433, 0.003220518660140052, 0.0042664940361554484, 0.0055645572463764725, 0.007145032936961341, 0.00903216794541896, 0.011240714624794276, 0.013772411454101767, 0.016612699303409546, 0.01972806854980693, 0.023064448848875745, 0.026547017898246508, 0.03008171226493538, 0.033558575058014864, 0.036856884316122565, 0.03985179392505357, 0.04242201381115595, 0.04445788876151675, 0.04586913364102335] + [0.046591467390725935] * 2 + [0.04586913364102335, 0.04445788876151675, 0.04242201381115595, 0.03985179392505357, 0.036856884316122565, 0.033558575058014864, 0.03008171226493538, 0.026547017898246508, 0.023064448848875745, 0.01972806854980693, 0.016612699303409546, 0.013772411454101767, 0.011240714624794276, 0.00903216794541896, 0.007145032936961341, 0.0055645572463764725, 0.0042664940361554484, 0.003220518660140052, 0.0023932862492013433],
            "type": "arbitrary",
        },
        "4227437304698026270_q": {
            "samples": [0.0004739828626347973, 0.000605105263877877, 0.000758302650957316, 0.0009324980698029323, 0.0011247844818732112, 0.0013301278575870894, 0.0015412073567589025, 0.0017484506728840134, 0.001940311363952912, 0.002103813560194254, 0.0022253589319032457, 0.002291754279497062, 0.0022913804264306247, 0.002215390306564263, 0.0020588025223459085, 0.0018213515192309643, 0.001507970022193434, 0.0011288135818353863, 0.0006987875828124651, 0.00023659729534353013, -0.00023659729534353013, -0.0006987875828124651, -0.0011288135818353863, -0.001507970022193434, -0.0018213515192309643, -0.0020588025223459085, -0.002215390306564263, -0.0022913804264306247, -0.002291754279497062, -0.0022253589319032457, -0.002103813560194254, -0.001940311363952912, -0.0017484506728840134, -0.0015412073567589025, -0.0013301278575870894, -0.0011247844818732112, -0.0009324980698029323, -0.000758302650957316, -0.000605105263877877, -0.0004739828626347973],
            "type": "arbitrary",
        },
        "-1622640846851456587_i": {
            "samples": [0.0022792331421113772, 0.0030670434292717173, 0.004063172389458684, 0.005299375827421255, 0.006804533254989522, 0.008601736015984197, 0.010705033433588154, 0.013116081138835082, 0.015821013823522863, 0.018787918780534586, 0.021965302411457444, 0.0252819081035956, 0.028648155058167014, 0.03195932642816306, 0.035100453310298665, 0.03795263918676092, 0.04040037411561582, 0.04233922855127105, 0.04368321993637169] + [0.044371130554057774] * 2 + [0.04368321993637169, 0.04233922855127105, 0.04040037411561582, 0.03795263918676092, 0.035100453310298665, 0.03195932642816306, 0.028648155058167014, 0.0252819081035956, 0.021965302411457444, 0.018787918780534586, 0.015821013823522863, 0.013116081138835082, 0.010705033433588154, 0.008601736015984197, 0.006804533254989522, 0.005299375827421255, 0.004063172389458684, 0.0030670434292717173, 0.0022792331421113772],
            "type": "arbitrary",
        },
        "-1622640846851456587_q": {
            "samples": [-0.0003371135926052946, -0.00043037254190225684, -0.0005393320119746714, -0.0006632260345053472, -0.0007999870195372876, -0.0009460345848855336, -0.0010961618867368734, -0.0012435607577720089, -0.0013800189547760761, -0.0014963075742999508, -0.0015827549970898645, -0.0016299777469488072, -0.0016297118492544635, -0.0015756649536172378, -0.0014642941116367657, -0.0012954104514072888, -0.0010725223036479326, -0.0008028526597751316, -0.0004970027633496671, -0.00016827647267789175, 0.00016827647267789175, 0.0004970027633496671, 0.0008028526597751316, 0.0010725223036479326, 0.0012954104514072888, 0.0014642941116367657, 0.0015756649536172378, 0.0016297118492544635, 0.0016299777469488072, 0.0015827549970898645, 0.0014963075742999508, 0.0013800189547760761, 0.0012435607577720089, 0.0010961618867368734, 0.0009460345848855336, 0.0007999870195372876, 0.0006632260345053472, 0.0005393320119746714, 0.00043037254190225684, 0.0003371135926052946],
            "type": "arbitrary",
        },
        "-936764638743741469_i": {
            "samples": [0.003246562889137074, 0.00436872788170377, 0.005787624112714998, 0.007548484873714245, 0.009692446435332047, 0.012252400342765566, 0.015248358594971943, 0.018682679489649103, 0.022535613140651677, 0.026761702763106104, 0.03128760035125274, 0.036011807260609076, 0.04080672368949988, 0.045523189895078156, 0.049997443001175715, 0.054060125597509584, 0.05754670414695249, 0.06030842814171945, 0.0622228231518524] + [0.06320269003828866] * 2 + [0.0622228231518524, 0.06030842814171945, 0.05754670414695249, 0.054060125597509584, 0.049997443001175715, 0.045523189895078156, 0.04080672368949988, 0.036011807260609076, 0.03128760035125274, 0.026761702763106104, 0.022535613140651677, 0.018682679489649103, 0.015248358594971943, 0.012252400342765566, 0.009692446435332047, 0.007548484873714245, 0.005787624112714998, 0.00436872788170377, 0.003246562889137074],
            "type": "arbitrary",
        },
        "-936764638743741469_q": {
            "samples": [-0.0005969368440154145, -0.0007620731781492398, -0.00095501088109963, -0.001174393630487691, -0.0014165602846367875, -0.0016751709566697956, -0.0019410057367957177, -0.002202009205113794, -0.002443639703694771, -0.002649555344761096, -0.002802630310782703, -0.0028862490075213165, -0.002885778174739802, -0.0027900757645783402, -0.0025928681752510198, -0.002293820965780617, -0.0018991464394179508, -0.0014216345571585276, -0.0008800572493327303, -0.00029797204481160747, 0.00029797204481160747, 0.0008800572493327303, 0.0014216345571585276, 0.0018991464394179508, 0.002293820965780617, 0.0025928681752510198, 0.0027900757645783402, 0.002885778174739802, 0.0028862490075213165, 0.002802630310782703, 0.002649555344761096, 0.002443639703694771, 0.002202009205113794, 0.0019410057367957177, 0.0016751709566697956, 0.0014165602846367875, 0.001174393630487691, 0.00095501088109963, 0.0007620731781492398, 0.0005969368440154145],
            "type": "arbitrary",
        },
        "5029432767767575771_i": {
            "samples": [0.0039285331133562355, 0.005286419124650838, 0.007003367484590221, 0.009134113151258604, 0.011728433445117809, 0.014826129081222163, 0.018451415761916643, 0.022607147166896917, 0.027269424765822888, 0.03238324316046246, 0.037859846925689104, 0.04357641669855608, 0.04937854917216424, 0.05508575223563695, 0.06049986312307866, 0.06541594935142703, 0.06963491560944543, 0.07297676498488637, 0.07529329617376786] + [0.07647899306044338] * 2 + [0.07529329617376786, 0.07297676498488637, 0.06963491560944543, 0.06541594935142703, 0.06049986312307866, 0.05508575223563695, 0.04937854917216424, 0.04357641669855608, 0.037859846925689104, 0.03238324316046246, 0.027269424765822888, 0.022607147166896917, 0.018451415761916643, 0.014826129081222163, 0.011728433445117809, 0.009134113151258604, 0.007003367484590221, 0.005286419124650838, 0.0039285331133562355],
            "type": "arbitrary",
        },
        "5029432767767575771_q": {
            "samples": [-0.0006666240675725744, -0.0008510386431980515, -0.0010665001574576354, -0.0013114939490429765, -0.001581931469591035, -0.0018707327051600514, -0.002167601401080632, -0.002459074771245488, -0.002728913544691143, -0.0029588680593112915, -0.00312981320621568, -0.003223193663970727, -0.0032226678655263743, -0.0031157930251174866, -0.0028955631521057185, -0.0025616047624167763, -0.0021208553920790897, -0.0015875981196266738, -0.0009827963362096755, -0.000332757708837456, 0.000332757708837456, 0.0009827963362096755, 0.0015875981196266738, 0.0021208553920790897, 0.0025616047624167763, 0.0028955631521057185, 0.0031157930251174866, 0.0032226678655263743, 0.003223193663970727, 0.00312981320621568, 0.0029588680593112915, 0.002728913544691143, 0.002459074771245488, 0.002167601401080632, 0.0018707327051600514, 0.001581931469591035, 0.0013114939490429765, 0.0010665001574576354, 0.0008510386431980515, 0.0006666240675725744],
            "type": "arbitrary",
        },
        "-7649439895581956161_i": {
            "samples": [0.003043407995762126, 0.004095353092026558, 0.005425461357929917, 0.00707613559479132, 0.009085937955640885, 0.011485701784869058, 0.014294186823074472, 0.017513603796589967, 0.02112543867582095, 0.025087079151297386, 0.029329766996296167, 0.033758354882173006, 0.038253227612815285, 0.042674559172363194, 0.04686883420819353, 0.05067729291364388, 0.053945697499531216, 0.05653460557701988, 0.05832920659965226] + [0.05924775794727617] * 2 + [0.05832920659965226, 0.05653460557701988, 0.053945697499531216, 0.05067729291364388, 0.04686883420819353, 0.042674559172363194, 0.038253227612815285, 0.033758354882173006, 0.029329766996296167, 0.025087079151297386, 0.02112543867582095, 0.017513603796589967, 0.014294186823074472, 0.011485701784869058, 0.009085937955640885, 0.00707613559479132, 0.005425461357929917, 0.004095353092026558, 0.003043407995762126],
            "type": "arbitrary",
        },
        "-7649439895581956161_q": {
            "samples": [-0.0001390932560563159, -0.00017757195047458902, -0.00022252868850884422, -0.00027364743120482057, -0.00033007508979476644, -0.0003903343965951593, -0.00045227700494884066, -0.0005130938612282216, -0.0005693965893092365, -0.0006173773384889591, -0.0006530455932769069, -0.0006725297261682904, -0.0006724200166315187, -0.0006501202373914705, -0.0006041685659649947, -0.0005344870736985878, -0.00044252329980084203, -0.0003312574545528508, -0.00020506361695190245, -6.943096634446426e-05, 6.943096634446426e-05, 0.00020506361695190245, 0.0003312574545528508, 0.00044252329980084203, 0.0005344870736985878, 0.0006041685659649947, 0.0006501202373914705, 0.0006724200166315187, 0.0006725297261682904, 0.0006530455932769069, 0.0006173773384889591, 0.0005693965893092365, 0.0005130938612282216, 0.00045227700494884066, 0.0003903343965951593, 0.00033007508979476644, 0.00027364743120482057, 0.00022252868850884422, 0.00017757195047458902, 0.0001390932560563159],
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
            "cosine": [(np.float64(1.0), 2000.0)],
            "sine": [(np.float64(-0.0), 2000.0)],
        },
        "sine_weights_B1/acquisition": {
            "cosine": [(np.float64(0.0), 2000.0)],
            "sine": [(np.float64(1.0), 2000.0)],
        },
        "minus_sine_weights_B1/acquisition": {
            "cosine": [(np.float64(-0.0), 2000.0)],
            "sine": [(np.float64(-1.0), 2000.0)],
        },
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
        "cosine_weights_B4/acquisition": {
            "cosine": [(np.float64(1.0), 2000.0)],
            "sine": [(np.float64(-0.0), 2000.0)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(np.float64(0.0), 2000.0)],
            "sine": [(np.float64(1.0), 2000.0)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(np.float64(-0.0), 2000.0)],
            "sine": [(np.float64(-1.0), 2000.0)],
        },
        "cosine_weights_B5/acquisition": {
            "cosine": [(np.float64(1.0), 2000.0)],
            "sine": [(np.float64(-0.0), 2000.0)],
        },
        "sine_weights_B5/acquisition": {
            "cosine": [(np.float64(0.0), 2000.0)],
            "sine": [(np.float64(1.0), 2000.0)],
        },
        "minus_sine_weights_B5/acquisition": {
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
                    "offset": 0.09223860900254983,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.4395472244576253,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.11719021104861632,
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
                    "offset": -0.3270396460963957,
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
                "5": {
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
                "-2492957474530439685": "-2492957474530439685_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_b84",
                "lo_frequency": 7400000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": 295786067.3723173,
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
                "5075140133721825083": "5075140133721825083_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_a07",
                "lo_frequency": 7400000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": -276815005.25032425,
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
                "6375682183705686214": "6375682183705686214_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_baa",
                "lo_frequency": 7400000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": 72723357.48168659,
        },
        "B5/acquisition": {
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
                "5042097768281963375": "5042097768281963375_B5/acquisition",
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
                "mixer": "B5/acquisition_mixer_943",
                "lo_frequency": 7400000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": 237546952.22525024,
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
                "5042097768281963375": "5042097768281963375_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_eee",
                "lo_frequency": 7400000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": -29903654.919409752,
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
                "-936764638743741469": "-936764638743741469",
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
                "mixer": "B3/drive_mixer_76e",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -114699359.50313663,
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
                "-1622640846851456587": "-1622640846851456587",
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
                "mixer": "B2/drive_mixer_55c",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 71116855.56381321,
        },
        "B5/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 1, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-7649439895581956161": "-7649439895581956161",
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
                "I": ('con3', 1, 5),
                "Q": ('con3', 1, 6),
                "mixer": "B5/drive_mixer_54a",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": -158164268.59013176,
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
                "4227437304698026270": "4227437304698026270",
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
                "I": ('con2', 1, 3),
                "Q": ('con2', 1, 4),
                "mixer": "B1/drive_mixer_8cd",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100165524.99305248,
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
                "5029432767767575771": "5029432767767575771",
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
                "I": ('con3', 1, 7),
                "Q": ('con3', 1, 8),
                "mixer": "B4/drive_mixer_c72",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 111771407.14482498,
        },
    },
    "pulses": {
        "5075140133721825083_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6697118023121392728_i",
                "Q": "-6697118023121392728_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "5042097768281963375_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2665187753934918941_i",
                "Q": "-2665187753934918941_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6375682183705686214_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "2862414565446642988_i",
                "Q": "2862414565446642988_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2492957474530439685_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6365607154033099368_i",
                "Q": "6365607154033099368_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "5042097768281963375_B5/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2665187753934918941_i",
                "Q": "-2665187753934918941_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "4227437304698026270": {
            "length": 40,
            "waveforms": {
                "I": "4227437304698026270_i",
                "Q": "4227437304698026270_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1622640846851456587": {
            "length": 40,
            "waveforms": {
                "I": "-1622640846851456587_i",
                "Q": "-1622640846851456587_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-936764638743741469": {
            "length": 40,
            "waveforms": {
                "I": "-936764638743741469_i",
                "Q": "-936764638743741469_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5029432767767575771": {
            "length": 40,
            "waveforms": {
                "I": "5029432767767575771_i",
                "Q": "5029432767767575771_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7649439895581956161": {
            "length": 40,
            "waveforms": {
                "I": "-7649439895581956161_i",
                "Q": "-7649439895581956161_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-6697118023121392728_i": {
            "type": "constant",
            "sample": 0.0045,
        },
        "-6697118023121392728_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2665187753934918941_i": {
            "type": "constant",
            "sample": 0.004,
        },
        "-2665187753934918941_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2862414565446642988_i": {
            "type": "constant",
            "sample": 0.00365,
        },
        "2862414565446642988_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "6365607154033099368_i": {
            "type": "constant",
            "sample": 0.003,
        },
        "6365607154033099368_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "4227437304698026270_i": {
            "type": "arbitrary",
            "samples": [0.0023932862492013433, 0.003220518660140052, 0.0042664940361554484, 0.0055645572463764725, 0.007145032936961341, 0.00903216794541896, 0.011240714624794276, 0.013772411454101767, 0.016612699303409546, 0.01972806854980693, 0.023064448848875745, 0.026547017898246508, 0.03008171226493538, 0.033558575058014864, 0.036856884316122565, 0.03985179392505357, 0.04242201381115595, 0.04445788876151675, 0.04586913364102335] + [0.046591467390725935] * 2 + [0.04586913364102335, 0.04445788876151675, 0.04242201381115595, 0.03985179392505357, 0.036856884316122565, 0.033558575058014864, 0.03008171226493538, 0.026547017898246508, 0.023064448848875745, 0.01972806854980693, 0.016612699303409546, 0.013772411454101767, 0.011240714624794276, 0.00903216794541896, 0.007145032936961341, 0.0055645572463764725, 0.0042664940361554484, 0.003220518660140052, 0.0023932862492013433],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4227437304698026270_q": {
            "type": "arbitrary",
            "samples": [0.0004739828626347973, 0.000605105263877877, 0.000758302650957316, 0.0009324980698029323, 0.0011247844818732112, 0.0013301278575870894, 0.0015412073567589025, 0.0017484506728840134, 0.001940311363952912, 0.002103813560194254, 0.0022253589319032457, 0.002291754279497062, 0.0022913804264306247, 0.002215390306564263, 0.0020588025223459085, 0.0018213515192309643, 0.001507970022193434, 0.0011288135818353863, 0.0006987875828124651, 0.00023659729534353013, -0.00023659729534353013, -0.0006987875828124651, -0.0011288135818353863, -0.001507970022193434, -0.0018213515192309643, -0.0020588025223459085, -0.002215390306564263, -0.0022913804264306247, -0.002291754279497062, -0.0022253589319032457, -0.002103813560194254, -0.001940311363952912, -0.0017484506728840134, -0.0015412073567589025, -0.0013301278575870894, -0.0011247844818732112, -0.0009324980698029323, -0.000758302650957316, -0.000605105263877877, -0.0004739828626347973],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1622640846851456587_i": {
            "type": "arbitrary",
            "samples": [0.0022792331421113772, 0.0030670434292717173, 0.004063172389458684, 0.005299375827421255, 0.006804533254989522, 0.008601736015984197, 0.010705033433588154, 0.013116081138835082, 0.015821013823522863, 0.018787918780534586, 0.021965302411457444, 0.0252819081035956, 0.028648155058167014, 0.03195932642816306, 0.035100453310298665, 0.03795263918676092, 0.04040037411561582, 0.04233922855127105, 0.04368321993637169] + [0.044371130554057774] * 2 + [0.04368321993637169, 0.04233922855127105, 0.04040037411561582, 0.03795263918676092, 0.035100453310298665, 0.03195932642816306, 0.028648155058167014, 0.0252819081035956, 0.021965302411457444, 0.018787918780534586, 0.015821013823522863, 0.013116081138835082, 0.010705033433588154, 0.008601736015984197, 0.006804533254989522, 0.005299375827421255, 0.004063172389458684, 0.0030670434292717173, 0.0022792331421113772],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1622640846851456587_q": {
            "type": "arbitrary",
            "samples": [-0.0003371135926052946, -0.00043037254190225684, -0.0005393320119746714, -0.0006632260345053472, -0.0007999870195372876, -0.0009460345848855336, -0.0010961618867368734, -0.0012435607577720089, -0.0013800189547760761, -0.0014963075742999508, -0.0015827549970898645, -0.0016299777469488072, -0.0016297118492544635, -0.0015756649536172378, -0.0014642941116367657, -0.0012954104514072888, -0.0010725223036479326, -0.0008028526597751316, -0.0004970027633496671, -0.00016827647267789175, 0.00016827647267789175, 0.0004970027633496671, 0.0008028526597751316, 0.0010725223036479326, 0.0012954104514072888, 0.0014642941116367657, 0.0015756649536172378, 0.0016297118492544635, 0.0016299777469488072, 0.0015827549970898645, 0.0014963075742999508, 0.0013800189547760761, 0.0012435607577720089, 0.0010961618867368734, 0.0009460345848855336, 0.0007999870195372876, 0.0006632260345053472, 0.0005393320119746714, 0.00043037254190225684, 0.0003371135926052946],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-936764638743741469_i": {
            "type": "arbitrary",
            "samples": [0.003246562889137074, 0.00436872788170377, 0.005787624112714998, 0.007548484873714245, 0.009692446435332047, 0.012252400342765566, 0.015248358594971943, 0.018682679489649103, 0.022535613140651677, 0.026761702763106104, 0.03128760035125274, 0.036011807260609076, 0.04080672368949988, 0.045523189895078156, 0.049997443001175715, 0.054060125597509584, 0.05754670414695249, 0.06030842814171945, 0.0622228231518524] + [0.06320269003828866] * 2 + [0.0622228231518524, 0.06030842814171945, 0.05754670414695249, 0.054060125597509584, 0.049997443001175715, 0.045523189895078156, 0.04080672368949988, 0.036011807260609076, 0.03128760035125274, 0.026761702763106104, 0.022535613140651677, 0.018682679489649103, 0.015248358594971943, 0.012252400342765566, 0.009692446435332047, 0.007548484873714245, 0.005787624112714998, 0.00436872788170377, 0.003246562889137074],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-936764638743741469_q": {
            "type": "arbitrary",
            "samples": [-0.0005969368440154145, -0.0007620731781492398, -0.00095501088109963, -0.001174393630487691, -0.0014165602846367875, -0.0016751709566697956, -0.0019410057367957177, -0.002202009205113794, -0.002443639703694771, -0.002649555344761096, -0.002802630310782703, -0.0028862490075213165, -0.002885778174739802, -0.0027900757645783402, -0.0025928681752510198, -0.002293820965780617, -0.0018991464394179508, -0.0014216345571585276, -0.0008800572493327303, -0.00029797204481160747, 0.00029797204481160747, 0.0008800572493327303, 0.0014216345571585276, 0.0018991464394179508, 0.002293820965780617, 0.0025928681752510198, 0.0027900757645783402, 0.002885778174739802, 0.0028862490075213165, 0.002802630310782703, 0.002649555344761096, 0.002443639703694771, 0.002202009205113794, 0.0019410057367957177, 0.0016751709566697956, 0.0014165602846367875, 0.001174393630487691, 0.00095501088109963, 0.0007620731781492398, 0.0005969368440154145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5029432767767575771_i": {
            "type": "arbitrary",
            "samples": [0.0039285331133562355, 0.005286419124650838, 0.007003367484590221, 0.009134113151258604, 0.011728433445117809, 0.014826129081222163, 0.018451415761916643, 0.022607147166896917, 0.027269424765822888, 0.03238324316046246, 0.037859846925689104, 0.04357641669855608, 0.04937854917216424, 0.05508575223563695, 0.06049986312307866, 0.06541594935142703, 0.06963491560944543, 0.07297676498488637, 0.07529329617376786] + [0.07647899306044338] * 2 + [0.07529329617376786, 0.07297676498488637, 0.06963491560944543, 0.06541594935142703, 0.06049986312307866, 0.05508575223563695, 0.04937854917216424, 0.04357641669855608, 0.037859846925689104, 0.03238324316046246, 0.027269424765822888, 0.022607147166896917, 0.018451415761916643, 0.014826129081222163, 0.011728433445117809, 0.009134113151258604, 0.007003367484590221, 0.005286419124650838, 0.0039285331133562355],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5029432767767575771_q": {
            "type": "arbitrary",
            "samples": [-0.0006666240675725744, -0.0008510386431980515, -0.0010665001574576354, -0.0013114939490429765, -0.001581931469591035, -0.0018707327051600514, -0.002167601401080632, -0.002459074771245488, -0.002728913544691143, -0.0029588680593112915, -0.00312981320621568, -0.003223193663970727, -0.0032226678655263743, -0.0031157930251174866, -0.0028955631521057185, -0.0025616047624167763, -0.0021208553920790897, -0.0015875981196266738, -0.0009827963362096755, -0.000332757708837456, 0.000332757708837456, 0.0009827963362096755, 0.0015875981196266738, 0.0021208553920790897, 0.0025616047624167763, 0.0028955631521057185, 0.0031157930251174866, 0.0032226678655263743, 0.003223193663970727, 0.00312981320621568, 0.0029588680593112915, 0.002728913544691143, 0.002459074771245488, 0.002167601401080632, 0.0018707327051600514, 0.001581931469591035, 0.0013114939490429765, 0.0010665001574576354, 0.0008510386431980515, 0.0006666240675725744],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7649439895581956161_i": {
            "type": "arbitrary",
            "samples": [0.003043407995762126, 0.004095353092026558, 0.005425461357929917, 0.00707613559479132, 0.009085937955640885, 0.011485701784869058, 0.014294186823074472, 0.017513603796589967, 0.02112543867582095, 0.025087079151297386, 0.029329766996296167, 0.033758354882173006, 0.038253227612815285, 0.042674559172363194, 0.04686883420819353, 0.05067729291364388, 0.053945697499531216, 0.05653460557701988, 0.05832920659965226] + [0.05924775794727617] * 2 + [0.05832920659965226, 0.05653460557701988, 0.053945697499531216, 0.05067729291364388, 0.04686883420819353, 0.042674559172363194, 0.038253227612815285, 0.033758354882173006, 0.029329766996296167, 0.025087079151297386, 0.02112543867582095, 0.017513603796589967, 0.014294186823074472, 0.011485701784869058, 0.009085937955640885, 0.00707613559479132, 0.005425461357929917, 0.004095353092026558, 0.003043407995762126],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7649439895581956161_q": {
            "type": "arbitrary",
            "samples": [-0.0001390932560563159, -0.00017757195047458902, -0.00022252868850884422, -0.00027364743120482057, -0.00033007508979476644, -0.0003903343965951593, -0.00045227700494884066, -0.0005130938612282216, -0.0005693965893092365, -0.0006173773384889591, -0.0006530455932769069, -0.0006725297261682904, -0.0006724200166315187, -0.0006501202373914705, -0.0006041685659649947, -0.0005344870736985878, -0.00044252329980084203, -0.0003312574545528508, -0.00020506361695190245, -6.943096634446426e-05, 6.943096634446426e-05, 0.00020506361695190245, 0.0003312574545528508, 0.00044252329980084203, 0.0005344870736985878, 0.0006041685659649947, 0.0006501202373914705, 0.0006724200166315187, 0.0006725297261682904, 0.0006530455932769069, 0.0006173773384889591, 0.0005693965893092365, 0.0005130938612282216, 0.00045227700494884066, 0.0003903343965951593, 0.00033007508979476644, 0.00027364743120482057, 0.00022252868850884422, 0.00017757195047458902, 0.0001390932560563159],
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
        "cosine_weights_B5/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_B5/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B5/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B4/acquisition_mixer_b84": [{'intermediate_frequency': 295786067.3723173, 'lo_frequency': 7400000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_a07": [{'intermediate_frequency': -276815005.25032425, 'lo_frequency': 7400000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_baa": [{'intermediate_frequency': 72723357.48168659, 'lo_frequency': 7400000000.0, 'correction': (1, 0, 0, 1)}],
        "B5/acquisition_mixer_943": [{'intermediate_frequency': 237546952.22525024, 'lo_frequency': 7400000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_eee": [{'intermediate_frequency': -29903654.919409752, 'lo_frequency': 7400000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_76e": [{'intermediate_frequency': -114699359.50313663, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_55c": [{'intermediate_frequency': 71116855.56381321, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B5/drive_mixer_54a": [{'intermediate_frequency': -158164268.59013176, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_8cd": [{'intermediate_frequency': 100165524.99305248, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_c72": [{'intermediate_frequency': 111771407.14482498, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

