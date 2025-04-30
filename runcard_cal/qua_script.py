
# Single QUA script generated at 2025-04-30 15:11:50.166437
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
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B2/acquisition")
    with for_(v1,0,(v1<256),(v1+1)):
        with for_(v8,0,(v8<=59),(v8+1)):
            with for_(v9,-1.9900000000000002,(v9<-1.79299),(v9+0.003980000000000095)):
                align()
                play("-5657030128259699195", "B1/drive")
                play("-899358143601977096", "B2/drive")
                wait(11, "B2/flux")
                with if_((v8==0), unsafe=True):
                    play("-5985338580302693505"*amp(v9), "B2/flux")
                with elif_((v8==1)):
                    play("4267554387595132513"*amp(v9), "B2/flux")
                with elif_((v8==2)):
                    play("4489048446793847761"*amp(v9), "B2/flux")
                with elif_((v8==3)):
                    play("2164490364707011308"*amp(v9), "B2/flux")
                with elif_((v8==4)):
                    play("2288450751812646496"*amp(v9), "B2/flux")
                with elif_((v8==5)):
                    play("1667124983925952952"*amp(v9), "B2/flux")
                with elif_((v8==6)):
                    play("-6526726121885772646"*amp(v9), "B2/flux")
                with elif_((v8==7)):
                    play("-962435088252343482"*amp(v9), "B2/flux")
                with elif_((v8==8)):
                    play("-4328966433882605783"*amp(v9), "B2/flux")
                with elif_((v8==9)):
                    play("-4107472374683890535"*amp(v9), "B2/flux")
                with elif_((v8==10)):
                    play("-300300468441266884"*amp(v9), "B2/flux")
                with elif_((v8==11)):
                    play("1125737442342873811"*amp(v9), "B2/flux")
                with elif_((v8==12)):
                    play("-356000812658553850"*amp(v9), "B2/flux")
                with elif_((v8==13)):
                    play("3323497130346040674"*amp(v9), "B2/flux")
                with elif_((v8==14)):
                    play("971131461583746454"*amp(v9), "B2/flux")
                with elif_((v8==15)):
                    play("-4648859916266969676"*amp(v9), "B2/flux")
                with elif_((v8==16)):
                    play("-6973417998353806129"*amp(v9), "B2/flux")
                with elif_((v8==17)):
                    play("-8896821289919005180"*amp(v9), "B2/flux")
                with elif_((v8==18)):
                    play("1356071677978820838"*amp(v9), "B2/flux")
                with elif_((v8==19)):
                    play("8623595025812392911"*amp(v9), "B2/flux")
                with elif_((v8==20)):
                    play("-4430203864046288830"*amp(v9), "B2/flux")
                with elif_((v8==21)):
                    play("-7625389359893991842"*amp(v9), "B2/flux")
                with elif_((v8==22)):
                    play("3153999657294009405"*amp(v9), "B2/flux")
                with elif_((v8==23)):
                    play("9008535242207467295"*amp(v9), "B2/flux")
                with elif_((v8==24)):
                    play("-3873917797868655157"*amp(v9), "B2/flux")
                with elif_((v8==25)):
                    play("-7240449143498917458"*amp(v9), "B2/flux")
                with elif_((v8==26)):
                    play("-7018955084300202210"*amp(v9), "B2/flux")
                with elif_((v8==27)):
                    play("-8166776901477070983"*amp(v9), "B2/flux")
                with elif_((v8==28)):
                    play("909379801510787355"*amp(v9), "B2/flux")
                with elif_((v8==29)):
                    play("8176903149344359428"*amp(v9), "B2/flux")
                with elif_((v8==30)):
                    play("412014420729728999"*amp(v9), "B2/flux")
                with elif_((v8==31)):
                    play("633508479928444247"*amp(v9), "B2/flux")
                with elif_((v8==32)):
                    play("-514313337248424526"*amp(v9), "B2/flux")
                with elif_((v8==33)):
                    play("8561843365739433812"*amp(v9), "B2/flux")
                with elif_((v8==34)):
                    play("-5362582937880114488"*amp(v9), "B2/flux")
                with elif_((v8==35)):
                    play("8064477984958375456"*amp(v9), "B2/flux")
                with elif_((v8==36)):
                    play("5712112316196081236"*amp(v9), "B2/flux")
                with elif_((v8==37)):
                    play("5434917912780079022"*amp(v9), "B2/flux")
                with elif_((v8==38)):
                    play("-2232437143741471347"*amp(v9), "B2/flux")
                with elif_((v8==39)):
                    play("2289880626348531969"*amp(v9), "B2/flux")
                with elif_((v8==40)):
                    play("6097052532591155620"*amp(v9), "B2/flux")
                with elif_((v8==41)):
                    play("4487640314351698832"*amp(v9), "B2/flux")
                with elif_((v8==42)):
                    play("-961005213716458009"*amp(v9), "B2/flux")
                with elif_((v8==43)):
                    play("-2884408505281657060"*amp(v9), "B2/flux")
                with elif_((v8==44)):
                    play("-8504399883132373190"*amp(v9), "B2/flux")
                with elif_((v8==45)):
                    play("5043926380529332505"*amp(v9), "B2/flux")
                with elif_((v8==46)):
                    play("-6306640195129206327"*amp(v9), "B2/flux")
                with elif_((v8==47)):
                    play("-2499468288886582676"*amp(v9), "B2/flux")
                with elif_((v8==48)):
                    play("2120383153296500700"*amp(v9), "B2/flux")
                with elif_((v8==49)):
                    play("-5129028361064879110"*amp(v9), "B2/flux")
                with elif_((v8==50)):
                    play("5650360656123122137"*amp(v9), "B2/flux")
                with elif_((v8==51)):
                    play("-1228036358861569338"*amp(v9), "B2/flux")
                with elif_((v8==52)):
                    play("-8895391415383119707"*amp(v9), "B2/flux")
                with elif_((v8==53)):
                    play("-9172585818799121921"*amp(v9), "B2/flux")
                with elif_((v8==54)):
                    play("6921792586148135475"*amp(v9), "B2/flux")
                with elif_((v8==55)):
                    play("-5143919853357783022"*amp(v9), "B2/flux")
                with elif_((v8==56)):
                    play("-621602083267779706"*amp(v9), "B2/flux")
                with elif_((v8==57)):
                    play("-1242927851154473250"*amp(v9), "B2/flux")
                with elif_((v8==58)):
                    play("-4093981982531484932"*amp(v9), "B2/flux")
                with elif_((v8==59)):
                    play("-3872487923332769684"*amp(v9), "B2/flux")
                wait(11, "B1/acquisition")
                wait(11, "B2/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B1/acquisition")
                with else_():
                    wait((v8/4), "B1/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B2/acquisition")
                with else_():
                    wait((v8/4), "B2/acquisition")
                wait(4, "B1/acquisition")
                wait(4, "B2/acquisition")
                with if_(((v8/4)<4)):
                    wait(4, "B2/drive")
                with else_():
                    wait((v8/4), "B2/drive")
                wait(4, "B2/drive")
                wait(11, "B1/acquisition")
                wait(11, "B2/acquisition")
                play("-899358143601977096", "B2/drive")
                measure("-5755598658197327036", "B1/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*-0.9988127626748439)-(v3*-0.04871411620717457))>0.0006911113845537218)))
                r1 = declare_stream()
                save(v4, r1)
                measure("5741643966098266678", "B2/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*-0.195212174212656)-(v6*-0.9807610346252382))>0.002446646735995352)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(50).buffer(60).average().save("-5755598658197327036_B1|acquisition_shots")
        r2.buffer(50).buffer(60).average().save("5741643966098266678_B2|acquisition_shots")


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
            "operations": {
                "-5867388394385087965": "-5867388394385087965",
                "6809367421762151503": "6809367421762151503",
                "-5985338580302693505": "-5985338580302693505",
                "4267554387595132513": "4267554387595132513",
                "4489048446793847761": "4489048446793847761",
                "2164490364707011308": "2164490364707011308",
                "2288450751812646496": "2288450751812646496",
                "1667124983925952952": "1667124983925952952",
                "-6526726121885772646": "-6526726121885772646",
                "-962435088252343482": "-962435088252343482",
                "-4328966433882605783": "-4328966433882605783",
                "-4107472374683890535": "-4107472374683890535",
                "-300300468441266884": "-300300468441266884",
                "1125737442342873811": "1125737442342873811",
                "-356000812658553850": "-356000812658553850",
                "3323497130346040674": "3323497130346040674",
                "971131461583746454": "971131461583746454",
                "-4648859916266969676": "-4648859916266969676",
                "-6973417998353806129": "-6973417998353806129",
                "-8896821289919005180": "-8896821289919005180",
                "1356071677978820838": "1356071677978820838",
                "8623595025812392911": "8623595025812392911",
                "-4430203864046288830": "-4430203864046288830",
                "-7625389359893991842": "-7625389359893991842",
                "3153999657294009405": "3153999657294009405",
                "9008535242207467295": "9008535242207467295",
                "-3873917797868655157": "-3873917797868655157",
                "-7240449143498917458": "-7240449143498917458",
                "-7018955084300202210": "-7018955084300202210",
                "-8166776901477070983": "-8166776901477070983",
                "909379801510787355": "909379801510787355",
                "8176903149344359428": "8176903149344359428",
                "412014420729728999": "412014420729728999",
                "633508479928444247": "633508479928444247",
                "-514313337248424526": "-514313337248424526",
                "8561843365739433812": "8561843365739433812",
                "-5362582937880114488": "-5362582937880114488",
                "8064477984958375456": "8064477984958375456",
                "5712112316196081236": "5712112316196081236",
                "5434917912780079022": "5434917912780079022",
                "-2232437143741471347": "-2232437143741471347",
                "2289880626348531969": "2289880626348531969",
                "6097052532591155620": "6097052532591155620",
                "4487640314351698832": "4487640314351698832",
                "-961005213716458009": "-961005213716458009",
                "-2884408505281657060": "-2884408505281657060",
                "-8504399883132373190": "-8504399883132373190",
                "5043926380529332505": "5043926380529332505",
                "-6306640195129206327": "-6306640195129206327",
                "-2499468288886582676": "-2499468288886582676",
                "2120383153296500700": "2120383153296500700",
                "-5129028361064879110": "-5129028361064879110",
                "5650360656123122137": "5650360656123122137",
                "-1228036358861569338": "-1228036358861569338",
                "-8895391415383119707": "-8895391415383119707",
                "-9172585818799121921": "-9172585818799121921",
                "6921792586148135475": "6921792586148135475",
                "-5143919853357783022": "-5143919853357783022",
                "-621602083267779706": "-621602083267779706",
                "-1242927851154473250": "-1242927851154473250",
                "-4093981982531484932": "-4093981982531484932",
                "-3872487923332769684": "-3872487923332769684",
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
                "5741643966098266678": "5741643966098266678_B2/acquisition",
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
                "-193334924239390645": "-193334924239390645_B4/acquisition",
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
                "-899358143601977096": "-899358143601977096",
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
                "5211710689442696482": "5211710689442696482",
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
                "8873580944738058236": "8873580944738058236_B3/acquisition",
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
                "-5657030128259699195": "-5657030128259699195",
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
                "-5063599797661085433": "-5063599797661085433",
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
                "-5755598658197327036": "-5755598658197327036_B1/acquisition",
            },
        },
    },
    "pulses": {
        "-899358143601977096": {
            "length": 40,
            "waveforms": {
                "I": "-899358143601977096_i",
                "Q": "-899358143601977096_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5211710689442696482": {
            "length": 40,
            "waveforms": {
                "I": "5211710689442696482_i",
                "Q": "5211710689442696482_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2833019928693392154": {
            "length": 60,
            "waveforms": {
                "single": "2833019928693392154",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5741643966098266678_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5000477159223041459_i",
                "Q": "5000477159223041459_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-193334924239390645_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "2740853735462715916_i",
                "Q": "2740853735462715916_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "6809367421762151503": {
            "length": 60,
            "waveforms": {
                "single": "6809367421762151503",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5985338580302693505": {
            "length": 16,
            "waveforms": {
                "single": "-5985338580302693505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4267554387595132513": {
            "length": 16,
            "waveforms": {
                "single": "4267554387595132513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4489048446793847761": {
            "length": 16,
            "waveforms": {
                "single": "4489048446793847761",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2164490364707011308": {
            "length": 16,
            "waveforms": {
                "single": "2164490364707011308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2288450751812646496": {
            "length": 16,
            "waveforms": {
                "single": "2288450751812646496",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1667124983925952952": {
            "length": 16,
            "waveforms": {
                "single": "1667124983925952952",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6526726121885772646": {
            "length": 16,
            "waveforms": {
                "single": "-6526726121885772646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-962435088252343482": {
            "length": 16,
            "waveforms": {
                "single": "-962435088252343482",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4328966433882605783": {
            "length": 16,
            "waveforms": {
                "single": "-4328966433882605783",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4107472374683890535": {
            "length": 16,
            "waveforms": {
                "single": "-4107472374683890535",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-300300468441266884": {
            "length": 16,
            "waveforms": {
                "single": "-300300468441266884",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1125737442342873811": {
            "length": 16,
            "waveforms": {
                "single": "1125737442342873811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-356000812658553850": {
            "length": 16,
            "waveforms": {
                "single": "-356000812658553850",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3323497130346040674": {
            "length": 16,
            "waveforms": {
                "single": "3323497130346040674",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "971131461583746454": {
            "length": 16,
            "waveforms": {
                "single": "971131461583746454",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4648859916266969676": {
            "length": 16,
            "waveforms": {
                "single": "-4648859916266969676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6973417998353806129": {
            "length": 16,
            "waveforms": {
                "single": "-6973417998353806129",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8896821289919005180": {
            "length": 20,
            "waveforms": {
                "single": "-8896821289919005180",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1356071677978820838": {
            "length": 20,
            "waveforms": {
                "single": "1356071677978820838",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8623595025812392911": {
            "length": 20,
            "waveforms": {
                "single": "8623595025812392911",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4430203864046288830": {
            "length": 20,
            "waveforms": {
                "single": "-4430203864046288830",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7625389359893991842": {
            "length": 24,
            "waveforms": {
                "single": "-7625389359893991842",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3153999657294009405": {
            "length": 24,
            "waveforms": {
                "single": "3153999657294009405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9008535242207467295": {
            "length": 24,
            "waveforms": {
                "single": "9008535242207467295",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3873917797868655157": {
            "length": 24,
            "waveforms": {
                "single": "-3873917797868655157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7240449143498917458": {
            "length": 28,
            "waveforms": {
                "single": "-7240449143498917458",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7018955084300202210": {
            "length": 28,
            "waveforms": {
                "single": "-7018955084300202210",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8166776901477070983": {
            "length": 28,
            "waveforms": {
                "single": "-8166776901477070983",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "909379801510787355": {
            "length": 28,
            "waveforms": {
                "single": "909379801510787355",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8176903149344359428": {
            "length": 32,
            "waveforms": {
                "single": "8176903149344359428",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "412014420729728999": {
            "length": 32,
            "waveforms": {
                "single": "412014420729728999",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "633508479928444247": {
            "length": 32,
            "waveforms": {
                "single": "633508479928444247",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-514313337248424526": {
            "length": 32,
            "waveforms": {
                "single": "-514313337248424526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8561843365739433812": {
            "length": 36,
            "waveforms": {
                "single": "8561843365739433812",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5362582937880114488": {
            "length": 36,
            "waveforms": {
                "single": "-5362582937880114488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8064477984958375456": {
            "length": 36,
            "waveforms": {
                "single": "8064477984958375456",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5712112316196081236": {
            "length": 36,
            "waveforms": {
                "single": "5712112316196081236",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5434917912780079022": {
            "length": 40,
            "waveforms": {
                "single": "5434917912780079022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2232437143741471347": {
            "length": 40,
            "waveforms": {
                "single": "-2232437143741471347",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2289880626348531969": {
            "length": 40,
            "waveforms": {
                "single": "2289880626348531969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6097052532591155620": {
            "length": 40,
            "waveforms": {
                "single": "6097052532591155620",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4487640314351698832": {
            "length": 44,
            "waveforms": {
                "single": "4487640314351698832",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-961005213716458009": {
            "length": 44,
            "waveforms": {
                "single": "-961005213716458009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2884408505281657060": {
            "length": 44,
            "waveforms": {
                "single": "-2884408505281657060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8504399883132373190": {
            "length": 44,
            "waveforms": {
                "single": "-8504399883132373190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5043926380529332505": {
            "length": 48,
            "waveforms": {
                "single": "5043926380529332505",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6306640195129206327": {
            "length": 48,
            "waveforms": {
                "single": "-6306640195129206327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2499468288886582676": {
            "length": 48,
            "waveforms": {
                "single": "-2499468288886582676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2120383153296500700": {
            "length": 48,
            "waveforms": {
                "single": "2120383153296500700",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5129028361064879110": {
            "length": 52,
            "waveforms": {
                "single": "-5129028361064879110",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5650360656123122137": {
            "length": 52,
            "waveforms": {
                "single": "5650360656123122137",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1228036358861569338": {
            "length": 52,
            "waveforms": {
                "single": "-1228036358861569338",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8895391415383119707": {
            "length": 52,
            "waveforms": {
                "single": "-8895391415383119707",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9172585818799121921": {
            "length": 56,
            "waveforms": {
                "single": "-9172585818799121921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6921792586148135475": {
            "length": 56,
            "waveforms": {
                "single": "6921792586148135475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5143919853357783022": {
            "length": 56,
            "waveforms": {
                "single": "-5143919853357783022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-621602083267779706": {
            "length": 56,
            "waveforms": {
                "single": "-621602083267779706",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1242927851154473250": {
            "length": 60,
            "waveforms": {
                "single": "-1242927851154473250",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4093981982531484932": {
            "length": 60,
            "waveforms": {
                "single": "-4093981982531484932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3872487923332769684": {
            "length": 60,
            "waveforms": {
                "single": "-3872487923332769684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5657030128259699195": {
            "length": 40,
            "waveforms": {
                "I": "-5657030128259699195_i",
                "Q": "-5657030128259699195_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5063599797661085433": {
            "length": 40,
            "waveforms": {
                "I": "-5063599797661085433_i",
                "Q": "-5063599797661085433_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1551283749241561855": {
            "length": 60,
            "waveforms": {
                "single": "-1551283749241561855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5755598658197327036_B1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-3187497921659568058_i",
                "Q": "-3187497921659568058_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
        },
        "8873580944738058236_B3/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-266336239404011620_i",
                "Q": "-266336239404011620_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
        },
        "-5867388394385087965": {
            "length": 60,
            "waveforms": {
                "single": "-5867388394385087965",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-899358143601977096_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-899358143601977096_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "5211710689442696482_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "5211710689442696482_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "2833019928693392154": {
            "sample": -0.2388,
            "type": "constant",
        },
        "5000477159223041459_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5000477159223041459_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2740853735462715916_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "2740853735462715916_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "6809367421762151503": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-5985338580302693505": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "4267554387595132513": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
        },
        "4489048446793847761": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "2164490364707011308": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "2288450751812646496": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "1667124983925952952": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-6526726121885772646": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-962435088252343482": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "-4328966433882605783": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-4107472374683890535": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "-300300468441266884": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "1125737442342873811": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-356000812658553850": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "3323497130346040674": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "971131461583746454": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4648859916266969676": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-6973417998353806129": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-8896821289919005180": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1356071677978820838": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8623595025812392911": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-4430203864046288830": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7625389359893991842": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3153999657294009405": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "9008535242207467295": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-3873917797868655157": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-7240449143498917458": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7018955084300202210": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8166776901477070983": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
        },
        "909379801510787355": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8176903149344359428": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "412014420729728999": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "633508479928444247": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-514313337248424526": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "8561843365739433812": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5362582937880114488": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8064477984958375456": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
        },
        "5712112316196081236": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5434917912780079022": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2232437143741471347": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2289880626348531969": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
        },
        "6097052532591155620": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "4487640314351698832": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-961005213716458009": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2884408505281657060": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-8504399883132373190": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5043926380529332505": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6306640195129206327": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2499468288886582676": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
        },
        "2120383153296500700": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-5129028361064879110": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5650360656123122137": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1228036358861569338": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-8895391415383119707": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-9172585818799121921": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6921792586148135475": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5143919853357783022": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
        },
        "-621602083267779706": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1242927851154473250": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4093981982531484932": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3872487923332769684": {
            "samples": [0.12562814070351758] * 59 + [0.0],
            "type": "arbitrary",
        },
        "-5657030128259699195_i": {
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "type": "arbitrary",
        },
        "-5657030128259699195_q": {
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "type": "arbitrary",
        },
        "-5063599797661085433_i": {
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "type": "arbitrary",
        },
        "-5063599797661085433_q": {
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "type": "arbitrary",
        },
        "-1551283749241561855": {
            "sample": 0.21734999999999974,
            "type": "constant",
        },
        "-3187497921659568058_i": {
            "sample": 0.0031,
            "type": "constant",
        },
        "-3187497921659568058_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-266336239404011620_i": {
            "sample": 0.0017,
            "type": "constant",
        },
        "-266336239404011620_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-5867388394385087965": {
            "sample": -0.28768,
            "type": "constant",
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
            "operations": {
                "-5867388394385087965": "-5867388394385087965",
                "6809367421762151503": "6809367421762151503",
                "-5985338580302693505": "-5985338580302693505",
                "4267554387595132513": "4267554387595132513",
                "4489048446793847761": "4489048446793847761",
                "2164490364707011308": "2164490364707011308",
                "2288450751812646496": "2288450751812646496",
                "1667124983925952952": "1667124983925952952",
                "-6526726121885772646": "-6526726121885772646",
                "-962435088252343482": "-962435088252343482",
                "-4328966433882605783": "-4328966433882605783",
                "-4107472374683890535": "-4107472374683890535",
                "-300300468441266884": "-300300468441266884",
                "1125737442342873811": "1125737442342873811",
                "-356000812658553850": "-356000812658553850",
                "3323497130346040674": "3323497130346040674",
                "971131461583746454": "971131461583746454",
                "-4648859916266969676": "-4648859916266969676",
                "-6973417998353806129": "-6973417998353806129",
                "-8896821289919005180": "-8896821289919005180",
                "1356071677978820838": "1356071677978820838",
                "8623595025812392911": "8623595025812392911",
                "-4430203864046288830": "-4430203864046288830",
                "-7625389359893991842": "-7625389359893991842",
                "3153999657294009405": "3153999657294009405",
                "9008535242207467295": "9008535242207467295",
                "-3873917797868655157": "-3873917797868655157",
                "-7240449143498917458": "-7240449143498917458",
                "-7018955084300202210": "-7018955084300202210",
                "-8166776901477070983": "-8166776901477070983",
                "909379801510787355": "909379801510787355",
                "8176903149344359428": "8176903149344359428",
                "412014420729728999": "412014420729728999",
                "633508479928444247": "633508479928444247",
                "-514313337248424526": "-514313337248424526",
                "8561843365739433812": "8561843365739433812",
                "-5362582937880114488": "-5362582937880114488",
                "8064477984958375456": "8064477984958375456",
                "5712112316196081236": "5712112316196081236",
                "5434917912780079022": "5434917912780079022",
                "-2232437143741471347": "-2232437143741471347",
                "2289880626348531969": "2289880626348531969",
                "6097052532591155620": "6097052532591155620",
                "4487640314351698832": "4487640314351698832",
                "-961005213716458009": "-961005213716458009",
                "-2884408505281657060": "-2884408505281657060",
                "-8504399883132373190": "-8504399883132373190",
                "5043926380529332505": "5043926380529332505",
                "-6306640195129206327": "-6306640195129206327",
                "-2499468288886582676": "-2499468288886582676",
                "2120383153296500700": "2120383153296500700",
                "-5129028361064879110": "-5129028361064879110",
                "5650360656123122137": "5650360656123122137",
                "-1228036358861569338": "-1228036358861569338",
                "-8895391415383119707": "-8895391415383119707",
                "-9172585818799121921": "-9172585818799121921",
                "6921792586148135475": "6921792586148135475",
                "-5143919853357783022": "-5143919853357783022",
                "-621602083267779706": "-621602083267779706",
                "-1242927851154473250": "-1242927851154473250",
                "-4093981982531484932": "-4093981982531484932",
                "-3872487923332769684": "-3872487923332769684",
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
                "5741643966098266678": "5741643966098266678_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_92b",
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
                "-193334924239390645": "-193334924239390645_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_17e",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "-899358143601977096": "-899358143601977096",
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
                "mixer": "B2/drive_mixer_f0e",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "5211710689442696482": "5211710689442696482",
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
                "mixer": "B4/drive_mixer_d10",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "8873580944738058236": "8873580944738058236_B3/acquisition",
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
                "mixer": "B3/acquisition_mixer_2ac",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 110622376.0,
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
                "-5657030128259699195": "-5657030128259699195",
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
                "mixer": "B1/drive_mixer_95e",
                "lo_frequency": 4900000000.0,
            },
            "intermediate_frequency": 100388701.0,
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
                "-5063599797661085433": "-5063599797661085433",
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
                "mixer": "B3/drive_mixer_08d",
                "lo_frequency": 5800000000.0,
            },
            "intermediate_frequency": -115376210.0,
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
                "-5755598658197327036": "-5755598658197327036_B1/acquisition",
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
                "mixer": "B1/acquisition_mixer_820",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": -237451236.0,
        },
    },
    "pulses": {
        "-899358143601977096": {
            "length": 40,
            "waveforms": {
                "I": "-899358143601977096_i",
                "Q": "-899358143601977096_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5211710689442696482": {
            "length": 40,
            "waveforms": {
                "I": "5211710689442696482_i",
                "Q": "5211710689442696482_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2833019928693392154": {
            "length": 60,
            "waveforms": {
                "single": "2833019928693392154",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5741643966098266678_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5000477159223041459_i",
                "Q": "5000477159223041459_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-193334924239390645_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "2740853735462715916_i",
                "Q": "2740853735462715916_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "6809367421762151503": {
            "length": 60,
            "waveforms": {
                "single": "6809367421762151503",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5985338580302693505": {
            "length": 16,
            "waveforms": {
                "single": "-5985338580302693505",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4267554387595132513": {
            "length": 16,
            "waveforms": {
                "single": "4267554387595132513",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4489048446793847761": {
            "length": 16,
            "waveforms": {
                "single": "4489048446793847761",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2164490364707011308": {
            "length": 16,
            "waveforms": {
                "single": "2164490364707011308",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2288450751812646496": {
            "length": 16,
            "waveforms": {
                "single": "2288450751812646496",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1667124983925952952": {
            "length": 16,
            "waveforms": {
                "single": "1667124983925952952",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6526726121885772646": {
            "length": 16,
            "waveforms": {
                "single": "-6526726121885772646",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-962435088252343482": {
            "length": 16,
            "waveforms": {
                "single": "-962435088252343482",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4328966433882605783": {
            "length": 16,
            "waveforms": {
                "single": "-4328966433882605783",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4107472374683890535": {
            "length": 16,
            "waveforms": {
                "single": "-4107472374683890535",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-300300468441266884": {
            "length": 16,
            "waveforms": {
                "single": "-300300468441266884",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1125737442342873811": {
            "length": 16,
            "waveforms": {
                "single": "1125737442342873811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-356000812658553850": {
            "length": 16,
            "waveforms": {
                "single": "-356000812658553850",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3323497130346040674": {
            "length": 16,
            "waveforms": {
                "single": "3323497130346040674",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "971131461583746454": {
            "length": 16,
            "waveforms": {
                "single": "971131461583746454",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4648859916266969676": {
            "length": 16,
            "waveforms": {
                "single": "-4648859916266969676",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6973417998353806129": {
            "length": 16,
            "waveforms": {
                "single": "-6973417998353806129",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8896821289919005180": {
            "length": 20,
            "waveforms": {
                "single": "-8896821289919005180",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1356071677978820838": {
            "length": 20,
            "waveforms": {
                "single": "1356071677978820838",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8623595025812392911": {
            "length": 20,
            "waveforms": {
                "single": "8623595025812392911",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4430203864046288830": {
            "length": 20,
            "waveforms": {
                "single": "-4430203864046288830",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7625389359893991842": {
            "length": 24,
            "waveforms": {
                "single": "-7625389359893991842",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3153999657294009405": {
            "length": 24,
            "waveforms": {
                "single": "3153999657294009405",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9008535242207467295": {
            "length": 24,
            "waveforms": {
                "single": "9008535242207467295",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3873917797868655157": {
            "length": 24,
            "waveforms": {
                "single": "-3873917797868655157",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7240449143498917458": {
            "length": 28,
            "waveforms": {
                "single": "-7240449143498917458",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7018955084300202210": {
            "length": 28,
            "waveforms": {
                "single": "-7018955084300202210",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8166776901477070983": {
            "length": 28,
            "waveforms": {
                "single": "-8166776901477070983",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "909379801510787355": {
            "length": 28,
            "waveforms": {
                "single": "909379801510787355",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8176903149344359428": {
            "length": 32,
            "waveforms": {
                "single": "8176903149344359428",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "412014420729728999": {
            "length": 32,
            "waveforms": {
                "single": "412014420729728999",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "633508479928444247": {
            "length": 32,
            "waveforms": {
                "single": "633508479928444247",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-514313337248424526": {
            "length": 32,
            "waveforms": {
                "single": "-514313337248424526",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8561843365739433812": {
            "length": 36,
            "waveforms": {
                "single": "8561843365739433812",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5362582937880114488": {
            "length": 36,
            "waveforms": {
                "single": "-5362582937880114488",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8064477984958375456": {
            "length": 36,
            "waveforms": {
                "single": "8064477984958375456",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5712112316196081236": {
            "length": 36,
            "waveforms": {
                "single": "5712112316196081236",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5434917912780079022": {
            "length": 40,
            "waveforms": {
                "single": "5434917912780079022",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2232437143741471347": {
            "length": 40,
            "waveforms": {
                "single": "-2232437143741471347",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2289880626348531969": {
            "length": 40,
            "waveforms": {
                "single": "2289880626348531969",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6097052532591155620": {
            "length": 40,
            "waveforms": {
                "single": "6097052532591155620",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4487640314351698832": {
            "length": 44,
            "waveforms": {
                "single": "4487640314351698832",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-961005213716458009": {
            "length": 44,
            "waveforms": {
                "single": "-961005213716458009",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2884408505281657060": {
            "length": 44,
            "waveforms": {
                "single": "-2884408505281657060",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8504399883132373190": {
            "length": 44,
            "waveforms": {
                "single": "-8504399883132373190",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5043926380529332505": {
            "length": 48,
            "waveforms": {
                "single": "5043926380529332505",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6306640195129206327": {
            "length": 48,
            "waveforms": {
                "single": "-6306640195129206327",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2499468288886582676": {
            "length": 48,
            "waveforms": {
                "single": "-2499468288886582676",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2120383153296500700": {
            "length": 48,
            "waveforms": {
                "single": "2120383153296500700",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5129028361064879110": {
            "length": 52,
            "waveforms": {
                "single": "-5129028361064879110",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5650360656123122137": {
            "length": 52,
            "waveforms": {
                "single": "5650360656123122137",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1228036358861569338": {
            "length": 52,
            "waveforms": {
                "single": "-1228036358861569338",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8895391415383119707": {
            "length": 52,
            "waveforms": {
                "single": "-8895391415383119707",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9172585818799121921": {
            "length": 56,
            "waveforms": {
                "single": "-9172585818799121921",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6921792586148135475": {
            "length": 56,
            "waveforms": {
                "single": "6921792586148135475",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5143919853357783022": {
            "length": 56,
            "waveforms": {
                "single": "-5143919853357783022",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-621602083267779706": {
            "length": 56,
            "waveforms": {
                "single": "-621602083267779706",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1242927851154473250": {
            "length": 60,
            "waveforms": {
                "single": "-1242927851154473250",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4093981982531484932": {
            "length": 60,
            "waveforms": {
                "single": "-4093981982531484932",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3872487923332769684": {
            "length": 60,
            "waveforms": {
                "single": "-3872487923332769684",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5657030128259699195": {
            "length": 40,
            "waveforms": {
                "I": "-5657030128259699195_i",
                "Q": "-5657030128259699195_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5063599797661085433": {
            "length": 40,
            "waveforms": {
                "I": "-5063599797661085433_i",
                "Q": "-5063599797661085433_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1551283749241561855": {
            "length": 60,
            "waveforms": {
                "single": "-1551283749241561855",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5755598658197327036_B1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-3187497921659568058_i",
                "Q": "-3187497921659568058_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B1/acquisition",
                "sin": "sine_weights_B1/acquisition",
                "minus_sin": "minus_sine_weights_B1/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8873580944738058236_B3/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-266336239404011620_i",
                "Q": "-266336239404011620_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B3/acquisition",
                "sin": "sine_weights_B3/acquisition",
                "minus_sin": "minus_sine_weights_B3/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-5867388394385087965": {
            "length": 60,
            "waveforms": {
                "single": "-5867388394385087965",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-899358143601977096_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-899358143601977096_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5211710689442696482_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5211710689442696482_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2833019928693392154": {
            "type": "constant",
            "sample": -0.2388,
        },
        "5000477159223041459_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "5000477159223041459_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2740853735462715916_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "2740853735462715916_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "6809367421762151503": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-5985338580302693505": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4267554387595132513": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4489048446793847761": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2164490364707011308": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2288450751812646496": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1667124983925952952": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6526726121885772646": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-962435088252343482": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4328966433882605783": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4107472374683890535": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-300300468441266884": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1125737442342873811": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-356000812658553850": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3323497130346040674": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "971131461583746454": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4648859916266969676": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6973417998353806129": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-8896821289919005180": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1356071677978820838": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8623595025812392911": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4430203864046288830": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-7625389359893991842": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3153999657294009405": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9008535242207467295": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3873917797868655157": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-7240449143498917458": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7018955084300202210": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8166776901477070983": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "909379801510787355": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "8176903149344359428": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "412014420729728999": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "633508479928444247": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-514313337248424526": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "8561843365739433812": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5362582937880114488": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8064477984958375456": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5712112316196081236": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5434917912780079022": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2232437143741471347": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2289880626348531969": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6097052532591155620": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "4487640314351698832": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-961005213716458009": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2884408505281657060": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8504399883132373190": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5043926380529332505": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6306640195129206327": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2499468288886582676": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2120383153296500700": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-5129028361064879110": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5650360656123122137": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1228036358861569338": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8895391415383119707": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-9172585818799121921": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6921792586148135475": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5143919853357783022": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-621602083267779706": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-1242927851154473250": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4093981982531484932": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3872487923332769684": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5657030128259699195_i": {
            "type": "arbitrary",
            "samples": [0.0022361110375831357, 0.003009016295098337, 0.0039862989265130756, 0.005199113930495341, 0.006675794431011323, 0.008438994893651268, 0.010502498834484402, 0.012867930560721863, 0.015521687089791392, 0.018432459489181957, 0.02154972839707475, 0.024803585345044128, 0.02810614436424776, 0.03135466980509781, 0.0344363679261974, 0.03723459168038863, 0.03963601652384273, 0.04153818867276975, 0.042856752322584096] + [0.04353164796913192] * 2 + [0.042856752322584096, 0.04153818867276975, 0.03963601652384273, 0.03723459168038863, 0.0344363679261974, 0.03135466980509781, 0.02810614436424776, 0.024803585345044128, 0.02154972839707475, 0.018432459489181957, 0.015521687089791392, 0.012867930560721863, 0.010502498834484402, 0.008438994893651268, 0.006675794431011323, 0.005199113930495341, 0.0039862989265130756, 0.003009016295098337, 0.0022361110375831357],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5657030128259699195_q": {
            "type": "arbitrary",
            "samples": [0.0004428548031463476, 0.000565365952321211, 0.0007085023482669725, 0.0008712577641337897, 0.0010509160764443607, 0.0012427738573853625, 0.0014399910511343848, 0.0016336239969666426, 0.0018128845468154792, 0.0019656490002135448, 0.002079212075811509, 0.002141247016115138, 0.0021408977152454346, 0.0020698981238521604, 0.0019235939896274329, 0.001701737197892762, 0.001408936524870972, 0.0010546805717695444, 0.0006528958361643671, 0.00022105914984324804, -0.00022105914984324804, -0.0006528958361643671, -0.0010546805717695444, -0.001408936524870972, -0.001701737197892762, -0.0019235939896274329, -0.0020698981238521604, -0.0021408977152454346, -0.002141247016115138, -0.002079212075811509, -0.0019656490002135448, -0.0018128845468154792, -0.0016336239969666426, -0.0014399910511343848, -0.0012427738573853625, -0.0010509160764443607, -0.0008712577641337897, -0.0007085023482669725, -0.000565365952321211, -0.0004428548031463476],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5063599797661085433_i": {
            "type": "arbitrary",
            "samples": [0.003281902155839329, 0.004416282062858765, 0.005850623167122966, 0.0076306511305401, 0.009797949997490538, 0.012385769341993818, 0.015414338996264144, 0.018886042928381978, 0.022780916272077543, 0.02705300743935812, 0.031628170021714405, 0.036403800548486256, 0.04125091027727048, 0.046018715841679235, 0.050541671784964645, 0.05464857721901986, 0.05817310763739141, 0.060964893363331246, 0.06290012681650281] + [0.06389065968367467] * 2 + [0.06290012681650281, 0.060964893363331246, 0.05817310763739141, 0.05464857721901986, 0.050541671784964645, 0.046018715841679235, 0.04125091027727048, 0.036403800548486256, 0.031628170021714405, 0.02705300743935812, 0.022780916272077543, 0.018886042928381978, 0.015414338996264144, 0.012385769341993818, 0.009797949997490538, 0.0076306511305401, 0.005850623167122966, 0.004416282062858765, 0.003281902155839329],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5063599797661085433_q": {
            "type": "arbitrary",
            "samples": [-0.0006034345805618549, -0.0007703684455470659, -0.0009654063009276765, -0.0011871770605762007, -0.0014319797308043336, -0.0016934054142272652, -0.001962133841115749, -0.002225978366727978, -0.0024702390452636764, -0.0026783961053341294, -0.002833137312619005, -0.002917666209937816, -0.0029171902520791645, -0.002820446108517724, -0.002621091888481888, -0.0023187895105601366, -0.001919818899746316, -0.001437109237454008, -0.0008896367889595412, -0.000301215509953357, 0.000301215509953357, 0.0008896367889595412, 0.001437109237454008, 0.001919818899746316, 0.0023187895105601366, 0.002621091888481888, 0.002820446108517724, 0.0029171902520791645, 0.002917666209937816, 0.002833137312619005, 0.0026783961053341294, 0.0024702390452636764, 0.002225978366727978, 0.001962133841115749, 0.0016934054142272652, 0.0014319797308043336, 0.0011871770605762007, 0.0009654063009276765, 0.0007703684455470659, 0.0006034345805618549],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1551283749241561855": {
            "type": "constant",
            "sample": 0.21734999999999974,
        },
        "-3187497921659568058_i": {
            "type": "constant",
            "sample": 0.0031,
        },
        "-3187497921659568058_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-266336239404011620_i": {
            "type": "constant",
            "sample": 0.0017,
        },
        "-266336239404011620_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-5867388394385087965": {
            "type": "constant",
            "sample": -0.28768,
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
        "B2/acquisition_mixer_92b": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_17e": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/drive_mixer_f0e": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_d10": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/acquisition_mixer_2ac": [{'intermediate_frequency': 110622376.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/drive_mixer_95e": [{'intermediate_frequency': 100388701.0, 'lo_frequency': 4900000000.0, 'correction': (1, 0, 0, 1)}],
        "B3/drive_mixer_08d": [{'intermediate_frequency': -115376210.0, 'lo_frequency': 5800000000.0, 'correction': (1, 0, 0, 1)}],
        "B1/acquisition_mixer_820": [{'intermediate_frequency': -237451236.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

