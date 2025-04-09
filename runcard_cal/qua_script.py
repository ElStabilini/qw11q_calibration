
# Single QUA script generated at 2025-04-09 15:38:46.604379
# QUA library version: 1.2.1

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
    v12 = declare(fixed, )
    v13 = declare(fixed, )
    v14 = declare(fixed, )
    v15 = declare(fixed, )
    v16 = declare(fixed, )
    v17 = declare(fixed, )
    v18 = declare(fixed, )
    v19 = declare(fixed, )
    v20 = declare(fixed, )
    v21 = declare(fixed, )
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
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "B1/acquisition")
    wait((4+(0*(Cast.to_int(v4)+Cast.to_int(v5)))), "B2/acquisition")
    wait((4+(0*(Cast.to_int(v6)+Cast.to_int(v7)))), "B3/acquisition")
    wait((4+(0*(Cast.to_int(v8)+Cast.to_int(v9)))), "B4/acquisition")
    wait((4+(0*(Cast.to_int(v10)+Cast.to_int(v11)))), "B5/acquisition")
    wait((4+(0*(Cast.to_int(v12)+Cast.to_int(v13)))), "D1/acquisition")
    wait((4+(0*(Cast.to_int(v14)+Cast.to_int(v15)))), "D2/acquisition")
    wait((4+(0*(Cast.to_int(v16)+Cast.to_int(v17)))), "D3/acquisition")
    wait((4+(0*(Cast.to_int(v18)+Cast.to_int(v19)))), "D4/acquisition")
    wait((4+(0*(Cast.to_int(v20)+Cast.to_int(v21)))), "D5/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        wait(11, "B1/acquisition")
        measure("-3097983578057558870", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        wait(251, "B1/acquisition")
        measure("-3097983578057558870", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        save(v2, r1)
        save(v3, r2)
        wait(11, "B2/acquisition")
        measure("3329345518335900802", "B2/acquisition", None, dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
        r3 = declare_stream()
        save(v4, r3)
        r4 = declare_stream()
        save(v5, r4)
        wait(251, "B2/acquisition")
        measure("3329345518335900802", "B2/acquisition", None, dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
        save(v4, r3)
        save(v5, r4)
        wait(11, "B3/acquisition")
        measure("-8777740371248684088", "B3/acquisition", None, dual_demod.full("cos", "sin", v6), dual_demod.full("minus_sin", "cos", v7))
        r5 = declare_stream()
        save(v6, r5)
        r6 = declare_stream()
        save(v7, r6)
        wait(251, "B3/acquisition")
        measure("-8777740371248684088", "B3/acquisition", None, dual_demod.full("cos", "sin", v6), dual_demod.full("minus_sin", "cos", v7))
        save(v6, r5)
        save(v7, r6)
        wait(11, "B4/acquisition")
        measure("6639288563090313839", "B4/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        r7 = declare_stream()
        save(v8, r7)
        r8 = declare_stream()
        save(v9, r8)
        wait(251, "B4/acquisition")
        measure("6639288563090313839", "B4/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        save(v8, r7)
        save(v9, r8)
        wait(11, "B5/acquisition")
        measure("-1863676690395318626", "B5/acquisition", None, dual_demod.full("cos", "sin", v10), dual_demod.full("minus_sin", "cos", v11))
        r9 = declare_stream()
        save(v10, r9)
        r10 = declare_stream()
        save(v11, r10)
        wait(251, "B5/acquisition")
        measure("-1863676690395318626", "B5/acquisition", None, dual_demod.full("cos", "sin", v10), dual_demod.full("minus_sin", "cos", v11))
        save(v10, r9)
        save(v11, r10)
        wait(11, "D1/acquisition")
        measure("5524603356640612863", "D1/acquisition", None, dual_demod.full("cos", "sin", v12), dual_demod.full("minus_sin", "cos", v13))
        r11 = declare_stream()
        save(v12, r11)
        r12 = declare_stream()
        save(v13, r12)
        wait(251, "D1/acquisition")
        measure("5524603356640612863", "D1/acquisition", None, dual_demod.full("cos", "sin", v12), dual_demod.full("minus_sin", "cos", v13))
        save(v12, r11)
        save(v13, r12)
        wait(11, "D2/acquisition")
        measure("1029718134435345812", "D2/acquisition", None, dual_demod.full("cos", "sin", v14), dual_demod.full("minus_sin", "cos", v15))
        r13 = declare_stream()
        save(v14, r13)
        r14 = declare_stream()
        save(v15, r14)
        wait(251, "D2/acquisition")
        measure("1029718134435345812", "D2/acquisition", None, dual_demod.full("cos", "sin", v14), dual_demod.full("minus_sin", "cos", v15))
        save(v14, r13)
        save(v15, r14)
        wait(11, "D3/acquisition")
        measure("6261815664588527823", "D3/acquisition", None, dual_demod.full("cos", "sin", v16), dual_demod.full("minus_sin", "cos", v17))
        r15 = declare_stream()
        save(v16, r15)
        r16 = declare_stream()
        save(v17, r16)
        wait(251, "D3/acquisition")
        measure("6261815664588527823", "D3/acquisition", None, dual_demod.full("cos", "sin", v16), dual_demod.full("minus_sin", "cos", v17))
        save(v16, r15)
        save(v17, r16)
        wait(11, "D4/acquisition")
        measure("6671956485931387906", "D4/acquisition", None, dual_demod.full("cos", "sin", v18), dual_demod.full("minus_sin", "cos", v19))
        r17 = declare_stream()
        save(v18, r17)
        r18 = declare_stream()
        save(v19, r18)
        wait(251, "D4/acquisition")
        measure("6671956485931387906", "D4/acquisition", None, dual_demod.full("cos", "sin", v18), dual_demod.full("minus_sin", "cos", v19))
        save(v18, r17)
        save(v19, r18)
        wait(11, "D5/acquisition")
        measure("-5221108505199109234", "D5/acquisition", None, dual_demod.full("cos", "sin", v20), dual_demod.full("minus_sin", "cos", v21))
        r19 = declare_stream()
        save(v20, r19)
        r20 = declare_stream()
        save(v21, r20)
        wait(251, "D5/acquisition")
        measure("-5221108505199109234", "D5/acquisition", None, dual_demod.full("cos", "sin", v20), dual_demod.full("minus_sin", "cos", v21))
        save(v20, r19)
        save(v21, r20)
        wait(50000, )
    with stream_processing():
        r1.buffer(2).buffer(5000).save("-3097983578057558870_B1|acquisition_I")
        r2.buffer(2).buffer(5000).save("-3097983578057558870_B1|acquisition_Q")
        r3.buffer(2).buffer(5000).save("3329345518335900802_B2|acquisition_I")
        r4.buffer(2).buffer(5000).save("3329345518335900802_B2|acquisition_Q")
        r5.buffer(2).buffer(5000).save("-8777740371248684088_B3|acquisition_I")
        r6.buffer(2).buffer(5000).save("-8777740371248684088_B3|acquisition_Q")
        r7.buffer(2).buffer(5000).save("6639288563090313839_B4|acquisition_I")
        r8.buffer(2).buffer(5000).save("6639288563090313839_B4|acquisition_Q")
        r9.buffer(2).buffer(5000).save("-1863676690395318626_B5|acquisition_I")
        r10.buffer(2).buffer(5000).save("-1863676690395318626_B5|acquisition_Q")
        r11.buffer(2).buffer(5000).save("5524603356640612863_D1|acquisition_I")
        r12.buffer(2).buffer(5000).save("5524603356640612863_D1|acquisition_Q")
        r13.buffer(2).buffer(5000).save("1029718134435345812_D2|acquisition_I")
        r14.buffer(2).buffer(5000).save("1029718134435345812_D2|acquisition_Q")
        r15.buffer(2).buffer(5000).save("6261815664588527823_D3|acquisition_I")
        r16.buffer(2).buffer(5000).save("6261815664588527823_D3|acquisition_Q")
        r17.buffer(2).buffer(5000).save("6671956485931387906_D4|acquisition_I")
        r18.buffer(2).buffer(5000).save("6671956485931387906_D4|acquisition_Q")
        r19.buffer(2).buffer(5000).save("-5221108505199109234_D5|acquisition_I")
        r20.buffer(2).buffer(5000).save("-5221108505199109234_D5|acquisition_Q")


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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
        "con8": {
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
        "octave6": {
            "connectivity": "con8",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
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
                "-3097983578057558870": "-3097983578057558870_B1/acquisition",
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
                "-8777740371248684088": "-8777740371248684088_B3/acquisition",
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
            "intermediate_frequency": 270679567.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-1863676690395318626": "-1863676690395318626_B5/acquisition",
            },
        },
        "D3/acquisition": {
            "RF_inputs": {
                "port": ('octave6', 1),
            },
            "RF_outputs": {
                "port": ('octave6', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con8', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 27730627.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "6261815664588527823": "6261815664588527823_D3/acquisition",
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
                "3329345518335900802": "3329345518335900802_B2/acquisition",
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
                "6639288563090313839": "6639288563090313839_B4/acquisition",
            },
        },
        "D1/acquisition": {
            "RF_inputs": {
                "port": ('octave6', 1),
            },
            "RF_outputs": {
                "port": ('octave6', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con8', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -320310131.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "5524603356640612863": "5524603356640612863_D1/acquisition",
            },
        },
        "D2/acquisition": {
            "RF_inputs": {
                "port": ('octave6', 1),
            },
            "RF_outputs": {
                "port": ('octave6', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con8', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -80885347.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "1029718134435345812": "1029718134435345812_D2/acquisition",
            },
        },
        "D4/acquisition": {
            "RF_inputs": {
                "port": ('octave6', 1),
            },
            "RF_outputs": {
                "port": ('octave6', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con8', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 242937024.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "6671956485931387906": "6671956485931387906_D4/acquisition",
            },
        },
        "D5/acquisition": {
            "RF_inputs": {
                "port": ('octave6', 1),
            },
            "RF_outputs": {
                "port": ('octave6', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con8', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": 178420035.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-5221108505199109234": "-5221108505199109234_D5/acquisition",
            },
        },
    },
    "pulses": {
        "-3097983578057558870_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6407178238671874429_i",
                "Q": "-6407178238671874429_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "3329345518335900802_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-4378740732794182783_i",
                "Q": "-4378740732794182783_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-8777740371248684088_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2599524842786379037_i",
                "Q": "-2599524842786379037_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "6639288563090313839_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-9212223884515517794_i",
                "Q": "-9212223884515517794_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-1863676690395318626_B5/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3766978535068811432_i",
                "Q": "3766978535068811432_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
        },
        "5524603356640612863_D1/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "-2880618927533702486_i",
                "Q": "-2880618927533702486_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "1029718134435345812_D2/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "7378150065293239613_i",
                "Q": "7378150065293239613_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D2/acquisition",
                "sin": "sine_weights_D2/acquisition",
                "minus_sin": "minus_sine_weights_D2/acquisition",
            },
        },
        "6261815664588527823_D3/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "-7196499707889099993_i",
                "Q": "-7196499707889099993_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D3/acquisition",
                "sin": "sine_weights_D3/acquisition",
                "minus_sin": "minus_sine_weights_D3/acquisition",
            },
        },
        "6671956485931387906_D4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8286799166278541925_i",
                "Q": "8286799166278541925_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D4/acquisition",
                "sin": "sine_weights_D4/acquisition",
                "minus_sin": "minus_sine_weights_D4/acquisition",
            },
        },
        "-5221108505199109234_D5/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8517985084161175822_i",
                "Q": "8517985084161175822_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D5/acquisition",
                "sin": "sine_weights_D5/acquisition",
                "minus_sin": "minus_sine_weights_D5/acquisition",
            },
        },
    },
    "waveforms": {
        "-6407178238671874429_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-6407178238671874429_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4378740732794182783_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-4378740732794182783_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2599524842786379037_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-2599524842786379037_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-9212223884515517794_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-9212223884515517794_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3766978535068811432_i": {
            "sample": 0.0035,
            "type": "constant",
        },
        "3766978535068811432_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2880618927533702486_i": {
            "sample": 0.002,
            "type": "constant",
        },
        "-2880618927533702486_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7378150065293239613_i": {
            "sample": 0.003,
            "type": "constant",
        },
        "7378150065293239613_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7196499707889099993_i": {
            "sample": 0.0025,
            "type": "constant",
        },
        "-7196499707889099993_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8286799166278541925_i": {
            "sample": 0.002,
            "type": "constant",
        },
        "8286799166278541925_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8517985084161175822_i": {
            "sample": 0.0018,
            "type": "constant",
        },
        "8517985084161175822_q": {
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
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 1000.0)],
            "sine": [(-0.0, 1000.0)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 1000.0)],
            "sine": [(1.0, 1000.0)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(-0.0, 1000.0)],
            "sine": [(-1.0, 1000.0)],
        },
        "cosine_weights_D2/acquisition": {
            "cosine": [(1.0, 1000.0)],
            "sine": [(-0.0, 1000.0)],
        },
        "sine_weights_D2/acquisition": {
            "cosine": [(0.0, 1000.0)],
            "sine": [(1.0, 1000.0)],
        },
        "minus_sine_weights_D2/acquisition": {
            "cosine": [(-0.0, 1000.0)],
            "sine": [(-1.0, 1000.0)],
        },
        "cosine_weights_D3/acquisition": {
            "cosine": [(1.0, 1000.0)],
            "sine": [(-0.0, 1000.0)],
        },
        "sine_weights_D3/acquisition": {
            "cosine": [(0.0, 1000.0)],
            "sine": [(1.0, 1000.0)],
        },
        "minus_sine_weights_D3/acquisition": {
            "cosine": [(-0.0, 1000.0)],
            "sine": [(-1.0, 1000.0)],
        },
        "cosine_weights_D4/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_D4/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_D4/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
        "cosine_weights_D5/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_D5/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_D5/acquisition": {
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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.933705257333166],
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
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
            },
            "digital_inputs": {},
        },
        "con8": {
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
                "-3097983578057558870": "-3097983578057558870_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_3d5",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "-8777740371248684088": "-8777740371248684088_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_c30",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "-1863676690395318626": "-1863676690395318626_B5/acquisition",
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
                "mixer": "B5/acquisition_mixer_dbe",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 270679567.0,
        },
        "D3/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con8', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con8', 1, 1),
                "out2": ('con8', 1, 2),
            },
            "operations": {
                "6261815664588527823": "6261815664588527823_D3/acquisition",
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
                "I": ('con8', 1, 1),
                "Q": ('con8', 1, 2),
                "mixer": "D3/acquisition_mixer_5bf",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 27730627.0,
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
                "3329345518335900802": "3329345518335900802_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_923",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "6639288563090313839": "6639288563090313839_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_6f4",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
        "D1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con8', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con8', 1, 1),
                "out2": ('con8', 1, 2),
            },
            "operations": {
                "5524603356640612863": "5524603356640612863_D1/acquisition",
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
                "I": ('con8', 1, 1),
                "Q": ('con8', 1, 2),
                "mixer": "D1/acquisition_mixer_907",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -320310131.0,
        },
        "D2/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con8', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con8', 1, 1),
                "out2": ('con8', 1, 2),
            },
            "operations": {
                "1029718134435345812": "1029718134435345812_D2/acquisition",
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
                "I": ('con8', 1, 1),
                "Q": ('con8', 1, 2),
                "mixer": "D2/acquisition_mixer_05c",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -80885347.0,
        },
        "D4/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con8', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con8', 1, 1),
                "out2": ('con8', 1, 2),
            },
            "operations": {
                "6671956485931387906": "6671956485931387906_D4/acquisition",
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
                "I": ('con8', 1, 1),
                "Q": ('con8', 1, 2),
                "mixer": "D4/acquisition_mixer_f5b",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 242937024.0,
        },
        "D5/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con8', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con8', 1, 1),
                "out2": ('con8', 1, 2),
            },
            "operations": {
                "-5221108505199109234": "-5221108505199109234_D5/acquisition",
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
                "I": ('con8', 1, 1),
                "Q": ('con8', 1, 2),
                "mixer": "D5/acquisition_mixer_97a",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 178420035.0,
        },
    },
    "pulses": {
        "-3097983578057558870_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6407178238671874429_i",
                "Q": "-6407178238671874429_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3329345518335900802_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-4378740732794182783_i",
                "Q": "-4378740732794182783_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-8777740371248684088_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2599524842786379037_i",
                "Q": "-2599524842786379037_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6639288563090313839_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-9212223884515517794_i",
                "Q": "-9212223884515517794_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-1863676690395318626_B5/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3766978535068811432_i",
                "Q": "3766978535068811432_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "5524603356640612863_D1/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "-2880618927533702486_i",
                "Q": "-2880618927533702486_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "1029718134435345812_D2/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "7378150065293239613_i",
                "Q": "7378150065293239613_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D2/acquisition",
                "sin": "sine_weights_D2/acquisition",
                "minus_sin": "minus_sine_weights_D2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6261815664588527823_D3/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "-7196499707889099993_i",
                "Q": "-7196499707889099993_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D3/acquisition",
                "sin": "sine_weights_D3/acquisition",
                "minus_sin": "minus_sine_weights_D3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6671956485931387906_D4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8286799166278541925_i",
                "Q": "8286799166278541925_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D4/acquisition",
                "sin": "sine_weights_D4/acquisition",
                "minus_sin": "minus_sine_weights_D4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5221108505199109234_D5/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8517985084161175822_i",
                "Q": "8517985084161175822_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D5/acquisition",
                "sin": "sine_weights_D5/acquisition",
                "minus_sin": "minus_sine_weights_D5/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-6407178238671874429_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-6407178238671874429_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4378740732794182783_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-4378740732794182783_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2599524842786379037_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-2599524842786379037_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-9212223884515517794_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-9212223884515517794_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3766978535068811432_i": {
            "type": "constant",
            "sample": 0.0035,
        },
        "3766978535068811432_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2880618927533702486_i": {
            "type": "constant",
            "sample": 0.002,
        },
        "-2880618927533702486_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7378150065293239613_i": {
            "type": "constant",
            "sample": 0.003,
        },
        "7378150065293239613_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-7196499707889099993_i": {
            "type": "constant",
            "sample": 0.0025,
        },
        "-7196499707889099993_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8286799166278541925_i": {
            "type": "constant",
            "sample": 0.002,
        },
        "8286799166278541925_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8517985084161175822_i": {
            "type": "constant",
            "sample": 0.0018,
        },
        "8517985084161175822_q": {
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
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "cosine_weights_D2/acquisition": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "sine_weights_D2/acquisition": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "minus_sine_weights_D2/acquisition": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "cosine_weights_D3/acquisition": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "sine_weights_D3/acquisition": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "minus_sine_weights_D3/acquisition": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "cosine_weights_D4/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_D4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_D4/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "cosine_weights_D5/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights_D5/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_D5/acquisition": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B1/acquisition_mixer_3d5": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_c30": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B5/acquisition_mixer_dbe": [{'intermediate_frequency': 270679567.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "D3/acquisition_mixer_5bf": [{'intermediate_frequency': 27730627.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_923": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_6f4": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "D1/acquisition_mixer_907": [{'intermediate_frequency': -320310131.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D2/acquisition_mixer_05c": [{'intermediate_frequency': -80885347.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D4/acquisition_mixer_f5b": [{'intermediate_frequency': 242937024.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D5/acquisition_mixer_97a": [{'intermediate_frequency': 178420035.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

