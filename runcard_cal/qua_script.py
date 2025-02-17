
# Single QUA script generated at 2025-02-16 17:44:23.760214
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
    a1 = declare(int, value=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
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
            with for_(v9,-1.99,(v9>-1.7508648104151439),(v9*0.9959183673469388)):
                align()
                play("-1931532868188852917", "B2/drive")
                play("-4119846616211447052", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("6832324453961964687"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("-7934921676742992405"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("-7713427617544277157"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-3906255711301653506"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("-5515667929541110294"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("-3961956055518940472"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-7328487401149202773"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("-7106993341950487525"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("2758121402574229707"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("-4909233653947320662"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("5943967540930159814"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("323976163079443684"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("3314407468751863380"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-8036159106906675452"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("169370182320316327"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("-7497984874201234042"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-7775179277617236256"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("3920841744345653012"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("7600339687350247536"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("7821833746548962784"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-5613194569332539734"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-2696575441349599267"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("-2475081382150884019"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-3193940822130657623"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("-2972446762931942375"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("-996181134127490760"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("4955888122879047190"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-8968538180740501110"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("-2587506546536867991"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("7375141870080929301"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-389746858533701128"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("-5838392386601857969"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-1316074616511854653"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("-3640632698598691106"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("-5992998367360985326"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("-6785669985030238159"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("4910351036932651109"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("4633156633516648895"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-3034198423004901474"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("8534148635719958667"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("-1707066148762601170"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("-3188804403764028831"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-1762766492979888136"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("2044405413262735515"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("6566723183352738831"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("5945397415466045287"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("5668203012050043073"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-8971369155416884892"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-8749875096218169644"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("-4227557326128166328"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("-6552115408215002781"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("-2029797638124999465"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("3079451791796129693"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("3203412178901764881"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("6120031306884705348"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("1100348156013643676"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("5622665926103646992"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("3685886067389919325"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("-4895743261794915059"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("-4674249202596199811"*amp(v9), "B4/flux")
                with elif_((v8==60)):
                    play("6105139814591801436"*amp(v9), "B4/flux")
                with elif_((v8==61)):
                    play("-773257200392890039"*amp(v9), "B4/flux")
                with elif_((v8==62)):
                    play("-2254995455394317700"*amp(v9), "B4/flux")
                with elif_((v8==63)):
                    play("2756720302433731398"*amp(v9), "B4/flux")
                with elif_((v8==64)):
                    play("2978214361632446646"*amp(v9), "B4/flux")
                with elif_((v8==65)):
                    play("-388316983997815655"*amp(v9), "B4/flux")
                with elif_((v8==66)):
                    play("5175974049635613509"*amp(v9), "B4/flux")
                with elif_((v8==67)):
                    play("8983145955878237160"*amp(v9), "B4/flux")
                with elif_((v8==68)):
                    play("3363154578027521030"*amp(v9), "B4/flux")
                with elif_((v8==69)):
                    play("167969082179818018"*amp(v9), "B4/flux")
                with elif_((v8==70)):
                    play("7264146580230830802"*amp(v9), "B4/flux")
                with elif_((v8==71)):
                    play("3208548597268393673"*amp(v9), "B4/flux")
                with elif_((v8==72)):
                    play("4634586508052534368"*amp(v9), "B4/flux")
                with elif_((v8==73)):
                    play("8441758414295158019"*amp(v9), "B4/flux")
                with elif_((v8==74)):
                    play("7820432646408464475"*amp(v9), "B4/flux")
                with elif_((v8==75)):
                    play("-7807225971411226734"*amp(v9), "B4/flux")
                with elif_((v8==76)):
                    play("-7585731912212511486"*amp(v9), "B4/flux")
                with elif_((v8==77)):
                    play("-3906233969207916962"*amp(v9), "B4/flux")
                with elif_((v8==78)):
                    play("2045835287798620988"*amp(v9), "B4/flux")
                with elif_((v8==79)):
                    play("-5166478165010629375"*amp(v9), "B4/flux")
                with elif_((v8==80)):
                    play("-154762407182580277"*amp(v9), "B4/flux")
                with elif_((v8==81)):
                    play("4465089035000503099"*amp(v9), "B4/flux")
                with elif_((v8==82)):
                    play("-3299799693614127330"*amp(v9), "B4/flux")
                with elif_((v8==83)):
                    play("2264491340019301834"*amp(v9), "B4/flux")
                with elif_((v8==84)):
                    play("-5929359765792423764"*amp(v9), "B4/flux")
                with elif_((v8==85)):
                    play("-6550685533679117308"*amp(v9), "B4/flux")
                with elif_((v8==86)):
                    play("-6329191474480402060"*amp(v9), "B4/flux")
                with elif_((v8==87)):
                    play("-8751283228660318573"*amp(v9), "B4/flux")
                with elif_((v8==88)):
                    play("-4131431786477235197"*amp(v9), "B4/flux")
                with elif_((v8==89)):
                    play("1723103798436222693"*amp(v9), "B4/flux")
                with elif_((v8==90)):
                    play("-5944251258085327676"*amp(v9), "B4/flux")
                with elif_((v8==91)):
                    play("5624095800639532465"*amp(v9), "B4/flux")
                with elif_((v8==92)):
                    play("-3746491570082160813"*amp(v9), "B4/flux")
                with elif_((v8==93)):
                    play("-6098857238844455033"*amp(v9), "B4/flux")
                with elif_((v8==94)):
                    play("-4672819328060314338"*amp(v9), "B4/flux")
                with elif_((v8==95)):
                    play("-865647421817690687"*amp(v9), "B4/flux")
                with elif_((v8==96)):
                    play("-6873417023041515603"*amp(v9), "B4/flux")
                with elif_((v8==97)):
                    play("1332112266185476176"*amp(v9), "B4/flux")
                with elif_((v8==98)):
                    play("2758150176969616871"*amp(v9), "B4/flux")
                with elif_((v8==99)):
                    play("6565322083212240522"*amp(v9), "B4/flux")
                with elif_((v8==100)):
                    play("3751366013387358287"*amp(v9), "B4/flux")
                with elif_((v8==101)):
                    play("5177403924171498982"*amp(v9), "B4/flux")
                with elif_((v8==102)):
                    play("8984575830414122633"*amp(v9), "B4/flux")
                with elif_((v8==103)):
                    play("-4939850473205425667"*amp(v9), "B4/flux")
                with elif_((v8==104)):
                    play("-7264408555292262120"*amp(v9), "B4/flux")
                with elif_((v8==105)):
                    play("-7042914496093546872"*amp(v9), "B4/flux")
                with elif_((v8==106)):
                    play("3209978471804279146"*amp(v9), "B4/flux")
                with elif_((v8==107)):
                    play("-1809704679066782526"*amp(v9), "B4/flux")
                with elif_((v8==108)):
                    play("1009380776823077881"*amp(v9), "B4/flux")
                with elif_((v8==109)):
                    play("388055008936384337"*amp(v9), "B4/flux")
                with elif_((v8==110)):
                    play("-7805796096875341261"*amp(v9), "B4/flux")
                with elif_((v8==111)):
                    play("-7584302037676626013"*amp(v9), "B4/flux")
                with elif_((v8==112)):
                    play("-210337451650928517"*amp(v9), "B4/flux")
                with elif_((v8==113)):
                    play("-5386542349673459150"*amp(v9), "B4/flux")
                with elif_((v8==114)):
                    play("994489284530173969"*amp(v9), "B4/flux")
                with elif_((v8==115)):
                    play("-153332532646694804"*amp(v9), "B4/flux")
                with elif_((v8==116)):
                    play("68161526552020444"*amp(v9), "B4/flux")
                with elif_((v8==117)):
                    play("2044427155356472059"*amp(v9), "B4/flux")
                with elif_((v8==118)):
                    play("2265921214555187307"*amp(v9), "B4/flux")
                with elif_((v8==119)):
                    play("6073093120797810958"*amp(v9), "B4/flux")
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
                play("-4119846616211447052", "B4/drive")
                measure("-5883642134343778711", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.7301907560047289)-(v3*0.6832433386760843))>0.002418478083593086)))
                r1 = declare_stream()
                save(v4, r1)
                measure("-9051730280076712279", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.47462054560365174)-(v6*0.8801905121568239))>-0.0004093731107439933)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(30).buffer(120).average().save("-5883642134343778711_B2|acquisition_shots")
        r2.buffer(30).buffer(120).average().save("-9051730280076712279_B4|acquisition_shots")


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
                "7366082749308304271": "7366082749308304271",
                "7499131031581951653": "7499131031581951653",
                "6832324453961964687": "6832324453961964687",
                "-7934921676742992405": "-7934921676742992405",
                "-7713427617544277157": "-7713427617544277157",
                "-3906255711301653506": "-3906255711301653506",
                "-5515667929541110294": "-5515667929541110294",
                "-3961956055518940472": "-3961956055518940472",
                "-7328487401149202773": "-7328487401149202773",
                "-7106993341950487525": "-7106993341950487525",
                "2758121402574229707": "2758121402574229707",
                "-4909233653947320662": "-4909233653947320662",
                "5943967540930159814": "5943967540930159814",
                "323976163079443684": "323976163079443684",
                "3314407468751863380": "3314407468751863380",
                "-8036159106906675452": "-8036159106906675452",
                "169370182320316327": "169370182320316327",
                "-7497984874201234042": "-7497984874201234042",
                "-7775179277617236256": "-7775179277617236256",
                "3920841744345653012": "3920841744345653012",
                "7600339687350247536": "7600339687350247536",
                "7821833746548962784": "7821833746548962784",
                "-5613194569332539734": "-5613194569332539734",
                "-2696575441349599267": "-2696575441349599267",
                "-2475081382150884019": "-2475081382150884019",
                "-3193940822130657623": "-3193940822130657623",
                "-2972446762931942375": "-2972446762931942375",
                "-996181134127490760": "-996181134127490760",
                "4955888122879047190": "4955888122879047190",
                "-8968538180740501110": "-8968538180740501110",
                "-2587506546536867991": "-2587506546536867991",
                "7375141870080929301": "7375141870080929301",
                "-389746858533701128": "-389746858533701128",
                "-5838392386601857969": "-5838392386601857969",
                "-1316074616511854653": "-1316074616511854653",
                "-3640632698598691106": "-3640632698598691106",
                "-5992998367360985326": "-5992998367360985326",
                "-6785669985030238159": "-6785669985030238159",
                "4910351036932651109": "4910351036932651109",
                "4633156633516648895": "4633156633516648895",
                "-3034198423004901474": "-3034198423004901474",
                "8534148635719958667": "8534148635719958667",
                "-1707066148762601170": "-1707066148762601170",
                "-3188804403764028831": "-3188804403764028831",
                "-1762766492979888136": "-1762766492979888136",
                "2044405413262735515": "2044405413262735515",
                "6566723183352738831": "6566723183352738831",
                "5945397415466045287": "5945397415466045287",
                "5668203012050043073": "5668203012050043073",
                "-8971369155416884892": "-8971369155416884892",
                "-8749875096218169644": "-8749875096218169644",
                "-4227557326128166328": "-4227557326128166328",
                "-6552115408215002781": "-6552115408215002781",
                "-2029797638124999465": "-2029797638124999465",
                "3079451791796129693": "3079451791796129693",
                "3203412178901764881": "3203412178901764881",
                "6120031306884705348": "6120031306884705348",
                "1100348156013643676": "1100348156013643676",
                "5622665926103646992": "5622665926103646992",
                "3685886067389919325": "3685886067389919325",
                "-4895743261794915059": "-4895743261794915059",
                "-4674249202596199811": "-4674249202596199811",
                "6105139814591801436": "6105139814591801436",
                "-773257200392890039": "-773257200392890039",
                "-2254995455394317700": "-2254995455394317700",
                "2756720302433731398": "2756720302433731398",
                "2978214361632446646": "2978214361632446646",
                "-388316983997815655": "-388316983997815655",
                "5175974049635613509": "5175974049635613509",
                "8983145955878237160": "8983145955878237160",
                "3363154578027521030": "3363154578027521030",
                "167969082179818018": "167969082179818018",
                "7264146580230830802": "7264146580230830802",
                "3208548597268393673": "3208548597268393673",
                "4634586508052534368": "4634586508052534368",
                "8441758414295158019": "8441758414295158019",
                "7820432646408464475": "7820432646408464475",
                "-7807225971411226734": "-7807225971411226734",
                "-7585731912212511486": "-7585731912212511486",
                "-3906233969207916962": "-3906233969207916962",
                "2045835287798620988": "2045835287798620988",
                "-5166478165010629375": "-5166478165010629375",
                "-154762407182580277": "-154762407182580277",
                "4465089035000503099": "4465089035000503099",
                "-3299799693614127330": "-3299799693614127330",
                "2264491340019301834": "2264491340019301834",
                "-5929359765792423764": "-5929359765792423764",
                "-6550685533679117308": "-6550685533679117308",
                "-6329191474480402060": "-6329191474480402060",
                "-8751283228660318573": "-8751283228660318573",
                "-4131431786477235197": "-4131431786477235197",
                "1723103798436222693": "1723103798436222693",
                "-5944251258085327676": "-5944251258085327676",
                "5624095800639532465": "5624095800639532465",
                "-3746491570082160813": "-3746491570082160813",
                "-6098857238844455033": "-6098857238844455033",
                "-4672819328060314338": "-4672819328060314338",
                "-865647421817690687": "-865647421817690687",
                "-6873417023041515603": "-6873417023041515603",
                "1332112266185476176": "1332112266185476176",
                "2758150176969616871": "2758150176969616871",
                "6565322083212240522": "6565322083212240522",
                "3751366013387358287": "3751366013387358287",
                "5177403924171498982": "5177403924171498982",
                "8984575830414122633": "8984575830414122633",
                "-4939850473205425667": "-4939850473205425667",
                "-7264408555292262120": "-7264408555292262120",
                "-7042914496093546872": "-7042914496093546872",
                "3209978471804279146": "3209978471804279146",
                "-1809704679066782526": "-1809704679066782526",
                "1009380776823077881": "1009380776823077881",
                "388055008936384337": "388055008936384337",
                "-7805796096875341261": "-7805796096875341261",
                "-7584302037676626013": "-7584302037676626013",
                "-210337451650928517": "-210337451650928517",
                "-5386542349673459150": "-5386542349673459150",
                "994489284530173969": "994489284530173969",
                "-153332532646694804": "-153332532646694804",
                "68161526552020444": "68161526552020444",
                "2044427155356472059": "2044427155356472059",
                "2265921214555187307": "2265921214555187307",
                "6073093120797810958": "6073093120797810958",
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
                "-1931532868188852917": "-1931532868188852917",
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
                "-9051730280076712279": "-9051730280076712279_B4/acquisition",
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
                "-5883642134343778711": "-5883642134343778711_B2/acquisition",
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
                "-4119846616211447052": "-4119846616211447052",
            },
        },
    },
    "pulses": {
        "-1931532868188852917": {
            "length": 40,
            "waveforms": {
                "I": "-1931532868188852917_i",
                "Q": "-1931532868188852917_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4119846616211447052": {
            "length": 40,
            "waveforms": {
                "I": "-4119846616211447052_i",
                "Q": "-4119846616211447052_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7366082749308304271": {
            "length": 120,
            "waveforms": {
                "single": "7366082749308304271",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5883642134343778711_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "5788555058534269470_i",
                "Q": "5788555058534269470_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-9051730280076712279_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-7423175196645376940_i",
                "Q": "-7423175196645376940_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "7499131031581951653": {
            "length": 120,
            "waveforms": {
                "single": "7499131031581951653",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6832324453961964687": {
            "length": 16,
            "waveforms": {
                "single": "6832324453961964687",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7934921676742992405": {
            "length": 16,
            "waveforms": {
                "single": "-7934921676742992405",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7713427617544277157": {
            "length": 16,
            "waveforms": {
                "single": "-7713427617544277157",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3906255711301653506": {
            "length": 16,
            "waveforms": {
                "single": "-3906255711301653506",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5515667929541110294": {
            "length": 16,
            "waveforms": {
                "single": "-5515667929541110294",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3961956055518940472": {
            "length": 16,
            "waveforms": {
                "single": "-3961956055518940472",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7328487401149202773": {
            "length": 16,
            "waveforms": {
                "single": "-7328487401149202773",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7106993341950487525": {
            "length": 16,
            "waveforms": {
                "single": "-7106993341950487525",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2758121402574229707": {
            "length": 16,
            "waveforms": {
                "single": "2758121402574229707",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4909233653947320662": {
            "length": 16,
            "waveforms": {
                "single": "-4909233653947320662",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5943967540930159814": {
            "length": 16,
            "waveforms": {
                "single": "5943967540930159814",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "323976163079443684": {
            "length": 16,
            "waveforms": {
                "single": "323976163079443684",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3314407468751863380": {
            "length": 16,
            "waveforms": {
                "single": "3314407468751863380",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8036159106906675452": {
            "length": 16,
            "waveforms": {
                "single": "-8036159106906675452",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "169370182320316327": {
            "length": 16,
            "waveforms": {
                "single": "169370182320316327",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7497984874201234042": {
            "length": 16,
            "waveforms": {
                "single": "-7497984874201234042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7775179277617236256": {
            "length": 16,
            "waveforms": {
                "single": "-7775179277617236256",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3920841744345653012": {
            "length": 20,
            "waveforms": {
                "single": "3920841744345653012",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7600339687350247536": {
            "length": 20,
            "waveforms": {
                "single": "7600339687350247536",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7821833746548962784": {
            "length": 20,
            "waveforms": {
                "single": "7821833746548962784",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5613194569332539734": {
            "length": 20,
            "waveforms": {
                "single": "-5613194569332539734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2696575441349599267": {
            "length": 24,
            "waveforms": {
                "single": "-2696575441349599267",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2475081382150884019": {
            "length": 24,
            "waveforms": {
                "single": "-2475081382150884019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3193940822130657623": {
            "length": 24,
            "waveforms": {
                "single": "-3193940822130657623",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2972446762931942375": {
            "length": 24,
            "waveforms": {
                "single": "-2972446762931942375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-996181134127490760": {
            "length": 28,
            "waveforms": {
                "single": "-996181134127490760",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4955888122879047190": {
            "length": 28,
            "waveforms": {
                "single": "4955888122879047190",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8968538180740501110": {
            "length": 28,
            "waveforms": {
                "single": "-8968538180740501110",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2587506546536867991": {
            "length": 28,
            "waveforms": {
                "single": "-2587506546536867991",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7375141870080929301": {
            "length": 32,
            "waveforms": {
                "single": "7375141870080929301",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-389746858533701128": {
            "length": 32,
            "waveforms": {
                "single": "-389746858533701128",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5838392386601857969": {
            "length": 32,
            "waveforms": {
                "single": "-5838392386601857969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1316074616511854653": {
            "length": 32,
            "waveforms": {
                "single": "-1316074616511854653",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3640632698598691106": {
            "length": 36,
            "waveforms": {
                "single": "-3640632698598691106",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5992998367360985326": {
            "length": 36,
            "waveforms": {
                "single": "-5992998367360985326",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6785669985030238159": {
            "length": 36,
            "waveforms": {
                "single": "-6785669985030238159",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4910351036932651109": {
            "length": 36,
            "waveforms": {
                "single": "4910351036932651109",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4633156633516648895": {
            "length": 40,
            "waveforms": {
                "single": "4633156633516648895",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3034198423004901474": {
            "length": 40,
            "waveforms": {
                "single": "-3034198423004901474",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8534148635719958667": {
            "length": 40,
            "waveforms": {
                "single": "8534148635719958667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1707066148762601170": {
            "length": 40,
            "waveforms": {
                "single": "-1707066148762601170",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3188804403764028831": {
            "length": 44,
            "waveforms": {
                "single": "-3188804403764028831",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1762766492979888136": {
            "length": 44,
            "waveforms": {
                "single": "-1762766492979888136",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2044405413262735515": {
            "length": 44,
            "waveforms": {
                "single": "2044405413262735515",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6566723183352738831": {
            "length": 44,
            "waveforms": {
                "single": "6566723183352738831",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5945397415466045287": {
            "length": 48,
            "waveforms": {
                "single": "5945397415466045287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5668203012050043073": {
            "length": 48,
            "waveforms": {
                "single": "5668203012050043073",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8971369155416884892": {
            "length": 48,
            "waveforms": {
                "single": "-8971369155416884892",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8749875096218169644": {
            "length": 48,
            "waveforms": {
                "single": "-8749875096218169644",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4227557326128166328": {
            "length": 52,
            "waveforms": {
                "single": "-4227557326128166328",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6552115408215002781": {
            "length": 52,
            "waveforms": {
                "single": "-6552115408215002781",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2029797638124999465": {
            "length": 52,
            "waveforms": {
                "single": "-2029797638124999465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3079451791796129693": {
            "length": 52,
            "waveforms": {
                "single": "3079451791796129693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3203412178901764881": {
            "length": 56,
            "waveforms": {
                "single": "3203412178901764881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6120031306884705348": {
            "length": 56,
            "waveforms": {
                "single": "6120031306884705348",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1100348156013643676": {
            "length": 56,
            "waveforms": {
                "single": "1100348156013643676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5622665926103646992": {
            "length": 56,
            "waveforms": {
                "single": "5622665926103646992",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3685886067389919325": {
            "length": 60,
            "waveforms": {
                "single": "3685886067389919325",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4895743261794915059": {
            "length": 60,
            "waveforms": {
                "single": "-4895743261794915059",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4674249202596199811": {
            "length": 60,
            "waveforms": {
                "single": "-4674249202596199811",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6105139814591801436": {
            "length": 60,
            "waveforms": {
                "single": "6105139814591801436",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-773257200392890039": {
            "length": 64,
            "waveforms": {
                "single": "-773257200392890039",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2254995455394317700": {
            "length": 64,
            "waveforms": {
                "single": "-2254995455394317700",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2756720302433731398": {
            "length": 64,
            "waveforms": {
                "single": "2756720302433731398",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2978214361632446646": {
            "length": 64,
            "waveforms": {
                "single": "2978214361632446646",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-388316983997815655": {
            "length": 68,
            "waveforms": {
                "single": "-388316983997815655",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5175974049635613509": {
            "length": 68,
            "waveforms": {
                "single": "5175974049635613509",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8983145955878237160": {
            "length": 68,
            "waveforms": {
                "single": "8983145955878237160",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3363154578027521030": {
            "length": 68,
            "waveforms": {
                "single": "3363154578027521030",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "167969082179818018": {
            "length": 72,
            "waveforms": {
                "single": "167969082179818018",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7264146580230830802": {
            "length": 72,
            "waveforms": {
                "single": "7264146580230830802",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3208548597268393673": {
            "length": 72,
            "waveforms": {
                "single": "3208548597268393673",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4634586508052534368": {
            "length": 72,
            "waveforms": {
                "single": "4634586508052534368",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8441758414295158019": {
            "length": 76,
            "waveforms": {
                "single": "8441758414295158019",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7820432646408464475": {
            "length": 76,
            "waveforms": {
                "single": "7820432646408464475",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7807225971411226734": {
            "length": 76,
            "waveforms": {
                "single": "-7807225971411226734",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7585731912212511486": {
            "length": 76,
            "waveforms": {
                "single": "-7585731912212511486",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3906233969207916962": {
            "length": 80,
            "waveforms": {
                "single": "-3906233969207916962",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2045835287798620988": {
            "length": 80,
            "waveforms": {
                "single": "2045835287798620988",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5166478165010629375": {
            "length": 80,
            "waveforms": {
                "single": "-5166478165010629375",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-154762407182580277": {
            "length": 80,
            "waveforms": {
                "single": "-154762407182580277",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4465089035000503099": {
            "length": 84,
            "waveforms": {
                "single": "4465089035000503099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3299799693614127330": {
            "length": 84,
            "waveforms": {
                "single": "-3299799693614127330",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2264491340019301834": {
            "length": 84,
            "waveforms": {
                "single": "2264491340019301834",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5929359765792423764": {
            "length": 84,
            "waveforms": {
                "single": "-5929359765792423764",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6550685533679117308": {
            "length": 88,
            "waveforms": {
                "single": "-6550685533679117308",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6329191474480402060": {
            "length": 88,
            "waveforms": {
                "single": "-6329191474480402060",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8751283228660318573": {
            "length": 88,
            "waveforms": {
                "single": "-8751283228660318573",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4131431786477235197": {
            "length": 88,
            "waveforms": {
                "single": "-4131431786477235197",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1723103798436222693": {
            "length": 92,
            "waveforms": {
                "single": "1723103798436222693",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5944251258085327676": {
            "length": 92,
            "waveforms": {
                "single": "-5944251258085327676",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5624095800639532465": {
            "length": 92,
            "waveforms": {
                "single": "5624095800639532465",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3746491570082160813": {
            "length": 92,
            "waveforms": {
                "single": "-3746491570082160813",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6098857238844455033": {
            "length": 96,
            "waveforms": {
                "single": "-6098857238844455033",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4672819328060314338": {
            "length": 96,
            "waveforms": {
                "single": "-4672819328060314338",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-865647421817690687": {
            "length": 96,
            "waveforms": {
                "single": "-865647421817690687",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6873417023041515603": {
            "length": 96,
            "waveforms": {
                "single": "-6873417023041515603",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1332112266185476176": {
            "length": 100,
            "waveforms": {
                "single": "1332112266185476176",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2758150176969616871": {
            "length": 100,
            "waveforms": {
                "single": "2758150176969616871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6565322083212240522": {
            "length": 100,
            "waveforms": {
                "single": "6565322083212240522",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3751366013387358287": {
            "length": 100,
            "waveforms": {
                "single": "3751366013387358287",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5177403924171498982": {
            "length": 104,
            "waveforms": {
                "single": "5177403924171498982",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8984575830414122633": {
            "length": 104,
            "waveforms": {
                "single": "8984575830414122633",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4939850473205425667": {
            "length": 104,
            "waveforms": {
                "single": "-4939850473205425667",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7264408555292262120": {
            "length": 104,
            "waveforms": {
                "single": "-7264408555292262120",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7042914496093546872": {
            "length": 108,
            "waveforms": {
                "single": "-7042914496093546872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3209978471804279146": {
            "length": 108,
            "waveforms": {
                "single": "3209978471804279146",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1809704679066782526": {
            "length": 108,
            "waveforms": {
                "single": "-1809704679066782526",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1009380776823077881": {
            "length": 108,
            "waveforms": {
                "single": "1009380776823077881",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "388055008936384337": {
            "length": 112,
            "waveforms": {
                "single": "388055008936384337",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7805796096875341261": {
            "length": 112,
            "waveforms": {
                "single": "-7805796096875341261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7584302037676626013": {
            "length": 112,
            "waveforms": {
                "single": "-7584302037676626013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-210337451650928517": {
            "length": 112,
            "waveforms": {
                "single": "-210337451650928517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5386542349673459150": {
            "length": 116,
            "waveforms": {
                "single": "-5386542349673459150",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "994489284530173969": {
            "length": 116,
            "waveforms": {
                "single": "994489284530173969",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-153332532646694804": {
            "length": 116,
            "waveforms": {
                "single": "-153332532646694804",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "68161526552020444": {
            "length": 116,
            "waveforms": {
                "single": "68161526552020444",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2044427155356472059": {
            "length": 120,
            "waveforms": {
                "single": "2044427155356472059",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2265921214555187307": {
            "length": 120,
            "waveforms": {
                "single": "2265921214555187307",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6073093120797810958": {
            "length": 120,
            "waveforms": {
                "single": "6073093120797810958",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-1931532868188852917_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "-1931532868188852917_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "-4119846616211447052_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "-4119846616211447052_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "7366082749308304271": {
            "sample": -0.2388,
            "type": "constant",
        },
        "5788555058534269470_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "5788555058534269470_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-7423175196645376940_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-7423175196645376940_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7499131031581951653": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "6832324453961964687": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-7934921676742992405": {
            "samples": [0.12311557788944723] + [0.0] * 15,
            "type": "arbitrary",
        },
        "-7713427617544277157": {
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-3906255711301653506": {
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "-5515667929541110294": {
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "-3961956055518940472": {
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-7328487401149202773": {
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "-7106993341950487525": {
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "2758121402574229707": {
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "-4909233653947320662": {
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "5943967540930159814": {
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "323976163079443684": {
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "3314407468751863380": {
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-8036159106906675452": {
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "169370182320316327": {
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7497984874201234042": {
            "samples": [0.12311557788944723] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-7775179277617236256": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3920841744345653012": {
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7600339687350247536": {
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7821833746548962784": {
            "samples": [0.12311557788944723] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-5613194569332539734": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-2696575441349599267": {
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2475081382150884019": {
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3193940822130657623": {
            "samples": [0.12311557788944723] * 23 + [0.0],
            "type": "arbitrary",
        },
        "-2972446762931942375": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-996181134127490760": {
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4955888122879047190": {
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8968538180740501110": {
            "samples": [0.12311557788944723] * 27 + [0.0],
            "type": "arbitrary",
        },
        "-2587506546536867991": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "7375141870080929301": {
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-389746858533701128": {
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5838392386601857969": {
            "samples": [0.12311557788944723] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-1316074616511854653": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-3640632698598691106": {
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5992998367360985326": {
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6785669985030238159": {
            "samples": [0.12311557788944723] * 35 + [0.0],
            "type": "arbitrary",
        },
        "4910351036932651109": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "4633156633516648895": {
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3034198423004901474": {
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8534148635719958667": {
            "samples": [0.12311557788944723] * 39 + [0.0],
            "type": "arbitrary",
        },
        "-1707066148762601170": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-3188804403764028831": {
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1762766492979888136": {
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2044405413262735515": {
            "samples": [0.12311557788944723] * 43 + [0.0],
            "type": "arbitrary",
        },
        "6566723183352738831": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "5945397415466045287": {
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5668203012050043073": {
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8971369155416884892": {
            "samples": [0.12311557788944723] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-8749875096218169644": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-4227557326128166328": {
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6552115408215002781": {
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2029797638124999465": {
            "samples": [0.12311557788944723] * 51 + [0.0],
            "type": "arbitrary",
        },
        "3079451791796129693": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3203412178901764881": {
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6120031306884705348": {
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1100348156013643676": {
            "samples": [0.12311557788944723] * 55 + [0.0],
            "type": "arbitrary",
        },
        "5622665926103646992": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "3685886067389919325": {
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4895743261794915059": {
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4674249202596199811": {
            "samples": [0.12311557788944723] * 59 + [0.0],
            "type": "arbitrary",
        },
        "6105139814591801436": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-773257200392890039": {
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2254995455394317700": {
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2756720302433731398": {
            "samples": [0.12311557788944723] * 63 + [0.0],
            "type": "arbitrary",
        },
        "2978214361632446646": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-388316983997815655": {
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "type": "arbitrary",
        },
        "5175974049635613509": {
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8983145955878237160": {
            "samples": [0.12311557788944723] * 67 + [0.0],
            "type": "arbitrary",
        },
        "3363154578027521030": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "167969082179818018": {
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7264146580230830802": {
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3208548597268393673": {
            "samples": [0.12311557788944723] * 71 + [0.0],
            "type": "arbitrary",
        },
        "4634586508052534368": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "8441758414295158019": {
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "type": "arbitrary",
        },
        "7820432646408464475": {
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7807225971411226734": {
            "samples": [0.12311557788944723] * 75 + [0.0],
            "type": "arbitrary",
        },
        "-7585731912212511486": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-3906233969207916962": {
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2045835287798620988": {
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5166478165010629375": {
            "samples": [0.12311557788944723] * 79 + [0.0],
            "type": "arbitrary",
        },
        "-154762407182580277": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "4465089035000503099": {
            "samples": [0.12311557788944723] * 81 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3299799693614127330": {
            "samples": [0.12311557788944723] * 82 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2264491340019301834": {
            "samples": [0.12311557788944723] * 83 + [0.0],
            "type": "arbitrary",
        },
        "-5929359765792423764": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-6550685533679117308": {
            "samples": [0.12311557788944723] * 85 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6329191474480402060": {
            "samples": [0.12311557788944723] * 86 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8751283228660318573": {
            "samples": [0.12311557788944723] * 87 + [0.0],
            "type": "arbitrary",
        },
        "-4131431786477235197": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1723103798436222693": {
            "samples": [0.12311557788944723] * 89 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5944251258085327676": {
            "samples": [0.12311557788944723] * 90 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5624095800639532465": {
            "samples": [0.12311557788944723] * 91 + [0.0],
            "type": "arbitrary",
        },
        "-3746491570082160813": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-6098857238844455033": {
            "samples": [0.12311557788944723] * 93 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4672819328060314338": {
            "samples": [0.12311557788944723] * 94 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-865647421817690687": {
            "samples": [0.12311557788944723] * 95 + [0.0],
            "type": "arbitrary",
        },
        "-6873417023041515603": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "1332112266185476176": {
            "samples": [0.12311557788944723] * 97 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2758150176969616871": {
            "samples": [0.12311557788944723] * 98 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6565322083212240522": {
            "samples": [0.12311557788944723] * 99 + [0.0],
            "type": "arbitrary",
        },
        "3751366013387358287": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "5177403924171498982": {
            "samples": [0.12311557788944723] * 101 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8984575830414122633": {
            "samples": [0.12311557788944723] * 102 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4939850473205425667": {
            "samples": [0.12311557788944723] * 103 + [0.0],
            "type": "arbitrary",
        },
        "-7264408555292262120": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-7042914496093546872": {
            "samples": [0.12311557788944723] * 105 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3209978471804279146": {
            "samples": [0.12311557788944723] * 106 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1809704679066782526": {
            "samples": [0.12311557788944723] * 107 + [0.0],
            "type": "arbitrary",
        },
        "1009380776823077881": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "388055008936384337": {
            "samples": [0.12311557788944723] * 109 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7805796096875341261": {
            "samples": [0.12311557788944723] * 110 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7584302037676626013": {
            "samples": [0.12311557788944723] * 111 + [0.0],
            "type": "arbitrary",
        },
        "-210337451650928517": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "-5386542349673459150": {
            "samples": [0.12311557788944723] * 113 + [0.0] * 3,
            "type": "arbitrary",
        },
        "994489284530173969": {
            "samples": [0.12311557788944723] * 114 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-153332532646694804": {
            "samples": [0.12311557788944723] * 115 + [0.0],
            "type": "arbitrary",
        },
        "68161526552020444": {
            "sample": 0.12311557788944723,
            "type": "constant",
        },
        "2044427155356472059": {
            "samples": [0.12311557788944723] * 117 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2265921214555187307": {
            "samples": [0.12311557788944723] * 118 + [0.0] * 2,
            "type": "arbitrary",
        },
        "6073093120797810958": {
            "samples": [0.12311557788944723] * 119 + [0.0],
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
                "7366082749308304271": "7366082749308304271",
                "7499131031581951653": "7499131031581951653",
                "6832324453961964687": "6832324453961964687",
                "-7934921676742992405": "-7934921676742992405",
                "-7713427617544277157": "-7713427617544277157",
                "-3906255711301653506": "-3906255711301653506",
                "-5515667929541110294": "-5515667929541110294",
                "-3961956055518940472": "-3961956055518940472",
                "-7328487401149202773": "-7328487401149202773",
                "-7106993341950487525": "-7106993341950487525",
                "2758121402574229707": "2758121402574229707",
                "-4909233653947320662": "-4909233653947320662",
                "5943967540930159814": "5943967540930159814",
                "323976163079443684": "323976163079443684",
                "3314407468751863380": "3314407468751863380",
                "-8036159106906675452": "-8036159106906675452",
                "169370182320316327": "169370182320316327",
                "-7497984874201234042": "-7497984874201234042",
                "-7775179277617236256": "-7775179277617236256",
                "3920841744345653012": "3920841744345653012",
                "7600339687350247536": "7600339687350247536",
                "7821833746548962784": "7821833746548962784",
                "-5613194569332539734": "-5613194569332539734",
                "-2696575441349599267": "-2696575441349599267",
                "-2475081382150884019": "-2475081382150884019",
                "-3193940822130657623": "-3193940822130657623",
                "-2972446762931942375": "-2972446762931942375",
                "-996181134127490760": "-996181134127490760",
                "4955888122879047190": "4955888122879047190",
                "-8968538180740501110": "-8968538180740501110",
                "-2587506546536867991": "-2587506546536867991",
                "7375141870080929301": "7375141870080929301",
                "-389746858533701128": "-389746858533701128",
                "-5838392386601857969": "-5838392386601857969",
                "-1316074616511854653": "-1316074616511854653",
                "-3640632698598691106": "-3640632698598691106",
                "-5992998367360985326": "-5992998367360985326",
                "-6785669985030238159": "-6785669985030238159",
                "4910351036932651109": "4910351036932651109",
                "4633156633516648895": "4633156633516648895",
                "-3034198423004901474": "-3034198423004901474",
                "8534148635719958667": "8534148635719958667",
                "-1707066148762601170": "-1707066148762601170",
                "-3188804403764028831": "-3188804403764028831",
                "-1762766492979888136": "-1762766492979888136",
                "2044405413262735515": "2044405413262735515",
                "6566723183352738831": "6566723183352738831",
                "5945397415466045287": "5945397415466045287",
                "5668203012050043073": "5668203012050043073",
                "-8971369155416884892": "-8971369155416884892",
                "-8749875096218169644": "-8749875096218169644",
                "-4227557326128166328": "-4227557326128166328",
                "-6552115408215002781": "-6552115408215002781",
                "-2029797638124999465": "-2029797638124999465",
                "3079451791796129693": "3079451791796129693",
                "3203412178901764881": "3203412178901764881",
                "6120031306884705348": "6120031306884705348",
                "1100348156013643676": "1100348156013643676",
                "5622665926103646992": "5622665926103646992",
                "3685886067389919325": "3685886067389919325",
                "-4895743261794915059": "-4895743261794915059",
                "-4674249202596199811": "-4674249202596199811",
                "6105139814591801436": "6105139814591801436",
                "-773257200392890039": "-773257200392890039",
                "-2254995455394317700": "-2254995455394317700",
                "2756720302433731398": "2756720302433731398",
                "2978214361632446646": "2978214361632446646",
                "-388316983997815655": "-388316983997815655",
                "5175974049635613509": "5175974049635613509",
                "8983145955878237160": "8983145955878237160",
                "3363154578027521030": "3363154578027521030",
                "167969082179818018": "167969082179818018",
                "7264146580230830802": "7264146580230830802",
                "3208548597268393673": "3208548597268393673",
                "4634586508052534368": "4634586508052534368",
                "8441758414295158019": "8441758414295158019",
                "7820432646408464475": "7820432646408464475",
                "-7807225971411226734": "-7807225971411226734",
                "-7585731912212511486": "-7585731912212511486",
                "-3906233969207916962": "-3906233969207916962",
                "2045835287798620988": "2045835287798620988",
                "-5166478165010629375": "-5166478165010629375",
                "-154762407182580277": "-154762407182580277",
                "4465089035000503099": "4465089035000503099",
                "-3299799693614127330": "-3299799693614127330",
                "2264491340019301834": "2264491340019301834",
                "-5929359765792423764": "-5929359765792423764",
                "-6550685533679117308": "-6550685533679117308",
                "-6329191474480402060": "-6329191474480402060",
                "-8751283228660318573": "-8751283228660318573",
                "-4131431786477235197": "-4131431786477235197",
                "1723103798436222693": "1723103798436222693",
                "-5944251258085327676": "-5944251258085327676",
                "5624095800639532465": "5624095800639532465",
                "-3746491570082160813": "-3746491570082160813",
                "-6098857238844455033": "-6098857238844455033",
                "-4672819328060314338": "-4672819328060314338",
                "-865647421817690687": "-865647421817690687",
                "-6873417023041515603": "-6873417023041515603",
                "1332112266185476176": "1332112266185476176",
                "2758150176969616871": "2758150176969616871",
                "6565322083212240522": "6565322083212240522",
                "3751366013387358287": "3751366013387358287",
                "5177403924171498982": "5177403924171498982",
                "8984575830414122633": "8984575830414122633",
                "-4939850473205425667": "-4939850473205425667",
                "-7264408555292262120": "-7264408555292262120",
                "-7042914496093546872": "-7042914496093546872",
                "3209978471804279146": "3209978471804279146",
                "-1809704679066782526": "-1809704679066782526",
                "1009380776823077881": "1009380776823077881",
                "388055008936384337": "388055008936384337",
                "-7805796096875341261": "-7805796096875341261",
                "-7584302037676626013": "-7584302037676626013",
                "-210337451650928517": "-210337451650928517",
                "-5386542349673459150": "-5386542349673459150",
                "994489284530173969": "994489284530173969",
                "-153332532646694804": "-153332532646694804",
                "68161526552020444": "68161526552020444",
                "2044427155356472059": "2044427155356472059",
                "2265921214555187307": "2265921214555187307",
                "6073093120797810958": "6073093120797810958",
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
                "-1931532868188852917": "-1931532868188852917",
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
                "mixer": "B2/drive_mixer_42f",
                "lo_frequency": 5900000000.0,
            },
            "intermediate_frequency": 63761228.0,
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
                "-9051730280076712279": "-9051730280076712279_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_c91",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 330300527.0,
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
                "-5883642134343778711": "-5883642134343778711_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_904",
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
                "-4119846616211447052": "-4119846616211447052",
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
                "mixer": "B4/drive_mixer_c25",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
        },
    },
    "pulses": {
        "-1931532868188852917": {
            "length": 40,
            "waveforms": {
                "I": "-1931532868188852917_i",
                "Q": "-1931532868188852917_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4119846616211447052": {
            "length": 40,
            "waveforms": {
                "I": "-4119846616211447052_i",
                "Q": "-4119846616211447052_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7366082749308304271": {
            "length": 120,
            "waveforms": {
                "single": "7366082749308304271",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5883642134343778711_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "5788555058534269470_i",
                "Q": "5788555058534269470_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "-9051730280076712279_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-7423175196645376940_i",
                "Q": "-7423175196645376940_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "7499131031581951653": {
            "length": 120,
            "waveforms": {
                "single": "7499131031581951653",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6832324453961964687": {
            "length": 16,
            "waveforms": {
                "single": "6832324453961964687",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7934921676742992405": {
            "length": 16,
            "waveforms": {
                "single": "-7934921676742992405",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7713427617544277157": {
            "length": 16,
            "waveforms": {
                "single": "-7713427617544277157",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3906255711301653506": {
            "length": 16,
            "waveforms": {
                "single": "-3906255711301653506",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5515667929541110294": {
            "length": 16,
            "waveforms": {
                "single": "-5515667929541110294",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3961956055518940472": {
            "length": 16,
            "waveforms": {
                "single": "-3961956055518940472",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7328487401149202773": {
            "length": 16,
            "waveforms": {
                "single": "-7328487401149202773",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7106993341950487525": {
            "length": 16,
            "waveforms": {
                "single": "-7106993341950487525",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2758121402574229707": {
            "length": 16,
            "waveforms": {
                "single": "2758121402574229707",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4909233653947320662": {
            "length": 16,
            "waveforms": {
                "single": "-4909233653947320662",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5943967540930159814": {
            "length": 16,
            "waveforms": {
                "single": "5943967540930159814",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "323976163079443684": {
            "length": 16,
            "waveforms": {
                "single": "323976163079443684",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3314407468751863380": {
            "length": 16,
            "waveforms": {
                "single": "3314407468751863380",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8036159106906675452": {
            "length": 16,
            "waveforms": {
                "single": "-8036159106906675452",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "169370182320316327": {
            "length": 16,
            "waveforms": {
                "single": "169370182320316327",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7497984874201234042": {
            "length": 16,
            "waveforms": {
                "single": "-7497984874201234042",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7775179277617236256": {
            "length": 16,
            "waveforms": {
                "single": "-7775179277617236256",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3920841744345653012": {
            "length": 20,
            "waveforms": {
                "single": "3920841744345653012",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7600339687350247536": {
            "length": 20,
            "waveforms": {
                "single": "7600339687350247536",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7821833746548962784": {
            "length": 20,
            "waveforms": {
                "single": "7821833746548962784",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5613194569332539734": {
            "length": 20,
            "waveforms": {
                "single": "-5613194569332539734",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2696575441349599267": {
            "length": 24,
            "waveforms": {
                "single": "-2696575441349599267",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2475081382150884019": {
            "length": 24,
            "waveforms": {
                "single": "-2475081382150884019",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3193940822130657623": {
            "length": 24,
            "waveforms": {
                "single": "-3193940822130657623",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2972446762931942375": {
            "length": 24,
            "waveforms": {
                "single": "-2972446762931942375",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-996181134127490760": {
            "length": 28,
            "waveforms": {
                "single": "-996181134127490760",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4955888122879047190": {
            "length": 28,
            "waveforms": {
                "single": "4955888122879047190",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8968538180740501110": {
            "length": 28,
            "waveforms": {
                "single": "-8968538180740501110",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2587506546536867991": {
            "length": 28,
            "waveforms": {
                "single": "-2587506546536867991",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7375141870080929301": {
            "length": 32,
            "waveforms": {
                "single": "7375141870080929301",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-389746858533701128": {
            "length": 32,
            "waveforms": {
                "single": "-389746858533701128",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5838392386601857969": {
            "length": 32,
            "waveforms": {
                "single": "-5838392386601857969",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1316074616511854653": {
            "length": 32,
            "waveforms": {
                "single": "-1316074616511854653",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3640632698598691106": {
            "length": 36,
            "waveforms": {
                "single": "-3640632698598691106",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5992998367360985326": {
            "length": 36,
            "waveforms": {
                "single": "-5992998367360985326",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6785669985030238159": {
            "length": 36,
            "waveforms": {
                "single": "-6785669985030238159",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4910351036932651109": {
            "length": 36,
            "waveforms": {
                "single": "4910351036932651109",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4633156633516648895": {
            "length": 40,
            "waveforms": {
                "single": "4633156633516648895",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3034198423004901474": {
            "length": 40,
            "waveforms": {
                "single": "-3034198423004901474",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8534148635719958667": {
            "length": 40,
            "waveforms": {
                "single": "8534148635719958667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1707066148762601170": {
            "length": 40,
            "waveforms": {
                "single": "-1707066148762601170",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3188804403764028831": {
            "length": 44,
            "waveforms": {
                "single": "-3188804403764028831",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1762766492979888136": {
            "length": 44,
            "waveforms": {
                "single": "-1762766492979888136",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2044405413262735515": {
            "length": 44,
            "waveforms": {
                "single": "2044405413262735515",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6566723183352738831": {
            "length": 44,
            "waveforms": {
                "single": "6566723183352738831",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5945397415466045287": {
            "length": 48,
            "waveforms": {
                "single": "5945397415466045287",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5668203012050043073": {
            "length": 48,
            "waveforms": {
                "single": "5668203012050043073",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8971369155416884892": {
            "length": 48,
            "waveforms": {
                "single": "-8971369155416884892",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8749875096218169644": {
            "length": 48,
            "waveforms": {
                "single": "-8749875096218169644",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4227557326128166328": {
            "length": 52,
            "waveforms": {
                "single": "-4227557326128166328",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6552115408215002781": {
            "length": 52,
            "waveforms": {
                "single": "-6552115408215002781",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2029797638124999465": {
            "length": 52,
            "waveforms": {
                "single": "-2029797638124999465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3079451791796129693": {
            "length": 52,
            "waveforms": {
                "single": "3079451791796129693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3203412178901764881": {
            "length": 56,
            "waveforms": {
                "single": "3203412178901764881",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6120031306884705348": {
            "length": 56,
            "waveforms": {
                "single": "6120031306884705348",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1100348156013643676": {
            "length": 56,
            "waveforms": {
                "single": "1100348156013643676",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5622665926103646992": {
            "length": 56,
            "waveforms": {
                "single": "5622665926103646992",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3685886067389919325": {
            "length": 60,
            "waveforms": {
                "single": "3685886067389919325",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4895743261794915059": {
            "length": 60,
            "waveforms": {
                "single": "-4895743261794915059",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4674249202596199811": {
            "length": 60,
            "waveforms": {
                "single": "-4674249202596199811",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6105139814591801436": {
            "length": 60,
            "waveforms": {
                "single": "6105139814591801436",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-773257200392890039": {
            "length": 64,
            "waveforms": {
                "single": "-773257200392890039",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2254995455394317700": {
            "length": 64,
            "waveforms": {
                "single": "-2254995455394317700",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2756720302433731398": {
            "length": 64,
            "waveforms": {
                "single": "2756720302433731398",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2978214361632446646": {
            "length": 64,
            "waveforms": {
                "single": "2978214361632446646",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-388316983997815655": {
            "length": 68,
            "waveforms": {
                "single": "-388316983997815655",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5175974049635613509": {
            "length": 68,
            "waveforms": {
                "single": "5175974049635613509",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8983145955878237160": {
            "length": 68,
            "waveforms": {
                "single": "8983145955878237160",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3363154578027521030": {
            "length": 68,
            "waveforms": {
                "single": "3363154578027521030",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "167969082179818018": {
            "length": 72,
            "waveforms": {
                "single": "167969082179818018",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7264146580230830802": {
            "length": 72,
            "waveforms": {
                "single": "7264146580230830802",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3208548597268393673": {
            "length": 72,
            "waveforms": {
                "single": "3208548597268393673",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4634586508052534368": {
            "length": 72,
            "waveforms": {
                "single": "4634586508052534368",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8441758414295158019": {
            "length": 76,
            "waveforms": {
                "single": "8441758414295158019",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7820432646408464475": {
            "length": 76,
            "waveforms": {
                "single": "7820432646408464475",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7807225971411226734": {
            "length": 76,
            "waveforms": {
                "single": "-7807225971411226734",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7585731912212511486": {
            "length": 76,
            "waveforms": {
                "single": "-7585731912212511486",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3906233969207916962": {
            "length": 80,
            "waveforms": {
                "single": "-3906233969207916962",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2045835287798620988": {
            "length": 80,
            "waveforms": {
                "single": "2045835287798620988",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5166478165010629375": {
            "length": 80,
            "waveforms": {
                "single": "-5166478165010629375",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-154762407182580277": {
            "length": 80,
            "waveforms": {
                "single": "-154762407182580277",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4465089035000503099": {
            "length": 84,
            "waveforms": {
                "single": "4465089035000503099",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3299799693614127330": {
            "length": 84,
            "waveforms": {
                "single": "-3299799693614127330",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2264491340019301834": {
            "length": 84,
            "waveforms": {
                "single": "2264491340019301834",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5929359765792423764": {
            "length": 84,
            "waveforms": {
                "single": "-5929359765792423764",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6550685533679117308": {
            "length": 88,
            "waveforms": {
                "single": "-6550685533679117308",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6329191474480402060": {
            "length": 88,
            "waveforms": {
                "single": "-6329191474480402060",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8751283228660318573": {
            "length": 88,
            "waveforms": {
                "single": "-8751283228660318573",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4131431786477235197": {
            "length": 88,
            "waveforms": {
                "single": "-4131431786477235197",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1723103798436222693": {
            "length": 92,
            "waveforms": {
                "single": "1723103798436222693",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5944251258085327676": {
            "length": 92,
            "waveforms": {
                "single": "-5944251258085327676",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5624095800639532465": {
            "length": 92,
            "waveforms": {
                "single": "5624095800639532465",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3746491570082160813": {
            "length": 92,
            "waveforms": {
                "single": "-3746491570082160813",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6098857238844455033": {
            "length": 96,
            "waveforms": {
                "single": "-6098857238844455033",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4672819328060314338": {
            "length": 96,
            "waveforms": {
                "single": "-4672819328060314338",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-865647421817690687": {
            "length": 96,
            "waveforms": {
                "single": "-865647421817690687",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6873417023041515603": {
            "length": 96,
            "waveforms": {
                "single": "-6873417023041515603",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1332112266185476176": {
            "length": 100,
            "waveforms": {
                "single": "1332112266185476176",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2758150176969616871": {
            "length": 100,
            "waveforms": {
                "single": "2758150176969616871",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6565322083212240522": {
            "length": 100,
            "waveforms": {
                "single": "6565322083212240522",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3751366013387358287": {
            "length": 100,
            "waveforms": {
                "single": "3751366013387358287",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5177403924171498982": {
            "length": 104,
            "waveforms": {
                "single": "5177403924171498982",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8984575830414122633": {
            "length": 104,
            "waveforms": {
                "single": "8984575830414122633",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4939850473205425667": {
            "length": 104,
            "waveforms": {
                "single": "-4939850473205425667",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7264408555292262120": {
            "length": 104,
            "waveforms": {
                "single": "-7264408555292262120",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7042914496093546872": {
            "length": 108,
            "waveforms": {
                "single": "-7042914496093546872",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3209978471804279146": {
            "length": 108,
            "waveforms": {
                "single": "3209978471804279146",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1809704679066782526": {
            "length": 108,
            "waveforms": {
                "single": "-1809704679066782526",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1009380776823077881": {
            "length": 108,
            "waveforms": {
                "single": "1009380776823077881",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "388055008936384337": {
            "length": 112,
            "waveforms": {
                "single": "388055008936384337",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7805796096875341261": {
            "length": 112,
            "waveforms": {
                "single": "-7805796096875341261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7584302037676626013": {
            "length": 112,
            "waveforms": {
                "single": "-7584302037676626013",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-210337451650928517": {
            "length": 112,
            "waveforms": {
                "single": "-210337451650928517",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5386542349673459150": {
            "length": 116,
            "waveforms": {
                "single": "-5386542349673459150",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "994489284530173969": {
            "length": 116,
            "waveforms": {
                "single": "994489284530173969",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-153332532646694804": {
            "length": 116,
            "waveforms": {
                "single": "-153332532646694804",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "68161526552020444": {
            "length": 116,
            "waveforms": {
                "single": "68161526552020444",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2044427155356472059": {
            "length": 120,
            "waveforms": {
                "single": "2044427155356472059",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2265921214555187307": {
            "length": 120,
            "waveforms": {
                "single": "2265921214555187307",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "6073093120797810958": {
            "length": 120,
            "waveforms": {
                "single": "6073093120797810958",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "-1931532868188852917_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1931532868188852917_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4119846616211447052_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4119846616211447052_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7366082749308304271": {
            "type": "constant",
            "sample": -0.2388,
        },
        "5788555058534269470_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "5788555058534269470_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-7423175196645376940_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-7423175196645376940_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "7499131031581951653": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "6832324453961964687": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7934921676742992405": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7713427617544277157": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3906255711301653506": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5515667929541110294": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3961956055518940472": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7328487401149202773": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7106993341950487525": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2758121402574229707": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4909233653947320662": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5943967540930159814": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "323976163079443684": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3314407468751863380": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8036159106906675452": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "169370182320316327": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7497984874201234042": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7775179277617236256": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3920841744345653012": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7600339687350247536": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7821833746548962784": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5613194569332539734": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-2696575441349599267": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2475081382150884019": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3193940822130657623": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2972446762931942375": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-996181134127490760": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4955888122879047190": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8968538180740501110": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2587506546536867991": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "7375141870080929301": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-389746858533701128": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5838392386601857969": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1316074616511854653": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-3640632698598691106": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5992998367360985326": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6785669985030238159": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4910351036932651109": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "4633156633516648895": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3034198423004901474": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8534148635719958667": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1707066148762601170": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-3188804403764028831": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1762766492979888136": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2044405413262735515": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6566723183352738831": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "5945397415466045287": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5668203012050043073": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8971369155416884892": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8749875096218169644": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-4227557326128166328": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6552115408215002781": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2029797638124999465": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3079451791796129693": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3203412178901764881": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6120031306884705348": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1100348156013643676": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5622665926103646992": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "3685886067389919325": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4895743261794915059": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4674249202596199811": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 59 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6105139814591801436": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-773257200392890039": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 61 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2254995455394317700": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 62 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2756720302433731398": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 63 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2978214361632446646": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-388316983997815655": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 65 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5175974049635613509": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 66 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8983145955878237160": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 67 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3363154578027521030": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "167969082179818018": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 69 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7264146580230830802": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 70 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3208548597268393673": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 71 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4634586508052534368": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "8441758414295158019": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 73 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7820432646408464475": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 74 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7807225971411226734": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 75 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7585731912212511486": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-3906233969207916962": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 77 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2045835287798620988": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 78 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5166478165010629375": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 79 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-154762407182580277": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "4465089035000503099": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 81 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3299799693614127330": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 82 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2264491340019301834": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 83 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5929359765792423764": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-6550685533679117308": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 85 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6329191474480402060": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 86 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8751283228660318573": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 87 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4131431786477235197": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "1723103798436222693": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 89 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5944251258085327676": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 90 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5624095800639532465": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 91 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3746491570082160813": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-6098857238844455033": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 93 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4672819328060314338": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 94 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-865647421817690687": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 95 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6873417023041515603": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "1332112266185476176": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 97 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2758150176969616871": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 98 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6565322083212240522": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 99 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3751366013387358287": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "5177403924171498982": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 101 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8984575830414122633": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 102 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4939850473205425667": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 103 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7264408555292262120": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-7042914496093546872": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 105 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3209978471804279146": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 106 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1809704679066782526": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 107 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1009380776823077881": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "388055008936384337": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 109 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7805796096875341261": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 110 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7584302037676626013": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 111 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-210337451650928517": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "-5386542349673459150": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 113 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "994489284530173969": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 114 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-153332532646694804": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 115 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "68161526552020444": {
            "type": "constant",
            "sample": 0.12311557788944723,
        },
        "2044427155356472059": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 117 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2265921214555187307": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 118 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6073093120797810958": {
            "type": "arbitrary",
            "samples": [0.12311557788944723] * 119 + [0.0],
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
        "B2/drive_mixer_42f": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_c91": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_904": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_c25": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

