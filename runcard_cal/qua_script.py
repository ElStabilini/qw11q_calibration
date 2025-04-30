
# Single QUA script generated at 2025-04-30 15:16:23.839107
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B1/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B3/acquisition")
    with for_(v1,0,(v1<256),(v1+1)):
        with for_(v8,0,(v8<=59),(v8+1)):
            with for_(v9,-1.99,(v9<-1.780414893617021),(v9+0.004234042553191486)):
                align()
                play("6288761140867283396", "B1/drive")
                play("-932845466564889230", "B3/drive")
                wait(11, "B3/flux")
                with if_((v8==0), unsafe=True):
                    play("3220552357337918655"*amp(v9), "B3/flux")
                with elif_((v8==1)):
                    play("-5361076971846915729"*amp(v9), "B3/flux")
                with elif_((v8==2)):
                    play("-5139582912648200481"*amp(v9), "B3/flux")
                with elif_((v8==3)):
                    play("-2775539060470640080"*amp(v9), "B3/flux")
                with elif_((v8==4)):
                    play("-2554045001271924832"*amp(v9), "B3/flux")
                with elif_((v8==5)):
                    play("6595923879405412735"*amp(v9), "B3/flux")
                with elif_((v8==6)):
                    play("-356285313268757969"*amp(v9), "B3/flux")
                with elif_((v8==7)):
                    play("-7949828192100829109"*amp(v9), "B3/flux")
                with elif_((v8==8)):
                    play("4876924503758006377"*amp(v9), "B3/flux")
                with elif_((v8==9)):
                    play("-8005528536318116075"*amp(v9), "B3/flux")
                with elif_((v8==10)):
                    play("200000752908875704"*amp(v9), "B3/flux")
                with elif_((v8==11)):
                    play("323961140014510892"*amp(v9), "B3/flux")
                with elif_((v8==12)):
                    play("-7343393916507039477"*amp(v9), "B3/flux")
                with elif_((v8==13)):
                    play("-7620588319923041691"*amp(v9), "B3/flux")
                with elif_((v8==14)):
                    play("2743214887216393003"*amp(v9), "B3/flux")
                with elif_((v8==15)):
                    play("-6293456045680741387"*amp(v9), "B3/flux")
                with elif_((v8==16)):
                    play("-6071961986482026139"*amp(v9), "B3/flux")
                with elif_((v8==17)):
                    play("4707427030705975108"*amp(v9), "B3/flux")
                with elif_((v8==18)):
                    play("-3874202298478859276"*amp(v9), "B3/flux")
                with elif_((v8==19)):
                    play("-2320490424456689454"*amp(v9), "B3/flux")
                with elif_((v8==20)):
                    play("-5687021770086951755"*amp(v9), "B3/flux")
                with elif_((v8==21)):
                    play("1580501577746620318"*amp(v9), "B3/flux")
                with elif_((v8==22)):
                    play("4399587033636480725"*amp(v9), "B3/flux")
                with elif_((v8==23)):
                    play("3778261265749787181"*amp(v9), "B3/flux")
                with elif_((v8==24)):
                    play("-8716413550953226485"*amp(v9), "B3/flux")
                with elif_((v8==25)):
                    play("1965441794141694702"*amp(v9), "B3/flux")
                with elif_((v8==26)):
                    play("7529732827775123866"*amp(v9), "B3/flux")
                with elif_((v8==27)):
                    play("-6394693475844424434"*amp(v9), "B3/flux")
                with elif_((v8==28)):
                    play("4384695541343576813"*amp(v9), "B3/flux")
                with elif_((v8==29)):
                    play("1189510045495873801"*amp(v9), "B3/flux")
                with elif_((v8==30)):
                    play("-6133713646554985238"*amp(v9), "B3/flux")
                with elif_((v8==31)):
                    play("1133809701278586835"*amp(v9), "B3/flux")
                with elif_((v8==32)):
                    play("5656127471368590151"*amp(v9), "B3/flux")
                with elif_((v8==33)):
                    play("-8983444696098337814"*amp(v9), "B3/flux")
                with elif_((v8==34)):
                    play("9186104974195211588"*amp(v9), "B3/flux")
                with elif_((v8==35)):
                    play("1518749917673661219"*amp(v9), "B3/flux")
                with elif_((v8==36)):
                    play("-833615751088633001"*amp(v9), "B3/flux")
                with elif_((v8==37)):
                    play("-1552475191068406605"*amp(v9), "B3/flux")
                with elif_((v8==38)):
                    play("-1330981131869691357"*amp(v9), "B3/flux")
                with elif_((v8==39)):
                    play("-1608175535285693571"*amp(v9), "B3/flux")
                with elif_((v8==40)):
                    play("866778556133475506"*amp(v9), "B3/flux")
                with elif_((v8==41)):
                    play("-4753212821717240624"*amp(v9), "B3/flux")
                with elif_((v8==42)):
                    play("-946040915474616973"*amp(v9), "B3/flux")
                with elif_((v8==43)):
                    play("9016607501143180319"*amp(v9), "B3/flux")
                with elif_((v8==44)):
                    play("-4907818802476367981"*amp(v9), "B3/flux")
                with elif_((v8==45)):
                    play("-4196926755539606951"*amp(v9), "B3/flux")
                with elif_((v8==46)):
                    play("325391014550396365"*amp(v9), "B3/flux")
                with elif_((v8==47)):
                    play("-1999167067536440088"*amp(v9), "B3/flux")
                with elif_((v8==48)):
                    play("2523150702553563228"*amp(v9), "B3/flux")
                with elif_((v8==49)):
                    play("2744644761752278476"*amp(v9), "B3/flux")
                with elif_((v8==50)):
                    play("3455536808689039506"*amp(v9), "B3/flux")
                with elif_((v8==51)):
                    play("6274622264578899913"*amp(v9), "B3/flux")
                with elif_((v8==52)):
                    play("-1392732791942650456"*amp(v9), "B3/flux")
                with elif_((v8==53)):
                    play("-8271129806927341931"*amp(v9), "B3/flux")
                with elif_((v8==54)):
                    play("-8049635747728626683"*amp(v9), "B3/flux")
                with elif_((v8==55)):
                    play("1026520955259231655"*amp(v9), "B3/flux")
                with elif_((v8==56)):
                    play("-121300861917637118"*amp(v9), "B3/flux")
                with elif_((v8==57)):
                    play("6259730772285996001"*amp(v9), "B3/flux")
                with elif_((v8==58)):
                    play("-7664695531333552299"*amp(v9), "B3/flux")
                with elif_((v8==59)):
                    play("2297952885284244993"*amp(v9), "B3/flux")
                wait(11, "B1/acquisition")
                wait(11, "B3/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B1/acquisition")
                with else_():
                    wait((v8/4), "B1/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B3/acquisition")
                with else_():
                    wait((v8/4), "B3/acquisition")
                wait(4, "B1/acquisition")
                wait(4, "B3/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B3/drive")
                with else_():
                    wait((v8/4), "B3/drive")
                wait(4, "B3/drive")
                wait(11, "B1/acquisition")
                wait(11, "B3/acquisition")
                play("-932845466564889230", "B3/drive")
                measure("2644281958318156425", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*-0.9988127626748439)-(v3*-0.04871411620717457))>0.0006911113845537218)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-5657642246959698803", "B3/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.48537056842023735)-(v6*0.8743085332486558))>0.0027410836483659383)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(50).buffer(60).average().save("2644281958318156425_B1|acquisition_shots")
        r2.buffer(50).buffer(60).average().save("-5657642246959698803_B3|acquisition_shots")


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
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
        "con3": {
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
            },
            "digital_outputs": {
                "1": {},
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
    },
    "octaves": {
        "octave3": {
            "connectivity": "con3",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 5800000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
            },
            "RF_inputs": {},
        },
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
            "operations": {
                "-4029810528850795609": "-4029810528850795609",
                "7309668643112294091": "7309668643112294091",
                "3220552357337918655": "3220552357337918655",
                "-5361076971846915729": "-5361076971846915729",
                "-5139582912648200481": "-5139582912648200481",
                "-2775539060470640080": "-2775539060470640080",
                "-2554045001271924832": "-2554045001271924832",
                "6595923879405412735": "6595923879405412735",
                "-356285313268757969": "-356285313268757969",
                "-7949828192100829109": "-7949828192100829109",
                "4876924503758006377": "4876924503758006377",
                "-8005528536318116075": "-8005528536318116075",
                "200000752908875704": "200000752908875704",
                "323961140014510892": "323961140014510892",
                "-7343393916507039477": "-7343393916507039477",
                "-7620588319923041691": "-7620588319923041691",
                "2743214887216393003": "2743214887216393003",
                "-6293456045680741387": "-6293456045680741387",
                "-6071961986482026139": "-6071961986482026139",
                "4707427030705975108": "4707427030705975108",
                "-3874202298478859276": "-3874202298478859276",
                "-2320490424456689454": "-2320490424456689454",
                "-5687021770086951755": "-5687021770086951755",
                "1580501577746620318": "1580501577746620318",
                "4399587033636480725": "4399587033636480725",
                "3778261265749787181": "3778261265749787181",
                "-8716413550953226485": "-8716413550953226485",
                "1965441794141694702": "1965441794141694702",
                "7529732827775123866": "7529732827775123866",
                "-6394693475844424434": "-6394693475844424434",
                "4384695541343576813": "4384695541343576813",
                "1189510045495873801": "1189510045495873801",
                "-6133713646554985238": "-6133713646554985238",
                "1133809701278586835": "1133809701278586835",
                "5656127471368590151": "5656127471368590151",
                "-8983444696098337814": "-8983444696098337814",
                "9186104974195211588": "9186104974195211588",
                "1518749917673661219": "1518749917673661219",
                "-833615751088633001": "-833615751088633001",
                "-1552475191068406605": "-1552475191068406605",
                "-1330981131869691357": "-1330981131869691357",
                "-1608175535285693571": "-1608175535285693571",
                "866778556133475506": "866778556133475506",
                "-4753212821717240624": "-4753212821717240624",
                "-946040915474616973": "-946040915474616973",
                "9016607501143180319": "9016607501143180319",
                "-4907818802476367981": "-4907818802476367981",
                "-4196926755539606951": "-4196926755539606951",
                "325391014550396365": "325391014550396365",
                "-1999167067536440088": "-1999167067536440088",
                "2523150702553563228": "2523150702553563228",
                "2744644761752278476": "2744644761752278476",
                "3455536808689039506": "3455536808689039506",
                "6274622264578899913": "6274622264578899913",
                "-1392732791942650456": "-1392732791942650456",
                "-8271129806927341931": "-8271129806927341931",
                "-8049635747728626683": "-8049635747728626683",
                "1026520955259231655": "1026520955259231655",
                "-121300861917637118": "-121300861917637118",
                "6259730772285996001": "6259730772285996001",
                "-7664695531333552299": "-7664695531333552299",
                "2297952885284244993": "2297952885284244993",
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
                "-932845466564889230": "-932845466564889230",
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
                "-5657642246959698803": "-5657642246959698803_B3/acquisition",
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
                "2644281958318156425": "2644281958318156425_B1/acquisition",
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
                "6288761140867283396": "6288761140867283396",
            },
        },
    },
    "pulses": {
        "6288761140867283396": {
            "length": 40,
            "waveforms": {
                "I": "6288761140867283396_i",
                "Q": "6288761140867283396_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-932845466564889230": {
            "length": 40,
            "waveforms": {
                "I": "-932845466564889230_i",
                "Q": "-932845466564889230_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4029810528850795609": {
            "length": 60,
            "waveforms": {
                "single": "-4029810528850795609",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2644281958318156425_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-499420078085948318_i",
                "Q": "-499420078085948318_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "-5657642246959698803_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-4580615797920718543_i",
                "Q": "-4580615797920718543_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "7309668643112294091": {
            "length": 60,
            "waveforms": {
                "single": "7309668643112294091",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3220552357337918655": {
            "length": 16,
            "waveforms": {
                "single": "3220552357337918655",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5361076971846915729": {
            "length": 16,
            "waveforms": {
                "single": "-5361076971846915729",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5139582912648200481": {
            "length": 16,
            "waveforms": {
                "single": "-5139582912648200481",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2775539060470640080": {
            "length": 16,
            "waveforms": {
                "single": "-2775539060470640080",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2554045001271924832": {
            "length": 16,
            "waveforms": {
                "single": "-2554045001271924832",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6595923879405412735": {
            "length": 16,
            "waveforms": {
                "single": "6595923879405412735",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-356285313268757969": {
            "length": 16,
            "waveforms": {
                "single": "-356285313268757969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7949828192100829109": {
            "length": 16,
            "waveforms": {
                "single": "-7949828192100829109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4876924503758006377": {
            "length": 16,
            "waveforms": {
                "single": "4876924503758006377",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8005528536318116075": {
            "length": 16,
            "waveforms": {
                "single": "-8005528536318116075",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "200000752908875704": {
            "length": 16,
            "waveforms": {
                "single": "200000752908875704",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "323961140014510892": {
            "length": 16,
            "waveforms": {
                "single": "323961140014510892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7343393916507039477": {
            "length": 16,
            "waveforms": {
                "single": "-7343393916507039477",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7620588319923041691": {
            "length": 16,
            "waveforms": {
                "single": "-7620588319923041691",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2743214887216393003": {
            "length": 16,
            "waveforms": {
                "single": "2743214887216393003",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6293456045680741387": {
            "length": 16,
            "waveforms": {
                "single": "-6293456045680741387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6071961986482026139": {
            "length": 16,
            "waveforms": {
                "single": "-6071961986482026139",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4707427030705975108": {
            "length": 20,
            "waveforms": {
                "single": "4707427030705975108",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3874202298478859276": {
            "length": 20,
            "waveforms": {
                "single": "-3874202298478859276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2320490424456689454": {
            "length": 20,
            "waveforms": {
                "single": "-2320490424456689454",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5687021770086951755": {
            "length": 20,
            "waveforms": {
                "single": "-5687021770086951755",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1580501577746620318": {
            "length": 24,
            "waveforms": {
                "single": "1580501577746620318",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4399587033636480725": {
            "length": 24,
            "waveforms": {
                "single": "4399587033636480725",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3778261265749787181": {
            "length": 24,
            "waveforms": {
                "single": "3778261265749787181",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8716413550953226485": {
            "length": 24,
            "waveforms": {
                "single": "-8716413550953226485",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1965441794141694702": {
            "length": 28,
            "waveforms": {
                "single": "1965441794141694702",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7529732827775123866": {
            "length": 28,
            "waveforms": {
                "single": "7529732827775123866",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6394693475844424434": {
            "length": 28,
            "waveforms": {
                "single": "-6394693475844424434",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4384695541343576813": {
            "length": 28,
            "waveforms": {
                "single": "4384695541343576813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1189510045495873801": {
            "length": 32,
            "waveforms": {
                "single": "1189510045495873801",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6133713646554985238": {
            "length": 32,
            "waveforms": {
                "single": "-6133713646554985238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1133809701278586835": {
            "length": 32,
            "waveforms": {
                "single": "1133809701278586835",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5656127471368590151": {
            "length": 32,
            "waveforms": {
                "single": "5656127471368590151",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8983444696098337814": {
            "length": 36,
            "waveforms": {
                "single": "-8983444696098337814",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9186104974195211588": {
            "length": 36,
            "waveforms": {
                "single": "9186104974195211588",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1518749917673661219": {
            "length": 36,
            "waveforms": {
                "single": "1518749917673661219",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-833615751088633001": {
            "length": 36,
            "waveforms": {
                "single": "-833615751088633001",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1552475191068406605": {
            "length": 40,
            "waveforms": {
                "single": "-1552475191068406605",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1330981131869691357": {
            "length": 40,
            "waveforms": {
                "single": "-1330981131869691357",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1608175535285693571": {
            "length": 40,
            "waveforms": {
                "single": "-1608175535285693571",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "866778556133475506": {
            "length": 40,
            "waveforms": {
                "single": "866778556133475506",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4753212821717240624": {
            "length": 44,
            "waveforms": {
                "single": "-4753212821717240624",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-946040915474616973": {
            "length": 44,
            "waveforms": {
                "single": "-946040915474616973",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9016607501143180319": {
            "length": 44,
            "waveforms": {
                "single": "9016607501143180319",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4907818802476367981": {
            "length": 44,
            "waveforms": {
                "single": "-4907818802476367981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4196926755539606951": {
            "length": 48,
            "waveforms": {
                "single": "-4196926755539606951",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "325391014550396365": {
            "length": 48,
            "waveforms": {
                "single": "325391014550396365",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1999167067536440088": {
            "length": 48,
            "waveforms": {
                "single": "-1999167067536440088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2523150702553563228": {
            "length": 48,
            "waveforms": {
                "single": "2523150702553563228",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2744644761752278476": {
            "length": 52,
            "waveforms": {
                "single": "2744644761752278476",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3455536808689039506": {
            "length": 52,
            "waveforms": {
                "single": "3455536808689039506",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6274622264578899913": {
            "length": 52,
            "waveforms": {
                "single": "6274622264578899913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1392732791942650456": {
            "length": 52,
            "waveforms": {
                "single": "-1392732791942650456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8271129806927341931": {
            "length": 56,
            "waveforms": {
                "single": "-8271129806927341931",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8049635747728626683": {
            "length": 56,
            "waveforms": {
                "single": "-8049635747728626683",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1026520955259231655": {
            "length": 56,
            "waveforms": {
                "single": "1026520955259231655",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-121300861917637118": {
            "length": 56,
            "waveforms": {
                "single": "-121300861917637118",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6259730772285996001": {
            "length": 60,
            "waveforms": {
                "single": "6259730772285996001",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7664695531333552299": {
            "length": 60,
            "waveforms": {
                "single": "-7664695531333552299",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2297952885284244993": {
            "length": 60,
            "waveforms": {
                "single": "2297952885284244993",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6288761140867283396_i": {
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "type": "arbitrary",
        },
        "6288761140867283396_q": {
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "type": "arbitrary",
        },
        "-932845466564889230_i": {
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "type": "arbitrary",
        },
        "-932845466564889230_q": {
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "type": "arbitrary",
        },
        "-4029810528850795609": {
            "sample": 0.21734999999999974,
            "type": "constant",
        },
        "-499420078085948318_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-499420078085948318_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-4580615797920718543_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-4580615797920718543_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7309668643112294091": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "3220552357337918655": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5361076971846915729": {
            "samples": [0.11809045226130653] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-5139582912648200481": {
            "samples": [0.11809045226130653] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-2775539060470640080": {
            "samples": [0.11809045226130653] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-2554045001271924832": {
            "samples": [0.11809045226130653] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "6595923879405412735": {
            "samples": [0.11809045226130653] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-356285313268757969": {
            "samples": [0.11809045226130653] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-7949828192100829109": {
            "samples": [0.11809045226130653] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "4876924503758006377": {
            "samples": [0.11809045226130653] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-8005528536318116075": {
            "samples": [0.11809045226130653] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "200000752908875704": {
            "samples": [0.11809045226130653] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "323961140014510892": {
            "samples": [0.11809045226130653] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-7343393916507039477": {
            "samples": [0.11809045226130653] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-7620588319923041691": {
            "samples": [0.11809045226130653] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2743214887216393003": {
            "samples": [0.11809045226130653] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6293456045680741387": {
            "samples": [0.11809045226130653] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-6071961986482026139": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "4707427030705975108": {
            "samples": [0.11809045226130653] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3874202298478859276": {
            "samples": [0.11809045226130653] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2320490424456689454": {
            "samples": [0.11809045226130653] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5687021770086951755": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "1580501577746620318": {
            "samples": [0.11809045226130653] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4399587033636480725": {
            "samples": [0.11809045226130653] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3778261265749787181": {
            "samples": [0.11809045226130653] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-8716413550953226485": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "1965441794141694702": {
            "samples": [0.11809045226130653] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7529732827775123866": {
            "samples": [0.11809045226130653] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6394693475844424434": {
            "samples": [0.11809045226130653] * 27 + [0.0],
            "type": "arbitrary",
        },
        "4384695541343576813": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "1189510045495873801": {
            "samples": [0.11809045226130653] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6133713646554985238": {
            "samples": [0.11809045226130653] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1133809701278586835": {
            "samples": [0.11809045226130653] * 31 + [0.0],
            "type": "arbitrary",
        },
        "5656127471368590151": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-8983444696098337814": {
            "samples": [0.11809045226130653] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "9186104974195211588": {
            "samples": [0.11809045226130653] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1518749917673661219": {
            "samples": [0.11809045226130653] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-833615751088633001": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-1552475191068406605": {
            "samples": [0.11809045226130653] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1330981131869691357": {
            "samples": [0.11809045226130653] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1608175535285693571": {
            "samples": [0.11809045226130653] * 39 + [0.0],
            "type": "arbitrary",
        },
        "866778556133475506": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-4753212821717240624": {
            "samples": [0.11809045226130653] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-946040915474616973": {
            "samples": [0.11809045226130653] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9016607501143180319": {
            "samples": [0.11809045226130653] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-4907818802476367981": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-4196926755539606951": {
            "samples": [0.11809045226130653] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "325391014550396365": {
            "samples": [0.11809045226130653] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1999167067536440088": {
            "samples": [0.11809045226130653] * 47 + [0.0],
            "type": "arbitrary",
        },
        "2523150702553563228": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "2744644761752278476": {
            "samples": [0.11809045226130653] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3455536808689039506": {
            "samples": [0.11809045226130653] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6274622264578899913": {
            "samples": [0.11809045226130653] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-1392732791942650456": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "-8271129806927341931": {
            "samples": [0.11809045226130653] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8049635747728626683": {
            "samples": [0.11809045226130653] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1026520955259231655": {
            "samples": [0.11809045226130653] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-121300861917637118": {
            "sample": 0.11809045226130653,
            "type": "constant",
        },
        "6259730772285996001": {
            "samples": [0.11809045226130653] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7664695531333552299": {
            "samples": [0.11809045226130653] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2297952885284244993": {
            "samples": [0.11809045226130653] * 59 + [0.0],
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
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.05128942239382605,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
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
        "con3": {
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
            },
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
            "operations": {
                "-4029810528850795609": "-4029810528850795609",
                "7309668643112294091": "7309668643112294091",
                "3220552357337918655": "3220552357337918655",
                "-5361076971846915729": "-5361076971846915729",
                "-5139582912648200481": "-5139582912648200481",
                "-2775539060470640080": "-2775539060470640080",
                "-2554045001271924832": "-2554045001271924832",
                "6595923879405412735": "6595923879405412735",
                "-356285313268757969": "-356285313268757969",
                "-7949828192100829109": "-7949828192100829109",
                "4876924503758006377": "4876924503758006377",
                "-8005528536318116075": "-8005528536318116075",
                "200000752908875704": "200000752908875704",
                "323961140014510892": "323961140014510892",
                "-7343393916507039477": "-7343393916507039477",
                "-7620588319923041691": "-7620588319923041691",
                "2743214887216393003": "2743214887216393003",
                "-6293456045680741387": "-6293456045680741387",
                "-6071961986482026139": "-6071961986482026139",
                "4707427030705975108": "4707427030705975108",
                "-3874202298478859276": "-3874202298478859276",
                "-2320490424456689454": "-2320490424456689454",
                "-5687021770086951755": "-5687021770086951755",
                "1580501577746620318": "1580501577746620318",
                "4399587033636480725": "4399587033636480725",
                "3778261265749787181": "3778261265749787181",
                "-8716413550953226485": "-8716413550953226485",
                "1965441794141694702": "1965441794141694702",
                "7529732827775123866": "7529732827775123866",
                "-6394693475844424434": "-6394693475844424434",
                "4384695541343576813": "4384695541343576813",
                "1189510045495873801": "1189510045495873801",
                "-6133713646554985238": "-6133713646554985238",
                "1133809701278586835": "1133809701278586835",
                "5656127471368590151": "5656127471368590151",
                "-8983444696098337814": "-8983444696098337814",
                "9186104974195211588": "9186104974195211588",
                "1518749917673661219": "1518749917673661219",
                "-833615751088633001": "-833615751088633001",
                "-1552475191068406605": "-1552475191068406605",
                "-1330981131869691357": "-1330981131869691357",
                "-1608175535285693571": "-1608175535285693571",
                "866778556133475506": "866778556133475506",
                "-4753212821717240624": "-4753212821717240624",
                "-946040915474616973": "-946040915474616973",
                "9016607501143180319": "9016607501143180319",
                "-4907818802476367981": "-4907818802476367981",
                "-4196926755539606951": "-4196926755539606951",
                "325391014550396365": "325391014550396365",
                "-1999167067536440088": "-1999167067536440088",
                "2523150702553563228": "2523150702553563228",
                "2744644761752278476": "2744644761752278476",
                "3455536808689039506": "3455536808689039506",
                "6274622264578899913": "6274622264578899913",
                "-1392732791942650456": "-1392732791942650456",
                "-8271129806927341931": "-8271129806927341931",
                "-8049635747728626683": "-8049635747728626683",
                "1026520955259231655": "1026520955259231655",
                "-121300861917637118": "-121300861917637118",
                "6259730772285996001": "6259730772285996001",
                "-7664695531333552299": "-7664695531333552299",
                "2297952885284244993": "2297952885284244993",
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
                "-932845466564889230": "-932845466564889230",
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
                "mixer": "B3/drive_mixer_b14",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-5657642246959698803": "-5657642246959698803_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_d02",
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
                "2644281958318156425": "2644281958318156425_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_4dc",
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
                "6288761140867283396": "6288761140867283396",
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
                "mixer": "B1/drive_mixer_809",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
        },
    },
    "pulses": {
        "6288761140867283396": {
            "length": 40,
            "waveforms": {
                "I": "6288761140867283396_i",
                "Q": "6288761140867283396_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-932845466564889230": {
            "length": 40,
            "waveforms": {
                "I": "-932845466564889230_i",
                "Q": "-932845466564889230_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4029810528850795609": {
            "length": 60,
            "waveforms": {
                "single": "-4029810528850795609",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2644281958318156425_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-499420078085948318_i",
                "Q": "-499420078085948318_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5657642246959698803_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-4580615797920718543_i",
                "Q": "-4580615797920718543_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7309668643112294091": {
            "length": 60,
            "waveforms": {
                "single": "7309668643112294091",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3220552357337918655": {
            "length": 16,
            "waveforms": {
                "single": "3220552357337918655",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5361076971846915729": {
            "length": 16,
            "waveforms": {
                "single": "-5361076971846915729",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5139582912648200481": {
            "length": 16,
            "waveforms": {
                "single": "-5139582912648200481",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2775539060470640080": {
            "length": 16,
            "waveforms": {
                "single": "-2775539060470640080",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2554045001271924832": {
            "length": 16,
            "waveforms": {
                "single": "-2554045001271924832",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6595923879405412735": {
            "length": 16,
            "waveforms": {
                "single": "6595923879405412735",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-356285313268757969": {
            "length": 16,
            "waveforms": {
                "single": "-356285313268757969",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7949828192100829109": {
            "length": 16,
            "waveforms": {
                "single": "-7949828192100829109",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4876924503758006377": {
            "length": 16,
            "waveforms": {
                "single": "4876924503758006377",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8005528536318116075": {
            "length": 16,
            "waveforms": {
                "single": "-8005528536318116075",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "200000752908875704": {
            "length": 16,
            "waveforms": {
                "single": "200000752908875704",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "323961140014510892": {
            "length": 16,
            "waveforms": {
                "single": "323961140014510892",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7343393916507039477": {
            "length": 16,
            "waveforms": {
                "single": "-7343393916507039477",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7620588319923041691": {
            "length": 16,
            "waveforms": {
                "single": "-7620588319923041691",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2743214887216393003": {
            "length": 16,
            "waveforms": {
                "single": "2743214887216393003",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6293456045680741387": {
            "length": 16,
            "waveforms": {
                "single": "-6293456045680741387",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6071961986482026139": {
            "length": 16,
            "waveforms": {
                "single": "-6071961986482026139",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4707427030705975108": {
            "length": 20,
            "waveforms": {
                "single": "4707427030705975108",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3874202298478859276": {
            "length": 20,
            "waveforms": {
                "single": "-3874202298478859276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2320490424456689454": {
            "length": 20,
            "waveforms": {
                "single": "-2320490424456689454",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5687021770086951755": {
            "length": 20,
            "waveforms": {
                "single": "-5687021770086951755",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1580501577746620318": {
            "length": 24,
            "waveforms": {
                "single": "1580501577746620318",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4399587033636480725": {
            "length": 24,
            "waveforms": {
                "single": "4399587033636480725",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3778261265749787181": {
            "length": 24,
            "waveforms": {
                "single": "3778261265749787181",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8716413550953226485": {
            "length": 24,
            "waveforms": {
                "single": "-8716413550953226485",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1965441794141694702": {
            "length": 28,
            "waveforms": {
                "single": "1965441794141694702",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7529732827775123866": {
            "length": 28,
            "waveforms": {
                "single": "7529732827775123866",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6394693475844424434": {
            "length": 28,
            "waveforms": {
                "single": "-6394693475844424434",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4384695541343576813": {
            "length": 28,
            "waveforms": {
                "single": "4384695541343576813",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1189510045495873801": {
            "length": 32,
            "waveforms": {
                "single": "1189510045495873801",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6133713646554985238": {
            "length": 32,
            "waveforms": {
                "single": "-6133713646554985238",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1133809701278586835": {
            "length": 32,
            "waveforms": {
                "single": "1133809701278586835",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5656127471368590151": {
            "length": 32,
            "waveforms": {
                "single": "5656127471368590151",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8983444696098337814": {
            "length": 36,
            "waveforms": {
                "single": "-8983444696098337814",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9186104974195211588": {
            "length": 36,
            "waveforms": {
                "single": "9186104974195211588",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1518749917673661219": {
            "length": 36,
            "waveforms": {
                "single": "1518749917673661219",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-833615751088633001": {
            "length": 36,
            "waveforms": {
                "single": "-833615751088633001",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1552475191068406605": {
            "length": 40,
            "waveforms": {
                "single": "-1552475191068406605",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1330981131869691357": {
            "length": 40,
            "waveforms": {
                "single": "-1330981131869691357",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1608175535285693571": {
            "length": 40,
            "waveforms": {
                "single": "-1608175535285693571",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "866778556133475506": {
            "length": 40,
            "waveforms": {
                "single": "866778556133475506",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4753212821717240624": {
            "length": 44,
            "waveforms": {
                "single": "-4753212821717240624",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-946040915474616973": {
            "length": 44,
            "waveforms": {
                "single": "-946040915474616973",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9016607501143180319": {
            "length": 44,
            "waveforms": {
                "single": "9016607501143180319",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4907818802476367981": {
            "length": 44,
            "waveforms": {
                "single": "-4907818802476367981",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4196926755539606951": {
            "length": 48,
            "waveforms": {
                "single": "-4196926755539606951",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "325391014550396365": {
            "length": 48,
            "waveforms": {
                "single": "325391014550396365",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1999167067536440088": {
            "length": 48,
            "waveforms": {
                "single": "-1999167067536440088",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2523150702553563228": {
            "length": 48,
            "waveforms": {
                "single": "2523150702553563228",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2744644761752278476": {
            "length": 52,
            "waveforms": {
                "single": "2744644761752278476",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3455536808689039506": {
            "length": 52,
            "waveforms": {
                "single": "3455536808689039506",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6274622264578899913": {
            "length": 52,
            "waveforms": {
                "single": "6274622264578899913",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1392732791942650456": {
            "length": 52,
            "waveforms": {
                "single": "-1392732791942650456",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8271129806927341931": {
            "length": 56,
            "waveforms": {
                "single": "-8271129806927341931",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8049635747728626683": {
            "length": 56,
            "waveforms": {
                "single": "-8049635747728626683",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1026520955259231655": {
            "length": 56,
            "waveforms": {
                "single": "1026520955259231655",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-121300861917637118": {
            "length": 56,
            "waveforms": {
                "single": "-121300861917637118",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6259730772285996001": {
            "length": 60,
            "waveforms": {
                "single": "6259730772285996001",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7664695531333552299": {
            "length": 60,
            "waveforms": {
                "single": "-7664695531333552299",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2297952885284244993": {
            "length": 60,
            "waveforms": {
                "single": "2297952885284244993",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "6288761140867283396_i": {
            "type": "arbitrary",
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6288761140867283396_q": {
            "type": "arbitrary",
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-932845466564889230_i": {
            "type": "arbitrary",
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-932845466564889230_q": {
            "type": "arbitrary",
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4029810528850795609": {
            "type": "constant",
            "sample": 0.21734999999999974,
        },
        "-499420078085948318_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-499420078085948318_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-4580615797920718543_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-4580615797920718543_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7309668643112294091": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "3220552357337918655": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5361076971846915729": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5139582912648200481": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2775539060470640080": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2554045001271924832": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6595923879405412735": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-356285313268757969": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7949828192100829109": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4876924503758006377": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8005528536318116075": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "200000752908875704": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "323961140014510892": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7343393916507039477": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7620588319923041691": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2743214887216393003": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6293456045680741387": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6071961986482026139": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "4707427030705975108": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3874202298478859276": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2320490424456689454": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5687021770086951755": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "1580501577746620318": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4399587033636480725": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3778261265749787181": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8716413550953226485": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "1965441794141694702": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7529732827775123866": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6394693475844424434": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4384695541343576813": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "1189510045495873801": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6133713646554985238": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1133809701278586835": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5656127471368590151": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-8983444696098337814": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9186104974195211588": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1518749917673661219": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-833615751088633001": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-1552475191068406605": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1330981131869691357": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1608175535285693571": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "866778556133475506": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-4753212821717240624": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-946040915474616973": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9016607501143180319": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4907818802476367981": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-4196926755539606951": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "325391014550396365": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1999167067536440088": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2523150702553563228": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "2744644761752278476": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3455536808689039506": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6274622264578899913": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1392732791942650456": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "-8271129806927341931": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8049635747728626683": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1026520955259231655": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-121300861917637118": {
            "type": "constant",
            "sample": 0.11809045226130653,
        },
        "6259730772285996001": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7664695531333552299": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2297952885284244993": {
            "type": "arbitrary",
            "samples": [0.11809045226130653] * 59 + [0.0],
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
    },
    "mixers": {
        "B3/drive_mixer_b14": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_d02": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_4dc": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_809": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

