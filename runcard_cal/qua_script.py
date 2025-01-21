
# Single QUA script generated at 2025-01-21 07:27:42.775006
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    set_dc_offset("B1/flux", "single", -0.08233987198571363)
    set_dc_offset("D1/flux", "single", 0.21674190528643072)
    set_dc_offset("B2/flux", "single", 0.30438797397930567)
    set_dc_offset("D2/flux", "single", -0.4253086474672965)
    set_dc_offset("B3/flux", "single", 0.34274625187777014)
    set_dc_offset("D3/flux", "single", -0.21477959018116385)
    set_dc_offset("B4/flux", "single", 0.30347347513189465)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("B5/flux", "single", -0.2839878581260484)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "B5/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        play("6278294832922906884", "B5/drive")
        wait(11, "B5/acquisition")
        measure("5610123544772032084", "B5/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        wait(25000, )
    with stream_processing():
        r1.buffer(5000).save("5610123544772032084_B5|acquisition_I")
        r2.buffer(5000).save("5610123544772032084_B5|acquisition_Q")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.08233987198571363,
                    "filter": {},
                },
                "2": {
                    "offset": 0.30438797397930567,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.30347347513189465,
                    "filter": {
                        "feedforward": [1.078098681992251, -0.923066404629278],
                        "feedback": [0.9999990463256836, -0.8449677226370271],
                    },
                },
                "5": {
                    "offset": -0.2839878581260484,
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
                "5": {
                    "offset": 0.0,
                    "filter": {},
                },
                "6": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
            "digital_outputs": {
                "5": {},
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
        "octave3": {
            "connectivity": "con3",
            "RF_outputs": {
                "3": {
                    "LO_frequency": 5900000000.0,
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
            "intermediate_frequency": 270679567.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "5610123544772032084": "5610123544772032084_B5/acquisition",
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
            "intermediate_frequency": -157953677.0,
            "operations": {
                "6278294832922906884": "6278294832922906884",
            },
        },
    },
    "pulses": {
        "5610123544772032084_B5/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5412142508717215363_i",
                "Q": "5412142508717215363_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
        },
        "6278294832922906884": {
            "length": 40,
            "waveforms": {
                "I": "6278294832922906884_i",
                "Q": "6278294832922906884_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5412142508717215363_i": {
            "sample": 0.0035,
            "type": "constant",
        },
        "5412142508717215363_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6278294832922906884_i": {
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "type": "arbitrary",
        },
        "6278294832922906884_q": {
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_B5/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_B5/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_B5/acquisition": {
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
                    "offset": -0.08233987198571363,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": 0.30438797397930567,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.34274625187777014,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.30347347513189465,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.078098681992251, -0.923066404629278],
                        "feedback": [0.9999990463256836, -0.8449677226370271],
                    },
                },
                "5": {
                    "offset": -0.2839878581260484,
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
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
        "con3": {
            "type": "opx1",
            "analog_outputs": {
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
            "digital_outputs": {
                "5": {
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
        "B5/acquisition": {
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
            "intermediate_frequency": 270679567.0,
            "operations": {
                "5610123544772032084": "5610123544772032084_B5/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B5/acquisition_mixer_c2c",
                "lo_frequency": 7370000000.0,
            },
        },
        "B5/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 5),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -157953677.0,
            "operations": {
                "6278294832922906884": "6278294832922906884",
            },
            "mixInputs": {
                "I": ('con3', 5),
                "Q": ('con3', 6),
                "mixer": "B5/drive_mixer_cbf",
                "lo_frequency": 5900000000.0,
            },
        },
    },
    "pulses": {
        "5610123544772032084_B5/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5412142508717215363_i",
                "Q": "5412142508717215363_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
            "operation": "measurement",
        },
        "6278294832922906884": {
            "length": 40,
            "waveforms": {
                "I": "6278294832922906884_i",
                "Q": "6278294832922906884_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "5412142508717215363_i": {
            "sample": 0.0035,
            "type": "constant",
        },
        "5412142508717215363_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6278294832922906884_i": {
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6278294832922906884_q": {
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
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
        "cosine_weights_B5/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B5/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B5/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B5/acquisition_mixer_c2c": [{'intermediate_frequency': 270679567.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B5/drive_mixer_cbf": [{'intermediate_frequency': -157953677.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

