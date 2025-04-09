
# Single QUA script generated at 2025-04-09 15:39:10.953984
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
    v14 = declare(fixed, )
    v15 = declare(fixed, )
    v16 = declare(int, )
    v17 = declare(fixed, )
    v18 = declare(fixed, )
    v19 = declare(int, )
    v20 = declare(fixed, )
    v21 = declare(fixed, )
    v22 = declare(int, )
    v23 = declare(fixed, )
    v24 = declare(fixed, )
    v25 = declare(int, )
    v26 = declare(fixed, )
    v27 = declare(fixed, )
    v28 = declare(int, )
    v29 = declare(fixed, )
    v30 = declare(fixed, )
    v31 = declare(int, )
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
    wait((4+(0*((Cast.to_int(v14)+Cast.to_int(v15))+Cast.to_int(v16)))), "B5/acquisition")
    wait((4+(0*((Cast.to_int(v17)+Cast.to_int(v18))+Cast.to_int(v19)))), "D1/acquisition")
    wait((4+(0*((Cast.to_int(v20)+Cast.to_int(v21))+Cast.to_int(v22)))), "D2/acquisition")
    wait((4+(0*((Cast.to_int(v23)+Cast.to_int(v24))+Cast.to_int(v25)))), "D3/acquisition")
    wait((4+(0*((Cast.to_int(v26)+Cast.to_int(v27))+Cast.to_int(v28)))), "D4/acquisition")
    wait((4+(0*((Cast.to_int(v29)+Cast.to_int(v30))+Cast.to_int(v31)))), "D5/acquisition")
    with for_(v1,0,(v1<5000),(v1+1)):
        align()
        play("740409870800413924", "B1/drive")
        wait(11, "B1/acquisition")
        measure("-3097983578057558870", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967670294372607)-(v3*0.08034605794199916))>0.0007870074932508873)))
        r1 = declare_stream()
        save(v4, r1)
        wait(251, "B1/acquisition")
        measure("-3097983578057558870", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967670294372607)-(v3*0.08034605794199916))>0.0007870074932508873)))
        save(v4, r1)
        play("-6517581333074707223", "B2/drive")
        wait(11, "B2/acquisition")
        measure("3329345518335900802", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7359973353402354)-(v6*0.6769844328875466))>0.0024378669440833717)))
        r2 = declare_stream()
        save(v7, r2)
        wait(251, "B2/acquisition")
        measure("3329345518335900802", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7359973353402354)-(v6*0.6769844328875466))>0.0024378669440833717)))
        save(v7, r2)
        play("3336423412446418861", "B3/drive")
        wait(11, "B3/acquisition")
        measure("-8777740371248684088", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8321494180571197)-(v9*-0.5545514818546579))>0.0026636797237234713)))
        r3 = declare_stream()
        save(v10, r3)
        wait(251, "B3/acquisition")
        measure("-8777740371248684088", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8321494180571197)-(v9*-0.5545514818546579))>0.0026636797237234713)))
        save(v10, r3)
        play("1738384850733880654", "B4/drive")
        wait(11, "B4/acquisition")
        measure("6639288563090313839", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.45141096231273753)-(v12*0.8923161676804294))>-0.000508161646537873)))
        r4 = declare_stream()
        save(v13, r4)
        wait(251, "B4/acquisition")
        measure("6639288563090313839", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.45141096231273753)-(v12*0.8923161676804294))>-0.000508161646537873)))
        save(v13, r4)
        play("4843395743109475609", "B5/drive")
        wait(11, "B5/acquisition")
        measure("-1863676690395318626", "B5/acquisition", None, dual_demod.full("cos", "sin", v14), dual_demod.full("minus_sin", "cos", v15))
        assign(v16, Cast.to_int((((v14*0.9566189640759325)-(v15*-0.29134199417572776))>0.0010562843616691592)))
        r5 = declare_stream()
        save(v16, r5)
        wait(251, "B5/acquisition")
        measure("-1863676690395318626", "B5/acquisition", None, dual_demod.full("cos", "sin", v14), dual_demod.full("minus_sin", "cos", v15))
        assign(v16, Cast.to_int((((v14*0.9566189640759325)-(v15*-0.29134199417572776))>0.0010562843616691592)))
        save(v16, r5)
        play("9097165523371219333", "D1/drive")
        wait(11, "D1/acquisition")
        measure("5524603356640612863", "D1/acquisition", None, dual_demod.full("cos", "sin", v17), dual_demod.full("minus_sin", "cos", v18))
        assign(v19, Cast.to_int((((v17*0.6944883250671872)-(v18*-0.7195039724319616))>0.001952998167648245)))
        r6 = declare_stream()
        save(v19, r6)
        wait(251, "D1/acquisition")
        measure("5524603356640612863", "D1/acquisition", None, dual_demod.full("cos", "sin", v17), dual_demod.full("minus_sin", "cos", v18))
        assign(v19, Cast.to_int((((v17*0.6944883250671872)-(v18*-0.7195039724319616))>0.001952998167648245)))
        save(v19, r6)
        play("-7395719825647265576", "D2/drive")
        wait(11, "D2/acquisition")
        measure("1029718134435345812", "D2/acquisition", None, dual_demod.full("cos", "sin", v20), dual_demod.full("minus_sin", "cos", v21))
        assign(v22, Cast.to_int((((v20*0.17395653039171746)-(v21*-0.9847533323295106))>0.0034645063414544194)))
        r7 = declare_stream()
        save(v22, r7)
        wait(251, "D2/acquisition")
        measure("1029718134435345812", "D2/acquisition", None, dual_demod.full("cos", "sin", v20), dual_demod.full("minus_sin", "cos", v21))
        assign(v22, Cast.to_int((((v20*0.17395653039171746)-(v21*-0.9847533323295106))>0.0034645063414544194)))
        save(v22, r7)
        play("8986332877144196991", "D3/drive")
        wait(11, "D3/acquisition")
        measure("6261815664588527823", "D3/acquisition", None, dual_demod.full("cos", "sin", v23), dual_demod.full("minus_sin", "cos", v24))
        assign(v25, Cast.to_int((((v23*0.7989861892381119)-(v24*-0.6013493738308539))>0.0022424279381051404)))
        r8 = declare_stream()
        save(v25, r8)
        wait(251, "D3/acquisition")
        measure("6261815664588527823", "D3/acquisition", None, dual_demod.full("cos", "sin", v23), dual_demod.full("minus_sin", "cos", v24))
        assign(v25, Cast.to_int((((v23*0.7989861892381119)-(v24*-0.6013493738308539))>0.0022424279381051404)))
        save(v25, r8)
        play("1672571126590852965", "D4/drive")
        wait(11, "D4/acquisition")
        measure("6671956485931387906", "D4/acquisition", None, dual_demod.full("cos", "sin", v26), dual_demod.full("minus_sin", "cos", v27))
        assign(v28, Cast.to_int((((v26*-0.7548906231950013)-(v27*-0.655850704819521))>0.0020330453601376305)))
        r9 = declare_stream()
        save(v28, r9)
        wait(251, "D4/acquisition")
        measure("6671956485931387906", "D4/acquisition", None, dual_demod.full("cos", "sin", v26), dual_demod.full("minus_sin", "cos", v27))
        assign(v28, Cast.to_int((((v26*-0.7548906231950013)-(v27*-0.655850704819521))>0.0020330453601376305)))
        save(v28, r9)
        play("7059028768878924406", "D5/drive")
        wait(11, "D5/acquisition")
        measure("-5221108505199109234", "D5/acquisition", None, dual_demod.full("cos", "sin", v29), dual_demod.full("minus_sin", "cos", v30))
        assign(v31, Cast.to_int((((v29*-0.9693172342922046)-(v30*-0.24581313899812443))>0.0030892145059463814)))
        r10 = declare_stream()
        save(v31, r10)
        wait(251, "D5/acquisition")
        measure("-5221108505199109234", "D5/acquisition", None, dual_demod.full("cos", "sin", v29), dual_demod.full("minus_sin", "cos", v30))
        assign(v31, Cast.to_int((((v29*-0.9693172342922046)-(v30*-0.24581313899812443))>0.0030892145059463814)))
        save(v31, r10)
        wait(50000, )
    with stream_processing():
        r1.buffer(2).buffer(5000).save("-3097983578057558870_B1|acquisition_shots")
        r2.buffer(2).buffer(5000).save("3329345518335900802_B2|acquisition_shots")
        r3.buffer(2).buffer(5000).save("-8777740371248684088_B3|acquisition_shots")
        r4.buffer(2).buffer(5000).save("6639288563090313839_B4|acquisition_shots")
        r5.buffer(2).buffer(5000).save("-1863676690395318626_B5|acquisition_shots")
        r6.buffer(2).buffer(5000).save("5524603356640612863_D1|acquisition_shots")
        r7.buffer(2).buffer(5000).save("1029718134435345812_D2|acquisition_shots")
        r8.buffer(2).buffer(5000).save("6261815664588527823_D3|acquisition_shots")
        r9.buffer(2).buffer(5000).save("6671956485931387906_D4|acquisition_shots")
        r10.buffer(2).buffer(5000).save("-5221108505199109234_D5|acquisition_shots")


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
                "7": {
                    "offset": 0.0,
                    "filter": {},
                },
                "8": {
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
                "9": {
                    "offset": 0.0,
                    "filter": {},
                },
                "10": {
                    "offset": 0.0,
                    "filter": {},
                },
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
                "1": {},
                "9": {},
                "5": {},
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
        "con6": {
            "type": "opx1",
            "analog_outputs": {
                "9": {
                    "offset": 0.0,
                    "filter": {},
                },
                "10": {
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
                "9": {},
                "7": {},
                "3": {},
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
                "5": {},
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
                "5": {
                    "LO_frequency": 6400000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "3": {
                    "LO_frequency": 5700000000.0,
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
        "octave5": {
            "connectivity": "con6",
            "RF_outputs": {
                "5": {
                    "LO_frequency": 5700000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "4": {
                    "LO_frequency": 5700000000.0,
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
            "RF_inputs": {},
        },
        "octave3": {
            "connectivity": "con3",
            "RF_outputs": {
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
        "D3/drive": {
            "RF_inputs": {
                "port": ('octave5', 5),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 9),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -42474814.0,
            "operations": {
                "8986332877144196991": "8986332877144196991",
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
                "4843395743109475609": "4843395743109475609",
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
                "-6517581333074707223": "-6517581333074707223",
            },
        },
        "D2/drive": {
            "RF_inputs": {
                "port": ('octave5', 4),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 7),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -131911418.0,
            "operations": {
                "-7395719825647265576": "-7395719825647265576",
            },
        },
        "D4/drive": {
            "RF_inputs": {
                "port": ('octave6', 5),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con8', 9),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -151379236.0,
            "operations": {
                "1672571126590852965": "1672571126590852965",
            },
        },
        "D5/drive": {
            "RF_inputs": {
                "port": ('octave6', 3),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con8', 5),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -167659616.0,
            "operations": {
                "7059028768878924406": "7059028768878924406",
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
                "1738384850733880654": "1738384850733880654",
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
                "3336423412446418861": "3336423412446418861",
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
                "740409870800413924": "740409870800413924",
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
            "intermediate_frequency": -140843611.0,
            "operations": {
                "9097165523371219333": "9097165523371219333",
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
        "740409870800413924": {
            "length": 40,
            "waveforms": {
                "I": "740409870800413924_i",
                "Q": "740409870800413924_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6517581333074707223": {
            "length": 40,
            "waveforms": {
                "I": "-6517581333074707223_i",
                "Q": "-6517581333074707223_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3336423412446418861": {
            "length": 40,
            "waveforms": {
                "I": "3336423412446418861_i",
                "Q": "3336423412446418861_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1738384850733880654": {
            "length": 40,
            "waveforms": {
                "I": "1738384850733880654_i",
                "Q": "1738384850733880654_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4843395743109475609": {
            "length": 40,
            "waveforms": {
                "I": "4843395743109475609_i",
                "Q": "4843395743109475609_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9097165523371219333": {
            "length": 40,
            "waveforms": {
                "I": "9097165523371219333_i",
                "Q": "9097165523371219333_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7395719825647265576": {
            "length": 40,
            "waveforms": {
                "I": "-7395719825647265576_i",
                "Q": "-7395719825647265576_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8986332877144196991": {
            "length": 40,
            "waveforms": {
                "I": "8986332877144196991_i",
                "Q": "8986332877144196991_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1672571126590852965": {
            "length": 40,
            "waveforms": {
                "I": "1672571126590852965_i",
                "Q": "1672571126590852965_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7059028768878924406": {
            "length": 40,
            "waveforms": {
                "I": "7059028768878924406_i",
                "Q": "7059028768878924406_q",
            },
            "digital_marker": "ON",
            "operation": "control",
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
        "740409870800413924_i": {
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "type": "arbitrary",
        },
        "740409870800413924_q": {
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "type": "arbitrary",
        },
        "-6517581333074707223_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-6517581333074707223_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "3336423412446418861_i": {
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "type": "arbitrary",
        },
        "3336423412446418861_q": {
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "type": "arbitrary",
        },
        "1738384850733880654_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "1738384850733880654_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "4843395743109475609_i": {
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "type": "arbitrary",
        },
        "4843395743109475609_q": {
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
            "type": "arbitrary",
        },
        "9097165523371219333_i": {
            "samples": [0.0021186376713302124, 0.0028509386024640963, 0.003776880008616207, 0.004925980170730048, 0.006325083741317202, 0.007995655040984588, 0.009950753473266662, 0.01219191801292339, 0.014706260305648729, 0.01746411622352052, 0.020417620422965944, 0.023500537054216276, 0.026629597209224802, 0.029707462422348698, 0.0326272645347187, 0.03527848451386975, 0.03755375128403387, 0.039355993437638064, 0.04060528677486101] + [0.04124472699807034] * 2 + [0.04060528677486101, 0.039355993437638064, 0.03755375128403387, 0.03527848451386975, 0.0326272645347187, 0.029707462422348698, 0.026629597209224802, 0.023500537054216276, 0.020417620422965944, 0.01746411622352052, 0.014706260305648729, 0.01219191801292339, 0.009950753473266662, 0.007995655040984588, 0.006325083741317202, 0.004925980170730048, 0.003776880008616207, 0.0028509386024640963, 0.0021186376713302124],
            "type": "arbitrary",
        },
        "9097165523371219333_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-7395719825647265576_i": {
            "samples": [0.0027272090608372736, 0.0036698609175815993, 0.004861775810266832, 0.006340951044585605, 0.008141942307220602, 0.010292379471101983, 0.012809073208545387, 0.01569400455952125, 0.018930583034245323, 0.022480623586002974, 0.026282511715789308, 0.030250985553636676, 0.03427885748385031, 0.03824082890107573, 0.04199933413510552, 0.045412107941243805, 0.04834093727123376, 0.05066086728930345, 0.052269015843925765] + [0.05309213307354877] * 2 + [0.052269015843925765, 0.05066086728930345, 0.04834093727123376, 0.045412107941243805, 0.04199933413510552, 0.03824082890107573, 0.03427885748385031, 0.030250985553636676, 0.026282511715789308, 0.022480623586002974, 0.018930583034245323, 0.01569400455952125, 0.012809073208545387, 0.010292379471101983, 0.008141942307220602, 0.006340951044585605, 0.004861775810266832, 0.0036698609175815993, 0.0027272090608372736],
            "type": "arbitrary",
        },
        "-7395719825647265576_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "8986332877144196991_i": {
            "samples": [0.0034887867867250608, 0.0046946757629379035, 0.006219434897913944, 0.008111672308990145, 0.010415593416585486, 0.013166543782205267, 0.01638602848673711, 0.020076581778901467, 0.024216980246685033, 0.028758375604732076, 0.033621947401363345, 0.03869862424574704, 0.04385128619988264, 0.04891964481172841, 0.053727718965858144, 0.05809351560826196, 0.061840225464053045, 0.06480799984900742, 0.06686522659741626] + [0.06791820070045508] * 2 + [0.06686522659741626, 0.06480799984900742, 0.061840225464053045, 0.05809351560826196, 0.053727718965858144, 0.04891964481172841, 0.04385128619988264, 0.03869862424574704, 0.033621947401363345, 0.028758375604732076, 0.024216980246685033, 0.020076581778901467, 0.01638602848673711, 0.013166543782205267, 0.010415593416585486, 0.008111672308990145, 0.006219434897913944, 0.0046946757629379035, 0.0034887867867250608],
            "type": "arbitrary",
        },
        "8986332877144196991_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "1672571126590852965_i": {
            "samples": [0.0040192528784384835, 0.005408495911908692, 0.007165092951744012, 0.009345042924638804, 0.011999272635274172, 0.015168501897873431, 0.018877505616591662, 0.02312920336980583, 0.027899144749669473, 0.033131054144193386, 0.03873412654101709, 0.044582706367485916, 0.05051882475384921, 0.056357821569914875, 0.06189695797035737, 0.06692656906279397, 0.07124296192172763, 0.07466198305098413, 0.07703200880366262] + [0.07824508643014971] * 2 + [0.07703200880366262, 0.07466198305098413, 0.07124296192172763, 0.06692656906279397, 0.06189695797035737, 0.056357821569914875, 0.05051882475384921, 0.044582706367485916, 0.03873412654101709, 0.033131054144193386, 0.027899144749669473, 0.02312920336980583, 0.018877505616591662, 0.015168501897873431, 0.011999272635274172, 0.009345042924638804, 0.007165092951744012, 0.005408495911908692, 0.0040192528784384835],
            "type": "arbitrary",
        },
        "1672571126590852965_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "7059028768878924406_i": {
            "samples": [0.003093069542748061, 0.004162180007867902, 0.005513992637509387, 0.007191602150970744, 0.009234199948552667, 0.011673122505209537, 0.014527435678150203, 0.017799386267769814, 0.02147015813731236, 0.025496443640628707, 0.029808362571980176, 0.03430921501314571, 0.038877433918083196, 0.04337091162605768, 0.04763362776050308, 0.05150423191316526, 0.05482596948238481, 0.05745712269437778, 0.05928100755379136] + [0.06021454758547358] * 2 + [0.05928100755379136, 0.05745712269437778, 0.05482596948238481, 0.05150423191316526, 0.04763362776050308, 0.04337091162605768, 0.038877433918083196, 0.03430921501314571, 0.029808362571980176, 0.025496443640628707, 0.02147015813731236, 0.017799386267769814, 0.014527435678150203, 0.011673122505209537, 0.009234199948552667, 0.007191602150970744, 0.005513992637509387, 0.004162180007867902, 0.003093069542748061],
            "type": "arbitrary",
        },
        "7059028768878924406_q": {
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
                "9": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "10": {
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
                "9": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "5": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
            },
            "digital_inputs": {},
        },
        "con6": {
            "type": "opx1",
            "analog_outputs": {
                "9": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "10": {
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
                "9": {
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
                "mixer": "B1/acquisition_mixer_7e0",
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
                "mixer": "B3/acquisition_mixer_7f0",
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
                "mixer": "B5/acquisition_mixer_3a1",
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
                "mixer": "D3/acquisition_mixer_195",
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
                "mixer": "B2/acquisition_mixer_4d2",
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
                "mixer": "B4/acquisition_mixer_391",
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
                "mixer": "D1/acquisition_mixer_287",
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
                "mixer": "D2/acquisition_mixer_92a",
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
                "mixer": "D4/acquisition_mixer_c76",
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
                "mixer": "D5/acquisition_mixer_14b",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 178420035.0,
        },
        "D3/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 1, 9),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "8986332877144196991": "8986332877144196991",
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
                "I": ('con6', 1, 9),
                "Q": ('con6', 1, 10),
                "mixer": "D3/drive_mixer_f92",
                "lo_frequency": 5700000000.0,
            },
            "intermediate_frequency": -42474814.0,
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
                "4843395743109475609": "4843395743109475609",
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
                "I": ('con3', 1, 5),
                "Q": ('con3', 1, 6),
                "mixer": "B5/drive_mixer_d5b",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": -157953677.0,
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
                "-6517581333074707223": "-6517581333074707223",
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
                "mixer": "B2/drive_mixer_e8c",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
        },
        "D2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "-7395719825647265576": "-7395719825647265576",
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
                "I": ('con6', 1, 7),
                "Q": ('con6', 1, 8),
                "mixer": "D2/drive_mixer_dd3",
                "lo_frequency": 5700000000.0,
            },
            "intermediate_frequency": -131911418.0,
        },
        "D4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con8', 1, 9),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "1672571126590852965": "1672571126590852965",
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
                "I": ('con8', 1, 9),
                "Q": ('con8', 1, 10),
                "mixer": "D4/drive_mixer_f2c",
                "lo_frequency": 6400000000.0,
            },
            "intermediate_frequency": -151379236.0,
        },
        "D5/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con8', 1, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "7059028768878924406": "7059028768878924406",
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
                "I": ('con8', 1, 5),
                "Q": ('con8', 1, 6),
                "mixer": "D5/drive_mixer_3f3",
                "lo_frequency": 5700000000.0,
            },
            "intermediate_frequency": -167659616.0,
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
                "1738384850733880654": "1738384850733880654",
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
                "mixer": "B4/drive_mixer_8ba",
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
                "3336423412446418861": "3336423412446418861",
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
                "mixer": "B3/drive_mixer_16a",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "740409870800413924": "740409870800413924",
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
                "mixer": "B1/drive_mixer_ee8",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
        },
        "D1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "9097165523371219333": "9097165523371219333",
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
                "I": ('con6', 1, 3),
                "Q": ('con6', 1, 4),
                "mixer": "D1/drive_mixer_79d",
                "lo_frequency": 5100000000.0,
            },
            "intermediate_frequency": -140843611.0,
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
        "740409870800413924": {
            "length": 40,
            "waveforms": {
                "I": "740409870800413924_i",
                "Q": "740409870800413924_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6517581333074707223": {
            "length": 40,
            "waveforms": {
                "I": "-6517581333074707223_i",
                "Q": "-6517581333074707223_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3336423412446418861": {
            "length": 40,
            "waveforms": {
                "I": "3336423412446418861_i",
                "Q": "3336423412446418861_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1738384850733880654": {
            "length": 40,
            "waveforms": {
                "I": "1738384850733880654_i",
                "Q": "1738384850733880654_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4843395743109475609": {
            "length": 40,
            "waveforms": {
                "I": "4843395743109475609_i",
                "Q": "4843395743109475609_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9097165523371219333": {
            "length": 40,
            "waveforms": {
                "I": "9097165523371219333_i",
                "Q": "9097165523371219333_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7395719825647265576": {
            "length": 40,
            "waveforms": {
                "I": "-7395719825647265576_i",
                "Q": "-7395719825647265576_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8986332877144196991": {
            "length": 40,
            "waveforms": {
                "I": "8986332877144196991_i",
                "Q": "8986332877144196991_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1672571126590852965": {
            "length": 40,
            "waveforms": {
                "I": "1672571126590852965_i",
                "Q": "1672571126590852965_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7059028768878924406": {
            "length": 40,
            "waveforms": {
                "I": "7059028768878924406_i",
                "Q": "7059028768878924406_q",
            },
            "integration_weights": {},
            "operation": "control",
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
        "740409870800413924_i": {
            "type": "arbitrary",
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "740409870800413924_q": {
            "type": "arbitrary",
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6517581333074707223_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6517581333074707223_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3336423412446418861_i": {
            "type": "arbitrary",
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3336423412446418861_q": {
            "type": "arbitrary",
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1738384850733880654_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1738384850733880654_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4843395743109475609_i": {
            "type": "arbitrary",
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4843395743109475609_q": {
            "type": "arbitrary",
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9097165523371219333_i": {
            "type": "arbitrary",
            "samples": [0.0021186376713302124, 0.0028509386024640963, 0.003776880008616207, 0.004925980170730048, 0.006325083741317202, 0.007995655040984588, 0.009950753473266662, 0.01219191801292339, 0.014706260305648729, 0.01746411622352052, 0.020417620422965944, 0.023500537054216276, 0.026629597209224802, 0.029707462422348698, 0.0326272645347187, 0.03527848451386975, 0.03755375128403387, 0.039355993437638064, 0.04060528677486101] + [0.04124472699807034] * 2 + [0.04060528677486101, 0.039355993437638064, 0.03755375128403387, 0.03527848451386975, 0.0326272645347187, 0.029707462422348698, 0.026629597209224802, 0.023500537054216276, 0.020417620422965944, 0.01746411622352052, 0.014706260305648729, 0.01219191801292339, 0.009950753473266662, 0.007995655040984588, 0.006325083741317202, 0.004925980170730048, 0.003776880008616207, 0.0028509386024640963, 0.0021186376713302124],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9097165523371219333_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7395719825647265576_i": {
            "type": "arbitrary",
            "samples": [0.0027272090608372736, 0.0036698609175815993, 0.004861775810266832, 0.006340951044585605, 0.008141942307220602, 0.010292379471101983, 0.012809073208545387, 0.01569400455952125, 0.018930583034245323, 0.022480623586002974, 0.026282511715789308, 0.030250985553636676, 0.03427885748385031, 0.03824082890107573, 0.04199933413510552, 0.045412107941243805, 0.04834093727123376, 0.05066086728930345, 0.052269015843925765] + [0.05309213307354877] * 2 + [0.052269015843925765, 0.05066086728930345, 0.04834093727123376, 0.045412107941243805, 0.04199933413510552, 0.03824082890107573, 0.03427885748385031, 0.030250985553636676, 0.026282511715789308, 0.022480623586002974, 0.018930583034245323, 0.01569400455952125, 0.012809073208545387, 0.010292379471101983, 0.008141942307220602, 0.006340951044585605, 0.004861775810266832, 0.0036698609175815993, 0.0027272090608372736],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7395719825647265576_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8986332877144196991_i": {
            "type": "arbitrary",
            "samples": [0.0034887867867250608, 0.0046946757629379035, 0.006219434897913944, 0.008111672308990145, 0.010415593416585486, 0.013166543782205267, 0.01638602848673711, 0.020076581778901467, 0.024216980246685033, 0.028758375604732076, 0.033621947401363345, 0.03869862424574704, 0.04385128619988264, 0.04891964481172841, 0.053727718965858144, 0.05809351560826196, 0.061840225464053045, 0.06480799984900742, 0.06686522659741626] + [0.06791820070045508] * 2 + [0.06686522659741626, 0.06480799984900742, 0.061840225464053045, 0.05809351560826196, 0.053727718965858144, 0.04891964481172841, 0.04385128619988264, 0.03869862424574704, 0.033621947401363345, 0.028758375604732076, 0.024216980246685033, 0.020076581778901467, 0.01638602848673711, 0.013166543782205267, 0.010415593416585486, 0.008111672308990145, 0.006219434897913944, 0.0046946757629379035, 0.0034887867867250608],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8986332877144196991_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1672571126590852965_i": {
            "type": "arbitrary",
            "samples": [0.0040192528784384835, 0.005408495911908692, 0.007165092951744012, 0.009345042924638804, 0.011999272635274172, 0.015168501897873431, 0.018877505616591662, 0.02312920336980583, 0.027899144749669473, 0.033131054144193386, 0.03873412654101709, 0.044582706367485916, 0.05051882475384921, 0.056357821569914875, 0.06189695797035737, 0.06692656906279397, 0.07124296192172763, 0.07466198305098413, 0.07703200880366262] + [0.07824508643014971] * 2 + [0.07703200880366262, 0.07466198305098413, 0.07124296192172763, 0.06692656906279397, 0.06189695797035737, 0.056357821569914875, 0.05051882475384921, 0.044582706367485916, 0.03873412654101709, 0.033131054144193386, 0.027899144749669473, 0.02312920336980583, 0.018877505616591662, 0.015168501897873431, 0.011999272635274172, 0.009345042924638804, 0.007165092951744012, 0.005408495911908692, 0.0040192528784384835],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1672571126590852965_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7059028768878924406_i": {
            "type": "arbitrary",
            "samples": [0.003093069542748061, 0.004162180007867902, 0.005513992637509387, 0.007191602150970744, 0.009234199948552667, 0.011673122505209537, 0.014527435678150203, 0.017799386267769814, 0.02147015813731236, 0.025496443640628707, 0.029808362571980176, 0.03430921501314571, 0.038877433918083196, 0.04337091162605768, 0.04763362776050308, 0.05150423191316526, 0.05482596948238481, 0.05745712269437778, 0.05928100755379136] + [0.06021454758547358] * 2 + [0.05928100755379136, 0.05745712269437778, 0.05482596948238481, 0.05150423191316526, 0.04763362776050308, 0.04337091162605768, 0.038877433918083196, 0.03430921501314571, 0.029808362571980176, 0.025496443640628707, 0.02147015813731236, 0.017799386267769814, 0.014527435678150203, 0.011673122505209537, 0.009234199948552667, 0.007191602150970744, 0.005513992637509387, 0.004162180007867902, 0.003093069542748061],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7059028768878924406_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
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
        "B1/acquisition_mixer_7e0": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_7f0": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B5/acquisition_mixer_3a1": [{'intermediate_frequency': 270679567.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "D3/acquisition_mixer_195": [{'intermediate_frequency': 27730627.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_4d2": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_391": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "D1/acquisition_mixer_287": [{'intermediate_frequency': -320310131.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D2/acquisition_mixer_92a": [{'intermediate_frequency': -80885347.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D4/acquisition_mixer_c76": [{'intermediate_frequency': 242937024.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D5/acquisition_mixer_14b": [{'intermediate_frequency': 178420035.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D3/drive_mixer_f92": [{'intermediate_frequency': -42474814.0, 'lo_frequency': 5700000000.0, 'correction': (1, 0, 0, 1)}],
        "B5/drive_mixer_d5b": [{'intermediate_frequency': -157953677.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_e8c": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "D2/drive_mixer_dd3": [{'intermediate_frequency': -131911418.0, 'lo_frequency': 5700000000.0, 'correction': (1, 0, 0, 1)}],
        "D4/drive_mixer_f2c": [{'intermediate_frequency': -151379236.0, 'lo_frequency': 6400000000.0, 'correction': (1, 0, 0, 1)}],
        "D5/drive_mixer_3f3": [{'intermediate_frequency': -167659616.0, 'lo_frequency': 5700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_8ba": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_16a": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_ee8": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "D1/drive_mixer_79d": [{'intermediate_frequency': -140843611.0, 'lo_frequency': 5100000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

