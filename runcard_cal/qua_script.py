
# Single QUA script generated at 2025-05-30 20:03:43.585583
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
    v9 = declare(int, )
    v10 = declare(int, )
    a1 = declare(int, value=[-96741901, -95741901, -94741901, -93741901, -92741901, -91741901, -90741901, -89741901, -88741901, -87741901, -86741901, -85741901, -84741901, -83741901, -82741901, -81741901, -80741901, -79741901, -78741901, -77741901, -76741901, -75741901, -74741901, -73741901, -72741901, -71741901, -70741901, -69741901, -68741901, -67741901])
    a2 = declare(int, value=[-193127360, -192127360, -191127360, -190127360, -189127360, -188127360, -187127360, -186127360, -185127360, -184127360, -183127360, -182127360, -181127360, -180127360, -179127360, -178127360, -177127360, -176127360, -175127360, -174127360, -173127360, -172127360, -171127360, -170127360, -169127360, -168127360, -167127360, -166127360, -165127360, -164127360])
    set_dc_offset("0/flux", "single", 0.47542516543032876)
    set_dc_offset("1/flux", "single", 0.3612981245395635)
    set_dc_offset("2/flux", "single", 0.5347210367348649)
    set_dc_offset("3/flux", "single", 0.8036553966185815)
    set_dc_offset("4/flux", "single", -0.07458798541755325)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "1/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "2/acquisition")
    with for_(v1,0,(v1<500),(v1+1)):
        with for_(v8,0.22111111111111112,(v8<2.1005555555555553),(v8+0.22111111111111112)):
            with for_each_((v9,v10),(a1,a2)):
                update_frequency("1/drive", v9, "Hz", False)
                update_frequency("2/drive", v10, "Hz", False)
                align()
                play("-9216978649607500600"*amp(v8), "1/drive")
                play("-9216978649607500600"*amp(v8), "1/drive")
                wait(11, "1/acquisition")
                measure("-3783826931632695953", "1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*-0.34242253033211995)-(v3*0.9395460663112525))>0.002643476183011851)))
                r1 = declare_stream()
                save(v4, r1)
                play("-9216978649607500600"*amp(v8), "2/drive")
                play("-9216978649607500600"*amp(v8), "2/drive")
                wait(11, "2/acquisition")
                measure("-8134695544567686510", "2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*-0.5222371793801518)-(v6*-0.8528002863936335))>-0.0004427367050247332)))
                r2 = declare_stream()
                save(v7, r2)
                wait(50000, )
    with stream_processing():
        r1.buffer(30).buffer(9).buffer(500).save("-3783826931632695953_1|acquisition_shots")
        r2.buffer(30).buffer(9).buffer(500).save("-8134695544567686510_2|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "4": {
                    "type": "LF",
                    "analog_outputs": {
                        "4": {
                            "offset": 0.47542516543032876,
                            "filter": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "1": {
                            "offset": 0.3612981245395635,
                            "filter": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "3": {
                            "offset": 0.5347210367348649,
                            "filter": {
                                "feedforward": [1.2636351569036441, -0.8232188600289677, -0.023584638849310263, -0.021177265809741615, 0.0019818771228793768, 0.018566245435279526, -0.00871919444276136, 0.0029207057818416583, -0.0026753197501048864, -0.009824924082361835, -0.00796679653743725, 0.011947706348409613, 0.003341842518842916, -0.004751172959027721, 0.0023062425297495108, 0.008316586034492656, -0.00771451388109923, 0.00015556469587163935, 0.0008330091025414715, -0.004488698619546089, 0.005365344729781505, -0.0006837922723672002, 0.0037696780547130616, -0.00911021303345722, 0.00036562761421022683, 0.0023091143796012716, -0.008705373420043074, 0.006767549541320114, 0.00589556012888095, -0.011731828850264376, 0.005008575336492184],
                                "feedback": [0.5874633945103754],
                            },
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "2": {
                            "offset": 0.8036553966185815,
                            "filter": {
                                "feedforward": [1.2234520961227922, -0.6969389285337555, -0.02769138330673253, -0.024860121491298535, -0.014292774551705262, 0.021421949905432187, -0.0011777971109444671, -0.0040987595190198, -0.008531719373108315, 0.0002077367545341895, -0.005295525394849506, 0.004158710161347265, 0.0038254634052596803, -0.0014707735693399151, 0.007813406095929058, -0.0022362981062549496, -0.0026825389313108704, -0.008546084311691708, 0.004949281082275419, -0.003016595671100195, 0.0008142471401767621, -0.0026335679848660267, 0.002497669374809954, -0.0021172027048112947, -0.0010707770484308118, -0.004577738364072215, 0.0013221649026706503, 0.009149085842958002, -0.010857175640066214, 0.003358522719122027, 0.00021572576825085632],
                                "feedback": [0.5091791853685043],
                            },
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": -0.07458798541755325,
                            "filter": {
                                "feedforward": [1.2381134243279095, -1.0529559918952465, 0.35306911939962116, -0.1638040790979965, -0.003226904445920352, 0.02526132654819567, -0.0018251092763359004, -0.004035743016841075, -0.010524269759444803, -0.007939220124088072, -0.015375126663621137, 0.01923982395182343, 0.006046019934125838, 0.004704896045249214, 0.0020939935701098037, 0.004295117900596931, 0.003824449652170595, -0.026540394249118505, -0.01495546551537057, 0.009664533684332425, -0.00015299699362413943, 0.014765621765855335, -0.012132948560529487, 0.014667660315440907, 0.0016430974676778995, -0.007047402321197055, -0.0213316020466652, 0.010012067579274909, 0.006614372986725079, -0.012248690590664094, 0.00696600204623011],
                                "feedback": [0.6136716461257441],
                            },
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {},
                },
                "1": {
                    "type": "LF",
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
                    },
                    "digital_outputs": {
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
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0,
                        },
                        "2": {
                            "offset": 0,
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
        },
    },
    "octaves": {
        "octave1": {
            "connectivity": ('con1', 1),
            "RF_outputs": {
                "1": {
                    "LO_frequency": 5700000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "3": {
                    "LO_frequency": 4900000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "RF_inputs": {},
        },
        "octave2": {
            "connectivity": ('con1', 2),
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7550000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7550000000.0,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
    },
    "elements": {
        "0/flux": {
            "singleInput": {
                "port": ('con1', 4, 4),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "1/flux": {
            "singleInput": {
                "port": ('con1', 4, 1),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "2/flux": {
            "singleInput": {
                "port": ('con1', 4, 3),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "3/flux": {
            "singleInput": {
                "port": ('con1', 4, 2),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "4/flux": {
            "singleInput": {
                "port": ('con1', 4, 5),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "2/drive": {
            "RF_inputs": {
                "port": ('octave1', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 1, 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -178127360.0,
            "operations": {
                "6754733634982680334": "6754733634982680334",
                "-9216978649607500600": "-9216978649607500600",
            },
        },
        "2/acquisition": {
            "RF_inputs": {
                "port": ('octave2', 1),
            },
            "RF_outputs": {
                "port": ('octave2', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 2, 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -50037942.0,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "-8134695544567686510": "-8134695544567686510_2/acquisition",
            },
        },
        "1/acquisition": {
            "RF_inputs": {
                "port": ('octave2', 1),
            },
            "RF_outputs": {
                "port": ('octave2', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 2, 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -211216529.0,
            "time_of_flight": 308.0,
            "smearing": 0.0,
            "operations": {
                "-3783826931632695953": "-3783826931632695953_1/acquisition",
            },
        },
        "1/drive": {
            "RF_inputs": {
                "port": ('octave1', 3),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 1, 5),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -81741901.0,
            "operations": {
                "6754733634982680334": "6754733634982680334",
                "-9216978649607500600": "-9216978649607500600",
            },
        },
    },
    "pulses": {
        "6754733634982680334": {
            "length": 40,
            "waveforms": {
                "I": "6754733634982680334_i",
                "Q": "6754733634982680334_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3783826931632695953_1/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "-4319750391190997304_i",
                "Q": "-4319750391190997304_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_1/acquisition",
                "sin": "sine_weights_1/acquisition",
                "minus_sin": "minus_sine_weights_1/acquisition",
            },
        },
        "-8134695544567686510_2/acquisition": {
            "length": 1000.0,
            "waveforms": {
                "I": "-4237273788562026683_i",
                "Q": "-4237273788562026683_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_2/acquisition",
                "sin": "sine_weights_2/acquisition",
                "minus_sin": "minus_sine_weights_2/acquisition",
            },
        },
        "-9216978649607500600": {
            "length": 40,
            "waveforms": {
                "I": "-9216978649607500600_i",
                "Q": "-9216978649607500600_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6754733634982680334_i": {
            "samples": [0.02647692516786481, 0.027364860214556017, 0.02823351412350265, 0.02907921347290821, 0.02989829283854879, 0.03068712083304984, 0.0314421266020593, 0.032159826510833385, 0.03283685074515002, 0.033469969544485945, 0.034056118783223385, 0.03459242461741514, 0.03507622692039201, 0.035505101240232276, 0.03587687902575106, 0.03618966588505701, 0.03644185766164836, 0.036632154137197864, 0.03675957019726441] + [0.03682344432577217] * 2 + [0.03675957019726441, 0.036632154137197864, 0.03644185766164836, 0.03618966588505701, 0.03587687902575106, 0.035505101240232276, 0.03507622692039201, 0.03459242461741514, 0.034056118783223385, 0.033469969544485945, 0.03283685074515002, 0.032159826510833385, 0.0314421266020593, 0.03068712083304984, 0.02989829283854879, 0.02907921347290821, 0.02823351412350265, 0.027364860214556017, 0.02647692516786481],
            "type": "arbitrary",
        },
        "6754733634982680334_q": {
            "samples": [-0.002420156441125143, -0.0023730464717310294, -0.002316030455443577, -0.0022490954170452443, -0.0021722978390508107, -0.0020857652441213567, -0.0019896970740365654, -0.0018843648346191437, -0.0017701114854807433, -0.001647350063517668, -0.0015165615395654163, -0.0013782919183501347, -0.0012331486026700318, -0.0010817960534133272, -0.0009249507873826446, -0.0007633757647629213, -0.0005978742272614185, -0.0004292830562952875, -0.0002584657279495154, -8.630494763852854e-05, 8.630494763852854e-05, 0.0002584657279495154, 0.0004292830562952875, 0.0005978742272614185, 0.0007633757647629213, 0.0009249507873826446, 0.0010817960534133272, 0.0012331486026700318, 0.0013782919183501347, 0.0015165615395654163, 0.001647350063517668, 0.0017701114854807433, 0.0018843648346191437, 0.0019896970740365654, 0.0020857652441213567, 0.0021722978390508107, 0.0022490954170452443, 0.002316030455443577, 0.0023730464717310294, 0.002420156441125143],
            "type": "arbitrary",
        },
        "-4319750391190997304_i": {
            "sample": 0.0035,
            "type": "constant",
        },
        "-4319750391190997304_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4237273788562026683_i": {
            "sample": 0.004,
            "type": "constant",
        },
        "-4237273788562026683_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-9216978649607500600_i": {
            "samples": [0.016255799315031617, 0.016800956799606682, 0.017334276417671417, 0.017853502831525356, 0.018356385613665666, 0.018840695233887404, 0.019304239326900324, 0.019744879076851657, 0.020160545549249353, 0.020549255797109624, 0.020909128566820017, 0.021238399430291845, 0.021535435173509015, 0.02179874727755785, 0.02202700433659563, 0.022219043267892223, 0.022373879181926, 0.022490713795359326, 0.02256894228634995] + [0.022608158509829893] * 2 + [0.02256894228634995, 0.022490713795359326, 0.022373879181926, 0.022219043267892223, 0.02202700433659563, 0.02179874727755785, 0.021535435173509015, 0.021238399430291845, 0.020909128566820017, 0.020549255797109624, 0.020160545549249353, 0.019744879076851657, 0.019304239326900324, 0.018840695233887404, 0.018356385613665666, 0.017853502831525356, 0.017334276417671417, 0.016800956799606682, 0.016255799315031617],
            "type": "arbitrary",
        },
        "-9216978649607500600_q": {
            "samples": [-0.0014858816561396087, -0.0014569579724658917, -0.0014219523623871086, -0.0013808568596257894, -0.0013337061422428963, -0.0012805785041782847, -0.0012215963949054115, -0.0011569265084092767, -0.0010867794085142228, -0.0010114086837639895, -0.0009311096314912039, -0.0008462174773006909, -0.0007571051428186764, -0.0006641805811130908, -0.0005678837055528561, -0.0004686829439321016, -0.00036707145532847345, -0.0002635630522893671, -0.00015868787545089807, -5.2987871507413815e-05, 5.2987871507413815e-05, 0.00015868787545089807, 0.0002635630522893671, 0.00036707145532847345, 0.0004686829439321016, 0.0005678837055528561, 0.0006641805811130908, 0.0007571051428186764, 0.0008462174773006909, 0.0009311096314912039, 0.0010114086837639895, 0.0010867794085142228, 0.0011569265084092767, 0.0012215963949054115, 0.0012805785041782847, 0.0013337061422428963, 0.0013808568596257894, 0.0014219523623871086, 0.0014569579724658917, 0.0014858816561396087],
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_1/acquisition": {
            "cosine": [(1.0, 1000.0)],
            "sine": [(-0.0, 1000.0)],
        },
        "sine_weights_1/acquisition": {
            "cosine": [(0.0, 1000.0)],
            "sine": [(1.0, 1000.0)],
        },
        "minus_sine_weights_1/acquisition": {
            "cosine": [(-0.0, 1000.0)],
            "sine": [(-1.0, 1000.0)],
        },
        "cosine_weights_2/acquisition": {
            "cosine": [(1.0, 1000.0)],
            "sine": [(-0.0, 1000.0)],
        },
        "sine_weights_2/acquisition": {
            "cosine": [(0.0, 1000.0)],
            "sine": [(1.0, 1000.0)],
        },
        "minus_sine_weights_2/acquisition": {
            "cosine": [(-0.0, 1000.0)],
            "sine": [(-1.0, 1000.0)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "4": {
                    "type": "LF",
                    "analog_outputs": {
                        "4": {
                            "offset": 0.47542516543032876,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "1": {
                            "offset": 0.3612981245395635,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "3": {
                            "offset": 0.5347210367348649,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [1.2636351569036441, -0.8232188600289677, -0.023584638849310263, -0.021177265809741615, 0.0019818771228793768, 0.018566245435279526, -0.00871919444276136, 0.0029207057818416583, -0.0026753197501048864, -0.009824924082361835, -0.00796679653743725, 0.011947706348409613, 0.003341842518842916, -0.004751172959027721, 0.0023062425297495108, 0.008316586034492656, -0.00771451388109923, 0.00015556469587163935, 0.0008330091025414715, -0.004488698619546089, 0.005365344729781505, -0.0006837922723672002, 0.0037696780547130616, -0.00911021303345722, 0.00036562761421022683, 0.0023091143796012716, -0.008705373420043074, 0.006767549541320114, 0.00589556012888095, -0.011731828850264376, 0.005008575336492184],
                                "feedback": [0.5874633945103754],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "2": {
                            "offset": 0.8036553966185815,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [1.2234520961227922, -0.6969389285337555, -0.02769138330673253, -0.024860121491298535, -0.014292774551705262, 0.021421949905432187, -0.0011777971109444671, -0.0040987595190198, -0.008531719373108315, 0.0002077367545341895, -0.005295525394849506, 0.004158710161347265, 0.0038254634052596803, -0.0014707735693399151, 0.007813406095929058, -0.0022362981062549496, -0.0026825389313108704, -0.008546084311691708, 0.004949281082275419, -0.003016595671100195, 0.0008142471401767621, -0.0026335679848660267, 0.002497669374809954, -0.0021172027048112947, -0.0010707770484308118, -0.004577738364072215, 0.0013221649026706503, 0.009149085842958002, -0.010857175640066214, 0.003358522719122027, 0.00021572576825085632],
                                "feedback": [0.5091791853685043],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": -0.07458798541755325,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [1.2381134243279095, -1.0529559918952465, 0.35306911939962116, -0.1638040790979965, -0.003226904445920352, 0.02526132654819567, -0.0018251092763359004, -0.004035743016841075, -0.010524269759444803, -0.007939220124088072, -0.015375126663621137, 0.01923982395182343, 0.006046019934125838, 0.004704896045249214, 0.0020939935701098037, 0.004295117900596931, 0.003824449652170595, -0.026540394249118505, -0.01495546551537057, 0.009664533684332425, -0.00015299699362413943, 0.014765621765855335, -0.012132948560529487, 0.014667660315440907, 0.0016430974676778995, -0.007047402321197055, -0.0213316020466652, 0.010012067579274909, 0.006614372986725079, -0.012248690590664094, 0.00696600204623011],
                                "feedback": [0.6136716461257441],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
                "1": {
                    "type": "LF",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                    },
                },
                "2": {
                    "type": "LF",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "0/flux": {
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
                "port": ('con1', 4, 4),
            },
            "intermediate_frequency": 0,
        },
        "1/flux": {
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
                "port": ('con1', 4, 1),
            },
            "intermediate_frequency": 0,
        },
        "2/flux": {
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
                "port": ('con1', 4, 3),
            },
            "intermediate_frequency": 0,
        },
        "3/flux": {
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
                "port": ('con1', 4, 2),
            },
            "intermediate_frequency": 0,
        },
        "4/flux": {
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
                "port": ('con1', 4, 5),
            },
            "intermediate_frequency": 0,
        },
        "2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "6754733634982680334": "6754733634982680334",
                "-9216978649607500600": "-9216978649607500600",
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
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "2/drive_mixer_491",
                "lo_frequency": 5700000000.0,
            },
            "intermediate_frequency": -178127360.0,
        },
        "2/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con1', 2, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 2, 1),
                "out2": ('con1', 2, 2),
            },
            "operations": {
                "-8134695544567686510": "-8134695544567686510_2/acquisition",
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
                "I": ('con1', 2, 1),
                "Q": ('con1', 2, 2),
                "mixer": "2/acquisition_mixer_289",
                "lo_frequency": 7550000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": -50037942.0,
        },
        "1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con1', 2, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 2, 1),
                "out2": ('con1', 2, 2),
            },
            "operations": {
                "-3783826931632695953": "-3783826931632695953_1/acquisition",
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
                "I": ('con1', 2, 1),
                "Q": ('con1', 2, 2),
                "mixer": "1/acquisition_mixer_b50",
                "lo_frequency": 7550000000.0,
            },
            "smearing": 0,
            "time_of_flight": 308,
            "intermediate_frequency": -211216529.0,
        },
        "1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con1', 1, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "6754733634982680334": "6754733634982680334",
                "-9216978649607500600": "-9216978649607500600",
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "1/drive_mixer_0c2",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": -81741901.0,
        },
    },
    "pulses": {
        "6754733634982680334": {
            "length": 40,
            "waveforms": {
                "I": "6754733634982680334_i",
                "Q": "6754733634982680334_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3783826931632695953_1/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "-4319750391190997304_i",
                "Q": "-4319750391190997304_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_1/acquisition",
                "sin": "sine_weights_1/acquisition",
                "minus_sin": "minus_sine_weights_1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-8134695544567686510_2/acquisition": {
            "length": 1000,
            "waveforms": {
                "I": "-4237273788562026683_i",
                "Q": "-4237273788562026683_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_2/acquisition",
                "sin": "sine_weights_2/acquisition",
                "minus_sin": "minus_sine_weights_2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-9216978649607500600": {
            "length": 40,
            "waveforms": {
                "I": "-9216978649607500600_i",
                "Q": "-9216978649607500600_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "6754733634982680334_i": {
            "type": "arbitrary",
            "samples": [0.02647692516786481, 0.027364860214556017, 0.02823351412350265, 0.02907921347290821, 0.02989829283854879, 0.03068712083304984, 0.0314421266020593, 0.032159826510833385, 0.03283685074515002, 0.033469969544485945, 0.034056118783223385, 0.03459242461741514, 0.03507622692039201, 0.035505101240232276, 0.03587687902575106, 0.03618966588505701, 0.03644185766164836, 0.036632154137197864, 0.03675957019726441] + [0.03682344432577217] * 2 + [0.03675957019726441, 0.036632154137197864, 0.03644185766164836, 0.03618966588505701, 0.03587687902575106, 0.035505101240232276, 0.03507622692039201, 0.03459242461741514, 0.034056118783223385, 0.033469969544485945, 0.03283685074515002, 0.032159826510833385, 0.0314421266020593, 0.03068712083304984, 0.02989829283854879, 0.02907921347290821, 0.02823351412350265, 0.027364860214556017, 0.02647692516786481],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6754733634982680334_q": {
            "type": "arbitrary",
            "samples": [-0.002420156441125143, -0.0023730464717310294, -0.002316030455443577, -0.0022490954170452443, -0.0021722978390508107, -0.0020857652441213567, -0.0019896970740365654, -0.0018843648346191437, -0.0017701114854807433, -0.001647350063517668, -0.0015165615395654163, -0.0013782919183501347, -0.0012331486026700318, -0.0010817960534133272, -0.0009249507873826446, -0.0007633757647629213, -0.0005978742272614185, -0.0004292830562952875, -0.0002584657279495154, -8.630494763852854e-05, 8.630494763852854e-05, 0.0002584657279495154, 0.0004292830562952875, 0.0005978742272614185, 0.0007633757647629213, 0.0009249507873826446, 0.0010817960534133272, 0.0012331486026700318, 0.0013782919183501347, 0.0015165615395654163, 0.001647350063517668, 0.0017701114854807433, 0.0018843648346191437, 0.0019896970740365654, 0.0020857652441213567, 0.0021722978390508107, 0.0022490954170452443, 0.002316030455443577, 0.0023730464717310294, 0.002420156441125143],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4319750391190997304_i": {
            "type": "constant",
            "sample": 0.0035,
        },
        "-4319750391190997304_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4237273788562026683_i": {
            "type": "constant",
            "sample": 0.004,
        },
        "-4237273788562026683_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-9216978649607500600_i": {
            "type": "arbitrary",
            "samples": [0.016255799315031617, 0.016800956799606682, 0.017334276417671417, 0.017853502831525356, 0.018356385613665666, 0.018840695233887404, 0.019304239326900324, 0.019744879076851657, 0.020160545549249353, 0.020549255797109624, 0.020909128566820017, 0.021238399430291845, 0.021535435173509015, 0.02179874727755785, 0.02202700433659563, 0.022219043267892223, 0.022373879181926, 0.022490713795359326, 0.02256894228634995] + [0.022608158509829893] * 2 + [0.02256894228634995, 0.022490713795359326, 0.022373879181926, 0.022219043267892223, 0.02202700433659563, 0.02179874727755785, 0.021535435173509015, 0.021238399430291845, 0.020909128566820017, 0.020549255797109624, 0.020160545549249353, 0.019744879076851657, 0.019304239326900324, 0.018840695233887404, 0.018356385613665666, 0.017853502831525356, 0.017334276417671417, 0.016800956799606682, 0.016255799315031617],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9216978649607500600_q": {
            "type": "arbitrary",
            "samples": [-0.0014858816561396087, -0.0014569579724658917, -0.0014219523623871086, -0.0013808568596257894, -0.0013337061422428963, -0.0012805785041782847, -0.0012215963949054115, -0.0011569265084092767, -0.0010867794085142228, -0.0010114086837639895, -0.0009311096314912039, -0.0008462174773006909, -0.0007571051428186764, -0.0006641805811130908, -0.0005678837055528561, -0.0004686829439321016, -0.00036707145532847345, -0.0002635630522893671, -0.00015868787545089807, -5.2987871507413815e-05, 5.2987871507413815e-05, 0.00015868787545089807, 0.0002635630522893671, 0.00036707145532847345, 0.0004686829439321016, 0.0005678837055528561, 0.0006641805811130908, 0.0007571051428186764, 0.0008462174773006909, 0.0009311096314912039, 0.0010114086837639895, 0.0010867794085142228, 0.0011569265084092767, 0.0012215963949054115, 0.0012805785041782847, 0.0013337061422428963, 0.0013808568596257894, 0.0014219523623871086, 0.0014569579724658917, 0.0014858816561396087],
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
        "cosine_weights_1/acquisition": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "sine_weights_1/acquisition": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "minus_sine_weights_1/acquisition": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "cosine_weights_2/acquisition": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "sine_weights_2/acquisition": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "minus_sine_weights_2/acquisition": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
    },
    "mixers": {
        "2/drive_mixer_491": [{'intermediate_frequency': -178127360.0, 'lo_frequency': 5700000000.0, 'correction': (1, 0, 0, 1)}],
        "2/acquisition_mixer_289": [{'intermediate_frequency': -50037942.0, 'lo_frequency': 7550000000.0, 'correction': (1, 0, 0, 1)}],
        "1/acquisition_mixer_b50": [{'intermediate_frequency': -211216529.0, 'lo_frequency': 7550000000.0, 'correction': (1, 0, 0, 1)}],
        "1/drive_mixer_0c2": [{'intermediate_frequency': -81741901.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

