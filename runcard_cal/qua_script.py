
# Single QUA script generated at 2025-02-17 11:04:50.493434
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
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B2/acquisition")
    wait((4+(0*((Cast.to_int(v5)+Cast.to_int(v6))+Cast.to_int(v7)))), "B4/acquisition")
    with for_(v1,0,(v1<256),(v1+1)):
        with for_(v8,0,(v8<=59),(v8+1)):
            with for_(v9,-1.9900000000000002,(v9<-1.3890199999999995),(v9+0.007959999999999967)):
                align()
                play("4602749578813007475", "B2/drive")
                play("-5588028311087956264", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("-3771244817455671925"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("8462667552616981714"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("5860322382555460549"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-890400669191201799"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("8900901897644036204"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("1307359018811965064"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-4312632359038751066"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("3892896930188240713"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("5107323941209020338"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-1893378611836868955"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("1913793294405754696"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("-4964603720578936779"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("-5908450627470600069"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("5537590893193062254"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("-4703623891289497583"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-4482129832090782335"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("40187937999220981"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("1744012936758046388"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("-7830549344248852373"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("2948839672939148874"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("7471157443029152190"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("2128953153153120772"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("2350447212351836020"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-7224115068655062741"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-7845440836541756285"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-5026355380651895878"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-8665327356327784387"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("7429051048619473009"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("4826705878557951844"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-6246073609125902276"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("7024465566561118707"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-3586723520060147398"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-6189068690121668563"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("6426073105973805853"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-1167469772858265287"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-3769814942919786452"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("1418068138518010362"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-4589701462705814554"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-782529556463190903"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("4503974389195553549"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("1308788893347850537"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("9070531702746656819"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("488902373561822435"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-7178452682959727934"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("1693729109742924921"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("1915223168941640169"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-4759198935757845823"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("8141365937790468892"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("474010881268918523"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("-9100551399737980238"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-7886124388717200613"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("8526306154185543276"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("8747800213384258524"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("5552614717536555512"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("-7501184172322126229"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("-7279690113123410981"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("2130383027689006245"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("2351877086887721493"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-6229752242297112891"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("4549636774890888356"*amp(v9), "B4/flux")
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
                play("-5588028311087956264", "B4/drive")
                measure("521970795558401185", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7633206605922164)-(v3*0.6460197900320566))>0.002433478909969987)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-6731957312620768847", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.5216599067641747)-(v6*0.8531535276108237))>-0.0004544464624298409)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(76).buffer(60).average().save("521970795558401185_B2|acquisition_shots")
        r2.buffer(76).buffer(60).average().save("-6731957312620768847_B4|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.25498290735703955,
                    "filter": {
                        "feedforward": [1.0733850337443736, -0.9864790585777543, -0.0005323888104498682, -0.0005259475398959013, 7.973032256636107e-05, -0.0016725113040139137, -0.0023176583016525022, 0.002973296582730941, -0.002852689981364934, -0.001539139450176758, 0.008399921852580278, 0.0057738695432430695, 0.0023171132353592347, -0.006922530514412358, 0.004616481924541356, -0.006183881461044106, -0.0004794180166864429, -0.004282945141175208, 0.005029153559383712, -0.00652156307616806, 0.005364980982312166],
                        "feedback": [0.9999990463256836, 0.9123677263043898],
                    },
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "filter": {
                        "feedforward": [1.0901051230297683, -1.0232644441550267, -0.0006252532895003595, -0.0006141100300566752, 0.008121708556303465, 0.0024752404210370074, -0.0004725999126392608, 0.003195999511191553, -0.009401662750096436, -0.009162109298267173, 0.007799464631907388, 0.006536301297249568, 0.0028538002595834664, -0.0019338464694733577, 0.00155684655210413, -0.0018616458394758225, -0.006539808707311681, 0.005615235090478333, -0.0013900128312052053, -0.0010374461453545932, 0.0008943957345949297],
                        "feedback": [0.9999990463256836, 0.9272227783745652],
                    },
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "filter": {
                        "feedforward": [1.088889257410577, -1.0126234439208628, -0.00022827806040770938, -0.00022691874558202754, 0.001839809971154677, -0.0054450654189005555, -0.0018179082654598761, 0.0005272402543389071, -0.005065664211626804, 0.0009512460413182737, 0.0069285887522925966, 0.008809118665910963, -0.0037407896697840715, -0.001441290690449959, -0.0015081864432025397, -0.003929777987759672, 0.0005129705526087183, -0.003664656487684447, 0.003588144419968449, -0.00027317439831977836, 0.0010998018643718927],
                        "feedback": [0.9999990463256836, 0.9268269104388525],
                    },
                },
                "4": {
                    "offset": 0.114743772754262,
                    "filter": {
                        "feedforward": [1.1007733004513929, -1.0338373310676314, -0.0004112070306083244, -0.00040624034702793307, 0.004792742757189549, -0.0029362732950892344, 0.0008924841656747927, -0.0019277499637905277, 0.00012369876998848703, -0.0038014391983210876, 0.006091493257461685, 0.006320856433508812, -0.004317289784430141, 0.0012374947962223264, -0.003230085628748808, -0.002550100709383478, -0.0011941277864627056, -0.0020443256802386545, -0.0004156642549092808, 0.004467419295992805, 6.059493035474965e-05],
                        "feedback": [0.9999990463256836, 0.932265844844647],
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
                "4": {
                    "LO_frequency": 5900000000.0,
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
                "-7020253597009942133": "-7020253597009942133",
                "8356808681133512007": "8356808681133512007",
                "-3771244817455671925": "-3771244817455671925",
                "8462667552616981714": "8462667552616981714",
                "5860322382555460549": "5860322382555460549",
                "-890400669191201799": "-890400669191201799",
                "8900901897644036204": "8900901897644036204",
                "1307359018811965064": "1307359018811965064",
                "-4312632359038751066": "-4312632359038751066",
                "3892896930188240713": "3892896930188240713",
                "5107323941209020338": "5107323941209020338",
                "-1893378611836868955": "-1893378611836868955",
                "1913793294405754696": "1913793294405754696",
                "-4964603720578936779": "-4964603720578936779",
                "-5908450627470600069": "-5908450627470600069",
                "5537590893193062254": "5537590893193062254",
                "-4703623891289497583": "-4703623891289497583",
                "-4482129832090782335": "-4482129832090782335",
                "40187937999220981": "40187937999220981",
                "1744012936758046388": "1744012936758046388",
                "-7830549344248852373": "-7830549344248852373",
                "2948839672939148874": "2948839672939148874",
                "7471157443029152190": "7471157443029152190",
                "2128953153153120772": "2128953153153120772",
                "2350447212351836020": "2350447212351836020",
                "-7224115068655062741": "-7224115068655062741",
                "-7845440836541756285": "-7845440836541756285",
                "-5026355380651895878": "-5026355380651895878",
                "-8665327356327784387": "-8665327356327784387",
                "7429051048619473009": "7429051048619473009",
                "4826705878557951844": "4826705878557951844",
                "-6246073609125902276": "-6246073609125902276",
                "7024465566561118707": "7024465566561118707",
                "-3586723520060147398": "-3586723520060147398",
                "-6189068690121668563": "-6189068690121668563",
                "6426073105973805853": "6426073105973805853",
                "-1167469772858265287": "-1167469772858265287",
                "-3769814942919786452": "-3769814942919786452",
                "1418068138518010362": "1418068138518010362",
                "-4589701462705814554": "-4589701462705814554",
                "-782529556463190903": "-782529556463190903",
                "4503974389195553549": "4503974389195553549",
                "1308788893347850537": "1308788893347850537",
                "9070531702746656819": "9070531702746656819",
                "488902373561822435": "488902373561822435",
                "-7178452682959727934": "-7178452682959727934",
                "1693729109742924921": "1693729109742924921",
                "1915223168941640169": "1915223168941640169",
                "-4759198935757845823": "-4759198935757845823",
                "8141365937790468892": "8141365937790468892",
                "474010881268918523": "474010881268918523",
                "-9100551399737980238": "-9100551399737980238",
                "-7886124388717200613": "-7886124388717200613",
                "8526306154185543276": "8526306154185543276",
                "8747800213384258524": "8747800213384258524",
                "5552614717536555512": "5552614717536555512",
                "-7501184172322126229": "-7501184172322126229",
                "-7279690113123410981": "-7279690113123410981",
                "2130383027689006245": "2130383027689006245",
                "2351877086887721493": "2351877086887721493",
                "-6229752242297112891": "-6229752242297112891",
                "4549636774890888356": "4549636774890888356",
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
                "4602749578813007475": "4602749578813007475",
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
                "521970795558401185": "521970795558401185_B2/acquisition",
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
                "-5588028311087956264": "-5588028311087956264",
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
                "-6731957312620768847": "-6731957312620768847_B4/acquisition",
            },
        },
    },
    "pulses": {
        "4602749578813007475": {
            "length": 40,
            "waveforms": {
                "I": "4602749578813007475_i",
                "Q": "4602749578813007475_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5588028311087956264": {
            "length": 40,
            "waveforms": {
                "I": "-5588028311087956264_i",
                "Q": "-5588028311087956264_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7020253597009942133": {
            "length": 60,
            "waveforms": {
                "single": "-7020253597009942133",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "521970795558401185_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5167207243399228800_i",
                "Q": "5167207243399228800_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-6731957312620768847_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "8148761029708680177_i",
                "Q": "8148761029708680177_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "8356808681133512007": {
            "length": 60,
            "waveforms": {
                "single": "8356808681133512007",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3771244817455671925": {
            "length": 16,
            "waveforms": {
                "single": "-3771244817455671925",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8462667552616981714": {
            "length": 16,
            "waveforms": {
                "single": "8462667552616981714",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5860322382555460549": {
            "length": 16,
            "waveforms": {
                "single": "5860322382555460549",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-890400669191201799": {
            "length": 16,
            "waveforms": {
                "single": "-890400669191201799",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8900901897644036204": {
            "length": 16,
            "waveforms": {
                "single": "8900901897644036204",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1307359018811965064": {
            "length": 16,
            "waveforms": {
                "single": "1307359018811965064",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4312632359038751066": {
            "length": 16,
            "waveforms": {
                "single": "-4312632359038751066",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3892896930188240713": {
            "length": 16,
            "waveforms": {
                "single": "3892896930188240713",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5107323941209020338": {
            "length": 16,
            "waveforms": {
                "single": "5107323941209020338",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1893378611836868955": {
            "length": 16,
            "waveforms": {
                "single": "-1893378611836868955",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1913793294405754696": {
            "length": 16,
            "waveforms": {
                "single": "1913793294405754696",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4964603720578936779": {
            "length": 16,
            "waveforms": {
                "single": "-4964603720578936779",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5908450627470600069": {
            "length": 16,
            "waveforms": {
                "single": "-5908450627470600069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5537590893193062254": {
            "length": 16,
            "waveforms": {
                "single": "5537590893193062254",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4703623891289497583": {
            "length": 16,
            "waveforms": {
                "single": "-4703623891289497583",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4482129832090782335": {
            "length": 16,
            "waveforms": {
                "single": "-4482129832090782335",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "40187937999220981": {
            "length": 16,
            "waveforms": {
                "single": "40187937999220981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1744012936758046388": {
            "length": 20,
            "waveforms": {
                "single": "1744012936758046388",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7830549344248852373": {
            "length": 20,
            "waveforms": {
                "single": "-7830549344248852373",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2948839672939148874": {
            "length": 20,
            "waveforms": {
                "single": "2948839672939148874",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7471157443029152190": {
            "length": 20,
            "waveforms": {
                "single": "7471157443029152190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2128953153153120772": {
            "length": 24,
            "waveforms": {
                "single": "2128953153153120772",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2350447212351836020": {
            "length": 24,
            "waveforms": {
                "single": "2350447212351836020",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7224115068655062741": {
            "length": 24,
            "waveforms": {
                "single": "-7224115068655062741",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7845440836541756285": {
            "length": 24,
            "waveforms": {
                "single": "-7845440836541756285",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5026355380651895878": {
            "length": 28,
            "waveforms": {
                "single": "-5026355380651895878",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8665327356327784387": {
            "length": 28,
            "waveforms": {
                "single": "-8665327356327784387",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7429051048619473009": {
            "length": 28,
            "waveforms": {
                "single": "7429051048619473009",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4826705878557951844": {
            "length": 28,
            "waveforms": {
                "single": "4826705878557951844",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6246073609125902276": {
            "length": 32,
            "waveforms": {
                "single": "-6246073609125902276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7024465566561118707": {
            "length": 32,
            "waveforms": {
                "single": "7024465566561118707",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3586723520060147398": {
            "length": 32,
            "waveforms": {
                "single": "-3586723520060147398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6189068690121668563": {
            "length": 32,
            "waveforms": {
                "single": "-6189068690121668563",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6426073105973805853": {
            "length": 36,
            "waveforms": {
                "single": "6426073105973805853",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1167469772858265287": {
            "length": 36,
            "waveforms": {
                "single": "-1167469772858265287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3769814942919786452": {
            "length": 36,
            "waveforms": {
                "single": "-3769814942919786452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1418068138518010362": {
            "length": 36,
            "waveforms": {
                "single": "1418068138518010362",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4589701462705814554": {
            "length": 40,
            "waveforms": {
                "single": "-4589701462705814554",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-782529556463190903": {
            "length": 40,
            "waveforms": {
                "single": "-782529556463190903",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4503974389195553549": {
            "length": 40,
            "waveforms": {
                "single": "4503974389195553549",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1308788893347850537": {
            "length": 40,
            "waveforms": {
                "single": "1308788893347850537",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9070531702746656819": {
            "length": 44,
            "waveforms": {
                "single": "9070531702746656819",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "488902373561822435": {
            "length": 44,
            "waveforms": {
                "single": "488902373561822435",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7178452682959727934": {
            "length": 44,
            "waveforms": {
                "single": "-7178452682959727934",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1693729109742924921": {
            "length": 44,
            "waveforms": {
                "single": "1693729109742924921",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1915223168941640169": {
            "length": 48,
            "waveforms": {
                "single": "1915223168941640169",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4759198935757845823": {
            "length": 48,
            "waveforms": {
                "single": "-4759198935757845823",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8141365937790468892": {
            "length": 48,
            "waveforms": {
                "single": "8141365937790468892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "474010881268918523": {
            "length": 48,
            "waveforms": {
                "single": "474010881268918523",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9100551399737980238": {
            "length": 52,
            "waveforms": {
                "single": "-9100551399737980238",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7886124388717200613": {
            "length": 52,
            "waveforms": {
                "single": "-7886124388717200613",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8526306154185543276": {
            "length": 52,
            "waveforms": {
                "single": "8526306154185543276",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8747800213384258524": {
            "length": 52,
            "waveforms": {
                "single": "8747800213384258524",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5552614717536555512": {
            "length": 56,
            "waveforms": {
                "single": "5552614717536555512",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7501184172322126229": {
            "length": 56,
            "waveforms": {
                "single": "-7501184172322126229",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7279690113123410981": {
            "length": 56,
            "waveforms": {
                "single": "-7279690113123410981",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2130383027689006245": {
            "length": 56,
            "waveforms": {
                "single": "2130383027689006245",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2351877086887721493": {
            "length": 60,
            "waveforms": {
                "single": "2351877086887721493",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6229752242297112891": {
            "length": 60,
            "waveforms": {
                "single": "-6229752242297112891",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4549636774890888356": {
            "length": 60,
            "waveforms": {
                "single": "4549636774890888356",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "4602749578813007475_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "4602749578813007475_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-5588028311087956264_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-5588028311087956264_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "-7020253597009942133": {
            "sample": -0.2388,
            "type": "constant",
        },
        "5167207243399228800_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5167207243399228800_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8148761029708680177_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "8148761029708680177_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "8356808681133512007": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-3771244817455671925": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8462667552616981714": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
        },
        "5860322382555460549": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-890400669191201799": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "8900901897644036204": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "1307359018811965064": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-4312632359038751066": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "3892896930188240713": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "5107323941209020338": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-1893378611836868955": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "1913793294405754696": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "-4964603720578936779": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "-5908450627470600069": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "5537590893193062254": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4703623891289497583": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4482129832090782335": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
        },
        "40187937999220981": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "1744012936758046388": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7830549344248852373": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2948839672939148874": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
        },
        "7471157443029152190": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2128953153153120772": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2350447212351836020": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7224115068655062741": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-7845440836541756285": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-5026355380651895878": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-8665327356327784387": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7429051048619473009": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
        },
        "4826705878557951844": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-6246073609125902276": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7024465566561118707": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3586723520060147398": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-6189068690121668563": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "6426073105973805853": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1167469772858265287": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3769814942919786452": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
        },
        "1418068138518010362": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-4589701462705814554": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-782529556463190903": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4503974389195553549": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
        },
        "1308788893347850537": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "9070531702746656819": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "488902373561822435": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7178452682959727934": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
        },
        "1693729109742924921": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "1915223168941640169": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4759198935757845823": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8141365937790468892": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
        },
        "474010881268918523": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-9100551399737980238": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7886124388717200613": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8526306154185543276": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
        },
        "8747800213384258524": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5552614717536555512": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7501184172322126229": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7279690113123410981": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
        },
        "2130383027689006245": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "2351877086887721493": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6229752242297112891": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4549636774890888356": {
            "samples": [0.12562814070351758] * 59 + [0.0],
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
                        "feedforward": [1.0733850337443736, -0.9864790585777543, -0.0005323888104498682, -0.0005259475398959013, 7.973032256636107e-05, -0.0016725113040139137, -0.0023176583016525022, 0.002973296582730941, -0.002852689981364934, -0.001539139450176758, 0.008399921852580278, 0.0057738695432430695, 0.0023171132353592347, -0.006922530514412358, 0.004616481924541356, -0.006183881461044106, -0.0004794180166864429, -0.004282945141175208, 0.005029153559383712, -0.00652156307616806, 0.005364980982312166],
                        "feedback": [0.9999990463256836, 0.9123677263043898],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.10729465913983083,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0901051230297683, -1.0232644441550267, -0.0006252532895003595, -0.0006141100300566752, 0.008121708556303465, 0.0024752404210370074, -0.0004725999126392608, 0.003195999511191553, -0.009401662750096436, -0.009162109298267173, 0.007799464631907388, 0.006536301297249568, 0.0028538002595834664, -0.0019338464694733577, 0.00155684655210413, -0.0018616458394758225, -0.006539808707311681, 0.005615235090478333, -0.0013900128312052053, -0.0010374461453545932, 0.0008943957345949297],
                        "feedback": [0.9999990463256836, 0.9272227783745652],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.2226188560782865,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.088889257410577, -1.0126234439208628, -0.00022827806040770938, -0.00022691874558202754, 0.001839809971154677, -0.0054450654189005555, -0.0018179082654598761, 0.0005272402543389071, -0.005065664211626804, 0.0009512460413182737, 0.0069285887522925966, 0.008809118665910963, -0.0037407896697840715, -0.001441290690449959, -0.0015081864432025397, -0.003929777987759672, 0.0005129705526087183, -0.003664656487684447, 0.003588144419968449, -0.00027317439831977836, 0.0010998018643718927],
                        "feedback": [0.9999990463256836, 0.9268269104388525],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.114743772754262,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1007733004513929, -1.0338373310676314, -0.0004112070306083244, -0.00040624034702793307, 0.004792742757189549, -0.0029362732950892344, 0.0008924841656747927, -0.0019277499637905277, 0.00012369876998848703, -0.0038014391983210876, 0.006091493257461685, 0.006320856433508812, -0.004317289784430141, 0.0012374947962223264, -0.003230085628748808, -0.002550100709383478, -0.0011941277864627056, -0.0020443256802386545, -0.0004156642549092808, 0.004467419295992805, 6.059493035474965e-05],
                        "feedback": [0.9999990463256836, 0.932265844844647],
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
            "operations": {
                "-7020253597009942133": "-7020253597009942133",
                "8356808681133512007": "8356808681133512007",
                "-3771244817455671925": "-3771244817455671925",
                "8462667552616981714": "8462667552616981714",
                "5860322382555460549": "5860322382555460549",
                "-890400669191201799": "-890400669191201799",
                "8900901897644036204": "8900901897644036204",
                "1307359018811965064": "1307359018811965064",
                "-4312632359038751066": "-4312632359038751066",
                "3892896930188240713": "3892896930188240713",
                "5107323941209020338": "5107323941209020338",
                "-1893378611836868955": "-1893378611836868955",
                "1913793294405754696": "1913793294405754696",
                "-4964603720578936779": "-4964603720578936779",
                "-5908450627470600069": "-5908450627470600069",
                "5537590893193062254": "5537590893193062254",
                "-4703623891289497583": "-4703623891289497583",
                "-4482129832090782335": "-4482129832090782335",
                "40187937999220981": "40187937999220981",
                "1744012936758046388": "1744012936758046388",
                "-7830549344248852373": "-7830549344248852373",
                "2948839672939148874": "2948839672939148874",
                "7471157443029152190": "7471157443029152190",
                "2128953153153120772": "2128953153153120772",
                "2350447212351836020": "2350447212351836020",
                "-7224115068655062741": "-7224115068655062741",
                "-7845440836541756285": "-7845440836541756285",
                "-5026355380651895878": "-5026355380651895878",
                "-8665327356327784387": "-8665327356327784387",
                "7429051048619473009": "7429051048619473009",
                "4826705878557951844": "4826705878557951844",
                "-6246073609125902276": "-6246073609125902276",
                "7024465566561118707": "7024465566561118707",
                "-3586723520060147398": "-3586723520060147398",
                "-6189068690121668563": "-6189068690121668563",
                "6426073105973805853": "6426073105973805853",
                "-1167469772858265287": "-1167469772858265287",
                "-3769814942919786452": "-3769814942919786452",
                "1418068138518010362": "1418068138518010362",
                "-4589701462705814554": "-4589701462705814554",
                "-782529556463190903": "-782529556463190903",
                "4503974389195553549": "4503974389195553549",
                "1308788893347850537": "1308788893347850537",
                "9070531702746656819": "9070531702746656819",
                "488902373561822435": "488902373561822435",
                "-7178452682959727934": "-7178452682959727934",
                "1693729109742924921": "1693729109742924921",
                "1915223168941640169": "1915223168941640169",
                "-4759198935757845823": "-4759198935757845823",
                "8141365937790468892": "8141365937790468892",
                "474010881268918523": "474010881268918523",
                "-9100551399737980238": "-9100551399737980238",
                "-7886124388717200613": "-7886124388717200613",
                "8526306154185543276": "8526306154185543276",
                "8747800213384258524": "8747800213384258524",
                "5552614717536555512": "5552614717536555512",
                "-7501184172322126229": "-7501184172322126229",
                "-7279690113123410981": "-7279690113123410981",
                "2130383027689006245": "2130383027689006245",
                "2351877086887721493": "2351877086887721493",
                "-6229752242297112891": "-6229752242297112891",
                "4549636774890888356": "4549636774890888356",
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
                "4602749578813007475": "4602749578813007475",
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
                "mixer": "B2/drive_mixer_e88",
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
                "521970795558401185": "521970795558401185_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_b25",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
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
                "-5588028311087956264": "-5588028311087956264",
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
                "mixer": "B4/drive_mixer_748",
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
                "-6731957312620768847": "-6731957312620768847_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_01a",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
        },
    },
    "pulses": {
        "4602749578813007475": {
            "length": 40,
            "waveforms": {
                "I": "4602749578813007475_i",
                "Q": "4602749578813007475_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5588028311087956264": {
            "length": 40,
            "waveforms": {
                "I": "-5588028311087956264_i",
                "Q": "-5588028311087956264_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7020253597009942133": {
            "length": 60,
            "waveforms": {
                "single": "-7020253597009942133",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "521970795558401185_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5167207243399228800_i",
                "Q": "5167207243399228800_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-6731957312620768847_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "8148761029708680177_i",
                "Q": "8148761029708680177_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8356808681133512007": {
            "length": 60,
            "waveforms": {
                "single": "8356808681133512007",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3771244817455671925": {
            "length": 16,
            "waveforms": {
                "single": "-3771244817455671925",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8462667552616981714": {
            "length": 16,
            "waveforms": {
                "single": "8462667552616981714",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5860322382555460549": {
            "length": 16,
            "waveforms": {
                "single": "5860322382555460549",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-890400669191201799": {
            "length": 16,
            "waveforms": {
                "single": "-890400669191201799",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8900901897644036204": {
            "length": 16,
            "waveforms": {
                "single": "8900901897644036204",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1307359018811965064": {
            "length": 16,
            "waveforms": {
                "single": "1307359018811965064",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4312632359038751066": {
            "length": 16,
            "waveforms": {
                "single": "-4312632359038751066",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3892896930188240713": {
            "length": 16,
            "waveforms": {
                "single": "3892896930188240713",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5107323941209020338": {
            "length": 16,
            "waveforms": {
                "single": "5107323941209020338",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1893378611836868955": {
            "length": 16,
            "waveforms": {
                "single": "-1893378611836868955",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1913793294405754696": {
            "length": 16,
            "waveforms": {
                "single": "1913793294405754696",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4964603720578936779": {
            "length": 16,
            "waveforms": {
                "single": "-4964603720578936779",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5908450627470600069": {
            "length": 16,
            "waveforms": {
                "single": "-5908450627470600069",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5537590893193062254": {
            "length": 16,
            "waveforms": {
                "single": "5537590893193062254",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4703623891289497583": {
            "length": 16,
            "waveforms": {
                "single": "-4703623891289497583",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4482129832090782335": {
            "length": 16,
            "waveforms": {
                "single": "-4482129832090782335",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "40187937999220981": {
            "length": 16,
            "waveforms": {
                "single": "40187937999220981",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1744012936758046388": {
            "length": 20,
            "waveforms": {
                "single": "1744012936758046388",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7830549344248852373": {
            "length": 20,
            "waveforms": {
                "single": "-7830549344248852373",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2948839672939148874": {
            "length": 20,
            "waveforms": {
                "single": "2948839672939148874",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7471157443029152190": {
            "length": 20,
            "waveforms": {
                "single": "7471157443029152190",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2128953153153120772": {
            "length": 24,
            "waveforms": {
                "single": "2128953153153120772",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2350447212351836020": {
            "length": 24,
            "waveforms": {
                "single": "2350447212351836020",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7224115068655062741": {
            "length": 24,
            "waveforms": {
                "single": "-7224115068655062741",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7845440836541756285": {
            "length": 24,
            "waveforms": {
                "single": "-7845440836541756285",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5026355380651895878": {
            "length": 28,
            "waveforms": {
                "single": "-5026355380651895878",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8665327356327784387": {
            "length": 28,
            "waveforms": {
                "single": "-8665327356327784387",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7429051048619473009": {
            "length": 28,
            "waveforms": {
                "single": "7429051048619473009",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4826705878557951844": {
            "length": 28,
            "waveforms": {
                "single": "4826705878557951844",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6246073609125902276": {
            "length": 32,
            "waveforms": {
                "single": "-6246073609125902276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7024465566561118707": {
            "length": 32,
            "waveforms": {
                "single": "7024465566561118707",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3586723520060147398": {
            "length": 32,
            "waveforms": {
                "single": "-3586723520060147398",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6189068690121668563": {
            "length": 32,
            "waveforms": {
                "single": "-6189068690121668563",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6426073105973805853": {
            "length": 36,
            "waveforms": {
                "single": "6426073105973805853",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1167469772858265287": {
            "length": 36,
            "waveforms": {
                "single": "-1167469772858265287",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3769814942919786452": {
            "length": 36,
            "waveforms": {
                "single": "-3769814942919786452",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1418068138518010362": {
            "length": 36,
            "waveforms": {
                "single": "1418068138518010362",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4589701462705814554": {
            "length": 40,
            "waveforms": {
                "single": "-4589701462705814554",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-782529556463190903": {
            "length": 40,
            "waveforms": {
                "single": "-782529556463190903",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4503974389195553549": {
            "length": 40,
            "waveforms": {
                "single": "4503974389195553549",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1308788893347850537": {
            "length": 40,
            "waveforms": {
                "single": "1308788893347850537",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9070531702746656819": {
            "length": 44,
            "waveforms": {
                "single": "9070531702746656819",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "488902373561822435": {
            "length": 44,
            "waveforms": {
                "single": "488902373561822435",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7178452682959727934": {
            "length": 44,
            "waveforms": {
                "single": "-7178452682959727934",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1693729109742924921": {
            "length": 44,
            "waveforms": {
                "single": "1693729109742924921",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1915223168941640169": {
            "length": 48,
            "waveforms": {
                "single": "1915223168941640169",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4759198935757845823": {
            "length": 48,
            "waveforms": {
                "single": "-4759198935757845823",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8141365937790468892": {
            "length": 48,
            "waveforms": {
                "single": "8141365937790468892",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "474010881268918523": {
            "length": 48,
            "waveforms": {
                "single": "474010881268918523",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-9100551399737980238": {
            "length": 52,
            "waveforms": {
                "single": "-9100551399737980238",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7886124388717200613": {
            "length": 52,
            "waveforms": {
                "single": "-7886124388717200613",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8526306154185543276": {
            "length": 52,
            "waveforms": {
                "single": "8526306154185543276",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8747800213384258524": {
            "length": 52,
            "waveforms": {
                "single": "8747800213384258524",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5552614717536555512": {
            "length": 56,
            "waveforms": {
                "single": "5552614717536555512",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7501184172322126229": {
            "length": 56,
            "waveforms": {
                "single": "-7501184172322126229",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7279690113123410981": {
            "length": 56,
            "waveforms": {
                "single": "-7279690113123410981",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2130383027689006245": {
            "length": 56,
            "waveforms": {
                "single": "2130383027689006245",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2351877086887721493": {
            "length": 60,
            "waveforms": {
                "single": "2351877086887721493",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6229752242297112891": {
            "length": 60,
            "waveforms": {
                "single": "-6229752242297112891",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4549636774890888356": {
            "length": 60,
            "waveforms": {
                "single": "4549636774890888356",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "4602749578813007475_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4602749578813007475_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5588028311087956264_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5588028311087956264_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7020253597009942133": {
            "type": "constant",
            "sample": -0.2388,
        },
        "5167207243399228800_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "5167207243399228800_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8148761029708680177_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "8148761029708680177_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "8356808681133512007": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-3771244817455671925": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8462667552616981714": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5860322382555460549": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-890400669191201799": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8900901897644036204": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1307359018811965064": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4312632359038751066": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3892896930188240713": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5107323941209020338": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1893378611836868955": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1913793294405754696": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4964603720578936779": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5908450627470600069": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5537590893193062254": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4703623891289497583": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4482129832090782335": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "40187937999220981": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "1744012936758046388": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7830549344248852373": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2948839672939148874": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7471157443029152190": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "2128953153153120772": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2350447212351836020": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7224115068655062741": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7845440836541756285": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-5026355380651895878": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8665327356327784387": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7429051048619473009": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4826705878557951844": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-6246073609125902276": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7024465566561118707": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3586723520060147398": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6189068690121668563": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "6426073105973805853": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1167469772858265287": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3769814942919786452": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1418068138518010362": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-4589701462705814554": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-782529556463190903": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4503974389195553549": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1308788893347850537": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "9070531702746656819": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "488902373561822435": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7178452682959727934": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1693729109742924921": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "1915223168941640169": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4759198935757845823": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8141365937790468892": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "474010881268918523": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-9100551399737980238": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7886124388717200613": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8526306154185543276": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8747800213384258524": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5552614717536555512": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7501184172322126229": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7279690113123410981": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2130383027689006245": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "2351877086887721493": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6229752242297112891": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4549636774890888356": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 59 + [0.0],
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
        "B2/drive_mixer_e88": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_b25": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_748": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_01a": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

