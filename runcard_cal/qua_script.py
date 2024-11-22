
# Single QUA script generated at 2024-11-22 09:01:22.674634
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    v5 = declare(fixed, )
    set_dc_offset("D1/flux", "single", 0.2205)
    set_dc_offset("D2/flux", "single", -0.421)
    set_dc_offset("D3/flux", "single", -0.2095)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "D1/acquisition")
    with for_(v1,0,(v1<1024),(v1+1)):
        with for_(v5,0.1259493670886076,(v5<2.002594936708861),(v5+0.025189873417721526)):
            align()
            play("-6950704694037758713"*amp(v5), "D1/drive")
            wait(11, "D1/acquisition")
            measure("-4086476114703021429", "D1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
            assign(v4, Cast.to_int((((v2*0.9832190513468051)-(v3*-0.1824288822217816))>0.0011543927554382514)))
            r1 = declare_stream()
            save(v4, r1)
            wait(12500, )
    with stream_processing():
        r1.buffer(75).buffer(1024).save("-4086476114703021429_D1|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
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
        "con6": {
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
            },
            "digital_outputs": {
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
    },
    "octaves": {
        "octave5": {
            "connectivity": "con6",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "2": {
                    "LO_frequency": 5100000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
    },
    "elements": {
        "D1/flux": {
            "singleInput": {
                "port": ('con9', 3),
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
        "D3/flux": {
            "singleInput": {
                "port": ('con9', 5),
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
        "D5/flux": {
            "singleInput": {
                "port": ('con9', 7),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D1/acquisition": {
            "RF_inputs": {
                "port": ('octave5', 1),
            },
            "RF_outputs": {
                "port": ('octave5', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -312367220.6387558,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-4086476114703021429": "-4086476114703021429_D1/acquisition",
            },
        },
        "D1/drive": {
            "RF_inputs": {
                "port": ('octave5', 2),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 3),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -141729925.0,
            "operations": {
                "-4545242770361676980": "-4545242770361676980",
                "-6950704694037758713": "-6950704694037758713",
            },
        },
    },
    "pulses": {
        "-4086476114703021429_D1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2323563586783510777_i",
                "Q": "-2323563586783510777_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "-4545242770361676980": {
            "length": 40,
            "waveforms": {
                "I": "-4545242770361676980_i",
                "Q": "-4545242770361676980_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6950704694037758713": {
            "length": 40,
            "waveforms": {
                "I": "-6950704694037758713_i",
                "Q": "-6950704694037758713_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-2323563586783510777_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-2323563586783510777_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4545242770361676980_i": {
            "samples": [0.0021284539268158677, 0.002864147818024836, 0.003794379376065839, 0.004948803648537274, 0.006354389666918888, 0.00803270120216617, 0.009996858165772686, 0.012248406663009498, 0.01477439862413155, 0.01754503247881094, 0.020512221109620934, 0.023609421777119107, 0.02675297976454476, 0.029845105609248693, 0.03277843600155558, 0.035441939842650656, 0.03772774857580174, 0.03953834103378605, 0.040793422705060006] + [0.041435825638072785] * 2 + [0.040793422705060006, 0.03953834103378605, 0.03772774857580174, 0.035441939842650656, 0.03277843600155558, 0.029845105609248693, 0.02675297976454476, 0.023609421777119107, 0.020512221109620934, 0.01754503247881094, 0.01477439862413155, 0.012248406663009498, 0.009996858165772686, 0.00803270120216617, 0.006354389666918888, 0.004948803648537274, 0.003794379376065839, 0.002864147818024836, 0.0021284539268158677],
            "type": "arbitrary",
        },
        "-4545242770361676980_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-6950704694037758713_i": {
            "samples": [0.0020352325524029963, 0.002738704747468298, 0.003628194308104388, 0.004732057459200572, 0.006076082050840349, 0.0076808874105310015, 0.009559018827893284, 0.011711954692352254, 0.014127314029763286, 0.016776600509865285, 0.019613833120100215, 0.02257538353958547, 0.025581260935271573, 0.028537958797499943, 0.03134281608201118, 0.0338896645961139, 0.03607536017714801, 0.03780665286016027, 0.039006764848077455] + [0.03962103201381435] * 2 + [0.039006764848077455, 0.03780665286016027, 0.03607536017714801, 0.0338896645961139, 0.03134281608201118, 0.028537958797499943, 0.025581260935271573, 0.02257538353958547, 0.019613833120100215, 0.016776600509865285, 0.014127314029763286, 0.011711954692352254, 0.009559018827893284, 0.0076808874105310015, 0.006076082050840349, 0.004732057459200572, 0.003628194308104388, 0.002738704747468298, 0.0020352325524029963],
            "type": "arbitrary",
        },
        "-6950704694037758713_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
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
        "con6": {
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
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
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
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
                "3": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
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
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 5),
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
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 7),
            },
        },
        "D1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con6', 1),
                "out2": ('con6', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": -312367220.6387558,
            "operations": {
                "-4086476114703021429": "-4086476114703021429_D1/acquisition",
            },
            "mixInputs": {
                "I": ('con6', 1),
                "Q": ('con6', 2),
                "mixer": "D1/acquisition_mixer_e48",
                "lo_frequency": 7450000000.0,
            },
        },
        "D1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 3),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -141729925.0,
            "operations": {
                "-4545242770361676980": "-4545242770361676980",
                "-6950704694037758713": "-6950704694037758713",
            },
            "mixInputs": {
                "I": ('con6', 3),
                "Q": ('con6', 4),
                "mixer": "D1/drive_mixer_db5",
                "lo_frequency": 5100000000.0,
            },
        },
    },
    "pulses": {
        "-4086476114703021429_D1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2323563586783510777_i",
                "Q": "-2323563586783510777_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
        },
        "-4545242770361676980": {
            "length": 40,
            "waveforms": {
                "I": "-4545242770361676980_i",
                "Q": "-4545242770361676980_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6950704694037758713": {
            "length": 40,
            "waveforms": {
                "I": "-6950704694037758713_i",
                "Q": "-6950704694037758713_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-2323563586783510777_i": {
            "sample": 0.0005,
            "type": "constant",
        },
        "-2323563586783510777_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4545242770361676980_i": {
            "samples": [0.0021284539268158677, 0.002864147818024836, 0.003794379376065839, 0.004948803648537274, 0.006354389666918888, 0.00803270120216617, 0.009996858165772686, 0.012248406663009498, 0.01477439862413155, 0.01754503247881094, 0.020512221109620934, 0.023609421777119107, 0.02675297976454476, 0.029845105609248693, 0.03277843600155558, 0.035441939842650656, 0.03772774857580174, 0.03953834103378605, 0.040793422705060006] + [0.041435825638072785] * 2 + [0.040793422705060006, 0.03953834103378605, 0.03772774857580174, 0.035441939842650656, 0.03277843600155558, 0.029845105609248693, 0.02675297976454476, 0.023609421777119107, 0.020512221109620934, 0.01754503247881094, 0.01477439862413155, 0.012248406663009498, 0.009996858165772686, 0.00803270120216617, 0.006354389666918888, 0.004948803648537274, 0.003794379376065839, 0.002864147818024836, 0.0021284539268158677],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4545242770361676980_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6950704694037758713_i": {
            "samples": [0.0020352325524029963, 0.002738704747468298, 0.003628194308104388, 0.004732057459200572, 0.006076082050840349, 0.0076808874105310015, 0.009559018827893284, 0.011711954692352254, 0.014127314029763286, 0.016776600509865285, 0.019613833120100215, 0.02257538353958547, 0.025581260935271573, 0.028537958797499943, 0.03134281608201118, 0.0338896645961139, 0.03607536017714801, 0.03780665286016027, 0.039006764848077455] + [0.03962103201381435] * 2 + [0.039006764848077455, 0.03780665286016027, 0.03607536017714801, 0.0338896645961139, 0.03134281608201118, 0.028537958797499943, 0.025581260935271573, 0.02257538353958547, 0.019613833120100215, 0.016776600509865285, 0.014127314029763286, 0.011711954692352254, 0.009559018827893284, 0.0076808874105310015, 0.006076082050840349, 0.004732057459200572, 0.003628194308104388, 0.002738704747468298, 0.0020352325524029963],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6950704694037758713_q": {
            "samples": [0.0] * 40,
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
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "D1/acquisition_mixer_e48": [{'intermediate_frequency': -312367220.6387558, 'lo_frequency': 7450000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "D1/drive_mixer_db5": [{'intermediate_frequency': -141729925.0, 'lo_frequency': 5100000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

