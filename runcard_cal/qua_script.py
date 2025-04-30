
# Single QUA script generated at 2025-04-30 13:39:59.601760
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
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
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "B4/acquisition")
    with for_(v1,0,(v1<2000),(v1+1)):
        with for_(v4,0,(v4<=79),(v4+1)):
            align()
            with if_((v4==0), unsafe=True):
                play("2501332154477808784", "B4/drive")
            with elif_((v4==1)):
                play("8453401411484346734", "B4/drive")
            with elif_((v4==2)):
                play("-6851736067330374729", "B4/drive")
            with elif_((v4==3)):
                play("-7795582974222038019", "B4/drive")
            with elif_((v4==4)):
                play("1076598818480614836", "B4/drive")
            with elif_((v4==5)):
                play("-8292948355003096375", "B4/drive")
            with elif_((v4==6)):
                play("7801430049944161021", "B4/drive")
            with elif_((v4==7)):
                play("7524235646528158807", "B4/drive")
            with elif_((v4==8)):
                play("-143119409993391562", "B4/drive")
            with elif_((v4==9)):
                play("8729062382709261293", "B4/drive")
            with elif_((v4==10)):
                play("3757872592209918210", "B4/drive")
            with elif_((v4==11)):
                play("-3491538922151461600", "B4/drive")
            with elif_((v4==12)):
                play("-3270044862952746352", "B4/drive")
            with elif_((v4==13)):
                play("4935484426274245427", "B4/drive")
            with elif_((v4==14)):
                play("-2065218126771643866", "B4/drive")
            with elif_((v4==15)):
                play("7133244114277412290", "B4/drive")
            with elif_((v4==16)):
                play("1513252736426696160", "B4/drive")
            with elif_((v4==17)):
                play("-6080290142405374980", "B4/drive")
            with elif_((v4==18)):
                play("-7839815485381487353", "B4/drive")
            with elif_((v4==19)):
                play("3013385709495993123", "B4/drive")
            with elif_((v4==20)):
                play("-3661036395203492869", "B4/drive")
            with elif_((v4==21)):
                play("861281374886510447", "B4/drive")
            with elif_((v4==22)):
                play("-5473855866811585348", "B4/drive")
            with elif_((v4==23)):
                play("2066108111067612933", "B4/drive")
            with elif_((v4==24)):
                play("4612752936911847132", "B4/drive")
            with elif_((v4==25)):
                play("1246221591281584831", "B4/drive")
            with elif_((v4==26)):
                play("8513744939115156904", "B4/drive")
            with elif_((v4==27)):
                play("6576965080401429237", "B4/drive")
            with elif_((v4==28)):
                play("-2004664248783405147", "B4/drive")
            with elif_((v4==29)):
                play("-1783170189584689899", "B4/drive")
            with elif_((v4==30)):
                play("8898685155510231288", "B4/drive")
            with elif_((v4==31)):
                play("9120179214708946536", "B4/drive")
            with elif_((v4==32)):
                play("636083557617192212", "B4/drive")
            with elif_((v4==33)):
                play("-1398229973189615515", "B4/drive")
            with elif_((v4==34)):
                play("5869293374643956558", "B4/drive")
            with elif_((v4==35)):
                play("2502762029013694257", "B4/drive")
            with elif_((v4==36)):
                play("8067053062647123421", "B4/drive")
            with elif_((v4==37)):
                play("-4525155426148970305", "B4/drive")
            with elif_((v4==38)):
                play("6254233591039030942", "B4/drive")
            with elif_((v4==39)):
                play("3059048095191327930", "B4/drive")
            with elif_((v4==40)):
                play("8451993279042197805", "B4/drive")
            with elif_((v4==41)):
                play("8673487338240913053", "B4/drive")
            with elif_((v4==42)):
                play("7525665521064044280", "B4/drive")
            with elif_((v4==43)):
                play("-7113906646402883685", "B4/drive")
            with elif_((v4==44)):
                play("8730492257245146766", "B4/drive")
            with elif_((v4==45)):
                play("-2342287230438707354", "B4/drive")
            with elif_((v4==46)):
                play("-4694652899201001574", "B4/drive")
            with elif_((v4==47)):
                play("-8061184244831263875", "B4/drive")
            with elif_((v4==48)):
                play("538556917825762772", "B4/drive")
            with elif_((v4==49)):
                play("-8116884589048550841", "B4/drive")
            with elif_((v4==50)):
                play("2736316605828929635", "B4/drive")
            with elif_((v4==51)):
                play("2957810665027644883", "B4/drive")
            with elif_((v4==52)):
                play("-408720680602617418", "B4/drive")
            with elif_((v4==53)):
                play("5155570353030811746", "B4/drive")
            with elif_((v4==54)):
                play("-3038280752780913852", "B4/drive")
            with elif_((v4==55)):
                play("3342750881422719267", "B4/drive")
            with elif_((v4==56)):
                play("-3535646133561972208", "B4/drive")
            with elif_((v4==57)):
                play("5540510569425886130", "B4/drive")
            with elif_((v4==58)):
                play("5762004628624601378", "B4/drive")
            with elif_((v4==59)):
                play("4614182811447732605", "B4/drive")
            with elif_((v4==60)):
                play("-3053172245073817764", "B4/drive")
            with elif_((v4==61)):
                play("6811942499450899468", "B4/drive")
            with elif_((v4==62)):
                play("-855412557070650901", "B4/drive")
            with elif_((v4==63)):
                play("-6401591757231887802", "B4/drive")
            with elif_((v4==64)):
                play("-6180097698033172554", "B4/drive")
            with elif_((v4==65)):
                play("2025431591193819225", "B4/drive")
            with elif_((v4==66)):
                play("-3982338010030005691", "B4/drive")
            with elif_((v4==67)):
                play("6797051007157995556", "B4/drive")
            with elif_((v4==68)):
                play("-5795157481638098170", "B4/drive")
            with elif_((v4==69)):
                play("-8990342977485801182", "B4/drive")
            with elif_((v4==70)):
                play("-3597397793634931307", "B4/drive")
            with elif_((v4==71)):
                play("-3375903734436216059", "B4/drive")
            with elif_((v4==72)):
                play("-6571089230283919071", "B4/drive")
            with elif_((v4==73)):
                play("6255663465574916415", "B4/drive")
            with elif_((v4==74)):
                play("-4373329542280752208", "B4/drive")
            with elif_((v4==75)):
                play("4055065770593715150", "B4/drive")
            with elif_((v4==76)):
                play("1702700101831420930", "B4/drive")
            with elif_((v4==77)):
                play("-5964654954690129439", "B4/drive")
            with elif_((v4==78)):
                play("3900459789834587793", "B4/drive")
            with elif_((v4==79)):
                play("-3766895266686962576", "B4/drive")
            with if_(((v4/4)<4)):
                wait(4, "B4/acquisition")
            with else_():
                wait((v4/4), "B4/acquisition")
            measure("305353331920272181", "B4/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
            r1 = declare_stream()
            save(v2, r1)
            r2 = declare_stream()
            save(v3, r2)
            wait(12500, )
    with stream_processing():
        r1.buffer(80).average().save("305353331920272181_B4|acquisition_I")
        r2.buffer(80).average().save("305353331920272181_B4|acquisition_Q")


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
                "305353331920272181": "305353331920272181_B4/acquisition",
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
                "8451993279042197805": "8451993279042197805",
                "2501332154477808784": "2501332154477808784",
                "8453401411484346734": "8453401411484346734",
                "-6851736067330374729": "-6851736067330374729",
                "-7795582974222038019": "-7795582974222038019",
                "1076598818480614836": "1076598818480614836",
                "-8292948355003096375": "-8292948355003096375",
                "7801430049944161021": "7801430049944161021",
                "7524235646528158807": "7524235646528158807",
                "-143119409993391562": "-143119409993391562",
                "8729062382709261293": "8729062382709261293",
                "3757872592209918210": "3757872592209918210",
                "-3491538922151461600": "-3491538922151461600",
                "-3270044862952746352": "-3270044862952746352",
                "4935484426274245427": "4935484426274245427",
                "-2065218126771643866": "-2065218126771643866",
                "7133244114277412290": "7133244114277412290",
                "1513252736426696160": "1513252736426696160",
                "-6080290142405374980": "-6080290142405374980",
                "-7839815485381487353": "-7839815485381487353",
                "3013385709495993123": "3013385709495993123",
                "-3661036395203492869": "-3661036395203492869",
                "861281374886510447": "861281374886510447",
                "-5473855866811585348": "-5473855866811585348",
                "2066108111067612933": "2066108111067612933",
                "4612752936911847132": "4612752936911847132",
                "1246221591281584831": "1246221591281584831",
                "8513744939115156904": "8513744939115156904",
                "6576965080401429237": "6576965080401429237",
                "-2004664248783405147": "-2004664248783405147",
                "-1783170189584689899": "-1783170189584689899",
                "8898685155510231288": "8898685155510231288",
                "9120179214708946536": "9120179214708946536",
                "636083557617192212": "636083557617192212",
                "-1398229973189615515": "-1398229973189615515",
                "5869293374643956558": "5869293374643956558",
                "2502762029013694257": "2502762029013694257",
                "8067053062647123421": "8067053062647123421",
                "-4525155426148970305": "-4525155426148970305",
                "6254233591039030942": "6254233591039030942",
                "3059048095191327930": "3059048095191327930",
                "8673487338240913053": "8673487338240913053",
                "7525665521064044280": "7525665521064044280",
                "-7113906646402883685": "-7113906646402883685",
                "8730492257245146766": "8730492257245146766",
                "-2342287230438707354": "-2342287230438707354",
                "-4694652899201001574": "-4694652899201001574",
                "-8061184244831263875": "-8061184244831263875",
                "538556917825762772": "538556917825762772",
                "-8116884589048550841": "-8116884589048550841",
                "2736316605828929635": "2736316605828929635",
                "2957810665027644883": "2957810665027644883",
                "-408720680602617418": "-408720680602617418",
                "5155570353030811746": "5155570353030811746",
                "-3038280752780913852": "-3038280752780913852",
                "3342750881422719267": "3342750881422719267",
                "-3535646133561972208": "-3535646133561972208",
                "5540510569425886130": "5540510569425886130",
                "5762004628624601378": "5762004628624601378",
                "4614182811447732605": "4614182811447732605",
                "-3053172245073817764": "-3053172245073817764",
                "6811942499450899468": "6811942499450899468",
                "-855412557070650901": "-855412557070650901",
                "-6401591757231887802": "-6401591757231887802",
                "-6180097698033172554": "-6180097698033172554",
                "2025431591193819225": "2025431591193819225",
                "-3982338010030005691": "-3982338010030005691",
                "6797051007157995556": "6797051007157995556",
                "-5795157481638098170": "-5795157481638098170",
                "-8990342977485801182": "-8990342977485801182",
                "-3597397793634931307": "-3597397793634931307",
                "-3375903734436216059": "-3375903734436216059",
                "-6571089230283919071": "-6571089230283919071",
                "6255663465574916415": "6255663465574916415",
                "-4373329542280752208": "-4373329542280752208",
                "4055065770593715150": "4055065770593715150",
                "1702700101831420930": "1702700101831420930",
                "-5964654954690129439": "-5964654954690129439",
                "3900459789834587793": "3900459789834587793",
                "-3766895266686962576": "-3766895266686962576",
            },
        },
    },
    "pulses": {
        "8451993279042197805": {
            "length": 40,
            "waveforms": {
                "I": "8451993279042197805_i",
                "Q": "8451993279042197805_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "305353331920272181_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "7245105225113558137_i",
                "Q": "7245105225113558137_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "2501332154477808784": {
            "length": 16,
            "waveforms": {
                "I": "2501332154477808784_i",
                "Q": "2501332154477808784_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8453401411484346734": {
            "length": 16,
            "waveforms": {
                "I": "8453401411484346734_i",
                "Q": "8453401411484346734_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6851736067330374729": {
            "length": 16,
            "waveforms": {
                "I": "-6851736067330374729_i",
                "Q": "-6851736067330374729_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7795582974222038019": {
            "length": 16,
            "waveforms": {
                "I": "-7795582974222038019_i",
                "Q": "-7795582974222038019_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1076598818480614836": {
            "length": 16,
            "waveforms": {
                "I": "1076598818480614836_i",
                "Q": "1076598818480614836_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8292948355003096375": {
            "length": 16,
            "waveforms": {
                "I": "-8292948355003096375_i",
                "Q": "-8292948355003096375_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7801430049944161021": {
            "length": 16,
            "waveforms": {
                "I": "7801430049944161021_i",
                "Q": "7801430049944161021_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7524235646528158807": {
            "length": 16,
            "waveforms": {
                "I": "7524235646528158807_i",
                "Q": "7524235646528158807_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-143119409993391562": {
            "length": 16,
            "waveforms": {
                "I": "-143119409993391562_i",
                "Q": "-143119409993391562_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8729062382709261293": {
            "length": 16,
            "waveforms": {
                "I": "8729062382709261293_i",
                "Q": "8729062382709261293_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3757872592209918210": {
            "length": 16,
            "waveforms": {
                "I": "3757872592209918210_i",
                "Q": "3757872592209918210_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3491538922151461600": {
            "length": 16,
            "waveforms": {
                "I": "-3491538922151461600_i",
                "Q": "-3491538922151461600_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3270044862952746352": {
            "length": 16,
            "waveforms": {
                "I": "-3270044862952746352_i",
                "Q": "-3270044862952746352_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4935484426274245427": {
            "length": 16,
            "waveforms": {
                "I": "4935484426274245427_i",
                "Q": "4935484426274245427_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2065218126771643866": {
            "length": 16,
            "waveforms": {
                "I": "-2065218126771643866_i",
                "Q": "-2065218126771643866_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7133244114277412290": {
            "length": 16,
            "waveforms": {
                "I": "7133244114277412290_i",
                "Q": "7133244114277412290_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1513252736426696160": {
            "length": 16,
            "waveforms": {
                "I": "1513252736426696160_i",
                "Q": "1513252736426696160_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6080290142405374980": {
            "length": 20,
            "waveforms": {
                "I": "-6080290142405374980_i",
                "Q": "-6080290142405374980_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7839815485381487353": {
            "length": 20,
            "waveforms": {
                "I": "-7839815485381487353_i",
                "Q": "-7839815485381487353_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3013385709495993123": {
            "length": 20,
            "waveforms": {
                "I": "3013385709495993123_i",
                "Q": "3013385709495993123_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3661036395203492869": {
            "length": 20,
            "waveforms": {
                "I": "-3661036395203492869_i",
                "Q": "-3661036395203492869_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "861281374886510447": {
            "length": 24,
            "waveforms": {
                "I": "861281374886510447_i",
                "Q": "861281374886510447_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5473855866811585348": {
            "length": 24,
            "waveforms": {
                "I": "-5473855866811585348_i",
                "Q": "-5473855866811585348_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2066108111067612933": {
            "length": 24,
            "waveforms": {
                "I": "2066108111067612933_i",
                "Q": "2066108111067612933_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4612752936911847132": {
            "length": 24,
            "waveforms": {
                "I": "4612752936911847132_i",
                "Q": "4612752936911847132_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1246221591281584831": {
            "length": 28,
            "waveforms": {
                "I": "1246221591281584831_i",
                "Q": "1246221591281584831_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8513744939115156904": {
            "length": 28,
            "waveforms": {
                "I": "8513744939115156904_i",
                "Q": "8513744939115156904_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6576965080401429237": {
            "length": 28,
            "waveforms": {
                "I": "6576965080401429237_i",
                "Q": "6576965080401429237_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2004664248783405147": {
            "length": 28,
            "waveforms": {
                "I": "-2004664248783405147_i",
                "Q": "-2004664248783405147_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1783170189584689899": {
            "length": 32,
            "waveforms": {
                "I": "-1783170189584689899_i",
                "Q": "-1783170189584689899_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8898685155510231288": {
            "length": 32,
            "waveforms": {
                "I": "8898685155510231288_i",
                "Q": "8898685155510231288_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9120179214708946536": {
            "length": 32,
            "waveforms": {
                "I": "9120179214708946536_i",
                "Q": "9120179214708946536_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "636083557617192212": {
            "length": 32,
            "waveforms": {
                "I": "636083557617192212_i",
                "Q": "636083557617192212_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1398229973189615515": {
            "length": 36,
            "waveforms": {
                "I": "-1398229973189615515_i",
                "Q": "-1398229973189615515_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5869293374643956558": {
            "length": 36,
            "waveforms": {
                "I": "5869293374643956558_i",
                "Q": "5869293374643956558_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2502762029013694257": {
            "length": 36,
            "waveforms": {
                "I": "2502762029013694257_i",
                "Q": "2502762029013694257_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8067053062647123421": {
            "length": 36,
            "waveforms": {
                "I": "8067053062647123421_i",
                "Q": "8067053062647123421_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4525155426148970305": {
            "length": 40,
            "waveforms": {
                "I": "-4525155426148970305_i",
                "Q": "-4525155426148970305_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6254233591039030942": {
            "length": 40,
            "waveforms": {
                "I": "6254233591039030942_i",
                "Q": "6254233591039030942_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3059048095191327930": {
            "length": 40,
            "waveforms": {
                "I": "3059048095191327930_i",
                "Q": "3059048095191327930_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8673487338240913053": {
            "length": 44,
            "waveforms": {
                "I": "8673487338240913053_i",
                "Q": "8673487338240913053_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7525665521064044280": {
            "length": 44,
            "waveforms": {
                "I": "7525665521064044280_i",
                "Q": "7525665521064044280_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7113906646402883685": {
            "length": 44,
            "waveforms": {
                "I": "-7113906646402883685_i",
                "Q": "-7113906646402883685_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8730492257245146766": {
            "length": 44,
            "waveforms": {
                "I": "8730492257245146766_i",
                "Q": "8730492257245146766_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2342287230438707354": {
            "length": 48,
            "waveforms": {
                "I": "-2342287230438707354_i",
                "Q": "-2342287230438707354_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4694652899201001574": {
            "length": 48,
            "waveforms": {
                "I": "-4694652899201001574_i",
                "Q": "-4694652899201001574_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8061184244831263875": {
            "length": 48,
            "waveforms": {
                "I": "-8061184244831263875_i",
                "Q": "-8061184244831263875_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "538556917825762772": {
            "length": 48,
            "waveforms": {
                "I": "538556917825762772_i",
                "Q": "538556917825762772_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8116884589048550841": {
            "length": 52,
            "waveforms": {
                "I": "-8116884589048550841_i",
                "Q": "-8116884589048550841_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2736316605828929635": {
            "length": 52,
            "waveforms": {
                "I": "2736316605828929635_i",
                "Q": "2736316605828929635_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2957810665027644883": {
            "length": 52,
            "waveforms": {
                "I": "2957810665027644883_i",
                "Q": "2957810665027644883_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-408720680602617418": {
            "length": 52,
            "waveforms": {
                "I": "-408720680602617418_i",
                "Q": "-408720680602617418_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5155570353030811746": {
            "length": 56,
            "waveforms": {
                "I": "5155570353030811746_i",
                "Q": "5155570353030811746_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3038280752780913852": {
            "length": 56,
            "waveforms": {
                "I": "-3038280752780913852_i",
                "Q": "-3038280752780913852_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3342750881422719267": {
            "length": 56,
            "waveforms": {
                "I": "3342750881422719267_i",
                "Q": "3342750881422719267_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3535646133561972208": {
            "length": 56,
            "waveforms": {
                "I": "-3535646133561972208_i",
                "Q": "-3535646133561972208_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5540510569425886130": {
            "length": 60,
            "waveforms": {
                "I": "5540510569425886130_i",
                "Q": "5540510569425886130_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5762004628624601378": {
            "length": 60,
            "waveforms": {
                "I": "5762004628624601378_i",
                "Q": "5762004628624601378_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4614182811447732605": {
            "length": 60,
            "waveforms": {
                "I": "4614182811447732605_i",
                "Q": "4614182811447732605_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3053172245073817764": {
            "length": 60,
            "waveforms": {
                "I": "-3053172245073817764_i",
                "Q": "-3053172245073817764_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6811942499450899468": {
            "length": 64,
            "waveforms": {
                "I": "6811942499450899468_i",
                "Q": "6811942499450899468_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-855412557070650901": {
            "length": 64,
            "waveforms": {
                "I": "-855412557070650901_i",
                "Q": "-855412557070650901_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6401591757231887802": {
            "length": 64,
            "waveforms": {
                "I": "-6401591757231887802_i",
                "Q": "-6401591757231887802_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6180097698033172554": {
            "length": 64,
            "waveforms": {
                "I": "-6180097698033172554_i",
                "Q": "-6180097698033172554_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2025431591193819225": {
            "length": 68,
            "waveforms": {
                "I": "2025431591193819225_i",
                "Q": "2025431591193819225_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3982338010030005691": {
            "length": 68,
            "waveforms": {
                "I": "-3982338010030005691_i",
                "Q": "-3982338010030005691_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6797051007157995556": {
            "length": 68,
            "waveforms": {
                "I": "6797051007157995556_i",
                "Q": "6797051007157995556_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5795157481638098170": {
            "length": 68,
            "waveforms": {
                "I": "-5795157481638098170_i",
                "Q": "-5795157481638098170_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8990342977485801182": {
            "length": 72,
            "waveforms": {
                "I": "-8990342977485801182_i",
                "Q": "-8990342977485801182_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3597397793634931307": {
            "length": 72,
            "waveforms": {
                "I": "-3597397793634931307_i",
                "Q": "-3597397793634931307_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3375903734436216059": {
            "length": 72,
            "waveforms": {
                "I": "-3375903734436216059_i",
                "Q": "-3375903734436216059_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6571089230283919071": {
            "length": 72,
            "waveforms": {
                "I": "-6571089230283919071_i",
                "Q": "-6571089230283919071_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6255663465574916415": {
            "length": 76,
            "waveforms": {
                "I": "6255663465574916415_i",
                "Q": "6255663465574916415_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4373329542280752208": {
            "length": 76,
            "waveforms": {
                "I": "-4373329542280752208_i",
                "Q": "-4373329542280752208_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4055065770593715150": {
            "length": 76,
            "waveforms": {
                "I": "4055065770593715150_i",
                "Q": "4055065770593715150_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1702700101831420930": {
            "length": 76,
            "waveforms": {
                "I": "1702700101831420930_i",
                "Q": "1702700101831420930_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5964654954690129439": {
            "length": 80,
            "waveforms": {
                "I": "-5964654954690129439_i",
                "Q": "-5964654954690129439_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3900459789834587793": {
            "length": 80,
            "waveforms": {
                "I": "3900459789834587793_i",
                "Q": "3900459789834587793_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3766895266686962576": {
            "length": 80,
            "waveforms": {
                "I": "-3766895266686962576_i",
                "Q": "-3766895266686962576_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "8451993279042197805_i": {
            "samples": [0.017174528874170345, 0.0231108546822752, 0.030616908044275828, 0.03993197601488685, 0.051273672141679986, 0.06481599483836066, 0.08066480888120327, 0.09883258981843836, 0.11921485946761638, 0.14157114847976826, 0.16551344113309885, 0.19050480299575512, 0.21587022281644042, 0.2408206358525739, 0.264489725836364, 0.2859815810506245, 0.3044258083809585, 0.3190355079648841, 0.32916278210089667] + [0.3343463416710043] * 2 + [0.32916278210089667, 0.3190355079648841, 0.3044258083809585, 0.2859815810506245, 0.264489725836364, 0.2408206358525739, 0.21587022281644042, 0.19050480299575512, 0.16551344113309885, 0.14157114847976826, 0.11921485946761638, 0.09883258981843836, 0.08066480888120327, 0.06481599483836066, 0.051273672141679986, 0.03993197601488685, 0.030616908044275828, 0.0231108546822752, 0.017174528874170345],
            "type": "arbitrary",
        },
        "8451993279042197805_q": {
            "samples": [-0.0029143076986720266, -0.0037205204408097114, -0.004662462354279371, -0.005733511732295232, -0.006915794500772051, -0.008178358673214188, -0.009476191692004622, -0.010750437744539836, -0.01193010294582253, -0.012935404501678717, -0.013682732391426474, -0.01409096755751043, -0.014088668902948038, -0.013621439792345822, -0.012658651849910958, -0.011198672300041734, -0.00927183025271327, -0.006940567626477934, -0.004296530935752181, -0.0014547304842873624, 0.0014547304842873624, 0.004296530935752181, 0.006940567626477934, 0.00927183025271327, 0.011198672300041734, 0.012658651849910958, 0.013621439792345822, 0.014088668902948038, 0.01409096755751043, 0.013682732391426474, 0.012935404501678717, 0.01193010294582253, 0.010750437744539836, 0.009476191692004622, 0.008178358673214188, 0.006915794500772051, 0.005733511732295232, 0.004662462354279371, 0.0037205204408097114, 0.0029143076986720266],
            "type": "arbitrary",
        },
        "7245105225113558137_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "7245105225113558137_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2501332154477808784_i": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2501332154477808784_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8453401411484346734_i": {
            "samples": [0.335] + [0.0] * 15,
            "type": "arbitrary",
        },
        "8453401411484346734_q": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-6851736067330374729_i": {
            "samples": [0.1533741761934908] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-6851736067330374729_q": {
            "samples": [-0.266930499069949, 0.266930499069949] + [0.0] * 14,
            "type": "arbitrary",
        },
        "-7795582974222038019_i": {
            "samples": [0.08353298994039425, 0.335, 0.08353298994039425] + [0.0] * 13,
            "type": "arbitrary",
        },
        "-7795582974222038019_q": {
            "samples": [-0.12922646358212256, 0.0, 0.12922646358212256] + [0.0] * 13,
            "type": "arbitrary",
        },
        "1076598818480614836_i": {
            "samples": [0.057761244004407214] + [0.2755634834035527] * 2 + [0.057761244004407214] + [0.0] * 12,
            "type": "arbitrary",
        },
        "1076598818480614836_q": {
            "samples": [-0.07539521028729018, -0.1198968104930001, 0.1198968104930001, 0.07539521028729018] + [0.0] * 12,
            "type": "arbitrary",
        },
        "-8292948355003096375_i": {
            "samples": [0.04533731988426526, 0.2031877710037322, 0.335, 0.2031877710037322, 0.04533731988426526] + [0.0] * 11,
            "type": "arbitrary",
        },
        "-8292948355003096375_q": {
            "samples": [-0.05049888307844908, -0.11316014617848255, 0.0, 0.11316014617848255, 0.05049888307844908] + [0.0] * 11,
            "type": "arbitrary",
        },
        "7801430049944161021_i": {
            "samples": [0.038244189603245146, 0.15337417619349084] + [0.3071465441702297] * 2 + [0.15337417619349084, 0.038244189603245146] + [0.0] * 10,
            "type": "arbitrary",
        },
        "7801430049944161021_q": {
            "samples": [-0.03697761640728767, -0.08897683302331631, -0.05939488957134061, 0.05939488957134061, 0.08897683302331631, 0.03697761640728767] + [0.0] * 10,
            "type": "arbitrary",
        },
        "7524235646528158807_i": {
            "samples": [0.03372408142392078, 0.12075000918027008, 0.25957053867588853, 0.335, 0.25957053867588853, 0.12075000918027008, 0.03372408142392078] + [0.0] * 9,
            "type": "arbitrary",
        },
        "7524235646528158807_q": {
            "samples": [-0.028747577024901508, -0.06862099807419665, -0.07375564422527067, 0.0, 0.07375564422527067, 0.06862099807419665, 0.028747577024901508] + [0.0] * 9,
            "type": "arbitrary",
        },
        "-143119409993391562_i": {
            "samples": [0.03061690804427584, 0.09883258981843837, 0.21587022281644047] + [0.3190355079648841] * 2 + [0.21587022281644047, 0.09883258981843837, 0.03061690804427584] + [0.0] * 8,
            "type": "arbitrary",
        },
        "-143119409993391562_q": {
            "samples": [-0.023312311771396862, -0.05375218872269918, -0.07044334451474019, -0.03470283813238967, 0.03470283813238967, 0.07044334451474019, 0.05375218872269918, 0.023312311771396862] + [0.0] * 8,
            "type": "arbitrary",
        },
        "8729062382709261293_i": {
            "samples": [0.028360426188547543, 0.08353298994039424, 0.18070151492460493, 0.28709395863081844, 0.335, 0.28709395863081844, 0.18070151492460493, 0.08353298994039424, 0.028360426188547543] + [0.0] * 7,
            "type": "arbitrary",
        },
        "8729062382709261293_q": {
            "samples": [-0.019499508635346482, -0.043075487860707515, -0.062121611418438694, -0.04934861599274998, 0.0, 0.04934861599274998, 0.062121611418438694, 0.043075487860707515, 0.019499508635346482] + [0.0] * 7,
            "type": "arbitrary",
        },
        "3757872592209918210_i": {
            "samples": [0.026652435420606278, 0.07244883088801225, 0.15337417619349078, 0.2528712666663175] + [0.3246931335495753] * 2 + [0.2528712666663175, 0.15337417619349078, 0.07244883088801225, 0.026652435420606278] + [0.0] * 6,
            "type": "arbitrary",
        },
        "3757872592209918210_q": {
            "samples": [-0.016698803562208948, -0.035304931106790914, -0.05338609981398979, -0.05281127899382707, -0.02260367483862046, 0.02260367483862046, 0.05281127899382707, 0.05338609981398979, 0.035304931106790914, 0.016698803562208948] + [0.0] * 6,
            "type": "arbitrary",
        },
        "-3491538922151461600_i": {
            "samples": [0.025317248028875385, 0.06415089032991214, 0.13220826782069808, 0.2216074096425405, 0.3021201381461697, 0.335, 0.3021201381461697, 0.2216074096425405, 0.13220826782069808, 0.06415089032991214, 0.025317248028875385] + [0.0] * 5,
            "type": "arbitrary",
        },
        "-3491538922151461600_q": {
            "samples": [-0.0145658915715221, -0.02952658714553387, -0.045638403314736224, -0.050999373970149676, -0.03476404045804078, 0.0, 0.03476404045804078, 0.050999373970149676, 0.045638403314736224, 0.02952658714553387, 0.0145658915715221] + [0.0] * 5,
            "type": "arbitrary",
        },
        "-3270044862952746352_i": {
            "samples": [0.0242462623660549, 0.057761244004407214, 0.11567244840843037, 0.19472646098759389, 0.2755634834035527] + [0.32780835134453135] * 2 + [0.2755634834035527, 0.19472646098759389, 0.11567244840843037, 0.057761244004407214, 0.0242462623660549] + [0.0] * 4,
            "type": "arbitrary",
        },
        "-3270044862952746352_q": {
            "samples": [-0.012893800316100719, -0.02513173676243006, -0.039144560642527484, -0.047069374808617497, -0.039965603497666695, -0.0158475988076564, 0.0158475988076564, 0.039965603497666695, 0.047069374808617497, 0.039144560642527484, 0.02513173676243006, 0.012893800316100719] + [0.0] * 4,
            "type": "arbitrary",
        },
        "4935484426274245427_i": {
            "samples": [0.023368959819382324, 0.05272122394039205, 0.10258570331944422, 0.1721644385966181, 0.24920417581611157, 0.3111160627814493, 0.335, 0.3111160627814493, 0.24920417581611157, 0.1721644385966181, 0.10258570331944422, 0.05272122394039205, 0.023368959819382324] + [0.0] * 3,
            "type": "arbitrary",
        },
        "4935484426274245427_q": {
            "samples": [-0.011551539566671312, -0.02171724476462936, -0.03380617765412908, -0.042551408787418456, -0.04106147526988523, -0.025631361264570395, 0.0, 0.025631361264570395, 0.04106147526988523, 0.042551408787418456, 0.03380617765412908, 0.02171724476462936, 0.011551539566671312] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2065218126771643866_i": {
            "samples": [0.02263766757455748, 0.048663114865035544, 0.09208172060258603, 0.1533741761934908, 0.2248725040764974, 0.29021894876787196] + [0.3297011553355644] * 2 + [0.29021894876787196, 0.2248725040764974, 0.1533741761934908, 0.09208172060258603, 0.048663114865035544, 0.02263766757455748] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2065218126771643866_q": {
            "samples": [-0.010452613832385651, -0.019012641735589635, -0.029435119992593836, -0.038132928438564126, -0.03993523420290153, -0.030924087593800692, -0.01171036264248111, 0.01171036264248111, 0.030924087593800692, 0.03993523420290153, 0.038132928438564126, 0.029435119992593836, 0.019012641735589635, 0.010452613832385651] + [0.0] * 2,
            "type": "arbitrary",
        },
        "7133244114277412290_i": {
            "samples": [0.02201905708653771, 0.04533731988426526, 0.08353298994039424, 0.13772261731990781, 0.2031877710037322, 0.26824702997713074, 0.31689642208376645, 0.335, 0.31689642208376645, 0.26824702997713074, 0.2031877710037322, 0.13772261731990781, 0.08353298994039424, 0.04533731988426526, 0.02201905708653771, 0.0],
            "type": "arbitrary",
        },
        "7133244114277412290_q": {
            "samples": [-0.009537843271337833, -0.016832961026149697, -0.025845292716424512, -0.03408934707923215, -0.03772004872616085, -0.033198490871774115, -0.019609691441397726, 0.0, 0.019609691441397726, 0.033198490871774115, 0.03772004872616085, 0.03408934707923215, 0.025845292716424512, 0.016832961026149697, 0.009537843271337833, 0.0],
            "type": "arbitrary",
        },
        "1513252736426696160_i": {
            "samples": [0.021489157391914197, 0.04256967948039585, 0.07648386094795835, 0.1246314522890466, 0.18419334621823985, 0.2468929274591887, 0.30014546803251035] + [0.3309355027251901] * 2 + [0.30014546803251035, 0.2468929274591887, 0.18419334621823985, 0.1246314522890466, 0.07648386094795835, 0.04256967948039585, 0.021489157391914197],
            "type": "arbitrary",
        },
        "1513252736426696160_q": {
            "samples": [-0.008765498650879703, -0.01504907179073338, -0.022878548609393957, -0.030502549922442612, -0.03506210283421528, -0.03356948162409208, -0.024486066597442055, -0.008999312691392763, 0.008999312691392763, 0.024486066597442055, 0.03356948162409208, 0.03506210283421528, 0.030502549922442612, 0.022878548609393957, 0.01504907179073338, 0.008765498650879703],
            "type": "arbitrary",
        },
        "-6080290142405374980_i": {
            "samples": [0.02103030393080685, 0.04023564801392218, 0.07060049149916642, 0.11361501285083114, 0.16768530014691396, 0.22697892583119728, 0.2817781759247988, 0.32081926804380095, 0.335, 0.32081926804380095, 0.2817781759247988, 0.22697892583119728, 0.16768530014691396, 0.11361501285083114, 0.07060049149916642, 0.04023564801392218, 0.02103030393080685] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6080290142405374980_q": {
            "samples": [-0.008105384765647523, -0.013568978048576047, -0.020407841588762153, -0.027368048190716376, -0.032314175812809647, -0.03280536625162984, -0.027150351011893187, -0.015456051041178698, 0.0, 0.015456051041178698, 0.027150351011893187, 0.03280536625162984, 0.032314175812809647, 0.027368048190716376, 0.020407841588762153, 0.013568978048576047, 0.008105384765647523] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7839815485381487353_i": {
            "samples": [0.02062920298020961, 0.03824418960324513, 0.06563539443280968, 0.10427984082962836, 0.15337417619349078, 0.2088304141698222, 0.26322363356897543, 0.3071465441702297] + [0.3317844364035494] * 2 + [0.3071465441702297, 0.26322363356897543, 0.2088304141698222, 0.15337417619349078, 0.10427984082962836, 0.06563539443280968, 0.03824418960324513, 0.02062920298020961] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7839815485381487353_q": {
            "samples": [-0.007535157025052252, -0.012325872135762552, -0.01833337358481, -0.024646427732106457, -0.02965894434110543, -0.031408899964035425, -0.028278464294322545, -0.01979829652378021, -0.007128808466805954, 0.007128808466805954, 0.01979829652378021, 0.028278464294322545, 0.031408899964035425, 0.02965894434110543, 0.024646427732106457, 0.01833337358481, 0.012325872135762552, 0.007535157025052252] + [0.0] * 2,
            "type": "arbitrary",
        },
        "3013385709495993123_i": {
            "samples": [0.020275664839288273, 0.03652745062458811, 0.06140275056025776, 0.09631202061755613, 0.14096047928005417, 0.19250341836808385, 0.2453034910191875, 0.2916709772433678, 0.32359880522556134, 0.335, 0.32359880522556134, 0.2916709772433678, 0.2453034910191875, 0.19250341836808385, 0.14096047928005417, 0.09631202061755613, 0.06140275056025776, 0.03652745062458811, 0.020275664839288273, 0.0],
            "type": "arbitrary",
        },
        "3013385709495993123_q": {
            "samples": [-0.007037952859044462, -0.011270367818087594, -0.016577330898278873, -0.022287455306265302, -0.027182920347148504, -0.029697998274578037, -0.028382701128608717, -0.022498416527740355, -0.012480605332509729, 0.0, 0.012480605332509729, 0.022498416527740355, 0.028382701128608717, 0.029697998274578037, 0.027182920347148504, 0.022287455306265302, 0.016577330898278873, 0.011270367818087594, 0.007037952859044462, 0.0],
            "type": "arbitrary",
        },
        "-3661036395203492869_i": {
            "samples": [0.01996175178526534, 0.035033965431815486, 0.0577612440044072, 0.08946236480082503, 0.130166972716642, 0.17791715699684066, 0.22845015164876664, 0.2755634834035527, 0.31225433494044175] + [0.3323930093171816] * 2 + [0.31225433494044175, 0.2755634834035527, 0.22845015164876664, 0.17791715699684066, 0.130166972716642, 0.08946236480082503, 0.0577612440044072, 0.035033965431815486, 0.01996175178526534],
            "type": "arbitrary",
        },
        "-3661036395203492869_q": {
            "samples": [-0.006600824824183911, -0.010365354837203843, -0.015079042057458032, -0.020240893584573465, -0.02491950694517732, -0.027868031646555515, -0.02783142518118325, -0.023979362098600028, -0.01630330624053474, -0.0057849263850300635, 0.0057849263850300635, 0.01630330624053474, 0.023979362098600028, 0.02783142518118325, 0.027868031646555515, 0.02491950694517732, 0.020240893584573465, 0.015079042057458032, 0.010365354837203843, 0.006600824824183911],
            "type": "arbitrary",
        },
        "861281374886510447_i": {
            "samples": [0.019681191070026235, 0.03372408142392077, 0.05460205803061823, 0.08353298994039424, 0.12075000918027004, 0.16492878122452376, 0.21285598123754915, 0.25957053867588853, 0.29909218802334814, 0.32563784554601377, 0.335, 0.32563784554601377, 0.29909218802334814, 0.25957053867588853, 0.21285598123754915, 0.16492878122452376, 0.12075000918027004, 0.08353298994039424, 0.05460205803061823, 0.03372408142392077, 0.019681191070026235] + [0.0] * 3,
            "type": "arbitrary",
        },
        "861281374886510447_q": {
            "samples": [-0.006213677809230891, -0.009582525674967169, -0.013791018851085725, -0.01846092336887465, -0.022873666024732214, -0.02603537317309713, -0.026880862697220138, -0.024585214741756897, -0.018885670943618493, -0.010280925821591165, 0.0, 0.010280925821591165, 0.018885670943618493, 0.024585214741756897, 0.026880862697220138, 0.02603537317309713, 0.022873666024732214, 0.01846092336887465, 0.013791018851085725, 0.009582525674967169, 0.006213677809230891] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5473855866811585348_i": {
            "samples": [0.019428961804270194, 0.03256681271497687, 0.05184040103472302, 0.07836621697191876, 0.11250111992155204, 0.1533741761934908, 0.198570657632372, 0.24414359709767736, 0.28506443503845413, 0.31608811754110755] + [0.33284400283199606] * 2 + [0.31608811754110755, 0.28506443503845413, 0.24414359709767736, 0.198570657632372, 0.1533741761934908, 0.11250111992155204, 0.07836621697191876, 0.05184040103472302, 0.03256681271497687, 0.019428961804270194] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5473855866811585348_q": {
            "samples": [-0.005868531962848885, -0.00889998844227892, -0.012675872407015893, -0.01690755179010933, -0.02103588476873646, -0.024266409006358996, -0.02570503317100362, -0.0245812500178251, -0.02050093303452428, -0.013639234925629937, -0.004787417702303888, 0.004787417702303888, 0.013639234925629937, 0.02050093303452428, 0.0245812500178251, 0.02570503317100362, 0.024266409006358996, 0.02103588476873646, 0.01690755179010933, 0.012675872407015893, 0.00889998844227892, 0.005868531962848885] + [0.0] * 2,
            "type": "arbitrary",
        },
        "2066108111067612933_i": {
            "samples": [0.019200998633816527, 0.03153763427294032, 0.04940945852482564, 0.07383576222521489, 0.1052444291296256, 0.14308929931825132, 0.18556278562274675, 0.2295357287420097, 0.27082290641336215, 0.3047868175633003, 0.32717691276241306, 0.335, 0.32717691276241306, 0.3047868175633003, 0.27082290641336215, 0.2295357287420097, 0.18556278562274675, 0.14308929931825132, 0.1052444291296256, 0.07383576222521489, 0.04940945852482564, 0.03153763427294032, 0.019200998633816527, 0.0],
            "type": "arbitrary",
        },
        "2066108111067612933_q": {
            "samples": [-0.005559001256830622, -0.008300598029216923, -0.011703961224731566, -0.015546657104542746, -0.019389982946130112, -0.022596370018955887, -0.02441974688567169, -0.024165209110380902, -0.02138390023601445, -0.016043770660172343, -0.008611185017168907, 0.0, 0.008611185017168907, 0.016043770660172343, 0.02138390023601445, 0.024165209110380902, 0.02441974688567169, 0.022596370018955887, 0.019389982946130112, 0.015546657104542746, 0.011703961224731566, 0.008300598029216923, 0.005559001256830622, 0.0],
            "type": "arbitrary",
        },
        "4612752936911847132_i": {
            "samples": [0.018993975525273342, 0.03061690804427584, 0.04725602620808614, 0.06983987939141756, 0.09883258981843837, 0.13392056842844244, 0.17375799850320736, 0.21587022281644047, 0.25679767497423667, 0.2925094141462924, 0.3190355079648841] + [0.33318743003725093] * 2 + [0.3190355079648841, 0.2925094141462924, 0.25679767497423667, 0.21587022281644047, 0.17375799850320736, 0.13392056842844244, 0.09883258981843837, 0.06983987939141756, 0.04725602620808614, 0.03061690804427584, 0.018993975525273342],
            "type": "arbitrary",
        },
        "4612752936911847132_q": {
            "samples": [-0.00527991794672436, -0.007770770590465619, -0.010851612145363086, -0.014349470156969593, -0.017917396240899726, -0.02104137418551962, -0.02310047732513894, -0.02348111483824673, -0.021725640589441455, -0.017676379444879525, -0.011567612710796555, -0.0040269113777358055, 0.0040269113777358055, 0.011567612710796555, 0.017676379444879525, 0.021725640589441455, 0.02348111483824673, 0.02310047732513894, 0.02104137418551962, 0.017917396240899726, 0.014349470156969593, 0.010851612145363086, 0.007770770590465619, 0.00527991794672436],
            "type": "arbitrary",
        },
        "1246221591281584831_i": {
            "samples": [0.0188051455494348, 0.029788741848894427, 0.04533731988426526, 0.06629606419301091, 0.09314249565182005, 0.12572921811521887, 0.16306200574659052, 0.2031877710037322, 0.24325992741968647, 0.27981552082277616, 0.30924397603952297, 0.328366555557763, 0.335, 0.328366555557763, 0.30924397603952297, 0.27981552082277616, 0.24325992741968647, 0.2031877710037322, 0.16306200574659052, 0.12572921811521887, 0.09314249565182005, 0.06629606419301091, 0.04533731988426526, 0.029788741848894427, 0.0188051455494348] + [0.0] * 3,
            "type": "arbitrary",
        },
        "1246221591281584831_q": {
            "samples": [-0.005027057702387244, -0.0072996287167996195, -0.010099776615689818, -0.013291872931666225, -0.01659945319948615, -0.01960605333948804, -0.0217951546772194, -0.022632029235696516, -0.021676366690925035, -0.018700317494244452, -0.013778031368946824, -0.007315008623498064, 0.0, 0.007315008623498064, 0.013778031368946824, 0.018700317494244452, 0.021676366690925035, 0.022632029235696516, 0.0217951546772194, 0.01960605333948804, 0.01659945319948615, 0.013291872931666225, 0.010099776615689818, 0.0072996287167996195, 0.005027057702387244] + [0.0] * 3,
            "type": "arbitrary",
        },
        "8513744939115156904_i": {
            "samples": [0.018632220484242054, 0.029040149801382868, 0.04361861819906231, 0.06313697466875423, 0.08807130795463632, 0.11839243089800454, 0.1533741761934908, 0.19147821128357728, 0.23036966677978418, 0.2670976333762239, 0.2984376416154312, 0.3213482744907335] + [0.333454942326377] * 2 + [0.3213482744907335, 0.2984376416154312, 0.2670976333762239, 0.23036966677978418, 0.19147821128357728, 0.1533741761934908, 0.11839243089800454, 0.08807130795463632, 0.06313697466875423, 0.04361861819906231, 0.029040149801382868, 0.018632220484242054] + [0.0] * 2,
            "type": "arbitrary",
        },
        "8513744939115156904_q": {
            "samples": [-0.004796935447931777, -0.006878376422405012, -0.00943301334614989, -0.012353687742751557, -0.015418517509108243, -0.018288346760014867, -0.020533115313072996, -0.021690586626291513, -0.021351434295765172, -0.019254282111555856, -0.015366779319437161, -0.009927879054501326, -0.0034339693102843046, 0.0034339693102843046, 0.009927879054501326, 0.015366779319437161, 0.019254282111555856, 0.021351434295765172, 0.021690586626291513, 0.020533115313072996, 0.018288346760014867, 0.015418517509108243, 0.012353687742751557, 0.00943301334614989, 0.006878376422405012, 0.004796935447931777] + [0.0] * 2,
            "type": "arbitrary",
        },
        "6576965080401429237_i": {
            "samples": [0.018473279177696554, 0.028360426188547543, 0.04207150146690682, 0.0603072839254428, 0.08353298994039425, 0.11180282646469633, 0.14459525404627885, 0.18070151492460493, 0.2182107025961194, 0.25462251354338644, 0.28709395863081844, 0.3127935618695679, 0.32930479663082324, 0.335, 0.32930479663082324, 0.3127935618695679, 0.28709395863081844, 0.25462251354338644, 0.2182107025961194, 0.18070151492460493, 0.14459525404627885, 0.11180282646469633, 0.08353298994039425, 0.0603072839254428, 0.04207150146690682, 0.028360426188547543, 0.018473279177696554, 0.0],
            "type": "arbitrary",
        },
        "6576965080401429237_q": {
            "samples": [-0.004586651677842015, -0.0064998362117821605, -0.008838714599194502, -0.011518029421431174, -0.014358495953569176, -0.017082490350075318, -0.019331274720551735, -0.020707203806146227, -0.02083792478268882, -0.01945204235015596, -0.016449538664249988, -0.011948027548055363, -0.006289360238642818, 0.0, 0.006289360238642818, 0.011948027548055363, 0.016449538664249988, 0.01945204235015596, 0.02083792478268882, 0.020707203806146227, 0.019331274720551735, 0.017082490350075318, 0.014358495953569176, 0.011518029421431174, 0.008838714599194502, 0.0064998362117821605, 0.004586651677842015, 0.0],
            "type": "arbitrary",
        },
        "-2004664248783405147_i": {
            "samples": [0.01832669698051233, 0.027740672691822843, 0.04067252185339826, 0.057761244004407214, 0.07945537814161627, 0.1058671894438005, 0.13663148616398643, 0.17080143881500964, 0.20681573668745798, 0.24256434403693863, 0.2755634834035527, 0.3032268778589075, 0.32319530739253516] + [0.333667357954713] * 2 + [0.32319530739253516, 0.3032268778589075, 0.2755634834035527, 0.24256434403693863, 0.20681573668745798, 0.17080143881500964, 0.13663148616398643, 0.1058671894438005, 0.07945537814161627, 0.057761244004407214, 0.04067252185339826, 0.027740672691822843, 0.01832669698051233],
            "type": "arbitrary",
        },
        "-2004664248783405147_q": {
            "samples": [-0.004393775342916468, -0.00615810204010712, -0.00830651437971437, -0.01077074432675574, -0.013404998936650005, -0.015980861550296318, -0.018198346731598845, -0.01971627019512014, -0.020200687511610076, -0.019384712095756564, -0.0171281157847143, -0.013462557854328296, -0.008609465403744269, -0.00296280866807351, 0.00296280866807351, 0.008609465403744269, 0.013462557854328296, 0.0171281157847143, 0.019384712095756564, 0.020200687511610076, 0.01971627019512014, 0.018198346731598845, 0.015980861550296318, 0.013404998936650005, 0.01077074432675574, 0.00830651437971437, 0.00615810204010712, 0.004393775342916468],
            "type": "arbitrary",
        },
        "-1783170189584689899_i": {
            "samples": [0.01819109081729815, 0.027173437275819532, 0.03940218911512964, 0.055460791446032894, 0.07577775115719239, 0.10050491499298748, 0.1293965885542483, 0.16171424994882153, 0.1961840487550165, 0.2310303486134008, 0.26409751327342346, 0.29305526517912, 0.3156637294659085, 0.3300576294131244, 0.335, 0.3300576294131244, 0.3156637294659085, 0.29305526517912, 0.26409751327342346, 0.2310303486134008, 0.1961840487550165, 0.16171424994882153, 0.1293965885542483, 0.10050491499298748, 0.07577775115719239, 0.055460791446032894, 0.03940218911512964, 0.027173437275819532, 0.01819109081729815] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1783170189584689899_q": {
            "samples": [-0.004216253593123107, -0.005848276217544015, -0.007827832855203727, -0.010099937692276888, -0.01254531756405119, -0.014975100876872502, -0.017137708842802888, -0.018740720230959636, -0.019487444441528914, -0.019124010979662546, -0.017488970687549114, -0.014554950401719634, -0.010451885069504847, -0.005464239453129454, 0.0, 0.005464239453129454, 0.010451885069504847, 0.014554950401719634, 0.017488970687549114, 0.019124010979662546, 0.019487444441528914, 0.018740720230959636, 0.017137708842802888, 0.014975100876872502, 0.01254531756405119, 0.010099937692276888, 0.007827832855203727, 0.005848276217544015, 0.004216253593123107] + [0.0] * 3,
            "type": "arbitrary",
        },
        "8898685155510231288_i": {
            "samples": [0.018065276005258656, 0.026652435420606278, 0.03824418960324513, 0.05337406619763714, 0.07244883088801225, 0.09564642406883689, 0.12281243951968074, 0.15337417619349078, 0.1862937960640249, 0.22008011583250495, 0.2528712666663175, 0.2825884624365186, 0.3071465441702297, 0.3246931335495753] + [0.33383882265507364] * 2 + [0.3246931335495753, 0.3071465441702297, 0.2825884624365186, 0.2528712666663175, 0.22008011583250495, 0.1862937960640249, 0.15337417619349078, 0.12281243951968074, 0.09564642406883689, 0.07244883088801225, 0.05337406619763714, 0.03824418960324513, 0.026652435420606278, 0.018065276005258656] + [0.0] * 2,
            "type": "arbitrary",
        },
        "8898685155510231288_q": {
            "samples": [-0.004052341492286493, -0.005566267854069648, -0.007395523281457531, -0.009495581447086331, -0.011768310368930305, -0.014056777673390908, -0.01614933772416663, -0.017795366604663264, -0.018732907208737402, -0.018725651149012805, -0.017603759664609024, -0.015300862194138468, -0.011878977914268127, -0.007534558279540153, -0.002582261839838253, 0.002582261839838253, 0.007534558279540153, 0.011878977914268127, 0.015300862194138468, 0.017603759664609024, 0.018725651149012805, 0.018732907208737402, 0.017795366604663264, 0.01614933772416663, 0.014056777673390908, 0.011768310368930305, 0.009495581447086331, 0.007395523281457531, 0.005566267854069648, 0.004052341492286493] + [0.0] * 2,
            "type": "arbitrary",
        },
        "9120179214708946536_i": {
            "samples": [0.017948231995864244, 0.026172332787393688, 0.03718477943055919, 0.05147424700465795, 0.06942514753265586, 0.09123167258594302, 0.11680904663006401, 0.14571670365027273, 0.1771104611031902, 0.20973992377457756, 0.24200259030715096, 0.27205764841995045, 0.2979915037262761, 0.31801590444538874, 0.33067077659093647, 0.335, 0.33067077659093647, 0.31801590444538874, 0.2979915037262761, 0.27205764841995045, 0.24200259030715096, 0.20973992377457756, 0.1771104611031902, 0.14571670365027273, 0.11680904663006401, 0.09123167258594302, 0.06942514753265586, 0.05147424700465795, 0.03718477943055919, 0.026172332787393688, 0.017948231995864244, 0.0],
            "type": "arbitrary",
        },
        "9120179214708946536_q": {
            "samples": [-0.003900546757049179, -0.005308636933246881, -0.007003596495697234, -0.00894919153137007, -0.011064251808252995, -0.013217770037266836, -0.015231109608965033, -0.016889308941461907, -0.017962004814673038, -0.018232444949255903, -0.017530833845502043, -0.015766434317235428, -0.012952025511544165, -0.009214916210579795, -0.004790803631168852, 0.0, 0.004790803631168852, 0.009214916210579795, 0.012952025511544165, 0.015766434317235428, 0.017530833845502043, 0.018232444949255903, 0.017962004814673038, 0.016889308941461907, 0.015231109608965033, 0.013217770037266836, 0.011064251808252995, 0.00894919153137007, 0.007003596495697234, 0.005308636933246881, 0.003900546757049179, 0.0],
            "type": "arbitrary",
        },
        "636083557617192212_i": {
            "samples": [0.01783907496397817, 0.025728574217187748, 0.036212308922245785, 0.04973863021096136, 0.0666697048114013, 0.08720880813294145, 0.11132412168314676, 0.13868047195598887, 0.16859257812915757, 0.20001321942977004, 0.23156667303054507, 0.26163179403067927, 0.28847095328142003, 0.3103921774609387, 0.3259241584509132] + [0.3339792195124562] * 2 + [0.3259241584509132, 0.3103921774609387, 0.28847095328142003, 0.26163179403067927, 0.23156667303054507, 0.20001321942977004, 0.16859257812915757, 0.13868047195598887, 0.11132412168314676, 0.08720880813294145, 0.0666697048114013, 0.04973863021096136, 0.036212308922245785, 0.025728574217187748, 0.01783907496397817],
            "type": "arbitrary",
        },
        "636083557617192212_q": {
            "samples": [-0.003759585919706981, -0.005072472577547105, -0.00664700447050471, -0.008453563504519482, -0.010424671016782855, -0.012450466839272898, -0.014379668307385634, -0.016027663742449842, -0.017192368099731983, -0.01767697886755576, -0.017317082713861034, -0.016008071622664523, -0.013727963626673716, -0.0105508333154453, -0.00664727732010924, -0.0022705205425751357, 0.0022705205425751357, 0.00664727732010924, 0.0105508333154453, 0.013727963626673716, 0.016008071622664523, 0.017317082713861034, 0.01767697886755576, 0.017192368099731983, 0.016027663742449842, 0.014379668307385634, 0.012450466839272898, 0.010424671016782855, 0.008453563504519482, 0.00664700447050471, 0.005072472577547105, 0.003759585919706981],
            "type": "arbitrary",
        },
        "-1398229973189615515_i": {
            "samples": [0.017737035702013577, 0.025317248028875396, 0.035316846930112555, 0.048147896727025775, 0.06415089032991214, 0.08353298994039425, 0.1063024650771302, 0.13220826782069808, 0.1606955555244329, 0.19088820144577595, 0.22160740964254055, 0.2514313569243291, 0.27879473737331245, 0.3021201381461697, 0.31996667493664244, 0.3311767137308752, 0.335, 0.3311767137308752, 0.31996667493664244, 0.3021201381461697, 0.27879473737331245, 0.2514313569243291, 0.22160740964254055, 0.19088820144577595, 0.1606955555244329, 0.13220826782069808, 0.1063024650771302, 0.08353298994039425, 0.06415089032991214, 0.048147896727025775, 0.035316846930112555, 0.025317248028875396, 0.017737035702013577] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1398229973189615515_q": {
            "samples": [-0.0036283492640250535, -0.004855297190507367, -0.00632146912846382, -0.008002556246061231, -0.009842195715177958, -0.011747860325647504, -0.013590999554778615, -0.015212801104912074, -0.01643621883652695, -0.017083827936499336, -0.016999791323383227, -0.01607302077866449, -0.014257803518539449, -0.011588013486013593, -0.008181685972103517, -0.004234165751098574, 0.0, 0.004234165751098574, 0.008181685972103517, 0.011588013486013593, 0.014257803518539449, 0.01607302077866449, 0.016999791323383227, 0.017083827936499336, 0.01643621883652695, 0.015212801104912074, 0.013590999554778615, 0.011747860325647504, 0.009842195715177958, 0.008002556246061231, 0.00632146912846382, 0.004855297190507367, 0.0036283492640250535] + [0.0] * 3,
            "type": "arbitrary",
        },
        "5869293374643956558_i": {
            "samples": [0.017641441660759188, 0.02493497746593123, 0.034489881768632505, 0.046685525260893146, 0.061841584934738375, 0.080165368266721, 0.10169527866587191, 0.12624744794124373, 0.1533741761934908, 0.18234325229833218, 0.21214605910522533, 0.24153944207048658, 0.26912185479884504, 0.2934389054980157, 0.3131080541508245, 0.32694793794681176] + [0.33409562173676594] * 2 + [0.32694793794681176, 0.3131080541508245, 0.2934389054980157, 0.26912185479884504, 0.24153944207048658, 0.21214605910522533, 0.18234325229833218, 0.1533741761934908, 0.12624744794124373, 0.10169527866587191, 0.080165368266721, 0.061841584934738375, 0.046685525260893146, 0.034489881768632505, 0.02493497746593123, 0.017641441660759188] + [0.0] * 2,
            "type": "arbitrary",
        },
        "5869293374643956558_q": {
            "samples": [-0.0035058725608859147, -0.004654990366536816, -0.006023346069521006, -0.007590914962161943, -0.009310408425658041, -0.011103572705463149, -0.012860806324502084, -0.014445225348695447, -0.01570179406293817, -0.016471345173496375, -0.016608347898729888, -0.016000326931145115, -0.014586113524631565, -0.012369833294107244, -0.009427843314765016, -0.005906741567682423, -0.002011957937285106, 0.002011957937285106, 0.005906741567682423, 0.009427843314765016, 0.012369833294107244, 0.014586113524631565, 0.016000326931145115, 0.016608347898729888, 0.016471345173496375, 0.01570179406293817, 0.014445225348695447, 0.012860806324502084, 0.011103572705463149, 0.009310408425658041, 0.007590914962161943, 0.006023346069521006, 0.004654990366536816, 0.0035058725608859147] + [0.0] * 2,
            "type": "arbitrary",
        },
        "2502762029013694257_i": {
            "samples": [0.01755170225839157, 0.024578833208408275, 0.033724081423920756, 0.04533731988426526, 0.059718433160991055, 0.07707221016292604, 0.09745947536045964, 0.12075000918027004, 0.1465841871295902, 0.17435079054193522, 0.2031877710037322, 0.23201072360874123, 0.25957053867588853, 0.2845375485503847, 0.30560511573756266, 0.32160182283063504, 0.3315990141318758, 0.335, 0.3315990141318758, 0.32160182283063504, 0.30560511573756266, 0.2845375485503847, 0.25957053867588853, 0.23201072360874123, 0.2031877710037322, 0.17435079054193522, 0.1465841871295902, 0.12075000918027004, 0.09745947536045964, 0.07707221016292604, 0.059718433160991055, 0.04533731988426526, 0.033724081423920756, 0.024578833208408275, 0.01755170225839157, 0.0],
            "type": "arbitrary",
        },
        "2502762029013694257_q": {
            "samples": [-0.0033913141201100394, -0.004469728034533736, -0.005749515404980298, -0.007214126154064155, -0.008823717810342309, -0.01051184414027202, -0.012184749579839485, -0.01372419961483933, -0.014994413601972225, -0.015853084028045177, -0.01616573516835465, -0.015821919212458114, -0.014751128845054138, -0.012935982831744852, -0.01042033613124651, -0.00731052137053586, -0.00376888672135471, 0.0, 0.00376888672135471, 0.00731052137053586, 0.01042033613124651, 0.012935982831744852, 0.014751128845054138, 0.015821919212458114, 0.01616573516835465, 0.015853084028045177, 0.014994413601972225, 0.01372419961483933, 0.012184749579839485, 0.01051184414027202, 0.008823717810342309, 0.007214126154064155, 0.005749515404980298, 0.004469728034533736, 0.0033913141201100394, 0.0],
            "type": "arbitrary",
        },
        "8067053062647123421_i": {
            "samples": [0.01746729678532834, 0.024246262366054892, 0.03301309997313815, 0.044091027487984664, 0.05776124400440721, 0.07422415503583513, 0.09355702264341355, 0.11567244840843036, 0.14028326653715065, 0.16687997174656105, 0.19472646098759386, 0.2228784763460159, 0.2502267269177905, 0.2755634834035527, 0.29766792682444976, 0.3154022776673242, 0.32780835134453135] + [0.33419319917662343] * 2 + [0.32780835134453135, 0.3154022776673242, 0.29766792682444976, 0.2755634834035527, 0.2502267269177905, 0.2228784763460159, 0.19472646098759386, 0.16687997174656105, 0.14028326653715065, 0.11567244840843036, 0.09355702264341355, 0.07422415503583513, 0.05776124400440721, 0.044091027487984664, 0.03301309997313815, 0.024246262366054892, 0.01746729678532834],
            "type": "arbitrary",
        },
        "8067053062647123421_q": {
            "samples": [-0.003283936032219589, -0.00429793343870024, -0.005497293772884255, -0.00686829851841081, -0.008377245587476687, -0.009967499353582524, -0.011558598373931233, -0.013048186880842496, -0.014317276627370614, -0.01523891631505295, -0.0156897916028725, -0.015563684831084793, -0.014785204150092587, -0.013321867832555567, -0.011192601151152188, -0.008471021319810805, -0.0052825329358854685, -0.0017951409457777952, 0.0017951409457777952, 0.0052825329358854685, 0.008471021319810805, 0.011192601151152188, 0.013321867832555567, 0.014785204150092587, 0.015563684831084793, 0.0156897916028725, 0.01523891631505295, 0.014317276627370614, 0.013048186880842496, 0.011558598373931233, 0.009967499353582524, 0.008377245587476687, 0.00686829851841081, 0.005497293772884255, 0.00429793343870024, 0.003283936032219589],
            "type": "arbitrary",
        },
        "-4525155426148970305_i": {
            "samples": [0.01738776438591863, 0.023935030466781828, 0.03235142029760381, 0.04293602631125434, 0.0559524972029222, 0.07159558289262412, 0.089954338354723, 0.11097550425506562, 0.13443156974280943, 0.15989855606019254, 0.18674842306657943, 0.21416005702807095, 0.24115103691015088, 0.26662994478875834, 0.2894661874564757, 0.3085715547266273, 0.32298552963552113, 0.33195512013119244, 0.335, 0.33195512013119244, 0.32298552963552113, 0.3085715547266273, 0.2894661874564757, 0.26662994478875834, 0.24115103691015088, 0.21416005702807095, 0.18674842306657943, 0.15989855606019254, 0.13443156974280943, 0.11097550425506562, 0.089954338354723, 0.07159558289262412, 0.0559524972029222, 0.04293602631125434, 0.03235142029760381, 0.023935030466781828, 0.01738776438591863] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4525155426148970305_q": {
            "samples": [-0.0031830887376103037, -0.004138237389163513, -0.005264363008859811, -0.0065500648787533795, -0.00796672826390364, -0.009465903566281835, -0.010978319196610463, -0.012415159588189003, -0.013672053971410589, -0.014635903778623081, -0.0151942554810711, -0.015246459627503829, -0.014715427327992933, -0.01355849300324456, -0.011775797442148302, -0.009414768327861877, -0.006569700259559274, -0.003376073289334262, 0.0, 0.003376073289334262, 0.006569700259559274, 0.009414768327861877, 0.011775797442148302, 0.01355849300324456, 0.014715427327992933, 0.015246459627503829, 0.0151942554810711, 0.014635903778623081, 0.013672053971410589, 0.012415159588189003, 0.010978319196610463, 0.009465903566281835, 0.00796672826390364, 0.0065500648787533795, 0.005264363008859811, 0.004138237389163513, 0.0031830887376103037] + [0.0] * 3,
            "type": "arbitrary",
        },
        "6254233591039030942_i": {
            "samples": [0.017312695713105425, 0.02364317376729328, 0.031734225501660565, 0.041863070983741736, 0.05427693508076088, 0.0691640791109188, 0.0866217459432558, 0.10662383979953585, 0.128991993677392, 0.1533741761934908, 0.17923498429372278, 0.2058611395137102, 0.2323844232662663, 0.2578224355152389, 0.28113534565106796, 0.3012945290206187, 0.3173570073167443, 0.32853828794888107] + [0.3342758012248797] * 2 + [0.32853828794888107, 0.3173570073167443, 0.3012945290206187, 0.28113534565106796, 0.2578224355152389, 0.2323844232662663, 0.2058611395137102, 0.17923498429372278, 0.1533741761934908, 0.128991993677392, 0.10662383979953585, 0.0866217459432558, 0.0691640791109188, 0.05427693508076088, 0.041863070983741736, 0.031734225501660565, 0.02364317376729328, 0.017312695713105425] + [0.0] * 2,
            "type": "arbitrary",
        },
        "6254233591039030942_q": {
            "samples": [-0.0030881982570208134, -0.003989445825408253, -0.005048711993667457, -0.006256501188374574, -0.007588432357986604, -0.009002914309719287, -0.010440124921594051, -0.011822815384348026, -0.013059327205873831, -0.01404897363526047, -0.014689616470546688, -0.014886903903549194, -0.01456428335405858, -0.013672632642363035, -0.012198227070398013, -0.010167824445654028, -0.007649919232291832, -0.004751667005132686, -0.0016115496565215104, 0.0016115496565215104, 0.004751667005132686, 0.007649919232291832, 0.010167824445654028, 0.012198227070398013, 0.013672632642363035, 0.01456428335405858, 0.014886903903549194, 0.014689616470546688, 0.01404897363526047, 0.013059327205873831, 0.011822815384348026, 0.010440124921594051, 0.009002914309719287, 0.007588432357986604, 0.006256501188374574, 0.005048711993667457, 0.003989445825408253, 0.0030881982570208134] + [0.0] * 2,
            "type": "arbitrary",
        },
        "3059048095191327930_i": {
            "samples": [0.01724172593940673, 0.023368959819382334, 0.03115729318755132, 0.04086408275045972, 0.05272122394039205, 0.06690998119944296, 0.08353298994039425, 0.10258570331944422, 0.12393025658662747, 0.14727517665833112, 0.17216443859661812, 0.1979789625072213, 0.2239527152239888, 0.24920417581611157, 0.2727821784571032, 0.2937232779502066, 0.3111160627814493, 0.32416654841211073, 0.3322581590912206, 0.335, 0.3322581590912206, 0.32416654841211073, 0.3111160627814493, 0.2937232779502066, 0.2727821784571032, 0.24920417581611157, 0.2239527152239888, 0.1979789625072213, 0.17216443859661812, 0.14727517665833112, 0.12393025658662747, 0.10258570331944422, 0.08353298994039425, 0.06690998119944296, 0.05272122394039205, 0.04086408275045972, 0.03115729318755132, 0.023368959819382334, 0.01724172593940673, 0.0],
            "type": "arbitrary",
        },
        "3059048095191327930_q": {
            "samples": [-0.002998755564833742, -0.003850513188890439, -0.004848588987017177, -0.005985059413995271, -0.007239081588209785, -0.008574833023886586, -0.009940497198624812, -0.011268725884709691, -0.012478913156011833, -0.013481439921969818, -0.014183802929139488, -0.01449825584686018, -0.01435030397458634, -0.013687158423295076, -0.012485120147521669, -0.010754868037418857, -0.00854378708819013, -0.005934784050225717, -0.003041461916399061, 0.0, 0.003041461916399061, 0.005934784050225717, 0.00854378708819013, 0.010754868037418857, 0.012485120147521669, 0.013687158423295076, 0.01435030397458634, 0.01449825584686018, 0.014183802929139488, 0.013481439921969818, 0.012478913156011833, 0.011268725884709691, 0.009940497198624812, 0.008574833023886586, 0.007239081588209785, 0.005985059413995271, 0.004848588987017177, 0.003850513188890439, 0.002998755564833742, 0.0],
            "type": "arbitrary",
        },
        "8673487338240913053_i": {
            "samples": [0.017110811988323652, 0.02286749551829838, 0.030109789199680825, 0.03906051422721497, 0.04992399452749992, 0.06286686827952646, 0.07799656113110516, 0.09533891666490042, 0.11481697469001541, 0.13623324934850542, 0.15925800097627804, 0.1834258473583767, 0.20814258168445188, 0.2327032608419634, 0.2563215556148666, 0.2781691223703619, 0.29742251351906746, 0.31331406251496546, 0.32518242480366655, 0.33251816223085684, 0.335, 0.33251816223085684, 0.32518242480366655, 0.31331406251496546, 0.29742251351906746, 0.2781691223703619, 0.2563215556148666, 0.2327032608419634, 0.20814258168445188, 0.1834258473583767, 0.15925800097627804, 0.13623324934850542, 0.11481697469001541, 0.09533891666490042, 0.07799656113110516, 0.06286686827952646, 0.04992399452749992, 0.03906051422721497, 0.030109789199680825, 0.02286749551829838, 0.017110811988323652] + [0.0] * 3,
            "type": "arbitrary",
        },
        "8673487338240913053_q": {
            "samples": [-0.0028344502842906484, -0.003598656817469114, -0.00448898804765578, -0.0054999039713432, -0.006616031107253624, -0.0078105445604640805, -0.009044232530626327, -0.010265539867948823, -0.01141183738469877, -0.012412064660348556, -0.013190749990439121, -0.013673234823437668, -0.013791742910414235, -0.01349176406734157, -0.012738098694757933, -0.0115198587378786, -0.009853761803634328, -0.007785192784893719, -0.005386731015804793, -0.0027541247022941353, 0.0, 0.0027541247022941353, 0.005386731015804793, 0.007785192784893719, 0.009853761803634328, 0.0115198587378786, 0.012738098694757933, 0.01349176406734157, 0.013791742910414235, 0.013673234823437668, 0.013190749990439121, 0.012412064660348556, 0.01141183738469877, 0.010265539867948823, 0.009044232530626327, 0.0078105445604640805, 0.006616031107253624, 0.0054999039713432, 0.00448898804765578, 0.003598656817469114, 0.0028344502842906484] + [0.0] * 3,
            "type": "arbitrary",
        },
        "7525665521064044280_i": {
            "samples": [0.017050312187589976, 0.022637667574557468, 0.029633029541901945, 0.03824418960324513, 0.04866311486503552, 0.06104911583203625, 0.0755098983609188, 0.092081720602586, 0.11071029262162224, 0.13123437414030117, 0.15337417619349078, 0.17672659685492575, 0.2007689828971011, 0.2248725040764974, 0.2483253899089188, 0.27036528603014404, 0.29021894876787196, 0.3071465441702297, 0.3204870862612083, 0.3297011553355644] + [0.3344070588118783] * 2 + [0.3297011553355644, 0.3204870862612083, 0.3071465441702297, 0.29021894876787196, 0.27036528603014404, 0.2483253899089188, 0.2248725040764974, 0.2007689828971011, 0.17672659685492575, 0.15337417619349078, 0.13123437414030117, 0.11071029262162224, 0.092081720602586, 0.0755098983609188, 0.06104911583203625, 0.04866311486503552, 0.03824418960324513, 0.029633029541901945, 0.022637667574557468, 0.017050312187589976] + [0.0] * 2,
            "type": "arbitrary",
        },
        "7525665521064044280_q": {
            "samples": [-0.002758821220629363, -0.003484204610795216, -0.00432698255208323, -0.005282516629612523, -0.006337547245196544, -0.0074687588673105825, -0.008641900257992729, -0.009811706664197947, -0.010922835000000769, -0.011911948479488387, -0.012710976146188043, -0.013251434107921064, -0.013469544398573889, -0.013311744734300511, -0.01274007088183993, -0.011736834482196506, -0.010308029197933567, -0.008484984224477231, -0.006323942390481052, -0.003903454214160371, -0.0013197230500407208, 0.0013197230500407208, 0.003903454214160371, 0.006323942390481052, 0.008484984224477231, 0.010308029197933567, 0.011736834482196506, 0.01274007088183993, 0.013311744734300511, 0.013469544398573889, 0.013251434107921064, 0.012710976146188043, 0.011911948479488387, 0.010922835000000769, 0.009811706664197947, 0.008641900257992729, 0.0074687588673105825, 0.006337547245196544, 0.005282516629612523, 0.00432698255208323, 0.003484204610795216, 0.002758821220629363] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7113906646402883685_i": {
            "samples": [0.016992792206179008, 0.022420284757886003, 0.029184044798159166, 0.037478122290260325, 0.047482999574864584, 0.05935078261347404, 0.07318848130781351, 0.08904037952415504, 0.1068708469174143, 0.1265492224897247, 0.14783854953997605, 0.17038991502633022, 0.19374391051757198, 0.21734027777785636, 0.24053615026653413, 0.26263250474062044, 0.2829075755107129, 0.3006551585403228, 0.3152250513718628, 0.3260624370407583, 0.3327429003609743, 0.335, 0.3327429003609743, 0.3260624370407583, 0.3152250513718628, 0.3006551585403228, 0.2829075755107129, 0.26263250474062044, 0.24053615026653413, 0.21734027777785636, 0.19374391051757198, 0.17038991502633022, 0.14783854953997605, 0.1265492224897247, 0.1068708469174143, 0.08904037952415504, 0.07318848130781351, 0.05935078261347404, 0.047482999574864584, 0.037478122290260325, 0.029184044798159166, 0.022420284757886003, 0.016992792206179008, 0.0],
            "type": "arbitrary",
        },
        "-7113906646402883685_q": {
            "samples": [-0.002687095320975051, -0.003376526411168444, -0.004175400274989588, -0.005079832125620023, -0.006078355529190671, -0.007150649054889436, -0.008266716150055314, -0.009386724453292961, -0.010461684885508958, -0.011435094513661564, -0.012245581395403162, -0.012830480399692258, -0.013130147411976666, -0.01309270057989777, -0.012678778862321187, -0.011865847355611029, -0.010651569671696072, -0.009055817929416484, -0.007121000399278935, -0.004910546151608634, -0.002505577434297394, 0.0, 0.002505577434297394, 0.004910546151608634, 0.007121000399278935, 0.009055817929416484, 0.010651569671696072, 0.011865847355611029, 0.012678778862321187, 0.01309270057989777, 0.013130147411976666, 0.012830480399692258, 0.012245581395403162, 0.011435094513661564, 0.010461684885508958, 0.009386724453292961, 0.008266716150055314, 0.007150649054889436, 0.006078355529190671, 0.005079832125620023, 0.004175400274989588, 0.003376526411168444, 0.002687095320975051, 0.0],
            "type": "arbitrary",
        },
        "8730492257245146766_i": {
            "samples": [0.016938037517348264, 0.022214373169088395, 0.028760530609220063, 0.036757975477438865, 0.046376517299302616, 0.05776124400440721, 0.07101773269130594, 0.086196359981087, 0.1032768321007622, 0.12215429685696323, 0.14262854334499814, 0.1643978009317781, 0.18705848792601548, 0.21011192099696277, 0.23297848983482242, 0.2550191634150701, 0.2755634834035527, 0.29394249340042455, 0.30952443535967816, 0.32175059943199913, 0.33016850844762313] + [0.33445969496577194] * 2 + [0.33016850844762313, 0.32175059943199913, 0.30952443535967816, 0.29394249340042455, 0.2755634834035527, 0.2550191634150701, 0.23297848983482242, 0.21011192099696277, 0.18705848792601548, 0.1643978009317781, 0.14262854334499814, 0.12215429685696323, 0.1032768321007622, 0.086196359981087, 0.07101773269130594, 0.05776124400440721, 0.046376517299302616, 0.036757975477438865, 0.028760530609220063, 0.022214373169088395, 0.016938037517348264],
            "type": "arbitrary",
        },
        "8730492257245146766_q": {
            "samples": [-0.002618979746070516, -0.003275054365158036, -0.004033314567480382, -0.0048905071874192595, -0.005836691911246695, -0.006854110026117289, -0.007916424797278918, -0.00898850610793582, -0.010026913442044755, -0.010981188601298968, -0.011796003061073113, -0.012414118663537713, -0.012780022373866582, -0.01284399738712753, -0.012566307380497993, -0.011921111850174769, -0.010899710044818193, -0.009512736717141283, -0.007791006627503704, -0.005784821501745438, -0.003561701311957981, -0.0012026641991162031, 0.0012026641991162031, 0.003561701311957981, 0.005784821501745438, 0.007791006627503704, 0.009512736717141283, 0.010899710044818193, 0.011921111850174769, 0.012566307380497993, 0.01284399738712753, 0.012780022373866582, 0.012414118663537713, 0.011796003061073113, 0.010981188601298968, 0.010026913442044755, 0.00898850610793582, 0.007916424797278918, 0.006854110026117289, 0.005836691911246695, 0.0048905071874192595, 0.004033314567480382, 0.003275054365158036, 0.002618979746070516],
            "type": "arbitrary",
        },
        "-2342287230438707354_i": {
            "samples": [0.016885853676522473, 0.02201905708653771, 0.028360426188547543, 0.03607988363866076, 0.04533731988426526, 0.05627103431377377, 0.06898462255545658, 0.08353298994039424, 0.09990842222077623, 0.1180278549234915, 0.13772261731990781, 0.15873195334244697, 0.18070151492460493, 0.2031877710037322, 0.22566888254048348, 0.24756208425390347, 0.26824702997713074, 0.28709395863081844, 0.30349498902168576, 0.31689642208376645, 0.3268296783217234, 0.33293846806435784, 0.335, 0.33293846806435784, 0.3268296783217234, 0.31689642208376645, 0.30349498902168576, 0.28709395863081844, 0.26824702997713074, 0.24756208425390347, 0.22566888254048348, 0.2031877710037322, 0.18070151492460493, 0.15873195334244697, 0.13772261731990781, 0.1180278549234915, 0.09990842222077623, 0.08353298994039424, 0.06898462255545658, 0.05627103431377377, 0.04533731988426526, 0.03607988363866076, 0.028360426188547543, 0.02201905708653771, 0.016885853676522473] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2342287230438707354_q": {
            "samples": [-0.0025542100963550523, -0.0031792810904459437, -0.003899901727069296, -0.004713349496246575, -0.005610987008716565, -0.0065772558239603745, -0.007588976184113599, -0.008615097572141503, -0.009617031776745309, -0.010549667728152313, -0.011363115693077382, -0.01200516022489109, -0.012424322283687736, -0.01257334957538695, -0.012412880665676662, -0.011914973623174648, -0.011066163623924706, -0.009869723198549995, -0.008346846581032755, -0.006536563813799242, -0.004494303500485123, -0.0022891533751638817, 0.0, 0.0022891533751638817, 0.004494303500485123, 0.006536563813799242, 0.008346846581032755, 0.009869723198549995, 0.011066163623924706, 0.011914973623174648, 0.012412880665676662, 0.01257334957538695, 0.012424322283687736, 0.01200516022489109, 0.011363115693077382, 0.010549667728152313, 0.009617031776745309, 0.008615097572141503, 0.007588976184113599, 0.0065772558239603745, 0.005610987008716565, 0.004713349496246575, 0.003899901727069296, 0.0031792810904459437, 0.0025542100963550523] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4694652899201001574_i": {
            "samples": [0.016836064028001252, 0.0218335469866987, 0.027981883429922777, 0.03544039163899544, 0.04435974116832225, 0.054871700064787254, 0.06707748178117125, 0.08103525545783677, 0.09674759604935303, 0.11414983320544946, 0.13310038183860678, 0.1533741761934908, 0.1746602615808129, 0.1965644117294024, 0.21861733569533248, 0.2402886320459908, 0.26100617026181516, 0.28018007366892095, 0.297229997275575, 0.31161399299860787, 0.3228569850153341, 0.33057677898769605] + [0.3345056227101372] * 2 + [0.33057677898769605, 0.3228569850153341, 0.31161399299860787, 0.297229997275575, 0.28018007366892095, 0.26100617026181516, 0.2402886320459908, 0.21861733569533248, 0.1965644117294024, 0.1746602615808129, 0.1533741761934908, 0.13310038183860678, 0.11414983320544946, 0.09674759604935303, 0.08103525545783677, 0.06707748178117125, 0.054871700064787254, 0.04435974116832225, 0.03544039163899544, 0.027981883429922777, 0.0218335469866987, 0.016836064028001252] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4694652899201001574_q": {
            "samples": [-0.0024925470553099926, -0.003088751960343029, -0.0037744274594776624, -0.004547297863026227, -0.0053998414824302215, -0.006318394577273482, -0.007282508047586256, -0.008264678857092443, -0.00923056880484113, -0.010139798594748442, -0.01094736487699141, -0.011605673872606475, -0.012067121466997198, -0.012287082527893005, -0.01222710951146848, -0.011858090688230861, -0.011163089583941306, -0.010139585779937918, -0.008800866440361063, -0.00717637748143488, -0.0053109287429903085, -0.003262750627261523, -0.0011005092711615099, 0.0011005092711615099, 0.003262750627261523, 0.0053109287429903085, 0.00717637748143488, 0.008800866440361063, 0.010139585779937918, 0.011163089583941306, 0.011858090688230861, 0.01222710951146848, 0.012287082527893005, 0.012067121466997198, 0.011605673872606475, 0.01094736487699141, 0.010139798594748442, 0.00923056880484113, 0.008264678857092443, 0.007282508047586256, 0.006318394577273482, 0.0053998414824302215, 0.004547297863026227, 0.0037744274594776624, 0.003088751960343029, 0.0024925470553099926] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8061184244831263875_i": {
            "samples": [0.016788507718561142, 0.021657129266262405, 0.027623240543868728, 0.03483640286609818, 0.04343871063074394, 0.053555674066433696, 0.0652858399979102, 0.07868961949809622, 0.09377797202299386, 0.11050175375775492, 0.12874265084905476, 0.14830666401208403, 0.16892107145526122, 0.1902356608233562, 0.21182878623136714, 0.233218483269582, 0.25387848495435106, 0.2732585577368615, 0.2908081597123593, 0.30600205772722716, 0.3183662692571892, 0.3275025546493579, 0.33310969919524747, 0.335, 0.33310969919524747, 0.3275025546493579, 0.3183662692571892, 0.30600205772722716, 0.2908081597123593, 0.2732585577368615, 0.25387848495435106, 0.233218483269582, 0.21182878623136714, 0.1902356608233562, 0.16892107145526122, 0.14830666401208403, 0.12874265084905476, 0.11050175375775492, 0.09377797202299386, 0.07868961949809622, 0.0652858399979102, 0.053555674066433696, 0.04343871063074394, 0.03483640286609818, 0.027623240543868728, 0.021657129266262405, 0.016788507718561142, 0.0],
            "type": "arbitrary",
        },
        "-8061184244831263875_q": {
            "samples": [-0.0024337734955974955, -0.00300305852544869, -0.0036562353774301087, -0.0043914053485284875, -0.005202004856349165, -0.0060760063832949445, -0.006995328990888799, -0.00793556136701815, -0.00886609381353562, -0.009750736780635745, -0.010548872080794094, -0.011217139956758609, -0.011711613702927216, -0.011990358212809731, -0.012016215646084892, -0.0117596170734657, -0.011201190012256891, -0.010333923653850871, -0.009164669734022518, -0.007714798098582083, -0.006019889638064424, -0.004128429894647781, -0.0020995562031984375, 0.0, 0.0020995562031984375, 0.004128429894647781, 0.006019889638064424, 0.007714798098582083, 0.009164669734022518, 0.010333923653850871, 0.011201190012256891, 0.0117596170734657, 0.012016215646084892, 0.011990358212809731, 0.011711613702927216, 0.011217139956758609, 0.010548872080794094, 0.009750736780635745, 0.00886609381353562, 0.00793556136701815, 0.006995328990888799, 0.0060760063832949445, 0.005202004856349165, 0.0043914053485284875, 0.0036562353774301087, 0.00300305852544869, 0.0024337734955974955, 0.0],
            "type": "arbitrary",
        },
        "538556917825762772_i": {
            "samples": [0.01674303797113176, 0.021489157391914208, 0.027282999474786657, 0.034265134889522625, 0.04256967948039585, 0.0523161670657943, 0.06360028458986718, 0.07648386094795837, 0.09098465461440518, 0.10706662222847899, 0.1246314522890466, 0.14351219703580465, 0.16346981600204136, 0.18419334621823985, 0.2053042335338458, 0.22636510283331646, 0.2468929274591887, 0.26637620435532533, 0.2842953829190331, 0.30014546803251035, 0.3134594571275351, 0.3238311091036365, 0.3309355027251901] + [0.33454593517216796] * 2 + [0.3309355027251901, 0.3238311091036365, 0.3134594571275351, 0.30014546803251035, 0.2842953829190331, 0.26637620435532533, 0.2468929274591887, 0.22636510283331646, 0.2053042335338458, 0.18419334621823985, 0.16346981600204136, 0.14351219703580465, 0.1246314522890466, 0.10706662222847899, 0.09098465461440518, 0.07648386094795837, 0.06360028458986718, 0.0523161670657943, 0.04256967948039585, 0.034265134889522625, 0.027282999474786657, 0.021489157391914208, 0.01674303797113176],
            "type": "arbitrary",
        },
        "538556917825762772_q": {
            "samples": [-0.0023776919754482707, -0.0029218328836265687, -0.003544737193892857, -0.004244824844356078, -0.005016357263577793, -0.0058487238172589264, -0.006725902622192118, -0.007626182869797987, -0.008522231290042655, -0.009381571039611703, -0.010167516640814205, -0.010840574384490077, -0.011360275974195852, -0.01168736761140509, -0.01178623179348669, -0.011627380072785437, -0.011189827208030693, -0.010463145160845308, -0.009449002496770805, -0.008162022199147351, -0.006629837580886867, -0.0048922883194019535, -0.00299977089713092, -0.0010108325759539086, 0.0010108325759539086, 0.00299977089713092, 0.0048922883194019535, 0.006629837580886867, 0.008162022199147351, 0.009449002496770805, 0.010463145160845308, 0.011189827208030693, 0.011627380072785437, 0.01178623179348669, 0.01168736761140509, 0.011360275974195852, 0.010840574384490077, 0.010167516640814205, 0.009381571039611703, 0.008522231290042655, 0.007626182869797987, 0.006725902622192118, 0.0058487238172589264, 0.005016357263577793, 0.004244824844356078, 0.003544737193892857, 0.0029218328836265687, 0.0023776919754482707],
            "type": "arbitrary",
        },
        "-8116884589048550841_i": {
            "samples": [0.01669952057970701, 0.02132904425280487, 0.026959806487407346, 0.03372408142392078, 0.04174855719550066, 0.05114707430080548, 0.06201233792131368, 0.07440693184201605, 0.08835409281105362, 0.10382882292686263, 0.12075000918027008, 0.1389742687674673, 0.15829223316684907, 0.17842791389577145, 0.19904165451593214, 0.21973696993608066, 0.240071316079867, 0.25957053867588853, 0.27774644364699735, 0.2941166417686991, 0.308225576534715, 0.3196654739046843, 0.32809587760191244, 0.3332604671029744, 0.335, 0.3332604671029744, 0.32809587760191244, 0.3196654739046843, 0.308225576534715, 0.2941166417686991, 0.27774644364699735, 0.25957053867588853, 0.240071316079867, 0.21973696993608066, 0.19904165451593214, 0.17842791389577145, 0.15829223316684907, 0.1389742687674673, 0.12075000918027008, 0.10382882292686263, 0.08835409281105362, 0.07440693184201605, 0.06201233792131368, 0.05114707430080548, 0.04174855719550066, 0.03372408142392078, 0.026959806487407346, 0.02132904425280487, 0.01669952057970701] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8116884589048550841_q": {
            "samples": [-0.002324122565430923, -0.0028447428441621117, -0.0034394043304898226, -0.0041067967178430725, -0.004841893683370888, -0.0056353147745744885, -0.00647283285215342, -0.007335101039734588, -0.00819767010157488, -0.009031356212992508, -0.009802999724885235, -0.010476628212908038, -0.011015003373287908, -0.011381493780751503, -0.01154217767592992, -0.011468045920472054, -0.011137149324153587, -0.010536520603610095, -0.009663702231257414, -0.008527728894231099, -0.007149446938193235, -0.005561100824309425, -0.003805174271919355, -0.0019325359473225414, 0.0, 0.0019325359473225414, 0.003805174271919355, 0.005561100824309425, 0.007149446938193235, 0.008527728894231099, 0.009663702231257414, 0.010536520603610095, 0.011137149324153587, 0.011468045920472054, 0.01154217767592992, 0.011381493780751503, 0.011015003373287908, 0.010476628212908038, 0.009802999724885235, 0.009031356212992508, 0.00819767010157488, 0.007335101039734588, 0.00647283285215342, 0.0056353147745744885, 0.004841893683370888, 0.0041067967178430725, 0.0034394043304898226, 0.0028447428441621117, 0.002324122565430923] + [0.0] * 3,
            "type": "arbitrary",
        },
        "2736316605828929635_i": {
            "samples": [0.016657832593137117, 0.021176255530221767, 0.026652435420606278, 0.03321097959110038, 0.04097165687121171, 0.050042894708890034, 0.06051435029232949, 0.07244883088801225, 0.08587395072404966, 0.10077401470968732, 0.11708270106691843, 0.13467716333670937, 0.15337417619349078, 0.17292890077174128, 0.19303673968005297, 0.213338590814534, 0.23342959979117167, 0.2528712666663175, 0.2712065023037421, 0.28797697580685166, 0.3027418710875207, 0.31509700122705464, 0.3246931335495753, 0.3312523699447631] + [0.33458151160973465] * 2 + [0.3312523699447631, 0.3246931335495753, 0.31509700122705464, 0.3027418710875207, 0.28797697580685166, 0.2712065023037421, 0.2528712666663175, 0.23342959979117167, 0.213338590814534, 0.19303673968005297, 0.17292890077174128, 0.15337417619349078, 0.13467716333670937, 0.11708270106691843, 0.10077401470968732, 0.08587395072404966, 0.07244883088801225, 0.06051435029232949, 0.050042894708890034, 0.04097165687121171, 0.03321097959110038, 0.026652435420606278, 0.021176255530221767, 0.016657832593137117] + [0.0] * 2,
            "type": "arbitrary",
        },
        "2736316605828929635_q": {
            "samples": [-0.002272900955979572, -0.002771487759704608, -0.0033397607124417894, -0.003976638193525707, -0.004677710301425255, -0.0054346673731065056, -0.006234850394107981, -0.007060986221358182, -0.007891168581951704, -0.008699137442067573, -0.009454894100303908, -0.010125667509408028, -0.010677219962797958, -0.011075449340341142, -0.011288213287005251, -0.011287271228325386, -0.01105021644689837, -0.010562255798765414, -0.009817691655785603, -0.008820970910084028, -0.007587189621609586, -0.006141977880898166, -0.004520734967724092, -0.002767235923186758, -0.0009316823688586992, 0.0009316823688586992, 0.002767235923186758, 0.004520734967724092, 0.006141977880898166, 0.007587189621609586, 0.008820970910084028, 0.009817691655785603, 0.010562255798765414, 0.01105021644689837, 0.011287271228325386, 0.011288213287005251, 0.011075449340341142, 0.010677219962797958, 0.010125667509408028, 0.009454894100303908, 0.008699137442067573, 0.007891168581951704, 0.007060986221358182, 0.006234850394107981, 0.0054346673731065056, 0.004677710301425255, 0.003976638193525707, 0.0033397607124417894, 0.002771487759704608, 0.002272900955979572] + [0.0] * 2,
            "type": "arbitrary",
        },
        "2957810665027644883_i": {
            "samples": [0.01661786116073915, 0.02103030393080685, 0.02635977319469312, 0.0327237816523808, 0.04023564801392218, 0.04899866090898294, 0.059099406478136725, 0.07060049149916642, 0.08353298994039425, 0.09788903016619835, 0.11361501285083114, 0.13060599590129102, 0.1487017930670628, 0.16768530014691396, 0.18728348269003153, 0.20717133188949574, 0.22697892583119728, 0.24630153117856524, 0.2647124600369022, 0.2817781759247988, 0.2970749411774412, 0.3102061353773037, 0.32081926804380095, 0.3286216720808554, 0.33339390470428626, 0.335, 0.33339390470428626, 0.3286216720808554, 0.32081926804380095, 0.3102061353773037, 0.2970749411774412, 0.2817781759247988, 0.2647124600369022, 0.24630153117856524, 0.22697892583119728, 0.20717133188949574, 0.18728348269003153, 0.16768530014691396, 0.1487017930670628, 0.13060599590129102, 0.11361501285083114, 0.09788903016619835, 0.08353298994039425, 0.07060049149916642, 0.059099406478136725, 0.04899866090898294, 0.04023564801392218, 0.0327237816523808, 0.02635977319469312, 0.02103030393080685, 0.01661786116073915, 0.0],
            "type": "arbitrary",
        },
        "2957810665027644883_q": {
            "samples": [-0.002223876804374156, -0.002701794921882508, -0.0032453765620306533, -0.0038537342003590104, -0.004522992682858684, -0.005245776668218839, -0.006010800453817439, -0.006802613862920717, -0.007601556681301327, -0.008383967741065718, -0.009122682730238793, -0.009787837286222876, -0.010347969686918985, -0.010771391937603217, -0.011027771332663342, -0.011089839181201986, -0.010935122083876614, -0.010547576620537577, -0.009919002832133234, -0.009050117003964395, -0.007951180533463342, -0.006642108486692404, -0.005152017013726233, -0.0035182102287958142, -0.001784650778388407, 0.0, 0.001784650778388407, 0.0035182102287958142, 0.005152017013726233, 0.006642108486692404, 0.007951180533463342, 0.009050117003964395, 0.009919002832133234, 0.010547576620537577, 0.010935122083876614, 0.011089839181201986, 0.011027771332663342, 0.010771391937603217, 0.010347969686918985, 0.009787837286222876, 0.009122682730238793, 0.008383967741065718, 0.007601556681301327, 0.006802613862920717, 0.006010800453817439, 0.005245776668218839, 0.004522992682858684, 0.0038537342003590104, 0.0032453765620306533, 0.002701794921882508, 0.002223876804374156, 0.0],
            "type": "arbitrary",
        },
        "-408720680602617418_i": {
            "samples": [0.01657950251700238, 0.020890744155519354, 0.02608080722947321, 0.03226063052550099, 0.039537515651160544, 0.04800987837539687, 0.05776124400440721, 0.06885368268695924, 0.08132096298750445, 0.09516177964375815, 0.11033347612997459, 0.12674672614287222, 0.14426165259967583, 0.16268584184053636, 0.18177465052534833, 0.20123410250188192, 0.2207265357907252, 0.23987899288322825, 0.2582941616625299, 0.2755634834035527, 0.2912818644132092, 0.30506327535078004, 0.31655641235105936, 0.32545953912806963, 0.33153363728856644] + [0.3346130657179247] * 2 + [0.33153363728856644, 0.32545953912806963, 0.31655641235105936, 0.30506327535078004, 0.2912818644132092, 0.2755634834035527, 0.2582941616625299, 0.23987899288322825, 0.2207265357907252, 0.20123410250188192, 0.18177465052534833, 0.16268584184053636, 0.14426165259967583, 0.12674672614287222, 0.11033347612997459, 0.09516177964375815, 0.08132096298750445, 0.06885368268695924, 0.05776124400440721, 0.04800987837539687, 0.039537515651160544, 0.03226063052550099, 0.02608080722947321, 0.020890744155519354, 0.01657950251700238],
            "type": "arbitrary",
        },
        "-408720680602617418_q": {
            "samples": [-0.002176912286652786, -0.002635416434473717, -0.003155863035396428, -0.003737529459898692, -0.004377005495376286, -0.0050677329589400915, -0.005799631560560782, -0.006558856924647869, -0.007327736037721211, -0.008084920515387258, -0.008805788584811894, -0.009463112599858525, -0.01002799079389511, -0.01047102091591148, -0.01076367097721486, -0.010879780544272001, -0.010797107059705819, -0.010498817769750753, -0.00997482093817558, -0.009222831576384625, -0.008249077623987995, -0.007068572189594676, -0.00570490497293551, -0.004189539302176429, -0.0025606375658279064, -0.0008614739599292228, 0.0008614739599292228, 0.0025606375658279064, 0.004189539302176429, 0.00570490497293551, 0.007068572189594676, 0.008249077623987995, 0.009222831576384625, 0.00997482093817558, 0.010498817769750753, 0.010797107059705819, 0.010879780544272001, 0.01076367097721486, 0.01047102091591148, 0.01002799079389511, 0.009463112599858525, 0.008805788584811894, 0.008084920515387258, 0.007327736037721211, 0.006558856924647869, 0.005799631560560782, 0.0050677329589400915, 0.004377005495376286, 0.003737529459898692, 0.003155863035396428, 0.002635416434473717, 0.002176912286652786],
            "type": "arbitrary",
        },
        "5155570353030811746_i": {
            "samples": [0.016542661086237562, 0.020757168497619577, 0.025814614488185412, 0.03181983851638414, 0.03887452481399994, 0.04707247247225583, 0.0564941815705114, 0.06720092132303716, 0.07922851714716522, 0.09258116099763809, 0.10722560670262912, 0.12308615247436733, 0.14004082967288922, 0.1579192047686583, 0.17650215660339347, 0.1955239123226293, 0.2146765145931542, 0.2336167550154471, 0.2519754522399875, 0.26936878913628715, 0.2854112642695508, 0.299729672518253, 0.3119774210071509, 0.32184842085515303, 0.32908978064121425, 0.3335125679406225, 0.335, 0.3335125679406225, 0.32908978064121425, 0.32184842085515303, 0.3119774210071509, 0.299729672518253, 0.2854112642695508, 0.26936878913628715, 0.2519754522399875, 0.2336167550154471, 0.2146765145931542, 0.1955239123226293, 0.17650215660339347, 0.1579192047686583, 0.14004082967288922, 0.12308615247436733, 0.10722560670262912, 0.09258116099763809, 0.07922851714716522, 0.06720092132303716, 0.0564941815705114, 0.04707247247225583, 0.03887452481399994, 0.03181983851638414, 0.025814614488185412, 0.020757168497619577, 0.016542661086237562] + [0.0] * 3,
            "type": "arbitrary",
        },
        "5155570353030811746_q": {
            "samples": [-0.0021318808254947126, -0.0025721264926059726, -0.0030708675740587043, -0.0036275216282989535, -0.004239083560566626, -0.00489971148844705, -0.005600385471159751, -0.006328678464144816, -0.007068678607209158, -0.007801098243383997, -0.008503597548914917, -0.00915133931745744, -0.00971777666737645, -0.010175658041612166, -0.010498215065595047, -0.01066048017808871, -0.010640664223324828, -0.010421511205340026, -0.00999153981938788, -0.009346080497032422, -0.008488023297012565, -0.007428206129296702, -0.006185393848949322, -0.004785825291998982, -0.003262335297148941, -0.0016530896527924813, 0.0, 0.0016530896527924813, 0.003262335297148941, 0.004785825291998982, 0.006185393848949322, 0.007428206129296702, 0.008488023297012565, 0.009346080497032422, 0.00999153981938788, 0.010421511205340026, 0.010640664223324828, 0.01066048017808871, 0.010498215065595047, 0.010175658041612166, 0.00971777666737645, 0.00915133931745744, 0.008503597548914917, 0.007801098243383997, 0.007068678607209158, 0.006328678464144816, 0.005600385471159751, 0.00489971148844705, 0.004239083560566626, 0.0036275216282989535, 0.0030708675740587043, 0.0025721264926059726, 0.0021318808254947126] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3038280752780913852_i": {
            "samples": [0.016507248690971008, 0.020629202980209618, 0.025560351909563264, 0.03139986879074453, 0.038244189603245146, 0.04618274222562704, 0.05529305625669434, 0.06563539443280969, 0.07724710779913953, 0.09013697549097037, 0.10427984082962836, 0.11961189270880439, 0.13602695940130002, 0.1533741761934908, 0.17145735528653616, 0.19003632477250224, 0.2088304141698222, 0.22752415058260944, 0.2457750982456412, 0.26322363356897543, 0.27950430809000565, 0.29425832418954645, 0.3071465441702297, 0.3178623823101586, 0.32614389956759143, 0.3317844364035494] + [0.3346411816713917] * 2 + [0.3317844364035494, 0.32614389956759143, 0.3178623823101586, 0.3071465441702297, 0.29425832418954645, 0.27950430809000565, 0.26322363356897543, 0.2457750982456412, 0.22752415058260944, 0.2088304141698222, 0.19003632477250224, 0.17145735528653616, 0.1533741761934908, 0.13602695940130002, 0.11961189270880439, 0.10427984082962836, 0.09013697549097037, 0.07724710779913953, 0.06563539443280969, 0.05529305625669434, 0.04618274222562704, 0.038244189603245146, 0.03139986879074453, 0.025560351909563264, 0.020629202980209618, 0.016507248690971008] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3038280752780913852_q": {
            "samples": [-0.0020886659696863334, -0.002511719008350751, -0.0029900698641855236, -0.0035232553358263904, -0.004108624045254186, -0.004740963365245198, -0.005412188068290606, -0.006111124528270001, -0.006823424321696394, -0.007531638258066104, -0.00821547591070215, -0.008852266571432198, -0.009417625479212441, -0.00988631478036848, -0.010233272905478272, -0.010434770118161964, -0.010469633321345144, -0.010320471282331592, -0.009974823661955774, -0.00942615476477418, -0.008674616532164513, -0.007727515227839197, -0.006599432174593403, -0.005311969846707473, -0.003893119108427239, -0.002376269488935318, -0.0007989099171003004, 0.0007989099171003004, 0.002376269488935318, 0.003893119108427239, 0.005311969846707473, 0.006599432174593403, 0.007727515227839197, 0.008674616532164513, 0.00942615476477418, 0.009974823661955774, 0.010320471282331592, 0.010469633321345144, 0.010434770118161964, 0.010233272905478272, 0.00988631478036848, 0.009417625479212441, 0.008852266571432198, 0.00821547591070215, 0.007531638258066104, 0.006823424321696394, 0.006111124528270001, 0.005412188068290606, 0.004740963365245198, 0.004108624045254186, 0.0035232553358263904, 0.0029900698641855236, 0.002511719008350751, 0.0020886659696863334] + [0.0] * 2,
            "type": "arbitrary",
        },
        "3342750881422719267_i": {
            "samples": [0.016473183850336713, 0.020506503958062083, 0.02531724802887537, 0.03099931918807137, 0.03764424617771005, 0.04533731988426526, 0.05415316834373543, 0.06415089032991211, 0.07536892046661006, 0.08781984995833064, 0.10148547205679116, 0.11631235551125596, 0.13220826782069806, 0.14903976901200047, 0.16663127286419055, 0.18476582445655004, 0.2031877710037322, 0.2216074096425405, 0.23970758580599483, 0.25715209570049663, 0.27359562441412816, 0.2886948365247474, 0.3021201381461697, 0.31356755689496396, 0.3227701465074378, 0.3295083207256078, 0.33361855866269197, 0.335, 0.33361855866269197, 0.3295083207256078, 0.3227701465074378, 0.31356755689496396, 0.3021201381461697, 0.2886948365247474, 0.27359562441412816, 0.25715209570049663, 0.23970758580599483, 0.2216074096425405, 0.2031877710037322, 0.18476582445655004, 0.16663127286419055, 0.14903976901200047, 0.13220826782069806, 0.11631235551125596, 0.10148547205679116, 0.08781984995833064, 0.07536892046661006, 0.06415089032991211, 0.05415316834373543, 0.04533731988426526, 0.03764424617771005, 0.03099931918807137, 0.02531724802887537, 0.020506503958062083, 0.016473183850336713, 0.0],
            "type": "arbitrary",
        },
        "3342750881422719267_q": {
            "samples": [-0.002047160404561595, -0.0024540055328002804, -0.002913178314304419, -0.0034243169929581737, -0.003985079633391114, -0.004590807552586281, -0.005234241170743775, -0.005905317429106773, -0.006591078120470913, -0.007275716348160993, -0.007940783600626927, -0.00856557253299183, -0.009127680662947247, -0.009603748268110337, -0.009970350538115817, -0.010205010448228729, -0.010287286016225687, -0.010199874794029937, -0.009929670807080668, -0.009468705702208488, -0.008814907328252044, -0.007972615692729343, -0.006952808091608157, -0.005773001588633749, -0.004456820853062189, -0.0030332411902774946, -0.0015355386955757115, 0.0, 0.0015355386955757115, 0.0030332411902774946, 0.004456820853062189, 0.005773001588633749, 0.006952808091608157, 0.007972615692729343, 0.008814907328252044, 0.009468705702208488, 0.009929670807080668, 0.010199874794029937, 0.010287286016225687, 0.010205010448228729, 0.009970350538115817, 0.009603748268110337, 0.009127680662947247, 0.00856557253299183, 0.007940783600626927, 0.007275716348160993, 0.006591078120470913, 0.005905317429106773, 0.005234241170743775, 0.004590807552586281, 0.003985079633391114, 0.0034243169929581737, 0.002913178314304419, 0.0024540055328002804, 0.002047160404561595, 0.0],
            "type": "arbitrary",
        },
        "-3535646133561972208_i": {
            "samples": [0.0164403911567603, 0.020388755120185502, 0.025084595620544388, 0.03061690804427584, 0.03707262910780947, 0.04453313546503025, 0.05307023273875479, 0.06274173753673878, 0.07358680075847314, 0.08562116513765215, 0.09883258981843837, 0.11317670586417525, 0.12857358500852906, 0.1449053061501027, 0.16201478733409075, 0.17970611371342504, 0.1977465341940047, 0.21587022281644047, 0.23378380886842698, 0.25117357740192264, 0.2677141357998929, 0.283078239809738, 0.296947381917303, 0.3090226736528391, 0.3190355079648841, 0.32675747306945074, 0.33200900787519416] + [0.3346663413355385] * 2 + [0.33200900787519416, 0.32675747306945074, 0.3190355079648841, 0.3090226736528391, 0.296947381917303, 0.283078239809738, 0.2677141357998929, 0.25117357740192264, 0.23378380886842698, 0.21587022281644047, 0.1977465341940047, 0.17970611371342504, 0.16201478733409075, 0.1449053061501027, 0.12857358500852906, 0.11317670586417525, 0.09883258981843837, 0.08562116513765215, 0.07358680075847314, 0.06274173753673878, 0.05307023273875479, 0.04453313546503025, 0.03707262910780947, 0.03061690804427584, 0.025084595620544388, 0.020388755120185502, 0.0164403911567603],
            "type": "arbitrary",
        },
        "-3535646133561972208_q": {
            "samples": [-0.00200726507594195, -0.0023988134327063613, -0.0028399269766429328, -0.003330330253056695, -0.0038679525429774026, -0.0044486237926805354, -0.0050658151738094915, -0.005710449445441402, -0.006370806607138327, -0.007032548730889293, -0.007678884103242739, -0.008290884818682627, -0.00884796385911986, -0.009328507808306177, -0.009710650240648043, -0.009973159246824728, -0.010096401421466927, -0.01006333493067717, -0.009860476982758914, -0.00947878702230868, -0.008914406929581046, -0.00816920381521596, -0.007251069678715051, -0.006173944880073752, -0.004957548304627095, -0.0036268151891687404, -0.0022110624765053163, -0.0007429197922590618, 0.0007429197922590618, 0.0022110624765053163, 0.0036268151891687404, 0.004957548304627095, 0.006173944880073752, 0.007251069678715051, 0.00816920381521596, 0.008914406929581046, 0.00947878702230868, 0.009860476982758914, 0.01006333493067717, 0.010096401421466927, 0.009973159246824728, 0.009710650240648043, 0.009328507808306177, 0.00884796385911986, 0.008290884818682627, 0.007678884103242739, 0.007032548730889293, 0.006370806607138327, 0.005710449445441402, 0.0050658151738094915, 0.0044486237926805354, 0.0038679525429774026, 0.003330330253056695, 0.0028399269766429328, 0.0023988134327063613, 0.00200726507594195],
            "type": "arbitrary",
        },
        "5540510569425886130_i": {
            "samples": [0.016408800720936062, 0.020275664839288273, 0.024861745221146623, 0.030251461741891666, 0.03652745062458811, 0.043767385600490656, 0.05204033614215418, 0.06140275056025776, 0.07189419144496126, 0.08353298994039424, 0.09631202061755613, 0.11019482694404885, 0.12511234521565842, 0.14096047928005417, 0.15759876702128542, 0.1748503508820372, 0.19250341836808385, 0.21031421558105412, 0.22801165990702196, 0.2453034910191875, 0.2618838075381023, 0.27744174614562184, 0.2916709772433678, 0.30427962288691446, 0.31500015457740793, 0.32359880522556134, 0.3298840342230199, 0.3337136180494152, 0.335, 0.3337136180494152, 0.3298840342230199, 0.32359880522556134, 0.31500015457740793, 0.30427962288691446, 0.2916709772433678, 0.27744174614562184, 0.2618838075381023, 0.2453034910191875, 0.22801165990702196, 0.21031421558105412, 0.19250341836808385, 0.1748503508820372, 0.15759876702128542, 0.14096047928005417, 0.12511234521565842, 0.11019482694404885, 0.09631202061755613, 0.08353298994039424, 0.07189419144496126, 0.06140275056025776, 0.05204033614215418, 0.043767385600490656, 0.03652745062458811, 0.030251461741891666, 0.024861745221146623, 0.020275664839288273, 0.016408800720936062] + [0.0] * 3,
            "type": "arbitrary",
        },
        "5540510569425886130_q": {
            "samples": [-0.0019688884127099467, -0.002345984286348154, -0.002770072849215823, -0.0032409520389237597, -0.0037567892726958645, -0.004313846349167867, -0.004906242441089008, -0.005525776966092957, -0.006161834514665067, -0.006801392820111713, -0.0074291517687551, -0.008027796588310147, -0.008578401692445102, -0.0090609734490495, -0.009455120807509026, -0.009740832860804554, -0.009899332758192679, -0.009913968730231553, -0.009771096158976478, -0.009460900376202905, -0.008978108810670982, -0.008322543622751848, -0.007499472175913451, -0.006519722402919049, -0.005399542815877758, -0.004160201777503244, -0.0028273366555189457, -0.0014300794322757195, 0.0, 0.0014300794322757195, 0.0028273366555189457, 0.004160201777503244, 0.005399542815877758, 0.006519722402919049, 0.007499472175913451, 0.008322543622751848, 0.008978108810670982, 0.009460900376202905, 0.009771096158976478, 0.009913968730231553, 0.009899332758192679, 0.009740832860804554, 0.009455120807509026, 0.0090609734490495, 0.008578401692445102, 0.008027796588310147, 0.0074291517687551, 0.006801392820111713, 0.006161834514665067, 0.005525776966092957, 0.004906242441089008, 0.004313846349167867, 0.0037567892726958645, 0.0032409520389237597, 0.002770072849215823, 0.002345984286348154, 0.0019688884127099467] + [0.0] * 3,
            "type": "arbitrary",
        },
        "5762004628624601378_i": {
            "samples": [0.016378347676530847, 0.020166963822382845, 0.02464809941330183, 0.02990190375027576, 0.03600698236650678, 0.04303750610804605, 0.05105989921153689, 0.06012918170394747, 0.0702850759547895, 0.08154802134750797, 0.09391527226903545, 0.10735728017340702, 0.12181457754839718, 0.13719538759698016, 0.15337417619349084, 0.17019134076237294, 0.1874541936776161, 0.2049393462349833, 0.22239653505781506, 0.23955385900927825, 0.25612431542194686, 0.27181344467901164, 0.2863278173487777, 0.2993840337281388, 0.3107178569605741, 0.32009307219680694, 0.32730965865162953, 0.3322108803946219] + [0.334688945035265] * 2 + [0.3322108803946219, 0.32730965865162953, 0.32009307219680694, 0.3107178569605741, 0.2993840337281388, 0.2863278173487777, 0.27181344467901164, 0.25612431542194686, 0.23955385900927825, 0.22239653505781506, 0.2049393462349833, 0.1874541936776161, 0.17019134076237294, 0.15337417619349084, 0.13719538759698016, 0.12181457754839718, 0.10735728017340702, 0.09391527226903545, 0.08154802134750797, 0.0702850759547895, 0.06012918170394747, 0.05105989921153689, 0.04303750610804605, 0.03600698236650678, 0.02990190375027576, 0.02464809941330183, 0.020166963822382845, 0.016378347676530847] + [0.0] * 2,
            "type": "arbitrary",
        },
        "5762004628624601378_q": {
            "samples": [-0.0019319456353301236, -0.0022953724687497057, -0.0027033935056318607, -0.0031558690549017064, -0.0036511759799596334, -0.004185958466225918, -0.004754911373669249, -0.005350615074410809, -0.005963441109106911, -0.006581547114285973, -0.007190977097380092, -0.007775879186293504, -0.008318847499095559, -0.008801387950742706, -0.009204499967929273, -0.009509357688369803, -0.00969806585906962, -0.009754457976512901, -0.009664897910602368, -0.00941904196686527, -0.00901051661011775, -0.00843746827796599, -0.007702946022365331, -0.006815085053508135, -0.005787069284814196, -0.0046368631056069465, -0.003386716043677543, -0.0020624577774178174, -0.0006926140978924638, 0.0006926140978924638, 0.0020624577774178174, 0.003386716043677543, 0.0046368631056069465, 0.005787069284814196, 0.006815085053508135, 0.007702946022365331, 0.00843746827796599, 0.00901051661011775, 0.00941904196686527, 0.009664897910602368, 0.009754457976512901, 0.00969806585906962, 0.009509357688369803, 0.009204499967929273, 0.008801387950742706, 0.008318847499095559, 0.007775879186293504, 0.007190977097380092, 0.006581547114285973, 0.005963441109106911, 0.005350615074410809, 0.004754911373669249, 0.004185958466225918, 0.0036511759799596334, 0.0031558690549017064, 0.0027033935056318607, 0.0022953724687497057, 0.0019319456353301236] + [0.0] * 2,
            "type": "arbitrary",
        },
        "4614182811447732605_i": {
            "samples": [0.01634897173725341, 0.020062403023516345, 0.024443107769010403, 0.02956724495444249, 0.035509639286464854, 0.04234114778542693, 0.050125643081760055, 0.058916678196277224, 0.06875392763840943, 0.079659529573118, 0.09163448146975535, 0.10465526473060204, 0.11867088992658452, 0.1336005612050422, 0.14933215429105517, 0.16572168595263273, 0.18259392326727863, 0.19974423884371661, 0.21694176464209772, 0.23393383452744687, 0.2504516374394403, 0.26621693307873934, 0.28094961481086794, 0.29437584476835565, 0.3062364384005989, 0.3162951439252993, 0.32434644930378553, 0.33022255730826106, 0.3337991983630799, 0.335, 0.3337991983630799, 0.33022255730826106, 0.32434644930378553, 0.3162951439252993, 0.3062364384005989, 0.29437584476835565, 0.28094961481086794, 0.26621693307873934, 0.2504516374394403, 0.23393383452744687, 0.21694176464209772, 0.19974423884371661, 0.18259392326727863, 0.16572168595263273, 0.14933215429105517, 0.1336005612050422, 0.11867088992658452, 0.10465526473060204, 0.09163448146975535, 0.079659529573118, 0.06875392763840943, 0.058916678196277224, 0.050125643081760055, 0.04234114778542693, 0.035509639286464854, 0.02956724495444249, 0.024443107769010403, 0.020062403023516345, 0.01634897173725341, 0.0],
            "type": "arbitrary",
        },
        "4614182811447732605_q": {
            "samples": [-0.0018963581394580969, -0.0022468439008986414, -0.002639685007763613, -0.0030747947181428187, -0.0035507344064161076, -0.004064487455774393, -0.00461126108802299, -0.005184332561988199, -0.005774956623944011, -0.006372350452165925, -0.006963770448169911, -0.0075346920122584355, -0.008069098922185032, -0.0085498832460278, -0.008959350118111706, -0.009279814558925426, -0.00949427029289124, -0.009587103746664582, -0.009544820659630074, -0.009356748553602688, -0.009015676167508658, -0.008518391223093582, -0.007866080745134263, -0.007064563615560401, -0.006124332886376585, -0.005060395194928278, -0.003891905815830109, -0.0026416097027627977, -0.0013351104908730241, 0.0, 0.0013351104908730241, 0.0026416097027627977, 0.003891905815830109, 0.005060395194928278, 0.006124332886376585, 0.007064563615560401, 0.007866080745134263, 0.008518391223093582, 0.009015676167508658, 0.009356748553602688, 0.009544820659630074, 0.009587103746664582, 0.00949427029289124, 0.009279814558925426, 0.008959350118111706, 0.0085498832460278, 0.008069098922185032, 0.0075346920122584355, 0.006963770448169911, 0.006372350452165925, 0.005774956623944011, 0.005184332561988199, 0.00461126108802299, 0.004064487455774393, 0.0035507344064161076, 0.0030747947181428187, 0.002639685007763613, 0.0022468439008986414, 0.0018963581394580969, 0.0],
            "type": "arbitrary",
        },
        "-3053172245073817764_i": {
            "samples": [0.016320616799946945, 0.01996175178526534, 0.024246262366054892, 0.029246575101332925, 0.035033965431815486, 0.04167615500942922, 0.049234559688591965, 0.0577612440044072, 0.06729566419935343, 0.07786130811768481, 0.08946236480082503, 0.1020805774348162, 0.11567244840843036, 0.130166972716642, 0.14546407413124934, 0.16143390623893508, 0.17791715699684066, 0.19472646098759386, 0.21164897899635338, 0.22845015164876664, 0.24487857520227582, 0.2606718864105229, 0.2755634834035527, 0.2892898547029117, 0.30159824272338287, 0.31225433494044175, 0.3210496581984047, 0.32780835134453135, 0.3323930093171816] + [0.33470932756705135] * 2 + [0.3323930093171816, 0.32780835134453135, 0.3210496581984047, 0.31225433494044175, 0.30159824272338287, 0.2892898547029117, 0.2755634834035527, 0.2606718864105229, 0.24487857520227582, 0.22845015164876664, 0.21164897899635338, 0.19472646098759386, 0.17791715699684066, 0.16143390623893508, 0.14546407413124934, 0.130166972716642, 0.11567244840843036, 0.1020805774348162, 0.08946236480082503, 0.07786130811768481, 0.06729566419935343, 0.0577612440044072, 0.049234559688591965, 0.04167615500942922, 0.035033965431815486, 0.029246575101332925, 0.024246262366054892, 0.01996175178526534, 0.016320616799946945],
            "type": "arbitrary",
        },
        "-3053172245073817764_q": {
            "samples": [-0.0018620529453157136, -0.002200274941394637, -0.002578760063220144, -0.002997466452645629, -0.0034551182790679476, -0.00394900033566353, -0.004474776639723755, -0.005026347352486011, -0.005595758788222605, -0.006173180825164837, -0.006746964528191154, -0.007303790172813821, -0.007828912128505498, -0.008306502315059108, -0.008720088384255656, -0.009053076691486693, -0.00928934388218517, -0.009413874961723499, -0.009413420512177074, -0.009277141727061082, -0.00899720957188574, -0.008569323973416662, -0.007993120699533342, -0.007272437567803253, -0.006415417698039063, -0.005434435413511581, -0.004345839648949369, -0.0031695197615312807, -0.0019283087950100212, -0.0006472488109234461, 0.0006472488109234461, 0.0019283087950100212, 0.0031695197615312807, 0.004345839648949369, 0.005434435413511581, 0.006415417698039063, 0.007272437567803253, 0.007993120699533342, 0.008569323973416662, 0.00899720957188574, 0.009277141727061082, 0.009413420512177074, 0.009413874961723499, 0.00928934388218517, 0.009053076691486693, 0.008720088384255656, 0.008306502315059108, 0.007828912128505498, 0.007303790172813821, 0.006746964528191154, 0.006173180825164837, 0.005595758788222605, 0.005026347352486011, 0.004474776639723755, 0.00394900033566353, 0.0034551182790679476, 0.002997466452645629, 0.002578760063220144, 0.002200274941394637, 0.0018620529453157136],
            "type": "arbitrary",
        },
        "6811942499450899468_i": {
            "samples": [0.016293230588224045, 0.019864796180380968, 0.024057093803686067, 0.028939055217545424, 0.03457862135226509, 0.04104054677546668, 0.04838388541897281, 0.05665920577961019, 0.0659056067517156, 0.07614762832958034, 0.0873921731563967, 0.09962557364816733, 0.11281095347738888, 0.12688603991222352, 0.1417615834206893, 0.1573205319562992, 0.17341808880900936, 0.1898827547917869, 0.20651841846681981, 0.22310751342632912, 0.23941521133948504, 0.2551945661632482, 0.27019247165018817, 0.2841562443926857, 0.2968406014752545, 0.3080147685009925, 0.3174694329797812, 0.32502325177997243, 0.3305286306312495, 0.3338765185945078, 0.335, 0.3338765185945078, 0.3305286306312495, 0.32502325177997243, 0.3174694329797812, 0.3080147685009925, 0.2968406014752545, 0.2841562443926857, 0.27019247165018817, 0.2551945661632482, 0.23941521133948504, 0.22310751342632912, 0.20651841846681981, 0.1898827547917869, 0.17341808880900936, 0.1573205319562992, 0.1417615834206893, 0.12688603991222352, 0.11281095347738888, 0.09962557364816733, 0.0873921731563967, 0.07614762832958034, 0.0659056067517156, 0.05665920577961019, 0.04838388541897281, 0.04104054677546668, 0.03457862135226509, 0.028939055217545424, 0.024057093803686067, 0.019864796180380968, 0.016293230588224045] + [0.0] * 3,
            "type": "arbitrary",
        },
        "6811942499450899468_q": {
            "samples": [-0.0018289622048070584, -0.0021555514021157763, -0.0025204463952343027, -0.002923643298006982, -0.003364010125421331, -0.0038390999516897334, -0.00434498473578221, -0.004876122312220392, -0.0054252694904665, -0.00598345388978962, -0.0065400159423479, -0.007082730358708726, -0.007598013263772801, -0.008071217247818313, -0.008487011887662882, -0.008829842106211027, -0.009084451355053494, -0.009236451379236727, -0.009272915642532797, -0.009182969745242502, -0.008958349715132445, -0.00859389819331569, -0.008087969474942723, -0.007442717184661814, -0.006664243018113594, -0.005762591270244784, -0.0047515814698422905, -0.0036484799007184088, -0.002473519579221687, -0.0012492867928092421, 0.0, 0.0012492867928092421, 0.002473519579221687, 0.0036484799007184088, 0.0047515814698422905, 0.005762591270244784, 0.006664243018113594, 0.007442717184661814, 0.008087969474942723, 0.00859389819331569, 0.008958349715132445, 0.009182969745242502, 0.009272915642532797, 0.009236451379236727, 0.009084451355053494, 0.008829842106211027, 0.008487011887662882, 0.008071217247818313, 0.007598013263772801, 0.007082730358708726, 0.0065400159423479, 0.00598345388978962, 0.0054252694904665, 0.004876122312220392, 0.00434498473578221, 0.0038390999516897334, 0.003364010125421331, 0.002923643298006982, 0.0025204463952343027, 0.0021555514021157763, 0.0018289622048070584] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-855412557070650901_i": {
            "samples": [0.016266764331896968, 0.019771337528975235, 0.023875167654401272, 0.028643910873716823, 0.03414237292596187, 0.04043249986686107, 0.04757107767551167, 0.05560718244931465, 0.064579443015132, 0.0745131981026747, 0.08541764951763871, 0.09728312962958431, 0.11007861450038131, 0.12374962170566102, 0.13821663307494672, 0.1533741761934908, 0.16909068394808982, 0.18520922851621907, 0.2015491953984185, 0.21790892536891884, 0.23406930913721002, 0.2497982731633614, 0.2648560479601382, 0.2790010651240334, 0.2919962891332453, 0.30361575738719915, 0.3136510794697187, 0.32191763610554974, 0.3282602209675409, 0.33255788478751336] + [0.3347277706597235] * 2 + [0.33255788478751336, 0.3282602209675409, 0.32191763610554974, 0.3136510794697187, 0.30361575738719915, 0.2919962891332453, 0.2790010651240334, 0.2648560479601382, 0.2497982731633614, 0.23406930913721002, 0.21790892536891884, 0.2015491953984185, 0.18520922851621907, 0.16909068394808982, 0.1533741761934908, 0.13821663307494672, 0.12374962170566102, 0.11007861450038131, 0.09728312962958431, 0.08541764951763871, 0.0745131981026747, 0.064579443015132, 0.05560718244931465, 0.04757107767551167, 0.04043249986686107, 0.03414237292596187, 0.028643910873716823, 0.023875167654401272, 0.019771337528975235, 0.016266764331896968] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-855412557070650901_q": {
            "samples": [-0.0017970227594479075, -0.0021125676721424074, -0.00246458529732475, -0.0028531037918472376, -0.0032771184497566797, -0.0037344215249363894, -0.004221449883924546, -0.004733161421972226, -0.005262951604705943, -0.005802621288455262, -0.00634240602444855, -0.006871075304849239, -0.007376107652101923, -0.007843944137480893, -0.008260318955628392, -0.008610661260320934, -0.008880557823706012, -0.009056261505978483, -0.009125226334715532, -0.00907664652087563, -0.008901974292275502, -0.008595390271141406, -0.008154200455647059, -0.007579135789207393, -0.006874533810094191, -0.006048386845532626, -0.00511224741169141, -0.004080988563323133, -0.002972424481369126, -0.0018068041177230851, -0.0006061977398117059, 0.0006061977398117059, 0.0018068041177230851, 0.002972424481369126, 0.004080988563323133, 0.00511224741169141, 0.006048386845532626, 0.006874533810094191, 0.007579135789207393, 0.008154200455647059, 0.008595390271141406, 0.008901974292275502, 0.00907664652087563, 0.009125226334715532, 0.009056261505978483, 0.008880557823706012, 0.008610661260320934, 0.008260318955628392, 0.007843944137480893, 0.007376107652101923, 0.006871075304849239, 0.00634240602444855, 0.005802621288455262, 0.005262951604705943, 0.004733161421972226, 0.004221449883924546, 0.0037344215249363894, 0.0032771184497566797, 0.0028531037918472376, 0.00246458529732475, 0.0021125676721424074, 0.0017970227594479075] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6401591757231887802_i": {
            "samples": [0.01624117247808034, 0.019681191070026256, 0.023700081297538995, 0.028360426188547557, 0.03372408142392078, 0.039850333886276554, 0.04679379399820855, 0.05460205803061826, 0.0633131942083855, 0.07295312435352355, 0.08353298994039428, 0.0950466066202214, 0.10746812326650107, 0.12075000918027008, 0.13482149516619077, 0.1495875898466755, 0.16492878122452378, 0.18070151492460498, 0.19673951498310518, 0.2128559812375492, 0.22884666052080463, 0.24449374864985263, 0.25957053867588853, 0.27384669034320225, 0.28709395863081844, 0.29909218802334814, 0.3096353559629908, 0.3185374355787059, 0.32563784554601377, 0.33080626442893113, 0.333946608000954, 0.335, 0.333946608000954, 0.33080626442893113, 0.32563784554601377, 0.3185374355787059, 0.3096353559629908, 0.29909218802334814, 0.28709395863081844, 0.27384669034320225, 0.25957053867588853, 0.24449374864985263, 0.22884666052080463, 0.2128559812375492, 0.19673951498310518, 0.18070151492460498, 0.16492878122452378, 0.1495875898466755, 0.13482149516619077, 0.12075000918027008, 0.10746812326650107, 0.0950466066202214, 0.08353298994039428, 0.07295312435352355, 0.0633131942083855, 0.05460205803061826, 0.04679379399820855, 0.039850333886276554, 0.03372408142392078, 0.028360426188547557, 0.023700081297538995, 0.019681191070026256, 0.01624117247808034, 0.0],
            "type": "arbitrary",
        },
        "-6401591757231887802_q": {
            "samples": [-0.00176617574311322, -0.0020712259364102986, -0.0024110303490801678, -0.0027856440907637835, -0.0031941752249890557, -0.0036346295734523654, -0.004103770932328403, -0.004597006283695243, -0.005108305993576153, -0.005630168859940528, -0.006153641122958217, -0.00666839712085666, -0.007162887153939176, -0.007624555341577404, -0.008040126910789274, -0.008395960583297545, -0.00867845772436571, -0.00887451591691981, -0.008972010892868863, -0.008960287565740046, -0.008830638531133623, -0.008576747069354402, -0.008195071580585628, -0.007685149618175738, -0.0070498022846785646, -0.00629522364787283, -0.005430944853374045, -0.004469668500182291, -0.003426975273863721, -0.0023209114135905517, -0.0011714719117808217, 0.0, 0.0011714719117808217, 0.0023209114135905517, 0.003426975273863721, 0.004469668500182291, 0.005430944853374045, 0.00629522364787283, 0.0070498022846785646, 0.007685149618175738, 0.008195071580585628, 0.008576747069354402, 0.008830638531133623, 0.008960287565740046, 0.008972010892868863, 0.00887451591691981, 0.00867845772436571, 0.008395960583297545, 0.008040126910789274, 0.007624555341577404, 0.007162887153939176, 0.00666839712085666, 0.006153641122958217, 0.005630168859940528, 0.005108305993576153, 0.004597006283695243, 0.004103770932328403, 0.0036346295734523654, 0.0031941752249890557, 0.0027856440907637835, 0.0024110303490801678, 0.0020712259364102986, 0.00176617574311322, 0.0],
            "type": "arbitrary",
        },
        "-6180097698033172554_i": {
            "samples": [0.016216412430376588, 0.019594184768852253, 0.023531461087949016, 0.028087938480488586, 0.0333226946581478, 0.039292497918621105, 0.04604987343385001, 0.053640957292574135, 0.06210318524859527, 0.07146287894211999, 0.08173280759377569, 0.0929098168252094, 0.1049726272823159, 0.11787991307855558, 0.13156877276933854, 0.1459537028089519, 0.1609261746655849, 0.1763549017278133, 0.19208686094813487, 0.20794910736261257, 0.22375138814191703, 0.23928952800230852, 0.2543495213081974, 0.26871222995742483, 0.28215855222499425, 0.294474898230074, 0.30545878453267716, 0.3149243452349405, 0.3227075511276572, 0.3286709326438658, 0.3327076168286677] + [0.3347445127562449] * 2 + [0.3327076168286677, 0.3286709326438658, 0.3227075511276572, 0.3149243452349405, 0.30545878453267716, 0.294474898230074, 0.28215855222499425, 0.26871222995742483, 0.2543495213081974, 0.23928952800230852, 0.22375138814191703, 0.20794910736261257, 0.19208686094813487, 0.1763549017278133, 0.1609261746655849, 0.1459537028089519, 0.13156877276933854, 0.11787991307855558, 0.1049726272823159, 0.0929098168252094, 0.08173280759377569, 0.07146287894211999, 0.06210318524859527, 0.053640957292574135, 0.04604987343385001, 0.039292497918621105, 0.0333226946581478, 0.028087938480488586, 0.023531461087949016, 0.019594184768852253, 0.016216412430376588],
            "type": "arbitrary",
        },
        "-6180097698033172554_q": {
            "samples": [-0.0017363662244007203, -0.0020314354774496595, -0.002359646272771454, -0.002721076299644575, -0.0031149336608541464, -0.00353941516380004, -0.003991577958148033, -0.004467232935977991, -0.004960868695206504, -0.005465614799921432, -0.0059732524776101815, -0.006474279723657468, -0.006958036021687266, -0.00741288955786247, -0.007826486975716212, -0.008186062498305356, -0.008478799792123846, -0.008692236454485958, -0.00881469769152934, -0.008835742848878144, -0.008746606189146808, -0.008540611886463349, -0.008213542795702767, -0.007763943265581512, -0.007193338144196442, -0.006506353139906354, -0.005710725736352062, -0.004817200727571458, -0.003839309879850876, -0.00279304093157581, -0.0016964067699709064, -0.0005689308258735929, 0.0005689308258735929, 0.0016964067699709064, 0.00279304093157581, 0.003839309879850876, 0.004817200727571458, 0.005710725736352062, 0.006506353139906354, 0.007193338144196442, 0.007763943265581512, 0.008213542795702767, 0.008540611886463349, 0.008746606189146808, 0.008835742848878144, 0.00881469769152934, 0.008692236454485958, 0.008478799792123846, 0.008186062498305356, 0.007826486975716212, 0.00741288955786247, 0.006958036021687266, 0.006474279723657468, 0.0059732524776101815, 0.005465614799921432, 0.004960868695206504, 0.004467232935977991, 0.003991577958148033, 0.00353941516380004, 0.0031149336608541464, 0.002721076299644575, 0.002359646272771454, 0.0020314354774496595, 0.0017363662244007203],
            "type": "arbitrary",
        },
        "2025431591193819225_i": {
            "samples": [0.01619244431301248, 0.01951015824464915, 0.023368959819382324, 0.027825833487822284, 0.0329372390801896, 0.03875755862614556, 0.04533731988426526, 0.05272122394039203, 0.06094601790475665, 0.0700382677228703, 0.08001209966926354, 0.0908669913720193, 0.1025857033194442, 0.11513244882518447, 0.12845140353102671, 0.14246565399003253, 0.1570766781718625, 0.1721644385966181, 0.18758815126708003, 0.2031877710037322, 0.2187862069148971, 0.23419225161672305, 0.24920417581611157, 0.2636139075819408, 0.2772116848037537, 0.2897910417647302, 0.3011539681579358, 0.3111160627814493, 0.3195114957851667, 0.3261975935346741, 0.33105886925538397, 0.334010340454945, 0.335, 0.334010340454945, 0.33105886925538397, 0.3261975935346741, 0.3195114957851667, 0.3111160627814493, 0.3011539681579358, 0.2897910417647302, 0.2772116848037537, 0.2636139075819408, 0.24920417581611157, 0.23419225161672305, 0.2187862069148971, 0.2031877710037322, 0.18758815126708003, 0.1721644385966181, 0.1570766781718625, 0.14246565399003253, 0.12845140353102671, 0.11513244882518447, 0.1025857033194442, 0.0908669913720193, 0.08001209966926354, 0.0700382677228703, 0.06094601790475665, 0.05272122394039203, 0.04533731988426526, 0.03875755862614556, 0.0329372390801896, 0.027825833487822284, 0.023368959819382324, 0.01951015824464915, 0.01619244431301248] + [0.0] * 3,
            "type": "arbitrary",
        },
        "2025431591193819225_q": {
            "samples": [-0.0017075428840861845, -0.001993112050162914, -0.0023103079133342625, -0.00265922698338335, -0.003039166214496298, -0.0034484934536585933, -0.0038845294675730066, -0.0043434489529258725, -0.004820208294758158, -0.00530850781601013, -0.005800795793588807, -0.006288320558344851, -0.006761235530825814, -0.007208760086750436, -0.007619396747231025, -0.007981202437909249, -0.008282108583591607, -0.00851028175748369, -0.008654513667383089, -0.008704626629114042, -0.008651878544369622, -0.00848934994635095, -0.008212295053977046, -0.007818439093464398, -0.0073082054602435845, -0.0066848585976713865, -0.005954551688605572, -0.005126272252914079, -0.004211683320204927, -0.0032248627558882515, -0.002181948280487402, -0.0011007004428847914, 0.0, 0.0011007004428847914, 0.002181948280487402, 0.0032248627558882515, 0.004211683320204927, 0.005126272252914079, 0.005954551688605572, 0.0066848585976713865, 0.0073082054602435845, 0.007818439093464398, 0.008212295053977046, 0.00848934994635095, 0.008651878544369622, 0.008704626629114042, 0.008654513667383089, 0.00851028175748369, 0.008282108583591607, 0.007981202437909249, 0.007619396747231025, 0.007208760086750436, 0.006761235530825814, 0.006288320558344851, 0.005800795793588807, 0.00530850781601013, 0.004820208294758158, 0.0043434489529258725, 0.0038845294675730066, 0.0034484934536585933, 0.003039166214496298, 0.00265922698338335, 0.0023103079133342625, 0.001993112050162914, 0.0017075428840861845] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3982338010030005691_i": {
            "samples": [0.016169230757186952, 0.0194289618042702, 0.023212254447670555, 0.027573541088657207, 0.032566812714976884, 0.038244189603245146, 0.04465428719963884, 0.05184040103472302, 0.0598385465922436, 0.06867540243603723, 0.07836621697191876, 0.08891275026434643, 0.10030133157077435, 0.11250111992155204, 0.12546265842434376, 0.1391168123715755, 0.15337417619349084, 0.1681250245502196, 0.18323986836613645, 0.198570657632372, 0.21395264988831578, 0.22920693728099034, 0.24414359709767736, 0.2585654019945559, 0.2722719982744677, 0.28506443503845413, 0.2967499053580553, 0.3071465441702297, 0.31608811754110755, 0.32342843512407077, 0.32904532251621066, 0.33284400283199606] + [0.33475975675503983] * 2 + [0.33284400283199606, 0.32904532251621066, 0.32342843512407077, 0.31608811754110755, 0.3071465441702297, 0.2967499053580553, 0.28506443503845413, 0.2722719982744677, 0.2585654019945559, 0.24414359709767736, 0.22920693728099034, 0.21395264988831578, 0.198570657632372, 0.18323986836613645, 0.1681250245502196, 0.15337417619349084, 0.1391168123715755, 0.12546265842434376, 0.11250111992155204, 0.10030133157077435, 0.08891275026434643, 0.07836621697191876, 0.06867540243603723, 0.0598385465922436, 0.05184040103472302, 0.04465428719963884, 0.038244189603245146, 0.032566812714976884, 0.027573541088657207, 0.023212254447670555, 0.0194289618042702, 0.016169230757186952] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3982338010030005691_q": {
            "samples": [-0.0016796577237259327, -0.0019561773209496283, -0.002262899326666904, -0.0025999358386085284, -0.002966662814092974, -0.003361601491571606, -0.0037823098741726867, -0.00422529080233863, -0.004685923477372001, -0.005158425309445353, -0.005635850596703108, -0.006110131757097959, -0.006572167614016871, -0.0070119615895788195, -0.007418810624632147, -0.007781543292191676, -0.008088803002119666, -0.00832936953727847, -0.008492509564532603, -0.008568344390334538, -0.008548221245580832, -0.00842507294473255, -0.0081937500059417, -0.007851309345924887, -0.007397244536958113, -0.006833644344841425, -0.006165268812532094, -0.005399535415576419, -0.004546411641876646, -0.003618214544941648, -0.0026293221590481244, -0.0015958059007679629, -0.0005349969661703505, 0.0005349969661703505, 0.0015958059007679629, 0.0026293221590481244, 0.003618214544941648, 0.004546411641876646, 0.005399535415576419, 0.006165268812532094, 0.006833644344841425, 0.007397244536958113, 0.007851309345924887, 0.0081937500059417, 0.00842507294473255, 0.008548221245580832, 0.008568344390334538, 0.008492509564532603, 0.00832936953727847, 0.008088803002119666, 0.007781543292191676, 0.007418810624632147, 0.0070119615895788195, 0.006572167614016871, 0.006110131757097959, 0.005635850596703108, 0.005158425309445353, 0.004685923477372001, 0.00422529080233863, 0.0037823098741726867, 0.003361601491571606, 0.002966662814092974, 0.0025999358386085284, 0.002262899326666904, 0.0019561773209496283, 0.0016796577237259327] + [0.0] * 2,
            "type": "arbitrary",
        },
        "6797051007157995556_i": {
            "samples": [0.016146736707229235, 0.01935045557021014, 0.02306104404338824, 0.027330531461535624, 0.03221057883027745, 0.0377511618413431, 0.0439990658132054, 0.050996213394137936, 0.05877785652896376, 0.06737067517340989, 0.07679083600420222, 0.08704207430663082, 0.09811387066455284, 0.10997980035906806, 0.12259613685980716, 0.13590079090120286, 0.14981266293231735, 0.1642314789370631, 0.17903816767184494, 0.19409582142382803, 0.20925126286893805, 0.2243372181675773, 0.23917507197313848, 0.25357815463572614, 0.2673554867978498, 0.28031588311556777, 0.2922722963146792, 0.303046266443439, 0.3124723290842048, 0.3204022312705101, 0.326708805454075, 0.33128936025907807, 0.3340684617545248, 0.335, 0.3340684617545248, 0.33128936025907807, 0.326708805454075, 0.3204022312705101, 0.3124723290842048, 0.303046266443439, 0.2922722963146792, 0.28031588311556777, 0.2673554867978498, 0.25357815463572614, 0.23917507197313848, 0.2243372181675773, 0.20925126286893805, 0.19409582142382803, 0.17903816767184494, 0.1642314789370631, 0.14981266293231735, 0.13590079090120286, 0.12259613685980716, 0.10997980035906806, 0.09811387066455284, 0.08704207430663082, 0.07679083600420222, 0.06737067517340989, 0.05877785652896376, 0.050996213394137936, 0.0439990658132054, 0.0377511618413431, 0.03221057883027745, 0.027330531461535624, 0.02306104404338824, 0.01935045557021014, 0.016146736707229235, 0.0],
            "type": "arbitrary",
        },
        "6797051007157995556_q": {
            "samples": [-0.0016526658019598954, -0.0019205583636415615, -0.0022173129632291075, -0.0025430545060733346, -0.002897229270047503, -0.003278496244181268, -0.0036846272258952294, -0.004112421440500327, -0.004557640756507102, -0.00501497160618527, -0.005478019434553905, -0.0059393408565672386, -0.0063905176844825905, -0.006822275599818847, -0.00722464851618241, -0.007587187665925077, -0.00789921222625086, -0.008150095983563817, -0.008329582242075731, -0.008428117050061348, -0.008437188985220907, -0.008349662345116493, -0.008160089750608432, -0.007864989986207794, -0.007463077434643859, -0.006955430736834684, -0.006345590301121045, -0.005639576928917771, -0.00484582700498139, -0.003975043266832202, -0.0030399639357658486, -0.002055056757328211, -0.0010361480507583927, 0.0, 0.0010361480507583927, 0.002055056757328211, 0.0030399639357658486, 0.003975043266832202, 0.00484582700498139, 0.005639576928917771, 0.006345590301121045, 0.006955430736834684, 0.007463077434643859, 0.007864989986207794, 0.008160089750608432, 0.008349662345116493, 0.008437188985220907, 0.008428117050061348, 0.008329582242075731, 0.008150095983563817, 0.00789921222625086, 0.007587187665925077, 0.00722464851618241, 0.006822275599818847, 0.0063905176844825905, 0.0059393408565672386, 0.005478019434553905, 0.00501497160618527, 0.004557640756507102, 0.004112421440500327, 0.0036846272258952294, 0.003278496244181268, 0.002897229270047503, 0.0025430545060733346, 0.0022173129632291075, 0.0019205583636415615, 0.0016526658019598954, 0.0],
            "type": "arbitrary",
        },
        "-5795157481638098170_i": {
            "samples": [0.016124929244458342, 0.01927450869228548, 0.022915047947641178, 0.027096311635182634, 0.031867760255259114, 0.03727733517381941, 0.0433700707396164, 0.0501865517594088, 0.057761244004407214, 0.06612073517476827, 0.07528193335650114, 0.08525027894381217, 0.09601803370354749, 0.10756271654683178, 0.11984575908657713, 0.1328114546971878, 0.14638627215138347, 0.160478598721249, 0.17497896779812425, 0.18976081270543432, 0.2046817717571848, 0.21958555027325724, 0.23430432392395412, 0.24866164534029045, 0.26247579343002314, 0.2755634834035527, 0.28774383628226063, 0.29884249073253005, 0.3086957284243868, 0.31715447755569254, 0.3240880582730757, 0.32938753873686566, 0.3329685814839935] + [0.3347736761831306] * 2 + [0.3329685814839935, 0.32938753873686566, 0.3240880582730757, 0.31715447755569254, 0.3086957284243868, 0.29884249073253005, 0.28774383628226063, 0.2755634834035527, 0.26247579343002314, 0.24866164534029045, 0.23430432392395412, 0.21958555027325724, 0.2046817717571848, 0.18976081270543432, 0.17497896779812425, 0.160478598721249, 0.14638627215138347, 0.1328114546971878, 0.11984575908657713, 0.10756271654683178, 0.09601803370354749, 0.08525027894381217, 0.07528193335650114, 0.06612073517476827, 0.057761244004407214, 0.0501865517594088, 0.0433700707396164, 0.03727733517381941, 0.031867760255259114, 0.027096311635182634, 0.022915047947641178, 0.01927450869228548, 0.016124929244458342],
            "type": "arbitrary",
        },
        "-5795157481638098170_q": {
            "samples": [-0.0016265249954969397, -0.0018861872056965174, -0.0021734489356647468, -0.002488445506941661, -0.0028306858516208787, -0.003198952824982751, -0.003591211154337307, -0.004004528122456261, -0.0044350123698405994, -0.004877776252992969, -0.005326926974140067, -0.005775591170449458, -0.006215976801198968, -0.006639475000960307, -0.007036803097447507, -0.00739818826785179, -0.007713589392591094, -0.007972952645895556, -0.008166494340727935, -0.008285002635163487, -0.00832014802784563, -0.00826479123867211, -0.00811327619439759, -0.007861695505945647, -0.007508116097600079, -0.00705275355841177, -0.006498085327002932, -0.005848894947592467, -0.005112242264347034, -0.0042973574349157604, -0.0034154598950035696, -0.0024795067260960494, -0.0015038780893792565, -0.000504010312593571, 0.000504010312593571, 0.0015038780893792565, 0.0024795067260960494, 0.0034154598950035696, 0.0042973574349157604, 0.005112242264347034, 0.005848894947592467, 0.006498085327002932, 0.00705275355841177, 0.007508116097600079, 0.007861695505945647, 0.00811327619439759, 0.00826479123867211, 0.00832014802784563, 0.008285002635163487, 0.008166494340727935, 0.007972952645895556, 0.007713589392591094, 0.00739818826785179, 0.007036803097447507, 0.006639475000960307, 0.006215976801198968, 0.005775591170449458, 0.005326926974140067, 0.004877776252992969, 0.0044350123698405994, 0.004004528122456261, 0.003591211154337307, 0.003198952824982751, 0.0028306858516208787, 0.002488445506941661, 0.0021734489356647468, 0.0018861872056965174, 0.0016265249954969397],
            "type": "arbitrary",
        },
        "-8990342977485801182_i": {
            "samples": [0.016103777426886866, 0.019200998633816527, 0.02277400410800667, 0.026870422382619677, 0.03153763427294032, 0.0368216505877448, 0.04276583078167506, 0.04940945852482564, 0.0567861985401308, 0.06492246773341098, 0.07383576222521489, 0.08353298994039425, 0.09400886543407902, 0.1052444291296256, 0.11720575662681057, 0.12984292476372225, 0.14308929931825132, 0.15686120435985737, 0.17105802519359786, 0.18556278562274675, 0.20024322611757164, 0.2149533928222676, 0.2295357287420097, 0.24382363866751464, 0.257644479282525, 0.27082290641336215, 0.2831844935082214, 0.2945595201462605, 0.3047868175633003, 0.31371755059708256, 0.32121881266830116, 0.32717691276241306, 0.3315002409409266, 0.3341216114955792, 0.335, 0.3341216114955792, 0.3315002409409266, 0.32717691276241306, 0.32121881266830116, 0.31371755059708256, 0.3047868175633003, 0.2945595201462605, 0.2831844935082214, 0.27082290641336215, 0.257644479282525, 0.24382363866751464, 0.2295357287420097, 0.2149533928222676, 0.20024322611757164, 0.18556278562274675, 0.17105802519359786, 0.15686120435985737, 0.14308929931825132, 0.12984292476372225, 0.11720575662681057, 0.1052444291296256, 0.09400886543407902, 0.08353298994039425, 0.07383576222521489, 0.06492246773341098, 0.0567861985401308, 0.04940945852482564, 0.04276583078167506, 0.0368216505877448, 0.03153763427294032, 0.026870422382619677, 0.02277400410800667, 0.019200998633816527, 0.016103777426886866] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8990342977485801182_q": {
            "samples": [-0.0016011957821335453, -0.0018530004189435407, -0.0021312143606549054, -0.002435981288413991, -0.002766866009738974, -0.003122762901837567, -0.003501811022805612, -0.0039013204082438556, -0.004317714333805181, -0.004746492388673883, -0.005182219034847583, -0.005618541894874894, -0.006048243300809695, -0.006463327648710038, -0.00685514585209303, -0.007214556708627986, -0.007532123339651963, -0.0077983411016984685, -0.008003891587726889, -0.00813991562855723, -0.008198296673347167, -0.008171944672725955, -0.008055069703460302, -0.007843434139644695, -0.007534572252674907, -0.00712796674533815, -0.006625172899078878, -0.006029882710489139, -0.005347923553390783, -0.004587188435956983, -0.003757497711121213, -0.0028703950057229694, -0.0019388830097225856, -0.0009771074583100395, 0.0, 0.0009771074583100395, 0.0019388830097225856, 0.0028703950057229694, 0.003757497711121213, 0.004587188435956983, 0.005347923553390783, 0.006029882710489139, 0.006625172899078878, 0.00712796674533815, 0.007534572252674907, 0.007843434139644695, 0.008055069703460302, 0.008171944672725955, 0.008198296673347167, 0.00813991562855723, 0.008003891587726889, 0.0077983411016984685, 0.007532123339651963, 0.007214556708627986, 0.00685514585209303, 0.006463327648710038, 0.006048243300809695, 0.005618541894874894, 0.005182219034847583, 0.004746492388673883, 0.004317714333805181, 0.0039013204082438556, 0.003501811022805612, 0.003122762901837567, 0.002766866009738974, 0.002435981288413991, 0.0021312143606549054, 0.0018530004189435407, 0.0016011957821335453] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3597397793634931307_i": {
            "samples": [0.016083252143132255, 0.019129810524250796, 0.022637667574557457, 0.026652435420606278, 0.03121952802097834, 0.03638312330362169, 0.04218497880950384, 0.048663114865035516, 0.05585038674456087, 0.06377297500938481, 0.07244883088801225, 0.08188612080984226, 0.092081720602586, 0.10301981497770468, 0.11467066133180417, 0.12698957819326176, 0.13991621751273156, 0.15337417619349078, 0.16727099565734846, 0.18149858885368278, 0.19593412210217995, 0.21044136482876674, 0.2248725040764974, 0.2390704032558961, 0.2528712666663175, 0.2661076536795146, 0.2786117699813084, 0.29021894876787196, 0.3007712230899501, 0.31012088233215496, 0.3181339016612776, 0.3246931335495753, 0.3297011553355644, 0.3330826761550278] + [0.3347864201538738] * 2 + [0.3330826761550278, 0.3297011553355644, 0.3246931335495753, 0.3181339016612776, 0.31012088233215496, 0.3007712230899501, 0.29021894876787196, 0.2786117699813084, 0.2661076536795146, 0.2528712666663175, 0.2390704032558961, 0.2248725040764974, 0.21044136482876674, 0.19593412210217995, 0.18149858885368278, 0.16727099565734846, 0.15337417619349078, 0.13991621751273156, 0.12698957819326176, 0.11467066133180417, 0.10301981497770468, 0.092081720602586, 0.08188612080984226, 0.07244883088801225, 0.06377297500938481, 0.05585038674456087, 0.048663114865035516, 0.04218497880950384, 0.03638312330362169, 0.03121952802097834, 0.026652435420606278, 0.022637667574557457, 0.019129810524250796, 0.016083252143132255] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3597397793634931307_q": {
            "samples": [-0.0015766410434764372, -0.0018209387498962395, -0.0020905227664771288, -0.0023855433660298496, -0.0027056152291757033, -0.0030497332632704746, -0.0034161942522824857, -0.003802528347117926, -0.0042054446472662614, -0.00462079519653178, -0.0050435615866844166, -0.005467868008819712, -0.0058870239985187684, -0.006293599285141984, -0.006679532089422709, -0.007036270943832808, -0.007354948679378161, -0.007626585687712826, -0.007842317998777073, -0.007993644191482656, -0.008072683764059693, -0.00807243841831427, -0.007987046840580308, -0.007812023063893862, -0.007544468427689582, -0.007183247549587729, -0.006729119600883146, -0.0061848175187601395, -0.005555069552106928, -0.00484655965559052, -0.004067825626120532, -0.0032290964055172082, -0.0023420725284962226, -0.0014196561454206328, -0.00047563926596371425, 0.00047563926596371425, 0.0014196561454206328, 0.0023420725284962226, 0.0032290964055172082, 0.004067825626120532, 0.00484655965559052, 0.005555069552106928, 0.0061848175187601395, 0.006729119600883146, 0.007183247549587729, 0.007544468427689582, 0.007812023063893862, 0.007987046840580308, 0.00807243841831427, 0.008072683764059693, 0.007993644191482656, 0.007842317998777073, 0.007626585687712826, 0.007354948679378161, 0.007036270943832808, 0.006679532089422709, 0.006293599285141984, 0.0058870239985187684, 0.005467868008819712, 0.0050435615866844166, 0.00462079519653178, 0.0042054446472662614, 0.003802528347117926, 0.0034161942522824857, 0.0030497332632704746, 0.0027056152291757033, 0.0023855433660298496, 0.0020905227664771288, 0.0018209387498962395, 0.0015766410434764372] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3375903734436216059_i": {
            "samples": [0.016063325979088387, 0.01906083657114538, 0.02250580913840038, 0.026441950880303954, 0.030912814343554734, 0.03596083653676888, 0.04162624299297049, 0.047945829106206726, 0.05495163768665448, 0.062669558567968, 0.0711178829757973, 0.08030585189782843, 0.09023224352214544, 0.10088404955554527, 0.11223529352416593, 0.12424604564911296, 0.13686168828295417, 0.15001248296505945, 0.163613484775246, 0.17756484181909513, 0.19175250747356232, 0.20604938069976686, 0.22031687566489933, 0.23440690660405733, 0.24816425789858457, 0.2614292934340567, 0.2740409441610348, 0.28583989915889035, 0.2966719141116083, 0.3063911425875728, 0.314863390405169, 0.32196919204893026, 0.3276066107893383, 0.3316936708730784, 0.33417034070890056, 0.335, 0.33417034070890056, 0.3316936708730784, 0.3276066107893383, 0.32196919204893026, 0.314863390405169, 0.3063911425875728, 0.2966719141116083, 0.28583989915889035, 0.2740409441610348, 0.2614292934340567, 0.24816425789858457, 0.23440690660405733, 0.22031687566489933, 0.20604938069976686, 0.19175250747356232, 0.17756484181909513, 0.163613484775246, 0.15001248296505945, 0.13686168828295417, 0.12424604564911296, 0.11223529352416593, 0.10088404955554527, 0.09023224352214544, 0.08030585189782843, 0.0711178829757973, 0.062669558567968, 0.05495163768665448, 0.047945829106206726, 0.04162624299297049, 0.03596083653676888, 0.030912814343554734, 0.026441950880303954, 0.02250580913840038, 0.01906083657114538, 0.016063325979088387, 0.0],
            "type": "arbitrary",
        },
        "-3375903734436216059_q": {
            "samples": [-0.0015528258853165229, -0.0017899467852740094, -0.0020512935588356384, -0.002337021551606808, -0.002646789995435261, -0.0029796845259973423, -0.00333414480671442, -0.003707900823329012, -0.004097921634641259, -0.004500380441051291, -0.004910639736462622, -0.005323260019323092, -0.005732035041661021, -0.006130055867500469, -0.006509805102279825, -0.006863281563884801, -0.007182154427795194, -0.007457944540423475, -0.0076822292140174275, -0.007846865460444968, -0.007944225362443429, -0.007967436193987884, -0.007910617058204616, -0.00776910327634743, -0.007539649587507558, -0.007220603442594154, -0.0068120403147860584, -0.006315853997189677, -0.005735796288746544, -0.0050774622305427885, -0.004348219074538987, -0.0035570793555377584, -0.002714520691934756, -0.0018322571509355114, -0.0009229690677889491, 0.0, 0.0009229690677889491, 0.0018322571509355114, 0.002714520691934756, 0.0035570793555377584, 0.004348219074538987, 0.0050774622305427885, 0.005735796288746544, 0.006315853997189677, 0.0068120403147860584, 0.007220603442594154, 0.007539649587507558, 0.00776910327634743, 0.007910617058204616, 0.007967436193987884, 0.007944225362443429, 0.007846865460444968, 0.0076822292140174275, 0.007457944540423475, 0.007182154427795194, 0.006863281563884801, 0.006509805102279825, 0.006130055867500469, 0.005732035041661021, 0.005323260019323092, 0.004910639736462622, 0.004500380441051291, 0.004097921634641259, 0.003707900823329012, 0.00333414480671442, 0.0029796845259973423, 0.002646789995435261, 0.002337021551606808, 0.0020512935588356384, 0.0017899467852740094, 0.0015528258853165229, 0.0],
            "type": "arbitrary",
        },
        "-6571089230283919071_i": {
            "samples": [0.01604397309607626, 0.018993975525273335, 0.022378214097318324, 0.026238595019304173, 0.030616908044275828, 0.035553935864719756, 0.04108843888273205, 0.04725602620808612, 0.054087929632206745, 0.06160970347838995, 0.06983987939141753, 0.0787886110194084, 0.08845634884536012, 0.09883258981843836, 0.10989474959004092, 0.1216072067710954, 0.1339205684284424, 0.14677120382218672, 0.1600810890230365, 0.1737579985032073, 0.1876960711367925, 0.2017767674590547, 0.21587022281644047, 0.22983698759617713, 0.2435301315575816, 0.25679767497423667, 0.26948529546491384, 0.28143924668932735, 0.2925094141462924, 0.30255242472122407, 0.31143472088817575, 0.3190355079648841, 0.3252494837926356, 0.329989264751213, 0.33318743003725093] + [0.3347981173752495] * 2 + [0.33318743003725093, 0.329989264751213, 0.3252494837926356, 0.3190355079648841, 0.31143472088817575, 0.30255242472122407, 0.2925094141462924, 0.28143924668932735, 0.26948529546491384, 0.25679767497423667, 0.2435301315575816, 0.22983698759617713, 0.21587022281644047, 0.2017767674590547, 0.1876960711367925, 0.1737579985032073, 0.1600810890230365, 0.14677120382218672, 0.1339205684284424, 0.1216072067710954, 0.10989474959004092, 0.09883258981843836, 0.08845634884536012, 0.0787886110194084, 0.06983987939141753, 0.06160970347838995, 0.054087929632206745, 0.04725602620808612, 0.04108843888273205, 0.035553935864719756, 0.030616908044275828, 0.026238595019304173, 0.022378214097318324, 0.018993975525273335, 0.01604397309607626],
            "type": "arbitrary",
        },
        "-6571089230283919071_q": {
            "samples": [-0.001529717473841873, -0.0017599726489081196, -0.0020134515384636355, -0.0022903132571723385, -0.002590256863488539, -0.002912449968241016, -0.003255461821091997, -0.003617204048454361, -0.003994882418829067, -0.004384963089554249, -0.004783156718989864, -0.005184423591255007, -0.005583002484434333, -0.005972465413633242, -0.0063457996030801735, -0.006695517103045926, -0.007013791395173208, -0.007292619162196899, -0.007524004183080861, -0.007700159108379647, -0.00781371973470148, -0.007857965395376714, -0.007827038279415577, -0.007716153940008521, -0.007521795005580186, -0.0072418801964804855, -0.0068759011987329565, -0.00642502075471286, -0.00589212648162651, -0.005281836385056806, -0.00460045374097027, -0.003855870903598852, -0.003057423573934482, -0.0022156990413086486, -0.001342303792578602, -0.00044959757600572303, 0.00044959757600572303, 0.001342303792578602, 0.0022156990413086486, 0.003057423573934482, 0.003855870903598852, 0.00460045374097027, 0.005281836385056806, 0.00589212648162651, 0.00642502075471286, 0.0068759011987329565, 0.0072418801964804855, 0.007521795005580186, 0.007716153940008521, 0.007827038279415577, 0.007857965395376714, 0.00781371973470148, 0.007700159108379647, 0.007524004183080861, 0.007292619162196899, 0.007013791395173208, 0.006695517103045926, 0.0063457996030801735, 0.005972465413633242, 0.005583002484434333, 0.005184423591255007, 0.004783156718989864, 0.004384963089554249, 0.003994882418829067, 0.003617204048454361, 0.003255461821091997, 0.002912449968241016, 0.002590256863488539, 0.0022903132571723385, 0.0020134515384636355, 0.0017599726489081196, 0.001529717473841873],
            "type": "arbitrary",
        },
        "6255663465574916415_i": {
            "samples": [0.016025169119338187, 0.018929132193355087, 0.02225468113496958, 0.026042018148828342, 0.030331262496184168, 0.03516162413428328, 0.0405704622478734, 0.04659223823906354, 0.053257378003682014, 0.06059106382373267, 0.06861198173579104, 0.077331055549729, 0.0867502035211574, 0.09686115774030199, 0.1076443893047986, 0.11906818402392137, 0.1310879135181106, 0.14364554493953316, 0.15666942902010444, 0.1700744007045045, 0.18376221928813738, 0.19762236589096485, 0.21153320549335114, 0.22536350897011118, 0.23897431800009786, 0.25222112288771514, 0.26495631074668563, 0.27703182972760326, 0.2883020045789962, 0.298626430344236, 0.307872864879158, 0.31592003750359626, 0.32266029073649866, 0.32800197483902266, 0.3318715207892068, 0.3342151261736102, 0.335, 0.3342151261736102, 0.3318715207892068, 0.32800197483902266, 0.32266029073649866, 0.31592003750359626, 0.307872864879158, 0.298626430344236, 0.2883020045789962, 0.27703182972760326, 0.26495631074668563, 0.25222112288771514, 0.23897431800009786, 0.22536350897011118, 0.21153320549335114, 0.19762236589096485, 0.18376221928813738, 0.1700744007045045, 0.15666942902010444, 0.14364554493953316, 0.1310879135181106, 0.11906818402392137, 0.1076443893047986, 0.09686115774030199, 0.0867502035211574, 0.077331055549729, 0.06861198173579104, 0.06059106382373267, 0.053257378003682014, 0.04659223823906354, 0.0405704622478734, 0.03516162413428328, 0.030331262496184168, 0.026042018148828342, 0.02225468113496958, 0.018929132193355087, 0.016025169119338187] + [0.0] * 3,
            "type": "arbitrary",
        },
        "6255663465574916415_q": {
            "samples": [-0.001507284886086783, -0.001730967726673968, -0.001976926464805784, -0.0022453228664481907, -0.0025358916171026257, -0.002847874475230854, -0.0031799583576094907, -0.0035302201866321734, -0.003896081514566676, -0.004274276017930893, -0.004660832905900805, -0.005051079093284066, -0.005439662639799255, -0.005820599448805021, -0.006187344553959861, -0.006532888514290232, -0.0068498785089285245, -0.0071307627037351575, -0.007367955393022458, -0.007554019347650789, -0.007681860777994114, -0.0077449314013975186, -0.007737431343153064, -0.007654506048534958, -0.0074924300850752355, -0.007248770703107037, -0.006922524320054752, -0.006514219706572249, -0.006025982570769481, -0.005461557434092855, -0.004826284126476641, -0.004127027842152673, -0.0033720634219953785, -0.002570916285915478, -0.0017341641475324464, -0.0008732052210973523, 0.0, 0.0008732052210973523, 0.0017341641475324464, 0.002570916285915478, 0.0033720634219953785, 0.004127027842152673, 0.004826284126476641, 0.005461557434092855, 0.006025982570769481, 0.006514219706572249, 0.006922524320054752, 0.007248770703107037, 0.0074924300850752355, 0.007654506048534958, 0.007737431343153064, 0.0077449314013975186, 0.007681860777994114, 0.007554019347650789, 0.007367955393022458, 0.0071307627037351575, 0.0068498785089285245, 0.006532888514290232, 0.006187344553959861, 0.005820599448805021, 0.005439662639799255, 0.005051079093284066, 0.004660832905900805, 0.004274276017930893, 0.003896081514566676, 0.0035302201866321734, 0.0031799583576094907, 0.002847874475230854, 0.0025358916171026257, 0.0022453228664481907, 0.001976926464805784, 0.001730967726673968, 0.001507284886086783] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4373329542280752208_i": {
            "samples": [0.01600689103586521, 0.018866216993554147, 0.022135021301713645, 0.025851892753078243, 0.030055366570318827, 0.03478315684995408, 0.04007128258908686, 0.04595309573996917, 0.05245822443960813, 0.05961144948750879, 0.06743153711262069, 0.0759300558694863, 0.08511020989968808, 0.09496572454070977, 0.10547982311083812, 0.11662433540706421, 0.1283589788091902, 0.1406308517126981, 0.1533741761934908, 0.1665103222827483, 0.17994814001851134, 0.19358461764290072, 0.2073058751155836, 0.22098849178368385, 0.23450115593062346, 0.24770661243097117, 0.2604638733235358, 0.27263064526751757, 0.284065918058832, 0.2946326501286176, 0.3042004806514514, 0.3126483939158908, 0.3198672602227703, 0.3257621789369635, 0.33025455346497773, 0.33328383477574686] + [0.33480887941094295] * 2 + [0.33328383477574686, 0.33025455346497773, 0.3257621789369635, 0.3198672602227703, 0.3126483939158908, 0.3042004806514514, 0.2946326501286176, 0.284065918058832, 0.27263064526751757, 0.2604638733235358, 0.24770661243097117, 0.23450115593062346, 0.22098849178368385, 0.2073058751155836, 0.19358461764290072, 0.17994814001851134, 0.1665103222827483, 0.1533741761934908, 0.1406308517126981, 0.1283589788091902, 0.11662433540706421, 0.10547982311083812, 0.09496572454070977, 0.08511020989968808, 0.0759300558694863, 0.06743153711262069, 0.05961144948750879, 0.05245822443960813, 0.04595309573996917, 0.04007128258908686, 0.03478315684995408, 0.030055366570318827, 0.025851892753078243, 0.022135021301713645, 0.018866216993554147, 0.01600689103586521] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4373329542280752208_q": {
            "samples": [-0.00148549897319633, -0.001702886416492852, -0.0019416526607858248, -0.002201961166486094, -0.0024835785088740308, -0.002785813584885731, -0.003107460276806339, -0.0034467461003043014, -0.0038012895332013466, -0.004168068798372383, -0.00454340484128512, -0.004922961085162406, -0.005301762254315467, -0.005674234124322456, -0.006034265488673571, -0.006375292935095152, -0.006690408218789962, -0.0069724871300001455, -0.007214337812701323, -0.007408865539273434, -0.007549250026810376, -0.0076291305411815185, -0.007642793322208881, -0.007585355322200696, -0.007452937920328851, -0.00724282418894869, -0.00695359346677222, -0.00658522744753098, -0.0061391827176153855, -0.00561842565422629, -0.005027426794928496, -0.004372113165324482, -0.003659778547961, -0.0028989532281684305, -0.0020992362917039036, -0.0012710950036430423, -0.00042563709906195203, 0.00042563709906195203, 0.0012710950036430423, 0.0020992362917039036, 0.0028989532281684305, 0.003659778547961, 0.004372113165324482, 0.005027426794928496, 0.00561842565422629, 0.0061391827176153855, 0.00658522744753098, 0.00695359346677222, 0.00724282418894869, 0.007452937920328851, 0.007585355322200696, 0.007642793322208881, 0.0076291305411815185, 0.007549250026810376, 0.007408865539273434, 0.007214337812701323, 0.0069724871300001455, 0.006690408218789962, 0.006375292935095152, 0.006034265488673571, 0.005674234124322456, 0.005301762254315467, 0.004922961085162406, 0.00454340484128512, 0.004168068798372383, 0.0038012895332013466, 0.0034467461003043014, 0.003107460276806339, 0.002785813584885731, 0.0024835785088740308, 0.002201961166486094, 0.0019416526607858248, 0.001702886416492852, 0.00148549897319633] + [0.0] * 2,
            "type": "arbitrary",
        },
        "4055065770593715150_i": {
            "samples": [0.01598911710065999, 0.0188051455494348, 0.02201905708653771, 0.02566791178046532, 0.029788741848894427, 0.03441783799233561, 0.03958993725589649, 0.04533731988426526, 0.05168882684302539, 0.05866881409562558, 0.06629606419301091, 0.07458268006942848, 0.08353298994039424, 0.09314249565182005, 0.10339689951426735, 0.11427124636235832, 0.12572921811521887, 0.13772261731990781, 0.1501910739202159, 0.16306200574659052, 0.17625085797130793, 0.1896616400882612, 0.2031877710037322, 0.21671323378055804, 0.23011403174822495, 0.24325992741968647, 0.2560164353324493, 0.26824702997713074, 0.27981552082277616, 0.2905885385164426, 0.30043807001520106, 0.30924397603952297, 0.31689642208376645, 0.32329815445954296, 0.328366555557763, 0.33203541766357547, 0.33425638210367814, 0.335, 0.33425638210367814, 0.33203541766357547, 0.328366555557763, 0.32329815445954296, 0.31689642208376645, 0.30924397603952297, 0.30043807001520106, 0.2905885385164426, 0.27981552082277616, 0.26824702997713074, 0.2560164353324493, 0.24325992741968647, 0.23011403174822495, 0.21671323378055804, 0.2031877710037322, 0.1896616400882612, 0.17625085797130793, 0.16306200574659052, 0.1501910739202159, 0.13772261731990781, 0.12572921811521887, 0.11427124636235832, 0.10339689951426735, 0.09314249565182005, 0.08353298994039424, 0.07458268006942848, 0.06629606419301091, 0.05866881409562558, 0.05168882684302539, 0.04533731988426526, 0.03958993725589649, 0.03441783799233561, 0.029788741848894427, 0.02566791178046532, 0.02201905708653771, 0.0188051455494348, 0.01598911710065999, 0.0],
            "type": "arbitrary",
        },
        "4055065770593715150_q": {
            "samples": [-0.0014643322352453987, -0.001675685900795748, -0.0019075686542675665, -0.0021601448329529403, -0.0024332095722665397, -0.0027261326230817442, -0.0030378052120239546, -0.0033665922052299397, -0.0037102919903156755, -0.004066106566217693, -0.004430624310555409, -0.004799817766176205, -0.005169058543284902, -0.005533151066495384, -0.005886386408430792, -0.006222616850668538, -0.0065353511131626815, -0.006817869415846429, -0.007063356708386242, -0.007265051559073134, -0.007416407368985848, -0.007511261812943273, -0.00754400974523217, -0.0075097742850668845, -0.007404570449891242, -0.007225455563641678, -0.006970660753519906, -0.006639698174354824, -0.006233439164748151, -0.00575415933243489, -0.005205547564160092, -0.004592677122982274, -0.003921938288279545, -0.0032009333577640263, -0.002438336207832688, -0.0016437199373055028, -0.0008273573393187059, 0.0, 0.0008273573393187059, 0.0016437199373055028, 0.002438336207832688, 0.0032009333577640263, 0.003921938288279545, 0.004592677122982274, 0.005205547564160092, 0.00575415933243489, 0.006233439164748151, 0.006639698174354824, 0.006970660753519906, 0.007225455563641678, 0.007404570449891242, 0.0075097742850668845, 0.00754400974523217, 0.007511261812943273, 0.007416407368985848, 0.007265051559073134, 0.007063356708386242, 0.006817869415846429, 0.0065353511131626815, 0.006222616850668538, 0.005886386408430792, 0.005533151066495384, 0.005169058543284902, 0.004799817766176205, 0.004430624310555409, 0.004066106566217693, 0.0037102919903156755, 0.0033665922052299397, 0.0030378052120239546, 0.0027261326230817442, 0.0024332095722665397, 0.0021601448329529403, 0.0019075686542675665, 0.001675685900795748, 0.0014643322352453987, 0.0],
            "type": "arbitrary",
        },
        "1702700101831420930_i": {
            "samples": [0.015971826750633567, 0.018745838318564814, 0.021906621570778002, 0.025489787088834318, 0.029530940093187952, 0.03406501622130355, 0.03912552610476153, 0.04474371535276346, 0.05094765032040883, 0.05776124400440721, 0.06520324043097167, 0.07328617982224232, 0.08201537047242512, 0.09138789644495696, 0.10139169272570417, 0.11200472114811168, 0.1231942810733752, 0.1349164883169264, 0.14711595405267008, 0.1597256923348375, 0.1726672804438833, 0.18585129053685806, 0.19917800417623904, 0.2125384133994536, 0.22581550330940284, 0.238885802002683, 0.25162117433882675, 0.2638908269530294, 0.2755634834035527, 0.28650968079773953, 0.2966041330107517, 0.305728101012872, 0.31377170811209554, 0.32063613728479784, 0.3262356493109964, 0.33049936416304193, 0.3333727539332711] + [0.3348188033492549] * 2 + [0.3333727539332711, 0.33049936416304193, 0.3262356493109964, 0.32063613728479784, 0.31377170811209554, 0.305728101012872, 0.2966041330107517, 0.28650968079773953, 0.2755634834035527, 0.2638908269530294, 0.25162117433882675, 0.238885802002683, 0.22581550330940284, 0.2125384133994536, 0.19917800417623904, 0.18585129053685806, 0.1726672804438833, 0.1597256923348375, 0.14711595405267008, 0.1349164883169264, 0.1231942810733752, 0.11200472114811168, 0.10139169272570417, 0.09138789644495696, 0.08201537047242512, 0.07328617982224232, 0.06520324043097167, 0.05776124400440721, 0.05094765032040883, 0.04474371535276346, 0.03912552610476153, 0.03406501622130355, 0.029530940093187952, 0.025489787088834318, 0.021906621570778002, 0.018745838318564814, 0.015971826750633567],
            "type": "arbitrary",
        },
        "1702700101831420930_q": {
            "samples": [-0.0014437587064907343, -0.0016493259391451099, -0.0018746168523406368, -0.0021197959633433073, -0.002384683997988934, -0.0026687059191312368, -0.0029708416367797714, -0.0032895814245941573, -0.0036228882081361627, -0.003968168962488957, -0.0043222574468875855, -0.00468141040036377, -0.0050413191166772614, -0.005397138004557326, -0.005743531320853083, -0.006074738745306208, -0.0063846598577689175, -0.006666956899056552, -0.006915174468053886, -0.007122874057915988, -0.007283780594891628, -0.007391937448756321, -0.007441865769419321, -0.007428723504540861, -0.007348459099847036, -0.007197954704517736, -0.006975153719360208, -0.006679167748246554, -0.006310358447000007, -0.005870390402021737, -0.0053622519966092415, -0.004790242209293641, -0.004159922399703141, -0.003478033329922932, -0.0027523788939104515, -0.0019916792318120016, -0.0012053970369516084, -0.0004035418698850424, 0.0004035418698850424, 0.0012053970369516084, 0.0019916792318120016, 0.0027523788939104515, 0.003478033329922932, 0.004159922399703141, 0.004790242209293641, 0.0053622519966092415, 0.005870390402021737, 0.006310358447000007, 0.006679167748246554, 0.006975153719360208, 0.007197954704517736, 0.007348459099847036, 0.007428723504540861, 0.007441865769419321, 0.007391937448756321, 0.007283780594891628, 0.007122874057915988, 0.006915174468053886, 0.006666956899056552, 0.0063846598577689175, 0.006074738745306208, 0.005743531320853083, 0.005397138004557326, 0.0050413191166772614, 0.00468141040036377, 0.0043222574468875855, 0.003968168962488957, 0.0036228882081361627, 0.0032895814245941573, 0.0029708416367797714, 0.0026687059191312368, 0.002384683997988934, 0.0021197959633433073, 0.0018746168523406368, 0.0016493259391451099, 0.0014437587064907343],
            "type": "arbitrary",
        },
        "-5964654954690129439_i": {
            "samples": [0.01595500052542091, 0.018688220252372753, 0.021797557655395837, 0.025317248028875385, 0.02928154093972213, 0.03372408142392077, 0.038677206642175575, 0.044171163850196773, 0.050233258923064815, 0.056886948236158225, 0.06415089032991214, 0.07203797733481726, 0.08055436945314527, 0.08969855872072248, 0.09946049063735012, 0.10982077389342855, 0.12075000918027008, 0.13220826782069808, 0.14414474959280488, 0.1564976465791464, 0.1691942361372918, 0.18215122118723745, 0.19527533003244837, 0.20846418101476213, 0.2216074096425405, 0.2345880476677823, 0.2472841352031804, 0.25957053867588853, 0.2713209395396829, 0.2824099515424439, 0.2927153182896367, 0.3021201381461697, 0.31051506042419413, 0.31780039550105493, 0.3238880821188577, 0.3287034576770394, 0.3321867818022852, 0.3342944697442287, 0.335, 0.3342944697442287, 0.3321867818022852, 0.3287034576770394, 0.3238880821188577, 0.31780039550105493, 0.31051506042419413, 0.3021201381461697, 0.2927153182896367, 0.2824099515424439, 0.2713209395396829, 0.25957053867588853, 0.2472841352031804, 0.2345880476677823, 0.2216074096425405, 0.20846418101476213, 0.19527533003244837, 0.18215122118723745, 0.1691942361372918, 0.1564976465791464, 0.14414474959280488, 0.13220826782069808, 0.12075000918027008, 0.10982077389342855, 0.09946049063735012, 0.08969855872072248, 0.08055436945314527, 0.07203797733481726, 0.06415089032991214, 0.056886948236158225, 0.050233258923064815, 0.044171163850196773, 0.038677206642175575, 0.03372408142392077, 0.02928154093972213, 0.025317248028875385, 0.021797557655395837, 0.018688220252372753, 0.01595500052542091] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5964654954690129439_q": {
            "samples": [-0.0014237538500570985, -0.0016237686789753766, -0.0018427432450170858, -0.002080841653074586, -0.0023379075679485135, -0.0026134160931728634, -0.0029064280157850546, -0.003215548233004371, -0.0035388903051697938, -0.0038740491483587073, -0.004218083877933409, -0.004567512730683191, -0.004918321820654453, -0.005265989217930894, -0.005605525480288301, -0.005931531319092373, -0.006238272552199696, -0.006519771902105175, -0.006769916556099109, -0.0069825797400297086, -0.007151753895249836, -0.007271692418806617, -0.00733705636046492, -0.007343061997014591, -0.007285624852878525, -0.007161495531165945, -0.006968382680750347, -0.006705058565933698, -0.006371443031379589, -0.005968662163414641, -0.0054990786278676885, -0.004966291494005826, -0.004375104305406069, -0.0037314611963237794, -0.003042351935334166, -0.0023156878621604926, -0.0015601517226214866, -0.0007850253553206056, 0.0, 0.0007850253553206056, 0.0015601517226214866, 0.0023156878621604926, 0.003042351935334166, 0.0037314611963237794, 0.004375104305406069, 0.004966291494005826, 0.0054990786278676885, 0.005968662163414641, 0.006371443031379589, 0.006705058565933698, 0.006968382680750347, 0.007161495531165945, 0.007285624852878525, 0.007343061997014591, 0.00733705636046492, 0.007271692418806617, 0.007151753895249836, 0.0069825797400297086, 0.006769916556099109, 0.006519771902105175, 0.006238272552199696, 0.005931531319092373, 0.005605525480288301, 0.005265989217930894, 0.004918321820654453, 0.004567512730683191, 0.004218083877933409, 0.0038740491483587073, 0.0035388903051697938, 0.003215548233004371, 0.0029064280157850546, 0.0026134160931728634, 0.0023379075679485135, 0.002080841653074586, 0.0018427432450170858, 0.0016237686789753766, 0.0014237538500570985] + [0.0] * 3,
            "type": "arbitrary",
        },
        "3900459789834587793_i": {
            "samples": [0.015938619994475607, 0.018632220484242054, 0.021691717354498864, 0.025150040151731633, 0.02904014980138288, 0.03339446157172324, 0.038244189603245146, 0.04361861819906233, 0.0495443081123884, 0.05604424927349826, 0.06313697466875424, 0.07083565329887223, 0.07914718316888532, 0.08807130795463633, 0.09759978320218574, 0.1077156195015173, 0.11839243089800457, 0.12959391674488052, 0.14127350416260492, 0.1533741761934908, 0.16582850759724396, 0.17855892604330395, 0.19147821128357734, 0.20449023884649972, 0.2174909680391135, 0.23036966677978418, 0.24301035824912698, 0.25529346680814324, 0.2670976333762239, 0.2783016637795294, 0.28878656775738754, 0.2984376416154312, 0.3071465441702297, 0.3148133138262399, 0.3213482744907335, 0.32667377963011773, 0.33072574709621244, 0.333454942326377] + [0.33482797399961145] * 2 + [0.333454942326377, 0.33072574709621244, 0.32667377963011773, 0.3213482744907335, 0.3148133138262399, 0.3071465441702297, 0.2984376416154312, 0.28878656775738754, 0.2783016637795294, 0.2670976333762239, 0.25529346680814324, 0.24301035824912698, 0.23036966677978418, 0.2174909680391135, 0.20449023884649972, 0.19147821128357734, 0.17855892604330395, 0.16582850759724396, 0.1533741761934908, 0.14127350416260492, 0.12959391674488052, 0.11839243089800457, 0.1077156195015173, 0.09759978320218574, 0.08807130795463633, 0.07914718316888532, 0.07083565329887223, 0.06313697466875424, 0.05604424927349826, 0.0495443081123884, 0.04361861819906233, 0.038244189603245146, 0.03339446157172324, 0.02904014980138288, 0.025150040151731633, 0.021691717354498864, 0.018632220484242054, 0.015938619994475607] + [0.0] * 2,
            "type": "arbitrary",
        },
        "3900459789834587793_q": {
            "samples": [-0.0014042944611662893, -0.0015989784826439257, -0.0018118971353209142, -0.0020432136100095987, -0.0022927921408016716, -0.0025601534081131166, -0.0028444320313298203, -0.0031443377820499644, -0.0034581222660301832, -0.003783552887617584, -0.004117895914250519, -0.00445791039156016, -0.004799854514864519, -0.005139505836369415, -0.005472196378502239, -0.0057928633356701216, -0.006096115586671624, -0.0063763157195856155, -0.006627676705955041, -0.006844371771024331, -0.007020655414423563, -0.007150992966122071, -0.007230195542097171, -0.007253556819444006, -0.007216987706776465, -0.007117144765255057, -0.00695154815692476, -0.006718684973494292, -0.006418094037185284, -0.006050428665713883, -0.00561749444824367, -0.005122259773145721, -0.004568837659333893, -0.00396243834213308, -0.0033092930181671085, -0.002616550123946141, -0.0018921464700013455, -0.0011446564367614345, -0.0003831232219587433, 0.0003831232219587433, 0.0011446564367614345, 0.0018921464700013455, 0.002616550123946141, 0.0033092930181671085, 0.00396243834213308, 0.004568837659333893, 0.005122259773145721, 0.00561749444824367, 0.006050428665713883, 0.006418094037185284, 0.006718684973494292, 0.00695154815692476, 0.007117144765255057, 0.007216987706776465, 0.007253556819444006, 0.007230195542097171, 0.007150992966122071, 0.007020655414423563, 0.006844371771024331, 0.006627676705955041, 0.0063763157195856155, 0.006096115586671624, 0.0057928633356701216, 0.005472196378502239, 0.005139505836369415, 0.004799854514864519, 0.00445791039156016, 0.004117895914250519, 0.003783552887617584, 0.0034581222660301832, 0.0031443377820499644, 0.0028444320313298203, 0.0025601534081131166, 0.0022927921408016716, 0.0020432136100095987, 0.0018118971353209142, 0.0015989784826439257, 0.0014042944611662893] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3766895266686962576_i": {
            "samples": [0.01592266768987036, 0.01857777204315171, 0.021588961148611543, 0.02498792402839221, 0.028806395952771204, 0.033075619856025106, 0.037825734921811356, 0.043085096953268745, 0.04887953787869817, 0.055231574632477354, 0.0621595806042154, 0.06967693576306537, 0.0777911743218606, 0.08650315128156519, 0.09580625126032391, 0.10568566453417727, 0.11611775607654642, 0.12706955347289367, 0.13849837881782598, 0.1503516480131679, 0.16256685824817907, 0.17507178086481573, 0.1877848723393205, 0.20061591083541075, 0.2134668598338051, 0.22623295388607134, 0.2388039947798945, 0.2510658395671019, 0.2629020552430802, 0.2741957086332468, 0.2848312544933537, 0.2946964802061052, 0.30368446197193943, 0.3116954852256655, 0.3186388812958499, 0.32443473313960525, 0.3290154053517367, 0.33232685752204755, 0.3343297052940832, 0.335, 0.3343297052940832, 0.33232685752204755, 0.3290154053517367, 0.32443473313960525, 0.3186388812958499, 0.3116954852256655, 0.30368446197193943, 0.2946964802061052, 0.2848312544933537, 0.2741957086332468, 0.2629020552430802, 0.2510658395671019, 0.2388039947798945, 0.22623295388607134, 0.2134668598338051, 0.20061591083541075, 0.1877848723393205, 0.17507178086481573, 0.16256685824817907, 0.1503516480131679, 0.13849837881782598, 0.12706955347289367, 0.11611775607654642, 0.10568566453417727, 0.09580625126032391, 0.08650315128156519, 0.0777911743218606, 0.06967693576306537, 0.0621595806042154, 0.055231574632477354, 0.04887953787869817, 0.043085096953268745, 0.037825734921811356, 0.033075619856025106, 0.028806395952771204, 0.02498792402839221, 0.021588961148611543, 0.01857777204315171, 0.01592266768987036, 0.0],
            "type": "arbitrary",
        },
        "-3766895266686962576_q": {
            "samples": [-0.0013853585781125664, -0.0015749217691863823, -0.0017820308930980022, -0.002006847803465706, -0.0022492551838088452, -0.002508815179585385, -0.002784729877642327, -0.003075805099900944, -0.003380419084923245, -0.0036964976931522773, -0.0040214977799400715, -0.004352400327036788, -0.004685714801861693, -0.005017496020800731, -0.005343374527009357, -0.005658601157029207, -0.0059581060697765365, -0.006236572055613813, -0.006488521445359386, -0.00670841541564537, -0.006890763957287167, -0.007030244258750277, -0.007121824780187323, -0.0071608918779747024, -0.007143375507495718, -0.007065870303399493, -0.006925748228867062, -0.006721259011459795, -0.006451614750665633, -0.006117055393160644, -0.005718892221587521, -0.005259527080349461, -0.004742445750259665, -0.004172184659841816, -0.0035542709567138657, -0.002895136826134297, -0.0022020098014353937, -0.0014827816279330938, -0.0007458589841019147, 0.0, 0.0007458589841019147, 0.0014827816279330938, 0.0022020098014353937, 0.002895136826134297, 0.0035542709567138657, 0.004172184659841816, 0.004742445750259665, 0.005259527080349461, 0.005718892221587521, 0.006117055393160644, 0.006451614750665633, 0.006721259011459795, 0.006925748228867062, 0.007065870303399493, 0.007143375507495718, 0.0071608918779747024, 0.007121824780187323, 0.007030244258750277, 0.006890763957287167, 0.00670841541564537, 0.006488521445359386, 0.006236572055613813, 0.0059581060697765365, 0.005658601157029207, 0.005343374527009357, 0.005017496020800731, 0.004685714801861693, 0.004352400327036788, 0.0040214977799400715, 0.0036964976931522773, 0.003380419084923245, 0.003075805099900944, 0.002784729877642327, 0.002508815179585385, 0.0022492551838088452, 0.002006847803465706, 0.0017820308930980022, 0.0015749217691863823, 0.0013853585781125664, 0.0],
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
                "305353331920272181": "305353331920272181_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_383",
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
                "8451993279042197805": "8451993279042197805",
                "2501332154477808784": "2501332154477808784",
                "8453401411484346734": "8453401411484346734",
                "-6851736067330374729": "-6851736067330374729",
                "-7795582974222038019": "-7795582974222038019",
                "1076598818480614836": "1076598818480614836",
                "-8292948355003096375": "-8292948355003096375",
                "7801430049944161021": "7801430049944161021",
                "7524235646528158807": "7524235646528158807",
                "-143119409993391562": "-143119409993391562",
                "8729062382709261293": "8729062382709261293",
                "3757872592209918210": "3757872592209918210",
                "-3491538922151461600": "-3491538922151461600",
                "-3270044862952746352": "-3270044862952746352",
                "4935484426274245427": "4935484426274245427",
                "-2065218126771643866": "-2065218126771643866",
                "7133244114277412290": "7133244114277412290",
                "1513252736426696160": "1513252736426696160",
                "-6080290142405374980": "-6080290142405374980",
                "-7839815485381487353": "-7839815485381487353",
                "3013385709495993123": "3013385709495993123",
                "-3661036395203492869": "-3661036395203492869",
                "861281374886510447": "861281374886510447",
                "-5473855866811585348": "-5473855866811585348",
                "2066108111067612933": "2066108111067612933",
                "4612752936911847132": "4612752936911847132",
                "1246221591281584831": "1246221591281584831",
                "8513744939115156904": "8513744939115156904",
                "6576965080401429237": "6576965080401429237",
                "-2004664248783405147": "-2004664248783405147",
                "-1783170189584689899": "-1783170189584689899",
                "8898685155510231288": "8898685155510231288",
                "9120179214708946536": "9120179214708946536",
                "636083557617192212": "636083557617192212",
                "-1398229973189615515": "-1398229973189615515",
                "5869293374643956558": "5869293374643956558",
                "2502762029013694257": "2502762029013694257",
                "8067053062647123421": "8067053062647123421",
                "-4525155426148970305": "-4525155426148970305",
                "6254233591039030942": "6254233591039030942",
                "3059048095191327930": "3059048095191327930",
                "8673487338240913053": "8673487338240913053",
                "7525665521064044280": "7525665521064044280",
                "-7113906646402883685": "-7113906646402883685",
                "8730492257245146766": "8730492257245146766",
                "-2342287230438707354": "-2342287230438707354",
                "-4694652899201001574": "-4694652899201001574",
                "-8061184244831263875": "-8061184244831263875",
                "538556917825762772": "538556917825762772",
                "-8116884589048550841": "-8116884589048550841",
                "2736316605828929635": "2736316605828929635",
                "2957810665027644883": "2957810665027644883",
                "-408720680602617418": "-408720680602617418",
                "5155570353030811746": "5155570353030811746",
                "-3038280752780913852": "-3038280752780913852",
                "3342750881422719267": "3342750881422719267",
                "-3535646133561972208": "-3535646133561972208",
                "5540510569425886130": "5540510569425886130",
                "5762004628624601378": "5762004628624601378",
                "4614182811447732605": "4614182811447732605",
                "-3053172245073817764": "-3053172245073817764",
                "6811942499450899468": "6811942499450899468",
                "-855412557070650901": "-855412557070650901",
                "-6401591757231887802": "-6401591757231887802",
                "-6180097698033172554": "-6180097698033172554",
                "2025431591193819225": "2025431591193819225",
                "-3982338010030005691": "-3982338010030005691",
                "6797051007157995556": "6797051007157995556",
                "-5795157481638098170": "-5795157481638098170",
                "-8990342977485801182": "-8990342977485801182",
                "-3597397793634931307": "-3597397793634931307",
                "-3375903734436216059": "-3375903734436216059",
                "-6571089230283919071": "-6571089230283919071",
                "6255663465574916415": "6255663465574916415",
                "-4373329542280752208": "-4373329542280752208",
                "4055065770593715150": "4055065770593715150",
                "1702700101831420930": "1702700101831420930",
                "-5964654954690129439": "-5964654954690129439",
                "3900459789834587793": "3900459789834587793",
                "-3766895266686962576": "-3766895266686962576",
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
                "mixer": "B4/drive_mixer_b5e",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "8451993279042197805": {
            "length": 40,
            "waveforms": {
                "I": "8451993279042197805_i",
                "Q": "8451993279042197805_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "305353331920272181_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "7245105225113558137_i",
                "Q": "7245105225113558137_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "2501332154477808784": {
            "length": 16,
            "waveforms": {
                "I": "2501332154477808784_i",
                "Q": "2501332154477808784_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8453401411484346734": {
            "length": 16,
            "waveforms": {
                "I": "8453401411484346734_i",
                "Q": "8453401411484346734_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6851736067330374729": {
            "length": 16,
            "waveforms": {
                "I": "-6851736067330374729_i",
                "Q": "-6851736067330374729_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7795582974222038019": {
            "length": 16,
            "waveforms": {
                "I": "-7795582974222038019_i",
                "Q": "-7795582974222038019_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1076598818480614836": {
            "length": 16,
            "waveforms": {
                "I": "1076598818480614836_i",
                "Q": "1076598818480614836_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8292948355003096375": {
            "length": 16,
            "waveforms": {
                "I": "-8292948355003096375_i",
                "Q": "-8292948355003096375_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7801430049944161021": {
            "length": 16,
            "waveforms": {
                "I": "7801430049944161021_i",
                "Q": "7801430049944161021_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7524235646528158807": {
            "length": 16,
            "waveforms": {
                "I": "7524235646528158807_i",
                "Q": "7524235646528158807_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-143119409993391562": {
            "length": 16,
            "waveforms": {
                "I": "-143119409993391562_i",
                "Q": "-143119409993391562_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8729062382709261293": {
            "length": 16,
            "waveforms": {
                "I": "8729062382709261293_i",
                "Q": "8729062382709261293_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3757872592209918210": {
            "length": 16,
            "waveforms": {
                "I": "3757872592209918210_i",
                "Q": "3757872592209918210_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3491538922151461600": {
            "length": 16,
            "waveforms": {
                "I": "-3491538922151461600_i",
                "Q": "-3491538922151461600_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3270044862952746352": {
            "length": 16,
            "waveforms": {
                "I": "-3270044862952746352_i",
                "Q": "-3270044862952746352_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4935484426274245427": {
            "length": 16,
            "waveforms": {
                "I": "4935484426274245427_i",
                "Q": "4935484426274245427_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2065218126771643866": {
            "length": 16,
            "waveforms": {
                "I": "-2065218126771643866_i",
                "Q": "-2065218126771643866_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7133244114277412290": {
            "length": 16,
            "waveforms": {
                "I": "7133244114277412290_i",
                "Q": "7133244114277412290_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1513252736426696160": {
            "length": 16,
            "waveforms": {
                "I": "1513252736426696160_i",
                "Q": "1513252736426696160_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6080290142405374980": {
            "length": 20,
            "waveforms": {
                "I": "-6080290142405374980_i",
                "Q": "-6080290142405374980_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7839815485381487353": {
            "length": 20,
            "waveforms": {
                "I": "-7839815485381487353_i",
                "Q": "-7839815485381487353_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3013385709495993123": {
            "length": 20,
            "waveforms": {
                "I": "3013385709495993123_i",
                "Q": "3013385709495993123_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3661036395203492869": {
            "length": 20,
            "waveforms": {
                "I": "-3661036395203492869_i",
                "Q": "-3661036395203492869_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "861281374886510447": {
            "length": 24,
            "waveforms": {
                "I": "861281374886510447_i",
                "Q": "861281374886510447_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5473855866811585348": {
            "length": 24,
            "waveforms": {
                "I": "-5473855866811585348_i",
                "Q": "-5473855866811585348_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2066108111067612933": {
            "length": 24,
            "waveforms": {
                "I": "2066108111067612933_i",
                "Q": "2066108111067612933_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4612752936911847132": {
            "length": 24,
            "waveforms": {
                "I": "4612752936911847132_i",
                "Q": "4612752936911847132_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1246221591281584831": {
            "length": 28,
            "waveforms": {
                "I": "1246221591281584831_i",
                "Q": "1246221591281584831_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8513744939115156904": {
            "length": 28,
            "waveforms": {
                "I": "8513744939115156904_i",
                "Q": "8513744939115156904_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6576965080401429237": {
            "length": 28,
            "waveforms": {
                "I": "6576965080401429237_i",
                "Q": "6576965080401429237_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2004664248783405147": {
            "length": 28,
            "waveforms": {
                "I": "-2004664248783405147_i",
                "Q": "-2004664248783405147_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1783170189584689899": {
            "length": 32,
            "waveforms": {
                "I": "-1783170189584689899_i",
                "Q": "-1783170189584689899_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8898685155510231288": {
            "length": 32,
            "waveforms": {
                "I": "8898685155510231288_i",
                "Q": "8898685155510231288_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9120179214708946536": {
            "length": 32,
            "waveforms": {
                "I": "9120179214708946536_i",
                "Q": "9120179214708946536_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "636083557617192212": {
            "length": 32,
            "waveforms": {
                "I": "636083557617192212_i",
                "Q": "636083557617192212_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1398229973189615515": {
            "length": 36,
            "waveforms": {
                "I": "-1398229973189615515_i",
                "Q": "-1398229973189615515_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5869293374643956558": {
            "length": 36,
            "waveforms": {
                "I": "5869293374643956558_i",
                "Q": "5869293374643956558_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2502762029013694257": {
            "length": 36,
            "waveforms": {
                "I": "2502762029013694257_i",
                "Q": "2502762029013694257_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8067053062647123421": {
            "length": 36,
            "waveforms": {
                "I": "8067053062647123421_i",
                "Q": "8067053062647123421_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4525155426148970305": {
            "length": 40,
            "waveforms": {
                "I": "-4525155426148970305_i",
                "Q": "-4525155426148970305_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6254233591039030942": {
            "length": 40,
            "waveforms": {
                "I": "6254233591039030942_i",
                "Q": "6254233591039030942_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3059048095191327930": {
            "length": 40,
            "waveforms": {
                "I": "3059048095191327930_i",
                "Q": "3059048095191327930_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8673487338240913053": {
            "length": 44,
            "waveforms": {
                "I": "8673487338240913053_i",
                "Q": "8673487338240913053_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7525665521064044280": {
            "length": 44,
            "waveforms": {
                "I": "7525665521064044280_i",
                "Q": "7525665521064044280_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7113906646402883685": {
            "length": 44,
            "waveforms": {
                "I": "-7113906646402883685_i",
                "Q": "-7113906646402883685_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8730492257245146766": {
            "length": 44,
            "waveforms": {
                "I": "8730492257245146766_i",
                "Q": "8730492257245146766_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2342287230438707354": {
            "length": 48,
            "waveforms": {
                "I": "-2342287230438707354_i",
                "Q": "-2342287230438707354_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4694652899201001574": {
            "length": 48,
            "waveforms": {
                "I": "-4694652899201001574_i",
                "Q": "-4694652899201001574_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8061184244831263875": {
            "length": 48,
            "waveforms": {
                "I": "-8061184244831263875_i",
                "Q": "-8061184244831263875_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "538556917825762772": {
            "length": 48,
            "waveforms": {
                "I": "538556917825762772_i",
                "Q": "538556917825762772_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8116884589048550841": {
            "length": 52,
            "waveforms": {
                "I": "-8116884589048550841_i",
                "Q": "-8116884589048550841_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2736316605828929635": {
            "length": 52,
            "waveforms": {
                "I": "2736316605828929635_i",
                "Q": "2736316605828929635_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2957810665027644883": {
            "length": 52,
            "waveforms": {
                "I": "2957810665027644883_i",
                "Q": "2957810665027644883_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-408720680602617418": {
            "length": 52,
            "waveforms": {
                "I": "-408720680602617418_i",
                "Q": "-408720680602617418_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5155570353030811746": {
            "length": 56,
            "waveforms": {
                "I": "5155570353030811746_i",
                "Q": "5155570353030811746_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3038280752780913852": {
            "length": 56,
            "waveforms": {
                "I": "-3038280752780913852_i",
                "Q": "-3038280752780913852_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3342750881422719267": {
            "length": 56,
            "waveforms": {
                "I": "3342750881422719267_i",
                "Q": "3342750881422719267_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3535646133561972208": {
            "length": 56,
            "waveforms": {
                "I": "-3535646133561972208_i",
                "Q": "-3535646133561972208_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5540510569425886130": {
            "length": 60,
            "waveforms": {
                "I": "5540510569425886130_i",
                "Q": "5540510569425886130_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5762004628624601378": {
            "length": 60,
            "waveforms": {
                "I": "5762004628624601378_i",
                "Q": "5762004628624601378_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4614182811447732605": {
            "length": 60,
            "waveforms": {
                "I": "4614182811447732605_i",
                "Q": "4614182811447732605_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3053172245073817764": {
            "length": 60,
            "waveforms": {
                "I": "-3053172245073817764_i",
                "Q": "-3053172245073817764_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6811942499450899468": {
            "length": 64,
            "waveforms": {
                "I": "6811942499450899468_i",
                "Q": "6811942499450899468_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-855412557070650901": {
            "length": 64,
            "waveforms": {
                "I": "-855412557070650901_i",
                "Q": "-855412557070650901_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6401591757231887802": {
            "length": 64,
            "waveforms": {
                "I": "-6401591757231887802_i",
                "Q": "-6401591757231887802_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6180097698033172554": {
            "length": 64,
            "waveforms": {
                "I": "-6180097698033172554_i",
                "Q": "-6180097698033172554_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2025431591193819225": {
            "length": 68,
            "waveforms": {
                "I": "2025431591193819225_i",
                "Q": "2025431591193819225_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3982338010030005691": {
            "length": 68,
            "waveforms": {
                "I": "-3982338010030005691_i",
                "Q": "-3982338010030005691_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6797051007157995556": {
            "length": 68,
            "waveforms": {
                "I": "6797051007157995556_i",
                "Q": "6797051007157995556_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5795157481638098170": {
            "length": 68,
            "waveforms": {
                "I": "-5795157481638098170_i",
                "Q": "-5795157481638098170_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8990342977485801182": {
            "length": 72,
            "waveforms": {
                "I": "-8990342977485801182_i",
                "Q": "-8990342977485801182_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3597397793634931307": {
            "length": 72,
            "waveforms": {
                "I": "-3597397793634931307_i",
                "Q": "-3597397793634931307_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3375903734436216059": {
            "length": 72,
            "waveforms": {
                "I": "-3375903734436216059_i",
                "Q": "-3375903734436216059_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6571089230283919071": {
            "length": 72,
            "waveforms": {
                "I": "-6571089230283919071_i",
                "Q": "-6571089230283919071_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6255663465574916415": {
            "length": 76,
            "waveforms": {
                "I": "6255663465574916415_i",
                "Q": "6255663465574916415_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4373329542280752208": {
            "length": 76,
            "waveforms": {
                "I": "-4373329542280752208_i",
                "Q": "-4373329542280752208_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4055065770593715150": {
            "length": 76,
            "waveforms": {
                "I": "4055065770593715150_i",
                "Q": "4055065770593715150_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1702700101831420930": {
            "length": 76,
            "waveforms": {
                "I": "1702700101831420930_i",
                "Q": "1702700101831420930_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5964654954690129439": {
            "length": 80,
            "waveforms": {
                "I": "-5964654954690129439_i",
                "Q": "-5964654954690129439_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3900459789834587793": {
            "length": 80,
            "waveforms": {
                "I": "3900459789834587793_i",
                "Q": "3900459789834587793_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3766895266686962576": {
            "length": 80,
            "waveforms": {
                "I": "-3766895266686962576_i",
                "Q": "-3766895266686962576_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "8451993279042197805_i": {
            "type": "arbitrary",
            "samples": [0.017174528874170345, 0.0231108546822752, 0.030616908044275828, 0.03993197601488685, 0.051273672141679986, 0.06481599483836066, 0.08066480888120327, 0.09883258981843836, 0.11921485946761638, 0.14157114847976826, 0.16551344113309885, 0.19050480299575512, 0.21587022281644042, 0.2408206358525739, 0.264489725836364, 0.2859815810506245, 0.3044258083809585, 0.3190355079648841, 0.32916278210089667] + [0.3343463416710043] * 2 + [0.32916278210089667, 0.3190355079648841, 0.3044258083809585, 0.2859815810506245, 0.264489725836364, 0.2408206358525739, 0.21587022281644042, 0.19050480299575512, 0.16551344113309885, 0.14157114847976826, 0.11921485946761638, 0.09883258981843836, 0.08066480888120327, 0.06481599483836066, 0.051273672141679986, 0.03993197601488685, 0.030616908044275828, 0.0231108546822752, 0.017174528874170345],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8451993279042197805_q": {
            "type": "arbitrary",
            "samples": [-0.0029143076986720266, -0.0037205204408097114, -0.004662462354279371, -0.005733511732295232, -0.006915794500772051, -0.008178358673214188, -0.009476191692004622, -0.010750437744539836, -0.01193010294582253, -0.012935404501678717, -0.013682732391426474, -0.01409096755751043, -0.014088668902948038, -0.013621439792345822, -0.012658651849910958, -0.011198672300041734, -0.00927183025271327, -0.006940567626477934, -0.004296530935752181, -0.0014547304842873624, 0.0014547304842873624, 0.004296530935752181, 0.006940567626477934, 0.00927183025271327, 0.011198672300041734, 0.012658651849910958, 0.013621439792345822, 0.014088668902948038, 0.01409096755751043, 0.013682732391426474, 0.012935404501678717, 0.01193010294582253, 0.010750437744539836, 0.009476191692004622, 0.008178358673214188, 0.006915794500772051, 0.005733511732295232, 0.004662462354279371, 0.0037205204408097114, 0.0029143076986720266],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7245105225113558137_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "7245105225113558137_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2501332154477808784_i": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2501332154477808784_q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8453401411484346734_i": {
            "type": "arbitrary",
            "samples": [0.335] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8453401411484346734_q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6851736067330374729_i": {
            "type": "arbitrary",
            "samples": [0.1533741761934908] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6851736067330374729_q": {
            "type": "arbitrary",
            "samples": [-0.266930499069949, 0.266930499069949] + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7795582974222038019_i": {
            "type": "arbitrary",
            "samples": [0.08353298994039425, 0.335, 0.08353298994039425] + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7795582974222038019_q": {
            "type": "arbitrary",
            "samples": [-0.12922646358212256, 0.0, 0.12922646358212256] + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1076598818480614836_i": {
            "type": "arbitrary",
            "samples": [0.057761244004407214] + [0.2755634834035527] * 2 + [0.057761244004407214] + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1076598818480614836_q": {
            "type": "arbitrary",
            "samples": [-0.07539521028729018, -0.1198968104930001, 0.1198968104930001, 0.07539521028729018] + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8292948355003096375_i": {
            "type": "arbitrary",
            "samples": [0.04533731988426526, 0.2031877710037322, 0.335, 0.2031877710037322, 0.04533731988426526] + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8292948355003096375_q": {
            "type": "arbitrary",
            "samples": [-0.05049888307844908, -0.11316014617848255, 0.0, 0.11316014617848255, 0.05049888307844908] + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7801430049944161021_i": {
            "type": "arbitrary",
            "samples": [0.038244189603245146, 0.15337417619349084] + [0.3071465441702297] * 2 + [0.15337417619349084, 0.038244189603245146] + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7801430049944161021_q": {
            "type": "arbitrary",
            "samples": [-0.03697761640728767, -0.08897683302331631, -0.05939488957134061, 0.05939488957134061, 0.08897683302331631, 0.03697761640728767] + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7524235646528158807_i": {
            "type": "arbitrary",
            "samples": [0.03372408142392078, 0.12075000918027008, 0.25957053867588853, 0.335, 0.25957053867588853, 0.12075000918027008, 0.03372408142392078] + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7524235646528158807_q": {
            "type": "arbitrary",
            "samples": [-0.028747577024901508, -0.06862099807419665, -0.07375564422527067, 0.0, 0.07375564422527067, 0.06862099807419665, 0.028747577024901508] + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-143119409993391562_i": {
            "type": "arbitrary",
            "samples": [0.03061690804427584, 0.09883258981843837, 0.21587022281644047] + [0.3190355079648841] * 2 + [0.21587022281644047, 0.09883258981843837, 0.03061690804427584] + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-143119409993391562_q": {
            "type": "arbitrary",
            "samples": [-0.023312311771396862, -0.05375218872269918, -0.07044334451474019, -0.03470283813238967, 0.03470283813238967, 0.07044334451474019, 0.05375218872269918, 0.023312311771396862] + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8729062382709261293_i": {
            "type": "arbitrary",
            "samples": [0.028360426188547543, 0.08353298994039424, 0.18070151492460493, 0.28709395863081844, 0.335, 0.28709395863081844, 0.18070151492460493, 0.08353298994039424, 0.028360426188547543] + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8729062382709261293_q": {
            "type": "arbitrary",
            "samples": [-0.019499508635346482, -0.043075487860707515, -0.062121611418438694, -0.04934861599274998, 0.0, 0.04934861599274998, 0.062121611418438694, 0.043075487860707515, 0.019499508635346482] + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3757872592209918210_i": {
            "type": "arbitrary",
            "samples": [0.026652435420606278, 0.07244883088801225, 0.15337417619349078, 0.2528712666663175] + [0.3246931335495753] * 2 + [0.2528712666663175, 0.15337417619349078, 0.07244883088801225, 0.026652435420606278] + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3757872592209918210_q": {
            "type": "arbitrary",
            "samples": [-0.016698803562208948, -0.035304931106790914, -0.05338609981398979, -0.05281127899382707, -0.02260367483862046, 0.02260367483862046, 0.05281127899382707, 0.05338609981398979, 0.035304931106790914, 0.016698803562208948] + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3491538922151461600_i": {
            "type": "arbitrary",
            "samples": [0.025317248028875385, 0.06415089032991214, 0.13220826782069808, 0.2216074096425405, 0.3021201381461697, 0.335, 0.3021201381461697, 0.2216074096425405, 0.13220826782069808, 0.06415089032991214, 0.025317248028875385] + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3491538922151461600_q": {
            "type": "arbitrary",
            "samples": [-0.0145658915715221, -0.02952658714553387, -0.045638403314736224, -0.050999373970149676, -0.03476404045804078, 0.0, 0.03476404045804078, 0.050999373970149676, 0.045638403314736224, 0.02952658714553387, 0.0145658915715221] + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3270044862952746352_i": {
            "type": "arbitrary",
            "samples": [0.0242462623660549, 0.057761244004407214, 0.11567244840843037, 0.19472646098759389, 0.2755634834035527] + [0.32780835134453135] * 2 + [0.2755634834035527, 0.19472646098759389, 0.11567244840843037, 0.057761244004407214, 0.0242462623660549] + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3270044862952746352_q": {
            "type": "arbitrary",
            "samples": [-0.012893800316100719, -0.02513173676243006, -0.039144560642527484, -0.047069374808617497, -0.039965603497666695, -0.0158475988076564, 0.0158475988076564, 0.039965603497666695, 0.047069374808617497, 0.039144560642527484, 0.02513173676243006, 0.012893800316100719] + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4935484426274245427_i": {
            "type": "arbitrary",
            "samples": [0.023368959819382324, 0.05272122394039205, 0.10258570331944422, 0.1721644385966181, 0.24920417581611157, 0.3111160627814493, 0.335, 0.3111160627814493, 0.24920417581611157, 0.1721644385966181, 0.10258570331944422, 0.05272122394039205, 0.023368959819382324] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4935484426274245427_q": {
            "type": "arbitrary",
            "samples": [-0.011551539566671312, -0.02171724476462936, -0.03380617765412908, -0.042551408787418456, -0.04106147526988523, -0.025631361264570395, 0.0, 0.025631361264570395, 0.04106147526988523, 0.042551408787418456, 0.03380617765412908, 0.02171724476462936, 0.011551539566671312] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2065218126771643866_i": {
            "type": "arbitrary",
            "samples": [0.02263766757455748, 0.048663114865035544, 0.09208172060258603, 0.1533741761934908, 0.2248725040764974, 0.29021894876787196] + [0.3297011553355644] * 2 + [0.29021894876787196, 0.2248725040764974, 0.1533741761934908, 0.09208172060258603, 0.048663114865035544, 0.02263766757455748] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2065218126771643866_q": {
            "type": "arbitrary",
            "samples": [-0.010452613832385651, -0.019012641735589635, -0.029435119992593836, -0.038132928438564126, -0.03993523420290153, -0.030924087593800692, -0.01171036264248111, 0.01171036264248111, 0.030924087593800692, 0.03993523420290153, 0.038132928438564126, 0.029435119992593836, 0.019012641735589635, 0.010452613832385651] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7133244114277412290_i": {
            "type": "arbitrary",
            "samples": [0.02201905708653771, 0.04533731988426526, 0.08353298994039424, 0.13772261731990781, 0.2031877710037322, 0.26824702997713074, 0.31689642208376645, 0.335, 0.31689642208376645, 0.26824702997713074, 0.2031877710037322, 0.13772261731990781, 0.08353298994039424, 0.04533731988426526, 0.02201905708653771, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7133244114277412290_q": {
            "type": "arbitrary",
            "samples": [-0.009537843271337833, -0.016832961026149697, -0.025845292716424512, -0.03408934707923215, -0.03772004872616085, -0.033198490871774115, -0.019609691441397726, 0.0, 0.019609691441397726, 0.033198490871774115, 0.03772004872616085, 0.03408934707923215, 0.025845292716424512, 0.016832961026149697, 0.009537843271337833, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1513252736426696160_i": {
            "type": "arbitrary",
            "samples": [0.021489157391914197, 0.04256967948039585, 0.07648386094795835, 0.1246314522890466, 0.18419334621823985, 0.2468929274591887, 0.30014546803251035] + [0.3309355027251901] * 2 + [0.30014546803251035, 0.2468929274591887, 0.18419334621823985, 0.1246314522890466, 0.07648386094795835, 0.04256967948039585, 0.021489157391914197],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1513252736426696160_q": {
            "type": "arbitrary",
            "samples": [-0.008765498650879703, -0.01504907179073338, -0.022878548609393957, -0.030502549922442612, -0.03506210283421528, -0.03356948162409208, -0.024486066597442055, -0.008999312691392763, 0.008999312691392763, 0.024486066597442055, 0.03356948162409208, 0.03506210283421528, 0.030502549922442612, 0.022878548609393957, 0.01504907179073338, 0.008765498650879703],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6080290142405374980_i": {
            "type": "arbitrary",
            "samples": [0.02103030393080685, 0.04023564801392218, 0.07060049149916642, 0.11361501285083114, 0.16768530014691396, 0.22697892583119728, 0.2817781759247988, 0.32081926804380095, 0.335, 0.32081926804380095, 0.2817781759247988, 0.22697892583119728, 0.16768530014691396, 0.11361501285083114, 0.07060049149916642, 0.04023564801392218, 0.02103030393080685] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6080290142405374980_q": {
            "type": "arbitrary",
            "samples": [-0.008105384765647523, -0.013568978048576047, -0.020407841588762153, -0.027368048190716376, -0.032314175812809647, -0.03280536625162984, -0.027150351011893187, -0.015456051041178698, 0.0, 0.015456051041178698, 0.027150351011893187, 0.03280536625162984, 0.032314175812809647, 0.027368048190716376, 0.020407841588762153, 0.013568978048576047, 0.008105384765647523] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7839815485381487353_i": {
            "type": "arbitrary",
            "samples": [0.02062920298020961, 0.03824418960324513, 0.06563539443280968, 0.10427984082962836, 0.15337417619349078, 0.2088304141698222, 0.26322363356897543, 0.3071465441702297] + [0.3317844364035494] * 2 + [0.3071465441702297, 0.26322363356897543, 0.2088304141698222, 0.15337417619349078, 0.10427984082962836, 0.06563539443280968, 0.03824418960324513, 0.02062920298020961] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7839815485381487353_q": {
            "type": "arbitrary",
            "samples": [-0.007535157025052252, -0.012325872135762552, -0.01833337358481, -0.024646427732106457, -0.02965894434110543, -0.031408899964035425, -0.028278464294322545, -0.01979829652378021, -0.007128808466805954, 0.007128808466805954, 0.01979829652378021, 0.028278464294322545, 0.031408899964035425, 0.02965894434110543, 0.024646427732106457, 0.01833337358481, 0.012325872135762552, 0.007535157025052252] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3013385709495993123_i": {
            "type": "arbitrary",
            "samples": [0.020275664839288273, 0.03652745062458811, 0.06140275056025776, 0.09631202061755613, 0.14096047928005417, 0.19250341836808385, 0.2453034910191875, 0.2916709772433678, 0.32359880522556134, 0.335, 0.32359880522556134, 0.2916709772433678, 0.2453034910191875, 0.19250341836808385, 0.14096047928005417, 0.09631202061755613, 0.06140275056025776, 0.03652745062458811, 0.020275664839288273, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3013385709495993123_q": {
            "type": "arbitrary",
            "samples": [-0.007037952859044462, -0.011270367818087594, -0.016577330898278873, -0.022287455306265302, -0.027182920347148504, -0.029697998274578037, -0.028382701128608717, -0.022498416527740355, -0.012480605332509729, 0.0, 0.012480605332509729, 0.022498416527740355, 0.028382701128608717, 0.029697998274578037, 0.027182920347148504, 0.022287455306265302, 0.016577330898278873, 0.011270367818087594, 0.007037952859044462, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3661036395203492869_i": {
            "type": "arbitrary",
            "samples": [0.01996175178526534, 0.035033965431815486, 0.0577612440044072, 0.08946236480082503, 0.130166972716642, 0.17791715699684066, 0.22845015164876664, 0.2755634834035527, 0.31225433494044175] + [0.3323930093171816] * 2 + [0.31225433494044175, 0.2755634834035527, 0.22845015164876664, 0.17791715699684066, 0.130166972716642, 0.08946236480082503, 0.0577612440044072, 0.035033965431815486, 0.01996175178526534],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3661036395203492869_q": {
            "type": "arbitrary",
            "samples": [-0.006600824824183911, -0.010365354837203843, -0.015079042057458032, -0.020240893584573465, -0.02491950694517732, -0.027868031646555515, -0.02783142518118325, -0.023979362098600028, -0.01630330624053474, -0.0057849263850300635, 0.0057849263850300635, 0.01630330624053474, 0.023979362098600028, 0.02783142518118325, 0.027868031646555515, 0.02491950694517732, 0.020240893584573465, 0.015079042057458032, 0.010365354837203843, 0.006600824824183911],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "861281374886510447_i": {
            "type": "arbitrary",
            "samples": [0.019681191070026235, 0.03372408142392077, 0.05460205803061823, 0.08353298994039424, 0.12075000918027004, 0.16492878122452376, 0.21285598123754915, 0.25957053867588853, 0.29909218802334814, 0.32563784554601377, 0.335, 0.32563784554601377, 0.29909218802334814, 0.25957053867588853, 0.21285598123754915, 0.16492878122452376, 0.12075000918027004, 0.08353298994039424, 0.05460205803061823, 0.03372408142392077, 0.019681191070026235] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "861281374886510447_q": {
            "type": "arbitrary",
            "samples": [-0.006213677809230891, -0.009582525674967169, -0.013791018851085725, -0.01846092336887465, -0.022873666024732214, -0.02603537317309713, -0.026880862697220138, -0.024585214741756897, -0.018885670943618493, -0.010280925821591165, 0.0, 0.010280925821591165, 0.018885670943618493, 0.024585214741756897, 0.026880862697220138, 0.02603537317309713, 0.022873666024732214, 0.01846092336887465, 0.013791018851085725, 0.009582525674967169, 0.006213677809230891] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5473855866811585348_i": {
            "type": "arbitrary",
            "samples": [0.019428961804270194, 0.03256681271497687, 0.05184040103472302, 0.07836621697191876, 0.11250111992155204, 0.1533741761934908, 0.198570657632372, 0.24414359709767736, 0.28506443503845413, 0.31608811754110755] + [0.33284400283199606] * 2 + [0.31608811754110755, 0.28506443503845413, 0.24414359709767736, 0.198570657632372, 0.1533741761934908, 0.11250111992155204, 0.07836621697191876, 0.05184040103472302, 0.03256681271497687, 0.019428961804270194] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5473855866811585348_q": {
            "type": "arbitrary",
            "samples": [-0.005868531962848885, -0.00889998844227892, -0.012675872407015893, -0.01690755179010933, -0.02103588476873646, -0.024266409006358996, -0.02570503317100362, -0.0245812500178251, -0.02050093303452428, -0.013639234925629937, -0.004787417702303888, 0.004787417702303888, 0.013639234925629937, 0.02050093303452428, 0.0245812500178251, 0.02570503317100362, 0.024266409006358996, 0.02103588476873646, 0.01690755179010933, 0.012675872407015893, 0.00889998844227892, 0.005868531962848885] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2066108111067612933_i": {
            "type": "arbitrary",
            "samples": [0.019200998633816527, 0.03153763427294032, 0.04940945852482564, 0.07383576222521489, 0.1052444291296256, 0.14308929931825132, 0.18556278562274675, 0.2295357287420097, 0.27082290641336215, 0.3047868175633003, 0.32717691276241306, 0.335, 0.32717691276241306, 0.3047868175633003, 0.27082290641336215, 0.2295357287420097, 0.18556278562274675, 0.14308929931825132, 0.1052444291296256, 0.07383576222521489, 0.04940945852482564, 0.03153763427294032, 0.019200998633816527, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2066108111067612933_q": {
            "type": "arbitrary",
            "samples": [-0.005559001256830622, -0.008300598029216923, -0.011703961224731566, -0.015546657104542746, -0.019389982946130112, -0.022596370018955887, -0.02441974688567169, -0.024165209110380902, -0.02138390023601445, -0.016043770660172343, -0.008611185017168907, 0.0, 0.008611185017168907, 0.016043770660172343, 0.02138390023601445, 0.024165209110380902, 0.02441974688567169, 0.022596370018955887, 0.019389982946130112, 0.015546657104542746, 0.011703961224731566, 0.008300598029216923, 0.005559001256830622, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4612752936911847132_i": {
            "type": "arbitrary",
            "samples": [0.018993975525273342, 0.03061690804427584, 0.04725602620808614, 0.06983987939141756, 0.09883258981843837, 0.13392056842844244, 0.17375799850320736, 0.21587022281644047, 0.25679767497423667, 0.2925094141462924, 0.3190355079648841] + [0.33318743003725093] * 2 + [0.3190355079648841, 0.2925094141462924, 0.25679767497423667, 0.21587022281644047, 0.17375799850320736, 0.13392056842844244, 0.09883258981843837, 0.06983987939141756, 0.04725602620808614, 0.03061690804427584, 0.018993975525273342],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4612752936911847132_q": {
            "type": "arbitrary",
            "samples": [-0.00527991794672436, -0.007770770590465619, -0.010851612145363086, -0.014349470156969593, -0.017917396240899726, -0.02104137418551962, -0.02310047732513894, -0.02348111483824673, -0.021725640589441455, -0.017676379444879525, -0.011567612710796555, -0.0040269113777358055, 0.0040269113777358055, 0.011567612710796555, 0.017676379444879525, 0.021725640589441455, 0.02348111483824673, 0.02310047732513894, 0.02104137418551962, 0.017917396240899726, 0.014349470156969593, 0.010851612145363086, 0.007770770590465619, 0.00527991794672436],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1246221591281584831_i": {
            "type": "arbitrary",
            "samples": [0.0188051455494348, 0.029788741848894427, 0.04533731988426526, 0.06629606419301091, 0.09314249565182005, 0.12572921811521887, 0.16306200574659052, 0.2031877710037322, 0.24325992741968647, 0.27981552082277616, 0.30924397603952297, 0.328366555557763, 0.335, 0.328366555557763, 0.30924397603952297, 0.27981552082277616, 0.24325992741968647, 0.2031877710037322, 0.16306200574659052, 0.12572921811521887, 0.09314249565182005, 0.06629606419301091, 0.04533731988426526, 0.029788741848894427, 0.0188051455494348] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1246221591281584831_q": {
            "type": "arbitrary",
            "samples": [-0.005027057702387244, -0.0072996287167996195, -0.010099776615689818, -0.013291872931666225, -0.01659945319948615, -0.01960605333948804, -0.0217951546772194, -0.022632029235696516, -0.021676366690925035, -0.018700317494244452, -0.013778031368946824, -0.007315008623498064, 0.0, 0.007315008623498064, 0.013778031368946824, 0.018700317494244452, 0.021676366690925035, 0.022632029235696516, 0.0217951546772194, 0.01960605333948804, 0.01659945319948615, 0.013291872931666225, 0.010099776615689818, 0.0072996287167996195, 0.005027057702387244] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8513744939115156904_i": {
            "type": "arbitrary",
            "samples": [0.018632220484242054, 0.029040149801382868, 0.04361861819906231, 0.06313697466875423, 0.08807130795463632, 0.11839243089800454, 0.1533741761934908, 0.19147821128357728, 0.23036966677978418, 0.2670976333762239, 0.2984376416154312, 0.3213482744907335] + [0.333454942326377] * 2 + [0.3213482744907335, 0.2984376416154312, 0.2670976333762239, 0.23036966677978418, 0.19147821128357728, 0.1533741761934908, 0.11839243089800454, 0.08807130795463632, 0.06313697466875423, 0.04361861819906231, 0.029040149801382868, 0.018632220484242054] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8513744939115156904_q": {
            "type": "arbitrary",
            "samples": [-0.004796935447931777, -0.006878376422405012, -0.00943301334614989, -0.012353687742751557, -0.015418517509108243, -0.018288346760014867, -0.020533115313072996, -0.021690586626291513, -0.021351434295765172, -0.019254282111555856, -0.015366779319437161, -0.009927879054501326, -0.0034339693102843046, 0.0034339693102843046, 0.009927879054501326, 0.015366779319437161, 0.019254282111555856, 0.021351434295765172, 0.021690586626291513, 0.020533115313072996, 0.018288346760014867, 0.015418517509108243, 0.012353687742751557, 0.00943301334614989, 0.006878376422405012, 0.004796935447931777] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6576965080401429237_i": {
            "type": "arbitrary",
            "samples": [0.018473279177696554, 0.028360426188547543, 0.04207150146690682, 0.0603072839254428, 0.08353298994039425, 0.11180282646469633, 0.14459525404627885, 0.18070151492460493, 0.2182107025961194, 0.25462251354338644, 0.28709395863081844, 0.3127935618695679, 0.32930479663082324, 0.335, 0.32930479663082324, 0.3127935618695679, 0.28709395863081844, 0.25462251354338644, 0.2182107025961194, 0.18070151492460493, 0.14459525404627885, 0.11180282646469633, 0.08353298994039425, 0.0603072839254428, 0.04207150146690682, 0.028360426188547543, 0.018473279177696554, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6576965080401429237_q": {
            "type": "arbitrary",
            "samples": [-0.004586651677842015, -0.0064998362117821605, -0.008838714599194502, -0.011518029421431174, -0.014358495953569176, -0.017082490350075318, -0.019331274720551735, -0.020707203806146227, -0.02083792478268882, -0.01945204235015596, -0.016449538664249988, -0.011948027548055363, -0.006289360238642818, 0.0, 0.006289360238642818, 0.011948027548055363, 0.016449538664249988, 0.01945204235015596, 0.02083792478268882, 0.020707203806146227, 0.019331274720551735, 0.017082490350075318, 0.014358495953569176, 0.011518029421431174, 0.008838714599194502, 0.0064998362117821605, 0.004586651677842015, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2004664248783405147_i": {
            "type": "arbitrary",
            "samples": [0.01832669698051233, 0.027740672691822843, 0.04067252185339826, 0.057761244004407214, 0.07945537814161627, 0.1058671894438005, 0.13663148616398643, 0.17080143881500964, 0.20681573668745798, 0.24256434403693863, 0.2755634834035527, 0.3032268778589075, 0.32319530739253516] + [0.333667357954713] * 2 + [0.32319530739253516, 0.3032268778589075, 0.2755634834035527, 0.24256434403693863, 0.20681573668745798, 0.17080143881500964, 0.13663148616398643, 0.1058671894438005, 0.07945537814161627, 0.057761244004407214, 0.04067252185339826, 0.027740672691822843, 0.01832669698051233],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2004664248783405147_q": {
            "type": "arbitrary",
            "samples": [-0.004393775342916468, -0.00615810204010712, -0.00830651437971437, -0.01077074432675574, -0.013404998936650005, -0.015980861550296318, -0.018198346731598845, -0.01971627019512014, -0.020200687511610076, -0.019384712095756564, -0.0171281157847143, -0.013462557854328296, -0.008609465403744269, -0.00296280866807351, 0.00296280866807351, 0.008609465403744269, 0.013462557854328296, 0.0171281157847143, 0.019384712095756564, 0.020200687511610076, 0.01971627019512014, 0.018198346731598845, 0.015980861550296318, 0.013404998936650005, 0.01077074432675574, 0.00830651437971437, 0.00615810204010712, 0.004393775342916468],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1783170189584689899_i": {
            "type": "arbitrary",
            "samples": [0.01819109081729815, 0.027173437275819532, 0.03940218911512964, 0.055460791446032894, 0.07577775115719239, 0.10050491499298748, 0.1293965885542483, 0.16171424994882153, 0.1961840487550165, 0.2310303486134008, 0.26409751327342346, 0.29305526517912, 0.3156637294659085, 0.3300576294131244, 0.335, 0.3300576294131244, 0.3156637294659085, 0.29305526517912, 0.26409751327342346, 0.2310303486134008, 0.1961840487550165, 0.16171424994882153, 0.1293965885542483, 0.10050491499298748, 0.07577775115719239, 0.055460791446032894, 0.03940218911512964, 0.027173437275819532, 0.01819109081729815] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1783170189584689899_q": {
            "type": "arbitrary",
            "samples": [-0.004216253593123107, -0.005848276217544015, -0.007827832855203727, -0.010099937692276888, -0.01254531756405119, -0.014975100876872502, -0.017137708842802888, -0.018740720230959636, -0.019487444441528914, -0.019124010979662546, -0.017488970687549114, -0.014554950401719634, -0.010451885069504847, -0.005464239453129454, 0.0, 0.005464239453129454, 0.010451885069504847, 0.014554950401719634, 0.017488970687549114, 0.019124010979662546, 0.019487444441528914, 0.018740720230959636, 0.017137708842802888, 0.014975100876872502, 0.01254531756405119, 0.010099937692276888, 0.007827832855203727, 0.005848276217544015, 0.004216253593123107] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8898685155510231288_i": {
            "type": "arbitrary",
            "samples": [0.018065276005258656, 0.026652435420606278, 0.03824418960324513, 0.05337406619763714, 0.07244883088801225, 0.09564642406883689, 0.12281243951968074, 0.15337417619349078, 0.1862937960640249, 0.22008011583250495, 0.2528712666663175, 0.2825884624365186, 0.3071465441702297, 0.3246931335495753] + [0.33383882265507364] * 2 + [0.3246931335495753, 0.3071465441702297, 0.2825884624365186, 0.2528712666663175, 0.22008011583250495, 0.1862937960640249, 0.15337417619349078, 0.12281243951968074, 0.09564642406883689, 0.07244883088801225, 0.05337406619763714, 0.03824418960324513, 0.026652435420606278, 0.018065276005258656] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8898685155510231288_q": {
            "type": "arbitrary",
            "samples": [-0.004052341492286493, -0.005566267854069648, -0.007395523281457531, -0.009495581447086331, -0.011768310368930305, -0.014056777673390908, -0.01614933772416663, -0.017795366604663264, -0.018732907208737402, -0.018725651149012805, -0.017603759664609024, -0.015300862194138468, -0.011878977914268127, -0.007534558279540153, -0.002582261839838253, 0.002582261839838253, 0.007534558279540153, 0.011878977914268127, 0.015300862194138468, 0.017603759664609024, 0.018725651149012805, 0.018732907208737402, 0.017795366604663264, 0.01614933772416663, 0.014056777673390908, 0.011768310368930305, 0.009495581447086331, 0.007395523281457531, 0.005566267854069648, 0.004052341492286493] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9120179214708946536_i": {
            "type": "arbitrary",
            "samples": [0.017948231995864244, 0.026172332787393688, 0.03718477943055919, 0.05147424700465795, 0.06942514753265586, 0.09123167258594302, 0.11680904663006401, 0.14571670365027273, 0.1771104611031902, 0.20973992377457756, 0.24200259030715096, 0.27205764841995045, 0.2979915037262761, 0.31801590444538874, 0.33067077659093647, 0.335, 0.33067077659093647, 0.31801590444538874, 0.2979915037262761, 0.27205764841995045, 0.24200259030715096, 0.20973992377457756, 0.1771104611031902, 0.14571670365027273, 0.11680904663006401, 0.09123167258594302, 0.06942514753265586, 0.05147424700465795, 0.03718477943055919, 0.026172332787393688, 0.017948231995864244, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9120179214708946536_q": {
            "type": "arbitrary",
            "samples": [-0.003900546757049179, -0.005308636933246881, -0.007003596495697234, -0.00894919153137007, -0.011064251808252995, -0.013217770037266836, -0.015231109608965033, -0.016889308941461907, -0.017962004814673038, -0.018232444949255903, -0.017530833845502043, -0.015766434317235428, -0.012952025511544165, -0.009214916210579795, -0.004790803631168852, 0.0, 0.004790803631168852, 0.009214916210579795, 0.012952025511544165, 0.015766434317235428, 0.017530833845502043, 0.018232444949255903, 0.017962004814673038, 0.016889308941461907, 0.015231109608965033, 0.013217770037266836, 0.011064251808252995, 0.00894919153137007, 0.007003596495697234, 0.005308636933246881, 0.003900546757049179, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "636083557617192212_i": {
            "type": "arbitrary",
            "samples": [0.01783907496397817, 0.025728574217187748, 0.036212308922245785, 0.04973863021096136, 0.0666697048114013, 0.08720880813294145, 0.11132412168314676, 0.13868047195598887, 0.16859257812915757, 0.20001321942977004, 0.23156667303054507, 0.26163179403067927, 0.28847095328142003, 0.3103921774609387, 0.3259241584509132] + [0.3339792195124562] * 2 + [0.3259241584509132, 0.3103921774609387, 0.28847095328142003, 0.26163179403067927, 0.23156667303054507, 0.20001321942977004, 0.16859257812915757, 0.13868047195598887, 0.11132412168314676, 0.08720880813294145, 0.0666697048114013, 0.04973863021096136, 0.036212308922245785, 0.025728574217187748, 0.01783907496397817],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "636083557617192212_q": {
            "type": "arbitrary",
            "samples": [-0.003759585919706981, -0.005072472577547105, -0.00664700447050471, -0.008453563504519482, -0.010424671016782855, -0.012450466839272898, -0.014379668307385634, -0.016027663742449842, -0.017192368099731983, -0.01767697886755576, -0.017317082713861034, -0.016008071622664523, -0.013727963626673716, -0.0105508333154453, -0.00664727732010924, -0.0022705205425751357, 0.0022705205425751357, 0.00664727732010924, 0.0105508333154453, 0.013727963626673716, 0.016008071622664523, 0.017317082713861034, 0.01767697886755576, 0.017192368099731983, 0.016027663742449842, 0.014379668307385634, 0.012450466839272898, 0.010424671016782855, 0.008453563504519482, 0.00664700447050471, 0.005072472577547105, 0.003759585919706981],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1398229973189615515_i": {
            "type": "arbitrary",
            "samples": [0.017737035702013577, 0.025317248028875396, 0.035316846930112555, 0.048147896727025775, 0.06415089032991214, 0.08353298994039425, 0.1063024650771302, 0.13220826782069808, 0.1606955555244329, 0.19088820144577595, 0.22160740964254055, 0.2514313569243291, 0.27879473737331245, 0.3021201381461697, 0.31996667493664244, 0.3311767137308752, 0.335, 0.3311767137308752, 0.31996667493664244, 0.3021201381461697, 0.27879473737331245, 0.2514313569243291, 0.22160740964254055, 0.19088820144577595, 0.1606955555244329, 0.13220826782069808, 0.1063024650771302, 0.08353298994039425, 0.06415089032991214, 0.048147896727025775, 0.035316846930112555, 0.025317248028875396, 0.017737035702013577] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1398229973189615515_q": {
            "type": "arbitrary",
            "samples": [-0.0036283492640250535, -0.004855297190507367, -0.00632146912846382, -0.008002556246061231, -0.009842195715177958, -0.011747860325647504, -0.013590999554778615, -0.015212801104912074, -0.01643621883652695, -0.017083827936499336, -0.016999791323383227, -0.01607302077866449, -0.014257803518539449, -0.011588013486013593, -0.008181685972103517, -0.004234165751098574, 0.0, 0.004234165751098574, 0.008181685972103517, 0.011588013486013593, 0.014257803518539449, 0.01607302077866449, 0.016999791323383227, 0.017083827936499336, 0.01643621883652695, 0.015212801104912074, 0.013590999554778615, 0.011747860325647504, 0.009842195715177958, 0.008002556246061231, 0.00632146912846382, 0.004855297190507367, 0.0036283492640250535] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5869293374643956558_i": {
            "type": "arbitrary",
            "samples": [0.017641441660759188, 0.02493497746593123, 0.034489881768632505, 0.046685525260893146, 0.061841584934738375, 0.080165368266721, 0.10169527866587191, 0.12624744794124373, 0.1533741761934908, 0.18234325229833218, 0.21214605910522533, 0.24153944207048658, 0.26912185479884504, 0.2934389054980157, 0.3131080541508245, 0.32694793794681176] + [0.33409562173676594] * 2 + [0.32694793794681176, 0.3131080541508245, 0.2934389054980157, 0.26912185479884504, 0.24153944207048658, 0.21214605910522533, 0.18234325229833218, 0.1533741761934908, 0.12624744794124373, 0.10169527866587191, 0.080165368266721, 0.061841584934738375, 0.046685525260893146, 0.034489881768632505, 0.02493497746593123, 0.017641441660759188] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5869293374643956558_q": {
            "type": "arbitrary",
            "samples": [-0.0035058725608859147, -0.004654990366536816, -0.006023346069521006, -0.007590914962161943, -0.009310408425658041, -0.011103572705463149, -0.012860806324502084, -0.014445225348695447, -0.01570179406293817, -0.016471345173496375, -0.016608347898729888, -0.016000326931145115, -0.014586113524631565, -0.012369833294107244, -0.009427843314765016, -0.005906741567682423, -0.002011957937285106, 0.002011957937285106, 0.005906741567682423, 0.009427843314765016, 0.012369833294107244, 0.014586113524631565, 0.016000326931145115, 0.016608347898729888, 0.016471345173496375, 0.01570179406293817, 0.014445225348695447, 0.012860806324502084, 0.011103572705463149, 0.009310408425658041, 0.007590914962161943, 0.006023346069521006, 0.004654990366536816, 0.0035058725608859147] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2502762029013694257_i": {
            "type": "arbitrary",
            "samples": [0.01755170225839157, 0.024578833208408275, 0.033724081423920756, 0.04533731988426526, 0.059718433160991055, 0.07707221016292604, 0.09745947536045964, 0.12075000918027004, 0.1465841871295902, 0.17435079054193522, 0.2031877710037322, 0.23201072360874123, 0.25957053867588853, 0.2845375485503847, 0.30560511573756266, 0.32160182283063504, 0.3315990141318758, 0.335, 0.3315990141318758, 0.32160182283063504, 0.30560511573756266, 0.2845375485503847, 0.25957053867588853, 0.23201072360874123, 0.2031877710037322, 0.17435079054193522, 0.1465841871295902, 0.12075000918027004, 0.09745947536045964, 0.07707221016292604, 0.059718433160991055, 0.04533731988426526, 0.033724081423920756, 0.024578833208408275, 0.01755170225839157, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2502762029013694257_q": {
            "type": "arbitrary",
            "samples": [-0.0033913141201100394, -0.004469728034533736, -0.005749515404980298, -0.007214126154064155, -0.008823717810342309, -0.01051184414027202, -0.012184749579839485, -0.01372419961483933, -0.014994413601972225, -0.015853084028045177, -0.01616573516835465, -0.015821919212458114, -0.014751128845054138, -0.012935982831744852, -0.01042033613124651, -0.00731052137053586, -0.00376888672135471, 0.0, 0.00376888672135471, 0.00731052137053586, 0.01042033613124651, 0.012935982831744852, 0.014751128845054138, 0.015821919212458114, 0.01616573516835465, 0.015853084028045177, 0.014994413601972225, 0.01372419961483933, 0.012184749579839485, 0.01051184414027202, 0.008823717810342309, 0.007214126154064155, 0.005749515404980298, 0.004469728034533736, 0.0033913141201100394, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8067053062647123421_i": {
            "type": "arbitrary",
            "samples": [0.01746729678532834, 0.024246262366054892, 0.03301309997313815, 0.044091027487984664, 0.05776124400440721, 0.07422415503583513, 0.09355702264341355, 0.11567244840843036, 0.14028326653715065, 0.16687997174656105, 0.19472646098759386, 0.2228784763460159, 0.2502267269177905, 0.2755634834035527, 0.29766792682444976, 0.3154022776673242, 0.32780835134453135] + [0.33419319917662343] * 2 + [0.32780835134453135, 0.3154022776673242, 0.29766792682444976, 0.2755634834035527, 0.2502267269177905, 0.2228784763460159, 0.19472646098759386, 0.16687997174656105, 0.14028326653715065, 0.11567244840843036, 0.09355702264341355, 0.07422415503583513, 0.05776124400440721, 0.044091027487984664, 0.03301309997313815, 0.024246262366054892, 0.01746729678532834],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8067053062647123421_q": {
            "type": "arbitrary",
            "samples": [-0.003283936032219589, -0.00429793343870024, -0.005497293772884255, -0.00686829851841081, -0.008377245587476687, -0.009967499353582524, -0.011558598373931233, -0.013048186880842496, -0.014317276627370614, -0.01523891631505295, -0.0156897916028725, -0.015563684831084793, -0.014785204150092587, -0.013321867832555567, -0.011192601151152188, -0.008471021319810805, -0.0052825329358854685, -0.0017951409457777952, 0.0017951409457777952, 0.0052825329358854685, 0.008471021319810805, 0.011192601151152188, 0.013321867832555567, 0.014785204150092587, 0.015563684831084793, 0.0156897916028725, 0.01523891631505295, 0.014317276627370614, 0.013048186880842496, 0.011558598373931233, 0.009967499353582524, 0.008377245587476687, 0.00686829851841081, 0.005497293772884255, 0.00429793343870024, 0.003283936032219589],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4525155426148970305_i": {
            "type": "arbitrary",
            "samples": [0.01738776438591863, 0.023935030466781828, 0.03235142029760381, 0.04293602631125434, 0.0559524972029222, 0.07159558289262412, 0.089954338354723, 0.11097550425506562, 0.13443156974280943, 0.15989855606019254, 0.18674842306657943, 0.21416005702807095, 0.24115103691015088, 0.26662994478875834, 0.2894661874564757, 0.3085715547266273, 0.32298552963552113, 0.33195512013119244, 0.335, 0.33195512013119244, 0.32298552963552113, 0.3085715547266273, 0.2894661874564757, 0.26662994478875834, 0.24115103691015088, 0.21416005702807095, 0.18674842306657943, 0.15989855606019254, 0.13443156974280943, 0.11097550425506562, 0.089954338354723, 0.07159558289262412, 0.0559524972029222, 0.04293602631125434, 0.03235142029760381, 0.023935030466781828, 0.01738776438591863] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4525155426148970305_q": {
            "type": "arbitrary",
            "samples": [-0.0031830887376103037, -0.004138237389163513, -0.005264363008859811, -0.0065500648787533795, -0.00796672826390364, -0.009465903566281835, -0.010978319196610463, -0.012415159588189003, -0.013672053971410589, -0.014635903778623081, -0.0151942554810711, -0.015246459627503829, -0.014715427327992933, -0.01355849300324456, -0.011775797442148302, -0.009414768327861877, -0.006569700259559274, -0.003376073289334262, 0.0, 0.003376073289334262, 0.006569700259559274, 0.009414768327861877, 0.011775797442148302, 0.01355849300324456, 0.014715427327992933, 0.015246459627503829, 0.0151942554810711, 0.014635903778623081, 0.013672053971410589, 0.012415159588189003, 0.010978319196610463, 0.009465903566281835, 0.00796672826390364, 0.0065500648787533795, 0.005264363008859811, 0.004138237389163513, 0.0031830887376103037] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6254233591039030942_i": {
            "type": "arbitrary",
            "samples": [0.017312695713105425, 0.02364317376729328, 0.031734225501660565, 0.041863070983741736, 0.05427693508076088, 0.0691640791109188, 0.0866217459432558, 0.10662383979953585, 0.128991993677392, 0.1533741761934908, 0.17923498429372278, 0.2058611395137102, 0.2323844232662663, 0.2578224355152389, 0.28113534565106796, 0.3012945290206187, 0.3173570073167443, 0.32853828794888107] + [0.3342758012248797] * 2 + [0.32853828794888107, 0.3173570073167443, 0.3012945290206187, 0.28113534565106796, 0.2578224355152389, 0.2323844232662663, 0.2058611395137102, 0.17923498429372278, 0.1533741761934908, 0.128991993677392, 0.10662383979953585, 0.0866217459432558, 0.0691640791109188, 0.05427693508076088, 0.041863070983741736, 0.031734225501660565, 0.02364317376729328, 0.017312695713105425] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6254233591039030942_q": {
            "type": "arbitrary",
            "samples": [-0.0030881982570208134, -0.003989445825408253, -0.005048711993667457, -0.006256501188374574, -0.007588432357986604, -0.009002914309719287, -0.010440124921594051, -0.011822815384348026, -0.013059327205873831, -0.01404897363526047, -0.014689616470546688, -0.014886903903549194, -0.01456428335405858, -0.013672632642363035, -0.012198227070398013, -0.010167824445654028, -0.007649919232291832, -0.004751667005132686, -0.0016115496565215104, 0.0016115496565215104, 0.004751667005132686, 0.007649919232291832, 0.010167824445654028, 0.012198227070398013, 0.013672632642363035, 0.01456428335405858, 0.014886903903549194, 0.014689616470546688, 0.01404897363526047, 0.013059327205873831, 0.011822815384348026, 0.010440124921594051, 0.009002914309719287, 0.007588432357986604, 0.006256501188374574, 0.005048711993667457, 0.003989445825408253, 0.0030881982570208134] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3059048095191327930_i": {
            "type": "arbitrary",
            "samples": [0.01724172593940673, 0.023368959819382334, 0.03115729318755132, 0.04086408275045972, 0.05272122394039205, 0.06690998119944296, 0.08353298994039425, 0.10258570331944422, 0.12393025658662747, 0.14727517665833112, 0.17216443859661812, 0.1979789625072213, 0.2239527152239888, 0.24920417581611157, 0.2727821784571032, 0.2937232779502066, 0.3111160627814493, 0.32416654841211073, 0.3322581590912206, 0.335, 0.3322581590912206, 0.32416654841211073, 0.3111160627814493, 0.2937232779502066, 0.2727821784571032, 0.24920417581611157, 0.2239527152239888, 0.1979789625072213, 0.17216443859661812, 0.14727517665833112, 0.12393025658662747, 0.10258570331944422, 0.08353298994039425, 0.06690998119944296, 0.05272122394039205, 0.04086408275045972, 0.03115729318755132, 0.023368959819382334, 0.01724172593940673, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3059048095191327930_q": {
            "type": "arbitrary",
            "samples": [-0.002998755564833742, -0.003850513188890439, -0.004848588987017177, -0.005985059413995271, -0.007239081588209785, -0.008574833023886586, -0.009940497198624812, -0.011268725884709691, -0.012478913156011833, -0.013481439921969818, -0.014183802929139488, -0.01449825584686018, -0.01435030397458634, -0.013687158423295076, -0.012485120147521669, -0.010754868037418857, -0.00854378708819013, -0.005934784050225717, -0.003041461916399061, 0.0, 0.003041461916399061, 0.005934784050225717, 0.00854378708819013, 0.010754868037418857, 0.012485120147521669, 0.013687158423295076, 0.01435030397458634, 0.01449825584686018, 0.014183802929139488, 0.013481439921969818, 0.012478913156011833, 0.011268725884709691, 0.009940497198624812, 0.008574833023886586, 0.007239081588209785, 0.005985059413995271, 0.004848588987017177, 0.003850513188890439, 0.002998755564833742, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8673487338240913053_i": {
            "type": "arbitrary",
            "samples": [0.017110811988323652, 0.02286749551829838, 0.030109789199680825, 0.03906051422721497, 0.04992399452749992, 0.06286686827952646, 0.07799656113110516, 0.09533891666490042, 0.11481697469001541, 0.13623324934850542, 0.15925800097627804, 0.1834258473583767, 0.20814258168445188, 0.2327032608419634, 0.2563215556148666, 0.2781691223703619, 0.29742251351906746, 0.31331406251496546, 0.32518242480366655, 0.33251816223085684, 0.335, 0.33251816223085684, 0.32518242480366655, 0.31331406251496546, 0.29742251351906746, 0.2781691223703619, 0.2563215556148666, 0.2327032608419634, 0.20814258168445188, 0.1834258473583767, 0.15925800097627804, 0.13623324934850542, 0.11481697469001541, 0.09533891666490042, 0.07799656113110516, 0.06286686827952646, 0.04992399452749992, 0.03906051422721497, 0.030109789199680825, 0.02286749551829838, 0.017110811988323652] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8673487338240913053_q": {
            "type": "arbitrary",
            "samples": [-0.0028344502842906484, -0.003598656817469114, -0.00448898804765578, -0.0054999039713432, -0.006616031107253624, -0.0078105445604640805, -0.009044232530626327, -0.010265539867948823, -0.01141183738469877, -0.012412064660348556, -0.013190749990439121, -0.013673234823437668, -0.013791742910414235, -0.01349176406734157, -0.012738098694757933, -0.0115198587378786, -0.009853761803634328, -0.007785192784893719, -0.005386731015804793, -0.0027541247022941353, 0.0, 0.0027541247022941353, 0.005386731015804793, 0.007785192784893719, 0.009853761803634328, 0.0115198587378786, 0.012738098694757933, 0.01349176406734157, 0.013791742910414235, 0.013673234823437668, 0.013190749990439121, 0.012412064660348556, 0.01141183738469877, 0.010265539867948823, 0.009044232530626327, 0.0078105445604640805, 0.006616031107253624, 0.0054999039713432, 0.00448898804765578, 0.003598656817469114, 0.0028344502842906484] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7525665521064044280_i": {
            "type": "arbitrary",
            "samples": [0.017050312187589976, 0.022637667574557468, 0.029633029541901945, 0.03824418960324513, 0.04866311486503552, 0.06104911583203625, 0.0755098983609188, 0.092081720602586, 0.11071029262162224, 0.13123437414030117, 0.15337417619349078, 0.17672659685492575, 0.2007689828971011, 0.2248725040764974, 0.2483253899089188, 0.27036528603014404, 0.29021894876787196, 0.3071465441702297, 0.3204870862612083, 0.3297011553355644] + [0.3344070588118783] * 2 + [0.3297011553355644, 0.3204870862612083, 0.3071465441702297, 0.29021894876787196, 0.27036528603014404, 0.2483253899089188, 0.2248725040764974, 0.2007689828971011, 0.17672659685492575, 0.15337417619349078, 0.13123437414030117, 0.11071029262162224, 0.092081720602586, 0.0755098983609188, 0.06104911583203625, 0.04866311486503552, 0.03824418960324513, 0.029633029541901945, 0.022637667574557468, 0.017050312187589976] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7525665521064044280_q": {
            "type": "arbitrary",
            "samples": [-0.002758821220629363, -0.003484204610795216, -0.00432698255208323, -0.005282516629612523, -0.006337547245196544, -0.0074687588673105825, -0.008641900257992729, -0.009811706664197947, -0.010922835000000769, -0.011911948479488387, -0.012710976146188043, -0.013251434107921064, -0.013469544398573889, -0.013311744734300511, -0.01274007088183993, -0.011736834482196506, -0.010308029197933567, -0.008484984224477231, -0.006323942390481052, -0.003903454214160371, -0.0013197230500407208, 0.0013197230500407208, 0.003903454214160371, 0.006323942390481052, 0.008484984224477231, 0.010308029197933567, 0.011736834482196506, 0.01274007088183993, 0.013311744734300511, 0.013469544398573889, 0.013251434107921064, 0.012710976146188043, 0.011911948479488387, 0.010922835000000769, 0.009811706664197947, 0.008641900257992729, 0.0074687588673105825, 0.006337547245196544, 0.005282516629612523, 0.00432698255208323, 0.003484204610795216, 0.002758821220629363] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7113906646402883685_i": {
            "type": "arbitrary",
            "samples": [0.016992792206179008, 0.022420284757886003, 0.029184044798159166, 0.037478122290260325, 0.047482999574864584, 0.05935078261347404, 0.07318848130781351, 0.08904037952415504, 0.1068708469174143, 0.1265492224897247, 0.14783854953997605, 0.17038991502633022, 0.19374391051757198, 0.21734027777785636, 0.24053615026653413, 0.26263250474062044, 0.2829075755107129, 0.3006551585403228, 0.3152250513718628, 0.3260624370407583, 0.3327429003609743, 0.335, 0.3327429003609743, 0.3260624370407583, 0.3152250513718628, 0.3006551585403228, 0.2829075755107129, 0.26263250474062044, 0.24053615026653413, 0.21734027777785636, 0.19374391051757198, 0.17038991502633022, 0.14783854953997605, 0.1265492224897247, 0.1068708469174143, 0.08904037952415504, 0.07318848130781351, 0.05935078261347404, 0.047482999574864584, 0.037478122290260325, 0.029184044798159166, 0.022420284757886003, 0.016992792206179008, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7113906646402883685_q": {
            "type": "arbitrary",
            "samples": [-0.002687095320975051, -0.003376526411168444, -0.004175400274989588, -0.005079832125620023, -0.006078355529190671, -0.007150649054889436, -0.008266716150055314, -0.009386724453292961, -0.010461684885508958, -0.011435094513661564, -0.012245581395403162, -0.012830480399692258, -0.013130147411976666, -0.01309270057989777, -0.012678778862321187, -0.011865847355611029, -0.010651569671696072, -0.009055817929416484, -0.007121000399278935, -0.004910546151608634, -0.002505577434297394, 0.0, 0.002505577434297394, 0.004910546151608634, 0.007121000399278935, 0.009055817929416484, 0.010651569671696072, 0.011865847355611029, 0.012678778862321187, 0.01309270057989777, 0.013130147411976666, 0.012830480399692258, 0.012245581395403162, 0.011435094513661564, 0.010461684885508958, 0.009386724453292961, 0.008266716150055314, 0.007150649054889436, 0.006078355529190671, 0.005079832125620023, 0.004175400274989588, 0.003376526411168444, 0.002687095320975051, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8730492257245146766_i": {
            "type": "arbitrary",
            "samples": [0.016938037517348264, 0.022214373169088395, 0.028760530609220063, 0.036757975477438865, 0.046376517299302616, 0.05776124400440721, 0.07101773269130594, 0.086196359981087, 0.1032768321007622, 0.12215429685696323, 0.14262854334499814, 0.1643978009317781, 0.18705848792601548, 0.21011192099696277, 0.23297848983482242, 0.2550191634150701, 0.2755634834035527, 0.29394249340042455, 0.30952443535967816, 0.32175059943199913, 0.33016850844762313] + [0.33445969496577194] * 2 + [0.33016850844762313, 0.32175059943199913, 0.30952443535967816, 0.29394249340042455, 0.2755634834035527, 0.2550191634150701, 0.23297848983482242, 0.21011192099696277, 0.18705848792601548, 0.1643978009317781, 0.14262854334499814, 0.12215429685696323, 0.1032768321007622, 0.086196359981087, 0.07101773269130594, 0.05776124400440721, 0.046376517299302616, 0.036757975477438865, 0.028760530609220063, 0.022214373169088395, 0.016938037517348264],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8730492257245146766_q": {
            "type": "arbitrary",
            "samples": [-0.002618979746070516, -0.003275054365158036, -0.004033314567480382, -0.0048905071874192595, -0.005836691911246695, -0.006854110026117289, -0.007916424797278918, -0.00898850610793582, -0.010026913442044755, -0.010981188601298968, -0.011796003061073113, -0.012414118663537713, -0.012780022373866582, -0.01284399738712753, -0.012566307380497993, -0.011921111850174769, -0.010899710044818193, -0.009512736717141283, -0.007791006627503704, -0.005784821501745438, -0.003561701311957981, -0.0012026641991162031, 0.0012026641991162031, 0.003561701311957981, 0.005784821501745438, 0.007791006627503704, 0.009512736717141283, 0.010899710044818193, 0.011921111850174769, 0.012566307380497993, 0.01284399738712753, 0.012780022373866582, 0.012414118663537713, 0.011796003061073113, 0.010981188601298968, 0.010026913442044755, 0.00898850610793582, 0.007916424797278918, 0.006854110026117289, 0.005836691911246695, 0.0048905071874192595, 0.004033314567480382, 0.003275054365158036, 0.002618979746070516],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2342287230438707354_i": {
            "type": "arbitrary",
            "samples": [0.016885853676522473, 0.02201905708653771, 0.028360426188547543, 0.03607988363866076, 0.04533731988426526, 0.05627103431377377, 0.06898462255545658, 0.08353298994039424, 0.09990842222077623, 0.1180278549234915, 0.13772261731990781, 0.15873195334244697, 0.18070151492460493, 0.2031877710037322, 0.22566888254048348, 0.24756208425390347, 0.26824702997713074, 0.28709395863081844, 0.30349498902168576, 0.31689642208376645, 0.3268296783217234, 0.33293846806435784, 0.335, 0.33293846806435784, 0.3268296783217234, 0.31689642208376645, 0.30349498902168576, 0.28709395863081844, 0.26824702997713074, 0.24756208425390347, 0.22566888254048348, 0.2031877710037322, 0.18070151492460493, 0.15873195334244697, 0.13772261731990781, 0.1180278549234915, 0.09990842222077623, 0.08353298994039424, 0.06898462255545658, 0.05627103431377377, 0.04533731988426526, 0.03607988363866076, 0.028360426188547543, 0.02201905708653771, 0.016885853676522473] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2342287230438707354_q": {
            "type": "arbitrary",
            "samples": [-0.0025542100963550523, -0.0031792810904459437, -0.003899901727069296, -0.004713349496246575, -0.005610987008716565, -0.0065772558239603745, -0.007588976184113599, -0.008615097572141503, -0.009617031776745309, -0.010549667728152313, -0.011363115693077382, -0.01200516022489109, -0.012424322283687736, -0.01257334957538695, -0.012412880665676662, -0.011914973623174648, -0.011066163623924706, -0.009869723198549995, -0.008346846581032755, -0.006536563813799242, -0.004494303500485123, -0.0022891533751638817, 0.0, 0.0022891533751638817, 0.004494303500485123, 0.006536563813799242, 0.008346846581032755, 0.009869723198549995, 0.011066163623924706, 0.011914973623174648, 0.012412880665676662, 0.01257334957538695, 0.012424322283687736, 0.01200516022489109, 0.011363115693077382, 0.010549667728152313, 0.009617031776745309, 0.008615097572141503, 0.007588976184113599, 0.0065772558239603745, 0.005610987008716565, 0.004713349496246575, 0.003899901727069296, 0.0031792810904459437, 0.0025542100963550523] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4694652899201001574_i": {
            "type": "arbitrary",
            "samples": [0.016836064028001252, 0.0218335469866987, 0.027981883429922777, 0.03544039163899544, 0.04435974116832225, 0.054871700064787254, 0.06707748178117125, 0.08103525545783677, 0.09674759604935303, 0.11414983320544946, 0.13310038183860678, 0.1533741761934908, 0.1746602615808129, 0.1965644117294024, 0.21861733569533248, 0.2402886320459908, 0.26100617026181516, 0.28018007366892095, 0.297229997275575, 0.31161399299860787, 0.3228569850153341, 0.33057677898769605] + [0.3345056227101372] * 2 + [0.33057677898769605, 0.3228569850153341, 0.31161399299860787, 0.297229997275575, 0.28018007366892095, 0.26100617026181516, 0.2402886320459908, 0.21861733569533248, 0.1965644117294024, 0.1746602615808129, 0.1533741761934908, 0.13310038183860678, 0.11414983320544946, 0.09674759604935303, 0.08103525545783677, 0.06707748178117125, 0.054871700064787254, 0.04435974116832225, 0.03544039163899544, 0.027981883429922777, 0.0218335469866987, 0.016836064028001252] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4694652899201001574_q": {
            "type": "arbitrary",
            "samples": [-0.0024925470553099926, -0.003088751960343029, -0.0037744274594776624, -0.004547297863026227, -0.0053998414824302215, -0.006318394577273482, -0.007282508047586256, -0.008264678857092443, -0.00923056880484113, -0.010139798594748442, -0.01094736487699141, -0.011605673872606475, -0.012067121466997198, -0.012287082527893005, -0.01222710951146848, -0.011858090688230861, -0.011163089583941306, -0.010139585779937918, -0.008800866440361063, -0.00717637748143488, -0.0053109287429903085, -0.003262750627261523, -0.0011005092711615099, 0.0011005092711615099, 0.003262750627261523, 0.0053109287429903085, 0.00717637748143488, 0.008800866440361063, 0.010139585779937918, 0.011163089583941306, 0.011858090688230861, 0.01222710951146848, 0.012287082527893005, 0.012067121466997198, 0.011605673872606475, 0.01094736487699141, 0.010139798594748442, 0.00923056880484113, 0.008264678857092443, 0.007282508047586256, 0.006318394577273482, 0.0053998414824302215, 0.004547297863026227, 0.0037744274594776624, 0.003088751960343029, 0.0024925470553099926] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8061184244831263875_i": {
            "type": "arbitrary",
            "samples": [0.016788507718561142, 0.021657129266262405, 0.027623240543868728, 0.03483640286609818, 0.04343871063074394, 0.053555674066433696, 0.0652858399979102, 0.07868961949809622, 0.09377797202299386, 0.11050175375775492, 0.12874265084905476, 0.14830666401208403, 0.16892107145526122, 0.1902356608233562, 0.21182878623136714, 0.233218483269582, 0.25387848495435106, 0.2732585577368615, 0.2908081597123593, 0.30600205772722716, 0.3183662692571892, 0.3275025546493579, 0.33310969919524747, 0.335, 0.33310969919524747, 0.3275025546493579, 0.3183662692571892, 0.30600205772722716, 0.2908081597123593, 0.2732585577368615, 0.25387848495435106, 0.233218483269582, 0.21182878623136714, 0.1902356608233562, 0.16892107145526122, 0.14830666401208403, 0.12874265084905476, 0.11050175375775492, 0.09377797202299386, 0.07868961949809622, 0.0652858399979102, 0.053555674066433696, 0.04343871063074394, 0.03483640286609818, 0.027623240543868728, 0.021657129266262405, 0.016788507718561142, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8061184244831263875_q": {
            "type": "arbitrary",
            "samples": [-0.0024337734955974955, -0.00300305852544869, -0.0036562353774301087, -0.0043914053485284875, -0.005202004856349165, -0.0060760063832949445, -0.006995328990888799, -0.00793556136701815, -0.00886609381353562, -0.009750736780635745, -0.010548872080794094, -0.011217139956758609, -0.011711613702927216, -0.011990358212809731, -0.012016215646084892, -0.0117596170734657, -0.011201190012256891, -0.010333923653850871, -0.009164669734022518, -0.007714798098582083, -0.006019889638064424, -0.004128429894647781, -0.0020995562031984375, 0.0, 0.0020995562031984375, 0.004128429894647781, 0.006019889638064424, 0.007714798098582083, 0.009164669734022518, 0.010333923653850871, 0.011201190012256891, 0.0117596170734657, 0.012016215646084892, 0.011990358212809731, 0.011711613702927216, 0.011217139956758609, 0.010548872080794094, 0.009750736780635745, 0.00886609381353562, 0.00793556136701815, 0.006995328990888799, 0.0060760063832949445, 0.005202004856349165, 0.0043914053485284875, 0.0036562353774301087, 0.00300305852544869, 0.0024337734955974955, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "538556917825762772_i": {
            "type": "arbitrary",
            "samples": [0.01674303797113176, 0.021489157391914208, 0.027282999474786657, 0.034265134889522625, 0.04256967948039585, 0.0523161670657943, 0.06360028458986718, 0.07648386094795837, 0.09098465461440518, 0.10706662222847899, 0.1246314522890466, 0.14351219703580465, 0.16346981600204136, 0.18419334621823985, 0.2053042335338458, 0.22636510283331646, 0.2468929274591887, 0.26637620435532533, 0.2842953829190331, 0.30014546803251035, 0.3134594571275351, 0.3238311091036365, 0.3309355027251901] + [0.33454593517216796] * 2 + [0.3309355027251901, 0.3238311091036365, 0.3134594571275351, 0.30014546803251035, 0.2842953829190331, 0.26637620435532533, 0.2468929274591887, 0.22636510283331646, 0.2053042335338458, 0.18419334621823985, 0.16346981600204136, 0.14351219703580465, 0.1246314522890466, 0.10706662222847899, 0.09098465461440518, 0.07648386094795837, 0.06360028458986718, 0.0523161670657943, 0.04256967948039585, 0.034265134889522625, 0.027282999474786657, 0.021489157391914208, 0.01674303797113176],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "538556917825762772_q": {
            "type": "arbitrary",
            "samples": [-0.0023776919754482707, -0.0029218328836265687, -0.003544737193892857, -0.004244824844356078, -0.005016357263577793, -0.0058487238172589264, -0.006725902622192118, -0.007626182869797987, -0.008522231290042655, -0.009381571039611703, -0.010167516640814205, -0.010840574384490077, -0.011360275974195852, -0.01168736761140509, -0.01178623179348669, -0.011627380072785437, -0.011189827208030693, -0.010463145160845308, -0.009449002496770805, -0.008162022199147351, -0.006629837580886867, -0.0048922883194019535, -0.00299977089713092, -0.0010108325759539086, 0.0010108325759539086, 0.00299977089713092, 0.0048922883194019535, 0.006629837580886867, 0.008162022199147351, 0.009449002496770805, 0.010463145160845308, 0.011189827208030693, 0.011627380072785437, 0.01178623179348669, 0.01168736761140509, 0.011360275974195852, 0.010840574384490077, 0.010167516640814205, 0.009381571039611703, 0.008522231290042655, 0.007626182869797987, 0.006725902622192118, 0.0058487238172589264, 0.005016357263577793, 0.004244824844356078, 0.003544737193892857, 0.0029218328836265687, 0.0023776919754482707],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8116884589048550841_i": {
            "type": "arbitrary",
            "samples": [0.01669952057970701, 0.02132904425280487, 0.026959806487407346, 0.03372408142392078, 0.04174855719550066, 0.05114707430080548, 0.06201233792131368, 0.07440693184201605, 0.08835409281105362, 0.10382882292686263, 0.12075000918027008, 0.1389742687674673, 0.15829223316684907, 0.17842791389577145, 0.19904165451593214, 0.21973696993608066, 0.240071316079867, 0.25957053867588853, 0.27774644364699735, 0.2941166417686991, 0.308225576534715, 0.3196654739046843, 0.32809587760191244, 0.3332604671029744, 0.335, 0.3332604671029744, 0.32809587760191244, 0.3196654739046843, 0.308225576534715, 0.2941166417686991, 0.27774644364699735, 0.25957053867588853, 0.240071316079867, 0.21973696993608066, 0.19904165451593214, 0.17842791389577145, 0.15829223316684907, 0.1389742687674673, 0.12075000918027008, 0.10382882292686263, 0.08835409281105362, 0.07440693184201605, 0.06201233792131368, 0.05114707430080548, 0.04174855719550066, 0.03372408142392078, 0.026959806487407346, 0.02132904425280487, 0.01669952057970701] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8116884589048550841_q": {
            "type": "arbitrary",
            "samples": [-0.002324122565430923, -0.0028447428441621117, -0.0034394043304898226, -0.0041067967178430725, -0.004841893683370888, -0.0056353147745744885, -0.00647283285215342, -0.007335101039734588, -0.00819767010157488, -0.009031356212992508, -0.009802999724885235, -0.010476628212908038, -0.011015003373287908, -0.011381493780751503, -0.01154217767592992, -0.011468045920472054, -0.011137149324153587, -0.010536520603610095, -0.009663702231257414, -0.008527728894231099, -0.007149446938193235, -0.005561100824309425, -0.003805174271919355, -0.0019325359473225414, 0.0, 0.0019325359473225414, 0.003805174271919355, 0.005561100824309425, 0.007149446938193235, 0.008527728894231099, 0.009663702231257414, 0.010536520603610095, 0.011137149324153587, 0.011468045920472054, 0.01154217767592992, 0.011381493780751503, 0.011015003373287908, 0.010476628212908038, 0.009802999724885235, 0.009031356212992508, 0.00819767010157488, 0.007335101039734588, 0.00647283285215342, 0.0056353147745744885, 0.004841893683370888, 0.0041067967178430725, 0.0034394043304898226, 0.0028447428441621117, 0.002324122565430923] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2736316605828929635_i": {
            "type": "arbitrary",
            "samples": [0.016657832593137117, 0.021176255530221767, 0.026652435420606278, 0.03321097959110038, 0.04097165687121171, 0.050042894708890034, 0.06051435029232949, 0.07244883088801225, 0.08587395072404966, 0.10077401470968732, 0.11708270106691843, 0.13467716333670937, 0.15337417619349078, 0.17292890077174128, 0.19303673968005297, 0.213338590814534, 0.23342959979117167, 0.2528712666663175, 0.2712065023037421, 0.28797697580685166, 0.3027418710875207, 0.31509700122705464, 0.3246931335495753, 0.3312523699447631] + [0.33458151160973465] * 2 + [0.3312523699447631, 0.3246931335495753, 0.31509700122705464, 0.3027418710875207, 0.28797697580685166, 0.2712065023037421, 0.2528712666663175, 0.23342959979117167, 0.213338590814534, 0.19303673968005297, 0.17292890077174128, 0.15337417619349078, 0.13467716333670937, 0.11708270106691843, 0.10077401470968732, 0.08587395072404966, 0.07244883088801225, 0.06051435029232949, 0.050042894708890034, 0.04097165687121171, 0.03321097959110038, 0.026652435420606278, 0.021176255530221767, 0.016657832593137117] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2736316605828929635_q": {
            "type": "arbitrary",
            "samples": [-0.002272900955979572, -0.002771487759704608, -0.0033397607124417894, -0.003976638193525707, -0.004677710301425255, -0.0054346673731065056, -0.006234850394107981, -0.007060986221358182, -0.007891168581951704, -0.008699137442067573, -0.009454894100303908, -0.010125667509408028, -0.010677219962797958, -0.011075449340341142, -0.011288213287005251, -0.011287271228325386, -0.01105021644689837, -0.010562255798765414, -0.009817691655785603, -0.008820970910084028, -0.007587189621609586, -0.006141977880898166, -0.004520734967724092, -0.002767235923186758, -0.0009316823688586992, 0.0009316823688586992, 0.002767235923186758, 0.004520734967724092, 0.006141977880898166, 0.007587189621609586, 0.008820970910084028, 0.009817691655785603, 0.010562255798765414, 0.01105021644689837, 0.011287271228325386, 0.011288213287005251, 0.011075449340341142, 0.010677219962797958, 0.010125667509408028, 0.009454894100303908, 0.008699137442067573, 0.007891168581951704, 0.007060986221358182, 0.006234850394107981, 0.0054346673731065056, 0.004677710301425255, 0.003976638193525707, 0.0033397607124417894, 0.002771487759704608, 0.002272900955979572] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2957810665027644883_i": {
            "type": "arbitrary",
            "samples": [0.01661786116073915, 0.02103030393080685, 0.02635977319469312, 0.0327237816523808, 0.04023564801392218, 0.04899866090898294, 0.059099406478136725, 0.07060049149916642, 0.08353298994039425, 0.09788903016619835, 0.11361501285083114, 0.13060599590129102, 0.1487017930670628, 0.16768530014691396, 0.18728348269003153, 0.20717133188949574, 0.22697892583119728, 0.24630153117856524, 0.2647124600369022, 0.2817781759247988, 0.2970749411774412, 0.3102061353773037, 0.32081926804380095, 0.3286216720808554, 0.33339390470428626, 0.335, 0.33339390470428626, 0.3286216720808554, 0.32081926804380095, 0.3102061353773037, 0.2970749411774412, 0.2817781759247988, 0.2647124600369022, 0.24630153117856524, 0.22697892583119728, 0.20717133188949574, 0.18728348269003153, 0.16768530014691396, 0.1487017930670628, 0.13060599590129102, 0.11361501285083114, 0.09788903016619835, 0.08353298994039425, 0.07060049149916642, 0.059099406478136725, 0.04899866090898294, 0.04023564801392218, 0.0327237816523808, 0.02635977319469312, 0.02103030393080685, 0.01661786116073915, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2957810665027644883_q": {
            "type": "arbitrary",
            "samples": [-0.002223876804374156, -0.002701794921882508, -0.0032453765620306533, -0.0038537342003590104, -0.004522992682858684, -0.005245776668218839, -0.006010800453817439, -0.006802613862920717, -0.007601556681301327, -0.008383967741065718, -0.009122682730238793, -0.009787837286222876, -0.010347969686918985, -0.010771391937603217, -0.011027771332663342, -0.011089839181201986, -0.010935122083876614, -0.010547576620537577, -0.009919002832133234, -0.009050117003964395, -0.007951180533463342, -0.006642108486692404, -0.005152017013726233, -0.0035182102287958142, -0.001784650778388407, 0.0, 0.001784650778388407, 0.0035182102287958142, 0.005152017013726233, 0.006642108486692404, 0.007951180533463342, 0.009050117003964395, 0.009919002832133234, 0.010547576620537577, 0.010935122083876614, 0.011089839181201986, 0.011027771332663342, 0.010771391937603217, 0.010347969686918985, 0.009787837286222876, 0.009122682730238793, 0.008383967741065718, 0.007601556681301327, 0.006802613862920717, 0.006010800453817439, 0.005245776668218839, 0.004522992682858684, 0.0038537342003590104, 0.0032453765620306533, 0.002701794921882508, 0.002223876804374156, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-408720680602617418_i": {
            "type": "arbitrary",
            "samples": [0.01657950251700238, 0.020890744155519354, 0.02608080722947321, 0.03226063052550099, 0.039537515651160544, 0.04800987837539687, 0.05776124400440721, 0.06885368268695924, 0.08132096298750445, 0.09516177964375815, 0.11033347612997459, 0.12674672614287222, 0.14426165259967583, 0.16268584184053636, 0.18177465052534833, 0.20123410250188192, 0.2207265357907252, 0.23987899288322825, 0.2582941616625299, 0.2755634834035527, 0.2912818644132092, 0.30506327535078004, 0.31655641235105936, 0.32545953912806963, 0.33153363728856644] + [0.3346130657179247] * 2 + [0.33153363728856644, 0.32545953912806963, 0.31655641235105936, 0.30506327535078004, 0.2912818644132092, 0.2755634834035527, 0.2582941616625299, 0.23987899288322825, 0.2207265357907252, 0.20123410250188192, 0.18177465052534833, 0.16268584184053636, 0.14426165259967583, 0.12674672614287222, 0.11033347612997459, 0.09516177964375815, 0.08132096298750445, 0.06885368268695924, 0.05776124400440721, 0.04800987837539687, 0.039537515651160544, 0.03226063052550099, 0.02608080722947321, 0.020890744155519354, 0.01657950251700238],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-408720680602617418_q": {
            "type": "arbitrary",
            "samples": [-0.002176912286652786, -0.002635416434473717, -0.003155863035396428, -0.003737529459898692, -0.004377005495376286, -0.0050677329589400915, -0.005799631560560782, -0.006558856924647869, -0.007327736037721211, -0.008084920515387258, -0.008805788584811894, -0.009463112599858525, -0.01002799079389511, -0.01047102091591148, -0.01076367097721486, -0.010879780544272001, -0.010797107059705819, -0.010498817769750753, -0.00997482093817558, -0.009222831576384625, -0.008249077623987995, -0.007068572189594676, -0.00570490497293551, -0.004189539302176429, -0.0025606375658279064, -0.0008614739599292228, 0.0008614739599292228, 0.0025606375658279064, 0.004189539302176429, 0.00570490497293551, 0.007068572189594676, 0.008249077623987995, 0.009222831576384625, 0.00997482093817558, 0.010498817769750753, 0.010797107059705819, 0.010879780544272001, 0.01076367097721486, 0.01047102091591148, 0.01002799079389511, 0.009463112599858525, 0.008805788584811894, 0.008084920515387258, 0.007327736037721211, 0.006558856924647869, 0.005799631560560782, 0.0050677329589400915, 0.004377005495376286, 0.003737529459898692, 0.003155863035396428, 0.002635416434473717, 0.002176912286652786],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5155570353030811746_i": {
            "type": "arbitrary",
            "samples": [0.016542661086237562, 0.020757168497619577, 0.025814614488185412, 0.03181983851638414, 0.03887452481399994, 0.04707247247225583, 0.0564941815705114, 0.06720092132303716, 0.07922851714716522, 0.09258116099763809, 0.10722560670262912, 0.12308615247436733, 0.14004082967288922, 0.1579192047686583, 0.17650215660339347, 0.1955239123226293, 0.2146765145931542, 0.2336167550154471, 0.2519754522399875, 0.26936878913628715, 0.2854112642695508, 0.299729672518253, 0.3119774210071509, 0.32184842085515303, 0.32908978064121425, 0.3335125679406225, 0.335, 0.3335125679406225, 0.32908978064121425, 0.32184842085515303, 0.3119774210071509, 0.299729672518253, 0.2854112642695508, 0.26936878913628715, 0.2519754522399875, 0.2336167550154471, 0.2146765145931542, 0.1955239123226293, 0.17650215660339347, 0.1579192047686583, 0.14004082967288922, 0.12308615247436733, 0.10722560670262912, 0.09258116099763809, 0.07922851714716522, 0.06720092132303716, 0.0564941815705114, 0.04707247247225583, 0.03887452481399994, 0.03181983851638414, 0.025814614488185412, 0.020757168497619577, 0.016542661086237562] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5155570353030811746_q": {
            "type": "arbitrary",
            "samples": [-0.0021318808254947126, -0.0025721264926059726, -0.0030708675740587043, -0.0036275216282989535, -0.004239083560566626, -0.00489971148844705, -0.005600385471159751, -0.006328678464144816, -0.007068678607209158, -0.007801098243383997, -0.008503597548914917, -0.00915133931745744, -0.00971777666737645, -0.010175658041612166, -0.010498215065595047, -0.01066048017808871, -0.010640664223324828, -0.010421511205340026, -0.00999153981938788, -0.009346080497032422, -0.008488023297012565, -0.007428206129296702, -0.006185393848949322, -0.004785825291998982, -0.003262335297148941, -0.0016530896527924813, 0.0, 0.0016530896527924813, 0.003262335297148941, 0.004785825291998982, 0.006185393848949322, 0.007428206129296702, 0.008488023297012565, 0.009346080497032422, 0.00999153981938788, 0.010421511205340026, 0.010640664223324828, 0.01066048017808871, 0.010498215065595047, 0.010175658041612166, 0.00971777666737645, 0.00915133931745744, 0.008503597548914917, 0.007801098243383997, 0.007068678607209158, 0.006328678464144816, 0.005600385471159751, 0.00489971148844705, 0.004239083560566626, 0.0036275216282989535, 0.0030708675740587043, 0.0025721264926059726, 0.0021318808254947126] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3038280752780913852_i": {
            "type": "arbitrary",
            "samples": [0.016507248690971008, 0.020629202980209618, 0.025560351909563264, 0.03139986879074453, 0.038244189603245146, 0.04618274222562704, 0.05529305625669434, 0.06563539443280969, 0.07724710779913953, 0.09013697549097037, 0.10427984082962836, 0.11961189270880439, 0.13602695940130002, 0.1533741761934908, 0.17145735528653616, 0.19003632477250224, 0.2088304141698222, 0.22752415058260944, 0.2457750982456412, 0.26322363356897543, 0.27950430809000565, 0.29425832418954645, 0.3071465441702297, 0.3178623823101586, 0.32614389956759143, 0.3317844364035494] + [0.3346411816713917] * 2 + [0.3317844364035494, 0.32614389956759143, 0.3178623823101586, 0.3071465441702297, 0.29425832418954645, 0.27950430809000565, 0.26322363356897543, 0.2457750982456412, 0.22752415058260944, 0.2088304141698222, 0.19003632477250224, 0.17145735528653616, 0.1533741761934908, 0.13602695940130002, 0.11961189270880439, 0.10427984082962836, 0.09013697549097037, 0.07724710779913953, 0.06563539443280969, 0.05529305625669434, 0.04618274222562704, 0.038244189603245146, 0.03139986879074453, 0.025560351909563264, 0.020629202980209618, 0.016507248690971008] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3038280752780913852_q": {
            "type": "arbitrary",
            "samples": [-0.0020886659696863334, -0.002511719008350751, -0.0029900698641855236, -0.0035232553358263904, -0.004108624045254186, -0.004740963365245198, -0.005412188068290606, -0.006111124528270001, -0.006823424321696394, -0.007531638258066104, -0.00821547591070215, -0.008852266571432198, -0.009417625479212441, -0.00988631478036848, -0.010233272905478272, -0.010434770118161964, -0.010469633321345144, -0.010320471282331592, -0.009974823661955774, -0.00942615476477418, -0.008674616532164513, -0.007727515227839197, -0.006599432174593403, -0.005311969846707473, -0.003893119108427239, -0.002376269488935318, -0.0007989099171003004, 0.0007989099171003004, 0.002376269488935318, 0.003893119108427239, 0.005311969846707473, 0.006599432174593403, 0.007727515227839197, 0.008674616532164513, 0.00942615476477418, 0.009974823661955774, 0.010320471282331592, 0.010469633321345144, 0.010434770118161964, 0.010233272905478272, 0.00988631478036848, 0.009417625479212441, 0.008852266571432198, 0.00821547591070215, 0.007531638258066104, 0.006823424321696394, 0.006111124528270001, 0.005412188068290606, 0.004740963365245198, 0.004108624045254186, 0.0035232553358263904, 0.0029900698641855236, 0.002511719008350751, 0.0020886659696863334] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3342750881422719267_i": {
            "type": "arbitrary",
            "samples": [0.016473183850336713, 0.020506503958062083, 0.02531724802887537, 0.03099931918807137, 0.03764424617771005, 0.04533731988426526, 0.05415316834373543, 0.06415089032991211, 0.07536892046661006, 0.08781984995833064, 0.10148547205679116, 0.11631235551125596, 0.13220826782069806, 0.14903976901200047, 0.16663127286419055, 0.18476582445655004, 0.2031877710037322, 0.2216074096425405, 0.23970758580599483, 0.25715209570049663, 0.27359562441412816, 0.2886948365247474, 0.3021201381461697, 0.31356755689496396, 0.3227701465074378, 0.3295083207256078, 0.33361855866269197, 0.335, 0.33361855866269197, 0.3295083207256078, 0.3227701465074378, 0.31356755689496396, 0.3021201381461697, 0.2886948365247474, 0.27359562441412816, 0.25715209570049663, 0.23970758580599483, 0.2216074096425405, 0.2031877710037322, 0.18476582445655004, 0.16663127286419055, 0.14903976901200047, 0.13220826782069806, 0.11631235551125596, 0.10148547205679116, 0.08781984995833064, 0.07536892046661006, 0.06415089032991211, 0.05415316834373543, 0.04533731988426526, 0.03764424617771005, 0.03099931918807137, 0.02531724802887537, 0.020506503958062083, 0.016473183850336713, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3342750881422719267_q": {
            "type": "arbitrary",
            "samples": [-0.002047160404561595, -0.0024540055328002804, -0.002913178314304419, -0.0034243169929581737, -0.003985079633391114, -0.004590807552586281, -0.005234241170743775, -0.005905317429106773, -0.006591078120470913, -0.007275716348160993, -0.007940783600626927, -0.00856557253299183, -0.009127680662947247, -0.009603748268110337, -0.009970350538115817, -0.010205010448228729, -0.010287286016225687, -0.010199874794029937, -0.009929670807080668, -0.009468705702208488, -0.008814907328252044, -0.007972615692729343, -0.006952808091608157, -0.005773001588633749, -0.004456820853062189, -0.0030332411902774946, -0.0015355386955757115, 0.0, 0.0015355386955757115, 0.0030332411902774946, 0.004456820853062189, 0.005773001588633749, 0.006952808091608157, 0.007972615692729343, 0.008814907328252044, 0.009468705702208488, 0.009929670807080668, 0.010199874794029937, 0.010287286016225687, 0.010205010448228729, 0.009970350538115817, 0.009603748268110337, 0.009127680662947247, 0.00856557253299183, 0.007940783600626927, 0.007275716348160993, 0.006591078120470913, 0.005905317429106773, 0.005234241170743775, 0.004590807552586281, 0.003985079633391114, 0.0034243169929581737, 0.002913178314304419, 0.0024540055328002804, 0.002047160404561595, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3535646133561972208_i": {
            "type": "arbitrary",
            "samples": [0.0164403911567603, 0.020388755120185502, 0.025084595620544388, 0.03061690804427584, 0.03707262910780947, 0.04453313546503025, 0.05307023273875479, 0.06274173753673878, 0.07358680075847314, 0.08562116513765215, 0.09883258981843837, 0.11317670586417525, 0.12857358500852906, 0.1449053061501027, 0.16201478733409075, 0.17970611371342504, 0.1977465341940047, 0.21587022281644047, 0.23378380886842698, 0.25117357740192264, 0.2677141357998929, 0.283078239809738, 0.296947381917303, 0.3090226736528391, 0.3190355079648841, 0.32675747306945074, 0.33200900787519416] + [0.3346663413355385] * 2 + [0.33200900787519416, 0.32675747306945074, 0.3190355079648841, 0.3090226736528391, 0.296947381917303, 0.283078239809738, 0.2677141357998929, 0.25117357740192264, 0.23378380886842698, 0.21587022281644047, 0.1977465341940047, 0.17970611371342504, 0.16201478733409075, 0.1449053061501027, 0.12857358500852906, 0.11317670586417525, 0.09883258981843837, 0.08562116513765215, 0.07358680075847314, 0.06274173753673878, 0.05307023273875479, 0.04453313546503025, 0.03707262910780947, 0.03061690804427584, 0.025084595620544388, 0.020388755120185502, 0.0164403911567603],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3535646133561972208_q": {
            "type": "arbitrary",
            "samples": [-0.00200726507594195, -0.0023988134327063613, -0.0028399269766429328, -0.003330330253056695, -0.0038679525429774026, -0.0044486237926805354, -0.0050658151738094915, -0.005710449445441402, -0.006370806607138327, -0.007032548730889293, -0.007678884103242739, -0.008290884818682627, -0.00884796385911986, -0.009328507808306177, -0.009710650240648043, -0.009973159246824728, -0.010096401421466927, -0.01006333493067717, -0.009860476982758914, -0.00947878702230868, -0.008914406929581046, -0.00816920381521596, -0.007251069678715051, -0.006173944880073752, -0.004957548304627095, -0.0036268151891687404, -0.0022110624765053163, -0.0007429197922590618, 0.0007429197922590618, 0.0022110624765053163, 0.0036268151891687404, 0.004957548304627095, 0.006173944880073752, 0.007251069678715051, 0.00816920381521596, 0.008914406929581046, 0.00947878702230868, 0.009860476982758914, 0.01006333493067717, 0.010096401421466927, 0.009973159246824728, 0.009710650240648043, 0.009328507808306177, 0.00884796385911986, 0.008290884818682627, 0.007678884103242739, 0.007032548730889293, 0.006370806607138327, 0.005710449445441402, 0.0050658151738094915, 0.0044486237926805354, 0.0038679525429774026, 0.003330330253056695, 0.0028399269766429328, 0.0023988134327063613, 0.00200726507594195],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5540510569425886130_i": {
            "type": "arbitrary",
            "samples": [0.016408800720936062, 0.020275664839288273, 0.024861745221146623, 0.030251461741891666, 0.03652745062458811, 0.043767385600490656, 0.05204033614215418, 0.06140275056025776, 0.07189419144496126, 0.08353298994039424, 0.09631202061755613, 0.11019482694404885, 0.12511234521565842, 0.14096047928005417, 0.15759876702128542, 0.1748503508820372, 0.19250341836808385, 0.21031421558105412, 0.22801165990702196, 0.2453034910191875, 0.2618838075381023, 0.27744174614562184, 0.2916709772433678, 0.30427962288691446, 0.31500015457740793, 0.32359880522556134, 0.3298840342230199, 0.3337136180494152, 0.335, 0.3337136180494152, 0.3298840342230199, 0.32359880522556134, 0.31500015457740793, 0.30427962288691446, 0.2916709772433678, 0.27744174614562184, 0.2618838075381023, 0.2453034910191875, 0.22801165990702196, 0.21031421558105412, 0.19250341836808385, 0.1748503508820372, 0.15759876702128542, 0.14096047928005417, 0.12511234521565842, 0.11019482694404885, 0.09631202061755613, 0.08353298994039424, 0.07189419144496126, 0.06140275056025776, 0.05204033614215418, 0.043767385600490656, 0.03652745062458811, 0.030251461741891666, 0.024861745221146623, 0.020275664839288273, 0.016408800720936062] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5540510569425886130_q": {
            "type": "arbitrary",
            "samples": [-0.0019688884127099467, -0.002345984286348154, -0.002770072849215823, -0.0032409520389237597, -0.0037567892726958645, -0.004313846349167867, -0.004906242441089008, -0.005525776966092957, -0.006161834514665067, -0.006801392820111713, -0.0074291517687551, -0.008027796588310147, -0.008578401692445102, -0.0090609734490495, -0.009455120807509026, -0.009740832860804554, -0.009899332758192679, -0.009913968730231553, -0.009771096158976478, -0.009460900376202905, -0.008978108810670982, -0.008322543622751848, -0.007499472175913451, -0.006519722402919049, -0.005399542815877758, -0.004160201777503244, -0.0028273366555189457, -0.0014300794322757195, 0.0, 0.0014300794322757195, 0.0028273366555189457, 0.004160201777503244, 0.005399542815877758, 0.006519722402919049, 0.007499472175913451, 0.008322543622751848, 0.008978108810670982, 0.009460900376202905, 0.009771096158976478, 0.009913968730231553, 0.009899332758192679, 0.009740832860804554, 0.009455120807509026, 0.0090609734490495, 0.008578401692445102, 0.008027796588310147, 0.0074291517687551, 0.006801392820111713, 0.006161834514665067, 0.005525776966092957, 0.004906242441089008, 0.004313846349167867, 0.0037567892726958645, 0.0032409520389237597, 0.002770072849215823, 0.002345984286348154, 0.0019688884127099467] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5762004628624601378_i": {
            "type": "arbitrary",
            "samples": [0.016378347676530847, 0.020166963822382845, 0.02464809941330183, 0.02990190375027576, 0.03600698236650678, 0.04303750610804605, 0.05105989921153689, 0.06012918170394747, 0.0702850759547895, 0.08154802134750797, 0.09391527226903545, 0.10735728017340702, 0.12181457754839718, 0.13719538759698016, 0.15337417619349084, 0.17019134076237294, 0.1874541936776161, 0.2049393462349833, 0.22239653505781506, 0.23955385900927825, 0.25612431542194686, 0.27181344467901164, 0.2863278173487777, 0.2993840337281388, 0.3107178569605741, 0.32009307219680694, 0.32730965865162953, 0.3322108803946219] + [0.334688945035265] * 2 + [0.3322108803946219, 0.32730965865162953, 0.32009307219680694, 0.3107178569605741, 0.2993840337281388, 0.2863278173487777, 0.27181344467901164, 0.25612431542194686, 0.23955385900927825, 0.22239653505781506, 0.2049393462349833, 0.1874541936776161, 0.17019134076237294, 0.15337417619349084, 0.13719538759698016, 0.12181457754839718, 0.10735728017340702, 0.09391527226903545, 0.08154802134750797, 0.0702850759547895, 0.06012918170394747, 0.05105989921153689, 0.04303750610804605, 0.03600698236650678, 0.02990190375027576, 0.02464809941330183, 0.020166963822382845, 0.016378347676530847] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5762004628624601378_q": {
            "type": "arbitrary",
            "samples": [-0.0019319456353301236, -0.0022953724687497057, -0.0027033935056318607, -0.0031558690549017064, -0.0036511759799596334, -0.004185958466225918, -0.004754911373669249, -0.005350615074410809, -0.005963441109106911, -0.006581547114285973, -0.007190977097380092, -0.007775879186293504, -0.008318847499095559, -0.008801387950742706, -0.009204499967929273, -0.009509357688369803, -0.00969806585906962, -0.009754457976512901, -0.009664897910602368, -0.00941904196686527, -0.00901051661011775, -0.00843746827796599, -0.007702946022365331, -0.006815085053508135, -0.005787069284814196, -0.0046368631056069465, -0.003386716043677543, -0.0020624577774178174, -0.0006926140978924638, 0.0006926140978924638, 0.0020624577774178174, 0.003386716043677543, 0.0046368631056069465, 0.005787069284814196, 0.006815085053508135, 0.007702946022365331, 0.00843746827796599, 0.00901051661011775, 0.00941904196686527, 0.009664897910602368, 0.009754457976512901, 0.00969806585906962, 0.009509357688369803, 0.009204499967929273, 0.008801387950742706, 0.008318847499095559, 0.007775879186293504, 0.007190977097380092, 0.006581547114285973, 0.005963441109106911, 0.005350615074410809, 0.004754911373669249, 0.004185958466225918, 0.0036511759799596334, 0.0031558690549017064, 0.0027033935056318607, 0.0022953724687497057, 0.0019319456353301236] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4614182811447732605_i": {
            "type": "arbitrary",
            "samples": [0.01634897173725341, 0.020062403023516345, 0.024443107769010403, 0.02956724495444249, 0.035509639286464854, 0.04234114778542693, 0.050125643081760055, 0.058916678196277224, 0.06875392763840943, 0.079659529573118, 0.09163448146975535, 0.10465526473060204, 0.11867088992658452, 0.1336005612050422, 0.14933215429105517, 0.16572168595263273, 0.18259392326727863, 0.19974423884371661, 0.21694176464209772, 0.23393383452744687, 0.2504516374394403, 0.26621693307873934, 0.28094961481086794, 0.29437584476835565, 0.3062364384005989, 0.3162951439252993, 0.32434644930378553, 0.33022255730826106, 0.3337991983630799, 0.335, 0.3337991983630799, 0.33022255730826106, 0.32434644930378553, 0.3162951439252993, 0.3062364384005989, 0.29437584476835565, 0.28094961481086794, 0.26621693307873934, 0.2504516374394403, 0.23393383452744687, 0.21694176464209772, 0.19974423884371661, 0.18259392326727863, 0.16572168595263273, 0.14933215429105517, 0.1336005612050422, 0.11867088992658452, 0.10465526473060204, 0.09163448146975535, 0.079659529573118, 0.06875392763840943, 0.058916678196277224, 0.050125643081760055, 0.04234114778542693, 0.035509639286464854, 0.02956724495444249, 0.024443107769010403, 0.020062403023516345, 0.01634897173725341, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4614182811447732605_q": {
            "type": "arbitrary",
            "samples": [-0.0018963581394580969, -0.0022468439008986414, -0.002639685007763613, -0.0030747947181428187, -0.0035507344064161076, -0.004064487455774393, -0.00461126108802299, -0.005184332561988199, -0.005774956623944011, -0.006372350452165925, -0.006963770448169911, -0.0075346920122584355, -0.008069098922185032, -0.0085498832460278, -0.008959350118111706, -0.009279814558925426, -0.00949427029289124, -0.009587103746664582, -0.009544820659630074, -0.009356748553602688, -0.009015676167508658, -0.008518391223093582, -0.007866080745134263, -0.007064563615560401, -0.006124332886376585, -0.005060395194928278, -0.003891905815830109, -0.0026416097027627977, -0.0013351104908730241, 0.0, 0.0013351104908730241, 0.0026416097027627977, 0.003891905815830109, 0.005060395194928278, 0.006124332886376585, 0.007064563615560401, 0.007866080745134263, 0.008518391223093582, 0.009015676167508658, 0.009356748553602688, 0.009544820659630074, 0.009587103746664582, 0.00949427029289124, 0.009279814558925426, 0.008959350118111706, 0.0085498832460278, 0.008069098922185032, 0.0075346920122584355, 0.006963770448169911, 0.006372350452165925, 0.005774956623944011, 0.005184332561988199, 0.00461126108802299, 0.004064487455774393, 0.0035507344064161076, 0.0030747947181428187, 0.002639685007763613, 0.0022468439008986414, 0.0018963581394580969, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3053172245073817764_i": {
            "type": "arbitrary",
            "samples": [0.016320616799946945, 0.01996175178526534, 0.024246262366054892, 0.029246575101332925, 0.035033965431815486, 0.04167615500942922, 0.049234559688591965, 0.0577612440044072, 0.06729566419935343, 0.07786130811768481, 0.08946236480082503, 0.1020805774348162, 0.11567244840843036, 0.130166972716642, 0.14546407413124934, 0.16143390623893508, 0.17791715699684066, 0.19472646098759386, 0.21164897899635338, 0.22845015164876664, 0.24487857520227582, 0.2606718864105229, 0.2755634834035527, 0.2892898547029117, 0.30159824272338287, 0.31225433494044175, 0.3210496581984047, 0.32780835134453135, 0.3323930093171816] + [0.33470932756705135] * 2 + [0.3323930093171816, 0.32780835134453135, 0.3210496581984047, 0.31225433494044175, 0.30159824272338287, 0.2892898547029117, 0.2755634834035527, 0.2606718864105229, 0.24487857520227582, 0.22845015164876664, 0.21164897899635338, 0.19472646098759386, 0.17791715699684066, 0.16143390623893508, 0.14546407413124934, 0.130166972716642, 0.11567244840843036, 0.1020805774348162, 0.08946236480082503, 0.07786130811768481, 0.06729566419935343, 0.0577612440044072, 0.049234559688591965, 0.04167615500942922, 0.035033965431815486, 0.029246575101332925, 0.024246262366054892, 0.01996175178526534, 0.016320616799946945],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3053172245073817764_q": {
            "type": "arbitrary",
            "samples": [-0.0018620529453157136, -0.002200274941394637, -0.002578760063220144, -0.002997466452645629, -0.0034551182790679476, -0.00394900033566353, -0.004474776639723755, -0.005026347352486011, -0.005595758788222605, -0.006173180825164837, -0.006746964528191154, -0.007303790172813821, -0.007828912128505498, -0.008306502315059108, -0.008720088384255656, -0.009053076691486693, -0.00928934388218517, -0.009413874961723499, -0.009413420512177074, -0.009277141727061082, -0.00899720957188574, -0.008569323973416662, -0.007993120699533342, -0.007272437567803253, -0.006415417698039063, -0.005434435413511581, -0.004345839648949369, -0.0031695197615312807, -0.0019283087950100212, -0.0006472488109234461, 0.0006472488109234461, 0.0019283087950100212, 0.0031695197615312807, 0.004345839648949369, 0.005434435413511581, 0.006415417698039063, 0.007272437567803253, 0.007993120699533342, 0.008569323973416662, 0.00899720957188574, 0.009277141727061082, 0.009413420512177074, 0.009413874961723499, 0.00928934388218517, 0.009053076691486693, 0.008720088384255656, 0.008306502315059108, 0.007828912128505498, 0.007303790172813821, 0.006746964528191154, 0.006173180825164837, 0.005595758788222605, 0.005026347352486011, 0.004474776639723755, 0.00394900033566353, 0.0034551182790679476, 0.002997466452645629, 0.002578760063220144, 0.002200274941394637, 0.0018620529453157136],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6811942499450899468_i": {
            "type": "arbitrary",
            "samples": [0.016293230588224045, 0.019864796180380968, 0.024057093803686067, 0.028939055217545424, 0.03457862135226509, 0.04104054677546668, 0.04838388541897281, 0.05665920577961019, 0.0659056067517156, 0.07614762832958034, 0.0873921731563967, 0.09962557364816733, 0.11281095347738888, 0.12688603991222352, 0.1417615834206893, 0.1573205319562992, 0.17341808880900936, 0.1898827547917869, 0.20651841846681981, 0.22310751342632912, 0.23941521133948504, 0.2551945661632482, 0.27019247165018817, 0.2841562443926857, 0.2968406014752545, 0.3080147685009925, 0.3174694329797812, 0.32502325177997243, 0.3305286306312495, 0.3338765185945078, 0.335, 0.3338765185945078, 0.3305286306312495, 0.32502325177997243, 0.3174694329797812, 0.3080147685009925, 0.2968406014752545, 0.2841562443926857, 0.27019247165018817, 0.2551945661632482, 0.23941521133948504, 0.22310751342632912, 0.20651841846681981, 0.1898827547917869, 0.17341808880900936, 0.1573205319562992, 0.1417615834206893, 0.12688603991222352, 0.11281095347738888, 0.09962557364816733, 0.0873921731563967, 0.07614762832958034, 0.0659056067517156, 0.05665920577961019, 0.04838388541897281, 0.04104054677546668, 0.03457862135226509, 0.028939055217545424, 0.024057093803686067, 0.019864796180380968, 0.016293230588224045] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6811942499450899468_q": {
            "type": "arbitrary",
            "samples": [-0.0018289622048070584, -0.0021555514021157763, -0.0025204463952343027, -0.002923643298006982, -0.003364010125421331, -0.0038390999516897334, -0.00434498473578221, -0.004876122312220392, -0.0054252694904665, -0.00598345388978962, -0.0065400159423479, -0.007082730358708726, -0.007598013263772801, -0.008071217247818313, -0.008487011887662882, -0.008829842106211027, -0.009084451355053494, -0.009236451379236727, -0.009272915642532797, -0.009182969745242502, -0.008958349715132445, -0.00859389819331569, -0.008087969474942723, -0.007442717184661814, -0.006664243018113594, -0.005762591270244784, -0.0047515814698422905, -0.0036484799007184088, -0.002473519579221687, -0.0012492867928092421, 0.0, 0.0012492867928092421, 0.002473519579221687, 0.0036484799007184088, 0.0047515814698422905, 0.005762591270244784, 0.006664243018113594, 0.007442717184661814, 0.008087969474942723, 0.00859389819331569, 0.008958349715132445, 0.009182969745242502, 0.009272915642532797, 0.009236451379236727, 0.009084451355053494, 0.008829842106211027, 0.008487011887662882, 0.008071217247818313, 0.007598013263772801, 0.007082730358708726, 0.0065400159423479, 0.00598345388978962, 0.0054252694904665, 0.004876122312220392, 0.00434498473578221, 0.0038390999516897334, 0.003364010125421331, 0.002923643298006982, 0.0025204463952343027, 0.0021555514021157763, 0.0018289622048070584] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-855412557070650901_i": {
            "type": "arbitrary",
            "samples": [0.016266764331896968, 0.019771337528975235, 0.023875167654401272, 0.028643910873716823, 0.03414237292596187, 0.04043249986686107, 0.04757107767551167, 0.05560718244931465, 0.064579443015132, 0.0745131981026747, 0.08541764951763871, 0.09728312962958431, 0.11007861450038131, 0.12374962170566102, 0.13821663307494672, 0.1533741761934908, 0.16909068394808982, 0.18520922851621907, 0.2015491953984185, 0.21790892536891884, 0.23406930913721002, 0.2497982731633614, 0.2648560479601382, 0.2790010651240334, 0.2919962891332453, 0.30361575738719915, 0.3136510794697187, 0.32191763610554974, 0.3282602209675409, 0.33255788478751336] + [0.3347277706597235] * 2 + [0.33255788478751336, 0.3282602209675409, 0.32191763610554974, 0.3136510794697187, 0.30361575738719915, 0.2919962891332453, 0.2790010651240334, 0.2648560479601382, 0.2497982731633614, 0.23406930913721002, 0.21790892536891884, 0.2015491953984185, 0.18520922851621907, 0.16909068394808982, 0.1533741761934908, 0.13821663307494672, 0.12374962170566102, 0.11007861450038131, 0.09728312962958431, 0.08541764951763871, 0.0745131981026747, 0.064579443015132, 0.05560718244931465, 0.04757107767551167, 0.04043249986686107, 0.03414237292596187, 0.028643910873716823, 0.023875167654401272, 0.019771337528975235, 0.016266764331896968] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-855412557070650901_q": {
            "type": "arbitrary",
            "samples": [-0.0017970227594479075, -0.0021125676721424074, -0.00246458529732475, -0.0028531037918472376, -0.0032771184497566797, -0.0037344215249363894, -0.004221449883924546, -0.004733161421972226, -0.005262951604705943, -0.005802621288455262, -0.00634240602444855, -0.006871075304849239, -0.007376107652101923, -0.007843944137480893, -0.008260318955628392, -0.008610661260320934, -0.008880557823706012, -0.009056261505978483, -0.009125226334715532, -0.00907664652087563, -0.008901974292275502, -0.008595390271141406, -0.008154200455647059, -0.007579135789207393, -0.006874533810094191, -0.006048386845532626, -0.00511224741169141, -0.004080988563323133, -0.002972424481369126, -0.0018068041177230851, -0.0006061977398117059, 0.0006061977398117059, 0.0018068041177230851, 0.002972424481369126, 0.004080988563323133, 0.00511224741169141, 0.006048386845532626, 0.006874533810094191, 0.007579135789207393, 0.008154200455647059, 0.008595390271141406, 0.008901974292275502, 0.00907664652087563, 0.009125226334715532, 0.009056261505978483, 0.008880557823706012, 0.008610661260320934, 0.008260318955628392, 0.007843944137480893, 0.007376107652101923, 0.006871075304849239, 0.00634240602444855, 0.005802621288455262, 0.005262951604705943, 0.004733161421972226, 0.004221449883924546, 0.0037344215249363894, 0.0032771184497566797, 0.0028531037918472376, 0.00246458529732475, 0.0021125676721424074, 0.0017970227594479075] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6401591757231887802_i": {
            "type": "arbitrary",
            "samples": [0.01624117247808034, 0.019681191070026256, 0.023700081297538995, 0.028360426188547557, 0.03372408142392078, 0.039850333886276554, 0.04679379399820855, 0.05460205803061826, 0.0633131942083855, 0.07295312435352355, 0.08353298994039428, 0.0950466066202214, 0.10746812326650107, 0.12075000918027008, 0.13482149516619077, 0.1495875898466755, 0.16492878122452378, 0.18070151492460498, 0.19673951498310518, 0.2128559812375492, 0.22884666052080463, 0.24449374864985263, 0.25957053867588853, 0.27384669034320225, 0.28709395863081844, 0.29909218802334814, 0.3096353559629908, 0.3185374355787059, 0.32563784554601377, 0.33080626442893113, 0.333946608000954, 0.335, 0.333946608000954, 0.33080626442893113, 0.32563784554601377, 0.3185374355787059, 0.3096353559629908, 0.29909218802334814, 0.28709395863081844, 0.27384669034320225, 0.25957053867588853, 0.24449374864985263, 0.22884666052080463, 0.2128559812375492, 0.19673951498310518, 0.18070151492460498, 0.16492878122452378, 0.1495875898466755, 0.13482149516619077, 0.12075000918027008, 0.10746812326650107, 0.0950466066202214, 0.08353298994039428, 0.07295312435352355, 0.0633131942083855, 0.05460205803061826, 0.04679379399820855, 0.039850333886276554, 0.03372408142392078, 0.028360426188547557, 0.023700081297538995, 0.019681191070026256, 0.01624117247808034, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6401591757231887802_q": {
            "type": "arbitrary",
            "samples": [-0.00176617574311322, -0.0020712259364102986, -0.0024110303490801678, -0.0027856440907637835, -0.0031941752249890557, -0.0036346295734523654, -0.004103770932328403, -0.004597006283695243, -0.005108305993576153, -0.005630168859940528, -0.006153641122958217, -0.00666839712085666, -0.007162887153939176, -0.007624555341577404, -0.008040126910789274, -0.008395960583297545, -0.00867845772436571, -0.00887451591691981, -0.008972010892868863, -0.008960287565740046, -0.008830638531133623, -0.008576747069354402, -0.008195071580585628, -0.007685149618175738, -0.0070498022846785646, -0.00629522364787283, -0.005430944853374045, -0.004469668500182291, -0.003426975273863721, -0.0023209114135905517, -0.0011714719117808217, 0.0, 0.0011714719117808217, 0.0023209114135905517, 0.003426975273863721, 0.004469668500182291, 0.005430944853374045, 0.00629522364787283, 0.0070498022846785646, 0.007685149618175738, 0.008195071580585628, 0.008576747069354402, 0.008830638531133623, 0.008960287565740046, 0.008972010892868863, 0.00887451591691981, 0.00867845772436571, 0.008395960583297545, 0.008040126910789274, 0.007624555341577404, 0.007162887153939176, 0.00666839712085666, 0.006153641122958217, 0.005630168859940528, 0.005108305993576153, 0.004597006283695243, 0.004103770932328403, 0.0036346295734523654, 0.0031941752249890557, 0.0027856440907637835, 0.0024110303490801678, 0.0020712259364102986, 0.00176617574311322, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6180097698033172554_i": {
            "type": "arbitrary",
            "samples": [0.016216412430376588, 0.019594184768852253, 0.023531461087949016, 0.028087938480488586, 0.0333226946581478, 0.039292497918621105, 0.04604987343385001, 0.053640957292574135, 0.06210318524859527, 0.07146287894211999, 0.08173280759377569, 0.0929098168252094, 0.1049726272823159, 0.11787991307855558, 0.13156877276933854, 0.1459537028089519, 0.1609261746655849, 0.1763549017278133, 0.19208686094813487, 0.20794910736261257, 0.22375138814191703, 0.23928952800230852, 0.2543495213081974, 0.26871222995742483, 0.28215855222499425, 0.294474898230074, 0.30545878453267716, 0.3149243452349405, 0.3227075511276572, 0.3286709326438658, 0.3327076168286677] + [0.3347445127562449] * 2 + [0.3327076168286677, 0.3286709326438658, 0.3227075511276572, 0.3149243452349405, 0.30545878453267716, 0.294474898230074, 0.28215855222499425, 0.26871222995742483, 0.2543495213081974, 0.23928952800230852, 0.22375138814191703, 0.20794910736261257, 0.19208686094813487, 0.1763549017278133, 0.1609261746655849, 0.1459537028089519, 0.13156877276933854, 0.11787991307855558, 0.1049726272823159, 0.0929098168252094, 0.08173280759377569, 0.07146287894211999, 0.06210318524859527, 0.053640957292574135, 0.04604987343385001, 0.039292497918621105, 0.0333226946581478, 0.028087938480488586, 0.023531461087949016, 0.019594184768852253, 0.016216412430376588],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6180097698033172554_q": {
            "type": "arbitrary",
            "samples": [-0.0017363662244007203, -0.0020314354774496595, -0.002359646272771454, -0.002721076299644575, -0.0031149336608541464, -0.00353941516380004, -0.003991577958148033, -0.004467232935977991, -0.004960868695206504, -0.005465614799921432, -0.0059732524776101815, -0.006474279723657468, -0.006958036021687266, -0.00741288955786247, -0.007826486975716212, -0.008186062498305356, -0.008478799792123846, -0.008692236454485958, -0.00881469769152934, -0.008835742848878144, -0.008746606189146808, -0.008540611886463349, -0.008213542795702767, -0.007763943265581512, -0.007193338144196442, -0.006506353139906354, -0.005710725736352062, -0.004817200727571458, -0.003839309879850876, -0.00279304093157581, -0.0016964067699709064, -0.0005689308258735929, 0.0005689308258735929, 0.0016964067699709064, 0.00279304093157581, 0.003839309879850876, 0.004817200727571458, 0.005710725736352062, 0.006506353139906354, 0.007193338144196442, 0.007763943265581512, 0.008213542795702767, 0.008540611886463349, 0.008746606189146808, 0.008835742848878144, 0.00881469769152934, 0.008692236454485958, 0.008478799792123846, 0.008186062498305356, 0.007826486975716212, 0.00741288955786247, 0.006958036021687266, 0.006474279723657468, 0.0059732524776101815, 0.005465614799921432, 0.004960868695206504, 0.004467232935977991, 0.003991577958148033, 0.00353941516380004, 0.0031149336608541464, 0.002721076299644575, 0.002359646272771454, 0.0020314354774496595, 0.0017363662244007203],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2025431591193819225_i": {
            "type": "arbitrary",
            "samples": [0.01619244431301248, 0.01951015824464915, 0.023368959819382324, 0.027825833487822284, 0.0329372390801896, 0.03875755862614556, 0.04533731988426526, 0.05272122394039203, 0.06094601790475665, 0.0700382677228703, 0.08001209966926354, 0.0908669913720193, 0.1025857033194442, 0.11513244882518447, 0.12845140353102671, 0.14246565399003253, 0.1570766781718625, 0.1721644385966181, 0.18758815126708003, 0.2031877710037322, 0.2187862069148971, 0.23419225161672305, 0.24920417581611157, 0.2636139075819408, 0.2772116848037537, 0.2897910417647302, 0.3011539681579358, 0.3111160627814493, 0.3195114957851667, 0.3261975935346741, 0.33105886925538397, 0.334010340454945, 0.335, 0.334010340454945, 0.33105886925538397, 0.3261975935346741, 0.3195114957851667, 0.3111160627814493, 0.3011539681579358, 0.2897910417647302, 0.2772116848037537, 0.2636139075819408, 0.24920417581611157, 0.23419225161672305, 0.2187862069148971, 0.2031877710037322, 0.18758815126708003, 0.1721644385966181, 0.1570766781718625, 0.14246565399003253, 0.12845140353102671, 0.11513244882518447, 0.1025857033194442, 0.0908669913720193, 0.08001209966926354, 0.0700382677228703, 0.06094601790475665, 0.05272122394039203, 0.04533731988426526, 0.03875755862614556, 0.0329372390801896, 0.027825833487822284, 0.023368959819382324, 0.01951015824464915, 0.01619244431301248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2025431591193819225_q": {
            "type": "arbitrary",
            "samples": [-0.0017075428840861845, -0.001993112050162914, -0.0023103079133342625, -0.00265922698338335, -0.003039166214496298, -0.0034484934536585933, -0.0038845294675730066, -0.0043434489529258725, -0.004820208294758158, -0.00530850781601013, -0.005800795793588807, -0.006288320558344851, -0.006761235530825814, -0.007208760086750436, -0.007619396747231025, -0.007981202437909249, -0.008282108583591607, -0.00851028175748369, -0.008654513667383089, -0.008704626629114042, -0.008651878544369622, -0.00848934994635095, -0.008212295053977046, -0.007818439093464398, -0.0073082054602435845, -0.0066848585976713865, -0.005954551688605572, -0.005126272252914079, -0.004211683320204927, -0.0032248627558882515, -0.002181948280487402, -0.0011007004428847914, 0.0, 0.0011007004428847914, 0.002181948280487402, 0.0032248627558882515, 0.004211683320204927, 0.005126272252914079, 0.005954551688605572, 0.0066848585976713865, 0.0073082054602435845, 0.007818439093464398, 0.008212295053977046, 0.00848934994635095, 0.008651878544369622, 0.008704626629114042, 0.008654513667383089, 0.00851028175748369, 0.008282108583591607, 0.007981202437909249, 0.007619396747231025, 0.007208760086750436, 0.006761235530825814, 0.006288320558344851, 0.005800795793588807, 0.00530850781601013, 0.004820208294758158, 0.0043434489529258725, 0.0038845294675730066, 0.0034484934536585933, 0.003039166214496298, 0.00265922698338335, 0.0023103079133342625, 0.001993112050162914, 0.0017075428840861845] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3982338010030005691_i": {
            "type": "arbitrary",
            "samples": [0.016169230757186952, 0.0194289618042702, 0.023212254447670555, 0.027573541088657207, 0.032566812714976884, 0.038244189603245146, 0.04465428719963884, 0.05184040103472302, 0.0598385465922436, 0.06867540243603723, 0.07836621697191876, 0.08891275026434643, 0.10030133157077435, 0.11250111992155204, 0.12546265842434376, 0.1391168123715755, 0.15337417619349084, 0.1681250245502196, 0.18323986836613645, 0.198570657632372, 0.21395264988831578, 0.22920693728099034, 0.24414359709767736, 0.2585654019945559, 0.2722719982744677, 0.28506443503845413, 0.2967499053580553, 0.3071465441702297, 0.31608811754110755, 0.32342843512407077, 0.32904532251621066, 0.33284400283199606] + [0.33475975675503983] * 2 + [0.33284400283199606, 0.32904532251621066, 0.32342843512407077, 0.31608811754110755, 0.3071465441702297, 0.2967499053580553, 0.28506443503845413, 0.2722719982744677, 0.2585654019945559, 0.24414359709767736, 0.22920693728099034, 0.21395264988831578, 0.198570657632372, 0.18323986836613645, 0.1681250245502196, 0.15337417619349084, 0.1391168123715755, 0.12546265842434376, 0.11250111992155204, 0.10030133157077435, 0.08891275026434643, 0.07836621697191876, 0.06867540243603723, 0.0598385465922436, 0.05184040103472302, 0.04465428719963884, 0.038244189603245146, 0.032566812714976884, 0.027573541088657207, 0.023212254447670555, 0.0194289618042702, 0.016169230757186952] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3982338010030005691_q": {
            "type": "arbitrary",
            "samples": [-0.0016796577237259327, -0.0019561773209496283, -0.002262899326666904, -0.0025999358386085284, -0.002966662814092974, -0.003361601491571606, -0.0037823098741726867, -0.00422529080233863, -0.004685923477372001, -0.005158425309445353, -0.005635850596703108, -0.006110131757097959, -0.006572167614016871, -0.0070119615895788195, -0.007418810624632147, -0.007781543292191676, -0.008088803002119666, -0.00832936953727847, -0.008492509564532603, -0.008568344390334538, -0.008548221245580832, -0.00842507294473255, -0.0081937500059417, -0.007851309345924887, -0.007397244536958113, -0.006833644344841425, -0.006165268812532094, -0.005399535415576419, -0.004546411641876646, -0.003618214544941648, -0.0026293221590481244, -0.0015958059007679629, -0.0005349969661703505, 0.0005349969661703505, 0.0015958059007679629, 0.0026293221590481244, 0.003618214544941648, 0.004546411641876646, 0.005399535415576419, 0.006165268812532094, 0.006833644344841425, 0.007397244536958113, 0.007851309345924887, 0.0081937500059417, 0.00842507294473255, 0.008548221245580832, 0.008568344390334538, 0.008492509564532603, 0.00832936953727847, 0.008088803002119666, 0.007781543292191676, 0.007418810624632147, 0.0070119615895788195, 0.006572167614016871, 0.006110131757097959, 0.005635850596703108, 0.005158425309445353, 0.004685923477372001, 0.00422529080233863, 0.0037823098741726867, 0.003361601491571606, 0.002966662814092974, 0.0025999358386085284, 0.002262899326666904, 0.0019561773209496283, 0.0016796577237259327] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6797051007157995556_i": {
            "type": "arbitrary",
            "samples": [0.016146736707229235, 0.01935045557021014, 0.02306104404338824, 0.027330531461535624, 0.03221057883027745, 0.0377511618413431, 0.0439990658132054, 0.050996213394137936, 0.05877785652896376, 0.06737067517340989, 0.07679083600420222, 0.08704207430663082, 0.09811387066455284, 0.10997980035906806, 0.12259613685980716, 0.13590079090120286, 0.14981266293231735, 0.1642314789370631, 0.17903816767184494, 0.19409582142382803, 0.20925126286893805, 0.2243372181675773, 0.23917507197313848, 0.25357815463572614, 0.2673554867978498, 0.28031588311556777, 0.2922722963146792, 0.303046266443439, 0.3124723290842048, 0.3204022312705101, 0.326708805454075, 0.33128936025907807, 0.3340684617545248, 0.335, 0.3340684617545248, 0.33128936025907807, 0.326708805454075, 0.3204022312705101, 0.3124723290842048, 0.303046266443439, 0.2922722963146792, 0.28031588311556777, 0.2673554867978498, 0.25357815463572614, 0.23917507197313848, 0.2243372181675773, 0.20925126286893805, 0.19409582142382803, 0.17903816767184494, 0.1642314789370631, 0.14981266293231735, 0.13590079090120286, 0.12259613685980716, 0.10997980035906806, 0.09811387066455284, 0.08704207430663082, 0.07679083600420222, 0.06737067517340989, 0.05877785652896376, 0.050996213394137936, 0.0439990658132054, 0.0377511618413431, 0.03221057883027745, 0.027330531461535624, 0.02306104404338824, 0.01935045557021014, 0.016146736707229235, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6797051007157995556_q": {
            "type": "arbitrary",
            "samples": [-0.0016526658019598954, -0.0019205583636415615, -0.0022173129632291075, -0.0025430545060733346, -0.002897229270047503, -0.003278496244181268, -0.0036846272258952294, -0.004112421440500327, -0.004557640756507102, -0.00501497160618527, -0.005478019434553905, -0.0059393408565672386, -0.0063905176844825905, -0.006822275599818847, -0.00722464851618241, -0.007587187665925077, -0.00789921222625086, -0.008150095983563817, -0.008329582242075731, -0.008428117050061348, -0.008437188985220907, -0.008349662345116493, -0.008160089750608432, -0.007864989986207794, -0.007463077434643859, -0.006955430736834684, -0.006345590301121045, -0.005639576928917771, -0.00484582700498139, -0.003975043266832202, -0.0030399639357658486, -0.002055056757328211, -0.0010361480507583927, 0.0, 0.0010361480507583927, 0.002055056757328211, 0.0030399639357658486, 0.003975043266832202, 0.00484582700498139, 0.005639576928917771, 0.006345590301121045, 0.006955430736834684, 0.007463077434643859, 0.007864989986207794, 0.008160089750608432, 0.008349662345116493, 0.008437188985220907, 0.008428117050061348, 0.008329582242075731, 0.008150095983563817, 0.00789921222625086, 0.007587187665925077, 0.00722464851618241, 0.006822275599818847, 0.0063905176844825905, 0.0059393408565672386, 0.005478019434553905, 0.00501497160618527, 0.004557640756507102, 0.004112421440500327, 0.0036846272258952294, 0.003278496244181268, 0.002897229270047503, 0.0025430545060733346, 0.0022173129632291075, 0.0019205583636415615, 0.0016526658019598954, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5795157481638098170_i": {
            "type": "arbitrary",
            "samples": [0.016124929244458342, 0.01927450869228548, 0.022915047947641178, 0.027096311635182634, 0.031867760255259114, 0.03727733517381941, 0.0433700707396164, 0.0501865517594088, 0.057761244004407214, 0.06612073517476827, 0.07528193335650114, 0.08525027894381217, 0.09601803370354749, 0.10756271654683178, 0.11984575908657713, 0.1328114546971878, 0.14638627215138347, 0.160478598721249, 0.17497896779812425, 0.18976081270543432, 0.2046817717571848, 0.21958555027325724, 0.23430432392395412, 0.24866164534029045, 0.26247579343002314, 0.2755634834035527, 0.28774383628226063, 0.29884249073253005, 0.3086957284243868, 0.31715447755569254, 0.3240880582730757, 0.32938753873686566, 0.3329685814839935] + [0.3347736761831306] * 2 + [0.3329685814839935, 0.32938753873686566, 0.3240880582730757, 0.31715447755569254, 0.3086957284243868, 0.29884249073253005, 0.28774383628226063, 0.2755634834035527, 0.26247579343002314, 0.24866164534029045, 0.23430432392395412, 0.21958555027325724, 0.2046817717571848, 0.18976081270543432, 0.17497896779812425, 0.160478598721249, 0.14638627215138347, 0.1328114546971878, 0.11984575908657713, 0.10756271654683178, 0.09601803370354749, 0.08525027894381217, 0.07528193335650114, 0.06612073517476827, 0.057761244004407214, 0.0501865517594088, 0.0433700707396164, 0.03727733517381941, 0.031867760255259114, 0.027096311635182634, 0.022915047947641178, 0.01927450869228548, 0.016124929244458342],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5795157481638098170_q": {
            "type": "arbitrary",
            "samples": [-0.0016265249954969397, -0.0018861872056965174, -0.0021734489356647468, -0.002488445506941661, -0.0028306858516208787, -0.003198952824982751, -0.003591211154337307, -0.004004528122456261, -0.0044350123698405994, -0.004877776252992969, -0.005326926974140067, -0.005775591170449458, -0.006215976801198968, -0.006639475000960307, -0.007036803097447507, -0.00739818826785179, -0.007713589392591094, -0.007972952645895556, -0.008166494340727935, -0.008285002635163487, -0.00832014802784563, -0.00826479123867211, -0.00811327619439759, -0.007861695505945647, -0.007508116097600079, -0.00705275355841177, -0.006498085327002932, -0.005848894947592467, -0.005112242264347034, -0.0042973574349157604, -0.0034154598950035696, -0.0024795067260960494, -0.0015038780893792565, -0.000504010312593571, 0.000504010312593571, 0.0015038780893792565, 0.0024795067260960494, 0.0034154598950035696, 0.0042973574349157604, 0.005112242264347034, 0.005848894947592467, 0.006498085327002932, 0.00705275355841177, 0.007508116097600079, 0.007861695505945647, 0.00811327619439759, 0.00826479123867211, 0.00832014802784563, 0.008285002635163487, 0.008166494340727935, 0.007972952645895556, 0.007713589392591094, 0.00739818826785179, 0.007036803097447507, 0.006639475000960307, 0.006215976801198968, 0.005775591170449458, 0.005326926974140067, 0.004877776252992969, 0.0044350123698405994, 0.004004528122456261, 0.003591211154337307, 0.003198952824982751, 0.0028306858516208787, 0.002488445506941661, 0.0021734489356647468, 0.0018861872056965174, 0.0016265249954969397],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8990342977485801182_i": {
            "type": "arbitrary",
            "samples": [0.016103777426886866, 0.019200998633816527, 0.02277400410800667, 0.026870422382619677, 0.03153763427294032, 0.0368216505877448, 0.04276583078167506, 0.04940945852482564, 0.0567861985401308, 0.06492246773341098, 0.07383576222521489, 0.08353298994039425, 0.09400886543407902, 0.1052444291296256, 0.11720575662681057, 0.12984292476372225, 0.14308929931825132, 0.15686120435985737, 0.17105802519359786, 0.18556278562274675, 0.20024322611757164, 0.2149533928222676, 0.2295357287420097, 0.24382363866751464, 0.257644479282525, 0.27082290641336215, 0.2831844935082214, 0.2945595201462605, 0.3047868175633003, 0.31371755059708256, 0.32121881266830116, 0.32717691276241306, 0.3315002409409266, 0.3341216114955792, 0.335, 0.3341216114955792, 0.3315002409409266, 0.32717691276241306, 0.32121881266830116, 0.31371755059708256, 0.3047868175633003, 0.2945595201462605, 0.2831844935082214, 0.27082290641336215, 0.257644479282525, 0.24382363866751464, 0.2295357287420097, 0.2149533928222676, 0.20024322611757164, 0.18556278562274675, 0.17105802519359786, 0.15686120435985737, 0.14308929931825132, 0.12984292476372225, 0.11720575662681057, 0.1052444291296256, 0.09400886543407902, 0.08353298994039425, 0.07383576222521489, 0.06492246773341098, 0.0567861985401308, 0.04940945852482564, 0.04276583078167506, 0.0368216505877448, 0.03153763427294032, 0.026870422382619677, 0.02277400410800667, 0.019200998633816527, 0.016103777426886866] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8990342977485801182_q": {
            "type": "arbitrary",
            "samples": [-0.0016011957821335453, -0.0018530004189435407, -0.0021312143606549054, -0.002435981288413991, -0.002766866009738974, -0.003122762901837567, -0.003501811022805612, -0.0039013204082438556, -0.004317714333805181, -0.004746492388673883, -0.005182219034847583, -0.005618541894874894, -0.006048243300809695, -0.006463327648710038, -0.00685514585209303, -0.007214556708627986, -0.007532123339651963, -0.0077983411016984685, -0.008003891587726889, -0.00813991562855723, -0.008198296673347167, -0.008171944672725955, -0.008055069703460302, -0.007843434139644695, -0.007534572252674907, -0.00712796674533815, -0.006625172899078878, -0.006029882710489139, -0.005347923553390783, -0.004587188435956983, -0.003757497711121213, -0.0028703950057229694, -0.0019388830097225856, -0.0009771074583100395, 0.0, 0.0009771074583100395, 0.0019388830097225856, 0.0028703950057229694, 0.003757497711121213, 0.004587188435956983, 0.005347923553390783, 0.006029882710489139, 0.006625172899078878, 0.00712796674533815, 0.007534572252674907, 0.007843434139644695, 0.008055069703460302, 0.008171944672725955, 0.008198296673347167, 0.00813991562855723, 0.008003891587726889, 0.0077983411016984685, 0.007532123339651963, 0.007214556708627986, 0.00685514585209303, 0.006463327648710038, 0.006048243300809695, 0.005618541894874894, 0.005182219034847583, 0.004746492388673883, 0.004317714333805181, 0.0039013204082438556, 0.003501811022805612, 0.003122762901837567, 0.002766866009738974, 0.002435981288413991, 0.0021312143606549054, 0.0018530004189435407, 0.0016011957821335453] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3597397793634931307_i": {
            "type": "arbitrary",
            "samples": [0.016083252143132255, 0.019129810524250796, 0.022637667574557457, 0.026652435420606278, 0.03121952802097834, 0.03638312330362169, 0.04218497880950384, 0.048663114865035516, 0.05585038674456087, 0.06377297500938481, 0.07244883088801225, 0.08188612080984226, 0.092081720602586, 0.10301981497770468, 0.11467066133180417, 0.12698957819326176, 0.13991621751273156, 0.15337417619349078, 0.16727099565734846, 0.18149858885368278, 0.19593412210217995, 0.21044136482876674, 0.2248725040764974, 0.2390704032558961, 0.2528712666663175, 0.2661076536795146, 0.2786117699813084, 0.29021894876787196, 0.3007712230899501, 0.31012088233215496, 0.3181339016612776, 0.3246931335495753, 0.3297011553355644, 0.3330826761550278] + [0.3347864201538738] * 2 + [0.3330826761550278, 0.3297011553355644, 0.3246931335495753, 0.3181339016612776, 0.31012088233215496, 0.3007712230899501, 0.29021894876787196, 0.2786117699813084, 0.2661076536795146, 0.2528712666663175, 0.2390704032558961, 0.2248725040764974, 0.21044136482876674, 0.19593412210217995, 0.18149858885368278, 0.16727099565734846, 0.15337417619349078, 0.13991621751273156, 0.12698957819326176, 0.11467066133180417, 0.10301981497770468, 0.092081720602586, 0.08188612080984226, 0.07244883088801225, 0.06377297500938481, 0.05585038674456087, 0.048663114865035516, 0.04218497880950384, 0.03638312330362169, 0.03121952802097834, 0.026652435420606278, 0.022637667574557457, 0.019129810524250796, 0.016083252143132255] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3597397793634931307_q": {
            "type": "arbitrary",
            "samples": [-0.0015766410434764372, -0.0018209387498962395, -0.0020905227664771288, -0.0023855433660298496, -0.0027056152291757033, -0.0030497332632704746, -0.0034161942522824857, -0.003802528347117926, -0.0042054446472662614, -0.00462079519653178, -0.0050435615866844166, -0.005467868008819712, -0.0058870239985187684, -0.006293599285141984, -0.006679532089422709, -0.007036270943832808, -0.007354948679378161, -0.007626585687712826, -0.007842317998777073, -0.007993644191482656, -0.008072683764059693, -0.00807243841831427, -0.007987046840580308, -0.007812023063893862, -0.007544468427689582, -0.007183247549587729, -0.006729119600883146, -0.0061848175187601395, -0.005555069552106928, -0.00484655965559052, -0.004067825626120532, -0.0032290964055172082, -0.0023420725284962226, -0.0014196561454206328, -0.00047563926596371425, 0.00047563926596371425, 0.0014196561454206328, 0.0023420725284962226, 0.0032290964055172082, 0.004067825626120532, 0.00484655965559052, 0.005555069552106928, 0.0061848175187601395, 0.006729119600883146, 0.007183247549587729, 0.007544468427689582, 0.007812023063893862, 0.007987046840580308, 0.00807243841831427, 0.008072683764059693, 0.007993644191482656, 0.007842317998777073, 0.007626585687712826, 0.007354948679378161, 0.007036270943832808, 0.006679532089422709, 0.006293599285141984, 0.0058870239985187684, 0.005467868008819712, 0.0050435615866844166, 0.00462079519653178, 0.0042054446472662614, 0.003802528347117926, 0.0034161942522824857, 0.0030497332632704746, 0.0027056152291757033, 0.0023855433660298496, 0.0020905227664771288, 0.0018209387498962395, 0.0015766410434764372] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3375903734436216059_i": {
            "type": "arbitrary",
            "samples": [0.016063325979088387, 0.01906083657114538, 0.02250580913840038, 0.026441950880303954, 0.030912814343554734, 0.03596083653676888, 0.04162624299297049, 0.047945829106206726, 0.05495163768665448, 0.062669558567968, 0.0711178829757973, 0.08030585189782843, 0.09023224352214544, 0.10088404955554527, 0.11223529352416593, 0.12424604564911296, 0.13686168828295417, 0.15001248296505945, 0.163613484775246, 0.17756484181909513, 0.19175250747356232, 0.20604938069976686, 0.22031687566489933, 0.23440690660405733, 0.24816425789858457, 0.2614292934340567, 0.2740409441610348, 0.28583989915889035, 0.2966719141116083, 0.3063911425875728, 0.314863390405169, 0.32196919204893026, 0.3276066107893383, 0.3316936708730784, 0.33417034070890056, 0.335, 0.33417034070890056, 0.3316936708730784, 0.3276066107893383, 0.32196919204893026, 0.314863390405169, 0.3063911425875728, 0.2966719141116083, 0.28583989915889035, 0.2740409441610348, 0.2614292934340567, 0.24816425789858457, 0.23440690660405733, 0.22031687566489933, 0.20604938069976686, 0.19175250747356232, 0.17756484181909513, 0.163613484775246, 0.15001248296505945, 0.13686168828295417, 0.12424604564911296, 0.11223529352416593, 0.10088404955554527, 0.09023224352214544, 0.08030585189782843, 0.0711178829757973, 0.062669558567968, 0.05495163768665448, 0.047945829106206726, 0.04162624299297049, 0.03596083653676888, 0.030912814343554734, 0.026441950880303954, 0.02250580913840038, 0.01906083657114538, 0.016063325979088387, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3375903734436216059_q": {
            "type": "arbitrary",
            "samples": [-0.0015528258853165229, -0.0017899467852740094, -0.0020512935588356384, -0.002337021551606808, -0.002646789995435261, -0.0029796845259973423, -0.00333414480671442, -0.003707900823329012, -0.004097921634641259, -0.004500380441051291, -0.004910639736462622, -0.005323260019323092, -0.005732035041661021, -0.006130055867500469, -0.006509805102279825, -0.006863281563884801, -0.007182154427795194, -0.007457944540423475, -0.0076822292140174275, -0.007846865460444968, -0.007944225362443429, -0.007967436193987884, -0.007910617058204616, -0.00776910327634743, -0.007539649587507558, -0.007220603442594154, -0.0068120403147860584, -0.006315853997189677, -0.005735796288746544, -0.0050774622305427885, -0.004348219074538987, -0.0035570793555377584, -0.002714520691934756, -0.0018322571509355114, -0.0009229690677889491, 0.0, 0.0009229690677889491, 0.0018322571509355114, 0.002714520691934756, 0.0035570793555377584, 0.004348219074538987, 0.0050774622305427885, 0.005735796288746544, 0.006315853997189677, 0.0068120403147860584, 0.007220603442594154, 0.007539649587507558, 0.00776910327634743, 0.007910617058204616, 0.007967436193987884, 0.007944225362443429, 0.007846865460444968, 0.0076822292140174275, 0.007457944540423475, 0.007182154427795194, 0.006863281563884801, 0.006509805102279825, 0.006130055867500469, 0.005732035041661021, 0.005323260019323092, 0.004910639736462622, 0.004500380441051291, 0.004097921634641259, 0.003707900823329012, 0.00333414480671442, 0.0029796845259973423, 0.002646789995435261, 0.002337021551606808, 0.0020512935588356384, 0.0017899467852740094, 0.0015528258853165229, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6571089230283919071_i": {
            "type": "arbitrary",
            "samples": [0.01604397309607626, 0.018993975525273335, 0.022378214097318324, 0.026238595019304173, 0.030616908044275828, 0.035553935864719756, 0.04108843888273205, 0.04725602620808612, 0.054087929632206745, 0.06160970347838995, 0.06983987939141753, 0.0787886110194084, 0.08845634884536012, 0.09883258981843836, 0.10989474959004092, 0.1216072067710954, 0.1339205684284424, 0.14677120382218672, 0.1600810890230365, 0.1737579985032073, 0.1876960711367925, 0.2017767674590547, 0.21587022281644047, 0.22983698759617713, 0.2435301315575816, 0.25679767497423667, 0.26948529546491384, 0.28143924668932735, 0.2925094141462924, 0.30255242472122407, 0.31143472088817575, 0.3190355079648841, 0.3252494837926356, 0.329989264751213, 0.33318743003725093] + [0.3347981173752495] * 2 + [0.33318743003725093, 0.329989264751213, 0.3252494837926356, 0.3190355079648841, 0.31143472088817575, 0.30255242472122407, 0.2925094141462924, 0.28143924668932735, 0.26948529546491384, 0.25679767497423667, 0.2435301315575816, 0.22983698759617713, 0.21587022281644047, 0.2017767674590547, 0.1876960711367925, 0.1737579985032073, 0.1600810890230365, 0.14677120382218672, 0.1339205684284424, 0.1216072067710954, 0.10989474959004092, 0.09883258981843836, 0.08845634884536012, 0.0787886110194084, 0.06983987939141753, 0.06160970347838995, 0.054087929632206745, 0.04725602620808612, 0.04108843888273205, 0.035553935864719756, 0.030616908044275828, 0.026238595019304173, 0.022378214097318324, 0.018993975525273335, 0.01604397309607626],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6571089230283919071_q": {
            "type": "arbitrary",
            "samples": [-0.001529717473841873, -0.0017599726489081196, -0.0020134515384636355, -0.0022903132571723385, -0.002590256863488539, -0.002912449968241016, -0.003255461821091997, -0.003617204048454361, -0.003994882418829067, -0.004384963089554249, -0.004783156718989864, -0.005184423591255007, -0.005583002484434333, -0.005972465413633242, -0.0063457996030801735, -0.006695517103045926, -0.007013791395173208, -0.007292619162196899, -0.007524004183080861, -0.007700159108379647, -0.00781371973470148, -0.007857965395376714, -0.007827038279415577, -0.007716153940008521, -0.007521795005580186, -0.0072418801964804855, -0.0068759011987329565, -0.00642502075471286, -0.00589212648162651, -0.005281836385056806, -0.00460045374097027, -0.003855870903598852, -0.003057423573934482, -0.0022156990413086486, -0.001342303792578602, -0.00044959757600572303, 0.00044959757600572303, 0.001342303792578602, 0.0022156990413086486, 0.003057423573934482, 0.003855870903598852, 0.00460045374097027, 0.005281836385056806, 0.00589212648162651, 0.00642502075471286, 0.0068759011987329565, 0.0072418801964804855, 0.007521795005580186, 0.007716153940008521, 0.007827038279415577, 0.007857965395376714, 0.00781371973470148, 0.007700159108379647, 0.007524004183080861, 0.007292619162196899, 0.007013791395173208, 0.006695517103045926, 0.0063457996030801735, 0.005972465413633242, 0.005583002484434333, 0.005184423591255007, 0.004783156718989864, 0.004384963089554249, 0.003994882418829067, 0.003617204048454361, 0.003255461821091997, 0.002912449968241016, 0.002590256863488539, 0.0022903132571723385, 0.0020134515384636355, 0.0017599726489081196, 0.001529717473841873],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6255663465574916415_i": {
            "type": "arbitrary",
            "samples": [0.016025169119338187, 0.018929132193355087, 0.02225468113496958, 0.026042018148828342, 0.030331262496184168, 0.03516162413428328, 0.0405704622478734, 0.04659223823906354, 0.053257378003682014, 0.06059106382373267, 0.06861198173579104, 0.077331055549729, 0.0867502035211574, 0.09686115774030199, 0.1076443893047986, 0.11906818402392137, 0.1310879135181106, 0.14364554493953316, 0.15666942902010444, 0.1700744007045045, 0.18376221928813738, 0.19762236589096485, 0.21153320549335114, 0.22536350897011118, 0.23897431800009786, 0.25222112288771514, 0.26495631074668563, 0.27703182972760326, 0.2883020045789962, 0.298626430344236, 0.307872864879158, 0.31592003750359626, 0.32266029073649866, 0.32800197483902266, 0.3318715207892068, 0.3342151261736102, 0.335, 0.3342151261736102, 0.3318715207892068, 0.32800197483902266, 0.32266029073649866, 0.31592003750359626, 0.307872864879158, 0.298626430344236, 0.2883020045789962, 0.27703182972760326, 0.26495631074668563, 0.25222112288771514, 0.23897431800009786, 0.22536350897011118, 0.21153320549335114, 0.19762236589096485, 0.18376221928813738, 0.1700744007045045, 0.15666942902010444, 0.14364554493953316, 0.1310879135181106, 0.11906818402392137, 0.1076443893047986, 0.09686115774030199, 0.0867502035211574, 0.077331055549729, 0.06861198173579104, 0.06059106382373267, 0.053257378003682014, 0.04659223823906354, 0.0405704622478734, 0.03516162413428328, 0.030331262496184168, 0.026042018148828342, 0.02225468113496958, 0.018929132193355087, 0.016025169119338187] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6255663465574916415_q": {
            "type": "arbitrary",
            "samples": [-0.001507284886086783, -0.001730967726673968, -0.001976926464805784, -0.0022453228664481907, -0.0025358916171026257, -0.002847874475230854, -0.0031799583576094907, -0.0035302201866321734, -0.003896081514566676, -0.004274276017930893, -0.004660832905900805, -0.005051079093284066, -0.005439662639799255, -0.005820599448805021, -0.006187344553959861, -0.006532888514290232, -0.0068498785089285245, -0.0071307627037351575, -0.007367955393022458, -0.007554019347650789, -0.007681860777994114, -0.0077449314013975186, -0.007737431343153064, -0.007654506048534958, -0.0074924300850752355, -0.007248770703107037, -0.006922524320054752, -0.006514219706572249, -0.006025982570769481, -0.005461557434092855, -0.004826284126476641, -0.004127027842152673, -0.0033720634219953785, -0.002570916285915478, -0.0017341641475324464, -0.0008732052210973523, 0.0, 0.0008732052210973523, 0.0017341641475324464, 0.002570916285915478, 0.0033720634219953785, 0.004127027842152673, 0.004826284126476641, 0.005461557434092855, 0.006025982570769481, 0.006514219706572249, 0.006922524320054752, 0.007248770703107037, 0.0074924300850752355, 0.007654506048534958, 0.007737431343153064, 0.0077449314013975186, 0.007681860777994114, 0.007554019347650789, 0.007367955393022458, 0.0071307627037351575, 0.0068498785089285245, 0.006532888514290232, 0.006187344553959861, 0.005820599448805021, 0.005439662639799255, 0.005051079093284066, 0.004660832905900805, 0.004274276017930893, 0.003896081514566676, 0.0035302201866321734, 0.0031799583576094907, 0.002847874475230854, 0.0025358916171026257, 0.0022453228664481907, 0.001976926464805784, 0.001730967726673968, 0.001507284886086783] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4373329542280752208_i": {
            "type": "arbitrary",
            "samples": [0.01600689103586521, 0.018866216993554147, 0.022135021301713645, 0.025851892753078243, 0.030055366570318827, 0.03478315684995408, 0.04007128258908686, 0.04595309573996917, 0.05245822443960813, 0.05961144948750879, 0.06743153711262069, 0.0759300558694863, 0.08511020989968808, 0.09496572454070977, 0.10547982311083812, 0.11662433540706421, 0.1283589788091902, 0.1406308517126981, 0.1533741761934908, 0.1665103222827483, 0.17994814001851134, 0.19358461764290072, 0.2073058751155836, 0.22098849178368385, 0.23450115593062346, 0.24770661243097117, 0.2604638733235358, 0.27263064526751757, 0.284065918058832, 0.2946326501286176, 0.3042004806514514, 0.3126483939158908, 0.3198672602227703, 0.3257621789369635, 0.33025455346497773, 0.33328383477574686] + [0.33480887941094295] * 2 + [0.33328383477574686, 0.33025455346497773, 0.3257621789369635, 0.3198672602227703, 0.3126483939158908, 0.3042004806514514, 0.2946326501286176, 0.284065918058832, 0.27263064526751757, 0.2604638733235358, 0.24770661243097117, 0.23450115593062346, 0.22098849178368385, 0.2073058751155836, 0.19358461764290072, 0.17994814001851134, 0.1665103222827483, 0.1533741761934908, 0.1406308517126981, 0.1283589788091902, 0.11662433540706421, 0.10547982311083812, 0.09496572454070977, 0.08511020989968808, 0.0759300558694863, 0.06743153711262069, 0.05961144948750879, 0.05245822443960813, 0.04595309573996917, 0.04007128258908686, 0.03478315684995408, 0.030055366570318827, 0.025851892753078243, 0.022135021301713645, 0.018866216993554147, 0.01600689103586521] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4373329542280752208_q": {
            "type": "arbitrary",
            "samples": [-0.00148549897319633, -0.001702886416492852, -0.0019416526607858248, -0.002201961166486094, -0.0024835785088740308, -0.002785813584885731, -0.003107460276806339, -0.0034467461003043014, -0.0038012895332013466, -0.004168068798372383, -0.00454340484128512, -0.004922961085162406, -0.005301762254315467, -0.005674234124322456, -0.006034265488673571, -0.006375292935095152, -0.006690408218789962, -0.0069724871300001455, -0.007214337812701323, -0.007408865539273434, -0.007549250026810376, -0.0076291305411815185, -0.007642793322208881, -0.007585355322200696, -0.007452937920328851, -0.00724282418894869, -0.00695359346677222, -0.00658522744753098, -0.0061391827176153855, -0.00561842565422629, -0.005027426794928496, -0.004372113165324482, -0.003659778547961, -0.0028989532281684305, -0.0020992362917039036, -0.0012710950036430423, -0.00042563709906195203, 0.00042563709906195203, 0.0012710950036430423, 0.0020992362917039036, 0.0028989532281684305, 0.003659778547961, 0.004372113165324482, 0.005027426794928496, 0.00561842565422629, 0.0061391827176153855, 0.00658522744753098, 0.00695359346677222, 0.00724282418894869, 0.007452937920328851, 0.007585355322200696, 0.007642793322208881, 0.0076291305411815185, 0.007549250026810376, 0.007408865539273434, 0.007214337812701323, 0.0069724871300001455, 0.006690408218789962, 0.006375292935095152, 0.006034265488673571, 0.005674234124322456, 0.005301762254315467, 0.004922961085162406, 0.00454340484128512, 0.004168068798372383, 0.0038012895332013466, 0.0034467461003043014, 0.003107460276806339, 0.002785813584885731, 0.0024835785088740308, 0.002201961166486094, 0.0019416526607858248, 0.001702886416492852, 0.00148549897319633] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4055065770593715150_i": {
            "type": "arbitrary",
            "samples": [0.01598911710065999, 0.0188051455494348, 0.02201905708653771, 0.02566791178046532, 0.029788741848894427, 0.03441783799233561, 0.03958993725589649, 0.04533731988426526, 0.05168882684302539, 0.05866881409562558, 0.06629606419301091, 0.07458268006942848, 0.08353298994039424, 0.09314249565182005, 0.10339689951426735, 0.11427124636235832, 0.12572921811521887, 0.13772261731990781, 0.1501910739202159, 0.16306200574659052, 0.17625085797130793, 0.1896616400882612, 0.2031877710037322, 0.21671323378055804, 0.23011403174822495, 0.24325992741968647, 0.2560164353324493, 0.26824702997713074, 0.27981552082277616, 0.2905885385164426, 0.30043807001520106, 0.30924397603952297, 0.31689642208376645, 0.32329815445954296, 0.328366555557763, 0.33203541766357547, 0.33425638210367814, 0.335, 0.33425638210367814, 0.33203541766357547, 0.328366555557763, 0.32329815445954296, 0.31689642208376645, 0.30924397603952297, 0.30043807001520106, 0.2905885385164426, 0.27981552082277616, 0.26824702997713074, 0.2560164353324493, 0.24325992741968647, 0.23011403174822495, 0.21671323378055804, 0.2031877710037322, 0.1896616400882612, 0.17625085797130793, 0.16306200574659052, 0.1501910739202159, 0.13772261731990781, 0.12572921811521887, 0.11427124636235832, 0.10339689951426735, 0.09314249565182005, 0.08353298994039424, 0.07458268006942848, 0.06629606419301091, 0.05866881409562558, 0.05168882684302539, 0.04533731988426526, 0.03958993725589649, 0.03441783799233561, 0.029788741848894427, 0.02566791178046532, 0.02201905708653771, 0.0188051455494348, 0.01598911710065999, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4055065770593715150_q": {
            "type": "arbitrary",
            "samples": [-0.0014643322352453987, -0.001675685900795748, -0.0019075686542675665, -0.0021601448329529403, -0.0024332095722665397, -0.0027261326230817442, -0.0030378052120239546, -0.0033665922052299397, -0.0037102919903156755, -0.004066106566217693, -0.004430624310555409, -0.004799817766176205, -0.005169058543284902, -0.005533151066495384, -0.005886386408430792, -0.006222616850668538, -0.0065353511131626815, -0.006817869415846429, -0.007063356708386242, -0.007265051559073134, -0.007416407368985848, -0.007511261812943273, -0.00754400974523217, -0.0075097742850668845, -0.007404570449891242, -0.007225455563641678, -0.006970660753519906, -0.006639698174354824, -0.006233439164748151, -0.00575415933243489, -0.005205547564160092, -0.004592677122982274, -0.003921938288279545, -0.0032009333577640263, -0.002438336207832688, -0.0016437199373055028, -0.0008273573393187059, 0.0, 0.0008273573393187059, 0.0016437199373055028, 0.002438336207832688, 0.0032009333577640263, 0.003921938288279545, 0.004592677122982274, 0.005205547564160092, 0.00575415933243489, 0.006233439164748151, 0.006639698174354824, 0.006970660753519906, 0.007225455563641678, 0.007404570449891242, 0.0075097742850668845, 0.00754400974523217, 0.007511261812943273, 0.007416407368985848, 0.007265051559073134, 0.007063356708386242, 0.006817869415846429, 0.0065353511131626815, 0.006222616850668538, 0.005886386408430792, 0.005533151066495384, 0.005169058543284902, 0.004799817766176205, 0.004430624310555409, 0.004066106566217693, 0.0037102919903156755, 0.0033665922052299397, 0.0030378052120239546, 0.0027261326230817442, 0.0024332095722665397, 0.0021601448329529403, 0.0019075686542675665, 0.001675685900795748, 0.0014643322352453987, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1702700101831420930_i": {
            "type": "arbitrary",
            "samples": [0.015971826750633567, 0.018745838318564814, 0.021906621570778002, 0.025489787088834318, 0.029530940093187952, 0.03406501622130355, 0.03912552610476153, 0.04474371535276346, 0.05094765032040883, 0.05776124400440721, 0.06520324043097167, 0.07328617982224232, 0.08201537047242512, 0.09138789644495696, 0.10139169272570417, 0.11200472114811168, 0.1231942810733752, 0.1349164883169264, 0.14711595405267008, 0.1597256923348375, 0.1726672804438833, 0.18585129053685806, 0.19917800417623904, 0.2125384133994536, 0.22581550330940284, 0.238885802002683, 0.25162117433882675, 0.2638908269530294, 0.2755634834035527, 0.28650968079773953, 0.2966041330107517, 0.305728101012872, 0.31377170811209554, 0.32063613728479784, 0.3262356493109964, 0.33049936416304193, 0.3333727539332711] + [0.3348188033492549] * 2 + [0.3333727539332711, 0.33049936416304193, 0.3262356493109964, 0.32063613728479784, 0.31377170811209554, 0.305728101012872, 0.2966041330107517, 0.28650968079773953, 0.2755634834035527, 0.2638908269530294, 0.25162117433882675, 0.238885802002683, 0.22581550330940284, 0.2125384133994536, 0.19917800417623904, 0.18585129053685806, 0.1726672804438833, 0.1597256923348375, 0.14711595405267008, 0.1349164883169264, 0.1231942810733752, 0.11200472114811168, 0.10139169272570417, 0.09138789644495696, 0.08201537047242512, 0.07328617982224232, 0.06520324043097167, 0.05776124400440721, 0.05094765032040883, 0.04474371535276346, 0.03912552610476153, 0.03406501622130355, 0.029530940093187952, 0.025489787088834318, 0.021906621570778002, 0.018745838318564814, 0.015971826750633567],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1702700101831420930_q": {
            "type": "arbitrary",
            "samples": [-0.0014437587064907343, -0.0016493259391451099, -0.0018746168523406368, -0.0021197959633433073, -0.002384683997988934, -0.0026687059191312368, -0.0029708416367797714, -0.0032895814245941573, -0.0036228882081361627, -0.003968168962488957, -0.0043222574468875855, -0.00468141040036377, -0.0050413191166772614, -0.005397138004557326, -0.005743531320853083, -0.006074738745306208, -0.0063846598577689175, -0.006666956899056552, -0.006915174468053886, -0.007122874057915988, -0.007283780594891628, -0.007391937448756321, -0.007441865769419321, -0.007428723504540861, -0.007348459099847036, -0.007197954704517736, -0.006975153719360208, -0.006679167748246554, -0.006310358447000007, -0.005870390402021737, -0.0053622519966092415, -0.004790242209293641, -0.004159922399703141, -0.003478033329922932, -0.0027523788939104515, -0.0019916792318120016, -0.0012053970369516084, -0.0004035418698850424, 0.0004035418698850424, 0.0012053970369516084, 0.0019916792318120016, 0.0027523788939104515, 0.003478033329922932, 0.004159922399703141, 0.004790242209293641, 0.0053622519966092415, 0.005870390402021737, 0.006310358447000007, 0.006679167748246554, 0.006975153719360208, 0.007197954704517736, 0.007348459099847036, 0.007428723504540861, 0.007441865769419321, 0.007391937448756321, 0.007283780594891628, 0.007122874057915988, 0.006915174468053886, 0.006666956899056552, 0.0063846598577689175, 0.006074738745306208, 0.005743531320853083, 0.005397138004557326, 0.0050413191166772614, 0.00468141040036377, 0.0043222574468875855, 0.003968168962488957, 0.0036228882081361627, 0.0032895814245941573, 0.0029708416367797714, 0.0026687059191312368, 0.002384683997988934, 0.0021197959633433073, 0.0018746168523406368, 0.0016493259391451099, 0.0014437587064907343],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5964654954690129439_i": {
            "type": "arbitrary",
            "samples": [0.01595500052542091, 0.018688220252372753, 0.021797557655395837, 0.025317248028875385, 0.02928154093972213, 0.03372408142392077, 0.038677206642175575, 0.044171163850196773, 0.050233258923064815, 0.056886948236158225, 0.06415089032991214, 0.07203797733481726, 0.08055436945314527, 0.08969855872072248, 0.09946049063735012, 0.10982077389342855, 0.12075000918027008, 0.13220826782069808, 0.14414474959280488, 0.1564976465791464, 0.1691942361372918, 0.18215122118723745, 0.19527533003244837, 0.20846418101476213, 0.2216074096425405, 0.2345880476677823, 0.2472841352031804, 0.25957053867588853, 0.2713209395396829, 0.2824099515424439, 0.2927153182896367, 0.3021201381461697, 0.31051506042419413, 0.31780039550105493, 0.3238880821188577, 0.3287034576770394, 0.3321867818022852, 0.3342944697442287, 0.335, 0.3342944697442287, 0.3321867818022852, 0.3287034576770394, 0.3238880821188577, 0.31780039550105493, 0.31051506042419413, 0.3021201381461697, 0.2927153182896367, 0.2824099515424439, 0.2713209395396829, 0.25957053867588853, 0.2472841352031804, 0.2345880476677823, 0.2216074096425405, 0.20846418101476213, 0.19527533003244837, 0.18215122118723745, 0.1691942361372918, 0.1564976465791464, 0.14414474959280488, 0.13220826782069808, 0.12075000918027008, 0.10982077389342855, 0.09946049063735012, 0.08969855872072248, 0.08055436945314527, 0.07203797733481726, 0.06415089032991214, 0.056886948236158225, 0.050233258923064815, 0.044171163850196773, 0.038677206642175575, 0.03372408142392077, 0.02928154093972213, 0.025317248028875385, 0.021797557655395837, 0.018688220252372753, 0.01595500052542091] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5964654954690129439_q": {
            "type": "arbitrary",
            "samples": [-0.0014237538500570985, -0.0016237686789753766, -0.0018427432450170858, -0.002080841653074586, -0.0023379075679485135, -0.0026134160931728634, -0.0029064280157850546, -0.003215548233004371, -0.0035388903051697938, -0.0038740491483587073, -0.004218083877933409, -0.004567512730683191, -0.004918321820654453, -0.005265989217930894, -0.005605525480288301, -0.005931531319092373, -0.006238272552199696, -0.006519771902105175, -0.006769916556099109, -0.0069825797400297086, -0.007151753895249836, -0.007271692418806617, -0.00733705636046492, -0.007343061997014591, -0.007285624852878525, -0.007161495531165945, -0.006968382680750347, -0.006705058565933698, -0.006371443031379589, -0.005968662163414641, -0.0054990786278676885, -0.004966291494005826, -0.004375104305406069, -0.0037314611963237794, -0.003042351935334166, -0.0023156878621604926, -0.0015601517226214866, -0.0007850253553206056, 0.0, 0.0007850253553206056, 0.0015601517226214866, 0.0023156878621604926, 0.003042351935334166, 0.0037314611963237794, 0.004375104305406069, 0.004966291494005826, 0.0054990786278676885, 0.005968662163414641, 0.006371443031379589, 0.006705058565933698, 0.006968382680750347, 0.007161495531165945, 0.007285624852878525, 0.007343061997014591, 0.00733705636046492, 0.007271692418806617, 0.007151753895249836, 0.0069825797400297086, 0.006769916556099109, 0.006519771902105175, 0.006238272552199696, 0.005931531319092373, 0.005605525480288301, 0.005265989217930894, 0.004918321820654453, 0.004567512730683191, 0.004218083877933409, 0.0038740491483587073, 0.0035388903051697938, 0.003215548233004371, 0.0029064280157850546, 0.0026134160931728634, 0.0023379075679485135, 0.002080841653074586, 0.0018427432450170858, 0.0016237686789753766, 0.0014237538500570985] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3900459789834587793_i": {
            "type": "arbitrary",
            "samples": [0.015938619994475607, 0.018632220484242054, 0.021691717354498864, 0.025150040151731633, 0.02904014980138288, 0.03339446157172324, 0.038244189603245146, 0.04361861819906233, 0.0495443081123884, 0.05604424927349826, 0.06313697466875424, 0.07083565329887223, 0.07914718316888532, 0.08807130795463633, 0.09759978320218574, 0.1077156195015173, 0.11839243089800457, 0.12959391674488052, 0.14127350416260492, 0.1533741761934908, 0.16582850759724396, 0.17855892604330395, 0.19147821128357734, 0.20449023884649972, 0.2174909680391135, 0.23036966677978418, 0.24301035824912698, 0.25529346680814324, 0.2670976333762239, 0.2783016637795294, 0.28878656775738754, 0.2984376416154312, 0.3071465441702297, 0.3148133138262399, 0.3213482744907335, 0.32667377963011773, 0.33072574709621244, 0.333454942326377] + [0.33482797399961145] * 2 + [0.333454942326377, 0.33072574709621244, 0.32667377963011773, 0.3213482744907335, 0.3148133138262399, 0.3071465441702297, 0.2984376416154312, 0.28878656775738754, 0.2783016637795294, 0.2670976333762239, 0.25529346680814324, 0.24301035824912698, 0.23036966677978418, 0.2174909680391135, 0.20449023884649972, 0.19147821128357734, 0.17855892604330395, 0.16582850759724396, 0.1533741761934908, 0.14127350416260492, 0.12959391674488052, 0.11839243089800457, 0.1077156195015173, 0.09759978320218574, 0.08807130795463633, 0.07914718316888532, 0.07083565329887223, 0.06313697466875424, 0.05604424927349826, 0.0495443081123884, 0.04361861819906233, 0.038244189603245146, 0.03339446157172324, 0.02904014980138288, 0.025150040151731633, 0.021691717354498864, 0.018632220484242054, 0.015938619994475607] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3900459789834587793_q": {
            "type": "arbitrary",
            "samples": [-0.0014042944611662893, -0.0015989784826439257, -0.0018118971353209142, -0.0020432136100095987, -0.0022927921408016716, -0.0025601534081131166, -0.0028444320313298203, -0.0031443377820499644, -0.0034581222660301832, -0.003783552887617584, -0.004117895914250519, -0.00445791039156016, -0.004799854514864519, -0.005139505836369415, -0.005472196378502239, -0.0057928633356701216, -0.006096115586671624, -0.0063763157195856155, -0.006627676705955041, -0.006844371771024331, -0.007020655414423563, -0.007150992966122071, -0.007230195542097171, -0.007253556819444006, -0.007216987706776465, -0.007117144765255057, -0.00695154815692476, -0.006718684973494292, -0.006418094037185284, -0.006050428665713883, -0.00561749444824367, -0.005122259773145721, -0.004568837659333893, -0.00396243834213308, -0.0033092930181671085, -0.002616550123946141, -0.0018921464700013455, -0.0011446564367614345, -0.0003831232219587433, 0.0003831232219587433, 0.0011446564367614345, 0.0018921464700013455, 0.002616550123946141, 0.0033092930181671085, 0.00396243834213308, 0.004568837659333893, 0.005122259773145721, 0.00561749444824367, 0.006050428665713883, 0.006418094037185284, 0.006718684973494292, 0.00695154815692476, 0.007117144765255057, 0.007216987706776465, 0.007253556819444006, 0.007230195542097171, 0.007150992966122071, 0.007020655414423563, 0.006844371771024331, 0.006627676705955041, 0.0063763157195856155, 0.006096115586671624, 0.0057928633356701216, 0.005472196378502239, 0.005139505836369415, 0.004799854514864519, 0.00445791039156016, 0.004117895914250519, 0.003783552887617584, 0.0034581222660301832, 0.0031443377820499644, 0.0028444320313298203, 0.0025601534081131166, 0.0022927921408016716, 0.0020432136100095987, 0.0018118971353209142, 0.0015989784826439257, 0.0014042944611662893] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3766895266686962576_i": {
            "type": "arbitrary",
            "samples": [0.01592266768987036, 0.01857777204315171, 0.021588961148611543, 0.02498792402839221, 0.028806395952771204, 0.033075619856025106, 0.037825734921811356, 0.043085096953268745, 0.04887953787869817, 0.055231574632477354, 0.0621595806042154, 0.06967693576306537, 0.0777911743218606, 0.08650315128156519, 0.09580625126032391, 0.10568566453417727, 0.11611775607654642, 0.12706955347289367, 0.13849837881782598, 0.1503516480131679, 0.16256685824817907, 0.17507178086481573, 0.1877848723393205, 0.20061591083541075, 0.2134668598338051, 0.22623295388607134, 0.2388039947798945, 0.2510658395671019, 0.2629020552430802, 0.2741957086332468, 0.2848312544933537, 0.2946964802061052, 0.30368446197193943, 0.3116954852256655, 0.3186388812958499, 0.32443473313960525, 0.3290154053517367, 0.33232685752204755, 0.3343297052940832, 0.335, 0.3343297052940832, 0.33232685752204755, 0.3290154053517367, 0.32443473313960525, 0.3186388812958499, 0.3116954852256655, 0.30368446197193943, 0.2946964802061052, 0.2848312544933537, 0.2741957086332468, 0.2629020552430802, 0.2510658395671019, 0.2388039947798945, 0.22623295388607134, 0.2134668598338051, 0.20061591083541075, 0.1877848723393205, 0.17507178086481573, 0.16256685824817907, 0.1503516480131679, 0.13849837881782598, 0.12706955347289367, 0.11611775607654642, 0.10568566453417727, 0.09580625126032391, 0.08650315128156519, 0.0777911743218606, 0.06967693576306537, 0.0621595806042154, 0.055231574632477354, 0.04887953787869817, 0.043085096953268745, 0.037825734921811356, 0.033075619856025106, 0.028806395952771204, 0.02498792402839221, 0.021588961148611543, 0.01857777204315171, 0.01592266768987036, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3766895266686962576_q": {
            "type": "arbitrary",
            "samples": [-0.0013853585781125664, -0.0015749217691863823, -0.0017820308930980022, -0.002006847803465706, -0.0022492551838088452, -0.002508815179585385, -0.002784729877642327, -0.003075805099900944, -0.003380419084923245, -0.0036964976931522773, -0.0040214977799400715, -0.004352400327036788, -0.004685714801861693, -0.005017496020800731, -0.005343374527009357, -0.005658601157029207, -0.0059581060697765365, -0.006236572055613813, -0.006488521445359386, -0.00670841541564537, -0.006890763957287167, -0.007030244258750277, -0.007121824780187323, -0.0071608918779747024, -0.007143375507495718, -0.007065870303399493, -0.006925748228867062, -0.006721259011459795, -0.006451614750665633, -0.006117055393160644, -0.005718892221587521, -0.005259527080349461, -0.004742445750259665, -0.004172184659841816, -0.0035542709567138657, -0.002895136826134297, -0.0022020098014353937, -0.0014827816279330938, -0.0007458589841019147, 0.0, 0.0007458589841019147, 0.0014827816279330938, 0.0022020098014353937, 0.002895136826134297, 0.0035542709567138657, 0.004172184659841816, 0.004742445750259665, 0.005259527080349461, 0.005718892221587521, 0.006117055393160644, 0.006451614750665633, 0.006721259011459795, 0.006925748228867062, 0.007065870303399493, 0.007143375507495718, 0.0071608918779747024, 0.007121824780187323, 0.007030244258750277, 0.006890763957287167, 0.00670841541564537, 0.006488521445359386, 0.006236572055613813, 0.0059581060697765365, 0.005658601157029207, 0.005343374527009357, 0.005017496020800731, 0.004685714801861693, 0.004352400327036788, 0.0040214977799400715, 0.0036964976931522773, 0.003380419084923245, 0.003075805099900944, 0.002784729877642327, 0.002508815179585385, 0.0022492551838088452, 0.002006847803465706, 0.0017820308930980022, 0.0015749217691863823, 0.0013853585781125664, 0.0],
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
        "B4/acquisition_mixer_383": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_b5e": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

