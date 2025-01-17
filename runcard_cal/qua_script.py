
# Single QUA script generated at 2025-01-17 19:05:58.621421
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B4/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-496555073634517914", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-275061014435802666", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("708271662546584572", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("7653273871375186899", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25540, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("6934414431395413295", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-6892478200131054945", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("1979703592571597910", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-3362500697304433508", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25539, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-3141006638105718260", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("538491304898876264", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("759985364097591512", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("3579070819987451919", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25538, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("4289962866924212949", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-6616817228906140386", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("1144925580492665896", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("6709216614126095060", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25537, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-7215209689493453240", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-2105960259572324082", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        play("3498786022822984025", "B4/drive")
        wait(11, "B4/flux")
        play("-6010382953312350754", "B4/flux")
        wait(46, "B4/drive")
        play("4259876652046545894", "B4/drive")
        wait(66, "B4/acquisition")
        measure("416824626841619673", "B4/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.5741899364498644)-(v3*0.818722124337495))>-0.0003871945431271703)))
        save(v4, r1)
        wait(25001, "B4/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B4/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(19).average().save("416824626841619673_B4|acquisition_shots")


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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
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
                "4": {
                    "LO_frequency": 6700000000.0,
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
            "operations": {
                "-496555073634517914": "-496555073634517914",
                "-275061014435802666": "-275061014435802666",
                "708271662546584572": "708271662546584572",
                "7653273871375186899": "7653273871375186899",
                "6934414431395413295": "6934414431395413295",
                "-6892478200131054945": "-6892478200131054945",
                "1979703592571597910": "1979703592571597910",
                "-3362500697304433508": "-3362500697304433508",
                "-3141006638105718260": "-3141006638105718260",
                "538491304898876264": "538491304898876264",
                "759985364097591512": "759985364097591512",
                "3579070819987451919": "3579070819987451919",
                "4289962866924212949": "4289962866924212949",
                "-6616817228906140386": "-6616817228906140386",
                "1144925580492665896": "1144925580492665896",
                "6709216614126095060": "6709216614126095060",
                "-7215209689493453240": "-7215209689493453240",
                "-2105960259572324082": "-2105960259572324082",
                "-6010382953312350754": "-6010382953312350754",
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
            "intermediate_frequency": 330298316.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "416824626841619673": "416824626841619673_B4/acquisition",
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
            "intermediate_frequency": 109678455.0,
            "operations": {
                "3498786022822984025": "3498786022822984025",
                "4259876652046545894": "4259876652046545894",
            },
        },
    },
    "pulses": {
        "3498786022822984025": {
            "length": 40,
            "waveforms": {
                "I": "3498786022822984025_i",
                "Q": "3498786022822984025_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8226251189239333718": {
            "length": 16,
            "waveforms": {
                "single": "-8226251189239333718",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "416824626841619673_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "3933238405037682965_i",
                "Q": "3933238405037682965_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-4419079282996710067": {
            "length": 16,
            "waveforms": {
                "single": "-4419079282996710067",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8407673412862125419": {
            "length": 16,
            "waveforms": {
                "single": "8407673412862125419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "814130534030054279": {
            "length": 16,
            "waveforms": {
                "single": "814130534030054279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5017471743584022921": {
            "length": 16,
            "waveforms": {
                "single": "-5017471743584022921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8253067432102998062": {
            "length": 16,
            "waveforms": {
                "single": "8253067432102998062",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3233384281231936390": {
            "length": 16,
            "waveforms": {
                "single": "3233384281231936390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4960466824579789208": {
            "length": 16,
            "waveforms": {
                "single": "-4960466824579789208",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2413497761445908288": {
            "length": 16,
            "waveforms": {
                "single": "2413497761445908288",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7033349203628991664": {
            "length": 16,
            "waveforms": {
                "single": "7033349203628991664",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2541213077377907097": {
            "length": 16,
            "waveforms": {
                "single": "-2541213077377907097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8238175939810094150": {
            "length": 16,
            "waveforms": {
                "single": "8238175939810094150",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-343453389374740234": {
            "length": 16,
            "waveforms": {
                "single": "-343453389374740234",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3982425365050628743": {
            "length": 16,
            "waveforms": {
                "single": "-3982425365050628743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4889756427652024112": {
            "length": 16,
            "waveforms": {
                "single": "4889756427652024112",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5111250486850739360": {
            "length": 16,
            "waveforms": {
                "single": "5111250486850739360",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5129964297631820477": {
            "length": 20,
            "waveforms": {
                "single": "-5129964297631820477",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7309010174853906223": {
            "length": 20,
            "waveforms": {
                "single": "7309010174853906223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3670038199178017714": {
            "length": 20,
            "waveforms": {
                "single": "3670038199178017714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5904524081828881047": {
            "length": 20,
            "waveforms": {
                "single": "-5904524081828881047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5683030022630165799": {
            "length": 24,
            "waveforms": {
                "single": "-5683030022630165799",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3706764393825714184": {
            "length": 24,
            "waveforms": {
                "single": "-3706764393825714184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3485270334626998936": {
            "length": 24,
            "waveforms": {
                "single": "-3485270334626998936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1702612746810797878": {
            "length": 24,
            "waveforms": {
                "single": "1702612746810797878",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-899732423250723287": {
            "length": 28,
            "waveforms": {
                "single": "-899732423250723287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3900372434813964741": {
            "length": 28,
            "waveforms": {
                "single": "3900372434813964741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3100330118231924552": {
            "length": 28,
            "waveforms": {
                "single": "-3100330118231924552",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5452695786994218772": {
            "length": 28,
            "waveforms": {
                "single": "-5452695786994218772",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6531237081779207922": {
            "length": 32,
            "waveforms": {
                "single": "6531237081779207922",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7745664092799987547": {
            "length": 32,
            "waveforms": {
                "single": "7745664092799987547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6893908074666940418": {
            "length": 32,
            "waveforms": {
                "single": "-6893908074666940418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1978273718035712437": {
            "length": 32,
            "waveforms": {
                "single": "1978273718035712437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2199767777234427685": {
            "length": 36,
            "waveforms": {
                "single": "2199767777234427685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8130604309195061931": {
            "length": 36,
            "waveforms": {
                "single": "8130604309195061931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5778238640432767711": {
            "length": 36,
            "waveforms": {
                "single": "5778238640432767711",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "758555489561706039": {
            "length": 36,
            "waveforms": {
                "single": "758555489561706039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4417649408460824594": {
            "length": 40,
            "waveforms": {
                "single": "-4417649408460824594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4196155349262109346": {
            "length": 40,
            "waveforms": {
                "single": "-4196155349262109346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5237535928246852696": {
            "length": 40,
            "waveforms": {
                "single": "-5237535928246852696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5016041869048137448": {
            "length": 40,
            "waveforms": {
                "single": "-5016041869048137448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4032709192065750210": {
            "length": 44,
            "waveforms": {
                "single": "-4032709192065750210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3234814155767821863": {
            "length": 44,
            "waveforms": {
                "single": "3234814155767821863",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2107390134108209555": {
            "length": 44,
            "waveforms": {
                "single": "-2107390134108209555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2414927635981793761": {
            "length": 44,
            "waveforms": {
                "single": "2414927635981793761",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2636421695180509009": {
            "length": 48,
            "waveforms": {
                "single": "2636421695180509009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3619754372162896247": {
            "length": 48,
            "waveforms": {
                "single": "3619754372162896247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7881987492718053042": {
            "length": 48,
            "waveforms": {
                "single": "-7881987492718053042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4740380897823222889": {
            "length": 48,
            "waveforms": {
                "single": "-4740380897823222889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8379352873499111398": {
            "length": 52,
            "waveforms": {
                "single": "-8379352873499111398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-173823584272119619": {
            "length": 52,
            "waveforms": {
                "single": "-173823584272119619",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6181593185495944535": {
            "length": 52,
            "waveforms": {
                "single": "-6181593185495944535",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-229523928489406585": {
            "length": 52,
            "waveforms": {
                "single": "-229523928489406585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2912082666405423568": {
            "length": 56,
            "waveforms": {
                "single": "2912082666405423568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7329132118077136269": {
            "length": 56,
            "waveforms": {
                "single": "-7329132118077136269",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5775407665756383929": {
            "length": 56,
            "waveforms": {
                "single": "5775407665756383929",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5575158909902154903": {
            "length": 56,
            "waveforms": {
                "single": "-5575158909902154903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7927524578664449123": {
            "length": 60,
            "waveforms": {
                "single": "-7927524578664449123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "101837386952794940": {
            "length": 60,
            "waveforms": {
                "single": "101837386952794940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7046839595781397267": {
            "length": 60,
            "waveforms": {
                "single": "7046839595781397267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4303726979877141565": {
            "length": 60,
            "waveforms": {
                "single": "-4303726979877141565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-496555073634517914": {
            "length": 64,
            "waveforms": {
                "single": "-496555073634517914",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-275061014435802666": {
            "length": 64,
            "waveforms": {
                "single": "-275061014435802666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "708271662546584572": {
            "length": 64,
            "waveforms": {
                "single": "708271662546584572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7653273871375186899": {
            "length": 64,
            "waveforms": {
                "single": "7653273871375186899",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6934414431395413295": {
            "length": 68,
            "waveforms": {
                "single": "6934414431395413295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6892478200131054945": {
            "length": 68,
            "waveforms": {
                "single": "-6892478200131054945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1979703592571597910": {
            "length": 68,
            "waveforms": {
                "single": "1979703592571597910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3362500697304433508": {
            "length": 68,
            "waveforms": {
                "single": "-3362500697304433508",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3141006638105718260": {
            "length": 72,
            "waveforms": {
                "single": "-3141006638105718260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "538491304898876264": {
            "length": 72,
            "waveforms": {
                "single": "538491304898876264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "759985364097591512": {
            "length": 72,
            "waveforms": {
                "single": "759985364097591512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3579070819987451919": {
            "length": 72,
            "waveforms": {
                "single": "3579070819987451919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4289962866924212949": {
            "length": 76,
            "waveforms": {
                "single": "4289962866924212949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6616817228906140386": {
            "length": 76,
            "waveforms": {
                "single": "-6616817228906140386",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1144925580492665896": {
            "length": 76,
            "waveforms": {
                "single": "1144925580492665896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6709216614126095060": {
            "length": 76,
            "waveforms": {
                "single": "6709216614126095060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7215209689493453240": {
            "length": 80,
            "waveforms": {
                "single": "-7215209689493453240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2105960259572324082": {
            "length": 80,
            "waveforms": {
                "single": "-2105960259572324082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6010382953312350754": {
            "length": 80,
            "waveforms": {
                "single": "-6010382953312350754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4259876652046545894": {
            "length": 40,
            "waveforms": {
                "I": "4259876652046545894_i",
                "Q": "4259876652046545894_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "3498786022822984025_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
        },
        "3498786022822984025_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "-8226251189239333718": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
        },
        "3933238405037682965_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "3933238405037682965_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4419079282996710067": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "8407673412862125419": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "814130534030054279": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-5017471743584022921": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "8253067432102998062": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3233384281231936390": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-4960466824579789208": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "2413497761445908288": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "7033349203628991664": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-2541213077377907097": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "8238175939810094150": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-343453389374740234": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3982425365050628743": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4889756427652024112": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
        },
        "5111250486850739360": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5129964297631820477": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7309010174853906223": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3670038199178017714": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5904524081828881047": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5683030022630165799": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3706764393825714184": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3485270334626998936": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
        },
        "1702612746810797878": {
            "sample": 0.175,
            "type": "constant",
        },
        "-899732423250723287": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3900372434813964741": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3100330118231924552": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-5452695786994218772": {
            "sample": 0.175,
            "type": "constant",
        },
        "6531237081779207922": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7745664092799987547": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6893908074666940418": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
        },
        "1978273718035712437": {
            "sample": 0.175,
            "type": "constant",
        },
        "2199767777234427685": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8130604309195061931": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5778238640432767711": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
        },
        "758555489561706039": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4417649408460824594": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4196155349262109346": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5237535928246852696": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-5016041869048137448": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4032709192065750210": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3234814155767821863": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2107390134108209555": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
        },
        "2414927635981793761": {
            "sample": 0.175,
            "type": "constant",
        },
        "2636421695180509009": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3619754372162896247": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7881987492718053042": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-4740380897823222889": {
            "sample": 0.175,
            "type": "constant",
        },
        "-8379352873499111398": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-173823584272119619": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6181593185495944535": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-229523928489406585": {
            "sample": 0.175,
            "type": "constant",
        },
        "2912082666405423568": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7329132118077136269": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5775407665756383929": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-5575158909902154903": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7927524578664449123": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "101837386952794940": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7046839595781397267": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-4303726979877141565": {
            "sample": 0.175,
            "type": "constant",
        },
        "-496555073634517914": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-275061014435802666": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "708271662546584572": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
        },
        "7653273871375186899": {
            "sample": 0.175,
            "type": "constant",
        },
        "6934414431395413295": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6892478200131054945": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1979703592571597910": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
        },
        "-3362500697304433508": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3141006638105718260": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "538491304898876264": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "759985364097591512": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
        },
        "3579070819987451919": {
            "sample": 0.175,
            "type": "constant",
        },
        "4289962866924212949": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6616817228906140386": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1144925580492665896": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
        },
        "6709216614126095060": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7215209689493453240": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2105960259572324082": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6010382953312350754": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
        },
        "4259876652046545894_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
        },
        "4259876652046545894_q": {
            "samples": [-0.00032311264588480903, -0.00041249837971684626, -0.0005169325628573798, -0.000635681039060383, -0.0007667620891775804, -0.000906744030872699, -0.0010506362701201647, -0.0011919133952948808, -0.0013227042327271718, -0.0014341631722800618, -0.0015170202748124885, -0.0015622817771297343, -0.0015620269226550444, -0.0015102246938684684, -0.0014034792875244936, -0.0012416096759145334, -0.0010279784823387492, -0.0007695087141126592, -0.0004763613256793087, -0.00016128764167269125, 0.00016128764167269125, 0.0004763613256793087, 0.0007695087141126592, 0.0010279784823387492, 0.0012416096759145334, 0.0014034792875244936, 0.0015102246938684684, 0.0015620269226550444, 0.0015622817771297343, 0.0015170202748124885, 0.0014341631722800618, 0.0013227042327271718, 0.0011919133952948808, 0.0010506362701201647, 0.000906744030872699, 0.0007667620891775804, 0.000635681039060383, 0.0005169325628573798, 0.00041249837971684626, 0.00032311264588480903],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
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
                        "feedforward": [1.0605851073784813, -0.9529722265285006],
                        "feedback": [0.890387119150019],
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
                "7": {
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
            "operations": {
                "-496555073634517914": "-496555073634517914",
                "-275061014435802666": "-275061014435802666",
                "708271662546584572": "708271662546584572",
                "7653273871375186899": "7653273871375186899",
                "6934414431395413295": "6934414431395413295",
                "-6892478200131054945": "-6892478200131054945",
                "1979703592571597910": "1979703592571597910",
                "-3362500697304433508": "-3362500697304433508",
                "-3141006638105718260": "-3141006638105718260",
                "538491304898876264": "538491304898876264",
                "759985364097591512": "759985364097591512",
                "3579070819987451919": "3579070819987451919",
                "4289962866924212949": "4289962866924212949",
                "-6616817228906140386": "-6616817228906140386",
                "1144925580492665896": "1144925580492665896",
                "6709216614126095060": "6709216614126095060",
                "-7215209689493453240": "-7215209689493453240",
                "-2105960259572324082": "-2105960259572324082",
                "-6010382953312350754": "-6010382953312350754",
            },
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
        "B4/acquisition": {
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
            "intermediate_frequency": 330298316.0,
            "operations": {
                "416824626841619673": "416824626841619673_B4/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B4/acquisition_mixer_9ef",
                "lo_frequency": 7370000000.0,
            },
        },
        "B4/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con3', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 109678455.0,
            "operations": {
                "3498786022822984025": "3498786022822984025",
                "4259876652046545894": "4259876652046545894",
            },
            "mixInputs": {
                "I": ('con3', 7),
                "Q": ('con3', 8),
                "mixer": "B4/drive_mixer_c1a",
                "lo_frequency": 6700000000.0,
            },
        },
    },
    "pulses": {
        "3498786022822984025": {
            "length": 40,
            "waveforms": {
                "I": "3498786022822984025_i",
                "Q": "3498786022822984025_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8226251189239333718": {
            "length": 16,
            "waveforms": {
                "single": "-8226251189239333718",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "416824626841619673_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "3933238405037682965_i",
                "Q": "3933238405037682965_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
        },
        "-4419079282996710067": {
            "length": 16,
            "waveforms": {
                "single": "-4419079282996710067",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8407673412862125419": {
            "length": 16,
            "waveforms": {
                "single": "8407673412862125419",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "814130534030054279": {
            "length": 16,
            "waveforms": {
                "single": "814130534030054279",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5017471743584022921": {
            "length": 16,
            "waveforms": {
                "single": "-5017471743584022921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8253067432102998062": {
            "length": 16,
            "waveforms": {
                "single": "8253067432102998062",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3233384281231936390": {
            "length": 16,
            "waveforms": {
                "single": "3233384281231936390",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4960466824579789208": {
            "length": 16,
            "waveforms": {
                "single": "-4960466824579789208",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2413497761445908288": {
            "length": 16,
            "waveforms": {
                "single": "2413497761445908288",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7033349203628991664": {
            "length": 16,
            "waveforms": {
                "single": "7033349203628991664",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2541213077377907097": {
            "length": 16,
            "waveforms": {
                "single": "-2541213077377907097",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8238175939810094150": {
            "length": 16,
            "waveforms": {
                "single": "8238175939810094150",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-343453389374740234": {
            "length": 16,
            "waveforms": {
                "single": "-343453389374740234",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3982425365050628743": {
            "length": 16,
            "waveforms": {
                "single": "-3982425365050628743",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4889756427652024112": {
            "length": 16,
            "waveforms": {
                "single": "4889756427652024112",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5111250486850739360": {
            "length": 16,
            "waveforms": {
                "single": "5111250486850739360",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5129964297631820477": {
            "length": 20,
            "waveforms": {
                "single": "-5129964297631820477",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7309010174853906223": {
            "length": 20,
            "waveforms": {
                "single": "7309010174853906223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3670038199178017714": {
            "length": 20,
            "waveforms": {
                "single": "3670038199178017714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5904524081828881047": {
            "length": 20,
            "waveforms": {
                "single": "-5904524081828881047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5683030022630165799": {
            "length": 24,
            "waveforms": {
                "single": "-5683030022630165799",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3706764393825714184": {
            "length": 24,
            "waveforms": {
                "single": "-3706764393825714184",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3485270334626998936": {
            "length": 24,
            "waveforms": {
                "single": "-3485270334626998936",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1702612746810797878": {
            "length": 24,
            "waveforms": {
                "single": "1702612746810797878",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-899732423250723287": {
            "length": 28,
            "waveforms": {
                "single": "-899732423250723287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3900372434813964741": {
            "length": 28,
            "waveforms": {
                "single": "3900372434813964741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3100330118231924552": {
            "length": 28,
            "waveforms": {
                "single": "-3100330118231924552",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5452695786994218772": {
            "length": 28,
            "waveforms": {
                "single": "-5452695786994218772",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6531237081779207922": {
            "length": 32,
            "waveforms": {
                "single": "6531237081779207922",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7745664092799987547": {
            "length": 32,
            "waveforms": {
                "single": "7745664092799987547",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6893908074666940418": {
            "length": 32,
            "waveforms": {
                "single": "-6893908074666940418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1978273718035712437": {
            "length": 32,
            "waveforms": {
                "single": "1978273718035712437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2199767777234427685": {
            "length": 36,
            "waveforms": {
                "single": "2199767777234427685",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8130604309195061931": {
            "length": 36,
            "waveforms": {
                "single": "8130604309195061931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5778238640432767711": {
            "length": 36,
            "waveforms": {
                "single": "5778238640432767711",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "758555489561706039": {
            "length": 36,
            "waveforms": {
                "single": "758555489561706039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4417649408460824594": {
            "length": 40,
            "waveforms": {
                "single": "-4417649408460824594",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4196155349262109346": {
            "length": 40,
            "waveforms": {
                "single": "-4196155349262109346",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5237535928246852696": {
            "length": 40,
            "waveforms": {
                "single": "-5237535928246852696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5016041869048137448": {
            "length": 40,
            "waveforms": {
                "single": "-5016041869048137448",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4032709192065750210": {
            "length": 44,
            "waveforms": {
                "single": "-4032709192065750210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3234814155767821863": {
            "length": 44,
            "waveforms": {
                "single": "3234814155767821863",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2107390134108209555": {
            "length": 44,
            "waveforms": {
                "single": "-2107390134108209555",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2414927635981793761": {
            "length": 44,
            "waveforms": {
                "single": "2414927635981793761",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2636421695180509009": {
            "length": 48,
            "waveforms": {
                "single": "2636421695180509009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3619754372162896247": {
            "length": 48,
            "waveforms": {
                "single": "3619754372162896247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7881987492718053042": {
            "length": 48,
            "waveforms": {
                "single": "-7881987492718053042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4740380897823222889": {
            "length": 48,
            "waveforms": {
                "single": "-4740380897823222889",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8379352873499111398": {
            "length": 52,
            "waveforms": {
                "single": "-8379352873499111398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-173823584272119619": {
            "length": 52,
            "waveforms": {
                "single": "-173823584272119619",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6181593185495944535": {
            "length": 52,
            "waveforms": {
                "single": "-6181593185495944535",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-229523928489406585": {
            "length": 52,
            "waveforms": {
                "single": "-229523928489406585",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2912082666405423568": {
            "length": 56,
            "waveforms": {
                "single": "2912082666405423568",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7329132118077136269": {
            "length": 56,
            "waveforms": {
                "single": "-7329132118077136269",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5775407665756383929": {
            "length": 56,
            "waveforms": {
                "single": "5775407665756383929",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5575158909902154903": {
            "length": 56,
            "waveforms": {
                "single": "-5575158909902154903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7927524578664449123": {
            "length": 60,
            "waveforms": {
                "single": "-7927524578664449123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "101837386952794940": {
            "length": 60,
            "waveforms": {
                "single": "101837386952794940",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7046839595781397267": {
            "length": 60,
            "waveforms": {
                "single": "7046839595781397267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4303726979877141565": {
            "length": 60,
            "waveforms": {
                "single": "-4303726979877141565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-496555073634517914": {
            "length": 64,
            "waveforms": {
                "single": "-496555073634517914",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-275061014435802666": {
            "length": 64,
            "waveforms": {
                "single": "-275061014435802666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "708271662546584572": {
            "length": 64,
            "waveforms": {
                "single": "708271662546584572",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7653273871375186899": {
            "length": 64,
            "waveforms": {
                "single": "7653273871375186899",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6934414431395413295": {
            "length": 68,
            "waveforms": {
                "single": "6934414431395413295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6892478200131054945": {
            "length": 68,
            "waveforms": {
                "single": "-6892478200131054945",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1979703592571597910": {
            "length": 68,
            "waveforms": {
                "single": "1979703592571597910",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3362500697304433508": {
            "length": 68,
            "waveforms": {
                "single": "-3362500697304433508",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3141006638105718260": {
            "length": 72,
            "waveforms": {
                "single": "-3141006638105718260",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "538491304898876264": {
            "length": 72,
            "waveforms": {
                "single": "538491304898876264",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "759985364097591512": {
            "length": 72,
            "waveforms": {
                "single": "759985364097591512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3579070819987451919": {
            "length": 72,
            "waveforms": {
                "single": "3579070819987451919",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4289962866924212949": {
            "length": 76,
            "waveforms": {
                "single": "4289962866924212949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6616817228906140386": {
            "length": 76,
            "waveforms": {
                "single": "-6616817228906140386",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1144925580492665896": {
            "length": 76,
            "waveforms": {
                "single": "1144925580492665896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6709216614126095060": {
            "length": 76,
            "waveforms": {
                "single": "6709216614126095060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7215209689493453240": {
            "length": 80,
            "waveforms": {
                "single": "-7215209689493453240",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2105960259572324082": {
            "length": 80,
            "waveforms": {
                "single": "-2105960259572324082",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6010382953312350754": {
            "length": 80,
            "waveforms": {
                "single": "-6010382953312350754",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4259876652046545894": {
            "length": 40,
            "waveforms": {
                "I": "4259876652046545894_i",
                "Q": "4259876652046545894_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "3498786022822984025_i": {
            "samples": [0.00032311264588480914, 0.0004124983797168464, 0.0005169325628573801, 0.0006356810390603833, 0.0007667620891775807, 0.0009067440308726994, 0.0010506362701201654, 0.0011919133952948814, 0.0013227042327271727, 0.0014341631722800626, 0.0015170202748124896, 0.0015622817771297356, 0.001562026922655046, 0.0015102246938684702, 0.0014034792875244953, 0.0012416096759145354, 0.0010279784823387513, 0.0007695087141126614, 0.0004763613256793109, 0.00016128764167269353, -0.00016128764167268897, -0.00047636132567930646, -0.000769508714112657, -0.001027978482338747, -0.0012416096759145314, -0.0014034792875244919, -0.0015102246938684667, -0.0015620269226550429, -0.001562281777129733, -0.0015170202748124874, -0.001434163172280061, -0.001322704232727171, -0.0011919133952948801, -0.001050636270120164, -0.0009067440308726985, -0.0007667620891775801, -0.0006356810390603827, -0.0005169325628573796, -0.0004124983797168461, -0.0003231126458848089],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3498786022822984025_q": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8226251189239333718": {
            "samples": [0.175] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3933238405037682965_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "3933238405037682965_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4419079282996710067": {
            "samples": [0.175] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8407673412862125419": {
            "samples": [0.175] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "814130534030054279": {
            "samples": [0.175] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5017471743584022921": {
            "samples": [0.175] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8253067432102998062": {
            "samples": [0.175] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3233384281231936390": {
            "samples": [0.175] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4960466824579789208": {
            "samples": [0.175] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2413497761445908288": {
            "samples": [0.175] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7033349203628991664": {
            "samples": [0.175] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2541213077377907097": {
            "samples": [0.175] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8238175939810094150": {
            "samples": [0.175] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-343453389374740234": {
            "samples": [0.175] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3982425365050628743": {
            "samples": [0.175] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4889756427652024112": {
            "samples": [0.175] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5111250486850739360": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5129964297631820477": {
            "samples": [0.175] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7309010174853906223": {
            "samples": [0.175] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3670038199178017714": {
            "samples": [0.175] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5904524081828881047": {
            "sample": 0.175,
            "type": "constant",
        },
        "-5683030022630165799": {
            "samples": [0.175] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3706764393825714184": {
            "samples": [0.175] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3485270334626998936": {
            "samples": [0.175] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1702612746810797878": {
            "sample": 0.175,
            "type": "constant",
        },
        "-899732423250723287": {
            "samples": [0.175] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3900372434813964741": {
            "samples": [0.175] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3100330118231924552": {
            "samples": [0.175] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5452695786994218772": {
            "sample": 0.175,
            "type": "constant",
        },
        "6531237081779207922": {
            "samples": [0.175] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7745664092799987547": {
            "samples": [0.175] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6893908074666940418": {
            "samples": [0.175] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1978273718035712437": {
            "sample": 0.175,
            "type": "constant",
        },
        "2199767777234427685": {
            "samples": [0.175] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8130604309195061931": {
            "samples": [0.175] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5778238640432767711": {
            "samples": [0.175] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "758555489561706039": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4417649408460824594": {
            "samples": [0.175] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4196155349262109346": {
            "samples": [0.175] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5237535928246852696": {
            "samples": [0.175] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5016041869048137448": {
            "sample": 0.175,
            "type": "constant",
        },
        "-4032709192065750210": {
            "samples": [0.175] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3234814155767821863": {
            "samples": [0.175] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2107390134108209555": {
            "samples": [0.175] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2414927635981793761": {
            "sample": 0.175,
            "type": "constant",
        },
        "2636421695180509009": {
            "samples": [0.175] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3619754372162896247": {
            "samples": [0.175] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7881987492718053042": {
            "samples": [0.175] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4740380897823222889": {
            "sample": 0.175,
            "type": "constant",
        },
        "-8379352873499111398": {
            "samples": [0.175] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-173823584272119619": {
            "samples": [0.175] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6181593185495944535": {
            "samples": [0.175] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-229523928489406585": {
            "sample": 0.175,
            "type": "constant",
        },
        "2912082666405423568": {
            "samples": [0.175] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7329132118077136269": {
            "samples": [0.175] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5775407665756383929": {
            "samples": [0.175] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5575158909902154903": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7927524578664449123": {
            "samples": [0.175] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "101837386952794940": {
            "samples": [0.175] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7046839595781397267": {
            "samples": [0.175] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4303726979877141565": {
            "sample": 0.175,
            "type": "constant",
        },
        "-496555073634517914": {
            "samples": [0.175] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-275061014435802666": {
            "samples": [0.175] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "708271662546584572": {
            "samples": [0.175] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7653273871375186899": {
            "sample": 0.175,
            "type": "constant",
        },
        "6934414431395413295": {
            "samples": [0.175] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6892478200131054945": {
            "samples": [0.175] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1979703592571597910": {
            "samples": [0.175] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3362500697304433508": {
            "sample": 0.175,
            "type": "constant",
        },
        "-3141006638105718260": {
            "samples": [0.175] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "538491304898876264": {
            "samples": [0.175] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "759985364097591512": {
            "samples": [0.175] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3579070819987451919": {
            "sample": 0.175,
            "type": "constant",
        },
        "4289962866924212949": {
            "samples": [0.175] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6616817228906140386": {
            "samples": [0.175] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1144925580492665896": {
            "samples": [0.175] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6709216614126095060": {
            "sample": 0.175,
            "type": "constant",
        },
        "-7215209689493453240": {
            "samples": [0.175] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2105960259572324082": {
            "samples": [0.175] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6010382953312350754": {
            "samples": [0.175] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4259876652046545894_i": {
            "samples": [0.0019041597662755052, 0.002562327035148681, 0.0033945318030438945, 0.004427304100887551, 0.005684770992945484, 0.007186223883436177, 0.008943400121845278, 0.010957682886551467, 0.01321748856132099, 0.015696156032903856, 0.01835066555202265, 0.02112148658076548, 0.023933779845466133, 0.02670006083072293, 0.02932428005569802, 0.03170710675804564, 0.0337520394522566, 0.03537183364567531, 0.03649465617508045] + [0.03706936338549691] * 2 + [0.03649465617508045, 0.03537183364567531, 0.0337520394522566, 0.03170710675804564, 0.02932428005569802, 0.02670006083072293, 0.023933779845466133, 0.02112148658076548, 0.01835066555202265, 0.015696156032903856, 0.01321748856132099, 0.010957682886551467, 0.008943400121845278, 0.007186223883436177, 0.005684770992945484, 0.004427304100887551, 0.0033945318030438945, 0.002562327035148681, 0.0019041597662755052],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4259876652046545894_q": {
            "samples": [-0.00032311264588480903, -0.00041249837971684626, -0.0005169325628573798, -0.000635681039060383, -0.0007667620891775804, -0.000906744030872699, -0.0010506362701201647, -0.0011919133952948808, -0.0013227042327271718, -0.0014341631722800618, -0.0015170202748124885, -0.0015622817771297343, -0.0015620269226550444, -0.0015102246938684684, -0.0014034792875244936, -0.0012416096759145334, -0.0010279784823387492, -0.0007695087141126592, -0.0004763613256793087, -0.00016128764167269125, 0.00016128764167269125, 0.0004763613256793087, 0.0007695087141126592, 0.0010279784823387492, 0.0012416096759145334, 0.0014034792875244936, 0.0015102246938684684, 0.0015620269226550444, 0.0015622817771297343, 0.0015170202748124885, 0.0014341631722800618, 0.0013227042327271718, 0.0011919133952948808, 0.0010506362701201647, 0.000906744030872699, 0.0007667620891775804, 0.000635681039060383, 0.0005169325628573798, 0.00041249837971684626, 0.00032311264588480903],
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
        "cosine_weights_B4/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B4/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B4/acquisition_mixer_9ef": [{'intermediate_frequency': 330298316.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B4/drive_mixer_c1a": [{'intermediate_frequency': 109678455.0, 'lo_frequency': 6700000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

