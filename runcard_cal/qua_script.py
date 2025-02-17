
# Single QUA script generated at 2025-02-17 11:18:23.616351
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
                play("1838827936985706616", "B2/drive")
                play("8147627902512691464", "B4/drive")
                wait(11, "B4/flux")
                with if_((v8==0), unsafe=True):
                    play("3158334417017949022"*amp(v9), "B4/flux")
                with elif_((v8==1)):
                    play("2881140013601946808"*amp(v9), "B4/flux")
                with elif_((v8==2)):
                    play("5356094105021115885"*amp(v9), "B4/flux")
                with elif_((v8==3)):
                    play("-2837757000790609713"*amp(v9), "B4/flux")
                with elif_((v8==4)):
                    play("3543274633413023406"*amp(v9), "B4/flux")
                with elif_((v8==5)):
                    play("1933862415173566618"*amp(v9), "B4/flux")
                with elif_((v8==6)):
                    play("-4816860636573095730"*amp(v9), "B4/flux")
                with elif_((v8==7)):
                    play("5962528380614905517"*amp(v9), "B4/flux")
                with elif_((v8==8)):
                    play("4814706563438036744"*amp(v9), "B4/flux")
                with elif_((v8==9)):
                    play("2490148481351200291"*amp(v9), "B4/flux")
                with elif_((v8==10)):
                    play("7012466251441203607"*amp(v9), "B4/flux")
                with elif_((v8==11)):
                    play("7233960310639918855"*amp(v9), "B4/flux")
                with elif_((v8==12)):
                    play("5199646779833111128"*amp(v9), "B4/flux")
                with elif_((v8==13)):
                    play("-7682806260243011324"*amp(v9), "B4/flux")
                with elif_((v8==14)):
                    play("3096582756944989923"*amp(v9), "B4/flux")
                with elif_((v8==15)):
                    play("7618900527034993239"*amp(v9), "B4/flux")
                with elif_((v8==16)):
                    play("-3560320198840986304"*amp(v9), "B4/flux")
                with elif_((v8==17)):
                    play("-8630083858671391514"*amp(v9), "B4/flux")
                with elif_((v8==18)):
                    play("4368014686970003261"*amp(v9), "B4/flux")
                with elif_((v8==19)):
                    play("-3396874041644627168"*amp(v9), "B4/flux")
                with elif_((v8==20)):
                    play("-3175379982445911920"*amp(v9), "B4/flux")
                with elif_((v8==21)):
                    play("-6370565478293614932"*amp(v9), "B4/flux")
                with elif_((v8==22)):
                    play("4752954903365077645"*amp(v9), "B4/flux")
                with elif_((v8==23)):
                    play("-6426265822510901898"*amp(v9), "B4/flux")
                with elif_((v8==24)):
                    play("4255589522584019289"*amp(v9), "B4/flux")
                with elif_((v8==25)):
                    play("1903223853821725069"*amp(v9), "B4/flux")
                with elif_((v8==26)):
                    play("-421334228265111384"*amp(v9), "B4/flux")
                with elif_((v8==27)):
                    play("-6041325606115827514"*amp(v9), "B4/flux")
                with elif_((v8==28)):
                    play("4322477601023607180"*amp(v9), "B4/flux")
                with elif_((v8==29)):
                    play("-2140333603912517742"*amp(v9), "B4/flux")
                with elif_((v8==30)):
                    play("-6195931586874954871"*amp(v9), "B4/flux")
                with elif_((v8==31)):
                    play("900245911176057913"*amp(v9), "B4/flux")
                with elif_((v8==32)):
                    play("-6693296967656013227"*amp(v9), "B4/flux")
                with elif_((v8==33)):
                    play("4086092049531988020"*amp(v9), "B4/flux")
                with elif_((v8==34)):
                    play("3808897646115985806"*amp(v9), "B4/flux")
                with elif_((v8==35)):
                    play("1456531977353691586"*amp(v9), "B4/flux")
                with elif_((v8==36)):
                    play("-6308356751260938843"*amp(v9), "B4/flux")
                with elif_((v8==37)):
                    play("-6086862692062223595"*amp(v9), "B4/flux")
                with elif_((v8==38)):
                    play("-1965699712493857681"*amp(v9), "B4/flux")
                with elif_((v8==39)):
                    play("8887501482383622795"*amp(v9), "B4/flux")
                with elif_((v8==40)):
                    play("9108995541582338043"*amp(v9), "B4/flux")
                with elif_((v8==41)):
                    play("5742464195952075742"*amp(v9), "B4/flux")
                with elif_((v8==42)):
                    play("-7139988844124046710"*amp(v9), "B4/flux")
                with elif_((v8==43)):
                    play("-2617671074034043394"*amp(v9), "B4/flux")
                with elif_((v8==44)):
                    play("-8952808315732139189"*amp(v9), "B4/flux")
                with elif_((v8==45)):
                    play("-1685284967898567116"*amp(v9), "B4/flux")
                with elif_((v8==46)):
                    play("-5051816313528829417"*amp(v9), "B4/flux")
                with elif_((v8==47)):
                    play("-6533554568530257078"*amp(v9), "B4/flux")
                with elif_((v8==48)):
                    play("-7681376385707125851"*amp(v9), "B4/flux")
                with elif_((v8==49)):
                    play("3098012631480875396"*amp(v9), "B4/flux")
                with elif_((v8==50)):
                    play("3221973018586510584"*amp(v9), "B4/flux")
                with elif_((v8==51)):
                    play("897414936499674131"*amp(v9), "B4/flux")
                with elif_((v8==52)):
                    play("-1454950732262620089"*amp(v9), "B4/flux")
                with elif_((v8==53)):
                    play("-28912821478479394"*amp(v9), "B4/flux")
                with elif_((v8==54)):
                    play("2446041269940689683"*amp(v9), "B4/flux")
                with elif_((v8==55)):
                    play("2168846866524687469"*amp(v9), "B4/flux")
                with elif_((v8==56)):
                    play("5976018772767311120"*amp(v9), "B4/flux")
                with elif_((v8==57)):
                    play("-976190419906859584"*amp(v9), "B4/flux")
                with elif_((v8==58)):
                    play("2830981486335764067"*amp(v9), "B4/flux")
                with elif_((v8==59)):
                    play("8395272519969193231"*amp(v9), "B4/flux")
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
                play("8147627902512691464", "B4/drive")
                measure("-1643082329865217703", "B2/acquisition", None, dual_demod.full("cos", "sin", v2), dual_demod.full("minus_sin", "cos", v3))
                assign(v4, Cast.to_int((((v2*0.12094611657124273)-(v3*0.9926590738447594))>0.0025239896807041085)))
                r1 = declare_stream()
                save(v4, r1)
                measure("8878890889279947537", "B4/acquisition", None, dual_demod.full("cos", "sin", v5), dual_demod.full("minus_sin", "cos", v6))
                assign(v7, Cast.to_int((((v5*0.6951343148494517)-(v6*0.7188798817040184))>-0.0004331116896107868)))
                r2 = declare_stream()
                save(v7, r2)
                wait(25000, )
    with stream_processing():
        r1.buffer(76).buffer(60).average().save("-1643082329865217703_B2|acquisition_shots")
        r2.buffer(76).buffer(60).average().save("8878890889279947537_B4|acquisition_shots")


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
                "5844962937684574577": "5844962937684574577",
                "2775281142118477101": "2775281142118477101",
                "3158334417017949022": "3158334417017949022",
                "2881140013601946808": "2881140013601946808",
                "5356094105021115885": "5356094105021115885",
                "-2837757000790609713": "-2837757000790609713",
                "3543274633413023406": "3543274633413023406",
                "1933862415173566618": "1933862415173566618",
                "-4816860636573095730": "-4816860636573095730",
                "5962528380614905517": "5962528380614905517",
                "4814706563438036744": "4814706563438036744",
                "2490148481351200291": "2490148481351200291",
                "7012466251441203607": "7012466251441203607",
                "7233960310639918855": "7233960310639918855",
                "5199646779833111128": "5199646779833111128",
                "-7682806260243011324": "-7682806260243011324",
                "3096582756944989923": "3096582756944989923",
                "7618900527034993239": "7618900527034993239",
                "-3560320198840986304": "-3560320198840986304",
                "-8630083858671391514": "-8630083858671391514",
                "4368014686970003261": "4368014686970003261",
                "-3396874041644627168": "-3396874041644627168",
                "-3175379982445911920": "-3175379982445911920",
                "-6370565478293614932": "-6370565478293614932",
                "4752954903365077645": "4752954903365077645",
                "-6426265822510901898": "-6426265822510901898",
                "4255589522584019289": "4255589522584019289",
                "1903223853821725069": "1903223853821725069",
                "-421334228265111384": "-421334228265111384",
                "-6041325606115827514": "-6041325606115827514",
                "4322477601023607180": "4322477601023607180",
                "-2140333603912517742": "-2140333603912517742",
                "-6195931586874954871": "-6195931586874954871",
                "900245911176057913": "900245911176057913",
                "-6693296967656013227": "-6693296967656013227",
                "4086092049531988020": "4086092049531988020",
                "3808897646115985806": "3808897646115985806",
                "1456531977353691586": "1456531977353691586",
                "-6308356751260938843": "-6308356751260938843",
                "-6086862692062223595": "-6086862692062223595",
                "-1965699712493857681": "-1965699712493857681",
                "8887501482383622795": "8887501482383622795",
                "9108995541582338043": "9108995541582338043",
                "5742464195952075742": "5742464195952075742",
                "-7139988844124046710": "-7139988844124046710",
                "-2617671074034043394": "-2617671074034043394",
                "-8952808315732139189": "-8952808315732139189",
                "-1685284967898567116": "-1685284967898567116",
                "-5051816313528829417": "-5051816313528829417",
                "-6533554568530257078": "-6533554568530257078",
                "-7681376385707125851": "-7681376385707125851",
                "3098012631480875396": "3098012631480875396",
                "3221973018586510584": "3221973018586510584",
                "897414936499674131": "897414936499674131",
                "-1454950732262620089": "-1454950732262620089",
                "-28912821478479394": "-28912821478479394",
                "2446041269940689683": "2446041269940689683",
                "2168846866524687469": "2168846866524687469",
                "5976018772767311120": "5976018772767311120",
                "-976190419906859584": "-976190419906859584",
                "2830981486335764067": "2830981486335764067",
                "8395272519969193231": "8395272519969193231",
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
                "1838827936985706616": "1838827936985706616",
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
                "8878890889279947537": "8878890889279947537_B4/acquisition",
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
                "8147627902512691464": "8147627902512691464",
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
                "-1643082329865217703": "-1643082329865217703_B2/acquisition",
            },
        },
    },
    "pulses": {
        "1838827936985706616": {
            "length": 40,
            "waveforms": {
                "I": "1838827936985706616_i",
                "Q": "1838827936985706616_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8147627902512691464": {
            "length": 40,
            "waveforms": {
                "I": "8147627902512691464_i",
                "Q": "8147627902512691464_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5844962937684574577": {
            "length": 60,
            "waveforms": {
                "single": "5844962937684574577",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1643082329865217703_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-2171439423006611619_i",
                "Q": "-2171439423006611619_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "8878890889279947537_B4/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-9209889246576681870_i",
                "Q": "-9209889246576681870_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
        },
        "2775281142118477101": {
            "length": 60,
            "waveforms": {
                "single": "2775281142118477101",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3158334417017949022": {
            "length": 16,
            "waveforms": {
                "single": "3158334417017949022",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2881140013601946808": {
            "length": 16,
            "waveforms": {
                "single": "2881140013601946808",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5356094105021115885": {
            "length": 16,
            "waveforms": {
                "single": "5356094105021115885",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2837757000790609713": {
            "length": 16,
            "waveforms": {
                "single": "-2837757000790609713",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3543274633413023406": {
            "length": 16,
            "waveforms": {
                "single": "3543274633413023406",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1933862415173566618": {
            "length": 16,
            "waveforms": {
                "single": "1933862415173566618",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4816860636573095730": {
            "length": 16,
            "waveforms": {
                "single": "-4816860636573095730",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5962528380614905517": {
            "length": 16,
            "waveforms": {
                "single": "5962528380614905517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4814706563438036744": {
            "length": 16,
            "waveforms": {
                "single": "4814706563438036744",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2490148481351200291": {
            "length": 16,
            "waveforms": {
                "single": "2490148481351200291",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7012466251441203607": {
            "length": 16,
            "waveforms": {
                "single": "7012466251441203607",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7233960310639918855": {
            "length": 16,
            "waveforms": {
                "single": "7233960310639918855",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5199646779833111128": {
            "length": 16,
            "waveforms": {
                "single": "5199646779833111128",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7682806260243011324": {
            "length": 16,
            "waveforms": {
                "single": "-7682806260243011324",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3096582756944989923": {
            "length": 16,
            "waveforms": {
                "single": "3096582756944989923",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7618900527034993239": {
            "length": 16,
            "waveforms": {
                "single": "7618900527034993239",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3560320198840986304": {
            "length": 16,
            "waveforms": {
                "single": "-3560320198840986304",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8630083858671391514": {
            "length": 20,
            "waveforms": {
                "single": "-8630083858671391514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4368014686970003261": {
            "length": 20,
            "waveforms": {
                "single": "4368014686970003261",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3396874041644627168": {
            "length": 20,
            "waveforms": {
                "single": "-3396874041644627168",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3175379982445911920": {
            "length": 20,
            "waveforms": {
                "single": "-3175379982445911920",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6370565478293614932": {
            "length": 24,
            "waveforms": {
                "single": "-6370565478293614932",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4752954903365077645": {
            "length": 24,
            "waveforms": {
                "single": "4752954903365077645",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6426265822510901898": {
            "length": 24,
            "waveforms": {
                "single": "-6426265822510901898",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4255589522584019289": {
            "length": 24,
            "waveforms": {
                "single": "4255589522584019289",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1903223853821725069": {
            "length": 28,
            "waveforms": {
                "single": "1903223853821725069",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-421334228265111384": {
            "length": 28,
            "waveforms": {
                "single": "-421334228265111384",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6041325606115827514": {
            "length": 28,
            "waveforms": {
                "single": "-6041325606115827514",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4322477601023607180": {
            "length": 28,
            "waveforms": {
                "single": "4322477601023607180",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2140333603912517742": {
            "length": 32,
            "waveforms": {
                "single": "-2140333603912517742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6195931586874954871": {
            "length": 32,
            "waveforms": {
                "single": "-6195931586874954871",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "900245911176057913": {
            "length": 32,
            "waveforms": {
                "single": "900245911176057913",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6693296967656013227": {
            "length": 32,
            "waveforms": {
                "single": "-6693296967656013227",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4086092049531988020": {
            "length": 36,
            "waveforms": {
                "single": "4086092049531988020",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3808897646115985806": {
            "length": 36,
            "waveforms": {
                "single": "3808897646115985806",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1456531977353691586": {
            "length": 36,
            "waveforms": {
                "single": "1456531977353691586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6308356751260938843": {
            "length": 36,
            "waveforms": {
                "single": "-6308356751260938843",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6086862692062223595": {
            "length": 40,
            "waveforms": {
                "single": "-6086862692062223595",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1965699712493857681": {
            "length": 40,
            "waveforms": {
                "single": "-1965699712493857681",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8887501482383622795": {
            "length": 40,
            "waveforms": {
                "single": "8887501482383622795",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9108995541582338043": {
            "length": 40,
            "waveforms": {
                "single": "9108995541582338043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5742464195952075742": {
            "length": 44,
            "waveforms": {
                "single": "5742464195952075742",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7139988844124046710": {
            "length": 44,
            "waveforms": {
                "single": "-7139988844124046710",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2617671074034043394": {
            "length": 44,
            "waveforms": {
                "single": "-2617671074034043394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8952808315732139189": {
            "length": 44,
            "waveforms": {
                "single": "-8952808315732139189",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1685284967898567116": {
            "length": 48,
            "waveforms": {
                "single": "-1685284967898567116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5051816313528829417": {
            "length": 48,
            "waveforms": {
                "single": "-5051816313528829417",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6533554568530257078": {
            "length": 48,
            "waveforms": {
                "single": "-6533554568530257078",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7681376385707125851": {
            "length": 48,
            "waveforms": {
                "single": "-7681376385707125851",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3098012631480875396": {
            "length": 52,
            "waveforms": {
                "single": "3098012631480875396",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3221973018586510584": {
            "length": 52,
            "waveforms": {
                "single": "3221973018586510584",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "897414936499674131": {
            "length": 52,
            "waveforms": {
                "single": "897414936499674131",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1454950732262620089": {
            "length": 52,
            "waveforms": {
                "single": "-1454950732262620089",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-28912821478479394": {
            "length": 56,
            "waveforms": {
                "single": "-28912821478479394",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2446041269940689683": {
            "length": 56,
            "waveforms": {
                "single": "2446041269940689683",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2168846866524687469": {
            "length": 56,
            "waveforms": {
                "single": "2168846866524687469",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5976018772767311120": {
            "length": 56,
            "waveforms": {
                "single": "5976018772767311120",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-976190419906859584": {
            "length": 60,
            "waveforms": {
                "single": "-976190419906859584",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2830981486335764067": {
            "length": 60,
            "waveforms": {
                "single": "2830981486335764067",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8395272519969193231": {
            "length": 60,
            "waveforms": {
                "single": "8395272519969193231",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "1838827936985706616_i": {
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "type": "arbitrary",
        },
        "1838827936985706616_q": {
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "type": "arbitrary",
        },
        "8147627902512691464_i": {
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "type": "arbitrary",
        },
        "8147627902512691464_q": {
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "type": "arbitrary",
        },
        "5844962937684574577": {
            "sample": -0.2388,
            "type": "constant",
        },
        "-2171439423006611619_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-2171439423006611619_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-9209889246576681870_i": {
            "sample": 0.0033,
            "type": "constant",
        },
        "-9209889246576681870_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "2775281142118477101": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "3158334417017949022": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2881140013601946808": {
            "samples": [0.12562814070351758] + [0.0] * 15,
            "type": "arbitrary",
        },
        "5356094105021115885": {
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "type": "arbitrary",
        },
        "-2837757000790609713": {
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "type": "arbitrary",
        },
        "3543274633413023406": {
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "type": "arbitrary",
        },
        "1933862415173566618": {
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "type": "arbitrary",
        },
        "-4816860636573095730": {
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "type": "arbitrary",
        },
        "5962528380614905517": {
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "type": "arbitrary",
        },
        "4814706563438036744": {
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "type": "arbitrary",
        },
        "2490148481351200291": {
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "type": "arbitrary",
        },
        "7012466251441203607": {
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "type": "arbitrary",
        },
        "7233960310639918855": {
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "type": "arbitrary",
        },
        "5199646779833111128": {
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-7682806260243011324": {
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3096582756944989923": {
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "type": "arbitrary",
        },
        "7618900527034993239": {
            "samples": [0.12562814070351758] * 15 + [0.0],
            "type": "arbitrary",
        },
        "-3560320198840986304": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-8630083858671391514": {
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4368014686970003261": {
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-3396874041644627168": {
            "samples": [0.12562814070351758] * 19 + [0.0],
            "type": "arbitrary",
        },
        "-3175379982445911920": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-6370565478293614932": {
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "type": "arbitrary",
        },
        "4752954903365077645": {
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6426265822510901898": {
            "samples": [0.12562814070351758] * 23 + [0.0],
            "type": "arbitrary",
        },
        "4255589522584019289": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "1903223853821725069": {
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-421334228265111384": {
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6041325606115827514": {
            "samples": [0.12562814070351758] * 27 + [0.0],
            "type": "arbitrary",
        },
        "4322477601023607180": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-2140333603912517742": {
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-6195931586874954871": {
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "type": "arbitrary",
        },
        "900245911176057913": {
            "samples": [0.12562814070351758] * 31 + [0.0],
            "type": "arbitrary",
        },
        "-6693296967656013227": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "4086092049531988020": {
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3808897646115985806": {
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1456531977353691586": {
            "samples": [0.12562814070351758] * 35 + [0.0],
            "type": "arbitrary",
        },
        "-6308356751260938843": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-6086862692062223595": {
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1965699712493857681": {
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8887501482383622795": {
            "samples": [0.12562814070351758] * 39 + [0.0],
            "type": "arbitrary",
        },
        "9108995541582338043": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "5742464195952075742": {
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7139988844124046710": {
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-2617671074034043394": {
            "samples": [0.12562814070351758] * 43 + [0.0],
            "type": "arbitrary",
        },
        "-8952808315732139189": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-1685284967898567116": {
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5051816313528829417": {
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6533554568530257078": {
            "samples": [0.12562814070351758] * 47 + [0.0],
            "type": "arbitrary",
        },
        "-7681376385707125851": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "3098012631480875396": {
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "type": "arbitrary",
        },
        "3221973018586510584": {
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "type": "arbitrary",
        },
        "897414936499674131": {
            "samples": [0.12562814070351758] * 51 + [0.0],
            "type": "arbitrary",
        },
        "-1454950732262620089": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-28912821478479394": {
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2446041269940689683": {
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2168846866524687469": {
            "samples": [0.12562814070351758] * 55 + [0.0],
            "type": "arbitrary",
        },
        "5976018772767311120": {
            "sample": 0.12562814070351758,
            "type": "constant",
        },
        "-976190419906859584": {
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "type": "arbitrary",
        },
        "2830981486335764067": {
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "type": "arbitrary",
        },
        "8395272519969193231": {
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
                "5844962937684574577": "5844962937684574577",
                "2775281142118477101": "2775281142118477101",
                "3158334417017949022": "3158334417017949022",
                "2881140013601946808": "2881140013601946808",
                "5356094105021115885": "5356094105021115885",
                "-2837757000790609713": "-2837757000790609713",
                "3543274633413023406": "3543274633413023406",
                "1933862415173566618": "1933862415173566618",
                "-4816860636573095730": "-4816860636573095730",
                "5962528380614905517": "5962528380614905517",
                "4814706563438036744": "4814706563438036744",
                "2490148481351200291": "2490148481351200291",
                "7012466251441203607": "7012466251441203607",
                "7233960310639918855": "7233960310639918855",
                "5199646779833111128": "5199646779833111128",
                "-7682806260243011324": "-7682806260243011324",
                "3096582756944989923": "3096582756944989923",
                "7618900527034993239": "7618900527034993239",
                "-3560320198840986304": "-3560320198840986304",
                "-8630083858671391514": "-8630083858671391514",
                "4368014686970003261": "4368014686970003261",
                "-3396874041644627168": "-3396874041644627168",
                "-3175379982445911920": "-3175379982445911920",
                "-6370565478293614932": "-6370565478293614932",
                "4752954903365077645": "4752954903365077645",
                "-6426265822510901898": "-6426265822510901898",
                "4255589522584019289": "4255589522584019289",
                "1903223853821725069": "1903223853821725069",
                "-421334228265111384": "-421334228265111384",
                "-6041325606115827514": "-6041325606115827514",
                "4322477601023607180": "4322477601023607180",
                "-2140333603912517742": "-2140333603912517742",
                "-6195931586874954871": "-6195931586874954871",
                "900245911176057913": "900245911176057913",
                "-6693296967656013227": "-6693296967656013227",
                "4086092049531988020": "4086092049531988020",
                "3808897646115985806": "3808897646115985806",
                "1456531977353691586": "1456531977353691586",
                "-6308356751260938843": "-6308356751260938843",
                "-6086862692062223595": "-6086862692062223595",
                "-1965699712493857681": "-1965699712493857681",
                "8887501482383622795": "8887501482383622795",
                "9108995541582338043": "9108995541582338043",
                "5742464195952075742": "5742464195952075742",
                "-7139988844124046710": "-7139988844124046710",
                "-2617671074034043394": "-2617671074034043394",
                "-8952808315732139189": "-8952808315732139189",
                "-1685284967898567116": "-1685284967898567116",
                "-5051816313528829417": "-5051816313528829417",
                "-6533554568530257078": "-6533554568530257078",
                "-7681376385707125851": "-7681376385707125851",
                "3098012631480875396": "3098012631480875396",
                "3221973018586510584": "3221973018586510584",
                "897414936499674131": "897414936499674131",
                "-1454950732262620089": "-1454950732262620089",
                "-28912821478479394": "-28912821478479394",
                "2446041269940689683": "2446041269940689683",
                "2168846866524687469": "2168846866524687469",
                "5976018772767311120": "5976018772767311120",
                "-976190419906859584": "-976190419906859584",
                "2830981486335764067": "2830981486335764067",
                "8395272519969193231": "8395272519969193231",
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
                "1838827936985706616": "1838827936985706616",
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
                "mixer": "B2/drive_mixer_8c2",
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
                "8878890889279947537": "8878890889279947537_B4/acquisition",
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
                "mixer": "B4/acquisition_mixer_e67",
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
                "8147627902512691464": "8147627902512691464",
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
                "mixer": "B4/drive_mixer_2b1",
                "lo_frequency": 6700000000.0,
            },
            "intermediate_frequency": 109615374.0,
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
                "-1643082329865217703": "-1643082329865217703_B2/acquisition",
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
                "mixer": "B2/acquisition_mixer_73d",
                "lo_frequency": 7370000000.0,
            },
            "smearing": 0,
            "time_of_flight": 224,
            "intermediate_frequency": 10040944.0,
        },
    },
    "pulses": {
        "1838827936985706616": {
            "length": 40,
            "waveforms": {
                "I": "1838827936985706616_i",
                "Q": "1838827936985706616_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8147627902512691464": {
            "length": 40,
            "waveforms": {
                "I": "8147627902512691464_i",
                "Q": "8147627902512691464_q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5844962937684574577": {
            "length": 60,
            "waveforms": {
                "single": "5844962937684574577",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1643082329865217703_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-2171439423006611619_i",
                "Q": "-2171439423006611619_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "8878890889279947537_B4/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-9209889246576681870_i",
                "Q": "-9209889246576681870_q",
            },
            "integration_weights": {
                "cos": "cosine_weights_B4/acquisition",
                "sin": "sine_weights_B4/acquisition",
                "minus_sin": "minus_sine_weights_B4/acquisition",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "2775281142118477101": {
            "length": 60,
            "waveforms": {
                "single": "2775281142118477101",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3158334417017949022": {
            "length": 16,
            "waveforms": {
                "single": "3158334417017949022",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2881140013601946808": {
            "length": 16,
            "waveforms": {
                "single": "2881140013601946808",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5356094105021115885": {
            "length": 16,
            "waveforms": {
                "single": "5356094105021115885",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2837757000790609713": {
            "length": 16,
            "waveforms": {
                "single": "-2837757000790609713",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3543274633413023406": {
            "length": 16,
            "waveforms": {
                "single": "3543274633413023406",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1933862415173566618": {
            "length": 16,
            "waveforms": {
                "single": "1933862415173566618",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-4816860636573095730": {
            "length": 16,
            "waveforms": {
                "single": "-4816860636573095730",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5962528380614905517": {
            "length": 16,
            "waveforms": {
                "single": "5962528380614905517",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4814706563438036744": {
            "length": 16,
            "waveforms": {
                "single": "4814706563438036744",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2490148481351200291": {
            "length": 16,
            "waveforms": {
                "single": "2490148481351200291",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7012466251441203607": {
            "length": 16,
            "waveforms": {
                "single": "7012466251441203607",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7233960310639918855": {
            "length": 16,
            "waveforms": {
                "single": "7233960310639918855",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5199646779833111128": {
            "length": 16,
            "waveforms": {
                "single": "5199646779833111128",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7682806260243011324": {
            "length": 16,
            "waveforms": {
                "single": "-7682806260243011324",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3096582756944989923": {
            "length": 16,
            "waveforms": {
                "single": "3096582756944989923",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "7618900527034993239": {
            "length": 16,
            "waveforms": {
                "single": "7618900527034993239",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3560320198840986304": {
            "length": 16,
            "waveforms": {
                "single": "-3560320198840986304",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8630083858671391514": {
            "length": 20,
            "waveforms": {
                "single": "-8630083858671391514",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4368014686970003261": {
            "length": 20,
            "waveforms": {
                "single": "4368014686970003261",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3396874041644627168": {
            "length": 20,
            "waveforms": {
                "single": "-3396874041644627168",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-3175379982445911920": {
            "length": 20,
            "waveforms": {
                "single": "-3175379982445911920",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6370565478293614932": {
            "length": 24,
            "waveforms": {
                "single": "-6370565478293614932",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4752954903365077645": {
            "length": 24,
            "waveforms": {
                "single": "4752954903365077645",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6426265822510901898": {
            "length": 24,
            "waveforms": {
                "single": "-6426265822510901898",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4255589522584019289": {
            "length": 24,
            "waveforms": {
                "single": "4255589522584019289",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1903223853821725069": {
            "length": 28,
            "waveforms": {
                "single": "1903223853821725069",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-421334228265111384": {
            "length": 28,
            "waveforms": {
                "single": "-421334228265111384",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6041325606115827514": {
            "length": 28,
            "waveforms": {
                "single": "-6041325606115827514",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4322477601023607180": {
            "length": 28,
            "waveforms": {
                "single": "4322477601023607180",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2140333603912517742": {
            "length": 32,
            "waveforms": {
                "single": "-2140333603912517742",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6195931586874954871": {
            "length": 32,
            "waveforms": {
                "single": "-6195931586874954871",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "900245911176057913": {
            "length": 32,
            "waveforms": {
                "single": "900245911176057913",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6693296967656013227": {
            "length": 32,
            "waveforms": {
                "single": "-6693296967656013227",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "4086092049531988020": {
            "length": 36,
            "waveforms": {
                "single": "4086092049531988020",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3808897646115985806": {
            "length": 36,
            "waveforms": {
                "single": "3808897646115985806",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "1456531977353691586": {
            "length": 36,
            "waveforms": {
                "single": "1456531977353691586",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6308356751260938843": {
            "length": 36,
            "waveforms": {
                "single": "-6308356751260938843",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6086862692062223595": {
            "length": 40,
            "waveforms": {
                "single": "-6086862692062223595",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1965699712493857681": {
            "length": 40,
            "waveforms": {
                "single": "-1965699712493857681",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8887501482383622795": {
            "length": 40,
            "waveforms": {
                "single": "8887501482383622795",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "9108995541582338043": {
            "length": 40,
            "waveforms": {
                "single": "9108995541582338043",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5742464195952075742": {
            "length": 44,
            "waveforms": {
                "single": "5742464195952075742",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7139988844124046710": {
            "length": 44,
            "waveforms": {
                "single": "-7139988844124046710",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-2617671074034043394": {
            "length": 44,
            "waveforms": {
                "single": "-2617671074034043394",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-8952808315732139189": {
            "length": 44,
            "waveforms": {
                "single": "-8952808315732139189",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1685284967898567116": {
            "length": 48,
            "waveforms": {
                "single": "-1685284967898567116",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-5051816313528829417": {
            "length": 48,
            "waveforms": {
                "single": "-5051816313528829417",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-6533554568530257078": {
            "length": 48,
            "waveforms": {
                "single": "-6533554568530257078",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-7681376385707125851": {
            "length": 48,
            "waveforms": {
                "single": "-7681376385707125851",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3098012631480875396": {
            "length": 52,
            "waveforms": {
                "single": "3098012631480875396",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "3221973018586510584": {
            "length": 52,
            "waveforms": {
                "single": "3221973018586510584",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "897414936499674131": {
            "length": 52,
            "waveforms": {
                "single": "897414936499674131",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-1454950732262620089": {
            "length": 52,
            "waveforms": {
                "single": "-1454950732262620089",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-28912821478479394": {
            "length": 56,
            "waveforms": {
                "single": "-28912821478479394",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2446041269940689683": {
            "length": 56,
            "waveforms": {
                "single": "2446041269940689683",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2168846866524687469": {
            "length": 56,
            "waveforms": {
                "single": "2168846866524687469",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "5976018772767311120": {
            "length": 56,
            "waveforms": {
                "single": "5976018772767311120",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "-976190419906859584": {
            "length": 60,
            "waveforms": {
                "single": "-976190419906859584",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "2830981486335764067": {
            "length": 60,
            "waveforms": {
                "single": "2830981486335764067",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "8395272519969193231": {
            "length": 60,
            "waveforms": {
                "single": "8395272519969193231",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "1838827936985706616_i": {
            "type": "arbitrary",
            "samples": [0.002498607865497148, 0.0033622443858905508, 0.004454250117549496, 0.005809437340997196, 0.00745946520249525, 0.009429647572849292, 0.011735386013558698, 0.014378495509078854, 0.017343776224214638, 0.020596243874322948, 0.024079448635276616, 0.02771527549125696, 0.03140552154923875, 0.035035391033067444, 0.03847884935649202, 0.04160555628836245, 0.04428888412915693, 0.04641435205671371, 0.04788770174785679] + [0.04864182331986816] * 2 + [0.04788770174785679, 0.04641435205671371, 0.04428888412915693, 0.04160555628836245, 0.03847884935649202, 0.035035391033067444, 0.03140552154923875, 0.02771527549125696, 0.024079448635276616, 0.020596243874322948, 0.017343776224214638, 0.014378495509078854, 0.011735386013558698, 0.009429647572849292, 0.00745946520249525, 0.005809437340997196, 0.004454250117549496, 0.0033622443858905508, 0.002498607865497148],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1838827936985706616_q": {
            "type": "arbitrary",
            "samples": [-0.0003695605589822674, -0.0004717956221428235, -0.0005912423711011767, -0.0007270611135824583, -0.0008769852554266742, -0.0010370898049673126, -0.001201666763024415, -0.0013632526805548264, -0.0015128448912183113, -0.0016403262155469834, -0.0017350941471569743, -0.0017868620563049856, -0.0017865705661286497, -0.0017273216915621018, -0.0016052314777011063, -0.0014200928738405017, -0.0011757518852737413, -0.0008801267116935522, -0.0005448389595322115, -0.00018447297489786595, 0.00018447297489786595, 0.0005448389595322115, 0.0008801267116935522, 0.0011757518852737413, 0.0014200928738405017, 0.0016052314777011063, 0.0017273216915621018, 0.0017865705661286497, 0.0017868620563049856, 0.0017350941471569743, 0.0016403262155469834, 0.0015128448912183113, 0.0013632526805548264, 0.001201666763024415, 0.0010370898049673126, 0.0008769852554266742, 0.0007270611135824583, 0.0005912423711011767, 0.0004717956221428235, 0.0003695605589822674],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8147627902512691464_i": {
            "type": "arbitrary",
            "samples": [0.0038253569864246145, 0.0051475804704049655, 0.006819436151522863, 0.00889422146886499, 0.011420406427672425, 0.014436746446062975, 0.017966821242846084, 0.022013409550756303, 0.026553240493014975, 0.031532753293030236, 0.03686552353339383, 0.042431957489282836, 0.04808170698957818, 0.053639020236493286, 0.05891093886641134, 0.06369791259346033, 0.06780607500037267, 0.0710601564824555, 0.07331584798662809] + [0.07447040459550726] * 2 + [0.07331584798662809, 0.0710601564824555, 0.06780607500037267, 0.06369791259346033, 0.05891093886641134, 0.053639020236493286, 0.04808170698957818, 0.042431957489282836, 0.03686552353339383, 0.031532753293030236, 0.026553240493014975, 0.022013409550756303, 0.017966821242846084, 0.014436746446062975, 0.011420406427672425, 0.00889422146886499, 0.006819436151522863, 0.0051475804704049655, 0.0038253569864246145],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8147627902512691464_q": {
            "type": "arbitrary",
            "samples": [-0.0006491163395155792, -0.0008286875852991652, -0.0010384903755763684, -0.0012770498289981517, -0.0015403847758521574, -0.0018216011465163134, -0.0021106730996404057, -0.002394491425907305, -0.0026572433507158827, -0.0028811585077681175, -0.0030476140760775368, -0.0031385420576323674, -0.003138030068374668, -0.0030339621107847987, -0.0028195161944500773, -0.0024943286442093964, -0.002065154793707444, -0.001545902601126369, -0.0009569848904087076, -0.0003240184031949085, 0.0003240184031949085, 0.0009569848904087076, 0.001545902601126369, 0.002065154793707444, 0.0024943286442093964, 0.0028195161944500773, 0.0030339621107847987, 0.003138030068374668, 0.0031385420576323674, 0.0030476140760775368, 0.0028811585077681175, 0.0026572433507158827, 0.002394491425907305, 0.0021106730996404057, 0.0018216011465163134, 0.0015403847758521574, 0.0012770498289981517, 0.0010384903755763684, 0.0008286875852991652, 0.0006491163395155792],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5844962937684574577": {
            "type": "constant",
            "sample": -0.2388,
        },
        "-2171439423006611619_i": {
            "type": "constant",
            "sample": 0.0021,
        },
        "-2171439423006611619_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "-9209889246576681870_i": {
            "type": "constant",
            "sample": 0.0033,
        },
        "-9209889246576681870_q": {
            "type": "constant",
            "sample": 0.0,
        },
        "2775281142118477101": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "3158334417017949022": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2881140013601946808": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] + [0.0] * 15,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5356094105021115885": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 2 + [0.0] * 14,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2837757000790609713": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 3 + [0.0] * 13,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3543274633413023406": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 4 + [0.0] * 12,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1933862415173566618": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 5 + [0.0] * 11,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4816860636573095730": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 6 + [0.0] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5962528380614905517": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 7 + [0.0] * 9,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4814706563438036744": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 8 + [0.0] * 8,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2490148481351200291": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 9 + [0.0] * 7,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7012466251441203607": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 10 + [0.0] * 6,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7233960310639918855": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 11 + [0.0] * 5,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5199646779833111128": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 12 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7682806260243011324": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 13 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3096582756944989923": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 14 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7618900527034993239": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 15 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3560320198840986304": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-8630083858671391514": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 17 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4368014686970003261": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 18 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3396874041644627168": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 19 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3175379982445911920": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-6370565478293614932": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 21 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4752954903365077645": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 22 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6426265822510901898": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 23 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4255589522584019289": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "1903223853821725069": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 25 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-421334228265111384": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 26 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6041325606115827514": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4322477601023607180": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-2140333603912517742": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 29 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6195931586874954871": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 30 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "900245911176057913": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 31 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6693296967656013227": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "4086092049531988020": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3808897646115985806": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1456531977353691586": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 35 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6308356751260938843": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-6086862692062223595": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 37 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1965699712493857681": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 38 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8887501482383622795": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 39 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9108995541582338043": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "5742464195952075742": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 41 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7139988844124046710": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 42 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2617671074034043394": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 43 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8952808315732139189": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-1685284967898567116": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 45 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5051816313528829417": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 46 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6533554568530257078": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 47 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7681376385707125851": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "3098012631480875396": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 49 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3221973018586510584": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 50 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "897414936499674131": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 51 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1454950732262620089": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-28912821478479394": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 53 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2446041269940689683": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 54 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2168846866524687469": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 55 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5976018772767311120": {
            "type": "constant",
            "sample": 0.12562814070351758,
        },
        "-976190419906859584": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 57 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2830981486335764067": {
            "type": "arbitrary",
            "samples": [0.12562814070351758] * 58 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8395272519969193231": {
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
        "B2/drive_mixer_8c2": [{'intermediate_frequency': 63761228.0, 'lo_frequency': 5900000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/acquisition_mixer_e67": [{'intermediate_frequency': 330300527.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
        "B4/drive_mixer_2b1": [{'intermediate_frequency': 109615374.0, 'lo_frequency': 6700000000.0, 'correction': (1, 0, 0, 1)}],
        "B2/acquisition_mixer_73d": [{'intermediate_frequency': 10040944.0, 'lo_frequency': 7370000000.0, 'correction': (1, 0, 0, 1)}],
    },
}

