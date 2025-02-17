
# Single QUA script generated at 2025-02-17 11:01:31.003734
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
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-5385823863904654200", "B1/drive")
        wait(11, "B1/flux")
        play("-8449598601566423739", "B1/flux")
        wait(46, "B1/drive")
        play("-4624733234681092331", "B1/drive")
        wait(66, "B1/acquisition")
        measure("5504251465012861040", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9993410690631209)-(v3*0.0362963866490671))>0.0009409261700918508)))
        r1 = declare_stream()
        save(v4, r1)
        play("-4876539538582613931", "B2/drive")
        wait(11, "B2/flux")
        play("-8449598601566423739", "B2/flux")
        wait(46, "B2/drive")
        play("-6763120815009540759", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-8447607386491423525", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7633206605922164)-(v6*0.6460197900320566))>0.002433478909969987)))
        r2 = declare_stream()
        save(v7, r2)
        play("-6631089008910610350", "B3/drive")
        wait(11, "B3/flux")
        play("-8449598601566423739", "B3/flux")
        wait(46, "B3/drive")
        play("-5869998379687048481", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-2107949202366456799", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8670288721857065)-(v9*-0.4982578998835662))>0.002654329922186903)))
        r3 = declare_stream()
        save(v10, r3)
        play("2302113620075516505", "B4/drive")
        wait(11, "B4/flux")
        play("-8449598601566423739", "B4/flux")
        wait(46, "B4/drive")
        play("3063204249299078374", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-1049427617566193436", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5216599067641747)-(v12*0.8531535276108237))>-0.0004544464624298409)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25001, "B4/acquisition")
        wait(25001, "B3/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B1/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B1/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        wait(25536, "B4/flux")
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        play("-5385823863904654200", "B1/drive")
        wait(11, "B1/flux")
        play("-6473332972761972124", "B1/flux")
        wait(46, "B1/drive")
        play("-4624733234681092331", "B1/drive")
        wait(66, "B1/acquisition")
        measure("5504251465012861040", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9993410690631209)-(v3*0.0362963866490671))>0.0009409261700918508)))
        save(v4, r1)
        play("-4876539538582613931", "B2/drive")
        wait(11, "B2/flux")
        play("-6473332972761972124", "B2/flux")
        wait(46, "B2/drive")
        play("-6763120815009540759", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-8447607386491423525", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7633206605922164)-(v6*0.6460197900320566))>0.002433478909969987)))
        save(v7, r2)
        play("-6631089008910610350", "B3/drive")
        wait(11, "B3/flux")
        play("-6473332972761972124", "B3/flux")
        wait(46, "B3/drive")
        play("-5869998379687048481", "B3/drive")
        wait(66, "B3/acquisition")
        measure("-2107949202366456799", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8670288721857065)-(v9*-0.4982578998835662))>0.002654329922186903)))
        save(v10, r3)
        play("2302113620075516505", "B4/drive")
        wait(11, "B4/flux")
        play("-6473332972761972124", "B4/flux")
        wait(46, "B4/drive")
        play("3063204249299078374", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-1049427617566193436", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.5216599067641747)-(v12*0.8531535276108237))>-0.0004544464624298409)))
        save(v13, r4)
        wait(25001, "B4/acquisition")
        wait(25001, "B3/acquisition")
        wait(25501, "B4/drive")
        wait(25536, "B1/flux")
        wait(25001, "B1/acquisition")
        wait(25501, "B1/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        wait(25536, "B4/flux")
        wait(25501, "B2/drive")
        wait(25536, "B2/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("5504251465012861040_B1|acquisition_shots")
        r2.buffer(2).average().save("-8447607386491423525_B2|acquisition_shots")
        r3.buffer(2).average().save("-2107949202366456799_B3|acquisition_shots")
        r4.buffer(2).average().save("-1049427617566193436_B4|acquisition_shots")


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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
            },
            "digital_outputs": {
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
            "operations": {
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
            },
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
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
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
            "operations": {
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
            },
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
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
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
                "-1049427617566193436": "-1049427617566193436_B4/acquisition",
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
                "-2107949202366456799": "-2107949202366456799_B3/acquisition",
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
                "2302113620075516505": "2302113620075516505",
                "3063204249299078374": "3063204249299078374",
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
            "intermediate_frequency": -237451236.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "5504251465012861040": "5504251465012861040_B1/acquisition",
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
                "-5385823863904654200": "-5385823863904654200",
                "-4624733234681092331": "-4624733234681092331",
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
                "-8447607386491423525": "-8447607386491423525_B2/acquisition",
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
                "-6631089008910610350": "-6631089008910610350",
                "-5869998379687048481": "-5869998379687048481",
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
                "-4876539538582613931": "-4876539538582613931",
                "-6763120815009540759": "-6763120815009540759",
            },
        },
    },
    "pulses": {
        "-5385823863904654200": {
            "length": 40,
            "waveforms": {
                "I": "-5385823863904654200_i",
                "Q": "-5385823863904654200_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5746963705409337186": {
            "length": 16,
            "waveforms": {
                "single": "5746963705409337186",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5504251465012861040_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7681098730583114721_i",
                "Q": "-7681098730583114721_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-4876539538582613931": {
            "length": 40,
            "waveforms": {
                "I": "-4876539538582613931_i",
                "Q": "-4876539538582613931_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8447607386491423525_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "506876350299494796_i",
                "Q": "506876350299494796_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-6631089008910610350": {
            "length": 40,
            "waveforms": {
                "I": "-6631089008910610350_i",
                "Q": "-6631089008910610350_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2107949202366456799_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "2286092240307298542_i",
                "Q": "2286092240307298542_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "2302113620075516505": {
            "length": 40,
            "waveforms": {
                "I": "2302113620075516505_i",
                "Q": "2302113620075516505_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1049427617566193436_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7912284648465748618_i",
                "Q": "-7912284648465748618_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "-8892608462057590779": {
            "length": 16,
            "waveforms": {
                "single": "-8892608462057590779",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8798788366096904658": {
            "length": 16,
            "waveforms": {
                "single": "-8798788366096904658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6694848774054423916": {
            "length": 16,
            "waveforms": {
                "single": "-6694848774054423916",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5268810863270283221": {
            "length": 16,
            "waveforms": {
                "single": "-5268810863270283221",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5094992343869151473": {
            "length": 16,
            "waveforms": {
                "single": "5094992343869151473",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3158212485155423806": {
            "length": 16,
            "waveforms": {
                "single": "3158212485155423806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5423416844029410578": {
            "length": 16,
            "waveforms": {
                "single": "-5423416844029410578",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "957614790174222541": {
            "length": 16,
            "waveforms": {
                "single": "957614790174222541",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5479932560264225857": {
            "length": 16,
            "waveforms": {
                "single": "5479932560264225857",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "31287032196069016": {
            "length": 16,
            "waveforms": {
                "single": "31287032196069016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8624154474678244597": {
            "length": 16,
            "waveforms": {
                "single": "-8624154474678244597",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2229046720199235879": {
            "length": 16,
            "waveforms": {
                "single": "2229046720199235879",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5438308336322314490": {
            "length": 16,
            "waveforms": {
                "single": "-5438308336322314490",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-915990566232311174": {
            "length": 16,
            "waveforms": {
                "single": "-915990566232311174",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4648300467401117990": {
            "length": 16,
            "waveforms": {
                "single": "4648300467401117990",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2613986936594310263": {
            "length": 20,
            "waveforms": {
                "single": "2613986936594310263",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2835480995793025511": {
            "length": 20,
            "waveforms": {
                "single": "2835480995793025511",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4042916019191665964": {
            "length": 20,
            "waveforms": {
                "single": "-4042916019191665964",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6736472997996335283": {
            "length": 20,
            "waveforms": {
                "single": "6736472997996335283",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5254734742994907622": {
            "length": 24,
            "waveforms": {
                "single": "5254734742994907622",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8180293572886594896": {
            "length": 24,
            "waveforms": {
                "single": "-8180293572886594896",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3560442130703511520": {
            "length": 24,
            "waveforms": {
                "single": "-3560442130703511520",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3436481743597876332": {
            "length": 24,
            "waveforms": {
                "single": "-3436481743597876332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5761039825684712785": {
            "length": 28,
            "waveforms": {
                "single": "-5761039825684712785",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2444489463542278994": {
            "length": 28,
            "waveforms": {
                "single": "2444489463542278994",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3870527374326419689": {
            "length": 28,
            "waveforms": {
                "single": "3870527374326419689",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2880195677420242659": {
            "length": 28,
            "waveforms": {
                "single": "-2880195677420242659",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4489607895659699447": {
            "length": 32,
            "waveforms": {
                "single": "-4489607895659699447",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-682435989417075796": {
            "length": 32,
            "waveforms": {
                "single": "-682435989417075796",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6302427367267791926": {
            "length": 32,
            "waveforms": {
                "single": "-6302427367267791926",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3827473275848622849": {
            "length": 32,
            "waveforms": {
                "single": "-3827473275848622849",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1736817757784806315": {
            "length": 36,
            "waveforms": {
                "single": "1736817757784806315",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3883173620065909815": {
            "length": 36,
            "waveforms": {
                "single": "-3883173620065909815",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7078359115913612827": {
            "length": 36,
            "waveforms": {
                "single": "-7078359115913612827",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6954398728807977639": {
            "length": 36,
            "waveforms": {
                "single": "-6954398728807977639",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9167787262814737524": {
            "length": 40,
            "waveforms": {
                "single": "9167787262814737524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3547795884964021394": {
            "length": 40,
            "waveforms": {
                "single": "3547795884964021394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6693418899518538443": {
            "length": 40,
            "waveforms": {
                "single": "-6693418899518538443",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6471924840319823195": {
            "length": 40,
            "waveforms": {
                "single": "-6471924840319823195",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7190784280299596799": {
            "length": 44,
            "waveforms": {
                "single": "-7190784280299596799",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4274165152316656332": {
            "length": 44,
            "waveforms": {
                "single": "-4274165152316656332",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8626399721231658383": {
            "length": 44,
            "waveforms": {
                "single": "8626399721231658383",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "959044664710108014": {
            "length": 44,
            "waveforms": {
                "single": "959044664710108014",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1180538723908823262": {
            "length": 48,
            "waveforms": {
                "single": "1180538723908823262",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7401090605276011122": {
            "length": 48,
            "waveforms": {
                "single": "-7401090605276011122",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3378298411911990125": {
            "length": 48,
            "waveforms": {
                "single": "3378298411911990125",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2167880788249246776": {
            "length": 48,
            "waveforms": {
                "single": "-2167880788249246776",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8611508228938754471": {
            "length": 52,
            "waveforms": {
                "single": "8611508228938754471",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7016150388880936738": {
            "length": 52,
            "waveforms": {
                "single": "-7016150388880936738",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "251372958952635335": {
            "length": 52,
            "waveforms": {
                "single": "251372958952635335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8456902248179627114": {
            "length": 52,
            "waveforms": {
                "single": "8456902248179627114",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2836910870328910984": {
            "length": 56,
            "waveforms": {
                "single": "2836910870328910984",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "512352788242074531": {
            "length": 56,
            "waveforms": {
                "single": "512352788242074531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5034670558332077847": {
            "length": 56,
            "waveforms": {
                "single": "5034670558332077847",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5256164617530793095": {
            "length": 56,
            "waveforms": {
                "single": "5256164617530793095",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8178863698350709423": {
            "length": 60,
            "waveforms": {
                "single": "-8178863698350709423",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3055566922549591830": {
            "length": 60,
            "waveforms": {
                "single": "3055566922549591830",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-139618573298111182": {
            "length": 60,
            "waveforms": {
                "single": "-139618573298111182",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5759609951148827312": {
            "length": 60,
            "waveforms": {
                "single": "-5759609951148827312",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1952438044906203661": {
            "length": 64,
            "waveforms": {
                "single": "-1952438044906203661",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3561850263145660449": {
            "length": 64,
            "waveforms": {
                "single": "-3561850263145660449",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8134170758817228819": {
            "length": 64,
            "waveforms": {
                "single": "8134170758817228819",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1671359553881103897": {
            "length": 64,
            "waveforms": {
                "single": "1671359553881103897",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-681006114881190323": {
            "length": 68,
            "waveforms": {
                "single": "-681006114881190323",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8348361171402740692": {
            "length": 68,
            "waveforms": {
                "single": "-8348361171402740692",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1516753573121976540": {
            "length": 68,
            "waveforms": {
                "single": "1516753573121976540",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1738247632320691788": {
            "length": 68,
            "waveforms": {
                "single": "1738247632320691788",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-296065898486115939": {
            "length": 72,
            "waveforms": {
                "single": "-296065898486115939",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6971457449347456134": {
            "length": 72,
            "waveforms": {
                "single": "6971457449347456134",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6748993943986886683": {
            "length": 72,
            "waveforms": {
                "single": "-6748993943986886683",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2123187848715766172": {
            "length": 72,
            "waveforms": {
                "single": "2123187848715766172",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9056032877160213371": {
            "length": 76,
            "waveforms": {
                "single": "-9056032877160213371",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7356397665742530518": {
            "length": 76,
            "waveforms": {
                "single": "7356397665742530518",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8570824676763310143": {
            "length": 76,
            "waveforms": {
                "single": "8570824676763310143",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8892586719963854235": {
            "length": 76,
            "waveforms": {
                "single": "-8892586719963854235",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8671092660765138987": {
            "length": 80,
            "waveforms": {
                "single": "-8671092660765138987",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8449598601566423739": {
            "length": 80,
            "waveforms": {
                "single": "-8449598601566423739",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6473332972761972124": {
            "length": 80,
            "waveforms": {
                "single": "-6473332972761972124",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4624733234681092331": {
            "length": 40,
            "waveforms": {
                "I": "-4624733234681092331_i",
                "Q": "-4624733234681092331_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6763120815009540759": {
            "length": 40,
            "waveforms": {
                "I": "-6763120815009540759_i",
                "Q": "-6763120815009540759_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5869998379687048481": {
            "length": 40,
            "waveforms": {
                "I": "-5869998379687048481_i",
                "Q": "-5869998379687048481_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3063204249299078374": {
            "length": 40,
            "waveforms": {
                "I": "3063204249299078374_i",
                "Q": "3063204249299078374_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-5385823863904654200_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "-5385823863904654200_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "5746963705409337186": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-7681098730583114721_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-7681098730583114721_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4876539538582613931_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "-4876539538582613931_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "506876350299494796_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "506876350299494796_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-6631089008910610350_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-6631089008910610350_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "2286092240307298542_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "2286092240307298542_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2302113620075516505_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "2302113620075516505_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-7912284648465748618_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-7912284648465748618_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-8892608462057590779": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-8798788366096904658": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-6694848774054423916": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-5268810863270283221": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "5094992343869151473": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3158212485155423806": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-5423416844029410578": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "957614790174222541": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "5479932560264225857": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "31287032196069016": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-8624154474678244597": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "2229046720199235879": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5438308336322314490": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-915990566232311174": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "4648300467401117990": {
            "sample": 0.25,
            "type": "constant",
        },
        "2613986936594310263": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2835480995793025511": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4042916019191665964": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "6736472997996335283": {
            "sample": 0.25,
            "type": "constant",
        },
        "5254734742994907622": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8180293572886594896": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3560442130703511520": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-3436481743597876332": {
            "sample": 0.25,
            "type": "constant",
        },
        "-5761039825684712785": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2444489463542278994": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3870527374326419689": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-2880195677420242659": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4489607895659699447": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-682435989417075796": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6302427367267791926": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-3827473275848622849": {
            "sample": 0.25,
            "type": "constant",
        },
        "1736817757784806315": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3883173620065909815": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7078359115913612827": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-6954398728807977639": {
            "sample": 0.25,
            "type": "constant",
        },
        "9167787262814737524": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3547795884964021394": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6693418899518538443": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-6471924840319823195": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7190784280299596799": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4274165152316656332": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8626399721231658383": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "959044664710108014": {
            "sample": 0.25,
            "type": "constant",
        },
        "1180538723908823262": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7401090605276011122": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3378298411911990125": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-2167880788249246776": {
            "sample": 0.25,
            "type": "constant",
        },
        "8611508228938754471": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7016150388880936738": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "251372958952635335": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "8456902248179627114": {
            "sample": 0.25,
            "type": "constant",
        },
        "2836910870328910984": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "512352788242074531": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5034670558332077847": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "5256164617530793095": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8178863698350709423": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3055566922549591830": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-139618573298111182": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-5759609951148827312": {
            "sample": 0.25,
            "type": "constant",
        },
        "-1952438044906203661": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3561850263145660449": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8134170758817228819": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "1671359553881103897": {
            "sample": 0.25,
            "type": "constant",
        },
        "-681006114881190323": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8348361171402740692": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1516753573121976540": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "1738247632320691788": {
            "sample": 0.25,
            "type": "constant",
        },
        "-296065898486115939": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6971457449347456134": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6748993943986886683": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "2123187848715766172": {
            "sample": 0.25,
            "type": "constant",
        },
        "-9056032877160213371": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7356397665742530518": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8570824676763310143": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-8892586719963854235": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8671092660765138987": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8449598601566423739": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6473332972761972124": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-4624733234681092331_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-4624733234681092331_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "-6763120815009540759_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "-6763120815009540759_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-5869998379687048481_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-5869998379687048481_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "3063204249299078374_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "3063204249299078374_q": {
            "samples": [-0.0003245581697577896, -0.0004143437926495826, -0.0005192451877881842, -0.0006385249144990759, -0.0007701923879260787, -0.0009108005732581567, -0.0010553365498202029, -0.0011972457129536525, -0.0013286216753579413, -0.0014405792538840587, -0.0015238070380387684, -0.0015692710288161837, -0.001569015034187334, -0.0015169810553923994, -0.0014097580972250387, -0.0012471643221046982, -0.001032577396853722, -0.0007729513005631845, -0.0004784924452043538, -0.00016200920159745424, 0.00016200920159745424, 0.0004784924452043538, 0.0007729513005631845, 0.001032577396853722, 0.0012471643221046982, 0.0014097580972250387, 0.0015169810553923994, 0.001569015034187334, 0.0015692710288161837, 0.0015238070380387684, 0.0014405792538840587, 0.0013286216753579413, 0.0011972457129536525, 0.0010553365498202029, 0.0009108005732581567, 0.0007701923879260787, 0.0006385249144990759, 0.0005192451877881842, 0.0004143437926495826, 0.0003245581697577896],
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
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
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
            "operations": {
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
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
            "operations": {
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
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
            "operations": {
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
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
                "-8449598601566423739": "-8449598601566423739",
                "-6473332972761972124": "-6473332972761972124",
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
                "-1049427617566193436": "-1049427617566193436_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_8b9",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "-2107949202366456799": "-2107949202366456799_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_bfb",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "2302113620075516505": "2302113620075516505",
                "3063204249299078374": "3063204249299078374",
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
                "mixer": "B4/drive_mixer_3e2",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "5504251465012861040": "5504251465012861040_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_3e5",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "-5385823863904654200": "-5385823863904654200",
                "-4624733234681092331": "-4624733234681092331",
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
                "mixer": "B1/drive_mixer_089",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "-8447607386491423525": "-8447607386491423525_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_a69",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-6631089008910610350": "-6631089008910610350",
                "-5869998379687048481": "-5869998379687048481",
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
                "mixer": "B3/drive_mixer_eb5",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-4876539538582613931": "-4876539538582613931",
                "-6763120815009540759": "-6763120815009540759",
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
                "mixer": "B2/drive_mixer_dcb",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
        },
    },
    "pulses": {
        "-5385823863904654200": {
            "length": 40,
            "waveforms": {
                "I": "-5385823863904654200_i",
                "Q": "-5385823863904654200_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5746963705409337186": {
            "length": 16,
            "waveforms": {
                "single": "5746963705409337186",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5504251465012861040_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7681098730583114721_i",
                "Q": "-7681098730583114721_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-4876539538582613931": {
            "length": 40,
            "waveforms": {
                "I": "-4876539538582613931_i",
                "Q": "-4876539538582613931_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8447607386491423525_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "506876350299494796_i",
                "Q": "506876350299494796_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-6631089008910610350": {
            "length": 40,
            "waveforms": {
                "I": "-6631089008910610350_i",
                "Q": "-6631089008910610350_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2107949202366456799_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "2286092240307298542_i",
                "Q": "2286092240307298542_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "2302113620075516505": {
            "length": 40,
            "waveforms": {
                "I": "2302113620075516505_i",
                "Q": "2302113620075516505_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1049427617566193436_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7912284648465748618_i",
                "Q": "-7912284648465748618_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-8892608462057590779": {
            "length": 16,
            "waveforms": {
                "single": "-8892608462057590779",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8798788366096904658": {
            "length": 16,
            "waveforms": {
                "single": "-8798788366096904658",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6694848774054423916": {
            "length": 16,
            "waveforms": {
                "single": "-6694848774054423916",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5268810863270283221": {
            "length": 16,
            "waveforms": {
                "single": "-5268810863270283221",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5094992343869151473": {
            "length": 16,
            "waveforms": {
                "single": "5094992343869151473",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3158212485155423806": {
            "length": 16,
            "waveforms": {
                "single": "3158212485155423806",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5423416844029410578": {
            "length": 16,
            "waveforms": {
                "single": "-5423416844029410578",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "957614790174222541": {
            "length": 16,
            "waveforms": {
                "single": "957614790174222541",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5479932560264225857": {
            "length": 16,
            "waveforms": {
                "single": "5479932560264225857",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "31287032196069016": {
            "length": 16,
            "waveforms": {
                "single": "31287032196069016",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8624154474678244597": {
            "length": 16,
            "waveforms": {
                "single": "-8624154474678244597",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2229046720199235879": {
            "length": 16,
            "waveforms": {
                "single": "2229046720199235879",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5438308336322314490": {
            "length": 16,
            "waveforms": {
                "single": "-5438308336322314490",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-915990566232311174": {
            "length": 16,
            "waveforms": {
                "single": "-915990566232311174",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4648300467401117990": {
            "length": 16,
            "waveforms": {
                "single": "4648300467401117990",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2613986936594310263": {
            "length": 20,
            "waveforms": {
                "single": "2613986936594310263",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2835480995793025511": {
            "length": 20,
            "waveforms": {
                "single": "2835480995793025511",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4042916019191665964": {
            "length": 20,
            "waveforms": {
                "single": "-4042916019191665964",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6736472997996335283": {
            "length": 20,
            "waveforms": {
                "single": "6736472997996335283",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5254734742994907622": {
            "length": 24,
            "waveforms": {
                "single": "5254734742994907622",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8180293572886594896": {
            "length": 24,
            "waveforms": {
                "single": "-8180293572886594896",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3560442130703511520": {
            "length": 24,
            "waveforms": {
                "single": "-3560442130703511520",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3436481743597876332": {
            "length": 24,
            "waveforms": {
                "single": "-3436481743597876332",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5761039825684712785": {
            "length": 28,
            "waveforms": {
                "single": "-5761039825684712785",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2444489463542278994": {
            "length": 28,
            "waveforms": {
                "single": "2444489463542278994",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3870527374326419689": {
            "length": 28,
            "waveforms": {
                "single": "3870527374326419689",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2880195677420242659": {
            "length": 28,
            "waveforms": {
                "single": "-2880195677420242659",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4489607895659699447": {
            "length": 32,
            "waveforms": {
                "single": "-4489607895659699447",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-682435989417075796": {
            "length": 32,
            "waveforms": {
                "single": "-682435989417075796",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6302427367267791926": {
            "length": 32,
            "waveforms": {
                "single": "-6302427367267791926",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3827473275848622849": {
            "length": 32,
            "waveforms": {
                "single": "-3827473275848622849",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1736817757784806315": {
            "length": 36,
            "waveforms": {
                "single": "1736817757784806315",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3883173620065909815": {
            "length": 36,
            "waveforms": {
                "single": "-3883173620065909815",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7078359115913612827": {
            "length": 36,
            "waveforms": {
                "single": "-7078359115913612827",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6954398728807977639": {
            "length": 36,
            "waveforms": {
                "single": "-6954398728807977639",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9167787262814737524": {
            "length": 40,
            "waveforms": {
                "single": "9167787262814737524",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3547795884964021394": {
            "length": 40,
            "waveforms": {
                "single": "3547795884964021394",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6693418899518538443": {
            "length": 40,
            "waveforms": {
                "single": "-6693418899518538443",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6471924840319823195": {
            "length": 40,
            "waveforms": {
                "single": "-6471924840319823195",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7190784280299596799": {
            "length": 44,
            "waveforms": {
                "single": "-7190784280299596799",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4274165152316656332": {
            "length": 44,
            "waveforms": {
                "single": "-4274165152316656332",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8626399721231658383": {
            "length": 44,
            "waveforms": {
                "single": "8626399721231658383",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "959044664710108014": {
            "length": 44,
            "waveforms": {
                "single": "959044664710108014",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1180538723908823262": {
            "length": 48,
            "waveforms": {
                "single": "1180538723908823262",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7401090605276011122": {
            "length": 48,
            "waveforms": {
                "single": "-7401090605276011122",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3378298411911990125": {
            "length": 48,
            "waveforms": {
                "single": "3378298411911990125",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2167880788249246776": {
            "length": 48,
            "waveforms": {
                "single": "-2167880788249246776",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8611508228938754471": {
            "length": 52,
            "waveforms": {
                "single": "8611508228938754471",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7016150388880936738": {
            "length": 52,
            "waveforms": {
                "single": "-7016150388880936738",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "251372958952635335": {
            "length": 52,
            "waveforms": {
                "single": "251372958952635335",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8456902248179627114": {
            "length": 52,
            "waveforms": {
                "single": "8456902248179627114",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2836910870328910984": {
            "length": 56,
            "waveforms": {
                "single": "2836910870328910984",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "512352788242074531": {
            "length": 56,
            "waveforms": {
                "single": "512352788242074531",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5034670558332077847": {
            "length": 56,
            "waveforms": {
                "single": "5034670558332077847",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5256164617530793095": {
            "length": 56,
            "waveforms": {
                "single": "5256164617530793095",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8178863698350709423": {
            "length": 60,
            "waveforms": {
                "single": "-8178863698350709423",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3055566922549591830": {
            "length": 60,
            "waveforms": {
                "single": "3055566922549591830",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-139618573298111182": {
            "length": 60,
            "waveforms": {
                "single": "-139618573298111182",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5759609951148827312": {
            "length": 60,
            "waveforms": {
                "single": "-5759609951148827312",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1952438044906203661": {
            "length": 64,
            "waveforms": {
                "single": "-1952438044906203661",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3561850263145660449": {
            "length": 64,
            "waveforms": {
                "single": "-3561850263145660449",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8134170758817228819": {
            "length": 64,
            "waveforms": {
                "single": "8134170758817228819",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1671359553881103897": {
            "length": 64,
            "waveforms": {
                "single": "1671359553881103897",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-681006114881190323": {
            "length": 68,
            "waveforms": {
                "single": "-681006114881190323",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8348361171402740692": {
            "length": 68,
            "waveforms": {
                "single": "-8348361171402740692",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1516753573121976540": {
            "length": 68,
            "waveforms": {
                "single": "1516753573121976540",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1738247632320691788": {
            "length": 68,
            "waveforms": {
                "single": "1738247632320691788",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-296065898486115939": {
            "length": 72,
            "waveforms": {
                "single": "-296065898486115939",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6971457449347456134": {
            "length": 72,
            "waveforms": {
                "single": "6971457449347456134",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6748993943986886683": {
            "length": 72,
            "waveforms": {
                "single": "-6748993943986886683",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2123187848715766172": {
            "length": 72,
            "waveforms": {
                "single": "2123187848715766172",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9056032877160213371": {
            "length": 76,
            "waveforms": {
                "single": "-9056032877160213371",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7356397665742530518": {
            "length": 76,
            "waveforms": {
                "single": "7356397665742530518",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8570824676763310143": {
            "length": 76,
            "waveforms": {
                "single": "8570824676763310143",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8892586719963854235": {
            "length": 76,
            "waveforms": {
                "single": "-8892586719963854235",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8671092660765138987": {
            "length": 80,
            "waveforms": {
                "single": "-8671092660765138987",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8449598601566423739": {
            "length": 80,
            "waveforms": {
                "single": "-8449598601566423739",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6473332972761972124": {
            "length": 80,
            "waveforms": {
                "single": "-6473332972761972124",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4624733234681092331": {
            "length": 40,
            "waveforms": {
                "I": "-4624733234681092331_i",
                "Q": "-4624733234681092331_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6763120815009540759": {
            "length": 40,
            "waveforms": {
                "I": "-6763120815009540759_i",
                "Q": "-6763120815009540759_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5869998379687048481": {
            "length": 40,
            "waveforms": {
                "I": "-5869998379687048481_i",
                "Q": "-5869998379687048481_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3063204249299078374": {
            "length": 40,
            "waveforms": {
                "I": "3063204249299078374_i",
                "Q": "3063204249299078374_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-5385823863904654200_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5385823863904654200_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5746963705409337186": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7681098730583114721_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-7681098730583114721_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4876539538582613931_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4876539538582613931_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "506876350299494796_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "506876350299494796_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-6631089008910610350_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6631089008910610350_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2286092240307298542_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "2286092240307298542_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2302113620075516505_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2302113620075516505_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7912284648465748618_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-7912284648465748618_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-8892608462057590779": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8798788366096904658": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6694848774054423916": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5268810863270283221": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5094992343869151473": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3158212485155423806": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5423416844029410578": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "957614790174222541": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5479932560264225857": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "31287032196069016": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8624154474678244597": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2229046720199235879": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5438308336322314490": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-915990566232311174": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4648300467401117990": {
            "type": "constant",
            "sample": 0.25,
        },
        "2613986936594310263": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2835480995793025511": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4042916019191665964": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6736472997996335283": {
            "type": "constant",
            "sample": 0.25,
        },
        "5254734742994907622": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8180293572886594896": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3560442130703511520": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3436481743597876332": {
            "type": "constant",
            "sample": 0.25,
        },
        "-5761039825684712785": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2444489463542278994": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3870527374326419689": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2880195677420242659": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4489607895659699447": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-682435989417075796": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6302427367267791926": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3827473275848622849": {
            "type": "constant",
            "sample": 0.25,
        },
        "1736817757784806315": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3883173620065909815": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7078359115913612827": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6954398728807977639": {
            "type": "constant",
            "sample": 0.25,
        },
        "9167787262814737524": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3547795884964021394": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6693418899518538443": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6471924840319823195": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7190784280299596799": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4274165152316656332": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8626399721231658383": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "959044664710108014": {
            "type": "constant",
            "sample": 0.25,
        },
        "1180538723908823262": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7401090605276011122": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3378298411911990125": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2167880788249246776": {
            "type": "constant",
            "sample": 0.25,
        },
        "8611508228938754471": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7016150388880936738": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "251372958952635335": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8456902248179627114": {
            "type": "constant",
            "sample": 0.25,
        },
        "2836910870328910984": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "512352788242074531": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5034670558332077847": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5256164617530793095": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8178863698350709423": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3055566922549591830": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-139618573298111182": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5759609951148827312": {
            "type": "constant",
            "sample": 0.25,
        },
        "-1952438044906203661": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3561850263145660449": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8134170758817228819": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1671359553881103897": {
            "type": "constant",
            "sample": 0.25,
        },
        "-681006114881190323": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8348361171402740692": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1516753573121976540": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1738247632320691788": {
            "type": "constant",
            "sample": 0.25,
        },
        "-296065898486115939": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6971457449347456134": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6748993943986886683": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2123187848715766172": {
            "type": "constant",
            "sample": 0.25,
        },
        "-9056032877160213371": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7356397665742530518": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8570824676763310143": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8892586719963854235": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8671092660765138987": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8449598601566423739": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6473332972761972124": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4624733234681092331_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4624733234681092331_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6763120815009540759_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6763120815009540759_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5869998379687048481_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5869998379687048481_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3063204249299078374_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3063204249299078374_q": {
            "type": "arbitrary",
            "samples": [-0.0003245581697577896, -0.0004143437926495826, -0.0005192451877881842, -0.0006385249144990759, -0.0007701923879260787, -0.0009108005732581567, -0.0010553365498202029, -0.0011972457129536525, -0.0013286216753579413, -0.0014405792538840587, -0.0015238070380387684, -0.0015692710288161837, -0.001569015034187334, -0.0015169810553923994, -0.0014097580972250387, -0.0012471643221046982, -0.001032577396853722, -0.0007729513005631845, -0.0004784924452043538, -0.00016200920159745424, 0.00016200920159745424, 0.0004784924452043538, 0.0007729513005631845, 0.001032577396853722, 0.0012471643221046982, 0.0014097580972250387, 0.0015169810553923994, 0.001569015034187334, 0.0015692710288161837, 0.0015238070380387684, 0.0014405792538840587, 0.0013286216753579413, 0.0011972457129536525, 0.0010553365498202029, 0.0009108005732581567, 0.0007701923879260787, 0.0006385249144990759, 0.0005192451877881842, 0.0004143437926495826, 0.0003245581697577896],
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
    },
    "mixers": {
        "B4/acquisition_mixer_8b9": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_bfb": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_3e2": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_3e5": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_089": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_a69": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_eb5": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_dcb": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

