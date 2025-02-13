
# Single QUA script generated at 2025-02-13 08:49:55.277015
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
    v8 = declare(int, )
    a1 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    v9 = declare(fixed, )
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B2/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B4/acquisition")
    with for_(v1,0,(v1<256),(v1+1)):
        with for_each_((v8),(a1)):
            with for_(v9,-1.99,(v9>-1.3455720302264527),(v9*0.9959183673469388)):
                align()
                play("-673914686829155272", "B2/drive")
                play("5008191769018423137", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-1134637526927045191"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("3485213915256038185"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("8496929673084087283"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("8718423732282802531"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-6909234885536888678"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("-7530560653423582222"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("8563817751523675174"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("-2297350836396817876"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("-3779089091398245537"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("743228678691757779"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("121902910805064235"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-8071948195006661363"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("3162482425893639890"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-32703069954063122"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-5652694447804779252"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-1845522541562155601"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-7853292142785980517"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("352237146441011262"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("1778275057225151957"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("5585446963467775608"*amp(v9), "B4/flux")
                wait(11, "B2/acquisition")
                wait(11, "B4/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B2/acquisition")
                with else_():
                    wait((v8/4), "B2/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B4/acquisition")
                with else_():
                    wait((v8/4), "B4/acquisition")
                wait(4, "B2/acquisition")
                wait(4, "B4/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B4/drive")
                with else_():
                    wait((v8/4), "B4/drive")
                wait(4, "B4/drive")
                wait(11, "B2/acquisition")
                wait(11, "B4/acquisition")
                play("5008191769018423137", "B4/drive")
                measure("-3281072096949613271", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.737567608426209)-(v3*0.6752732950446377))>0.002483971740210947)))
                r1 = declare_stream()
                save(v4, r1)
                measure("7911743868580768313", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.48499080963062013)-(v6*0.8745192476863134))>-0.00041542394370853547)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(80).buffer(20).average().save("-3281072096949613271_B2|acquisition_shots")
        r2.buffer(80).buffer(20).average().save("7911743868580768313_B4|acquisition_shots")


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
                "-8363238826448225505": "-8363238826448225505",
                "4103708708466347947": "4103708708466347947",
                "-1134637526927045191": "-1134637526927045191",
                "3485213915256038185": "3485213915256038185",
                "8496929673084087283": "8496929673084087283",
                "8718423732282802531": "8718423732282802531",
                "-6909234885536888678": "-6909234885536888678",
                "-7530560653423582222": "-7530560653423582222",
                "8563817751523675174": "8563817751523675174",
                "-2297350836396817876": "-2297350836396817876",
                "-3779089091398245537": "-3779089091398245537",
                "743228678691757779": "743228678691757779",
                "121902910805064235": "121902910805064235",
                "-8071948195006661363": "-8071948195006661363",
                "3162482425893639890": "3162482425893639890",
                "-32703069954063122": "-32703069954063122",
                "-5652694447804779252": "-5652694447804779252",
                "-1845522541562155601": "-1845522541562155601",
                "-7853292142785980517": "-7853292142785980517",
                "352237146441011262": "352237146441011262",
                "1778275057225151957": "1778275057225151957",
                "5585446963467775608": "5585446963467775608",
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
            "intermediate_frequency": 330300527.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "7911743868580768313": "7911743868580768313_B4/acquisition",
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
                "5008191769018423137": "5008191769018423137",
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
                "-673914686829155272": "-673914686829155272",
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
                "-3281072096949613271": "-3281072096949613271_B2/acquisition",
            },
        },
    },
    "pulses": {
        "-673914686829155272": {
            "length": 40,
            "waveforms": {
                "I": "-673914686829155272_i",
                "Q": "-673914686829155272_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5008191769018423137": {
            "length": 40,
            "waveforms": {
                "I": "5008191769018423137_i",
                "Q": "5008191769018423137_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8363238826448225505": {
            "length": 20,
            "waveforms": {
                "single": "-8363238826448225505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3281072096949613271_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-9053090361207037944_i",
                "Q": "-9053090361207037944_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "7911743868580768313_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-6071536574897586567_i",
                "Q": "-6071536574897586567_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "4103708708466347947": {
            "length": 20,
            "waveforms": {
                "single": "4103708708466347947",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1134637526927045191": {
            "length": 16,
            "waveforms": {
                "single": "-1134637526927045191",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3485213915256038185": {
            "length": 16,
            "waveforms": {
                "single": "3485213915256038185",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8496929673084087283": {
            "length": 16,
            "waveforms": {
                "single": "8496929673084087283",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8718423732282802531": {
            "length": 16,
            "waveforms": {
                "single": "8718423732282802531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6909234885536888678": {
            "length": 16,
            "waveforms": {
                "single": "-6909234885536888678",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7530560653423582222": {
            "length": 16,
            "waveforms": {
                "single": "-7530560653423582222",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8563817751523675174": {
            "length": 16,
            "waveforms": {
                "single": "8563817751523675174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2297350836396817876": {
            "length": 16,
            "waveforms": {
                "single": "-2297350836396817876",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3779089091398245537": {
            "length": 16,
            "waveforms": {
                "single": "-3779089091398245537",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "743228678691757779": {
            "length": 16,
            "waveforms": {
                "single": "743228678691757779",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "121902910805064235": {
            "length": 16,
            "waveforms": {
                "single": "121902910805064235",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8071948195006661363": {
            "length": 16,
            "waveforms": {
                "single": "-8071948195006661363",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3162482425893639890": {
            "length": 16,
            "waveforms": {
                "single": "3162482425893639890",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-32703069954063122": {
            "length": 16,
            "waveforms": {
                "single": "-32703069954063122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5652694447804779252": {
            "length": 16,
            "waveforms": {
                "single": "-5652694447804779252",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1845522541562155601": {
            "length": 16,
            "waveforms": {
                "single": "-1845522541562155601",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7853292142785980517": {
            "length": 16,
            "waveforms": {
                "single": "-7853292142785980517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "352237146441011262": {
            "length": 20,
            "waveforms": {
                "single": "352237146441011262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1778275057225151957": {
            "length": 20,
            "waveforms": {
                "single": "1778275057225151957",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5585446963467775608": {
            "length": 20,
            "waveforms": {
                "single": "5585446963467775608",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-673914686829155272_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-673914686829155272_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "5008191769018423137_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "5008191769018423137_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-8363238826448225505": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-9053090361207037944_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-9053090361207037944_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6071536574897586567_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-6071536574897586567_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "4103708708466347947": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-1134637526927045191": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "3485213915256038185": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
        },
        "8496929673084087283": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "8718423732282802531": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-6909234885536888678": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-7530560653423582222": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "8563817751523675174": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-2297350836396817876": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-3779089091398245537": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "743228678691757779": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "121902910805064235": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-8071948195006661363": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "3162482425893639890": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-32703069954063122": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5652694447804779252": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1845522541562155601": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-7853292142785980517": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "352237146441011262": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1778275057225151957": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5585446963467775608": {
            "samples": [0.12311557788944723] * 19 + [0.0],
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
            "operations": {
                "-8363238826448225505": "-8363238826448225505",
                "4103708708466347947": "4103708708466347947",
                "-1134637526927045191": "-1134637526927045191",
                "3485213915256038185": "3485213915256038185",
                "8496929673084087283": "8496929673084087283",
                "8718423732282802531": "8718423732282802531",
                "-6909234885536888678": "-6909234885536888678",
                "-7530560653423582222": "-7530560653423582222",
                "8563817751523675174": "8563817751523675174",
                "-2297350836396817876": "-2297350836396817876",
                "-3779089091398245537": "-3779089091398245537",
                "743228678691757779": "743228678691757779",
                "121902910805064235": "121902910805064235",
                "-8071948195006661363": "-8071948195006661363",
                "3162482425893639890": "3162482425893639890",
                "-32703069954063122": "-32703069954063122",
                "-5652694447804779252": "-5652694447804779252",
                "-1845522541562155601": "-1845522541562155601",
                "-7853292142785980517": "-7853292142785980517",
                "352237146441011262": "352237146441011262",
                "1778275057225151957": "1778275057225151957",
                "5585446963467775608": "5585446963467775608",
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
                "7911743868580768313": "7911743868580768313_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_825",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "5008191769018423137": "5008191769018423137",
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
                "mixer": "B4/drive_mixer_c94",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "-673914686829155272": "-673914686829155272",
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
                "mixer": "B2/drive_mixer_fad",
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
                "-3281072096949613271": "-3281072096949613271_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_70f",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "-673914686829155272": {
            "length": 40,
            "waveforms": {
                "I": "-673914686829155272_i",
                "Q": "-673914686829155272_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5008191769018423137": {
            "length": 40,
            "waveforms": {
                "I": "5008191769018423137_i",
                "Q": "5008191769018423137_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8363238826448225505": {
            "length": 20,
            "waveforms": {
                "single": "-8363238826448225505",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3281072096949613271_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-9053090361207037944_i",
                "Q": "-9053090361207037944_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7911743868580768313_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-6071536574897586567_i",
                "Q": "-6071536574897586567_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "4103708708466347947": {
            "length": 20,
            "waveforms": {
                "single": "4103708708466347947",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1134637526927045191": {
            "length": 16,
            "waveforms": {
                "single": "-1134637526927045191",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3485213915256038185": {
            "length": 16,
            "waveforms": {
                "single": "3485213915256038185",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8496929673084087283": {
            "length": 16,
            "waveforms": {
                "single": "8496929673084087283",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8718423732282802531": {
            "length": 16,
            "waveforms": {
                "single": "8718423732282802531",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6909234885536888678": {
            "length": 16,
            "waveforms": {
                "single": "-6909234885536888678",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7530560653423582222": {
            "length": 16,
            "waveforms": {
                "single": "-7530560653423582222",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8563817751523675174": {
            "length": 16,
            "waveforms": {
                "single": "8563817751523675174",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2297350836396817876": {
            "length": 16,
            "waveforms": {
                "single": "-2297350836396817876",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3779089091398245537": {
            "length": 16,
            "waveforms": {
                "single": "-3779089091398245537",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "743228678691757779": {
            "length": 16,
            "waveforms": {
                "single": "743228678691757779",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "121902910805064235": {
            "length": 16,
            "waveforms": {
                "single": "121902910805064235",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8071948195006661363": {
            "length": 16,
            "waveforms": {
                "single": "-8071948195006661363",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3162482425893639890": {
            "length": 16,
            "waveforms": {
                "single": "3162482425893639890",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-32703069954063122": {
            "length": 16,
            "waveforms": {
                "single": "-32703069954063122",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5652694447804779252": {
            "length": 16,
            "waveforms": {
                "single": "-5652694447804779252",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1845522541562155601": {
            "length": 16,
            "waveforms": {
                "single": "-1845522541562155601",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7853292142785980517": {
            "length": 16,
            "waveforms": {
                "single": "-7853292142785980517",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "352237146441011262": {
            "length": 20,
            "waveforms": {
                "single": "352237146441011262",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1778275057225151957": {
            "length": 20,
            "waveforms": {
                "single": "1778275057225151957",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5585446963467775608": {
            "length": 20,
            "waveforms": {
                "single": "5585446963467775608",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-673914686829155272_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-673914686829155272_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5008191769018423137_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5008191769018423137_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8363238826448225505": {
            "type": "constant",
            "sample": -0.2388,
        },
        "-9053090361207037944_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-9053090361207037944_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-6071536574897586567_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-6071536574897586567_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "4103708708466347947": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-1134637526927045191": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3485213915256038185": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8496929673084087283": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8718423732282802531": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6909234885536888678": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7530560653423582222": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8563817751523675174": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2297350836396817876": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3779089091398245537": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "743228678691757779": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "121902910805064235": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8071948195006661363": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3162482425893639890": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-32703069954063122": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5652694447804779252": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1845522541562155601": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7853292142785980517": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "352237146441011262": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1778275057225151957": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5585446963467775608": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 19 + [0.0],
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
        "B4/acquisition_mixer_825": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_c94": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_fad": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_70f": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

