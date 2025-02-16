
# Single QUA script generated at 2025-02-16 14:23:53.877503
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
        play("3898880453943063528", "B1/drive")
        wait(11, "B1/flux")
        play("-1842817198641536596", "B1/flux")
        wait(46, "B1/drive")
        play("4659971083166625397", "B1/drive")
        wait(66, "B1/acquisition")
        measure("6585270118705349135", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        r1 = declare_stream()
        save(v4, r1)
        play("3127692063079506005", "B2/drive")
        wait(11, "B2/flux")
        play("-1842817198641536596", "B2/flux")
        wait(46, "B2/drive")
        play("3888782692303067874", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-6676865194900398041", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        r2 = declare_stream()
        save(v7, r2)
        play("-2587561901132669542", "B3/drive")
        wait(11, "B3/flux")
        play("-1842817198641536596", "B3/flux")
        wait(46, "B3/drive")
        play("-1826471271909107673", "B3/drive")
        wait(66, "B3/acquisition")
        measure("2767705647931182791", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        r3 = declare_stream()
        save(v10, r3)
        play("-2032606375604854086", "B4/drive")
        wait(11, "B4/flux")
        play("-1842817198641536596", "B4/flux")
        wait(46, "B4/drive")
        play("-1271515746381292217", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-572130150252921974", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        r4 = declare_stream()
        save(v13, r4)
        wait(25536, "B1/flux")
        wait(25501, "B2/drive")
        wait(25536, "B4/flux")
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25001, "B3/acquisition")
        wait(25001, "B1/acquisition")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        play("3898880453943063528", "B1/drive")
        wait(11, "B1/flux")
        play("6362712090585455183", "B1/flux")
        wait(46, "B1/drive")
        play("4659971083166625397", "B1/drive")
        wait(66, "B1/acquisition")
        measure("6585270118705349135", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
        assign(v4, Cast.to_int((((v2*0.9967019904271117)-(v3*0.08114888957116839))>0.0009208204328015715)))
        save(v4, r1)
        play("3127692063079506005", "B2/drive")
        wait(11, "B2/flux")
        play("6362712090585455183", "B2/flux")
        wait(46, "B2/drive")
        play("3888782692303067874", "B2/drive")
        wait(66, "B2/acquisition")
        measure("-6676865194900398041", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
        assign(v7, Cast.to_int((((v5*0.7386661925213004)-(v6*0.6740714027653786))>0.0026726729978320107)))
        save(v7, r2)
        play("-2587561901132669542", "B3/drive")
        wait(11, "B3/flux")
        play("6362712090585455183", "B3/flux")
        wait(46, "B3/drive")
        play("-1826471271909107673", "B3/drive")
        wait(66, "B3/acquisition")
        measure("2767705647931182791", "B3/acquisition", None, dual_demod.full("cos", "sin", v8), dual_demod.full("minus_sin", "cos", v9))
        assign(v10, Cast.to_int((((v8*-0.8459998192018453)-(v9*-0.5331831823214654))>0.0026818753539089865)))
        save(v10, r3)
        play("-2032606375604854086", "B4/drive")
        wait(11, "B4/flux")
        play("6362712090585455183", "B4/flux")
        wait(46, "B4/drive")
        play("-1271515746381292217", "B4/drive")
        wait(66, "B4/acquisition")
        measure("-572130150252921974", "B4/acquisition", None, dual_demod.full("cos", "sin", v11), dual_demod.full("minus_sin", "cos", v12))
        assign(v13, Cast.to_int((((v11*0.4781750072295442)-(v12*0.8782645742946856))>-0.00048643881283392637)))
        save(v13, r4)
        wait(25536, "B1/flux")
        wait(25501, "B2/drive")
        wait(25536, "B4/flux")
        wait(25501, "B1/drive")
        wait(25501, "B4/drive")
        wait(25001, "B4/acquisition")
        wait(25001, "B3/acquisition")
        wait(25001, "B1/acquisition")
        wait(25536, "B3/flux")
        wait(25501, "B3/drive")
        wait(25001, "B2/acquisition")
        wait(25536, "B2/flux")
        wait(25000, )
    with stream_processing():
        r1.buffer(2).average().save("6585270118705349135_B1|acquisition_shots")
        r2.buffer(2).average().save("-6676865194900398041_B2|acquisition_shots")
        r3.buffer(2).average().save("2767705647931182791_B3|acquisition_shots")
        r4.buffer(2).average().save("-572130150252921974_B4|acquisition_shots")


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
                        "feedforward": [],
                        "feedback": [],
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
                "3": {},
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "3127692063079506005": "3127692063079506005",
                "3888782692303067874": "3888782692303067874",
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
                "3898880453943063528": "3898880453943063528",
                "4659971083166625397": "4659971083166625397",
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
                "-2032606375604854086": "-2032606375604854086",
                "-1271515746381292217": "-1271515746381292217",
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
                "-572130150252921974": "-572130150252921974_B4/acquisition",
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
                "2767705647931182791": "2767705647931182791_B3/acquisition",
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
                "6585270118705349135": "6585270118705349135_B1/acquisition",
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
                "-2587561901132669542": "-2587561901132669542",
                "-1826471271909107673": "-1826471271909107673",
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
                "-6676865194900398041": "-6676865194900398041_B2/acquisition",
            },
        },
    },
    "pulses": {
        "3898880453943063528": {
            "length": 40,
            "waveforms": {
                "I": "3898880453943063528_i",
                "Q": "3898880453943063528_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5594310502760609825": {
            "length": 16,
            "waveforms": {
                "single": "-5594310502760609825",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6585270118705349135_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5154946332764312586_i",
                "Q": "5154946332764312586_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "3127692063079506005": {
            "length": 40,
            "waveforms": {
                "I": "3127692063079506005_i",
                "Q": "3127692063079506005_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6676865194900398041_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8944564030662553975_i",
                "Q": "8944564030662553975_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-2587561901132669542": {
            "length": 40,
            "waveforms": {
                "I": "-2587561901132669542_i",
                "Q": "-2587561901132669542_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2767705647931182791_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8076108015019869024_i",
                "Q": "8076108015019869024_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-2032606375604854086": {
            "length": 40,
            "waveforms": {
                "I": "-2032606375604854086_i",
                "Q": "-2032606375604854086_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-572130150252921974_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2122268873753178136_i",
                "Q": "-2122268873753178136_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "3277871289942043030": {
            "length": 16,
            "waveforms": {
                "single": "3277871289942043030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2334024383050379740": {
            "length": 16,
            "waveforms": {
                "single": "2334024383050379740",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2457984770156014928": {
            "length": 16,
            "waveforms": {
                "single": "2457984770156014928",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5209370286365535441": {
            "length": 16,
            "waveforms": {
                "single": "-5209370286365535441",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3662811506337117414": {
            "length": 16,
            "waveforms": {
                "single": "3662811506337117414",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7838930358543831875": {
            "length": 16,
            "waveforms": {
                "single": "-7838930358543831875",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2940458658644169372": {
            "length": 16,
            "waveforms": {
                "single": "2940458658644169372",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3937938356340522103": {
            "length": 16,
            "waveforms": {
                "single": "-3937938356340522103",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2443093277863111016": {
            "length": 16,
            "waveforms": {
                "single": "2443093277863111016",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-407960853513900666": {
            "length": 16,
            "waveforms": {
                "single": "-407960853513900666",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-186466794315185418": {
            "length": 16,
            "waveforms": {
                "single": "-186466794315185418",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8019062494911806361": {
            "length": 16,
            "waveforms": {
                "single": "8019062494911806361",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3331504080746732471": {
            "length": 16,
            "waveforms": {
                "single": "-3331504080746732471",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5656062162833568924": {
            "length": 16,
            "waveforms": {
                "single": "-5656062162833568924",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6803883980010437697": {
            "length": 16,
            "waveforms": {
                "single": "-6803883980010437697",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8727287271575636748": {
            "length": 20,
            "waveforms": {
                "single": "-8727287271575636748",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4099465424283198738": {
            "length": 20,
            "waveforms": {
                "single": "4099465424283198738",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8782987615792923714": {
            "length": 20,
            "waveforms": {
                "single": "-8782987615792923714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-577458326565931935": {
            "length": 20,
            "waveforms": {
                "single": "-577458326565931935",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6197449704416648065": {
            "length": 24,
            "waveforms": {
                "single": "-6197449704416648065",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8120852995981847116": {
            "length": 24,
            "waveforms": {
                "single": "-8120852995981847116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3999690016413481202": {
            "length": 24,
            "waveforms": {
                "single": "-3999690016413481202",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7696331005549408066": {
            "length": 24,
            "waveforms": {
                "single": "7696331005549408066",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4497055397194539558": {
            "length": 28,
            "waveforms": {
                "single": "-4497055397194539558",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6849421065956833778": {
            "length": 28,
            "waveforms": {
                "single": "-6849421065956833778",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3929967951231167469": {
            "length": 28,
            "waveforms": {
                "single": "3929967951231167469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1078913819854155787": {
            "length": 28,
            "waveforms": {
                "single": "1078913819854155787",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1300407879052871035": {
            "length": 32,
            "waveforms": {
                "single": "1300407879052871035",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "581548439073097431": {
            "length": 32,
            "waveforms": {
                "single": "581548439073097431",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "803042498271812679": {
            "length": 32,
            "waveforms": {
                "single": "803042498271812679",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8509883324884086996": {
            "length": 32,
            "waveforms": {
                "single": "8509883324884086996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8731377384082802244": {
            "length": 36,
            "waveforms": {
                "single": "8731377384082802244",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8952871443281517492": {
            "length": 36,
            "waveforms": {
                "single": "8952871443281517492",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1187982714666887063": {
            "length": 36,
            "waveforms": {
                "single": "1187982714666887063",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7296112942424867261": {
            "length": 36,
            "waveforms": {
                "single": "-7296112942424867261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2284397184596818163": {
            "length": 40,
            "waveforms": {
                "single": "-2284397184596818163",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2062903125398102915": {
            "length": 40,
            "waveforms": {
                "single": "-2062903125398102915",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6142626163828888864": {
            "length": 40,
            "waveforms": {
                "single": "6142626163828888864",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "134856562605063948": {
            "length": 40,
            "waveforms": {
                "single": "134856562605063948",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "356350621803779196": {
            "length": 44,
            "waveforms": {
                "single": "356350621803779196",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1677962909003028531": {
            "length": 44,
            "waveforms": {
                "single": "-1677962909003028531",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1456468849804313283": {
            "length": 44,
            "waveforms": {
                "single": "-1456468849804313283",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8408645894720403949": {
            "length": 44,
            "waveforms": {
                "single": "8408645894720403949",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "741290838198853580": {
            "length": 48,
            "waveforms": {
                "single": "741290838198853580",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1611074830563440640": {
            "length": 48,
            "waveforms": {
                "single": "-1611074830563440640",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8073886035499565562": {
            "length": 48,
            "waveforms": {
                "single": "-8073886035499565562",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "586684857439726223": {
            "length": 48,
            "waveforms": {
                "single": "586684857439726223",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2012722768223866918": {
            "length": 52,
            "waveforms": {
                "single": "2012722768223866918",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5819894674466490569": {
            "length": 52,
            "waveforms": {
                "single": "5819894674466490569",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5530671901192048263": {
            "length": 52,
            "waveforms": {
                "single": "-5530671901192048263",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8725857397039751275": {
            "length": 52,
            "waveforms": {
                "single": "-8725857397039751275",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8239148421668372680": {
            "length": 56,
            "waveforms": {
                "single": "8239148421668372680",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5195879894213129838": {
            "length": 56,
            "waveforms": {
                "single": "-5195879894213129838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4974385835014414590": {
            "length": 56,
            "waveforms": {
                "single": "-4974385835014414590",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-452068064924411274": {
            "length": 56,
            "waveforms": {
                "single": "-452068064924411274",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2776626147011247727": {
            "length": 60,
            "waveforms": {
                "single": "-2776626147011247727",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2555132087812532479": {
            "length": 60,
            "waveforms": {
                "single": "-2555132087812532479",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6854941052999884747": {
            "length": 60,
            "waveforms": {
                "single": "6854941052999884747",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7076435112198599995": {
            "length": 60,
            "waveforms": {
                "single": "7076435112198599995",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8551223505621091214": {
            "length": 64,
            "waveforms": {
                "single": "-8551223505621091214",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4875837417217398730": {
            "length": 64,
            "waveforms": {
                "single": "4875837417217398730",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3318013688594326868": {
            "length": 64,
            "waveforms": {
                "single": "-3318013688594326868",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7461375328593674379": {
            "length": 64,
            "waveforms": {
                "single": "7461375328593674379",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7295091164419280841": {
            "length": 68,
            "waveforms": {
                "single": "7295091164419280841",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-898759941392444757": {
            "length": 68,
            "waveforms": {
                "single": "-898759941392444757",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8566114997913995126": {
            "length": 68,
            "waveforms": {
                "single": "-8566114997913995126",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4334449875634319589": {
            "length": 68,
            "waveforms": {
                "single": "4334449875634319589",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1520493805809437354": {
            "length": 72,
            "waveforms": {
                "single": "1520493805809437354",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6532209563637486452": {
            "length": 72,
            "waveforms": {
                "single": "6532209563637486452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6753703622836201700": {
            "length": 72,
            "waveforms": {
                "single": "6753703622836201700",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3487511161646358137": {
            "length": 72,
            "waveforms": {
                "single": "-3487511161646358137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2061473250862217442": {
            "length": 76,
            "waveforms": {
                "single": "-2061473250862217442",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9172957370038083811": {
            "length": 76,
            "waveforms": {
                "single": "9172957370038083811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7138643839231276084": {
            "length": 76,
            "waveforms": {
                "single": "7138643839231276084",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3943458343383573072": {
            "length": 76,
            "waveforms": {
                "single": "3943458343383573072",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7407108232274965760": {
            "length": 80,
            "waveforms": {
                "single": "-7407108232274965760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1842817198641536596": {
            "length": 80,
            "waveforms": {
                "single": "-1842817198641536596",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6362712090585455183": {
            "length": 80,
            "waveforms": {
                "single": "6362712090585455183",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4659971083166625397": {
            "length": 40,
            "waveforms": {
                "I": "4659971083166625397_i",
                "Q": "4659971083166625397_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3888782692303067874": {
            "length": 40,
            "waveforms": {
                "I": "3888782692303067874_i",
                "Q": "3888782692303067874_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1826471271909107673": {
            "length": 40,
            "waveforms": {
                "I": "-1826471271909107673_i",
                "Q": "-1826471271909107673_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1271515746381292217": {
            "length": 40,
            "waveforms": {
                "I": "-1271515746381292217_i",
                "Q": "-1271515746381292217_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "3898880453943063528_i": {
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "type": "arbitrary",
        },
        "3898880453943063528_q": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "-5594310502760609825": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
        },
        "5154946332764312586_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "5154946332764312586_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3127692063079506005_i": {
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "type": "arbitrary",
        },
        "3127692063079506005_q": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "8944564030662553975_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "8944564030662553975_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2587561901132669542_i": {
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "type": "arbitrary",
        },
        "-2587561901132669542_q": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "8076108015019869024_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "8076108015019869024_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-2032606375604854086_i": {
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "type": "arbitrary",
        },
        "-2032606375604854086_q": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-2122268873753178136_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-2122268873753178136_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "3277871289942043030": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "2334024383050379740": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "2457984770156014928": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-5209370286365535441": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "3662811506337117414": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-7838930358543831875": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "2940458658644169372": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-3937938356340522103": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "2443093277863111016": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-407960853513900666": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-186466794315185418": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "8019062494911806361": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3331504080746732471": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5656062162833568924": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-6803883980010437697": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8727287271575636748": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4099465424283198738": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8782987615792923714": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-577458326565931935": {
            "sample": 0.25,
            "type": "constant",
        },
        "-6197449704416648065": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8120852995981847116": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3999690016413481202": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
        },
        "7696331005549408066": {
            "sample": 0.25,
            "type": "constant",
        },
        "-4497055397194539558": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6849421065956833778": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3929967951231167469": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
        },
        "1078913819854155787": {
            "sample": 0.25,
            "type": "constant",
        },
        "1300407879052871035": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "581548439073097431": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "803042498271812679": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
        },
        "8509883324884086996": {
            "sample": 0.25,
            "type": "constant",
        },
        "8731377384082802244": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8952871443281517492": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1187982714666887063": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-7296112942424867261": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2284397184596818163": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2062903125398102915": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6142626163828888864": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
        },
        "134856562605063948": {
            "sample": 0.25,
            "type": "constant",
        },
        "356350621803779196": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1677962909003028531": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1456468849804313283": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
        },
        "8408645894720403949": {
            "sample": 0.25,
            "type": "constant",
        },
        "741290838198853580": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1611074830563440640": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8073886035499565562": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
        },
        "586684857439726223": {
            "sample": 0.25,
            "type": "constant",
        },
        "2012722768223866918": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5819894674466490569": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5530671901192048263": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-8725857397039751275": {
            "sample": 0.25,
            "type": "constant",
        },
        "8239148421668372680": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5195879894213129838": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4974385835014414590": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-452068064924411274": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2776626147011247727": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2555132087812532479": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6854941052999884747": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
        },
        "7076435112198599995": {
            "sample": 0.25,
            "type": "constant",
        },
        "-8551223505621091214": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4875837417217398730": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3318013688594326868": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
        },
        "7461375328593674379": {
            "sample": 0.25,
            "type": "constant",
        },
        "7295091164419280841": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-898759941392444757": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8566114997913995126": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
        },
        "4334449875634319589": {
            "sample": 0.25,
            "type": "constant",
        },
        "1520493805809437354": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6532209563637486452": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6753703622836201700": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
        },
        "-3487511161646358137": {
            "sample": 0.25,
            "type": "constant",
        },
        "-2061473250862217442": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9172957370038083811": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7138643839231276084": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
        },
        "3943458343383573072": {
            "sample": 0.25,
            "type": "constant",
        },
        "-7407108232274965760": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1842817198641536596": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6362712090585455183": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
        },
        "4659971083166625397_i": {
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "type": "arbitrary",
        },
        "4659971083166625397_q": {
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "type": "arbitrary",
        },
        "3888782692303067874_i": {
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "type": "arbitrary",
        },
        "3888782692303067874_q": {
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "type": "arbitrary",
        },
        "-1826471271909107673_i": {
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "type": "arbitrary",
        },
        "-1826471271909107673_q": {
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "type": "arbitrary",
        },
        "-1271515746381292217_i": {
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "type": "arbitrary",
        },
        "-1271515746381292217_q": {
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
                        "feedforward": [],
                        "feedback": [],
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
                "1": {
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "-1842817198641536596": "-1842817198641536596",
                "6362712090585455183": "6362712090585455183",
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
                "3127692063079506005": "3127692063079506005",
                "3888782692303067874": "3888782692303067874",
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
                "mixer": "B2/drive_mixer_807",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "3898880453943063528": "3898880453943063528",
                "4659971083166625397": "4659971083166625397",
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
                "mixer": "B1/drive_mixer_2a0",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "-2032606375604854086": "-2032606375604854086",
                "-1271515746381292217": "-1271515746381292217",
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
                "mixer": "B4/drive_mixer_fa8",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "-572130150252921974": "-572130150252921974_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_e8f",
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
                "2767705647931182791": "2767705647931182791_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_bf1",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "6585270118705349135": "6585270118705349135_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_618",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
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
                "-2587561901132669542": "-2587561901132669542",
                "-1826471271909107673": "-1826471271909107673",
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
                "mixer": "B3/drive_mixer_fa7",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-6676865194900398041": "-6676865194900398041_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_16e",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "3898880453943063528": {
            "length": 40,
            "waveforms": {
                "I": "3898880453943063528_i",
                "Q": "3898880453943063528_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5594310502760609825": {
            "length": 16,
            "waveforms": {
                "single": "-5594310502760609825",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6585270118705349135_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5154946332764312586_i",
                "Q": "5154946332764312586_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3127692063079506005": {
            "length": 40,
            "waveforms": {
                "I": "3127692063079506005_i",
                "Q": "3127692063079506005_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6676865194900398041_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8944564030662553975_i",
                "Q": "8944564030662553975_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2587561901132669542": {
            "length": 40,
            "waveforms": {
                "I": "-2587561901132669542_i",
                "Q": "-2587561901132669542_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2767705647931182791_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8076108015019869024_i",
                "Q": "8076108015019869024_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-2032606375604854086": {
            "length": 40,
            "waveforms": {
                "I": "-2032606375604854086_i",
                "Q": "-2032606375604854086_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-572130150252921974_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2122268873753178136_i",
                "Q": "-2122268873753178136_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "3277871289942043030": {
            "length": 16,
            "waveforms": {
                "single": "3277871289942043030",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2334024383050379740": {
            "length": 16,
            "waveforms": {
                "single": "2334024383050379740",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2457984770156014928": {
            "length": 16,
            "waveforms": {
                "single": "2457984770156014928",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5209370286365535441": {
            "length": 16,
            "waveforms": {
                "single": "-5209370286365535441",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3662811506337117414": {
            "length": 16,
            "waveforms": {
                "single": "3662811506337117414",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7838930358543831875": {
            "length": 16,
            "waveforms": {
                "single": "-7838930358543831875",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2940458658644169372": {
            "length": 16,
            "waveforms": {
                "single": "2940458658644169372",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3937938356340522103": {
            "length": 16,
            "waveforms": {
                "single": "-3937938356340522103",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2443093277863111016": {
            "length": 16,
            "waveforms": {
                "single": "2443093277863111016",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-407960853513900666": {
            "length": 16,
            "waveforms": {
                "single": "-407960853513900666",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-186466794315185418": {
            "length": 16,
            "waveforms": {
                "single": "-186466794315185418",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8019062494911806361": {
            "length": 16,
            "waveforms": {
                "single": "8019062494911806361",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3331504080746732471": {
            "length": 16,
            "waveforms": {
                "single": "-3331504080746732471",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5656062162833568924": {
            "length": 16,
            "waveforms": {
                "single": "-5656062162833568924",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6803883980010437697": {
            "length": 16,
            "waveforms": {
                "single": "-6803883980010437697",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8727287271575636748": {
            "length": 20,
            "waveforms": {
                "single": "-8727287271575636748",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4099465424283198738": {
            "length": 20,
            "waveforms": {
                "single": "4099465424283198738",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8782987615792923714": {
            "length": 20,
            "waveforms": {
                "single": "-8782987615792923714",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-577458326565931935": {
            "length": 20,
            "waveforms": {
                "single": "-577458326565931935",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6197449704416648065": {
            "length": 24,
            "waveforms": {
                "single": "-6197449704416648065",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8120852995981847116": {
            "length": 24,
            "waveforms": {
                "single": "-8120852995981847116",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3999690016413481202": {
            "length": 24,
            "waveforms": {
                "single": "-3999690016413481202",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7696331005549408066": {
            "length": 24,
            "waveforms": {
                "single": "7696331005549408066",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4497055397194539558": {
            "length": 28,
            "waveforms": {
                "single": "-4497055397194539558",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6849421065956833778": {
            "length": 28,
            "waveforms": {
                "single": "-6849421065956833778",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3929967951231167469": {
            "length": 28,
            "waveforms": {
                "single": "3929967951231167469",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1078913819854155787": {
            "length": 28,
            "waveforms": {
                "single": "1078913819854155787",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1300407879052871035": {
            "length": 32,
            "waveforms": {
                "single": "1300407879052871035",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "581548439073097431": {
            "length": 32,
            "waveforms": {
                "single": "581548439073097431",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "803042498271812679": {
            "length": 32,
            "waveforms": {
                "single": "803042498271812679",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8509883324884086996": {
            "length": 32,
            "waveforms": {
                "single": "8509883324884086996",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8731377384082802244": {
            "length": 36,
            "waveforms": {
                "single": "8731377384082802244",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8952871443281517492": {
            "length": 36,
            "waveforms": {
                "single": "8952871443281517492",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1187982714666887063": {
            "length": 36,
            "waveforms": {
                "single": "1187982714666887063",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7296112942424867261": {
            "length": 36,
            "waveforms": {
                "single": "-7296112942424867261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2284397184596818163": {
            "length": 40,
            "waveforms": {
                "single": "-2284397184596818163",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2062903125398102915": {
            "length": 40,
            "waveforms": {
                "single": "-2062903125398102915",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6142626163828888864": {
            "length": 40,
            "waveforms": {
                "single": "6142626163828888864",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "134856562605063948": {
            "length": 40,
            "waveforms": {
                "single": "134856562605063948",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "356350621803779196": {
            "length": 44,
            "waveforms": {
                "single": "356350621803779196",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1677962909003028531": {
            "length": 44,
            "waveforms": {
                "single": "-1677962909003028531",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1456468849804313283": {
            "length": 44,
            "waveforms": {
                "single": "-1456468849804313283",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8408645894720403949": {
            "length": 44,
            "waveforms": {
                "single": "8408645894720403949",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "741290838198853580": {
            "length": 48,
            "waveforms": {
                "single": "741290838198853580",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1611074830563440640": {
            "length": 48,
            "waveforms": {
                "single": "-1611074830563440640",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8073886035499565562": {
            "length": 48,
            "waveforms": {
                "single": "-8073886035499565562",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "586684857439726223": {
            "length": 48,
            "waveforms": {
                "single": "586684857439726223",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2012722768223866918": {
            "length": 52,
            "waveforms": {
                "single": "2012722768223866918",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5819894674466490569": {
            "length": 52,
            "waveforms": {
                "single": "5819894674466490569",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5530671901192048263": {
            "length": 52,
            "waveforms": {
                "single": "-5530671901192048263",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8725857397039751275": {
            "length": 52,
            "waveforms": {
                "single": "-8725857397039751275",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8239148421668372680": {
            "length": 56,
            "waveforms": {
                "single": "8239148421668372680",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5195879894213129838": {
            "length": 56,
            "waveforms": {
                "single": "-5195879894213129838",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4974385835014414590": {
            "length": 56,
            "waveforms": {
                "single": "-4974385835014414590",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-452068064924411274": {
            "length": 56,
            "waveforms": {
                "single": "-452068064924411274",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2776626147011247727": {
            "length": 60,
            "waveforms": {
                "single": "-2776626147011247727",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2555132087812532479": {
            "length": 60,
            "waveforms": {
                "single": "-2555132087812532479",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6854941052999884747": {
            "length": 60,
            "waveforms": {
                "single": "6854941052999884747",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7076435112198599995": {
            "length": 60,
            "waveforms": {
                "single": "7076435112198599995",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8551223505621091214": {
            "length": 64,
            "waveforms": {
                "single": "-8551223505621091214",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4875837417217398730": {
            "length": 64,
            "waveforms": {
                "single": "4875837417217398730",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3318013688594326868": {
            "length": 64,
            "waveforms": {
                "single": "-3318013688594326868",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7461375328593674379": {
            "length": 64,
            "waveforms": {
                "single": "7461375328593674379",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7295091164419280841": {
            "length": 68,
            "waveforms": {
                "single": "7295091164419280841",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-898759941392444757": {
            "length": 68,
            "waveforms": {
                "single": "-898759941392444757",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8566114997913995126": {
            "length": 68,
            "waveforms": {
                "single": "-8566114997913995126",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4334449875634319589": {
            "length": 68,
            "waveforms": {
                "single": "4334449875634319589",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1520493805809437354": {
            "length": 72,
            "waveforms": {
                "single": "1520493805809437354",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6532209563637486452": {
            "length": 72,
            "waveforms": {
                "single": "6532209563637486452",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6753703622836201700": {
            "length": 72,
            "waveforms": {
                "single": "6753703622836201700",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3487511161646358137": {
            "length": 72,
            "waveforms": {
                "single": "-3487511161646358137",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2061473250862217442": {
            "length": 76,
            "waveforms": {
                "single": "-2061473250862217442",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9172957370038083811": {
            "length": 76,
            "waveforms": {
                "single": "9172957370038083811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7138643839231276084": {
            "length": 76,
            "waveforms": {
                "single": "7138643839231276084",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3943458343383573072": {
            "length": 76,
            "waveforms": {
                "single": "3943458343383573072",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7407108232274965760": {
            "length": 80,
            "waveforms": {
                "single": "-7407108232274965760",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1842817198641536596": {
            "length": 80,
            "waveforms": {
                "single": "-1842817198641536596",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6362712090585455183": {
            "length": 80,
            "waveforms": {
                "single": "6362712090585455183",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4659971083166625397": {
            "length": 40,
            "waveforms": {
                "I": "4659971083166625397_i",
                "Q": "4659971083166625397_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3888782692303067874": {
            "length": 40,
            "waveforms": {
                "I": "3888782692303067874_i",
                "Q": "3888782692303067874_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1826471271909107673": {
            "length": 40,
            "waveforms": {
                "I": "-1826471271909107673_i",
                "Q": "-1826471271909107673_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1271515746381292217": {
            "length": 40,
            "waveforms": {
                "I": "-1271515746381292217_i",
                "Q": "-1271515746381292217_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "3898880453943063528_i": {
            "type": "arbitrary",
            "samples": [-0.00022142740157317373, -0.0002826829761606054, -0.00035425117413348615, -0.0004356288820668947, -0.0005254580382221801, -0.0006213869286926811, -0.0007199955255671921, -0.0008168119984833208, -0.0009064422734077392, -0.0009828245001067717, -0.0010396060379057538, -0.0010706235080575682, -0.0010704488576227164, -0.0010349490619260794, -0.0009617969948137154, -0.0008508685989463798, -0.0007044682624354848, -0.0005273402858847709, -0.00032644791808218227, -0.00011052957492162269, 0.00011052957492162535, 0.0003264479180821849, 0.0005273402858847735, 0.0007044682624354872, 0.0008508685989463821, 0.0009617969948137175, 0.001034949061926081, 0.0010704488576227182, 0.00107062350805757, 0.0010396060379057551, 0.000982824500106773, 0.0009064422734077401, 0.0008168119984833217, 0.0007199955255671927, 0.0006213869286926815, 0.0005254580382221805, 0.000435628882066895, 0.00035425117413348636, 0.0002826829761606056, 0.0002214274015731739],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3898880453943063528_q": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5594310502760609825": {
            "type": "arbitrary",
            "samples": [0.25] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5154946332764312586_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "5154946332764312586_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3127692063079506005_i": {
            "type": "arbitrary",
            "samples": [0.0001847802794911338, 0.0002358978110714119, 0.00029562118555058855, 0.00036353055679122937, 0.0004384926277133374, 0.0005185449024836567, 0.000600833381512208, 0.0006816263402774137, 0.0007564224456091563, 0.0008201631077734924, 0.000867547073578488, 0.0008934310281524939, 0.0008932852830643261, 0.0008636608457810521, 0.0008026157388505544, 0.0007100464369202522, 0.0005878759426368721, 0.0004400633558467776, 0.0002724194797661072, 9.223648744893448e-05, -9.22364874489315e-05, -0.00027241947976610427, -0.00044006335584677477, -0.0005878759426368692, -0.0007100464369202496, -0.000802615738850552, -0.0008636608457810499, -0.0008932852830643241, -0.0008934310281524921, -0.0008675470735784865, -0.0008201631077734911, -0.0007564224456091552, -0.0006816263402774129, -0.0006008333815122073, -0.0005185449024836561, -0.00043849262771333695, -0.00036353055679122905, -0.0002956211855505882, -0.0002358978110714117, -0.00018478027949113364],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3127692063079506005_q": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8944564030662553975_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "8944564030662553975_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2587561901132669542_i": {
            "type": "arbitrary",
            "samples": [0.00030171729028092756, 0.0003851842227735331, 0.0004827031504638384, 0.0005935885302881006, 0.0007159898654021671, 0.0008467027071136329, 0.000981066920557875, 0.0011129891833639896, 0.0012351195226318389, 0.0013391980526670656, 0.0014165686563095033, 0.001458833104968909, 0.0014585951260395835, 0.0014102230542588634, 0.0013105459442409456, 0.00115939475528007, 0.0009599094498731598, 0.0007185546187270059, 0.00044481839447977256, 0.00015060775497668046, -0.00015060775497667656, -0.00044481839447976866, -0.0007185546187270022, -0.0009599094498731563, -0.0011593947552800666, -0.0013105459442409426, -0.0014102230542588608, -0.001458595126039581, -0.001458833104968907, -0.0014165686563095015, -0.0013391980526670638, -0.0012351195226318376, -0.0011129891833639883, -0.0009810669205578741, -0.0008467027071136323, -0.0007159898654021665, -0.0005935885302881001, -0.0004827031504638381, -0.00038518422277353286, -0.00030171729028092735],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2587561901132669542_q": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8076108015019869024_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "8076108015019869024_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-2032606375604854086_i": {
            "type": "arbitrary",
            "samples": [0.0003245581697577897, 0.00041434379264958276, 0.0005192451877881844, 0.0006385249144990762, 0.000770192387926079, 0.0009108005732581571, 0.0010553365498202035, 0.0011972457129536531, 0.0013286216753579422, 0.0014405792538840596, 0.0015238070380387695, 0.001569271028816185, 0.0015690150341873355, 0.001516981055392401, 0.0014097580972250404, 0.0012471643221047002, 0.0010325773968537242, 0.0007729513005631867, 0.00047849244520435603, 0.00016200920159745652, -0.00016200920159745196, -0.0004784924452043516, -0.0007729513005631823, -0.0010325773968537198, -0.0012471643221046963, -0.001409758097225037, -0.0015169810553923976, -0.0015690150341873324, -0.0015692710288161824, -0.0015238070380387673, -0.0014405792538840579, -0.0013286216753579405, -0.0011972457129536518, -0.0010553365498202022, -0.0009108005732581562, -0.0007701923879260784, -0.0006385249144990755, -0.000519245187788184, -0.00041434379264958243, -0.0003245581697577895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2032606375604854086_q": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2122268873753178136_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-2122268873753178136_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "3277871289942043030": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2334024383050379740": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2457984770156014928": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5209370286365535441": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3662811506337117414": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7838930358543831875": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2940458658644169372": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3937938356340522103": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2443093277863111016": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-407960853513900666": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-186466794315185418": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8019062494911806361": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3331504080746732471": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5656062162833568924": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6803883980010437697": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8727287271575636748": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4099465424283198738": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8782987615792923714": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-577458326565931935": {
            "type": "constant",
            "sample": 0.25,
        },
        "-6197449704416648065": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8120852995981847116": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3999690016413481202": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7696331005549408066": {
            "type": "constant",
            "sample": 0.25,
        },
        "-4497055397194539558": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6849421065956833778": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3929967951231167469": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1078913819854155787": {
            "type": "constant",
            "sample": 0.25,
        },
        "1300407879052871035": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "581548439073097431": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "803042498271812679": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8509883324884086996": {
            "type": "constant",
            "sample": 0.25,
        },
        "8731377384082802244": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8952871443281517492": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1187982714666887063": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7296112942424867261": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2284397184596818163": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2062903125398102915": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6142626163828888864": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "134856562605063948": {
            "type": "constant",
            "sample": 0.25,
        },
        "356350621803779196": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1677962909003028531": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1456468849804313283": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8408645894720403949": {
            "type": "constant",
            "sample": 0.25,
        },
        "741290838198853580": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1611074830563440640": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8073886035499565562": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "586684857439726223": {
            "type": "constant",
            "sample": 0.25,
        },
        "2012722768223866918": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5819894674466490569": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5530671901192048263": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8725857397039751275": {
            "type": "constant",
            "sample": 0.25,
        },
        "8239148421668372680": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5195879894213129838": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4974385835014414590": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-452068064924411274": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2776626147011247727": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2555132087812532479": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6854941052999884747": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7076435112198599995": {
            "type": "constant",
            "sample": 0.25,
        },
        "-8551223505621091214": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4875837417217398730": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3318013688594326868": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7461375328593674379": {
            "type": "constant",
            "sample": 0.25,
        },
        "7295091164419280841": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-898759941392444757": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8566114997913995126": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4334449875634319589": {
            "type": "constant",
            "sample": 0.25,
        },
        "1520493805809437354": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6532209563637486452": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6753703622836201700": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3487511161646358137": {
            "type": "constant",
            "sample": 0.25,
        },
        "-2061473250862217442": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9172957370038083811": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7138643839231276084": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3943458343383573072": {
            "type": "constant",
            "sample": 0.25,
        },
        "-7407108232274965760": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1842817198641536596": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6362712090585455183": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4659971083166625397_i": {
            "type": "arbitrary",
            "samples": [0.0011180555187915678, 0.0015045081475491685, 0.0019931494632565378, 0.0025995569652476707, 0.0033378972155056613, 0.004219497446825634, 0.005251249417242201, 0.006433965280360931, 0.007760843544895696, 0.009216229744590979, 0.010774864198537374, 0.012401792672522064, 0.01405307218212388, 0.015677334902548905, 0.0172181839630987, 0.018617295840194316, 0.019818008261921365, 0.020769094336384877, 0.021428376161292048] + [0.02176582398456596] * 2 + [0.021428376161292048, 0.020769094336384877, 0.019818008261921365, 0.018617295840194316, 0.0172181839630987, 0.015677334902548905, 0.01405307218212388, 0.012401792672522064, 0.010774864198537374, 0.009216229744590979, 0.007760843544895696, 0.006433965280360931, 0.005251249417242201, 0.004219497446825634, 0.0033378972155056613, 0.0025995569652476707, 0.0019931494632565378, 0.0015045081475491685, 0.0011180555187915678],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4659971083166625397_q": {
            "type": "arbitrary",
            "samples": [0.0002214274015731738, 0.0002826829761606055, 0.00035425117413348626, 0.00043562888206689486, 0.0005254580382221803, 0.0006213869286926813, 0.0007199955255671924, 0.0008168119984833213, 0.0009064422734077396, 0.0009828245001067724, 0.0010396060379057545, 0.001070623508057569, 0.0010704488576227173, 0.0010349490619260802, 0.0009617969948137164, 0.000850868598946381, 0.000704468262435486, 0.0005273402858847722, 0.0003264479180821836, 0.00011052957492162402, -0.00011052957492162402, -0.0003264479180821836, -0.0005273402858847722, -0.000704468262435486, -0.000850868598946381, -0.0009617969948137164, -0.0010349490619260802, -0.0010704488576227173, -0.001070623508057569, -0.0010396060379057545, -0.0009828245001067724, -0.0009064422734077396, -0.0008168119984833213, -0.0007199955255671924, -0.0006213869286926813, -0.0005254580382221803, -0.00043562888206689486, -0.00035425117413348626, -0.0002826829761606055, -0.0002214274015731738],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3888782692303067874_i": {
            "type": "arbitrary",
            "samples": [0.0012493039327485741, 0.0016811221929452756, 0.0022271250587747485, 0.0029047186704985986, 0.0037297326012476254, 0.004714823786424647, 0.00586769300677935, 0.007189247754539428, 0.008671888112107319, 0.010298121937161474, 0.01203972431763831, 0.013857637745628482, 0.01570276077461938, 0.017517695516533722, 0.019239424678246013, 0.020802778144181227, 0.022144442064578468, 0.023207176028356858, 0.023943850873928398] + [0.024320911659934084] * 2 + [0.023943850873928398, 0.023207176028356858, 0.022144442064578468, 0.020802778144181227, 0.019239424678246013, 0.017517695516533722, 0.01570276077461938, 0.013857637745628482, 0.01203972431763831, 0.010298121937161474, 0.008671888112107319, 0.007189247754539428, 0.00586769300677935, 0.004714823786424647, 0.0037297326012476254, 0.0029047186704985986, 0.0022271250587747485, 0.0016811221929452756, 0.0012493039327485741],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3888782692303067874_q": {
            "type": "arbitrary",
            "samples": [-0.00018478027949113372, -0.0002358978110714118, -0.0002956211855505884, -0.0003635305567912292, -0.00043849262771333716, -0.0005185449024836564, -0.0006008333815122076, -0.0006816263402774133, -0.0007564224456091558, -0.0008201631077734918, -0.0008675470735784872, -0.000893431028152493, -0.0008932852830643251, -0.000863660845781051, -0.0008026157388505532, -0.0007100464369202509, -0.0005878759426368707, -0.0004400633558467762, -0.00027241947976610573, -9.223648744893299e-05, 9.223648744893299e-05, 0.00027241947976610573, 0.0004400633558467762, 0.0005878759426368707, 0.0007100464369202509, 0.0008026157388505532, 0.000863660845781051, 0.0008932852830643251, 0.000893431028152493, 0.0008675470735784872, 0.0008201631077734918, 0.0007564224456091558, 0.0006816263402774133, 0.0006008333815122076, 0.0005185449024836564, 0.00043849262771333716, 0.0003635305567912292, 0.0002956211855505884, 0.0002358978110714118, 0.00018478027949113372],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1826471271909107673_i": {
            "type": "arbitrary",
            "samples": [0.0016409510779196645, 0.0022081410314293824, 0.002925311583561483, 0.00381532556527005, 0.004898974998745269, 0.006192884670996909, 0.007707169498132072, 0.009443021464190989, 0.011390458136038771, 0.01352650371967906, 0.015814085010857203, 0.018201900274243128, 0.02062545513863524, 0.023009357920839617, 0.025270835892482323, 0.02732428860950993, 0.029086553818695706, 0.030482446681665623, 0.031450063408251405] + [0.03194532984183734] * 2 + [0.031450063408251405, 0.030482446681665623, 0.029086553818695706, 0.02732428860950993, 0.025270835892482323, 0.023009357920839617, 0.02062545513863524, 0.018201900274243128, 0.015814085010857203, 0.01352650371967906, 0.011390458136038771, 0.009443021464190989, 0.007707169498132072, 0.006192884670996909, 0.004898974998745269, 0.00381532556527005, 0.002925311583561483, 0.0022081410314293824, 0.0016409510779196645],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1826471271909107673_q": {
            "type": "arbitrary",
            "samples": [-0.00030171729028092745, -0.00038518422277353297, -0.00048270315046383824, -0.0005935885302881004, -0.0007159898654021668, -0.0008467027071136326, -0.0009810669205578746, -0.001112989183363989, -0.0012351195226318382, -0.0013391980526670647, -0.0014165686563095024, -0.001458833104968908, -0.0014585951260395822, -0.001410223054258862, -0.001310545944240944, -0.0011593947552800683, -0.000959909449873158, -0.000718554618727004, -0.0004448183944797706, -0.0001506077549766785, 0.0001506077549766785, 0.0004448183944797706, 0.000718554618727004, 0.000959909449873158, 0.0011593947552800683, 0.001310545944240944, 0.001410223054258862, 0.0014585951260395822, 0.001458833104968908, 0.0014165686563095024, 0.0013391980526670647, 0.0012351195226318382, 0.001112989183363989, 0.0009810669205578746, 0.0008467027071136326, 0.0007159898654021668, 0.0005935885302881004, 0.00048270315046383824, 0.00038518422277353297, 0.00030171729028092745],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1271515746381292217_i": {
            "type": "arbitrary",
            "samples": [0.0019126784932123073, 0.0025737902352024828, 0.0034097180757614314, 0.004447110734432495, 0.005710203213836212, 0.0072183732230314875, 0.008983410621423042, 0.011006704775378151, 0.013276620246507487, 0.015766376646515118, 0.018432761766696917, 0.021215978744641418, 0.02404085349478909, 0.026819510118246643, 0.02945546943320567, 0.031848956296730166, 0.033903037500186334, 0.03553007824122775, 0.036657923993314044] + [0.03723520229775363] * 2 + [0.036657923993314044, 0.03553007824122775, 0.033903037500186334, 0.031848956296730166, 0.02945546943320567, 0.026819510118246643, 0.02404085349478909, 0.021215978744641418, 0.018432761766696917, 0.015766376646515118, 0.013276620246507487, 0.011006704775378151, 0.008983410621423042, 0.0072183732230314875, 0.005710203213836212, 0.004447110734432495, 0.0034097180757614314, 0.0025737902352024828, 0.0019126784932123073],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1271515746381292217_q": {
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
        "B2/drive_mixer_807": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_2a0": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_fa8": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_e8f": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_bf1": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_618": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_fa7": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_16e": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

