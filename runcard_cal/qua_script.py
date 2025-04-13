
# Single QUA script generated at 2025-04-13 06:53:02.113289
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
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("5176814012209829707", "B1/drive")
        wait(11, "B1/acquisition")
        measure("-4383068751078855141", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967670294372607)-(v3*0.08034605794199916))>0.0007870074932508873)))
        r1 = declare_stream()
        save(v4, r1)
        wait(251, "B1/acquisition")
        measure("-4383068751078855141", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967670294372607)-(v3*0.08034605794199916))>0.0007870074932508873)))
        save(v4, r1)
        play("4964852096969565385", "B2/drive")
        wait(11, "B2/acquisition")
        measure("655023474242713013", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7359973353402354)-(v6*0.6769844328875466))>0.0024378669440833717)))
        r2 = declare_stream()
        save(v7, r2)
        wait(251, "B2/acquisition")
        measure("655023474242713013", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7359973353402354)-(v6*0.6769844328875466))>0.0024378669440833717)))
        save(v7, r2)
        play("9105045368679289218", "B3/drive")
        wait(11, "B3/acquisition")
        measure("8677196891534736965", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8321494180571197)-(v9*-0.5545514818546579))>0.0026636797237234713)))
        r3 = declare_stream()
        save(v10, r3)
        wait(251, "B3/acquisition")
        measure("8677196891534736965", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8321494180571197)-(v9*-0.5545514818546579))>0.0026636797237234713)))
        save(v10, r3)
        play("-5990111968500139490", "B4/drive")
        wait(11, "B4/acquisition")
        measure("-1708668195284224625", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.45141096231273753)-(v12*0.8923161676804294))>-0.000508161646537873)))
        r4 = declare_stream()
        save(v13, r4)
        wait(251, "B4/acquisition")
        measure("-1708668195284224625", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.45141096231273753)-(v12*0.8923161676804294))>-0.000508161646537873)))
        save(v13, r4)
        play("-5138561108344998364", "B5/drive")
        wait(11, "B5/acquisition")
        measure("3163872000775174377", "B5/acquisition", None, dual_demod.full("cos", "sin", v14), dual_demod.full("minus_sin", "cos", v15))
        assign(v16, Cast.to_int((((v14*0.9566189640759325)-(v15*-0.29134199417572776))>0.0010562843616691592)))
        r5 = declare_stream()
        save(v16, r5)
        wait(251, "B5/acquisition")
        measure("3163872000775174377", "B5/acquisition", None, dual_demod.full("cos", "sin", v14), dual_demod.full("minus_sin", "cos", v15))
        assign(v16, Cast.to_int((((v14*0.9566189640759325)-(v15*-0.29134199417572776))>0.0010562843616691592)))
        save(v16, r5)
        play("8099399498643982552", "D1/drive")
        wait(11, "D1/acquisition")
        measure("-5753346437254992459", "D1/acquisition", None, dual_demod.full("cos", "sin", v17), dual_demod.full("minus_sin", "cos", v18))
        assign(v19, Cast.to_int((((v17*0.6944883250671872)-(v18*-0.7195039724319616))>0.001952998167648245)))
        r6 = declare_stream()
        save(v19, r6)
        wait(251, "D1/acquisition")
        measure("-5753346437254992459", "D1/acquisition", None, dual_demod.full("cos", "sin", v17), dual_demod.full("minus_sin", "cos", v18))
        assign(v19, Cast.to_int((((v17*0.6944883250671872)-(v18*-0.7195039724319616))>0.001952998167648245)))
        save(v19, r6)
        play("-2723346263107630268", "D2/drive")
        wait(11, "D2/acquisition")
        measure("-5849874276475891382", "D2/acquisition", None, dual_demod.full("cos", "sin", v20), dual_demod.full("minus_sin", "cos", v21))
        assign(v22, Cast.to_int((((v20*0.17395653039171746)-(v21*-0.9847533323295106))>0.0034645063414544194)))
        r7 = declare_stream()
        save(v22, r7)
        wait(251, "D2/acquisition")
        measure("-5849874276475891382", "D2/acquisition", None, dual_demod.full("cos", "sin", v20), dual_demod.full("minus_sin", "cos", v21))
        assign(v22, Cast.to_int((((v20*0.17395653039171746)-(v21*-0.9847533323295106))>0.0034645063414544194)))
        save(v22, r7)
        play("3638702829804310671", "D3/drive")
        wait(11, "D3/acquisition")
        measure("-5310484156864437688", "D3/acquisition", None, dual_demod.full("cos", "sin", v23), dual_demod.full("minus_sin", "cos", v24))
        assign(v25, Cast.to_int((((v23*0.7989861892381119)-(v24*-0.6013493738308539))>0.0022424279381051404)))
        r8 = declare_stream()
        save(v25, r8)
        wait(251, "D3/acquisition")
        measure("-5310484156864437688", "D3/acquisition", None, dual_demod.full("cos", "sin", v23), dual_demod.full("minus_sin", "cos", v24))
        assign(v25, Cast.to_int((((v23*0.7989861892381119)-(v24*-0.6013493738308539))>0.0022424279381051404)))
        save(v25, r8)
        play("6344944689130488273", "D4/drive")
        wait(11, "D4/acquisition")
        measure("-2952602700002519212", "D4/acquisition", None, dual_demod.full("cos", "sin", v26), dual_demod.full("minus_sin", "cos", v27))
        assign(v28, Cast.to_int((((v26*-0.7548906231950013)-(v27*-0.655850704819521))>0.0020330453601376305)))
        r9 = declare_stream()
        save(v28, r9)
        wait(251, "D4/acquisition")
        measure("-2952602700002519212", "D4/acquisition", None, dual_demod.full("cos", "sin", v26), dual_demod.full("minus_sin", "cos", v27))
        assign(v28, Cast.to_int((((v26*-0.7548906231950013)-(v27*-0.655850704819521))>0.0020330453601376305)))
        save(v28, r9)
        play("1662905361167319497", "D5/drive")
        wait(11, "D5/acquisition")
        measure("-3969279117661301619", "D5/acquisition", None, dual_demod.full("cos", "sin", v29), dual_demod.full("minus_sin", "cos", v30))
        assign(v31, Cast.to_int((((v29*-0.9693172342922046)-(v30*-0.24581313899812443))>0.0030892145059463814)))
        r10 = declare_stream()
        save(v31, r10)
        wait(251, "D5/acquisition")
        measure("-3969279117661301619", "D5/acquisition", None, dual_demod.full("cos", "sin", v29), dual_demod.full("minus_sin", "cos", v30))
        assign(v31, Cast.to_int((((v29*-0.9693172342922046)-(v30*-0.24581313899812443))>0.0030892145059463814)))
        save(v31, r10)
        wait(25000, )
    with stream_processing():
        r1.buffer(2).buffer(2048).save("-4383068751078855141_B1|acquisition_shots")
        r2.buffer(2).buffer(2048).save("655023474242713013_B2|acquisition_shots")
        r3.buffer(2).buffer(2048).save("8677196891534736965_B3|acquisition_shots")
        r4.buffer(2).buffer(2048).save("-1708668195284224625_B4|acquisition_shots")
        r5.buffer(2).buffer(2048).save("3163872000775174377_B5|acquisition_shots")
        r6.buffer(2).buffer(2048).save("-5753346437254992459_D1|acquisition_shots")
        r7.buffer(2).buffer(2048).save("-5849874276475891382_D2|acquisition_shots")
        r8.buffer(2).buffer(2048).save("-5310484156864437688_D3|acquisition_shots")
        r9.buffer(2).buffer(2048).save("-2952602700002519212_D4|acquisition_shots")
        r10.buffer(2).buffer(2048).save("-3969279117661301619_D5|acquisition_shots")


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
                "3": {
                    "offset": 0.0,
                    "filter": {},
                },
                "4": {
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
                "9": {},
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
                "7": {},
                "1": {},
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
                "2": {
                    "LO_frequency": 5100000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
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
            },
            "RF_inputs": {},
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
                "3": {
                    "LO_frequency": 5900000000.0,
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
                "-4383068751078855141": "-4383068751078855141_B1/acquisition",
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
                "3163872000775174377": "3163872000775174377_B5/acquisition",
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
                "-5753346437254992459": "-5753346437254992459_D1/acquisition",
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
                "655023474242713013": "655023474242713013_B2/acquisition",
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
                "-2952602700002519212": "-2952602700002519212_D4/acquisition",
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
                "-5849874276475891382": "-5849874276475891382_D2/acquisition",
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
                "-3969279117661301619": "-3969279117661301619_D5/acquisition",
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
                "-5310484156864437688": "-5310484156864437688_D3/acquisition",
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
                "8677196891534736965": "8677196891534736965_B3/acquisition",
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
                "-1708668195284224625": "-1708668195284224625_B4/acquisition",
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
                "8099399498643982552": "8099399498643982552",
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
                "-5990111968500139490": "-5990111968500139490",
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
                "5176814012209829707": "5176814012209829707",
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
                "3638702829804310671": "3638702829804310671",
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
                "9105045368679289218": "9105045368679289218",
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
                "6344944689130488273": "6344944689130488273",
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
                "4964852096969565385": "4964852096969565385",
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
                "-5138561108344998364": "-5138561108344998364",
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
                "-2723346263107630268": "-2723346263107630268",
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
                "1662905361167319497": "1662905361167319497",
            },
        },
    },
    "pulses": {
        "-4383068751078855141_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-1617220326871862349_i",
                "Q": "-1617220326871862349_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "655023474242713013_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "2220890731398097629_i",
                "Q": "2220890731398097629_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "8677196891534736965_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5619782395189964918_i",
                "Q": "-5619782395189964918_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-1708668195284224625_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "2628584789746539538_i",
                "Q": "2628584789746539538_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "3163872000775174377_B5/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-5491450243856359976_i",
                "Q": "-5491450243856359976_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
        },
        "-5753346437254992459_D1/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "2113313894551515077_i",
                "Q": "2113313894551515077_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "-5849874276475891382_D2/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "-6074661186331094440_i",
                "Q": "-6074661186331094440_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D2/acquisition",
                "sin": "sine_weights_D2/acquisition",
                "minus_sin": "minus_sine_weights_D2/acquisition",
            },
        },
        "-5310484156864437688_D3/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "7939742262136837016_i",
                "Q": "7939742262136837016_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D3/acquisition",
                "sin": "sine_weights_D3/acquisition",
                "minus_sin": "minus_sine_weights_D3/acquisition",
            },
        },
        "-2952602700002519212_D4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8017658901281486308_i",
                "Q": "-8017658901281486308_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D4/acquisition",
                "sin": "sine_weights_D4/acquisition",
                "minus_sin": "minus_sine_weights_D4/acquisition",
            },
        },
        "-3969279117661301619_D5/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "591774120059458988_i",
                "Q": "591774120059458988_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D5/acquisition",
                "sin": "sine_weights_D5/acquisition",
                "minus_sin": "minus_sine_weights_D5/acquisition",
            },
        },
        "5176814012209829707": {
            "length": 40,
            "waveforms": {
                "I": "5176814012209829707_i",
                "Q": "5176814012209829707_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4964852096969565385": {
            "length": 40,
            "waveforms": {
                "I": "4964852096969565385_i",
                "Q": "4964852096969565385_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9105045368679289218": {
            "length": 40,
            "waveforms": {
                "I": "9105045368679289218_i",
                "Q": "9105045368679289218_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5990111968500139490": {
            "length": 40,
            "waveforms": {
                "I": "-5990111968500139490_i",
                "Q": "-5990111968500139490_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5138561108344998364": {
            "length": 40,
            "waveforms": {
                "I": "-5138561108344998364_i",
                "Q": "-5138561108344998364_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8099399498643982552": {
            "length": 40,
            "waveforms": {
                "I": "8099399498643982552_i",
                "Q": "8099399498643982552_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2723346263107630268": {
            "length": 40,
            "waveforms": {
                "I": "-2723346263107630268_i",
                "Q": "-2723346263107630268_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3638702829804310671": {
            "length": 40,
            "waveforms": {
                "I": "3638702829804310671_i",
                "Q": "3638702829804310671_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6344944689130488273": {
            "length": 40,
            "waveforms": {
                "I": "6344944689130488273_i",
                "Q": "6344944689130488273_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1662905361167319497": {
            "length": 40,
            "waveforms": {
                "I": "1662905361167319497_i",
                "Q": "1662905361167319497_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1617220326871862349_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-1617220326871862349_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2220890731398097629_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "2220890731398097629_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5619782395189964918_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-5619782395189964918_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2628584789746539538_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "2628584789746539538_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5491450243856359976_i": {
            "sample": 0.0035,
            "type": "constant",
        },
        "-5491450243856359976_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2113313894551515077_i": {
            "sample": 0.002,
            "type": "constant",
        },
        "2113313894551515077_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6074661186331094440_i": {
            "sample": 0.003,
            "type": "constant",
        },
        "-6074661186331094440_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7939742262136837016_i": {
            "sample": 0.0025,
            "type": "constant",
        },
        "7939742262136837016_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8017658901281486308_i": {
            "sample": 0.002,
            "type": "constant",
        },
        "-8017658901281486308_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "591774120059458988_i": {
            "sample": 0.0018,
            "type": "constant",
        },
        "591774120059458988_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "5176814012209829707_i": {
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "type": "arbitrary",
        },
        "5176814012209829707_q": {
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "type": "arbitrary",
        },
        "4964852096969565385_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "4964852096969565385_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "9105045368679289218_i": {
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "type": "arbitrary",
        },
        "9105045368679289218_q": {
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "type": "arbitrary",
        },
        "-5990111968500139490_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-5990111968500139490_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-5138561108344998364_i": {
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "type": "arbitrary",
        },
        "-5138561108344998364_q": {
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
            "type": "arbitrary",
        },
        "8099399498643982552_i": {
            "samples": [0.0021186376713302124, 0.0028509386024640963, 0.003776880008616207, 0.004925980170730048, 0.006325083741317202, 0.007995655040984588, 0.009950753473266662, 0.01219191801292339, 0.014706260305648729, 0.01746411622352052, 0.020417620422965944, 0.023500537054216276, 0.026629597209224802, 0.029707462422348698, 0.0326272645347187, 0.03527848451386975, 0.03755375128403387, 0.039355993437638064, 0.04060528677486101] + [0.04124472699807034] * 2 + [0.04060528677486101, 0.039355993437638064, 0.03755375128403387, 0.03527848451386975, 0.0326272645347187, 0.029707462422348698, 0.026629597209224802, 0.023500537054216276, 0.020417620422965944, 0.01746411622352052, 0.014706260305648729, 0.01219191801292339, 0.009950753473266662, 0.007995655040984588, 0.006325083741317202, 0.004925980170730048, 0.003776880008616207, 0.0028509386024640963, 0.0021186376713302124],
            "type": "arbitrary",
        },
        "8099399498643982552_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-2723346263107630268_i": {
            "samples": [0.0027272090608372736, 0.0036698609175815993, 0.004861775810266832, 0.006340951044585605, 0.008141942307220602, 0.010292379471101983, 0.012809073208545387, 0.01569400455952125, 0.018930583034245323, 0.022480623586002974, 0.026282511715789308, 0.030250985553636676, 0.03427885748385031, 0.03824082890107573, 0.04199933413510552, 0.045412107941243805, 0.04834093727123376, 0.05066086728930345, 0.052269015843925765] + [0.05309213307354877] * 2 + [0.052269015843925765, 0.05066086728930345, 0.04834093727123376, 0.045412107941243805, 0.04199933413510552, 0.03824082890107573, 0.03427885748385031, 0.030250985553636676, 0.026282511715789308, 0.022480623586002974, 0.018930583034245323, 0.01569400455952125, 0.012809073208545387, 0.010292379471101983, 0.008141942307220602, 0.006340951044585605, 0.004861775810266832, 0.0036698609175815993, 0.0027272090608372736],
            "type": "arbitrary",
        },
        "-2723346263107630268_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "3638702829804310671_i": {
            "samples": [0.0034887867867250608, 0.0046946757629379035, 0.006219434897913944, 0.008111672308990145, 0.010415593416585486, 0.013166543782205267, 0.01638602848673711, 0.020076581778901467, 0.024216980246685033, 0.028758375604732076, 0.033621947401363345, 0.03869862424574704, 0.04385128619988264, 0.04891964481172841, 0.053727718965858144, 0.05809351560826196, 0.061840225464053045, 0.06480799984900742, 0.06686522659741626] + [0.06791820070045508] * 2 + [0.06686522659741626, 0.06480799984900742, 0.061840225464053045, 0.05809351560826196, 0.053727718965858144, 0.04891964481172841, 0.04385128619988264, 0.03869862424574704, 0.033621947401363345, 0.028758375604732076, 0.024216980246685033, 0.020076581778901467, 0.01638602848673711, 0.013166543782205267, 0.010415593416585486, 0.008111672308990145, 0.006219434897913944, 0.0046946757629379035, 0.0034887867867250608],
            "type": "arbitrary",
        },
        "3638702829804310671_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "6344944689130488273_i": {
            "samples": [0.0040192528784384835, 0.005408495911908692, 0.007165092951744012, 0.009345042924638804, 0.011999272635274172, 0.015168501897873431, 0.018877505616591662, 0.02312920336980583, 0.027899144749669473, 0.033131054144193386, 0.03873412654101709, 0.044582706367485916, 0.05051882475384921, 0.056357821569914875, 0.06189695797035737, 0.06692656906279397, 0.07124296192172763, 0.07466198305098413, 0.07703200880366262] + [0.07824508643014971] * 2 + [0.07703200880366262, 0.07466198305098413, 0.07124296192172763, 0.06692656906279397, 0.06189695797035737, 0.056357821569914875, 0.05051882475384921, 0.044582706367485916, 0.03873412654101709, 0.033131054144193386, 0.027899144749669473, 0.02312920336980583, 0.018877505616591662, 0.015168501897873431, 0.011999272635274172, 0.009345042924638804, 0.007165092951744012, 0.005408495911908692, 0.0040192528784384835],
            "type": "arbitrary",
        },
        "6344944689130488273_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "1662905361167319497_i": {
            "samples": [0.003093069542748061, 0.004162180007867902, 0.005513992637509387, 0.007191602150970744, 0.009234199948552667, 0.011673122505209537, 0.014527435678150203, 0.017799386267769814, 0.02147015813731236, 0.025496443640628707, 0.029808362571980176, 0.03430921501314571, 0.038877433918083196, 0.04337091162605768, 0.04763362776050308, 0.05150423191316526, 0.05482596948238481, 0.05745712269437778, 0.05928100755379136] + [0.06021454758547358] * 2 + [0.05928100755379136, 0.05745712269437778, 0.05482596948238481, 0.05150423191316526, 0.04763362776050308, 0.04337091162605768, 0.038877433918083196, 0.03430921501314571, 0.029808362571980176, 0.025496443640628707, 0.02147015813731236, 0.017799386267769814, 0.014527435678150203, 0.011673122505209537, 0.009234199948552667, 0.007191602150970744, 0.005513992637509387, 0.004162180007867902, 0.003093069542748061],
            "type": "arbitrary",
        },
        "1662905361167319497_q": {
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
                "3": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
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
                "5": {
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
                "-4383068751078855141": "-4383068751078855141_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_72f",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "3163872000775174377": "3163872000775174377_B5/acquisition",
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
                "mixer": "B5/acquisition_mixer_6d2",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 270679567.0,
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
                "-5753346437254992459": "-5753346437254992459_D1/acquisition",
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
                "mixer": "D1/acquisition_mixer_a94",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -320310131.0,
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
                "655023474242713013": "655023474242713013_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_8bc",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-2952602700002519212": "-2952602700002519212_D4/acquisition",
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
                "mixer": "D4/acquisition_mixer_61c",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 242937024.0,
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
                "-5849874276475891382": "-5849874276475891382_D2/acquisition",
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
                "mixer": "D2/acquisition_mixer_ead",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -80885347.0,
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
                "-3969279117661301619": "-3969279117661301619_D5/acquisition",
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
                "mixer": "D5/acquisition_mixer_cd3",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 178420035.0,
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
                "-5310484156864437688": "-5310484156864437688_D3/acquisition",
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
                "mixer": "D3/acquisition_mixer_529",
                "lo_frequency": 7450000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 27730627.0,
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
                "8677196891534736965": "8677196891534736965_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_209",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "-1708668195284224625": "-1708668195284224625_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_2ea",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "8099399498643982552": "8099399498643982552",
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
                "mixer": "D1/drive_mixer_c26",
                "lo_frequency": 5100000000.0,
            },
            "intermediate_frequency": -140843611.0,
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
                "-5990111968500139490": "-5990111968500139490",
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
                "mixer": "B4/drive_mixer_94b",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "5176814012209829707": "5176814012209829707",
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
                "mixer": "B1/drive_mixer_361",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "3638702829804310671": "3638702829804310671",
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
                "mixer": "D3/drive_mixer_3c2",
                "lo_frequency": 5700000000.0,
            },
            "intermediate_frequency": -42474814.0,
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
                "9105045368679289218": "9105045368679289218",
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
                "mixer": "B3/drive_mixer_fec",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "6344944689130488273": "6344944689130488273",
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
                "mixer": "D4/drive_mixer_797",
                "lo_frequency": 6400000000.0,
            },
            "intermediate_frequency": -151379236.0,
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
                "4964852096969565385": "4964852096969565385",
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
                "mixer": "B2/drive_mixer_548",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "-5138561108344998364": "-5138561108344998364",
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
                "mixer": "B5/drive_mixer_923",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": -157953677.0,
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
                "-2723346263107630268": "-2723346263107630268",
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
                "mixer": "D2/drive_mixer_57b",
                "lo_frequency": 5700000000.0,
            },
            "intermediate_frequency": -131911418.0,
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
                "1662905361167319497": "1662905361167319497",
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
                "mixer": "D5/drive_mixer_356",
                "lo_frequency": 5700000000.0,
            },
            "intermediate_frequency": -167659616.0,
        },
    },
    "pulses": {
        "-4383068751078855141_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-1617220326871862349_i",
                "Q": "-1617220326871862349_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "655023474242713013_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "2220890731398097629_i",
                "Q": "2220890731398097629_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8677196891534736965_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5619782395189964918_i",
                "Q": "-5619782395189964918_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-1708668195284224625_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "2628584789746539538_i",
                "Q": "2628584789746539538_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3163872000775174377_B5/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-5491450243856359976_i",
                "Q": "-5491450243856359976_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B5/acquisition",
                "sin": "sine_weights_B5/acquisition",
                "minus_sin": "minus_sine_weights_B5/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5753346437254992459_D1/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "2113313894551515077_i",
                "Q": "2113313894551515077_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5849874276475891382_D2/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "-6074661186331094440_i",
                "Q": "-6074661186331094440_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D2/acquisition",
                "sin": "sine_weights_D2/acquisition",
                "minus_sin": "minus_sine_weights_D2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5310484156864437688_D3/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "7939742262136837016_i",
                "Q": "7939742262136837016_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D3/acquisition",
                "sin": "sine_weights_D3/acquisition",
                "minus_sin": "minus_sine_weights_D3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2952602700002519212_D4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8017658901281486308_i",
                "Q": "-8017658901281486308_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D4/acquisition",
                "sin": "sine_weights_D4/acquisition",
                "minus_sin": "minus_sine_weights_D4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-3969279117661301619_D5/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "591774120059458988_i",
                "Q": "591774120059458988_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_D5/acquisition",
                "sin": "sine_weights_D5/acquisition",
                "minus_sin": "minus_sine_weights_D5/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "5176814012209829707": {
            "length": 40,
            "waveforms": {
                "I": "5176814012209829707_i",
                "Q": "5176814012209829707_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4964852096969565385": {
            "length": 40,
            "waveforms": {
                "I": "4964852096969565385_i",
                "Q": "4964852096969565385_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9105045368679289218": {
            "length": 40,
            "waveforms": {
                "I": "9105045368679289218_i",
                "Q": "9105045368679289218_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5990111968500139490": {
            "length": 40,
            "waveforms": {
                "I": "-5990111968500139490_i",
                "Q": "-5990111968500139490_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5138561108344998364": {
            "length": 40,
            "waveforms": {
                "I": "-5138561108344998364_i",
                "Q": "-5138561108344998364_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8099399498643982552": {
            "length": 40,
            "waveforms": {
                "I": "8099399498643982552_i",
                "Q": "8099399498643982552_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2723346263107630268": {
            "length": 40,
            "waveforms": {
                "I": "-2723346263107630268_i",
                "Q": "-2723346263107630268_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3638702829804310671": {
            "length": 40,
            "waveforms": {
                "I": "3638702829804310671_i",
                "Q": "3638702829804310671_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6344944689130488273": {
            "length": 40,
            "waveforms": {
                "I": "6344944689130488273_i",
                "Q": "6344944689130488273_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1662905361167319497": {
            "length": 40,
            "waveforms": {
                "I": "1662905361167319497_i",
                "Q": "1662905361167319497_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-1617220326871862349_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-1617220326871862349_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2220890731398097629_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "2220890731398097629_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-5619782395189964918_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-5619782395189964918_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2628584789746539538_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "2628584789746539538_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-5491450243856359976_i": {
            "type": "constant",
            "sample": 0.0035,
        },
        "-5491450243856359976_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2113313894551515077_i": {
            "type": "constant",
            "sample": 0.002,
        },
        "2113313894551515077_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-6074661186331094440_i": {
            "type": "constant",
            "sample": 0.003,
        },
        "-6074661186331094440_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7939742262136837016_i": {
            "type": "constant",
            "sample": 0.0025,
        },
        "7939742262136837016_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-8017658901281486308_i": {
            "type": "constant",
            "sample": 0.002,
        },
        "-8017658901281486308_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "591774120059458988_i": {
            "type": "constant",
            "sample": 0.0018,
        },
        "591774120059458988_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "5176814012209829707_i": {
            "type": "arbitrary",
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5176814012209829707_q": {
            "type": "arbitrary",
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4964852096969565385_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4964852096969565385_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9105045368679289218_i": {
            "type": "arbitrary",
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9105045368679289218_q": {
            "type": "arbitrary",
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5990111968500139490_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5990111968500139490_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5138561108344998364_i": {
            "type": "arbitrary",
            "samples": [0.003210436758514374, 0.0043201148594094714, 0.0057232223217037635, 0.0074644891034601965, 0.009584593731431584, 0.012116061750124899, 0.015078682474966102, 0.018474787961693977, 0.022284848091033857, 0.026463911898514898, 0.030939447558358396, 0.03561108585231316, 0.0403526468455786, 0.045016630570441536, 0.049441096422242946, 0.05345857151539096, 0.0569063531597978, 0.059637346069048865, 0.06153043864748369] + [0.062499402064515215] * 2 + [0.06153043864748369, 0.059637346069048865, 0.0569063531597978, 0.05345857151539096, 0.049441096422242946, 0.045016630570441536, 0.0403526468455786, 0.03561108585231316, 0.030939447558358396, 0.026463911898514898, 0.022284848091033857, 0.018474787961693977, 0.015078682474966102, 0.012116061750124899, 0.009584593731431584, 0.0074644891034601965, 0.0057232223217037635, 0.0043201148594094714, 0.003210436758514374],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5138561108344998364_q": {
            "type": "arbitrary",
            "samples": [-0.00014672699247897722, -0.00018731748023220754, -0.00023474154053863093, -0.00028866578954787474, -0.000348190319149663, -0.0004117567860394008, -0.0004770989376844743, -0.0005412535535652532, -0.0006006462962036469, -0.000651260331877515, -0.0006888861370415736, -0.0007094396009640512, -0.0007093238703324363, -0.0006858002313465702, -0.0006373266335679754, -0.000563820871451389, -0.00046680992826396634, -0.0003494375746233332, -0.00021631794837005983, -7.324148679435377e-05, 7.324148679435377e-05, 0.00021631794837005983, 0.0003494375746233332, 0.00046680992826396634, 0.000563820871451389, 0.0006373266335679754, 0.0006858002313465702, 0.0007093238703324363, 0.0007094396009640512, 0.0006888861370415736, 0.000651260331877515, 0.0006006462962036469, 0.0005412535535652532, 0.0004770989376844743, 0.0004117567860394008, 0.000348190319149663, 0.00028866578954787474, 0.00023474154053863093, 0.00018731748023220754, 0.00014672699247897722],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8099399498643982552_i": {
            "type": "arbitrary",
            "samples": [0.0021186376713302124, 0.0028509386024640963, 0.003776880008616207, 0.004925980170730048, 0.006325083741317202, 0.007995655040984588, 0.009950753473266662, 0.01219191801292339, 0.014706260305648729, 0.01746411622352052, 0.020417620422965944, 0.023500537054216276, 0.026629597209224802, 0.029707462422348698, 0.0326272645347187, 0.03527848451386975, 0.03755375128403387, 0.039355993437638064, 0.04060528677486101] + [0.04124472699807034] * 2 + [0.04060528677486101, 0.039355993437638064, 0.03755375128403387, 0.03527848451386975, 0.0326272645347187, 0.029707462422348698, 0.026629597209224802, 0.023500537054216276, 0.020417620422965944, 0.01746411622352052, 0.014706260305648729, 0.01219191801292339, 0.009950753473266662, 0.007995655040984588, 0.006325083741317202, 0.004925980170730048, 0.003776880008616207, 0.0028509386024640963, 0.0021186376713302124],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8099399498643982552_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2723346263107630268_i": {
            "type": "arbitrary",
            "samples": [0.0027272090608372736, 0.0036698609175815993, 0.004861775810266832, 0.006340951044585605, 0.008141942307220602, 0.010292379471101983, 0.012809073208545387, 0.01569400455952125, 0.018930583034245323, 0.022480623586002974, 0.026282511715789308, 0.030250985553636676, 0.03427885748385031, 0.03824082890107573, 0.04199933413510552, 0.045412107941243805, 0.04834093727123376, 0.05066086728930345, 0.052269015843925765] + [0.05309213307354877] * 2 + [0.052269015843925765, 0.05066086728930345, 0.04834093727123376, 0.045412107941243805, 0.04199933413510552, 0.03824082890107573, 0.03427885748385031, 0.030250985553636676, 0.026282511715789308, 0.022480623586002974, 0.018930583034245323, 0.01569400455952125, 0.012809073208545387, 0.010292379471101983, 0.008141942307220602, 0.006340951044585605, 0.004861775810266832, 0.0036698609175815993, 0.0027272090608372736],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2723346263107630268_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3638702829804310671_i": {
            "type": "arbitrary",
            "samples": [0.0034887867867250608, 0.0046946757629379035, 0.006219434897913944, 0.008111672308990145, 0.010415593416585486, 0.013166543782205267, 0.01638602848673711, 0.020076581778901467, 0.024216980246685033, 0.028758375604732076, 0.033621947401363345, 0.03869862424574704, 0.04385128619988264, 0.04891964481172841, 0.053727718965858144, 0.05809351560826196, 0.061840225464053045, 0.06480799984900742, 0.06686522659741626] + [0.06791820070045508] * 2 + [0.06686522659741626, 0.06480799984900742, 0.061840225464053045, 0.05809351560826196, 0.053727718965858144, 0.04891964481172841, 0.04385128619988264, 0.03869862424574704, 0.033621947401363345, 0.028758375604732076, 0.024216980246685033, 0.020076581778901467, 0.01638602848673711, 0.013166543782205267, 0.010415593416585486, 0.008111672308990145, 0.006219434897913944, 0.0046946757629379035, 0.0034887867867250608],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3638702829804310671_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6344944689130488273_i": {
            "type": "arbitrary",
            "samples": [0.0040192528784384835, 0.005408495911908692, 0.007165092951744012, 0.009345042924638804, 0.011999272635274172, 0.015168501897873431, 0.018877505616591662, 0.02312920336980583, 0.027899144749669473, 0.033131054144193386, 0.03873412654101709, 0.044582706367485916, 0.05051882475384921, 0.056357821569914875, 0.06189695797035737, 0.06692656906279397, 0.07124296192172763, 0.07466198305098413, 0.07703200880366262] + [0.07824508643014971] * 2 + [0.07703200880366262, 0.07466198305098413, 0.07124296192172763, 0.06692656906279397, 0.06189695797035737, 0.056357821569914875, 0.05051882475384921, 0.044582706367485916, 0.03873412654101709, 0.033131054144193386, 0.027899144749669473, 0.02312920336980583, 0.018877505616591662, 0.015168501897873431, 0.011999272635274172, 0.009345042924638804, 0.007165092951744012, 0.005408495911908692, 0.0040192528784384835],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6344944689130488273_q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1662905361167319497_i": {
            "type": "arbitrary",
            "samples": [0.003093069542748061, 0.004162180007867902, 0.005513992637509387, 0.007191602150970744, 0.009234199948552667, 0.011673122505209537, 0.014527435678150203, 0.017799386267769814, 0.02147015813731236, 0.025496443640628707, 0.029808362571980176, 0.03430921501314571, 0.038877433918083196, 0.04337091162605768, 0.04763362776050308, 0.05150423191316526, 0.05482596948238481, 0.05745712269437778, 0.05928100755379136] + [0.06021454758547358] * 2 + [0.05928100755379136, 0.05745712269437778, 0.05482596948238481, 0.05150423191316526, 0.04763362776050308, 0.04337091162605768, 0.038877433918083196, 0.03430921501314571, 0.029808362571980176, 0.025496443640628707, 0.02147015813731236, 0.017799386267769814, 0.014527435678150203, 0.011673122505209537, 0.009234199948552667, 0.007191602150970744, 0.005513992637509387, 0.004162180007867902, 0.003093069542748061],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1662905361167319497_q": {
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
        "B1/acquisition_mixer_72f": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B5/acquisition_mixer_6d2": [{'intermediate_frequency': 270679567.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "D1/acquisition_mixer_a94": [{'intermediate_frequency': -320310131.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_8bc": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "D4/acquisition_mixer_61c": [{'intermediate_frequency': 242937024.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D2/acquisition_mixer_ead": [{'intermediate_frequency': -80885347.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D5/acquisition_mixer_cd3": [{'intermediate_frequency': 178420035.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "D3/acquisition_mixer_529": [{'intermediate_frequency': 27730627.0, 'lo_frequency': 7450000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_209": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_2ea": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "D1/drive_mixer_c26": [{'intermediate_frequency': -140843611.0, 'lo_frequency': 5100000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_94b": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_361": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "D3/drive_mixer_3c2": [{'intermediate_frequency': -42474814.0, 'lo_frequency': 5700000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_fec": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "D4/drive_mixer_797": [{'intermediate_frequency': -151379236.0, 'lo_frequency': 6400000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_548": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B5/drive_mixer_923": [{'intermediate_frequency': -157953677.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "D2/drive_mixer_57b": [{'intermediate_frequency': -131911418.0, 'lo_frequency': 5700000000.0, 'correction': (1, 0, 0, 1)}],
        "D5/drive_mixer_356": [{'intermediate_frequency': -167659616.0, 'lo_frequency': 5700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

