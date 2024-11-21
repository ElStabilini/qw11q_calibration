
# Single QUA script generated at 2024-11-21 09:07:31.684477
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    set_dc_offset("D1/flux", "single", 0.2205)
    set_dc_offset("D2/flux", "single", -0.421)
    set_dc_offset("D3/flux", "single", -0.2095)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "D1/acquisition")
    with for_(v1,0,(v1<3000),(v1+1)):
        with for_(v4,20,(v4<=99),(v4+1)):
            align()
            with if_((v4==20), unsafe=True):
                play("7096592949341909951", "D1/drive")
            with elif_((v4==21)):
                play("-115720503467340412", "D1/drive")
            with elif_((v4==22)):
                play("-1263542320644209185", "D1/drive")
            with elif_((v4==23)):
                play("5117489313559423934", "D1/drive")
            with elif_((v4==24)):
                play("-8709403317967044306", "D1/drive")
            with elif_((v4==25)):
                play("1155711426557672926", "D1/drive")
            with elif_((v4==26)):
                play("7536743060761306045", "D1/drive")
            with elif_((v4==27)):
                play("6388921243584437272", "D1/drive")
            with elif_((v4==28)):
                play("-1278433812937113097", "D1/drive")
            with elif_((v4==29)):
                play("4285857220696316067", "D1/drive")
            with elif_((v4==30)):
                play("8808174990786319383", "D1/drive")
            with elif_((v4==31)):
                play("1140819934264769014", "D1/drive")
            with elif_((v4==32)):
                play("6995355519178226904", "D1/drive")
            with elif_((v4==33)):
                play("4670797437091390451", "D1/drive")
            with elif_((v4==34)):
                play("9193115207181393767", "D1/drive")
            with elif_((v4==35)):
                play("-9032134807329442601", "D1/drive")
            with elif_((v4==36)):
                play("6219423770532406003", "D1/drive")
            with elif_((v4==37)):
                play("4185110239725598276", "D1/drive")
            with elif_((v4==38)):
                play("4018826075551204738", "D1/drive")
            with elif_((v4==39)):
                play("-1601165302299511392", "D1/drive")
            with elif_((v4==40)):
                play("6604363986927480387", "D1/drive")
            with elif_((v4==41)):
                play("8030401897711621082", "D1/drive")
            with elif_((v4==42)):
                play("-1755771283058638749", "D1/drive")
            with elif_((v4==43)):
                play("9023617734129362498", "D1/drive")
            with elif_((v4==44)):
                play("3477438533968125597", "D1/drive")
            with elif_((v4==45)):
                play("-4189916522553424772", "D1/drive")
            with elif_((v4==46)):
                play("5675198221971292460", "D1/drive")
            with elif_((v4==47)):
                play("5896692281170007708", "D1/drive")
            with elif_((v4==48)):
                play("-7538336034711494810", "D1/drive")
            with elif_((v4==49)):
                play("-2918484592528411434", "D1/drive")
            with elif_((v4==50)):
                play("1759314727475078776", "D1/drive")
            with elif_((v4==51)):
                play("-5119082287509612699", "D1/drive")
            with elif_((v4==52)):
                play("-4897588228310897451", "D1/drive")
            with elif_((v4==53)):
                play("-2533544376133337050", "D1/drive")
            with elif_((v4==54)):
                play("3030746657500092114", "D1/drive")
            with elif_((v4==55)):
                play("-4636608399021458255", "D1/drive")
            with elif_((v4==56)):
                play("-114290628931454939", "D1/drive")
            with elif_((v4==57)):
                play("107203430267260309", "D1/drive")
            with elif_((v4==58)):
                play("-7985027911179528293", "D1/drive")
            with elif_((v4==59)):
                play("-7763533851980813045", "D1/drive")
            with elif_((v4==60)):
                play("7316678876098476270", "D1/drive")
            with elif_((v4==61)):
                play("7538172935297191518", "D1/drive")
            with elif_((v4==62)):
                play("-7101399232169736447", "D1/drive")
            with elif_((v4==63)):
                play("-7378593635585738661", "D1/drive")
            with elif_((v4==64)):
                play("2985209571553696033", "D1/drive")
            with elif_((v4==65)):
                play("-3477601633382428889", "D1/drive")
            with elif_((v4==66)):
                play("-5829967302144723109", "D1/drive")
            with elif_((v4==67)):
                play("6609007170341003591", "D1/drive")
            with elif_((v4==68)):
                play("-3632207614141556246", "D1/drive")
            with elif_((v4==69)):
                play("-2078495740119386424", "D1/drive")
            with elif_((v4==70)):
                play("1601002202885208100", "D1/drive")
            with elif_((v4==71)):
                play("119263947883780439", "D1/drive")
            with elif_((v4==72)):
                play("7215441445934793223", "D1/drive")
            with elif_((v4==73)):
                play("4020255950087090211", "D1/drive")
            with elif_((v4==74)):
                play("-8474418866615923455", "D1/drive")
            with elif_((v4==75)):
                play("7550233452913711648", "D1/drive")
            with elif_((v4==76)):
                play("7771727512112426896", "D1/drive")
            with elif_((v4==77)):
                play("4405196166482164595", "D1/drive")
            with elif_((v4==78)):
                play("4626690225680879843", "D1/drive")
            with elif_((v4==79)):
                play("1775636094303868161", "D1/drive")
            with elif_((v4==80)):
                play("1154310326417174617", "D1/drive")
            with elif_((v4==81)):
                play("1375804385615889865", "D1/drive")
            with elif_((v4==82)):
                play("-6389084342998740564", "D1/drive")
            with elif_((v4==83)):
                play("3573564073619056728", "D1/drive")
            with elif_((v4==84)):
                play("-9018644415177036998", "D1/drive")
            with elif_((v4==85)):
                play("1760744602010964249", "D1/drive")
            with elif_((v4==86)):
                play("-5117652412973727226", "D1/drive")
            with elif_((v4==87)):
                play("5661736604214274021", "D1/drive")
            with elif_((v4==88)):
                play("4179998349212846360", "D1/drive")
            with elif_((v4==89)):
                play("-1366180850948390541", "D1/drive")
            with elif_((v4==90)):
                play("1108773240470778536", "D1/drive")
            with elif_((v4==91)):
                play("-4511218137379937594", "D1/drive")
            with elif_((v4==92)):
                play("-6835776219466774047", "D1/drive")
            with elif_((v4==93)):
                play("-2313458449376770731", "D1/drive")
            with elif_((v4==94)):
                play("-7762103977444927572", "D1/drive")
            with elif_((v4==95)):
                play("-3954932071202303921", "D1/drive")
            with elif_((v4==96)):
                play("8484042401283422779", "D1/drive")
            with elif_((v4==97)):
                play("-1757172383199137058", "D1/drive")
            with elif_((v4==98)):
                play("-7377163761049853188", "D1/drive")
            with elif_((v4==99)):
                play("-4902209669630684111", "D1/drive")
            with if_(((v4/4)<4)):
                wait(4, "D1/acquisition")
            with else_():
                wait((v4/4), "D1/acquisition")
            measure("411307349810644873", "D1/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
            r1 = declare_stream()
            save(v2, r1)
            r2 = declare_stream()
            save(v3, r2)
            wait(12500, )
    with stream_processing():
        r1.buffer(80).average().save("411307349810644873_D1|acquisition_I")
        r2.buffer(80).average().save("411307349810644873_D1|acquisition_Q")


config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "filter": {},
                },
                "7": {
                    "offset": -0.04,
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
        "con6": {
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
        "octave5": {
            "connectivity": "con6",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
                "2": {
                    "LO_frequency": 5100000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                },
            },
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7450000000.0,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
    },
    "elements": {
        "D1/flux": {
            "singleInput": {
                "port": ('con9', 3),
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
        "D3/flux": {
            "singleInput": {
                "port": ('con9', 5),
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
        "D5/flux": {
            "singleInput": {
                "port": ('con9', 7),
            },
            "intermediate_frequency": 0,
            "operations": {},
        },
        "D1/acquisition": {
            "RF_inputs": {
                "port": ('octave5', 1),
            },
            "RF_outputs": {
                "port": ('octave5', 1),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 1),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -312363546.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "411307349810644873": "411307349810644873_D1/acquisition",
            },
        },
        "D1/drive": {
            "RF_inputs": {
                "port": ('octave5', 2),
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con6', 3),
                    "delay": 57,
                    "buffer": 18,
                },
            },
            "intermediate_frequency": -141729925.0,
            "operations": {
                "6604363986927480387": "6604363986927480387",
                "7096592949341909951": "7096592949341909951",
                "-115720503467340412": "-115720503467340412",
                "-1263542320644209185": "-1263542320644209185",
                "5117489313559423934": "5117489313559423934",
                "-8709403317967044306": "-8709403317967044306",
                "1155711426557672926": "1155711426557672926",
                "7536743060761306045": "7536743060761306045",
                "6388921243584437272": "6388921243584437272",
                "-1278433812937113097": "-1278433812937113097",
                "4285857220696316067": "4285857220696316067",
                "8808174990786319383": "8808174990786319383",
                "1140819934264769014": "1140819934264769014",
                "6995355519178226904": "6995355519178226904",
                "4670797437091390451": "4670797437091390451",
                "9193115207181393767": "9193115207181393767",
                "-9032134807329442601": "-9032134807329442601",
                "6219423770532406003": "6219423770532406003",
                "4185110239725598276": "4185110239725598276",
                "4018826075551204738": "4018826075551204738",
                "-1601165302299511392": "-1601165302299511392",
                "8030401897711621082": "8030401897711621082",
                "-1755771283058638749": "-1755771283058638749",
                "9023617734129362498": "9023617734129362498",
                "3477438533968125597": "3477438533968125597",
                "-4189916522553424772": "-4189916522553424772",
                "5675198221971292460": "5675198221971292460",
                "5896692281170007708": "5896692281170007708",
                "-7538336034711494810": "-7538336034711494810",
                "-2918484592528411434": "-2918484592528411434",
                "1759314727475078776": "1759314727475078776",
                "-5119082287509612699": "-5119082287509612699",
                "-4897588228310897451": "-4897588228310897451",
                "-2533544376133337050": "-2533544376133337050",
                "3030746657500092114": "3030746657500092114",
                "-4636608399021458255": "-4636608399021458255",
                "-114290628931454939": "-114290628931454939",
                "107203430267260309": "107203430267260309",
                "-7985027911179528293": "-7985027911179528293",
                "-7763533851980813045": "-7763533851980813045",
                "7316678876098476270": "7316678876098476270",
                "7538172935297191518": "7538172935297191518",
                "-7101399232169736447": "-7101399232169736447",
                "-7378593635585738661": "-7378593635585738661",
                "2985209571553696033": "2985209571553696033",
                "-3477601633382428889": "-3477601633382428889",
                "-5829967302144723109": "-5829967302144723109",
                "6609007170341003591": "6609007170341003591",
                "-3632207614141556246": "-3632207614141556246",
                "-2078495740119386424": "-2078495740119386424",
                "1601002202885208100": "1601002202885208100",
                "119263947883780439": "119263947883780439",
                "7215441445934793223": "7215441445934793223",
                "4020255950087090211": "4020255950087090211",
                "-8474418866615923455": "-8474418866615923455",
                "7550233452913711648": "7550233452913711648",
                "7771727512112426896": "7771727512112426896",
                "4405196166482164595": "4405196166482164595",
                "4626690225680879843": "4626690225680879843",
                "1775636094303868161": "1775636094303868161",
                "1154310326417174617": "1154310326417174617",
                "1375804385615889865": "1375804385615889865",
                "-6389084342998740564": "-6389084342998740564",
                "3573564073619056728": "3573564073619056728",
                "-9018644415177036998": "-9018644415177036998",
                "1760744602010964249": "1760744602010964249",
                "-5117652412973727226": "-5117652412973727226",
                "5661736604214274021": "5661736604214274021",
                "4179998349212846360": "4179998349212846360",
                "-1366180850948390541": "-1366180850948390541",
                "1108773240470778536": "1108773240470778536",
                "-4511218137379937594": "-4511218137379937594",
                "-6835776219466774047": "-6835776219466774047",
                "-2313458449376770731": "-2313458449376770731",
                "-7762103977444927572": "-7762103977444927572",
                "-3954932071202303921": "-3954932071202303921",
                "8484042401283422779": "8484042401283422779",
                "-1757172383199137058": "-1757172383199137058",
                "-7377163761049853188": "-7377163761049853188",
                "-4902209669630684111": "-4902209669630684111",
            },
        },
    },
    "pulses": {
        "6604363986927480387": {
            "length": 40,
            "waveforms": {
                "I": "6604363986927480387_i",
                "Q": "6604363986927480387_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "411307349810644873_D1/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "6980102099601109786_i",
                "Q": "6980102099601109786_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
        },
        "7096592949341909951": {
            "length": 20,
            "waveforms": {
                "I": "7096592949341909951_i",
                "Q": "7096592949341909951_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-115720503467340412": {
            "length": 24,
            "waveforms": {
                "I": "-115720503467340412_i",
                "Q": "-115720503467340412_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1263542320644209185": {
            "length": 24,
            "waveforms": {
                "I": "-1263542320644209185_i",
                "Q": "-1263542320644209185_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5117489313559423934": {
            "length": 24,
            "waveforms": {
                "I": "5117489313559423934_i",
                "Q": "5117489313559423934_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8709403317967044306": {
            "length": 24,
            "waveforms": {
                "I": "-8709403317967044306_i",
                "Q": "-8709403317967044306_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1155711426557672926": {
            "length": 28,
            "waveforms": {
                "I": "1155711426557672926_i",
                "Q": "1155711426557672926_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7536743060761306045": {
            "length": 28,
            "waveforms": {
                "I": "7536743060761306045_i",
                "Q": "7536743060761306045_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6388921243584437272": {
            "length": 28,
            "waveforms": {
                "I": "6388921243584437272_i",
                "Q": "6388921243584437272_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1278433812937113097": {
            "length": 28,
            "waveforms": {
                "I": "-1278433812937113097_i",
                "Q": "-1278433812937113097_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4285857220696316067": {
            "length": 32,
            "waveforms": {
                "I": "4285857220696316067_i",
                "Q": "4285857220696316067_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8808174990786319383": {
            "length": 32,
            "waveforms": {
                "I": "8808174990786319383_i",
                "Q": "8808174990786319383_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1140819934264769014": {
            "length": 32,
            "waveforms": {
                "I": "1140819934264769014_i",
                "Q": "1140819934264769014_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6995355519178226904": {
            "length": 32,
            "waveforms": {
                "I": "6995355519178226904_i",
                "Q": "6995355519178226904_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4670797437091390451": {
            "length": 36,
            "waveforms": {
                "I": "4670797437091390451_i",
                "Q": "4670797437091390451_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9193115207181393767": {
            "length": 36,
            "waveforms": {
                "I": "9193115207181393767_i",
                "Q": "9193115207181393767_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9032134807329442601": {
            "length": 36,
            "waveforms": {
                "I": "-9032134807329442601_i",
                "Q": "-9032134807329442601_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6219423770532406003": {
            "length": 36,
            "waveforms": {
                "I": "6219423770532406003_i",
                "Q": "6219423770532406003_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4185110239725598276": {
            "length": 40,
            "waveforms": {
                "I": "4185110239725598276_i",
                "Q": "4185110239725598276_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4018826075551204738": {
            "length": 40,
            "waveforms": {
                "I": "4018826075551204738_i",
                "Q": "4018826075551204738_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1601165302299511392": {
            "length": 40,
            "waveforms": {
                "I": "-1601165302299511392_i",
                "Q": "-1601165302299511392_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8030401897711621082": {
            "length": 44,
            "waveforms": {
                "I": "8030401897711621082_i",
                "Q": "8030401897711621082_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1755771283058638749": {
            "length": 44,
            "waveforms": {
                "I": "-1755771283058638749_i",
                "Q": "-1755771283058638749_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9023617734129362498": {
            "length": 44,
            "waveforms": {
                "I": "9023617734129362498_i",
                "Q": "9023617734129362498_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3477438533968125597": {
            "length": 44,
            "waveforms": {
                "I": "3477438533968125597_i",
                "Q": "3477438533968125597_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4189916522553424772": {
            "length": 48,
            "waveforms": {
                "I": "-4189916522553424772_i",
                "Q": "-4189916522553424772_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5675198221971292460": {
            "length": 48,
            "waveforms": {
                "I": "5675198221971292460_i",
                "Q": "5675198221971292460_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5896692281170007708": {
            "length": 48,
            "waveforms": {
                "I": "5896692281170007708_i",
                "Q": "5896692281170007708_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7538336034711494810": {
            "length": 48,
            "waveforms": {
                "I": "-7538336034711494810_i",
                "Q": "-7538336034711494810_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2918484592528411434": {
            "length": 52,
            "waveforms": {
                "I": "-2918484592528411434_i",
                "Q": "-2918484592528411434_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1759314727475078776": {
            "length": 52,
            "waveforms": {
                "I": "1759314727475078776_i",
                "Q": "1759314727475078776_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5119082287509612699": {
            "length": 52,
            "waveforms": {
                "I": "-5119082287509612699_i",
                "Q": "-5119082287509612699_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4897588228310897451": {
            "length": 52,
            "waveforms": {
                "I": "-4897588228310897451_i",
                "Q": "-4897588228310897451_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2533544376133337050": {
            "length": 56,
            "waveforms": {
                "I": "-2533544376133337050_i",
                "Q": "-2533544376133337050_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3030746657500092114": {
            "length": 56,
            "waveforms": {
                "I": "3030746657500092114_i",
                "Q": "3030746657500092114_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4636608399021458255": {
            "length": 56,
            "waveforms": {
                "I": "-4636608399021458255_i",
                "Q": "-4636608399021458255_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-114290628931454939": {
            "length": 56,
            "waveforms": {
                "I": "-114290628931454939_i",
                "Q": "-114290628931454939_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "107203430267260309": {
            "length": 60,
            "waveforms": {
                "I": "107203430267260309_i",
                "Q": "107203430267260309_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7985027911179528293": {
            "length": 60,
            "waveforms": {
                "I": "-7985027911179528293_i",
                "Q": "-7985027911179528293_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7763533851980813045": {
            "length": 60,
            "waveforms": {
                "I": "-7763533851980813045_i",
                "Q": "-7763533851980813045_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7316678876098476270": {
            "length": 60,
            "waveforms": {
                "I": "7316678876098476270_i",
                "Q": "7316678876098476270_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7538172935297191518": {
            "length": 64,
            "waveforms": {
                "I": "7538172935297191518_i",
                "Q": "7538172935297191518_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7101399232169736447": {
            "length": 64,
            "waveforms": {
                "I": "-7101399232169736447_i",
                "Q": "-7101399232169736447_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7378593635585738661": {
            "length": 64,
            "waveforms": {
                "I": "-7378593635585738661_i",
                "Q": "-7378593635585738661_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2985209571553696033": {
            "length": 64,
            "waveforms": {
                "I": "2985209571553696033_i",
                "Q": "2985209571553696033_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3477601633382428889": {
            "length": 68,
            "waveforms": {
                "I": "-3477601633382428889_i",
                "Q": "-3477601633382428889_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5829967302144723109": {
            "length": 68,
            "waveforms": {
                "I": "-5829967302144723109_i",
                "Q": "-5829967302144723109_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6609007170341003591": {
            "length": 68,
            "waveforms": {
                "I": "6609007170341003591_i",
                "Q": "6609007170341003591_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3632207614141556246": {
            "length": 68,
            "waveforms": {
                "I": "-3632207614141556246_i",
                "Q": "-3632207614141556246_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2078495740119386424": {
            "length": 72,
            "waveforms": {
                "I": "-2078495740119386424_i",
                "Q": "-2078495740119386424_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1601002202885208100": {
            "length": 72,
            "waveforms": {
                "I": "1601002202885208100_i",
                "Q": "1601002202885208100_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "119263947883780439": {
            "length": 72,
            "waveforms": {
                "I": "119263947883780439_i",
                "Q": "119263947883780439_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7215441445934793223": {
            "length": 72,
            "waveforms": {
                "I": "7215441445934793223_i",
                "Q": "7215441445934793223_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4020255950087090211": {
            "length": 76,
            "waveforms": {
                "I": "4020255950087090211_i",
                "Q": "4020255950087090211_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8474418866615923455": {
            "length": 76,
            "waveforms": {
                "I": "-8474418866615923455_i",
                "Q": "-8474418866615923455_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7550233452913711648": {
            "length": 76,
            "waveforms": {
                "I": "7550233452913711648_i",
                "Q": "7550233452913711648_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7771727512112426896": {
            "length": 76,
            "waveforms": {
                "I": "7771727512112426896_i",
                "Q": "7771727512112426896_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4405196166482164595": {
            "length": 80,
            "waveforms": {
                "I": "4405196166482164595_i",
                "Q": "4405196166482164595_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4626690225680879843": {
            "length": 80,
            "waveforms": {
                "I": "4626690225680879843_i",
                "Q": "4626690225680879843_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1775636094303868161": {
            "length": 80,
            "waveforms": {
                "I": "1775636094303868161_i",
                "Q": "1775636094303868161_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1154310326417174617": {
            "length": 80,
            "waveforms": {
                "I": "1154310326417174617_i",
                "Q": "1154310326417174617_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1375804385615889865": {
            "length": 84,
            "waveforms": {
                "I": "1375804385615889865_i",
                "Q": "1375804385615889865_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6389084342998740564": {
            "length": 84,
            "waveforms": {
                "I": "-6389084342998740564_i",
                "Q": "-6389084342998740564_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3573564073619056728": {
            "length": 84,
            "waveforms": {
                "I": "3573564073619056728_i",
                "Q": "3573564073619056728_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9018644415177036998": {
            "length": 84,
            "waveforms": {
                "I": "-9018644415177036998_i",
                "Q": "-9018644415177036998_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1760744602010964249": {
            "length": 88,
            "waveforms": {
                "I": "1760744602010964249_i",
                "Q": "1760744602010964249_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5117652412973727226": {
            "length": 88,
            "waveforms": {
                "I": "-5117652412973727226_i",
                "Q": "-5117652412973727226_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5661736604214274021": {
            "length": 88,
            "waveforms": {
                "I": "5661736604214274021_i",
                "Q": "5661736604214274021_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4179998349212846360": {
            "length": 88,
            "waveforms": {
                "I": "4179998349212846360_i",
                "Q": "4179998349212846360_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1366180850948390541": {
            "length": 92,
            "waveforms": {
                "I": "-1366180850948390541_i",
                "Q": "-1366180850948390541_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1108773240470778536": {
            "length": 92,
            "waveforms": {
                "I": "1108773240470778536_i",
                "Q": "1108773240470778536_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4511218137379937594": {
            "length": 92,
            "waveforms": {
                "I": "-4511218137379937594_i",
                "Q": "-4511218137379937594_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6835776219466774047": {
            "length": 92,
            "waveforms": {
                "I": "-6835776219466774047_i",
                "Q": "-6835776219466774047_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2313458449376770731": {
            "length": 96,
            "waveforms": {
                "I": "-2313458449376770731_i",
                "Q": "-2313458449376770731_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7762103977444927572": {
            "length": 96,
            "waveforms": {
                "I": "-7762103977444927572_i",
                "Q": "-7762103977444927572_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3954932071202303921": {
            "length": 96,
            "waveforms": {
                "I": "-3954932071202303921_i",
                "Q": "-3954932071202303921_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8484042401283422779": {
            "length": 96,
            "waveforms": {
                "I": "8484042401283422779_i",
                "Q": "8484042401283422779_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1757172383199137058": {
            "length": 100,
            "waveforms": {
                "I": "-1757172383199137058_i",
                "Q": "-1757172383199137058_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7377163761049853188": {
            "length": 100,
            "waveforms": {
                "I": "-7377163761049853188_i",
                "Q": "-7377163761049853188_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4902209669630684111": {
            "length": 100,
            "waveforms": {
                "I": "-4902209669630684111_i",
                "Q": "-4902209669630684111_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6604363986927480387_i": {
            "samples": [0.0025633625185328877, 0.0034493812958619704, 0.004569687767802362, 0.005959996420132366, 0.007652786886817909, 0.009674029080352337, 0.01203952371361243, 0.014751132808722143, 0.01779326260710692, 0.021130022161159442, 0.02470349867658192, 0.028433552685933602, 0.032219436241259766, 0.03594337848545879, 0.0394760784830394, 0.042683818067257386, 0.04543668781805351, 0.04761723999475882, 0.04912877344789502] + [0.04990243905537378] * 2 + [0.04912877344789502, 0.04761723999475882, 0.04543668781805351, 0.042683818067257386, 0.0394760784830394, 0.03594337848545879, 0.032219436241259766, 0.028433552685933602, 0.02470349867658192, 0.021130022161159442, 0.01779326260710692, 0.014751132808722143, 0.01203952371361243, 0.009674029080352337, 0.007652786886817909, 0.005959996420132366, 0.004569687767802362, 0.0034493812958619704, 0.0025633625185328877],
            "type": "arbitrary",
        },
        "6604363986927480387_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "6980102099601109786_i": {
            "sample": 0.0015,
            "type": "constant",
        },
        "6980102099601109786_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7096592949341909951_i": {
            "samples": [0.0029793659380993043, 0.005228950064450073, 0.008621081194687642, 0.013352591761317168, 0.01942790637561821, 0.02655479955176726, 0.03409703755951741, 0.04112887811993324, 0.04660512461797638] + [0.04961089691301218] * 2 + [0.04660512461797638, 0.04112887811993324, 0.03409703755951741, 0.02655479955176726, 0.01942790637561821, 0.013352591761317168, 0.008621081194687642, 0.005228950064450073, 0.0029793659380993043],
            "type": "arbitrary",
        },
        "7096592949341909951_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
        },
        "-115720503467340412_i": {
            "samples": [0.0029374912044815276, 0.0050334449886448905, 0.008149560900092273, 0.012467610438864811, 0.01802238942989105, 0.024616236003660263, 0.031769549438440174, 0.03874187144416247, 0.04464062507811166, 0.04860266351433041, 0.05, 0.04860266351433041, 0.04464062507811166, 0.03874187144416247, 0.031769549438440174, 0.024616236003660263, 0.01802238942989105, 0.012467610438864811, 0.008149560900092273, 0.0050334449886448905, 0.0029374912044815276] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-115720503467340412_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "-1263542320644209185_i": {
            "samples": [0.0028998450454134615, 0.0048607183156681895, 0.007737373288764629, 0.011696450294316233, 0.016791211928589855, 0.022891668088580716, 0.029637411586921195, 0.036439342850399604, 0.04254693060275435, 0.04717733097628471] + [0.049678209377909864] * 2 + [0.04717733097628471, 0.04254693060275435, 0.036439342850399604, 0.029637411586921195, 0.022891668088580716, 0.016791211928589855, 0.011696450294316233, 0.007737373288764629, 0.0048607183156681895, 0.0028998450454134615] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1263542320644209185_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "5117489313559423934_i": {
            "samples": [0.002865820691614407, 0.0047071095929761666, 0.0073745460484814385, 0.011020263018688789, 0.015708123750690386, 0.02135661183854497, 0.027695938152648772, 0.03425906399134473, 0.04042132931542719, 0.0454905697855672, 0.048832375039166126, 0.05, 0.048832375039166126, 0.0454905697855672, 0.04042132931542719, 0.03425906399134473, 0.027695938152648772, 0.02135661183854497, 0.015708123750690386, 0.011020263018688789, 0.0073745460484814385, 0.0047071095929761666, 0.002865820691614407, 0.0],
            "type": "arbitrary",
        },
        "5117489313559423934_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "-8709403317967044306_i": {
            "samples": [0.002834921720190051, 0.0045696877678023645, 0.007053138240012856, 0.010423862595733963, 0.014751132808722145, 0.019988144541558575, 0.025934029627344382, 0.03221943624125977, 0.03832801119018458, 0.043658121514372, 0.04761723999475882] + [0.049729467169738945] * 2 + [0.04761723999475882, 0.043658121514372, 0.03832801119018458, 0.03221943624125977, 0.025934029627344382, 0.019988144541558575, 0.014751132808722145, 0.010423862595733963, 0.007053138240012856, 0.0045696877678023645, 0.002834921720190051],
            "type": "arbitrary",
        },
        "-8709403317967044306_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
        },
        "1155711426557672926_i": {
            "samples": [0.0028067381417066863, 0.004446080872969317, 0.0067667641618306355, 0.009894934954180734, 0.013901865022659707, 0.01876555494256998, 0.024337612797998585, 0.030326532985631673, 0.03630745185368455, 0.0417635105705636, 0.04615581731933179, 0.04900993366533776, 0.05, 0.04900993366533776, 0.04615581731933179, 0.0417635105705636, 0.03630745185368455, 0.030326532985631673, 0.024337612797998585, 0.01876555494256998, 0.013901865022659707, 0.009894934954180734, 0.0067667641618306355, 0.004446080872969317, 0.0028067381417066863] + [0.0] * 3,
            "type": "arbitrary",
        },
        "1155711426557672926_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "7536743060761306045_i": {
            "samples": [0.0027809284304838883, 0.004334350716624308, 0.006510241522248106, 0.009423429055037943, 0.013144971336512882, 0.017670512074329035, 0.022891668088580716, 0.028578837505011535, 0.03438353235519167, 0.03986531841436178, 0.04454293158439271, 0.04796242902846769] + [0.0497693943770712] * 2 + [0.04796242902846769, 0.04454293158439271, 0.03986531841436178, 0.03438353235519167, 0.028578837505011535, 0.022891668088580716, 0.017670512074329035, 0.013144971336512882, 0.009423429055037943, 0.006510241522248106, 0.004334350716624308, 0.0027809284304838883] + [0.0] * 2,
            "type": "arbitrary",
        },
        "7536743060761306045_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "6388921243584437272_i": {
            "samples": [0.0027572058474173962, 0.004232899431126499, 0.006279328577150272, 0.009001087153051165, 0.012467610438864815, 0.01668698902458154, 0.021581381200937142, 0.026970375361881335, 0.03256876158151036, 0.03800336023035619, 0.04284984457176395, 0.04668560624918924, 0.049149969646391525, 0.05, 0.049149969646391525, 0.04668560624918924, 0.04284984457176395, 0.03800336023035619, 0.03256876158151036, 0.026970375361881335, 0.021581381200937142, 0.01668698902458154, 0.012467610438864815, 0.009001087153051165, 0.006279328577150272, 0.004232899431126499, 0.0027572058474173962, 0.0],
            "type": "arbitrary",
        },
        "6388921243584437272_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "-1278433812937113097_i": {
            "samples": [0.002735327907539154, 0.00414039890922729, 0.0060705256497609345, 0.008621081194687644, 0.0118590116629278, 0.015801073051313504, 0.0203927591289532, 0.025492752061941737, 0.03086802040111313, 0.03620363343834905, 0.04112887811993324, 0.04525774296401605, 0.048238105580975396] + [0.04980109820219597] * 2 + [0.048238105580975396, 0.04525774296401605, 0.04112887811993324, 0.03620363343834905, 0.03086802040111313, 0.025492752061941737, 0.0203927591289532, 0.015801073051313504, 0.0118590116629278, 0.008621081194687644, 0.0060705256497609345, 0.00414039890922729, 0.002735327907539154],
            "type": "arbitrary",
        },
        "-1278433812937113097_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
        },
        "4285857220696316067_i": {
            "samples": [0.0027150881816862906, 0.004055736906838736, 0.005880923748526811, 0.008277730066572073, 0.01131011211301379, 0.015000733581042909, 0.019312923664813176, 0.02413645521624202, 0.02928120130671888, 0.03448214158408967, 0.03941753929454081, 0.0437395918177791, 0.047113989472523654, 0.04926233274822752, 0.05, 0.04926233274822752, 0.047113989472523654, 0.0437395918177791, 0.03941753929454081, 0.03448214158408967, 0.02928120130671888, 0.02413645521624202, 0.019312923664813176, 0.015000733581042909, 0.01131011211301379, 0.008277730066572073, 0.005880923748526811, 0.004055736906838736, 0.0027150881816862906] + [0.0] * 3,
            "type": "arbitrary",
        },
        "4285857220696316067_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "8808174990786319383_i": {
            "samples": [0.002696309851531143, 0.003977975435911384, 0.005708088000484348, 0.007966278536960766, 0.010813258341494367, 0.014275585681915955, 0.01833021485368369, 0.022891668088580716, 0.027805044188660435, 0.032847778482463424, 0.03774198009945037, 0.04217738245321173, 0.04584276778660145, 0.04846166172381721] + [0.04982668994851846] * 2 + [0.04846166172381721, 0.04584276778660145, 0.04217738245321173, 0.03774198009945037, 0.032847778482463424, 0.027805044188660435, 0.022891668088580716, 0.01833021485368369, 0.014275585681915955, 0.010813258341494367, 0.007966278536960766, 0.005708088000484348, 0.003977975435911384, 0.002696309851531143] + [0.0] * 2,
            "type": "arbitrary",
        },
        "8808174990786319383_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "1140819934264769014_i": {
            "samples": [0.0026788405963976483, 0.00390631832647667, 0.005549967079187939, 0.007682723433531037, 0.010361962318306845, 0.01361666755014075, 0.01743418606418866, 0.021748761738846677, 0.026434397179580627, 0.031304466235011576, 0.03611978959808223, 0.040605619167156784, 0.0444763438397427, 0.047465060364983394, 0.049353847252378576, 0.05, 0.049353847252378576, 0.047465060364983394, 0.0444763438397427, 0.040605619167156784, 0.03611978959808223, 0.031304466235011576, 0.026434397179580627, 0.021748761738846677, 0.01743418606418866, 0.01361666755014075, 0.010361962318306845, 0.007682723433531037, 0.005549967079187939, 0.00390631832647667, 0.0026788405963976483, 0.0],
            "type": "arbitrary",
        },
        "1140819934264769014_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "6995355519178226904_i": {
            "samples": [0.0026625485020862942, 0.003840085704057873, 0.005404822227200863, 0.007423676150889755, 0.00995070221065691, 0.013016240019842008, 0.016615540549723397, 0.020698577903878936, 0.02516307136256083, 0.029852719317876128, 0.034562190004558964, 0.03904952149711631, 0.04305536616140598, 0.04632719066581175, 0.04864539678371839] + [0.04984764470335167] * 2 + [0.04864539678371839, 0.04632719066581175, 0.04305536616140598, 0.03904952149711631, 0.034562190004558964, 0.029852719317876128, 0.02516307136256083, 0.020698577903878936, 0.016615540549723397, 0.013016240019842008, 0.00995070221065691, 0.007423676150889755, 0.005404822227200863, 0.003840085704057873, 0.0026625485020862942],
            "type": "arbitrary",
        },
        "6995355519178226904_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
        },
        "4670797437091390451_i": {
            "samples": [0.002647318761494564, 0.0037786937356530438, 0.0052711711835988885, 0.007186253242839668, 0.009574759750733157, 0.012467610438864815, 0.015866039563750777, 0.019732577286671354, 0.023984411272303417, 0.02849077633519044, 0.03307573278246874, 0.037527068197661065, 0.04161115483183768, 0.04509255793226413, 0.047756220139797384, 0.04942936025833958, 0.05, 0.04942936025833958, 0.047756220139797384, 0.04509255793226413, 0.04161115483183768, 0.037527068197661065, 0.03307573278246874, 0.02849077633519044, 0.023984411272303417, 0.019732577286671354, 0.015866039563750777, 0.012467610438864815, 0.009574759750733157, 0.007186253242839668, 0.0052711711835988885, 0.0037786937356530438, 0.002647318761494564] + [0.0] * 3,
            "type": "arbitrary",
        },
        "4670797437091390451_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "9193115207181393767_i": {
            "samples": [0.0026330509941431624, 0.00372163842775093, 0.00514774354755709, 0.006967988844909425, 0.009230087303692295, 0.011964980338316566, 0.015178399800876406, 0.018842902677797573, 0.022891668088580716, 0.027215410790795848, 0.03166359091122766, 0.03605066299559501, 0.04016744101475299, 0.043796851566868016, 0.04673254539564545, 0.048798199693554] + [0.049865018169666556] * 2 + [0.048798199693554, 0.04673254539564545, 0.043796851566868016, 0.04016744101475299, 0.03605066299559501, 0.03166359091122766, 0.027215410790795848, 0.022891668088580716, 0.018842902677797573, 0.015178399800876406, 0.011964980338316566, 0.009230087303692295, 0.006967988844909425, 0.00514774354755709, 0.00372163842775093, 0.0026330509941431624] + [0.0] * 2,
            "type": "arbitrary",
        },
        "9193115207181393767_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "-9032134807329442601_i": {
            "samples": [0.002619657053491279, 0.0036684825684191453, 0.005033444988644889, 0.0067667641618306355, 0.008913198979252397, 0.011503314949690454, 0.01454619035230741, 0.01802238942989105, 0.02187823688501346, 0.026022506051035107, 0.030326532985631673, 0.03462846621025988, 0.03874187144416247, 0.04246829082841563, 0.045612703841427266, 0.04800027206427389, 0.049492390168936695, 0.05, 0.049492390168936695, 0.04800027206427389, 0.045612703841427266, 0.04246829082841563, 0.03874187144416247, 0.03462846621025988, 0.030326532985631673, 0.026022506051035107, 0.02187823688501346, 0.01802238942989105, 0.01454619035230741, 0.011503314949690454, 0.008913198979252397, 0.0067667641618306355, 0.005033444988644889, 0.0036684825684191453, 0.002619657053491279, 0.0],
            "type": "arbitrary",
        },
        "-9032134807329442601_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "6219423770532406003_i": {
            "samples": [0.0026070592216907973, 0.003618845129261924, 0.004927328354199723, 0.006580750371340995, 0.008621081194687642, 0.011078232094900766, 0.013963734722897546, 0.017264544538571694, 0.020937800975694126, 0.024907458469635976, 0.029063650893670724, 0.03326544423074864, 0.0373472726742971, 0.04112887811993324, 0.044428048779768615, 0.04707496681601854, 0.048926619603661396] + [0.04987958196666021] * 2 + [0.048926619603661396, 0.04707496681601854, 0.044428048779768615, 0.04112887811993324, 0.0373472726742971, 0.03326544423074864, 0.029063650893670724, 0.024907458469635976, 0.020937800975694126, 0.017264544538571694, 0.013963734722897546, 0.011078232094900766, 0.008621081194687642, 0.006580750371340995, 0.004927328354199723, 0.003618845129261924, 0.0026070592216907973],
            "type": "arbitrary",
        },
        "6219423770532406003_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
        },
        "4185110239725598276_i": {
            "samples": [0.002595188714316214, 0.0035723926069823626, 0.004828570193672211, 0.00640836213600811, 0.008351118985510775, 0.01068590789442151, 0.013426020649958657, 0.016563508097770987, 0.02006441339444917, 0.023865456128386947, 0.02787289896516111, 0.03196418761612999, 0.03599269207614192, 0.03979551414757587, 0.04320390857559339, 0.04605545592934736, 0.04820679546798823, 0.04954554031808842, 0.05, 0.04954554031808842, 0.04820679546798823, 0.04605545592934736, 0.04320390857559339, 0.03979551414757587, 0.03599269207614192, 0.03196418761612999, 0.02787289896516111, 0.023865456128386947, 0.02006441339444917, 0.016563508097770987, 0.013426020649958657, 0.01068590789442151, 0.008351118985510775, 0.00640836213600811, 0.004828570193672211, 0.0035723926069823626, 0.002595188714316214] + [0.0] * 3,
            "type": "arbitrary",
        },
        "4185110239725598276_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "4018826075551204738_i": {
            "samples": [0.0025839844347918545, 0.0035288319055661616, 0.004736451567412025, 0.006248219549812199, 0.00810103508668073, 0.010322996882226687, 0.012928618797500867, 0.015914005940229233, 0.01925253636976, 0.022891668088580716, 0.026751490193092954, 0.030725543211001523, 0.03468424227854721, 0.03848096052466252, 0.04196049935090567, 0.044969332689644585, 0.04736671750996184, 0.04903556536550464] + [0.049891910630579066] * 2 + [0.04903556536550464, 0.04736671750996184, 0.044969332689644585, 0.04196049935090567, 0.03848096052466252, 0.03468424227854721, 0.030725543211001523, 0.026751490193092954, 0.022891668088580716, 0.01925253636976, 0.015914005940229233, 0.012928618797500867, 0.010322996882226687, 0.00810103508668073, 0.006248219549812199, 0.004736451567412025, 0.0035288319055661616, 0.0025839844347918545] + [0.0] * 2,
            "type": "arbitrary",
        },
        "4018826075551204738_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "-1601165302299511392_i": {
            "samples": [0.0025733919312547356, 0.0034879044506540796, 0.004650342266798705, 0.006099116828426824, 0.007868839394088365, 0.009986564358125815, 0.012467610438864815, 0.015311299002902122, 0.018497053221884698, 0.021981369650497184, 0.025696184865166883, 0.02954909888167482, 0.03342577839164012, 0.037194653106882324, 0.04071375797867211, 0.04383929521644875, 0.04643523325096258, 0.0483830669271807, 0.04959077001361501, 0.05, 0.04959077001361501, 0.0483830669271807, 0.04643523325096258, 0.04383929521644875, 0.04071375797867211, 0.037194653106882324, 0.03342577839164012, 0.02954909888167482, 0.025696184865166883, 0.021981369650497184, 0.018497053221884698, 0.015311299002902122, 0.012467610438864815, 0.009986564358125815, 0.007868839394088365, 0.006099116828426824, 0.004650342266798705, 0.0034879044506540796, 0.0025733919312547356, 0.0],
            "type": "arbitrary",
        },
        "-1601165302299511392_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
        },
        "8030401897711621082_i": {
            "samples": [0.0025538525355706942, 0.003413059032581848, 0.004493998388012063, 0.005829927496599249, 0.007451342466791033, 0.009383114668586039, 0.011641277780761964, 0.01422968905446275, 0.01713686189403215, 0.02033332079828439, 0.0237698508919818, 0.027376992143041297, 0.03106605696782864, 0.03473182997641245, 0.03825694859923382, 0.041517779458262974, 0.04439141992821902, 0.046763292912681415, 0.048534690269203956, 0.049629576452366694, 0.05, 0.049629576452366694, 0.048534690269203956, 0.046763292912681415, 0.04439141992821902, 0.041517779458262974, 0.03825694859923382, 0.03473182997641245, 0.03106605696782864, 0.027376992143041297, 0.0237698508919818, 0.02033332079828439, 0.01713686189403215, 0.01422968905446275, 0.011641277780761964, 0.009383114668586039, 0.007451342466791033, 0.005829927496599249, 0.004493998388012063, 0.003413059032581848, 0.0025538525355706942] + [0.0] * 3,
            "type": "arbitrary",
        },
        "8030401897711621082_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "-1755771283058638749_i": {
            "samples": [0.002544822714565668, 0.0033787563544115623, 0.004422840230134619, 0.005708088000484348, 0.007263151472393362, 0.009111808333139739, 0.011270134083719225, 0.013743540388445672, 0.016523924271883917, 0.019587220020940474, 0.022891668088580716, 0.02637710400819787, 0.029965519835388223, 0.03356306030992498, 0.037063491031181915, 0.04035302776569314, 0.04331626101013014, 0.04584276778660145, 0.04783389347182214, 0.04920912766202454] + [0.04991150131520572] * 2 + [0.04920912766202454, 0.04783389347182214, 0.04584276778660145, 0.04331626101013014, 0.04035302776569314, 0.037063491031181915, 0.03356306030992498, 0.029965519835388223, 0.02637710400819787, 0.022891668088580716, 0.019587220020940474, 0.016523924271883917, 0.013743540388445672, 0.011270134083719225, 0.009111808333139739, 0.007263151472393362, 0.005708088000484348, 0.004422840230134619, 0.0033787563544115623, 0.002544822714565668] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-1755771283058638749_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "9023617734129362498_i": {
            "samples": [0.0025362376427132847, 0.003346311157893433, 0.004355827581814801, 0.005593749595561242, 0.0070870148619200865, 0.008858325763205081, 0.01092365392653933, 0.013289608884202246, 0.015950872674240942, 0.01888794365518279, 0.022065455155220307, 0.02543133060094481, 0.02891700156978686, 0.0324388474295308, 0.035900917950228976, 0.039198881304570214, 0.04222501127025566, 0.04487390425974968, 0.04704851513012878, 0.048666035379217654, 0.04966311945686184, 0.05, 0.04966311945686184, 0.048666035379217654, 0.04704851513012878, 0.04487390425974968, 0.04222501127025566, 0.039198881304570214, 0.035900917950228976, 0.0324388474295308, 0.02891700156978686, 0.02543133060094481, 0.022065455155220307, 0.01888794365518279, 0.015950872674240942, 0.013289608884202246, 0.01092365392653933, 0.008858325763205081, 0.0070870148619200865, 0.005593749595561242, 0.004355827581814801, 0.003346311157893433, 0.0025362376427132847, 0.0],
            "type": "arbitrary",
        },
        "9023617734129362498_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "3477438533968125597_i": {
            "samples": [0.002528065301096756, 0.003315578084938566, 0.004292616508838816, 0.005486264996632666, 0.006921868253627256, 0.008621081194687642, 0.010599661595717305, 0.01286512835538612, 0.015414452552352569, 0.0182319846055169, 0.02128784229029823, 0.024536985213698223, 0.02791917730239037, 0.03135998820850191, 0.03477290893057051, 0.0380625617037418, 0.04112887811993324, 0.04387201394036187, 0.046197676919354946, 0.04802247752716405, 0.0492788818578542] + [0.049919357457577904] * 2 + [0.0492788818578542, 0.04802247752716405, 0.046197676919354946, 0.04387201394036187, 0.04112887811993324, 0.0380625617037418, 0.03477290893057051, 0.03135998820850191, 0.02791917730239037, 0.024536985213698223, 0.02128784229029823, 0.0182319846055169, 0.015414452552352569, 0.01286512835538612, 0.010599661595717305, 0.008621081194687642, 0.006921868253627256, 0.005486264996632666, 0.004292616508838816, 0.003315578084938566, 0.002528065301096756],
            "type": "arbitrary",
        },
        "3477438533968125597_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
        },
        "-4189916522553424772_i": {
            "samples": [0.0025202766681376824, 0.003286426430826524, 0.004232899431126499, 0.005385057259501606, 0.0067667641618306355, 0.008398661837876681, 0.010296212321709937, 0.012467610438864811, 0.014911704809071079, 0.017616097749774847, 0.020555614525359374, 0.023691336319768205, 0.026970375361881335, 0.030326532985631673, 0.03368192276723634, 0.03694956481401544, 0.040036870145840404, 0.04284984457176395, 0.045297759555475485, 0.04729797344533827, 0.0487805490032423, 0.049692308666322065, 0.05, 0.049692308666322065, 0.0487805490032423, 0.04729797344533827, 0.045297759555475485, 0.04284984457176395, 0.040036870145840404, 0.03694956481401544, 0.03368192276723634, 0.030326532985631673, 0.026970375361881335, 0.023691336319768205, 0.020555614525359374, 0.017616097749774847, 0.014911704809071079, 0.012467610438864811, 0.010296212321709937, 0.008398661837876681, 0.0067667641618306355, 0.005385057259501606, 0.004232899431126499, 0.003286426430826524, 0.0025202766681376824] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4189916522553424772_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "5675198221971292460_i": {
            "samples": [0.0025128453773136197, 0.0032587383562236866, 0.004176400511928773, 0.005289610692387379, 0.006620856890794367, 0.008189805979818993, 0.010011564444950933, 0.012094814247438324, 0.01443993970885866, 0.017037288538126784, 0.01986572863262788, 0.022891668088580716, 0.026068695758330287, 0.029337971899910803, 0.03262945308885559, 0.03586397493223743, 0.0389561448151963, 0.041817921443122526, 0.04436268616053358, 0.04650955119382207, 0.048187609703781206, 0.04933981775935761] + [0.04992621234479659] * 2 + [0.04933981775935761, 0.048187609703781206, 0.04650955119382207, 0.04436268616053358, 0.041817921443122526, 0.0389561448151963, 0.03586397493223743, 0.03262945308885559, 0.029337971899910803, 0.026068695758330287, 0.022891668088580716, 0.01986572863262788, 0.017037288538126784, 0.01443993970885866, 0.012094814247438324, 0.010011564444950933, 0.008189805979818993, 0.006620856890794367, 0.005289610692387379, 0.004176400511928773, 0.0032587383562236866, 0.0025128453773136197] + [0.0] * 2,
            "type": "arbitrary",
        },
        "5675198221971292460_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "5896692281170007708_i": {
            "samples": [0.002505747420680767, 0.003232407353173493, 0.004122871722965482, 0.005199463114343012, 0.006483389646379692, 0.007993384189019955, 0.009744155223568687, 0.011744719328074062, 0.01399671224223789, 0.01649279906832163, 0.019215321022246976, 0.022135322986878217, 0.025212100217203166, 0.028393382212441223, 0.031616236750950315, 0.03480872884620627, 0.03789231118721658, 0.040784859363710665, 0.04340420294214317, 0.04567194891451151, 0.047517353620476, 0.04888097830587432, 0.04971786555152947, 0.05, 0.04971786555152947, 0.04888097830587432, 0.047517353620476, 0.04567194891451151, 0.04340420294214317, 0.040784859363710665, 0.03789231118721658, 0.03480872884620627, 0.031616236750950315, 0.028393382212441223, 0.025212100217203166, 0.022135322986878217, 0.019215321022246976, 0.01649279906832163, 0.01399671224223789, 0.011744719328074062, 0.009744155223568687, 0.007993384189019955, 0.006483389646379692, 0.005199463114343012, 0.004122871722965482, 0.003232407353173493, 0.002505747420680767, 0.0],
            "type": "arbitrary",
        },
        "5896692281170007708_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "-7538336034711494810_i": {
            "samples": [0.0024989608912136954, 0.0032073369241662993, 0.004072089473848755, 0.005114199237242183, 0.006353683504536693, 0.007808383144148403, 0.009492579789532414, 0.011415501634023637, 0.013579799196179876, 0.015980092869922236, 0.018601709296872628, 0.021419730900866366, 0.02439848000030468, 0.02749154421167759, 0.030642422915499373, 0.03378583624377857, 0.03684969066555055, 0.03975764244109334, 0.0424321467043333, 0.044797831049628416, 0.04678499360112465, 0.048333001358751716, 0.04939335861570002] + [0.049932229130174324] * 2 + [0.04939335861570002, 0.048333001358751716, 0.04678499360112465, 0.044797831049628416, 0.0424321467043333, 0.03975764244109334, 0.03684969066555055, 0.03378583624377857, 0.030642422915499373, 0.02749154421167759, 0.02439848000030468, 0.021419730900866366, 0.018601709296872628, 0.015980092869922236, 0.013579799196179876, 0.011415501634023637, 0.009492579789532414, 0.007808383144148403, 0.006353683504536693, 0.005114199237242183, 0.004072089473848755, 0.0032073369241662993, 0.0024989608912136954],
            "type": "arbitrary",
        },
        "-7538336034711494810_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
        },
        "-2918484592528411434_i": {
            "samples": [0.0024924657581652256, 0.003183439440717145, 0.0040238517145384095, 0.005033444988644893, 0.006231127939626965, 0.007633891686687384, 0.009255572824076668, 0.011105512215226277, 0.01318717803150054, 0.015496839242815317, 0.018022389429891057, 0.020742428174248848, 0.023625706442813293, 0.026631031924742005, 0.0297077096292436, 0.032796562677026964, 0.035831539713412984, 0.03874187144416247, 0.0414546930816414, 0.0438980062341342, 0.046003817393241046, 0.047711264761893184, 0.04896953397043469, 0.04974036822432454, 0.05, 0.04974036822432454, 0.04896953397043469, 0.047711264761893184, 0.046003817393241046, 0.0438980062341342, 0.0414546930816414, 0.03874187144416247, 0.035831539713412984, 0.032796562677026964, 0.0297077096292436, 0.026631031924742005, 0.023625706442813293, 0.020742428174248848, 0.018022389429891057, 0.015496839242815317, 0.01318717803150054, 0.011105512215226277, 0.009255572824076668, 0.007633891686687384, 0.006231127939626965, 0.005033444988644893, 0.0040238517145384095, 0.003183439440717145, 0.0024924657581652256] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2918484592528411434_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "1759314727475078776_i": {
            "samples": [0.0024862436706174803, 0.0031606351537644428, 0.003977975435911384, 0.0049568626255373695, 0.006115172667345031, 0.007469088762520901, 0.0090319925809447, 0.010813258341494367, 0.01281700757075368, 0.015040897717863778, 0.017475030009987826, 0.020101069154732743, 0.022891668088580716, 0.025810283697274818, 0.028811453683589994, 0.03184158071858716, 0.03484023877480174, 0.03774198009945037, 0.04047858243339435, 0.04298163818012712, 0.0451853538936598, 0.047029403168217104, 0.04846166172381721, 0.049440652230561655] + [0.04993753904622905] * 2 + [0.049440652230561655, 0.04846166172381721, 0.047029403168217104, 0.0451853538936598, 0.04298163818012712, 0.04047858243339435, 0.03774198009945037, 0.03484023877480174, 0.03184158071858716, 0.028811453683589994, 0.025810283697274818, 0.022891668088580716, 0.020101069154732743, 0.017475030009987826, 0.015040897717863778, 0.01281700757075368, 0.010813258341494367, 0.0090319925809447, 0.007469088762520901, 0.006115172667345031, 0.0049568626255373695, 0.003977975435911384, 0.0031606351537644428, 0.0024862436706174803] + [0.0] * 2,
            "type": "arbitrary",
        },
        "1759314727475078776_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "-5119082287509612699_i": {
            "samples": [0.002480277785184948, 0.003138851332956246, 0.003934294506670615, 0.004884146515280716, 0.006005320599092863, 0.00731323297148999, 0.008820806937035332, 0.010537386790920361, 0.012467610438864815, 0.01461030300988035, 0.016957464604601662, 0.019493432224073286, 0.02219429747269594, 0.025027656738345366, 0.027952758610452468, 0.030921094311865033, 0.0338774516165966, 0.03676142256396496, 0.03950932239356749, 0.04205644416788042, 0.044339543459319584, 0.04629942319064234, 0.04788347284235835, 0.049048010758336626, 0.04976028428422183, 0.05, 0.04976028428422183, 0.049048010758336626, 0.04788347284235835, 0.04629942319064234, 0.044339543459319584, 0.04205644416788042, 0.03950932239356749, 0.03676142256396496, 0.0338774516165966, 0.030921094311865033, 0.027952758610452468, 0.025027656738345366, 0.02219429747269594, 0.019493432224073286, 0.016957464604601662, 0.01461030300988035, 0.012467610438864815, 0.010537386790920361, 0.008820806937035332, 0.00731323297148999, 0.006005320599092863, 0.004884146515280716, 0.003934294506670615, 0.003138851332956246, 0.002480277785184948, 0.0],
            "type": "arbitrary",
        },
        "-5119082287509612699_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "-4897588228310897451_i": {
            "samples": [0.0024745526144779677, 0.0031180215157491573, 0.0038926577954437624, 0.0048150194814180584, 0.005901121738979186, 0.007165653488865205, 0.008621081194687642, 0.01027666905775511, 0.012137457162314097, 0.01420325069309823, 0.016467683004473817, 0.01891742181236899, 0.021531589940250125, 0.024281468931423338, 0.0271305448545296, 0.030034940671922673, 0.03294425907324257, 0.03580283475869078, 0.03855136741231789, 0.04112887811993324, 0.04347490513629988, 0.04553183214190747, 0.047247225724038715, 0.048576050616129796, 0.049482632431129325] + [0.04994224861461563] * 2 + [0.049482632431129325, 0.048576050616129796, 0.047247225724038715, 0.04553183214190747, 0.04347490513629988, 0.04112887811993324, 0.03855136741231789, 0.03580283475869078, 0.03294425907324257, 0.030034940671922673, 0.0271305448545296, 0.024281468931423338, 0.021531589940250125, 0.01891742181236899, 0.016467683004473817, 0.01420325069309823, 0.012137457162314097, 0.01027666905775511, 0.008621081194687642, 0.007165653488865205, 0.005901121738979186, 0.0048150194814180584, 0.0038926577954437624, 0.0031180215157491573, 0.0024745526144779677],
            "type": "arbitrary",
        },
        "-4897588228310897451_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
        },
        "-2533544376133337050_i": {
            "samples": [0.002469053893468293, 0.0030980848503909817, 0.0038529275355500612, 0.004749229629311066, 0.005802167882686558, 0.007025742160038183, 0.008431967398583791, 0.010029988257169727, 0.011825151813009735, 0.013818083730990761, 0.016003821895914795, 0.018371067533487658, 0.020901616369087942, 0.023570030562486313, 0.026343605463193056, 0.02918267348098945, 0.032041270834799136, 0.034868172390365236, 0.03760827645372948, 0.04020429688601301, 0.04259869615963446, 0.0447357720176497, 0.04656379418017178, 0.04803707773957508, 0.04911787770764392, 0.049777995215018286, 0.05, 0.049777995215018286, 0.04911787770764392, 0.04803707773957508, 0.04656379418017178, 0.0447357720176497, 0.04259869615963446, 0.04020429688601301, 0.03760827645372948, 0.034868172390365236, 0.032041270834799136, 0.02918267348098945, 0.026343605463193056, 0.023570030562486313, 0.020901616369087942, 0.018371067533487658, 0.016003821895914795, 0.013818083730990761, 0.011825151813009735, 0.010029988257169727, 0.008431967398583791, 0.007025742160038183, 0.005802167882686558, 0.004749229629311066, 0.0038529275355500612, 0.0030980848503909817, 0.002469053893468293] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2533544376133337050_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "3030746657500092114_i": {
            "samples": [0.0024637684613389565, 0.0030789855194342714, 0.003814977896949741, 0.004686547580708139, 0.0057080880004843505, 0.006892946600839856, 0.008252694963685723, 0.009796327527285029, 0.011529419074498436, 0.013453279924025428, 0.015564155347705725, 0.01785252129982155, 0.02030253125392538, 0.022891668088580716, 0.02559065004276659, 0.028363630563060033, 0.03116871853280928, 0.03395882844516559, 0.03668285048442406, 0.039287109487906785, 0.04171706090895607, 0.04391915286411141, 0.04584276778660145, 0.04744214661345651, 0.04867819396531215, 0.04952006513485812] + [0.04994644502558085] * 2 + [0.04952006513485812, 0.04867819396531215, 0.04744214661345651, 0.04584276778660145, 0.04391915286411141, 0.04171706090895607, 0.039287109487906785, 0.03668285048442406, 0.03395882844516559, 0.03116871853280928, 0.028363630563060033, 0.02559065004276659, 0.022891668088580716, 0.02030253125392538, 0.01785252129982155, 0.015564155347705725, 0.013453279924025428, 0.011529419074498436, 0.009796327527285029, 0.008252694963685723, 0.006892946600839856, 0.0057080880004843505, 0.004686547580708139, 0.003814977896949741, 0.0030789855194342714, 0.0024637684613389565] + [0.0] * 2,
            "type": "arbitrary",
        },
        "3030746657500092114_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "-4636608399021458255_i": {
            "samples": [0.0024586841567666735, 0.0030606722325465796, 0.0037786937356530403, 0.0046267640579210996, 0.005618544205628365, 0.0067667641618306355, 0.008082562439363497, 0.009574759750733151, 0.011249092606956727, 0.013107440292288157, 0.015147085381610621, 0.017360053061381487, 0.019732577286671354, 0.022244741643582158, 0.024870339233461276, 0.027576988724858215, 0.030326532985631673, 0.03307573278246873, 0.03577725161283505, 0.03838090980604428, 0.0408351678230042, 0.043088781570857826, 0.04509255793226413, 0.04680112789477074, 0.0481746487324534, 0.049180346376956396, 0.049793814725774925, 0.05, 0.049793814725774925, 0.049180346376956396, 0.0481746487324534, 0.04680112789477074, 0.04509255793226413, 0.043088781570857826, 0.0408351678230042, 0.03838090980604428, 0.03577725161283505, 0.03307573278246873, 0.030326532985631673, 0.027576988724858215, 0.024870339233461276, 0.022244741643582158, 0.019732577286671354, 0.017360053061381487, 0.015147085381610621, 0.013107440292288157, 0.011249092606956727, 0.009574759750733151, 0.008082562439363497, 0.0067667641618306355, 0.005618544205628365, 0.0046267640579210996, 0.0037786937356530403, 0.0030606722325465796, 0.0024586841567666735, 0.0],
            "type": "arbitrary",
        },
        "-4636608399021458255_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "-114290628931454939_i": {
            "samples": [0.0024537897248895976, 0.0030430977791321644, 0.00374396949560364, 0.0045696877678023645, 0.00553322822504619, 0.006646736636571679, 0.00792093025951564, 0.009364438438319222, 0.010983104590816887, 0.012779278378754054, 0.014751132808722145, 0.01689204565136944, 0.01919008731470583, 0.021627657634343687, 0.024181311542401607, 0.026821808016929113, 0.02951440808865742, 0.03221943624125977, 0.034893105801257755, 0.03748859364207801, 0.039957333701476555, 0.042250483553692236, 0.044320504763776566, 0.04612278711236404, 0.04761723999475882, 0.04876977209991802, 0.04955358326495435] + [0.049950200199334105] * 2 + [0.04955358326495435, 0.04876977209991802, 0.04761723999475882, 0.04612278711236404, 0.044320504763776566, 0.042250483553692236, 0.039957333701476555, 0.03748859364207801, 0.034893105801257755, 0.03221943624125977, 0.02951440808865742, 0.026821808016929113, 0.024181311542401607, 0.021627657634343687, 0.01919008731470583, 0.01689204565136944, 0.014751132808722145, 0.012779278378754054, 0.010983104590816887, 0.009364438438319222, 0.00792093025951564, 0.006646736636571679, 0.00553322822504619, 0.0045696877678023645, 0.00374396949560364, 0.0030430977791321644, 0.0024537897248895976],
            "type": "arbitrary",
        },
        "-114290628931454939_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
        },
        "107203430267260309_i": {
            "samples": [0.002449074734468069, 0.003026218632729593, 0.0037107082419621826, 0.00451514354356592, 0.00545185830217733, 0.0065324456120135314, 0.0077672143495752495, 0.009164589635859368, 0.010730476335068845, 0.012467610438864811, 0.014374928450381512, 0.016446989096126696, 0.01867348436054603, 0.021038877504485697, 0.023522204033027672, 0.026097067295826448, 0.02873185348777371, 0.031390181430008074, 0.034031591030898804, 0.03661246134614739, 0.03908713545344811, 0.04140921584263013, 0.0435329816781146, 0.045414869087599175, 0.04701494844438925, 0.048298329138143484, 0.049236423018361175, 0.04980800269394257, 0.05, 0.04980800269394257, 0.049236423018361175, 0.048298329138143484, 0.04701494844438925, 0.045414869087599175, 0.0435329816781146, 0.04140921584263013, 0.03908713545344811, 0.03661246134614739, 0.034031591030898804, 0.031390181430008074, 0.02873185348777371, 0.026097067295826448, 0.023522204033027672, 0.021038877504485697, 0.01867348436054603, 0.016446989096126696, 0.014374928450381512, 0.012467610438864811, 0.010730476335068845, 0.009164589635859368, 0.0077672143495752495, 0.0065324456120135314, 0.00545185830217733, 0.00451514354356592, 0.0037107082419621826, 0.003026218632729593, 0.002449074734468069] + [0.0] * 3,
            "type": "arbitrary",
        },
        "107203430267260309_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "-7985027911179528293_i": {
            "samples": [0.002444529503959828, 0.0030099946003556487, 0.003678820807955497, 0.004462970708996382, 0.005374176472612954, 0.006423508374335231, 0.007620880479333864, 0.008974504731932459, 0.010490309843998432, 0.012171346469777309, 0.01401720481627395, 0.016023474652747317, 0.018181280231104057, 0.020476923521937335, 0.02289166808858072, 0.02540169265110044, 0.02797823786233076, 0.030587962124624377, 0.03319351269519628, 0.03575430731481765, 0.03822750976446968, 0.04056917084761368, 0.04273549512668324, 0.044684184138528184, 0.04637579954635434, 0.0477750854025085, 0.04885218785845216, 0.049583713491734606] + [0.04995357388586044] * 2 + [0.049583713491734606, 0.04885218785845216, 0.0477750854025085, 0.04637579954635434, 0.044684184138528184, 0.04273549512668324, 0.04056917084761368, 0.03822750976446968, 0.03575430731481765, 0.03319351269519628, 0.030587962124624377, 0.02797823786233076, 0.02540169265110044, 0.02289166808858072, 0.020476923521937335, 0.018181280231104057, 0.016023474652747317, 0.01401720481627395, 0.012171346469777309, 0.010490309843998432, 0.008974504731932459, 0.007620880479333864, 0.006423508374335231, 0.005374176472612954, 0.004462970708996382, 0.003678820807955497, 0.0030099946003556487, 0.002444529503959828] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7985027911179528293_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "-7763533851980813045_i": {
            "samples": [0.0024401450354109566, 0.002994388510972589, 0.0036482250401508065, 0.004413021634991416, 0.005299946162158934, 0.006319574296332377, 0.0074814392659343365, 0.008793534059145854, 0.01026178024453872, 0.011889482025838508, 0.013676788279067962, 0.015620188765761498, 0.017712073123370822, 0.019940382269409286, 0.02228838123747092, 0.02473457999293026, 0.02725282436825054, 0.029812572961748746, 0.03237936785702951, 0.03491549769066371, 0.037380841408871684, 0.03973387060876707, 0.0419327783299803, 0.04393669324900831, 0.045706931104567, 0.047208230436611834, 0.048409917806535155, 0.04928694885197926, 0.04982077587508655, 0.05, 0.04982077587508655, 0.04928694885197926, 0.048409917806535155, 0.047208230436611834, 0.045706931104567, 0.04393669324900831, 0.0419327783299803, 0.03973387060876707, 0.037380841408871684, 0.03491549769066371, 0.03237936785702951, 0.029812572961748746, 0.02725282436825054, 0.02473457999293026, 0.02228838123747092, 0.019940382269409286, 0.017712073123370822, 0.015620188765761498, 0.013676788279067962, 0.011889482025838508, 0.01026178024453872, 0.008793534059145854, 0.0074814392659343365, 0.006319574296332377, 0.005299946162158934, 0.004413021634991416, 0.0036482250401508065, 0.002994388510972589, 0.0024401450354109566, 0.0],
            "type": "arbitrary",
        },
        "-7763533851980813045_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "7316678876098476270_i": {
            "samples": [0.002435912955215962, 0.0029793659380993043, 0.003618845129261924, 0.004365160462885511, 0.005228950064450073, 0.006220321643198391, 0.007348441744565965, 0.008621081194687642, 0.010044128984978123, 0.011621090763833554, 0.013352591761317168, 0.015235907079823315, 0.017264544538571694, 0.01942790637561821, 0.021711055840484977, 0.024094612871482846, 0.02655479955176726, 0.029063650893670724, 0.031589399850201996, 0.03409703755951741, 0.03654904107496654, 0.038906251703063124, 0.04112887811993324, 0.043177590254165926, 0.04501466309304222, 0.04660512461797638, 0.047917859432597715, 0.048926619603661396, 0.04961089691301218] + [0.049956616054783784] * 2 + [0.04961089691301218, 0.048926619603661396, 0.047917859432597715, 0.04660512461797638, 0.04501466309304222, 0.043177590254165926, 0.04112887811993324, 0.038906251703063124, 0.03654904107496654, 0.03409703755951741, 0.031589399850201996, 0.029063650893670724, 0.02655479955176726, 0.024094612871482846, 0.021711055840484977, 0.01942790637561821, 0.017264544538571694, 0.015235907079823315, 0.013352591761317168, 0.011621090763833554, 0.010044128984978123, 0.008621081194687642, 0.007348441744565965, 0.006220321643198391, 0.005228950064450073, 0.004365160462885511, 0.003618845129261924, 0.0029793659380993043, 0.002435912955215962],
            "type": "arbitrary",
        },
        "7316678876098476270_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
        },
        "7538172935297191518_i": {
            "samples": [0.002431825460928962, 0.002964894952295667, 0.003590611015475533, 0.004319261972767974, 0.005160988261532103, 0.006125454742606967, 0.007221475435667583, 0.00845659787755376, 0.009836657724136656, 0.011365317661131394, 0.013043607933790552, 0.01486948860420408, 0.016837455742893862, 0.01893821491227217, 0.021158445286670047, 0.02348067641138794, 0.025883296837165577, 0.028340709670415954, 0.03082364454728654, 0.03329962886960136, 0.03573361363275896, 0.038088741218395256, 0.04032723457465495, 0.04241137976010234, 0.04430456738436634, 0.04597235350761083, 0.047383497459668834, 0.04851093310148842, 0.04933263143749993, 0.04983231620813549, 0.05, 0.04983231620813549, 0.04933263143749993, 0.04851093310148842, 0.047383497459668834, 0.04597235350761083, 0.04430456738436634, 0.04241137976010234, 0.04032723457465495, 0.038088741218395256, 0.03573361363275896, 0.03329962886960136, 0.03082364454728654, 0.028340709670415954, 0.025883296837165577, 0.02348067641138794, 0.021158445286670047, 0.01893821491227217, 0.016837455742893862, 0.01486948860420408, 0.013043607933790552, 0.011365317661131394, 0.009836657724136656, 0.00845659787755376, 0.007221475435667583, 0.006125454742606967, 0.005160988261532103, 0.004319261972767974, 0.003590611015475533, 0.002964894952295667, 0.002431825460928962] + [0.0] * 3,
            "type": "arbitrary",
        },
        "7538172935297191518_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "-7101399232169736447_i": {
            "samples": [0.0024278752734174583, 0.00295094589984705, 0.0035634578588658616, 0.00427521057816669, 0.0050958765561137116, 0.006034701472665832, 0.007100160847091294, 0.008299579470046963, 0.009638722838079402, 0.011121372851145478, 0.012748902913080404, 0.014519870093967808, 0.016429643955280793, 0.018470092791889704, 0.0206293482201413, 0.022891668088580716, 0.025237415514640274, 0.027643168435256577, 0.030081969462450522, 0.032523720204316243, 0.03493571778167314, 0.0372833243527405, 0.0395307534268863, 0.04164195001851245, 0.04358153569152915, 0.045315784684656586, 0.04681359395070428, 0.04804740837396265, 0.04899406283097626, 0.04963550519216617] + [0.049959368755182615] * 2 + [0.04963550519216617, 0.04899406283097626, 0.04804740837396265, 0.04681359395070428, 0.045315784684656586, 0.04358153569152915, 0.04164195001851245, 0.0395307534268863, 0.0372833243527405, 0.03493571778167314, 0.032523720204316243, 0.030081969462450522, 0.027643168435256577, 0.025237415514640274, 0.022891668088580716, 0.0206293482201413, 0.018470092791889704, 0.016429643955280793, 0.014519870093967808, 0.012748902913080404, 0.011121372851145478, 0.009638722838079402, 0.008299579470046963, 0.007100160847091294, 0.006034701472665832, 0.0050958765561137116, 0.00427521057816669, 0.0035634578588658616, 0.00295094589984705, 0.0024278752734174583] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7101399232169736447_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "-7378593635585738661_i": {
            "samples": [0.0024240555937433345, 0.0029374912044815306, 0.0035373255667968647, 0.004232899431126501, 0.005033444988644893, 0.00594781102780247, 0.006984148357941575, 0.008149560900092277, 0.009449730478863508, 0.010888526022913963, 0.012467610438864817, 0.014186060689585282, 0.016040018397985235, 0.018022389429891057, 0.020122611218834442, 0.022326505947265, 0.024616236003660266, 0.02697037536188134, 0.029364106713896294, 0.031769549438440174, 0.0341562179881798, 0.036491604276097406, 0.03874187144416247, 0.040872640349731676, 0.04284984457176395, 0.04464062507811166, 0.046214232233282214, 0.04754290083264267, 0.04860266351433041, 0.049374069317750915, 0.049842777313575226, 0.05, 0.049842777313575226, 0.049374069317750915, 0.04860266351433041, 0.04754290083264267, 0.046214232233282214, 0.04464062507811166, 0.04284984457176395, 0.040872640349731676, 0.03874187144416247, 0.036491604276097406, 0.0341562179881798, 0.031769549438440174, 0.029364106713896294, 0.02697037536188134, 0.024616236003660266, 0.022326505947265, 0.020122611218834442, 0.018022389429891057, 0.016040018397985235, 0.014186060689585282, 0.012467610438864817, 0.010888526022913963, 0.009449730478863508, 0.008149560900092277, 0.006984148357941575, 0.00594781102780247, 0.005033444988644893, 0.004232899431126501, 0.0035373255667968647, 0.0029374912044815306, 0.0024240555937433345, 0.0],
            "type": "arbitrary",
        },
        "-7378593635585738661_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "2985209571553696033_i": {
            "samples": [0.0024203600642353114, 0.0029245051893809332, 0.003512158371335674, 0.00419222962395352, 0.0049735365161414635, 0.005864551928152404, 0.006873115437888062, 0.008006113028742408, 0.00926913212665601, 0.010666101334644774, 0.012198926506533684, 0.013867136839583492, 0.015667556310793418, 0.017594016877396354, 0.01963713026408038, 0.02178413474760476, 0.024018832039639535, 0.026321627123554223, 0.028669680738527593, 0.03103718020337501, 0.033395729573420456, 0.03571485492571769, 0.03796261512062647, 0.04010630297872012, 0.04211321674999914, 0.043951477347772244, 0.04559086336308615, 0.047003633617155295, 0.04816530613845629, 0.049055363081174, 0.0496578532580101] + [0.04996186757555894] * 2 + [0.0496578532580101, 0.049055363081174, 0.04816530613845629, 0.047003633617155295, 0.04559086336308615, 0.043951477347772244, 0.04211321674999914, 0.04010630297872012, 0.03796261512062647, 0.03571485492571769, 0.033395729573420456, 0.03103718020337501, 0.028669680738527593, 0.026321627123554223, 0.024018832039639535, 0.02178413474760476, 0.01963713026408038, 0.017594016877396354, 0.015667556310793418, 0.013867136839583492, 0.012198926506533684, 0.010666101334644774, 0.00926913212665601, 0.008006113028742408, 0.006873115437888062, 0.005864551928152404, 0.0049735365161414635, 0.00419222962395352, 0.003512158371335674, 0.0029245051893809332, 0.0024203600642353114],
            "type": "arbitrary",
        },
        "2985209571553696033_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
        },
        "-3477601633382428889_i": {
            "samples": [0.002416782733285445, 0.0029119639171118136, 0.0034879044506540783, 0.00415310947579437, 0.004916005832864119, 0.005784710242708293, 0.0067667641618306355, 0.007868839394088363, 0.0090964205827995, 0.010453472794458255, 0.01194210442824829, 0.013562237518211834, 0.015311299002902118, 0.017183947585848427, 0.01917185127328757, 0.02126353044627351, 0.023444280324158583, 0.02569618486516688, 0.027998231532400004, 0.030326532985631673, 0.032654657748492105, 0.03495406740548105, 0.037194653106882324, 0.03934535934058818, 0.04137487832891846, 0.04325239429324332, 0.04494835345640833, 0.04643523325096258, 0.04768828295300995, 0.04868620799024986, 0.049411771530654326, 0.049852289620141044, 0.05, 0.049852289620141044, 0.049411771530654326, 0.04868620799024986, 0.04768828295300995, 0.04643523325096258, 0.04494835345640833, 0.04325239429324332, 0.04137487832891846, 0.03934535934058818, 0.037194653106882324, 0.03495406740548105, 0.032654657748492105, 0.030326532985631673, 0.027998231532400004, 0.02569618486516688, 0.023444280324158583, 0.02126353044627351, 0.01917185127328757, 0.017183947585848427, 0.015311299002902118, 0.013562237518211834, 0.01194210442824829, 0.010453472794458255, 0.0090964205827995, 0.007868839394088363, 0.0067667641618306355, 0.005784710242708293, 0.004916005832864119, 0.00415310947579437, 0.0034879044506540783, 0.0029119639171118136, 0.002416782733285445] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-3477601633382428889_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "-5829967302144723109_i": {
            "samples": [0.0024133180234607392, 0.0028998450454134628, 0.00346451558920456, 0.004115453893829434, 0.004860718315668192, 0.0057080880004843505, 0.006664818985020722, 0.007737373288764629, 0.008931126357051284, 0.010250060065080184, 0.011696450294316233, 0.013270559740947228, 0.014970347995637963, 0.016791211928589855, 0.018725769914081158, 0.02076370333904112, 0.02289166808858072, 0.025093287246301433, 0.027349234084497978, 0.029637411586921195, 0.03193323132661429, 0.03420999063895378, 0.036439342850399604, 0.038591851043963565, 0.04063761168275637, 0.04254693060275435, 0.04429103065045601, 0.04584276778660145, 0.04717733097628471, 0.04827290076478668, 0.0491112421665986, 0.049678209377909864] + [0.049964142799259675] * 2 + [0.049678209377909864, 0.0491112421665986, 0.04827290076478668, 0.04717733097628471, 0.04584276778660145, 0.04429103065045601, 0.04254693060275435, 0.04063761168275637, 0.038591851043963565, 0.036439342850399604, 0.03420999063895378, 0.03193323132661429, 0.029637411586921195, 0.027349234084497978, 0.025093287246301433, 0.02289166808858072, 0.02076370333904112, 0.018725769914081158, 0.016791211928589855, 0.014970347995637963, 0.013270559740947228, 0.011696450294316233, 0.010250060065080184, 0.008931126357051284, 0.007737373288764629, 0.006664818985020722, 0.0057080880004843505, 0.004860718315668192, 0.004115453893829434, 0.00346451558920456, 0.0028998450454134628, 0.0024133180234607392] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5829967302144723109_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "6609007170341003591_i": {
            "samples": [0.002409960702571528, 0.0028881276970462895, 0.0034419468721474987, 0.004079183800229198, 0.004807549079145888, 0.005634501767364641, 0.006567024748239613, 0.007611375133453423, 0.008772814407308023, 0.010055324652747746, 0.011461318806597346, 0.012991354374124001, 0.01464386129321684, 0.016414895575980307, 0.018297930874598085, 0.02028370013450789, 0.02236009894512199, 0.024512161035382552, 0.026722114577887302, 0.028969525585645972, 0.03123153177148329, 0.033483166890683175, 0.03569777193628933, 0.037847485766526294, 0.03990380399967908, 0.04183819150978624, 0.043622730793235705, 0.04523078603633418, 0.046637661057344, 0.047821228547837324, 0.04876250827672761, 0.049446173172996724, 0.049860964440973855, 0.05, 0.049860964440973855, 0.049446173172996724, 0.04876250827672761, 0.047821228547837324, 0.046637661057344, 0.04523078603633418, 0.043622730793235705, 0.04183819150978624, 0.03990380399967908, 0.037847485766526294, 0.03569777193628933, 0.033483166890683175, 0.03123153177148329, 0.028969525585645972, 0.026722114577887302, 0.024512161035382552, 0.02236009894512199, 0.02028370013450789, 0.018297930874598085, 0.016414895575980307, 0.01464386129321684, 0.012991354374124001, 0.011461318806597346, 0.010055324652747746, 0.008772814407308023, 0.007611375133453423, 0.006567024748239613, 0.005634501767364641, 0.004807549079145888, 0.004079183800229198, 0.0034419468721474987, 0.0028881276970462895, 0.002409960702571528, 0.0],
            "type": "arbitrary",
        },
        "6609007170341003591_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "-3632207614141556246_i": {
            "samples": [0.0024067058573818425, 0.002876792342132161, 0.0034201564100956984, 0.004044225617191438, 0.004756382127650614, 0.005563781369226778, 0.006473144886509911, 0.007490530113344597, 0.008621081194687644, 0.009868766443995265, 0.011236109456194202, 0.012723922230419727, 0.014331049806499624, 0.016054136798034593, 0.01788742672933987, 0.019822605178684748, 0.021848697336027387, 0.02395202965988791, 0.026116263850466306, 0.02832250935902005, 0.030549518172714146, 0.03277396272735183, 0.03497079461551554, 0.037113678408998575, 0.03917549155671987, 0.04112887811993324, 0.0429468412361583, 0.044603356825750756, 0.046073989317072656, 0.0473364891874168, 0.04837135198105608, 0.049162319214457566, 0.04969680320656619] + [0.04996622032584039] * 2 + [0.04969680320656619, 0.049162319214457566, 0.04837135198105608, 0.0473364891874168, 0.046073989317072656, 0.044603356825750756, 0.0429468412361583, 0.04112887811993324, 0.03917549155671987, 0.037113678408998575, 0.03497079461551554, 0.03277396272735183, 0.030549518172714146, 0.02832250935902005, 0.026116263850466306, 0.02395202965988791, 0.021848697336027387, 0.019822605178684748, 0.01788742672933987, 0.016054136798034593, 0.014331049806499624, 0.012723922230419727, 0.011236109456194202, 0.009868766443995265, 0.008621081194687644, 0.007490530113344597, 0.006473144886509911, 0.005563781369226778, 0.004756382127650614, 0.004044225617191438, 0.0034201564100956984, 0.002876792342132161, 0.0024067058573818425],
            "type": "arbitrary",
        },
        "-3632207614141556246_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
        },
        "-2078495740119386424_i": {
            "samples": [0.002403548869684607, 0.002865820691614407, 0.0033991050907472642, 0.0040105108033760715, 0.0047071095929761666, 0.005495768744439523, 0.006382959818160457, 0.0073745460484814385, 0.008475552020915043, 0.00968992055722552, 0.011020263018688789, 0.012467610438864815, 0.01403117394538493, 0.015708123750690386, 0.017493396511464265, 0.019379541009510785, 0.02135661183854497, 0.023412120053710055, 0.02553104853635789, 0.027695938152648772, 0.02988704867426442, 0.032082595943622026, 0.03425906399134473, 0.036391587860823076, 0.03845439989291418, 0.04042132931542719, 0.042266342314659915, 0.04396410748451649, 0.0454905697855672, 0.04682351501448994, 0.047943106368403154, 0.048832375039166126, 0.04947764790163084, 0.049868897238146144, 0.05, 0.049868897238146144, 0.04947764790163084, 0.048832375039166126, 0.047943106368403154, 0.04682351501448994, 0.0454905697855672, 0.04396410748451649, 0.042266342314659915, 0.04042132931542719, 0.03845439989291418, 0.036391587860823076, 0.03425906399134473, 0.032082595943622026, 0.02988704867426442, 0.027695938152648772, 0.02553104853635789, 0.023412120053710055, 0.02135661183854497, 0.019379541009510785, 0.017493396511464265, 0.015708123750690386, 0.01403117394538493, 0.012467610438864815, 0.011020263018688789, 0.00968992055722552, 0.008475552020915043, 0.0073745460484814385, 0.006382959818160457, 0.005495768744439523, 0.0047071095929761666, 0.0040105108033760715, 0.0033991050907472642, 0.002865820691614407, 0.002403548869684607] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2078495740119386424_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "1601002202885208100_i": {
            "samples": [0.002400485394497352, 0.002855195600634447, 0.003378756354411561, 0.003977975435911384, 0.004659631047907215, 0.005430316910988311, 0.006296265493955797, 0.00726315147239336, 0.008335878618591175, 0.009518354479012657, 0.010813258341494367, 0.012221809076095859, 0.013743540388445672, 0.015376091787717117, 0.017115024079373757, 0.018953668387053993, 0.020883017539213667, 0.022891668088580716, 0.02496582024736544, 0.02708934161995265, 0.029243898821220887, 0.031409158929666676, 0.03356306030992498, 0.03568214973968598, 0.03774198009945037, 0.03971756025067383, 0.04158384626586692, 0.04331626101013014, 0.04489122732685822, 0.04628669885554552, 0.04748267188974292, 0.04846166172381721, 0.04920912766202454, 0.049713832261944445] + [0.04996812241102594] * 2 + [0.049713832261944445, 0.04920912766202454, 0.04846166172381721, 0.04748267188974292, 0.04628669885554552, 0.04489122732685822, 0.04331626101013014, 0.04158384626586692, 0.03971756025067383, 0.03774198009945037, 0.03568214973968598, 0.03356306030992498, 0.031409158929666676, 0.029243898821220887, 0.02708934161995265, 0.02496582024736544, 0.022891668088580716, 0.020883017539213667, 0.018953668387053993, 0.017115024079373757, 0.015376091787717117, 0.013743540388445672, 0.012221809076095859, 0.010813258341494367, 0.009518354479012657, 0.008335878618591175, 0.00726315147239336, 0.006296265493955797, 0.005430316910988311, 0.004659631047907215, 0.003977975435911384, 0.003378756354411561, 0.002855195600634447, 0.002400485394497352] + [0.0] * 2,
            "type": "arbitrary",
        },
        "1601002202885208100_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "119263947883780439_i": {
            "samples": [0.0023975113401624457, 0.0028449009807679673, 0.0033590759908060266, 0.003946559832881187, 0.0046138528870977216, 0.005367289035338639, 0.0062128720885030585, 0.007156093896448765, 0.008201736968157385, 0.009353665457905674, 0.010614609399372732, 0.011985948044452004, 0.013467499033156036, 0.015057320829185861, 0.016751536346890437, 0.018544185917778053, 0.020427117654172263, 0.02238992283060589, 0.024419923100782986, 0.02650221519687987, 0.028619777234860047, 0.030753638910412964, 0.032883115770880496, 0.03498610546329214, 0.03703944147740068, 0.039019297527471145, 0.04090163345687087, 0.04266267151625229, 0.04427939016591169, 0.045730021281727276, 0.0469945358813685, 0.04805510329088511, 0.04889650907303556, 0.049506518040757966, 0.04987617025505978, 0.05, 0.04987617025505978, 0.049506518040757966, 0.04889650907303556, 0.04805510329088511, 0.0469945358813685, 0.045730021281727276, 0.04427939016591169, 0.04266267151625229, 0.04090163345687087, 0.039019297527471145, 0.03703944147740068, 0.03498610546329214, 0.032883115770880496, 0.030753638910412964, 0.028619777234860047, 0.02650221519687987, 0.024419923100782986, 0.02238992283060589, 0.020427117654172263, 0.018544185917778053, 0.016751536346890437, 0.015057320829185861, 0.013467499033156036, 0.011985948044452004, 0.010614609399372732, 0.009353665457905674, 0.008201736968157385, 0.007156093896448765, 0.0062128720885030585, 0.005367289035338639, 0.0046138528870977216, 0.003946559832881187, 0.0033590759908060266, 0.0028449009807679673, 0.0023975113401624457, 0.0],
            "type": "arbitrary",
        },
        "119263947883780439_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "7215441445934793223_i": {
            "samples": [0.0023946228501606362, 0.0028349217201900498, 0.00334003195482363, 0.003916208211836444, 0.004569687767802362, 0.005306557591749217, 0.006132602818318216, 0.007053138240012854, 0.008072825318239813, 0.009195478131102977, 0.010423862595733961, 0.011759494182001253, 0.013202440126173151, 0.014751132808722143, 0.01640220143134939, 0.01815032936882021, 0.01998814454155857, 0.021906149824206973, 0.023892699854184553, 0.025934029627344375, 0.028014338975640676, 0.030115935441649956, 0.03221943624125977, 0.03430402799942942, 0.03634778082948979, 0.03832801119018458, 0.04022168589028565, 0.04200585771482498, 0.043658121514372, 0.0451570783166006, 0.0464827941624143, 0.04761723999475882, 0.0485446990735277, 0.04925212906734522, 0.049729467169738945] + [0.049969868264962615] * 2 + [0.049729467169738945, 0.04925212906734522, 0.0485446990735277, 0.04761723999475882, 0.0464827941624143, 0.0451570783166006, 0.043658121514372, 0.04200585771482498, 0.04022168589028565, 0.03832801119018458, 0.03634778082948979, 0.03430402799942942, 0.03221943624125977, 0.030115935441649956, 0.028014338975640676, 0.025934029627344375, 0.023892699854184553, 0.021906149824206973, 0.01998814454155857, 0.01815032936882021, 0.01640220143134939, 0.014751132808722143, 0.013202440126173151, 0.011759494182001253, 0.010423862595733961, 0.009195478131102977, 0.008072825318239813, 0.007053138240012854, 0.006132602818318216, 0.005306557591749217, 0.004569687767802362, 0.003916208211836444, 0.00334003195482363, 0.0028349217201900498, 0.0023946228501606362],
            "type": "arbitrary",
        },
        "7215441445934793223_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
        },
        "4020255950087090211_i": {
            "samples": [0.002391816286468386, 0.002825243610948521, 0.0033215941992491907, 0.0038868683804221408, 0.004527054103908085, 0.0052480036021318325, 0.006055292872816925, 0.0069540654088154534, 0.007948862388609255, 0.009043442361751145, 0.010240594288924036, 0.01154194858951179, 0.012947791570322002, 0.014456889214970445, 0.01606632676191024, 0.017771370749839012, 0.019565360226583672, 0.02143963357306465, 0.023383496868672304, 0.02538423891112007, 0.02742719690867722, 0.029495875506114155, 0.03157212022288823, 0.033636344622404654, 0.03566780865673102, 0.03764494371458435, 0.03954571802189338, 0.04134803428770198, 0.043030149937163614, 0.04457110900660239, 0.045951173862560896, 0.04715224440352183, 0.04815825234873114, 0.048955518632689946, 0.04953306280435922, 0.04988285465277764, 0.05, 0.04988285465277764, 0.04953306280435922, 0.048955518632689946, 0.04815825234873114, 0.04715224440352183, 0.045951173862560896, 0.04457110900660239, 0.043030149937163614, 0.04134803428770198, 0.03954571802189338, 0.03764494371458435, 0.03566780865673102, 0.033636344622404654, 0.03157212022288823, 0.029495875506114155, 0.02742719690867722, 0.02538423891112007, 0.023383496868672304, 0.02143963357306465, 0.019565360226583672, 0.017771370749839012, 0.01606632676191024, 0.014456889214970445, 0.012947791570322002, 0.01154194858951179, 0.010240594288924036, 0.009043442361751145, 0.007948862388609255, 0.0069540654088154534, 0.006055292872816925, 0.0052480036021318325, 0.004527054103908085, 0.0038868683804221408, 0.0033215941992491907, 0.002825243610948521, 0.002391816286468386] + [0.0] * 3,
            "type": "arbitrary",
        },
        "4020255950087090211_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "-8474418866615923455_i": {
            "samples": [0.0023890882143082406, 0.002815853282620022, 0.0033037345226438275, 0.0038584914556833196, 0.004485875607510272, 0.005191515947754341, 0.005980788446132368, 0.006858671005965548, 0.007829585737254945, 0.008897231266792356, 0.010064408524271744, 0.01133284415962482, 0.01270301640293852, 0.014173988737419369, 0.015743257180722108, 0.017406617224934955, 0.019158056538685103, 0.020989679360104194, 0.022891668088580716, 0.024852286907872882, 0.026857931346046467, 0.028893226513865777, 0.030941175390385614, 0.03298335698263938, 0.03500017252695872, 0.03697113618372704, 0.038875204973662064, 0.04069114108470412, 0.042397898217736124, 0.043975022407256356, 0.045403056813649464, 0.04666393939043146, 0.04774138212280154, 0.048621220736860225, 0.04929172439775786, 0.049743855936678634] + [0.04997147453894671] * 2 + [0.049743855936678634, 0.04929172439775786, 0.048621220736860225, 0.04774138212280154, 0.04666393939043146, 0.045403056813649464, 0.043975022407256356, 0.042397898217736124, 0.04069114108470412, 0.038875204973662064, 0.03697113618372704, 0.03500017252695872, 0.03298335698263938, 0.030941175390385614, 0.028893226513865777, 0.026857931346046467, 0.024852286907872882, 0.022891668088580716, 0.020989679360104194, 0.019158056538685103, 0.017406617224934955, 0.015743257180722108, 0.014173988737419369, 0.01270301640293852, 0.01133284415962482, 0.010064408524271744, 0.008897231266792356, 0.007829585737254945, 0.006858671005965548, 0.005980788446132368, 0.005191515947754341, 0.004485875607510272, 0.0038584914556833196, 0.0033037345226438275, 0.002815853282620022, 0.0023890882143082406] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-8474418866615923455_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "7550233452913711648_i": {
            "samples": [0.002386435388158208, 0.0028067381417066863, 0.003286426430826524, 0.003831031609024675, 0.004446080872969317, 0.005136990745124717, 0.005908945859089028, 0.0067667641618306355, 0.007714750275078417, 0.008756539417257549, 0.009894934954180734, 0.011131743293944549, 0.012467610438864811, 0.013901865022659707, 0.01543237306183095, 0.0170554099048296, 0.01876555494256998, 0.020555614525359374, 0.022416578197047152, 0.024337612797998585, 0.026306098204672824, 0.02830770747585988, 0.030326532985631673, 0.03234525877321762, 0.03434537787286939, 0.03630745185368455, 0.038211408258574525, 0.040036870145840404, 0.0417635105705636, 0.043371423659170544, 0.04484150298734344, 0.04615581731933179, 0.04729797344533827, 0.04825345588948402, 0.04900993366533776, 0.049557525024414247, 0.04988901225428032, 0.05, 0.04988901225428032, 0.049557525024414247, 0.04900993366533776, 0.04825345588948402, 0.04729797344533827, 0.04615581731933179, 0.04484150298734344, 0.043371423659170544, 0.0417635105705636, 0.040036870145840404, 0.038211408258574525, 0.03630745185368455, 0.03434537787286939, 0.03234525877321762, 0.030326532985631673, 0.02830770747585988, 0.026306098204672824, 0.024337612797998585, 0.022416578197047152, 0.020555614525359374, 0.01876555494256998, 0.0170554099048296, 0.01543237306183095, 0.013901865022659707, 0.012467610438864811, 0.011131743293944549, 0.009894934954180734, 0.008756539417257549, 0.007714750275078417, 0.0067667641618306355, 0.005908945859089028, 0.005136990745124717, 0.004446080872969317, 0.003831031609024675, 0.003286426430826524, 0.0028067381417066863, 0.002386435388158208, 0.0],
            "type": "arbitrary",
        },
        "7550233452913711648_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "7771727512112426896_i": {
            "samples": [0.0023838547389005323, 0.0027978863162037033, 0.0032696450105638808, 0.003804445834154376, 0.004407602998983276, 0.005084330779299037, 0.005839630761904705, 0.00667816647056171, 0.0076041269134938545, 0.008621081194687642, 0.009731826929995772, 0.010938235794364525, 0.012241100070511211, 0.013639984544023426, 0.01513308846652301, 0.016717122559419654, 0.018387206130354505, 0.02013678930103379, 0.021957605082488073, 0.023839655572363803, 0.025771235887146762, 0.027738998587590755, 0.029728060324811796, 0.03172215125364979, 0.03370380646408998, 0.03565459731383328, 0.03755539915504877, 0.03938669059000439, 0.04112887811993324, 0.04276263892503575, 0.044269273583694285, 0.045631059852667466, 0.0468315982256859, 0.04785613989325341, 0.04869188795686513, 0.0493282633079167, 0.049757127452727035] + [0.04997295572376939] * 2 + [0.049757127452727035, 0.0493282633079167, 0.04869188795686513, 0.04785613989325341, 0.0468315982256859, 0.045631059852667466, 0.044269273583694285, 0.04276263892503575, 0.04112887811993324, 0.03938669059000439, 0.03755539915504877, 0.03565459731383328, 0.03370380646408998, 0.03172215125364979, 0.029728060324811796, 0.027738998587590755, 0.025771235887146762, 0.023839655572363803, 0.021957605082488073, 0.02013678930103379, 0.018387206130354505, 0.016717122559419654, 0.01513308846652301, 0.013639984544023426, 0.012241100070511211, 0.010938235794364525, 0.009731826929995772, 0.008621081194687642, 0.0076041269134938545, 0.00667816647056171, 0.005839630761904705, 0.005084330779299037, 0.004407602998983276, 0.003804445834154376, 0.0032696450105638808, 0.0027978863162037033, 0.0023838547389005323],
            "type": "arbitrary",
        },
        "7771727512112426896_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
        },
        "4405196166482164595_i": {
            "samples": [0.002381343362003121, 0.0027892866048317543, 0.0032533668142381844, 0.0037786937356530425, 0.004370379244734646, 0.0050334449886448905, 0.0057727174092799365, 0.006592711022417429, 0.007497501331800719, 0.008490589288978839, 0.009574759750733155, 0.010751936915644368, 0.012023040216887354, 0.013387844585182461, 0.014844849348858226, 0.016391160282601274, 0.018022389429891057, 0.019732577286671354, 0.021514141730269384, 0.023357857698380058, 0.02525287106526743, 0.027186749430930964, 0.029145571646634085, 0.031114056867874947, 0.03307573278246873, 0.03501314144295258, 0.0369080798810717, 0.03874187144416247, 0.04049566261786312, 0.04215073903618566, 0.04368885347606519, 0.04509255793226413, 0.04634553140659614, 0.04743289485090372, 0.04834150479385936, 0.04906021756373722, 0.049580116686908246, 0.04989469697675056, 0.05, 0.04989469697675056, 0.049580116686908246, 0.04906021756373722, 0.04834150479385936, 0.04743289485090372, 0.04634553140659614, 0.04509255793226413, 0.04368885347606519, 0.04215073903618566, 0.04049566261786312, 0.03874187144416247, 0.0369080798810717, 0.03501314144295258, 0.03307573278246873, 0.031114056867874947, 0.029145571646634085, 0.027186749430930964, 0.02525287106526743, 0.023357857698380058, 0.021514141730269384, 0.019732577286671354, 0.018022389429891057, 0.016391160282601274, 0.014844849348858226, 0.013387844585182461, 0.012023040216887354, 0.010751936915644368, 0.009574759750733155, 0.008490589288978839, 0.007497501331800719, 0.006592711022417429, 0.0057727174092799365, 0.0050334449886448905, 0.004370379244734646, 0.0037786937356530425, 0.0032533668142381844, 0.0027892866048317543, 0.002381343362003121] + [0.0] * 3,
            "type": "arbitrary",
        },
        "4405196166482164595_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
        },
        "4626690225680879843_i": {
            "samples": [0.0023788985066381502, 0.0027809284304838883, 0.0032375697544028154, 0.003753737336079348, 0.004334350716624311, 0.004984247995779588, 0.0057080880004843505, 0.006510241522248109, 0.007394672852595283, 0.008364813324402726, 0.009423429055037947, 0.010572485566995856, 0.011813012413266466, 0.013144971336512885, 0.014567131821221753, 0.01607695813455482, 0.01767051207432904, 0.01934237563356426, 0.021085597636209694, 0.022891668088580716, 0.02475052352197671, 0.02665058597661253, 0.028578837505011542, 0.03052093117111936, 0.03246133851330052, 0.03438353235519167, 0.0362702027237503, 0.0381035025086781, 0.03986531841436178, 0.04153756175813872, 0.043102472799610075, 0.04454293158439271, 0.04584276778660145, 0.04698706176511043, 0.04796242902846769, 0.04875728054180862, 0.049362051805404844, 0.0497693943770712] + [0.04997432447755395] * 2 + [0.0497693943770712, 0.049362051805404844, 0.04875728054180862, 0.04796242902846769, 0.04698706176511043, 0.04584276778660145, 0.04454293158439271, 0.043102472799610075, 0.04153756175813872, 0.03986531841436178, 0.0381035025086781, 0.0362702027237503, 0.03438353235519167, 0.03246133851330052, 0.03052093117111936, 0.028578837505011542, 0.02665058597661253, 0.02475052352197671, 0.022891668088580716, 0.021085597636209694, 0.01934237563356426, 0.01767051207432904, 0.01607695813455482, 0.014567131821221753, 0.013144971336512885, 0.011813012413266466, 0.010572485566995856, 0.009423429055037947, 0.008364813324402726, 0.007394672852595283, 0.006510241522248109, 0.0057080880004843505, 0.004984247995779588, 0.004334350716624311, 0.003753737336079348, 0.0032375697544028154, 0.0027809284304838883, 0.0023788985066381502] + [0.0] * 2,
            "type": "arbitrary",
        },
        "4626690225680879843_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
        },
        "1775636094303868161_i": {
            "samples": [0.0023765175656522927, 0.00277280179748533, 0.003222233007255454, 0.003729540899760031, 0.0042994620825031644, 0.004936659680003747, 0.005645632077882292, 0.006430611485562499, 0.007295453414731069, 0.008243518601862293, 0.009277549343912747, 0.010399542651203787, 0.011610623033113523, 0.012910918101726147, 0.014299440486615508, 0.015773979781220488, 0.017331008369633794, 0.01896560499595428, 0.020671399823556116, 0.022440544479577298, 0.024263710186295383, 0.026130116546987422, 0.02802759288646575, 0.02994267325901653, 0.031860725348329115, 0.03376611252030916, 0.03564238728058127, 0.03747251336822416, 0.03923911272284779, 0.04092473263182789, 0.04251212753632145, 0.043984549284493316, 0.04532603910028947, 0.04652171421278589, 0.04755804198445521, 0.04842309449844854, 0.04910677691816965, 0.049601023510753364, 0.04989995601404226, 0.05, 0.04989995601404226, 0.049601023510753364, 0.04910677691816965, 0.04842309449844854, 0.04755804198445521, 0.04652171421278589, 0.04532603910028947, 0.043984549284493316, 0.04251212753632145, 0.04092473263182789, 0.03923911272284779, 0.03747251336822416, 0.03564238728058127, 0.03376611252030916, 0.031860725348329115, 0.02994267325901653, 0.02802759288646575, 0.026130116546987422, 0.024263710186295383, 0.022440544479577298, 0.020671399823556116, 0.01896560499595428, 0.017331008369633794, 0.015773979781220488, 0.014299440486615508, 0.012910918101726147, 0.011610623033113523, 0.010399542651203787, 0.009277549343912747, 0.008243518601862293, 0.007295453414731069, 0.006430611485562499, 0.005645632077882292, 0.004936659680003747, 0.0042994620825031644, 0.003729540899760031, 0.003222233007255454, 0.00277280179748533, 0.0023765175656522927, 0.0],
            "type": "arbitrary",
        },
        "1775636094303868161_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
        },
        "1154310326417174617_i": {
            "samples": [0.0023741980663118723, 0.0027648972523077447, 0.0032073369241662967, 0.0037060707716190452, 0.004265661310659706, 0.004890604787077224, 0.005585245978070846, 0.006353683504536691, 0.007199666634441962, 0.00812648494662392, 0.009136852622855698, 0.010232789530572876, 0.011415501634023632, 0.012685263611333798, 0.014041306841966548, 0.015481716146257238, 0.017003338789898063, 0.01860170929687262, 0.02027099353233575, 0.022003955313550594, 0.02379194847753636, 0.025624936878516826, 0.02749154421167759, 0.029379134872581925, 0.03127392627966391, 0.033161132231419775, 0.035025135965740424, 0.03684969066555054, 0.038618144244593276, 0.0403136843834164, 0.041919599002129805, 0.04341954668575614, 0.04479783104962841, 0.046039672671701934, 0.0471314720457076, 0.04806105703700783, 0.048817908557594714, 0.04939335861570002, 0.0497807555286759] + [0.04997559189699447] * 2 + [0.0497807555286759, 0.04939335861570002, 0.048817908557594714, 0.04806105703700783, 0.0471314720457076, 0.046039672671701934, 0.04479783104962841, 0.04341954668575614, 0.041919599002129805, 0.0403136843834164, 0.038618144244593276, 0.03684969066555054, 0.035025135965740424, 0.033161132231419775, 0.03127392627966391, 0.029379134872581925, 0.02749154421167759, 0.025624936878516826, 0.02379194847753636, 0.022003955313550594, 0.02027099353233575, 0.01860170929687262, 0.017003338789898063, 0.015481716146257238, 0.014041306841966548, 0.012685263611333798, 0.011415501634023632, 0.010232789530572876, 0.009136852622855698, 0.00812648494662392, 0.007199666634441962, 0.006353683504536691, 0.005585245978070846, 0.004890604787077224, 0.004265661310659706, 0.0037060707716190452, 0.0032073369241662967, 0.0027648972523077447, 0.0023741980663118723],
            "type": "arbitrary",
        },
        "1154310326417174617_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
        },
        "1375804385615889865_i": {
            "samples": [0.0023719376617539777, 0.0027572058474173954, 0.003192862950491985, 0.0036832952295819906, 0.004232899431126499, 0.004846012572645961, 0.005526832330445386, 0.006279328577150269, 0.007107146946222248, 0.008013505651825247, 0.009001087153051162, 0.010071926609742871, 0.011227299419639394, 0.012467610438864811, 0.013792287754816857, 0.015199684087177015, 0.01668698902458154, 0.018250155348319173, 0.019883842639177397, 0.02158138120093714, 0.023334759059131748, 0.025134634405631767, 0.026970375361881335, 0.028830128334327694, 0.03070091554758425, 0.032568761581510355, 0.03441884792917923, 0.03623569375865828, 0.03800336023035619, 0.03970567492278966, 0.04132647218290696, 0.04284984457176395, 0.044260400049559875, 0.04554351915970706, 0.04668560624918924, 0.04767432871595663, 0.04849883841124281, 0.049149969646391525, 0.049620408753911195, 0.04990483081790261, 0.05, 0.04990483081790261, 0.049620408753911195, 0.049149969646391525, 0.04849883841124281, 0.04767432871595663, 0.04668560624918924, 0.04554351915970706, 0.044260400049559875, 0.04284984457176395, 0.04132647218290696, 0.03970567492278966, 0.03800336023035619, 0.03623569375865828, 0.03441884792917923, 0.032568761581510355, 0.03070091554758425, 0.028830128334327694, 0.026970375361881335, 0.025134634405631767, 0.023334759059131748, 0.02158138120093714, 0.019883842639177397, 0.018250155348319173, 0.01668698902458154, 0.015199684087177015, 0.013792287754816857, 0.012467610438864811, 0.011227299419639394, 0.010071926609742871, 0.009001087153051162, 0.008013505651825247, 0.007107146946222248, 0.006279328577150269, 0.005526832330445386, 0.004846012572645961, 0.004232899431126499, 0.0036832952295819906, 0.003192862950491985, 0.0027572058474173954, 0.0023719376617539777] + [0.0] * 3,
            "type": "arbitrary",
        },
        "1375804385615889865_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
        },
        "-6389084342998740564_i": {
            "samples": [0.0023697341230815502, 0.0027497191079700937, 0.003178793550988529, 0.003661184349251405, 0.004201130317136066, 0.004802816476033676, 0.005470299598572874, 0.006207425493364534, 0.007017738815929368, 0.007904386509011268, 0.008870016302179503, 0.009916672026138945, 0.011045687809812412, 0.012257583515331636, 0.01355196401427587, 0.01492742510443359, 0.01638146899710487, 0.017910432358655807, 0.019509429856531403, 0.021172316031397853, 0.02289166808858072, 0.024658791871943433, 0.026463752854039426, 0.02829543345402747, 0.030141617389831035, 0.031989101097731676, 0.03382383152912155, 0.035631068881849984, 0.03739557206640686, 0.03910180397075797, 0.04073415289842753, 0.04227716593857408, 0.043715789509102224, 0.0450356119165765, 0.04622310251860319, 0.04726584196970143, 0.04815273808954074, 0.04887422211602598, 0.04942242049219364, 0.04979129787620506] + [0.04997676774289315] * 2 + [0.04979129787620506, 0.04942242049219364, 0.04887422211602598, 0.04815273808954074, 0.04726584196970143, 0.04622310251860319, 0.0450356119165765, 0.043715789509102224, 0.04227716593857408, 0.04073415289842753, 0.03910180397075797, 0.03739557206640686, 0.035631068881849984, 0.03382383152912155, 0.031989101097731676, 0.030141617389831035, 0.02829543345402747, 0.026463752854039426, 0.024658791871943433, 0.02289166808858072, 0.021172316031397853, 0.019509429856531403, 0.017910432358655807, 0.01638146899710487, 0.01492742510443359, 0.01355196401427587, 0.012257583515331636, 0.011045687809812412, 0.009916672026138945, 0.008870016302179503, 0.007904386509011268, 0.007017738815929368, 0.006207425493364534, 0.005470299598572874, 0.004802816476033676, 0.004201130317136066, 0.003661184349251405, 0.003178793550988529, 0.0027497191079700937, 0.0023697341230815502] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-6389084342998740564_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
        },
        "3573564073619056728_i": {
            "samples": [0.002367585332046556, 0.002742429001095446, 0.0031651121412089953, 0.003639709879688648, 0.0041703104847918586, 0.004760953821469017, 0.0054155616602510085, 0.006137860272902416, 0.0069312960193502, 0.007798944917806579, 0.008743417486256922, 0.009766760439516934, 0.010870357111619398, 0.01205482873719094, 0.013319938955978312, 0.014664504089895237, 0.016086311870337322, 0.017582051354369247, 0.019147256752444986, 0.020776267790237824, 0.022462209038039648, 0.024196990361033722, 0.02597133027379668, 0.027774803527376324, 0.02959591372555346, 0.03142219117030988, 0.033240315490314754, 0.03503626192859949, 0.03679546947713834, 0.038503028369162424, 0.0401438837980271, 0.041703052147697824, 0.043165845516891024, 0.04451809991721775, 0.04574640224315968, 0.04683831096255842, 0.047782565470367404, 0.0485692791906385, 0.04919011180175932, 0.04963841639207437, 0.049909357916148325, 0.05, 0.049909357916148325, 0.04963841639207437, 0.04919011180175932, 0.0485692791906385, 0.047782565470367404, 0.04683831096255842, 0.04574640224315968, 0.04451809991721775, 0.043165845516891024, 0.041703052147697824, 0.0401438837980271, 0.038503028369162424, 0.03679546947713834, 0.03503626192859949, 0.033240315490314754, 0.03142219117030988, 0.02959591372555346, 0.027774803527376324, 0.02597133027379668, 0.024196990361033722, 0.022462209038039648, 0.020776267790237824, 0.019147256752444986, 0.017582051354369247, 0.016086311870337322, 0.014664504089895237, 0.013319938955978312, 0.01205482873719094, 0.010870357111619398, 0.009766760439516934, 0.008743417486256922, 0.007798944917806579, 0.0069312960193502, 0.006137860272902416, 0.0054155616602510085, 0.004760953821469017, 0.0041703104847918586, 0.003639709879688648, 0.0031651121412089953, 0.002742429001095446, 0.002367585332046556, 0.0],
            "type": "arbitrary",
        },
        "3573564073619056728_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
        },
        "-9018644415177036998_i": {
            "samples": [0.0023654892742708774, 0.0027353279075391515, 0.003151803024336082, 0.003618845129261924, 0.004140398909227288, 0.0047203655441330665, 0.005362537422570768, 0.0060705256497609345, 0.0068476809801616524, 0.007697009067600198, 0.008621081194687642, 0.009621941912718581, 0.010701015284218336, 0.011859011662927799, 0.013095837159927582, 0.014410508119241997, 0.015801073051313504, 0.017264544538571694, 0.018796843625467123, 0.0203927591289532, 0.022045924149701537, 0.023748811827015427, 0.025492752061941737, 0.02726797053697746, 0.029063650893670724, 0.030868020401113125, 0.03266845887158564, 0.03445162996993254, 0.03620363343834905, 0.03791017613764978, 0.039556759210257725, 0.04112887811993324, 0.04261223183894916, 0.04399293705396253, 0.04525774296401605, 0.04639424206178008, 0.047391072232571156, 0.048238105580975396, 0.048926619603661396, 0.04944944666606251, 0.04980109820219597] + [0.04997786062858862] * 2 + [0.04980109820219597, 0.04944944666606251, 0.048926619603661396, 0.048238105580975396, 0.047391072232571156, 0.04639424206178008, 0.04525774296401605, 0.04399293705396253, 0.04261223183894916, 0.04112887811993324, 0.039556759210257725, 0.03791017613764978, 0.03620363343834905, 0.03445162996993254, 0.03266845887158564, 0.030868020401113125, 0.029063650893670724, 0.02726797053697746, 0.025492752061941737, 0.023748811827015427, 0.022045924149701537, 0.0203927591289532, 0.018796843625467123, 0.017264544538571694, 0.015801073051313504, 0.014410508119241997, 0.013095837159927582, 0.011859011662927799, 0.010701015284218336, 0.009621941912718581, 0.008621081194687642, 0.007697009067600198, 0.0068476809801616524, 0.0060705256497609345, 0.005362537422570768, 0.0047203655441330665, 0.004140398909227288, 0.003618845129261924, 0.003151803024336082, 0.0027353279075391515, 0.0023654892742708774],
            "type": "arbitrary",
        },
        "-9018644415177036998_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
        },
        "1760744602010964249_i": {
            "samples": [0.0023634440329593502, 0.0027284085954552796, 0.003138851332956245, 0.0035985648606288896, 0.0041113568557084494, 0.004680995938689247, 0.005311150468688069, 0.00600532059909286, 0.0067667641618306355, 0.007598417184809545, 0.008502810091413515, 0.009481980876368503, 0.010537386790920358, 0.011669816293375147, 0.012879303219463201, 0.014165045291316809, 0.01552532920487773, 0.01695746460460166, 0.018457729263681805, 0.020021327731311947, 0.021642365581140174, 0.023313841194520603, 0.025027656738345366, 0.026774649652645865, 0.028544645553053374, 0.030326532985631673, 0.032108359957239506, 0.0338774516165966, 0.035620547894877584, 0.03732395934686225, 0.03897373888245319, 0.040555866562226706, 0.04205644416788042, 0.04346189586630725, 0.04475917098022608, 0.04593594467215388, 0.046980812252376526, 0.04788347284235835, 0.04863489826575815, 0.049227483298830255, 0.04965517378525212, 0.04991356959803134, 0.05, 0.04991356959803134, 0.04965517378525212, 0.049227483298830255, 0.04863489826575815, 0.04788347284235835, 0.046980812252376526, 0.04593594467215388, 0.04475917098022608, 0.04346189586630725, 0.04205644416788042, 0.040555866562226706, 0.03897373888245319, 0.03732395934686225, 0.035620547894877584, 0.0338774516165966, 0.032108359957239506, 0.030326532985631673, 0.028544645553053374, 0.026774649652645865, 0.025027656738345366, 0.023313841194520603, 0.021642365581140174, 0.020021327731311947, 0.018457729263681805, 0.01695746460460166, 0.01552532920487773, 0.014165045291316809, 0.012879303219463201, 0.011669816293375147, 0.010537386790920358, 0.009481980876368503, 0.008502810091413515, 0.007598417184809545, 0.0067667641618306355, 0.00600532059909286, 0.005311150468688069, 0.004680995938689247, 0.0041113568557084494, 0.0035985648606288896, 0.003138851332956245, 0.0027284085954552796, 0.0023634440329593502] + [0.0] * 3,
            "type": "arbitrary",
        },
        "1760744602010964249_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
        },
        "-5117652412973727226_i": {
            "samples": [0.0023614477830638096, 0.0027216641961612113, 0.0031262429753324637, 0.003578845194019041, 0.0040831477242977785, 0.004642792428202869, 0.0052613287333539305, 0.0059421499025434435, 0.006688423508546294, 0.007503016839910196, 0.008388418185686591, 0.009346655170821307, 0.010379211532248009, 0.011486943930939034, 0.012670000579125477, 0.013927743616257138, 0.015258677283788763, 0.016660384019739603, 0.018129470612149777, 0.019661526510158164, 0.021251096288042743, 0.022891668088580713, 0.02457567963695314, 0.02629454311685732, 0.028038689840620853, 0.029797635231494826, 0.03156006417787868, 0.03331393632715323, 0.03504661037417321, 0.036744985880981476, 0.038395660655756815, 0.03998510123679154, 0.04149982358780436, 0.04292658072989966, 0.0442525537275051, 0.04546554222331691, 0.04655415059090276, 0.047507965750505046, 0.048317722777824534, 0.04897545462768124, 0.049474622591320176, 0.04981022450099476] + [0.04997887817809232] * 2 + [0.04981022450099476, 0.049474622591320176, 0.04897545462768124, 0.048317722777824534, 0.047507965750505046, 0.04655415059090276, 0.04546554222331691, 0.0442525537275051, 0.04292658072989966, 0.04149982358780436, 0.03998510123679154, 0.038395660655756815, 0.036744985880981476, 0.03504661037417321, 0.03331393632715323, 0.03156006417787868, 0.029797635231494826, 0.028038689840620853, 0.02629454311685732, 0.02457567963695314, 0.022891668088580713, 0.021251096288042743, 0.019661526510158164, 0.018129470612149777, 0.016660384019739603, 0.015258677283788763, 0.013927743616257138, 0.012670000579125477, 0.011486943930939034, 0.010379211532248009, 0.009346655170821307, 0.008388418185686591, 0.007503016839910196, 0.006688423508546294, 0.0059421499025434435, 0.0052613287333539305, 0.004642792428202869, 0.0040831477242977785, 0.003578845194019041, 0.0031262429753324637, 0.0027216641961612113, 0.0023614477830638096] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5117652412973727226_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
        },
        "5661736604214274021_i": {
            "samples": [0.0023594987858608523, 0.0027150881816862893, 0.0031139645857773107, 0.0035596635180664376, 0.004055736906838736, 0.004605705351574352, 0.005213004204556965, 0.005880923748526811, 0.006612543930766052, 0.007410664308975208, 0.00827773006657207, 0.009215755159204355, 0.010226243854141788, 0.01131011211301379, 0.012467610438864815, 0.013698249953282927, 0.015000733581042905, 0.016372894291256584, 0.017811642369046546, 0.019312923664813172, 0.020871690685061783, 0.022481888246841455, 0.024136455216242015, 0.025827343591189503, 0.027545555873158847, 0.02928120130671888, 0.031023571157490146, 0.03276123275757919, 0.03448214158408967, 0.03617377016362694, 0.03782325212764544, 0.03941753929454081, 0.04094356923922737, 0.04238844044386423, 0.0437395918177791, 0.044984983142411124, 0.04611327284821754, 0.047113989472523654, 0.0479776931850282, 0.04869612390285605, 0.04926233274822752, 0.049670793924314345, 0.04991749449086604, 0.05, 0.04991749449086604, 0.049670793924314345, 0.04926233274822752, 0.04869612390285605, 0.0479776931850282, 0.047113989472523654, 0.04611327284821754, 0.044984983142411124, 0.0437395918177791, 0.04238844044386423, 0.04094356923922737, 0.03941753929454081, 0.03782325212764544, 0.03617377016362694, 0.03448214158408967, 0.03276123275757919, 0.031023571157490146, 0.02928120130671888, 0.027545555873158847, 0.025827343591189503, 0.024136455216242015, 0.022481888246841455, 0.020871690685061783, 0.019312923664813172, 0.017811642369046546, 0.016372894291256584, 0.015000733581042905, 0.013698249953282927, 0.012467610438864815, 0.01131011211301379, 0.010226243854141788, 0.009215755159204355, 0.00827773006657207, 0.007410664308975208, 0.006612543930766052, 0.005880923748526811, 0.005213004204556965, 0.004605705351574352, 0.004055736906838736, 0.0035596635180664376, 0.0031139645857773107, 0.0027150881816862893, 0.0023594987858608523, 0.0],
            "type": "arbitrary",
        },
        "5661736604214274021_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
        },
        "4179998349212846360_i": {
            "samples": [0.0023575953839095015, 0.002708674343961557, 0.003102003478767531, 0.0035409984075191283, 0.00402909165514829, 0.0045696877678023645, 0.005166112648902035, 0.005821557364281266, 0.006539016831393066, 0.007321223984968252, 0.00817058019581819, 0.009089082905899914, 0.010078251625859302, 0.01113905361502447, 0.012271830721827588, 0.013476228998271037, 0.014751132808722145, 0.01609460522468131, 0.017503836527409104, 0.018975102624404182, 0.020503735119741663, 0.0220841046595669, 0.023709619001476934, 0.02537273703070116, 0.027064999669333657, 0.02877707830168332, 0.030498840975286517, 0.03221943624125977, 0.03392739407907832, 0.03561074292056631, 0.03725714135797283, 0.03885402270429286, 0.04038875018356396, 0.0418487801776481, 0.04322183065625878, 0.04449605167986177, 0.04566019470012907, 0.046703777297440935, 0.04761723999475882, 0.04839209187467782, 0.04902104190148081, 0.04949811310957606, 0.0498187371580125] + [0.04997982715937286] * 2 + [0.0498187371580125, 0.04949811310957606, 0.04902104190148081, 0.04839209187467782, 0.04761723999475882, 0.046703777297440935, 0.04566019470012907, 0.04449605167986177, 0.04322183065625878, 0.0418487801776481, 0.04038875018356396, 0.03885402270429286, 0.03725714135797283, 0.03561074292056631, 0.03392739407907832, 0.03221943624125977, 0.030498840975286517, 0.02877707830168332, 0.027064999669333657, 0.02537273703070116, 0.023709619001476934, 0.0220841046595669, 0.020503735119741663, 0.018975102624404182, 0.017503836527409104, 0.01609460522468131, 0.014751132808722145, 0.013476228998271037, 0.012271830721827588, 0.01113905361502447, 0.010078251625859302, 0.009089082905899914, 0.00817058019581819, 0.007321223984968252, 0.006539016831393066, 0.005821557364281266, 0.005166112648902035, 0.0045696877678023645, 0.00402909165514829, 0.0035409984075191283, 0.003102003478767531, 0.002708674343961557, 0.0023575953839095015],
            "type": "arbitrary",
        },
        "4179998349212846360_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
        },
        "-1366180850948390541_i": {
            "samples": [0.0023557359963581035, 0.002702416775512681, 0.0030903476064767566, 0.003522829547219092, 0.004003180959416371, 0.004534695275563765, 0.005120593358589029, 0.005763970676858676, 0.006467739668992819, 0.007234567834485123, 0.008066812254210081, 0.00896645141527161, 0.009935015382480405, 0.0109735155187145, 0.012082375102822195, 0.013261362320668355, 0.014509527206492262, 0.015825144182227458, 0.01720566187655127, 0.01864766189857047, 0.020146828189494592, 0.021697928476803786, 0.023294809208003968, 0.024930405145275957, 0.02659676455996392, 0.028285090680370613, 0.02998579972286272, 0.03168859548158114, 0.0333825600743261, 0.03505626005097021, 0.036697866676605594, 0.038295288815846165, 0.03983631647894344, 0.041308772756270824, 0.04270067157648922, 0.044000378485671676, 0.04519677146892932, 0.046279398730104206, 0.04723863031438423, 0.04806580050654053, 0.048753338064773985, 0.04929488155526912, 0.04968537733136282, 0.04992115804719207, 0.05, 0.04992115804719207, 0.04968537733136282, 0.04929488155526912, 0.048753338064773985, 0.04806580050654053, 0.04723863031438423, 0.046279398730104206, 0.04519677146892932, 0.044000378485671676, 0.04270067157648922, 0.041308772756270824, 0.03983631647894344, 0.038295288815846165, 0.036697866676605594, 0.03505626005097021, 0.0333825600743261, 0.03168859548158114, 0.02998579972286272, 0.028285090680370613, 0.02659676455996392, 0.024930405145275957, 0.023294809208003968, 0.021697928476803786, 0.020146828189494592, 0.01864766189857047, 0.01720566187655127, 0.015825144182227458, 0.014509527206492262, 0.013261362320668355, 0.012082375102822195, 0.0109735155187145, 0.009935015382480405, 0.00896645141527161, 0.008066812254210081, 0.007234567834485123, 0.006467739668992819, 0.005763970676858676, 0.005120593358589029, 0.004534695275563765, 0.004003180959416371, 0.003522829547219092, 0.0030903476064767566, 0.002702416775512681, 0.0023557359963581035] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1366180850948390541_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
        },
        "1108773240470778536_i": {
            "samples": [0.002353919114572558, 0.002696309851531143, 0.00307898551943427, 0.0035051376618063196, 0.003977975435911384, 0.004500685846748754, 0.005076388918068964, 0.005708088000484348, 0.006398615554804989, 0.007150574896042875, 0.007966278536960766, 0.00884768392586556, 0.009796327527285027, 0.010813258341494367, 0.011898972094507545, 0.013053347448852982, 0.014275585681915955, 0.015564155347705725, 0.01691674347479884, 0.01833021485368369, 0.019800580927307347, 0.021322979716784412, 0.022891668088580716, 0.0245000274999269, 0.026140584147037346, 0.027805044188660435, 0.029484344429800732, 0.03116871853280928, 0.032847778482463424, 0.03451061067637399, 0.036145885651279325, 0.03774198009945037, 0.039287109487906785, 0.040769469276886745, 0.04217738245321173, 0.04349945085839971, 0.04472470760917139, 0.04584276778660145, 0.04684397451519882, 0.04771953756838331, 0.04846166172381721, 0.04906366225031764, 0.04952006513485812, 0.04982668994851846] + [0.04998071359715336] * 2 + [0.04982668994851846, 0.04952006513485812, 0.04906366225031764, 0.04846166172381721, 0.04771953756838331, 0.04684397451519882, 0.04584276778660145, 0.04472470760917139, 0.04349945085839971, 0.04217738245321173, 0.040769469276886745, 0.039287109487906785, 0.03774198009945037, 0.036145885651279325, 0.03451061067637399, 0.032847778482463424, 0.03116871853280928, 0.029484344429800732, 0.027805044188660435, 0.026140584147037346, 0.0245000274999269, 0.022891668088580716, 0.021322979716784412, 0.019800580927307347, 0.01833021485368369, 0.01691674347479884, 0.015564155347705725, 0.014275585681915955, 0.013053347448852982, 0.011898972094507545, 0.010813258341494367, 0.009796327527285027, 0.00884768392586556, 0.007966278536960766, 0.007150574896042875, 0.006398615554804989, 0.005708088000484348, 0.005076388918068964, 0.004500685846748754, 0.003977975435911384, 0.0035051376618063196, 0.00307898551943427, 0.002696309851531143, 0.002353919114572558] + [0.0] * 2,
            "type": "arbitrary",
        },
        "1108773240470778536_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
        },
        "-4511218137379937594_i": {
            "samples": [0.0023521432980605113, 0.0026903482132105095, 0.0030679063300458726, 0.0034879044506540766, 0.003953447223179746, 0.004467619672724645, 0.005033444988644889, 0.005653837747975059, 0.006331552880619031, 0.007069130816380236, 0.00786883939408836, 0.008732613255708736, 0.009661991589606147, 0.010658055222875662, 0.011721364188337703, 0.012851897002720597, 0.0140489929839709, 0.015311299002902116, 0.016636722103163252, 0.01802238942989105, 0.019464616878161044, 0.0209588878050457, 0.022499843042273794, 0.024081283299824993, 0.02569618486516688, 0.02733672928041425, 0.028994347423940886, 0.030659778138672513, 0.03232314124242926, 0.03397402443335853, 0.03560158327372894, 0.037194653106882324, 0.03874187144416247, 0.040231809060531525, 0.04165310776858627, 0.042994622609584025, 0.04424556601489621, 0.04539565135896793, 0.04643523325096258, 0.04735544190081372, 0.0481483089486141, 0.04880688226446461, 0.049325327407432035, 0.049699013673513974, 0.04992458295798774, 0.05, 0.04992458295798774, 0.049699013673513974, 0.049325327407432035, 0.04880688226446461, 0.0481483089486141, 0.04735544190081372, 0.04643523325096258, 0.04539565135896793, 0.04424556601489621, 0.042994622609584025, 0.04165310776858627, 0.040231809060531525, 0.03874187144416247, 0.037194653106882324, 0.03560158327372894, 0.03397402443335853, 0.03232314124242926, 0.030659778138672513, 0.028994347423940886, 0.02733672928041425, 0.02569618486516688, 0.024081283299824993, 0.022499843042273794, 0.0209588878050457, 0.019464616878161044, 0.01802238942989105, 0.016636722103163252, 0.015311299002902116, 0.0140489929839709, 0.012851897002720597, 0.011721364188337703, 0.010658055222875662, 0.009661991589606147, 0.008732613255708736, 0.00786883939408836, 0.007069130816380236, 0.006331552880619031, 0.005653837747975059, 0.005033444988644889, 0.004467619672724645, 0.003953447223179746, 0.0034879044506540766, 0.0030679063300458726, 0.0026903482132105095, 0.0023521432980605113, 0.0],
            "type": "arbitrary",
        },
        "-4511218137379937594_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
        },
        "-6835776219466774047_i": {
            "samples": [0.0023504071706684183, 0.002684526752245091, 0.003057099678737945, 0.0034711125275900465, 0.003929569886006754, 0.004435459022221865, 0.004991710109454501, 0.005601152164127267, 0.006266464974861447, 0.006990127421560913, 0.007774362712087754, 0.008621081194687642, 0.009531821534077656, 0.010507691164227685, 0.011549307047327269, 0.012656737872029408, 0.013829448910539591, 0.015066250819290425, 0.016365253707858633, 0.01772382781187781, 0.019138572084960222, 0.020605291969744585, 0.022118987517657437, 0.023673852900300094, 0.025263288193100687, 0.026879924115683254, 0.028515660186145615, 0.03016171649210398, 0.03180869900505531, 0.033446678072439624, 0.0350652794207335, 0.036653786700647804, 0.0382012543101879, 0.03969662895135058, 0.04112887811993324, 0.04248712350336351, 0.04376077707607792, 0.044939677542379666, 0.04601422468837087, 0.04697550917162547, 0.04781543530237421, 0.048526834454084955, 0.049103566883684835, 0.04954060993977659, 0.049834130886838246] + [0.04998154286874318] * 2 + [0.049834130886838246, 0.04954060993977659, 0.049103566883684835, 0.048526834454084955, 0.04781543530237421, 0.04697550917162547, 0.04601422468837087, 0.044939677542379666, 0.04376077707607792, 0.04248712350336351, 0.04112887811993324, 0.03969662895135058, 0.0382012543101879, 0.036653786700647804, 0.0350652794207335, 0.033446678072439624, 0.03180869900505531, 0.03016171649210398, 0.028515660186145615, 0.026879924115683254, 0.025263288193100687, 0.023673852900300094, 0.022118987517657437, 0.020605291969744585, 0.019138572084960222, 0.01772382781187781, 0.016365253707858633, 0.015066250819290425, 0.013829448910539591, 0.012656737872029408, 0.011549307047327269, 0.010507691164227685, 0.009531821534077656, 0.008621081194687642, 0.007774362712087754, 0.006990127421560913, 0.006266464974861447, 0.005601152164127267, 0.004991710109454501, 0.004435459022221865, 0.003929569886006754, 0.0034711125275900465, 0.003057099678737945, 0.002684526752245091, 0.0023504071706684183],
            "type": "arbitrary",
        },
        "-6835776219466774047_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
        },
        "-2313458449376770731_i": {
            "samples": [0.0023487094170303773, 0.0026788405963976483, 0.0030465557025082116, 0.0034547453650004786, 0.00390631832647667, 0.004404168109843033, 0.004951135513422761, 0.005549967079187939, 0.00620326978449356, 0.00691346231996685, 0.007682723433531037, 0.008512937940321689, 0.009405641117495178, 0.010361962318306845, 0.011382568747762917, 0.012467610438864811, 0.01361666755014075, 0.014828701168026055, 0.016102008838123887, 0.01743418606418866, 0.018822095000024644, 0.02026184151517824, 0.021748761738846677, 0.02327741907718648, 0.024841612557469243, 0.026434397179580627, 0.028048116753501297, 0.029674449473986737, 0.031304466235011576, 0.03292870142192064, 0.03453723564470059, 0.03611978959808223, 0.03766582796051853, 0.039164671981945176, 0.040605619167156784, 0.04197806824496479, 0.04327164742994413, 0.0444763438397427, 0.04558263183192654, 0.04658159797435142, 0.047465060364983394, 0.04822568007240598, 0.04885706257690151, 0.049353847252378576, 0.04971178313839497, 0.04992778950448698, 0.05, 0.04992778950448698, 0.04971178313839497, 0.049353847252378576, 0.04885706257690151, 0.04822568007240598, 0.047465060364983394, 0.04658159797435142, 0.04558263183192654, 0.0444763438397427, 0.04327164742994413, 0.04197806824496479, 0.040605619167156784, 0.039164671981945176, 0.03766582796051853, 0.03611978959808223, 0.03453723564470059, 0.03292870142192064, 0.031304466235011576, 0.029674449473986737, 0.028048116753501297, 0.026434397179580627, 0.024841612557469243, 0.02327741907718648, 0.021748761738846677, 0.02026184151517824, 0.018822095000024644, 0.01743418606418866, 0.016102008838123887, 0.014828701168026055, 0.01361666755014075, 0.012467610438864811, 0.011382568747762917, 0.010361962318306845, 0.009405641117495178, 0.008512937940321689, 0.007682723433531037, 0.00691346231996685, 0.00620326978449356, 0.005549967079187939, 0.004951135513422761, 0.004404168109843033, 0.00390631832647667, 0.0034547453650004786, 0.0030465557025082116, 0.0026788405963976483, 0.0023487094170303773] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-2313458449376770731_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
        },
        "-7762103977444927572_i": {
            "samples": [0.002347048779249552, 0.002673285096051335, 0.0030362650056868575, 0.0034387872419526506, 0.003883668701533285, 0.004373712974291932, 0.0049116749569081235, 0.005500221680700284, 0.006141889580543693, 0.006839038534534935, 0.007593803111526728, 0.008408041573549649, 0.009283283289787775, 0.010220675325219643, 0.011220929067069556, 0.012284267842470251, 0.013410376557778703, 0.014598354450409277, 0.01584667208459727, 0.01715313374019508, 0.018514846335837026, 0.019928195992504606, 0.021388833279221975, 0.022891668088580716, 0.024430874966110842, 0.02599990956513435, 0.027591536719521245, 0.029197870423497665, 0.030810425784009523, 0.03242018277163988, 0.0340176613459811, 0.03559300727656994, 0.03713608772737931, 0.03863659542810152, 0.04008416002583862, 0.041468465003015625, 0.04277936836771416, 0.04400702517701141, 0.045142009847387025, 0.04617543614298125, 0.04709907271550833, 0.04790545210078051, 0.048587971156587625, 0.04914098105423956, 0.049559865109167794, 0.04984110295101274] + [0.04998231978575862] * 2 + [0.04984110295101274, 0.049559865109167794, 0.04914098105423956, 0.048587971156587625, 0.04790545210078051, 0.04709907271550833, 0.04617543614298125, 0.045142009847387025, 0.04400702517701141, 0.04277936836771416, 0.041468465003015625, 0.04008416002583862, 0.03863659542810152, 0.03713608772737931, 0.03559300727656994, 0.0340176613459811, 0.03242018277163988, 0.030810425784009523, 0.029197870423497665, 0.027591536719521245, 0.02599990956513435, 0.024430874966110842, 0.022891668088580716, 0.021388833279221975, 0.019928195992504606, 0.018514846335837026, 0.01715313374019508, 0.01584667208459727, 0.014598354450409277, 0.013410376557778703, 0.012284267842470251, 0.011220929067069556, 0.010220675325219643, 0.009283283289787775, 0.008408041573549649, 0.007593803111526728, 0.006839038534534935, 0.006141889580543693, 0.005500221680700284, 0.0049116749569081235, 0.004373712974291932, 0.003883668701533285, 0.0034387872419526506, 0.0030362650056868575, 0.002673285096051335, 0.002347048779249552] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7762103977444927572_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
        },
        "-3954932071202303921_i": {
            "samples": [0.0023454240537945543, 0.00266785581166854, 0.0030262186327295916, 0.003423223196004869, 0.003861598346498577, 0.004344061365504695, 0.0048732845618869895, 0.005451858302177329, 0.006082250685299729, 0.0067667641618306355, 0.007507489496236231, 0.008306257571426221, 0.009164589635859368, 0.01008364669168461, 0.011064178815137814, 0.012106475284621122, 0.013210316464479142, 0.014374928450381508, 0.015598941522470409, 0.016880353472302736, 0.0182164988667091, 0.0196040252840437, 0.021038877504485697, 0.022516290555281746, 0.024030792404005234, 0.025576216958733813, 0.027145727875001597, 0.02873185348777371, 0.030326532985631673, 0.031921173727724704, 0.03350671937640114, 0.03507372828494667, 0.03661246134614739, 0.03811297827941045, 0.039565241118007945, 0.04095922345972151, 0.04228502386959872, 0.04353298167811459, 0.044693793306593524, 0.04575862717834858, 0.04671923524177146, 0.04756805914264066, 0.048298329138143484, 0.04890415394425274, 0.0493805998496571, 0.04972375761069428, 0.049930795858806304, 0.05, 0.049930795858806304, 0.04972375761069428, 0.0493805998496571, 0.04890415394425274, 0.048298329138143484, 0.04756805914264066, 0.04671923524177146, 0.04575862717834858, 0.044693793306593524, 0.04353298167811459, 0.04228502386959872, 0.04095922345972151, 0.039565241118007945, 0.03811297827941045, 0.03661246134614739, 0.03507372828494667, 0.03350671937640114, 0.031921173727724704, 0.030326532985631673, 0.02873185348777371, 0.027145727875001597, 0.025576216958733813, 0.024030792404005234, 0.022516290555281746, 0.021038877504485697, 0.0196040252840437, 0.0182164988667091, 0.016880353472302736, 0.015598941522470409, 0.014374928450381508, 0.013210316464479142, 0.012106475284621122, 0.011064178815137814, 0.01008364669168461, 0.009164589635859368, 0.008306257571426221, 0.007507489496236231, 0.0067667641618306355, 0.006082250685299729, 0.005451858302177329, 0.0048732845618869895, 0.004344061365504695, 0.003861598346498577, 0.003423223196004869, 0.0030262186327295916, 0.00266785581166854, 0.0023454240537945543, 0.0],
            "type": "arbitrary",
        },
        "-3954932071202303921_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
        },
        "8484042401283422779_i": {
            "samples": [0.0023438340885947664, 0.002662548502086295, 0.003016408042880571, 0.003408038978403922, 0.003840085704057874, 0.004315182639942583, 0.004835922669629573, 0.005404822227200863, 0.006024283219370086, 0.006696552055769085, 0.007423676150889755, 0.008207458353881215, 0.009049409855302368, 0.009950702210656914, 0.010912119206528896, 0.011934009373685717, 0.01301624001984201, 0.014158153710107577, 0.015358528162793315, 0.016615540549723397, 0.017926737191282762, 0.019289009615272894, 0.020698577903878936, 0.022150982183836033, 0.02364108302101215, 0.025163071362560838, 0.026710488528717453, 0.028276256594121682, 0.029852719317876128, 0.0314316935857174, 0.03300453112063725, 0.03456219000455897, 0.03609531533820894, 0.03759432815440884, 0.03904952149711631, 0.040451162390149786, 0.04178959825099127, 0.04305536616140598, 0.04423930329240693, 0.04533265670024928, 0.04632719066581175, 0.04721528974415928, 0.047990055725537405, 0.04864539678371839, 0.049176107201602724, 0.04957793621528276, 0.04984764470335167] + [0.04998304866405808] * 2 + [0.04984764470335167, 0.04957793621528276, 0.049176107201602724, 0.04864539678371839, 0.047990055725537405, 0.04721528974415928, 0.04632719066581175, 0.04533265670024928, 0.04423930329240693, 0.04305536616140598, 0.04178959825099127, 0.040451162390149786, 0.03904952149711631, 0.03759432815440884, 0.03609531533820894, 0.03456219000455897, 0.03300453112063725, 0.0314316935857174, 0.029852719317876128, 0.028276256594121682, 0.026710488528717453, 0.025163071362560838, 0.02364108302101215, 0.022150982183836033, 0.020698577903878936, 0.019289009615272894, 0.017926737191282762, 0.016615540549723397, 0.015358528162793315, 0.014158153710107577, 0.01301624001984201, 0.011934009373685717, 0.010912119206528896, 0.009950702210656914, 0.009049409855302368, 0.008207458353881215, 0.007423676150889755, 0.006696552055769085, 0.006024283219370086, 0.005404822227200863, 0.004835922669629573, 0.004315182639942583, 0.003840085704057874, 0.003408038978403922, 0.003016408042880571, 0.002662548502086295, 0.0023438340885947664],
            "type": "arbitrary",
        },
        "8484042401283422779_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
        },
        "-1757172383199137058_i": {
            "samples": [0.0023422777803198446, 0.0026573591135838955, 0.003006825086557508, 0.0033932210123972066, 0.003819110258265289, 0.004287047663374263, 0.00479954970491761, 0.00535906150767277, 0.005967920866984466, 0.006628319533989669, 0.00734226209496504, 0.00811152286192766, 0.008937601277212043, 0.00982167641856898, 0.010764561271088567, 0.01176665750551206, 0.012827911566761958, 0.013947772929280167, 0.015125155414584882, 0.016358402489055148, 0.017645257464282145, 0.01898283950666276, 0.02036762632592945, 0.021795444353162226, 0.023261467137206407, 0.024760222584608464, 0.026285609543097933, 0.02783092408385142, 0.029388895675488788, 0.030951733265812565, 0.03251118109913282, 0.034058583901559664, 0.03558496086826492, 0.03708108769010378, 0.03853758566704166, 0.03994501677750795, 0.04129398341097818, 0.0425752313304191, 0.04377975431599434, 0.044898898855378545, 0.04592446719227338, 0.0468488170256052, 0.04766495616889826, 0.048366630533019005, 0.04894840388546867, 0.049405727964275475, 0.04973500168195559, 0.04993361834171834, 0.05, 0.04993361834171834, 0.04973500168195559, 0.049405727964275475, 0.04894840388546867, 0.048366630533019005, 0.04766495616889826, 0.0468488170256052, 0.04592446719227338, 0.044898898855378545, 0.04377975431599434, 0.0425752313304191, 0.04129398341097818, 0.03994501677750795, 0.03853758566704166, 0.03708108769010378, 0.03558496086826492, 0.034058583901559664, 0.03251118109913282, 0.030951733265812565, 0.029388895675488788, 0.02783092408385142, 0.026285609543097933, 0.024760222584608464, 0.023261467137206407, 0.021795444353162226, 0.02036762632592945, 0.01898283950666276, 0.017645257464282145, 0.016358402489055148, 0.015125155414584882, 0.013947772929280167, 0.012827911566761958, 0.01176665750551206, 0.010764561271088567, 0.00982167641856898, 0.008937601277212043, 0.00811152286192766, 0.00734226209496504, 0.006628319533989669, 0.005967920866984466, 0.00535906150767277, 0.00479954970491761, 0.004287047663374263, 0.003819110258265289, 0.0033932210123972066, 0.003006825086557508, 0.0026573591135838955, 0.0023422777803198446] + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1757172383199137058_q": {
            "samples": [0.0] * 100,
            "type": "arbitrary",
        },
        "-7377163761049853188_i": {
            "samples": [0.0023407540718299795, 0.002652283769664158, 0.00299746198332459, 0.0033787563544115645, 0.0037986524731640687, 0.004259628720537644, 0.004764128049941792, 0.005314526795062467, 0.005913100658053454, 0.006561988105067251, 0.007263151472393365, 0.008018336164919445, 0.008829028407540337, 0.009696412087621814, 0.010621325300621516, 0.011604217279296836, 0.012645106447333757, 0.013743540388445675, 0.01489855855980506, 0.01610865860199775, 0.017371767104643564, 0.018685215675796316, 0.020045723132955003, 0.021449384583134792, 0.022891668088580716, 0.024367419523501705, 0.025870876116356845, 0.02739568904301677, 0.02893495529041042, 0.030481258850476114, 0.03202672113332439, 0.03356306030992498, 0.035081659112196295, 0.036573640436263995, 0.03802994991724154, 0.0394414444756411, 0.040798985680890736, 0.04209353664069587, 0.04331626101013014, 0.04445862262494371, 0.04551248420266807, 0.04647020352505927, 0.04732472551790415, 0.04806966868005799, 0.04869940438277257, 0.04920912766202454, 0.049594918258907945, 0.049853790823621756] + [0.0499837333837949] * 2 + [0.049853790823621756, 0.049594918258907945, 0.04920912766202454, 0.04869940438277257, 0.04806966868005799, 0.04732472551790415, 0.04647020352505927, 0.04551248420266807, 0.04445862262494371, 0.04331626101013014, 0.04209353664069587, 0.040798985680890736, 0.0394414444756411, 0.03802994991724154, 0.036573640436263995, 0.035081659112196295, 0.03356306030992498, 0.03202672113332439, 0.030481258850476114, 0.02893495529041042, 0.02739568904301677, 0.025870876116356845, 0.024367419523501705, 0.022891668088580716, 0.021449384583134792, 0.020045723132955003, 0.018685215675796316, 0.017371767104643564, 0.01610865860199775, 0.01489855855980506, 0.013743540388445675, 0.012645106447333757, 0.011604217279296836, 0.010621325300621516, 0.009696412087621814, 0.008829028407540337, 0.008018336164919445, 0.007263151472393365, 0.006561988105067251, 0.005913100658053454, 0.005314526795062467, 0.004764128049941792, 0.004259628720537644, 0.0037986524731640687, 0.0033787563544115645, 0.00299746198332459, 0.002652283769664158, 0.0023407540718299795] + [0.0] * 2,
            "type": "arbitrary",
        },
        "-7377163761049853188_q": {
            "samples": [0.0] * 100,
            "type": "arbitrary",
        },
        "-4902209669630684111_i": {
            "samples": [0.0023392619497844816, 0.002647318761494563, 0.0029883113013304528, 0.003364632657872833, 0.0037786937356530425, 0.004232899431126499, 0.004729621927095248, 0.0052711711835988885, 0.005859762765638613, 0.006497483214903075, 0.007186253242839665, 0.007927789094654854, 0.008723562506622177, 0.009574759750733155, 0.010482240329397893, 0.011446495946626277, 0.012467610438864811, 0.013545221396378827, 0.014678484242745097, 0.015866039563750774, 0.017105984486043, 0.018395848898737684, 0.019732577286671354, 0.021112516901222664, 0.022531412933208747, 0.023984411272303413, 0.025466069339249494, 0.026970375361881335, 0.02849077633519044, 0.03002021476142527, 0.03155117411106762, 0.03307573278246873, 0.03458562617033715, 0.03607231628483439, 0.03752706819766106, 0.038941032433230265, 0.04030533227586364, 0.04161115483183768, 0.04284984457176395, 0.04401299798757799, 0.04509255793226413, 0.04608090617173868, 0.04697095266880169, 0.047756220139797384, 0.04843092247589471, 0.04899003570223589, 0.04942936025833958, 0.04974557352006636, 0.0499362716444125, 0.05, 0.0499362716444125, 0.04974557352006636, 0.04942936025833958, 0.04899003570223589, 0.04843092247589471, 0.047756220139797384, 0.04697095266880169, 0.04608090617173868, 0.04509255793226413, 0.04401299798757799, 0.04284984457176395, 0.04161115483183768, 0.04030533227586364, 0.038941032433230265, 0.03752706819766106, 0.03607231628483439, 0.03458562617033715, 0.03307573278246873, 0.03155117411106762, 0.03002021476142527, 0.02849077633519044, 0.026970375361881335, 0.025466069339249494, 0.023984411272303413, 0.022531412933208747, 0.021112516901222664, 0.019732577286671354, 0.018395848898737684, 0.017105984486043, 0.015866039563750774, 0.014678484242745097, 0.013545221396378827, 0.012467610438864811, 0.011446495946626277, 0.010482240329397893, 0.009574759750733155, 0.008723562506622177, 0.007927789094654854, 0.007186253242839665, 0.006497483214903075, 0.005859762765638613, 0.0052711711835988885, 0.004729621927095248, 0.004232899431126499, 0.0037786937356530425, 0.003364632657872833, 0.0029883113013304528, 0.002647318761494563, 0.0023392619497844816, 0.0],
            "type": "arbitrary",
        },
        "-4902209669630684111_q": {
            "samples": [0.0] * 100,
            "type": "arbitrary",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000.0)],
            "sine": [(-0.0, 2000.0)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000.0)],
            "sine": [(1.0, 2000.0)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(-0.0, 2000.0)],
            "sine": [(-1.0, 2000.0)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.2205,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.421,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.2095,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0725851073784813, -0.9529722265285006],
                        "feedback": [0.880387119150019],
                    },
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "7": {
                    "offset": -0.04,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
        },
        "con6": {
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
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 10,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
                "3": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
            },
        },
        "D2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 4),
            },
        },
        "D3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 5),
            },
        },
        "D4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 6),
            },
        },
        "D5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 7),
            },
        },
        "D1/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con6', 1),
                "out2": ('con6', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": -312363546.0,
            "operations": {
                "411307349810644873": "411307349810644873_D1/acquisition",
            },
            "mixInputs": {
                "I": ('con6', 1),
                "Q": ('con6', 2),
                "mixer": "D1/acquisition_mixer_8f5",
                "lo_frequency": 7450000000.0,
            },
        },
        "D1/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con6', 3),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": -141729925.0,
            "operations": {
                "6604363986927480387": "6604363986927480387",
                "7096592949341909951": "7096592949341909951",
                "-115720503467340412": "-115720503467340412",
                "-1263542320644209185": "-1263542320644209185",
                "5117489313559423934": "5117489313559423934",
                "-8709403317967044306": "-8709403317967044306",
                "1155711426557672926": "1155711426557672926",
                "7536743060761306045": "7536743060761306045",
                "6388921243584437272": "6388921243584437272",
                "-1278433812937113097": "-1278433812937113097",
                "4285857220696316067": "4285857220696316067",
                "8808174990786319383": "8808174990786319383",
                "1140819934264769014": "1140819934264769014",
                "6995355519178226904": "6995355519178226904",
                "4670797437091390451": "4670797437091390451",
                "9193115207181393767": "9193115207181393767",
                "-9032134807329442601": "-9032134807329442601",
                "6219423770532406003": "6219423770532406003",
                "4185110239725598276": "4185110239725598276",
                "4018826075551204738": "4018826075551204738",
                "-1601165302299511392": "-1601165302299511392",
                "8030401897711621082": "8030401897711621082",
                "-1755771283058638749": "-1755771283058638749",
                "9023617734129362498": "9023617734129362498",
                "3477438533968125597": "3477438533968125597",
                "-4189916522553424772": "-4189916522553424772",
                "5675198221971292460": "5675198221971292460",
                "5896692281170007708": "5896692281170007708",
                "-7538336034711494810": "-7538336034711494810",
                "-2918484592528411434": "-2918484592528411434",
                "1759314727475078776": "1759314727475078776",
                "-5119082287509612699": "-5119082287509612699",
                "-4897588228310897451": "-4897588228310897451",
                "-2533544376133337050": "-2533544376133337050",
                "3030746657500092114": "3030746657500092114",
                "-4636608399021458255": "-4636608399021458255",
                "-114290628931454939": "-114290628931454939",
                "107203430267260309": "107203430267260309",
                "-7985027911179528293": "-7985027911179528293",
                "-7763533851980813045": "-7763533851980813045",
                "7316678876098476270": "7316678876098476270",
                "7538172935297191518": "7538172935297191518",
                "-7101399232169736447": "-7101399232169736447",
                "-7378593635585738661": "-7378593635585738661",
                "2985209571553696033": "2985209571553696033",
                "-3477601633382428889": "-3477601633382428889",
                "-5829967302144723109": "-5829967302144723109",
                "6609007170341003591": "6609007170341003591",
                "-3632207614141556246": "-3632207614141556246",
                "-2078495740119386424": "-2078495740119386424",
                "1601002202885208100": "1601002202885208100",
                "119263947883780439": "119263947883780439",
                "7215441445934793223": "7215441445934793223",
                "4020255950087090211": "4020255950087090211",
                "-8474418866615923455": "-8474418866615923455",
                "7550233452913711648": "7550233452913711648",
                "7771727512112426896": "7771727512112426896",
                "4405196166482164595": "4405196166482164595",
                "4626690225680879843": "4626690225680879843",
                "1775636094303868161": "1775636094303868161",
                "1154310326417174617": "1154310326417174617",
                "1375804385615889865": "1375804385615889865",
                "-6389084342998740564": "-6389084342998740564",
                "3573564073619056728": "3573564073619056728",
                "-9018644415177036998": "-9018644415177036998",
                "1760744602010964249": "1760744602010964249",
                "-5117652412973727226": "-5117652412973727226",
                "5661736604214274021": "5661736604214274021",
                "4179998349212846360": "4179998349212846360",
                "-1366180850948390541": "-1366180850948390541",
                "1108773240470778536": "1108773240470778536",
                "-4511218137379937594": "-4511218137379937594",
                "-6835776219466774047": "-6835776219466774047",
                "-2313458449376770731": "-2313458449376770731",
                "-7762103977444927572": "-7762103977444927572",
                "-3954932071202303921": "-3954932071202303921",
                "8484042401283422779": "8484042401283422779",
                "-1757172383199137058": "-1757172383199137058",
                "-7377163761049853188": "-7377163761049853188",
                "-4902209669630684111": "-4902209669630684111",
            },
            "mixInputs": {
                "I": ('con6', 3),
                "Q": ('con6', 4),
                "mixer": "D1/drive_mixer_b94",
                "lo_frequency": 5100000000.0,
            },
        },
    },
    "pulses": {
        "6604363986927480387": {
            "length": 40,
            "waveforms": {
                "I": "6604363986927480387_i",
                "Q": "6604363986927480387_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "411307349810644873_D1/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "6980102099601109786_i",
                "Q": "6980102099601109786_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_D1/acquisition",
                "sin": "sine_weights_D1/acquisition",
                "minus_sin": "minus_sine_weights_D1/acquisition",
            },
            "operation": "measurement",
        },
        "7096592949341909951": {
            "length": 20,
            "waveforms": {
                "I": "7096592949341909951_i",
                "Q": "7096592949341909951_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-115720503467340412": {
            "length": 24,
            "waveforms": {
                "I": "-115720503467340412_i",
                "Q": "-115720503467340412_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1263542320644209185": {
            "length": 24,
            "waveforms": {
                "I": "-1263542320644209185_i",
                "Q": "-1263542320644209185_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5117489313559423934": {
            "length": 24,
            "waveforms": {
                "I": "5117489313559423934_i",
                "Q": "5117489313559423934_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8709403317967044306": {
            "length": 24,
            "waveforms": {
                "I": "-8709403317967044306_i",
                "Q": "-8709403317967044306_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1155711426557672926": {
            "length": 28,
            "waveforms": {
                "I": "1155711426557672926_i",
                "Q": "1155711426557672926_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7536743060761306045": {
            "length": 28,
            "waveforms": {
                "I": "7536743060761306045_i",
                "Q": "7536743060761306045_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6388921243584437272": {
            "length": 28,
            "waveforms": {
                "I": "6388921243584437272_i",
                "Q": "6388921243584437272_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1278433812937113097": {
            "length": 28,
            "waveforms": {
                "I": "-1278433812937113097_i",
                "Q": "-1278433812937113097_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4285857220696316067": {
            "length": 32,
            "waveforms": {
                "I": "4285857220696316067_i",
                "Q": "4285857220696316067_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8808174990786319383": {
            "length": 32,
            "waveforms": {
                "I": "8808174990786319383_i",
                "Q": "8808174990786319383_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1140819934264769014": {
            "length": 32,
            "waveforms": {
                "I": "1140819934264769014_i",
                "Q": "1140819934264769014_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6995355519178226904": {
            "length": 32,
            "waveforms": {
                "I": "6995355519178226904_i",
                "Q": "6995355519178226904_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4670797437091390451": {
            "length": 36,
            "waveforms": {
                "I": "4670797437091390451_i",
                "Q": "4670797437091390451_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9193115207181393767": {
            "length": 36,
            "waveforms": {
                "I": "9193115207181393767_i",
                "Q": "9193115207181393767_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9032134807329442601": {
            "length": 36,
            "waveforms": {
                "I": "-9032134807329442601_i",
                "Q": "-9032134807329442601_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6219423770532406003": {
            "length": 36,
            "waveforms": {
                "I": "6219423770532406003_i",
                "Q": "6219423770532406003_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4185110239725598276": {
            "length": 40,
            "waveforms": {
                "I": "4185110239725598276_i",
                "Q": "4185110239725598276_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4018826075551204738": {
            "length": 40,
            "waveforms": {
                "I": "4018826075551204738_i",
                "Q": "4018826075551204738_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1601165302299511392": {
            "length": 40,
            "waveforms": {
                "I": "-1601165302299511392_i",
                "Q": "-1601165302299511392_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8030401897711621082": {
            "length": 44,
            "waveforms": {
                "I": "8030401897711621082_i",
                "Q": "8030401897711621082_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1755771283058638749": {
            "length": 44,
            "waveforms": {
                "I": "-1755771283058638749_i",
                "Q": "-1755771283058638749_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9023617734129362498": {
            "length": 44,
            "waveforms": {
                "I": "9023617734129362498_i",
                "Q": "9023617734129362498_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3477438533968125597": {
            "length": 44,
            "waveforms": {
                "I": "3477438533968125597_i",
                "Q": "3477438533968125597_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4189916522553424772": {
            "length": 48,
            "waveforms": {
                "I": "-4189916522553424772_i",
                "Q": "-4189916522553424772_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5675198221971292460": {
            "length": 48,
            "waveforms": {
                "I": "5675198221971292460_i",
                "Q": "5675198221971292460_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5896692281170007708": {
            "length": 48,
            "waveforms": {
                "I": "5896692281170007708_i",
                "Q": "5896692281170007708_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7538336034711494810": {
            "length": 48,
            "waveforms": {
                "I": "-7538336034711494810_i",
                "Q": "-7538336034711494810_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2918484592528411434": {
            "length": 52,
            "waveforms": {
                "I": "-2918484592528411434_i",
                "Q": "-2918484592528411434_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1759314727475078776": {
            "length": 52,
            "waveforms": {
                "I": "1759314727475078776_i",
                "Q": "1759314727475078776_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5119082287509612699": {
            "length": 52,
            "waveforms": {
                "I": "-5119082287509612699_i",
                "Q": "-5119082287509612699_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4897588228310897451": {
            "length": 52,
            "waveforms": {
                "I": "-4897588228310897451_i",
                "Q": "-4897588228310897451_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2533544376133337050": {
            "length": 56,
            "waveforms": {
                "I": "-2533544376133337050_i",
                "Q": "-2533544376133337050_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3030746657500092114": {
            "length": 56,
            "waveforms": {
                "I": "3030746657500092114_i",
                "Q": "3030746657500092114_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4636608399021458255": {
            "length": 56,
            "waveforms": {
                "I": "-4636608399021458255_i",
                "Q": "-4636608399021458255_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-114290628931454939": {
            "length": 56,
            "waveforms": {
                "I": "-114290628931454939_i",
                "Q": "-114290628931454939_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "107203430267260309": {
            "length": 60,
            "waveforms": {
                "I": "107203430267260309_i",
                "Q": "107203430267260309_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7985027911179528293": {
            "length": 60,
            "waveforms": {
                "I": "-7985027911179528293_i",
                "Q": "-7985027911179528293_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7763533851980813045": {
            "length": 60,
            "waveforms": {
                "I": "-7763533851980813045_i",
                "Q": "-7763533851980813045_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7316678876098476270": {
            "length": 60,
            "waveforms": {
                "I": "7316678876098476270_i",
                "Q": "7316678876098476270_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7538172935297191518": {
            "length": 64,
            "waveforms": {
                "I": "7538172935297191518_i",
                "Q": "7538172935297191518_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7101399232169736447": {
            "length": 64,
            "waveforms": {
                "I": "-7101399232169736447_i",
                "Q": "-7101399232169736447_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7378593635585738661": {
            "length": 64,
            "waveforms": {
                "I": "-7378593635585738661_i",
                "Q": "-7378593635585738661_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2985209571553696033": {
            "length": 64,
            "waveforms": {
                "I": "2985209571553696033_i",
                "Q": "2985209571553696033_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3477601633382428889": {
            "length": 68,
            "waveforms": {
                "I": "-3477601633382428889_i",
                "Q": "-3477601633382428889_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5829967302144723109": {
            "length": 68,
            "waveforms": {
                "I": "-5829967302144723109_i",
                "Q": "-5829967302144723109_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6609007170341003591": {
            "length": 68,
            "waveforms": {
                "I": "6609007170341003591_i",
                "Q": "6609007170341003591_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3632207614141556246": {
            "length": 68,
            "waveforms": {
                "I": "-3632207614141556246_i",
                "Q": "-3632207614141556246_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2078495740119386424": {
            "length": 72,
            "waveforms": {
                "I": "-2078495740119386424_i",
                "Q": "-2078495740119386424_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1601002202885208100": {
            "length": 72,
            "waveforms": {
                "I": "1601002202885208100_i",
                "Q": "1601002202885208100_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "119263947883780439": {
            "length": 72,
            "waveforms": {
                "I": "119263947883780439_i",
                "Q": "119263947883780439_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7215441445934793223": {
            "length": 72,
            "waveforms": {
                "I": "7215441445934793223_i",
                "Q": "7215441445934793223_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4020255950087090211": {
            "length": 76,
            "waveforms": {
                "I": "4020255950087090211_i",
                "Q": "4020255950087090211_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8474418866615923455": {
            "length": 76,
            "waveforms": {
                "I": "-8474418866615923455_i",
                "Q": "-8474418866615923455_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7550233452913711648": {
            "length": 76,
            "waveforms": {
                "I": "7550233452913711648_i",
                "Q": "7550233452913711648_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7771727512112426896": {
            "length": 76,
            "waveforms": {
                "I": "7771727512112426896_i",
                "Q": "7771727512112426896_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4405196166482164595": {
            "length": 80,
            "waveforms": {
                "I": "4405196166482164595_i",
                "Q": "4405196166482164595_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4626690225680879843": {
            "length": 80,
            "waveforms": {
                "I": "4626690225680879843_i",
                "Q": "4626690225680879843_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1775636094303868161": {
            "length": 80,
            "waveforms": {
                "I": "1775636094303868161_i",
                "Q": "1775636094303868161_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1154310326417174617": {
            "length": 80,
            "waveforms": {
                "I": "1154310326417174617_i",
                "Q": "1154310326417174617_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1375804385615889865": {
            "length": 84,
            "waveforms": {
                "I": "1375804385615889865_i",
                "Q": "1375804385615889865_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6389084342998740564": {
            "length": 84,
            "waveforms": {
                "I": "-6389084342998740564_i",
                "Q": "-6389084342998740564_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3573564073619056728": {
            "length": 84,
            "waveforms": {
                "I": "3573564073619056728_i",
                "Q": "3573564073619056728_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-9018644415177036998": {
            "length": 84,
            "waveforms": {
                "I": "-9018644415177036998_i",
                "Q": "-9018644415177036998_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1760744602010964249": {
            "length": 88,
            "waveforms": {
                "I": "1760744602010964249_i",
                "Q": "1760744602010964249_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5117652412973727226": {
            "length": 88,
            "waveforms": {
                "I": "-5117652412973727226_i",
                "Q": "-5117652412973727226_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5661736604214274021": {
            "length": 88,
            "waveforms": {
                "I": "5661736604214274021_i",
                "Q": "5661736604214274021_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4179998349212846360": {
            "length": 88,
            "waveforms": {
                "I": "4179998349212846360_i",
                "Q": "4179998349212846360_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1366180850948390541": {
            "length": 92,
            "waveforms": {
                "I": "-1366180850948390541_i",
                "Q": "-1366180850948390541_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1108773240470778536": {
            "length": 92,
            "waveforms": {
                "I": "1108773240470778536_i",
                "Q": "1108773240470778536_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4511218137379937594": {
            "length": 92,
            "waveforms": {
                "I": "-4511218137379937594_i",
                "Q": "-4511218137379937594_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6835776219466774047": {
            "length": 92,
            "waveforms": {
                "I": "-6835776219466774047_i",
                "Q": "-6835776219466774047_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-2313458449376770731": {
            "length": 96,
            "waveforms": {
                "I": "-2313458449376770731_i",
                "Q": "-2313458449376770731_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7762103977444927572": {
            "length": 96,
            "waveforms": {
                "I": "-7762103977444927572_i",
                "Q": "-7762103977444927572_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-3954932071202303921": {
            "length": 96,
            "waveforms": {
                "I": "-3954932071202303921_i",
                "Q": "-3954932071202303921_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8484042401283422779": {
            "length": 96,
            "waveforms": {
                "I": "8484042401283422779_i",
                "Q": "8484042401283422779_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1757172383199137058": {
            "length": 100,
            "waveforms": {
                "I": "-1757172383199137058_i",
                "Q": "-1757172383199137058_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7377163761049853188": {
            "length": 100,
            "waveforms": {
                "I": "-7377163761049853188_i",
                "Q": "-7377163761049853188_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4902209669630684111": {
            "length": 100,
            "waveforms": {
                "I": "-4902209669630684111_i",
                "Q": "-4902209669630684111_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "6604363986927480387_i": {
            "samples": [0.0025633625185328877, 0.0034493812958619704, 0.004569687767802362, 0.005959996420132366, 0.007652786886817909, 0.009674029080352337, 0.01203952371361243, 0.014751132808722143, 0.01779326260710692, 0.021130022161159442, 0.02470349867658192, 0.028433552685933602, 0.032219436241259766, 0.03594337848545879, 0.0394760784830394, 0.042683818067257386, 0.04543668781805351, 0.04761723999475882, 0.04912877344789502] + [0.04990243905537378] * 2 + [0.04912877344789502, 0.04761723999475882, 0.04543668781805351, 0.042683818067257386, 0.0394760784830394, 0.03594337848545879, 0.032219436241259766, 0.028433552685933602, 0.02470349867658192, 0.021130022161159442, 0.01779326260710692, 0.014751132808722143, 0.01203952371361243, 0.009674029080352337, 0.007652786886817909, 0.005959996420132366, 0.004569687767802362, 0.0034493812958619704, 0.0025633625185328877],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6604363986927480387_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6980102099601109786_i": {
            "sample": 0.0015,
            "type": "constant",
        },
        "6980102099601109786_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "7096592949341909951_i": {
            "samples": [0.0029793659380993043, 0.005228950064450073, 0.008621081194687642, 0.013352591761317168, 0.01942790637561821, 0.02655479955176726, 0.03409703755951741, 0.04112887811993324, 0.04660512461797638] + [0.04961089691301218] * 2 + [0.04660512461797638, 0.04112887811993324, 0.03409703755951741, 0.02655479955176726, 0.01942790637561821, 0.013352591761317168, 0.008621081194687642, 0.005228950064450073, 0.0029793659380993043],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7096592949341909951_q": {
            "samples": [0.0] * 20,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-115720503467340412_i": {
            "samples": [0.0029374912044815276, 0.0050334449886448905, 0.008149560900092273, 0.012467610438864811, 0.01802238942989105, 0.024616236003660263, 0.031769549438440174, 0.03874187144416247, 0.04464062507811166, 0.04860266351433041, 0.05, 0.04860266351433041, 0.04464062507811166, 0.03874187144416247, 0.031769549438440174, 0.024616236003660263, 0.01802238942989105, 0.012467610438864811, 0.008149560900092273, 0.0050334449886448905, 0.0029374912044815276] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-115720503467340412_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1263542320644209185_i": {
            "samples": [0.0028998450454134615, 0.0048607183156681895, 0.007737373288764629, 0.011696450294316233, 0.016791211928589855, 0.022891668088580716, 0.029637411586921195, 0.036439342850399604, 0.04254693060275435, 0.04717733097628471] + [0.049678209377909864] * 2 + [0.04717733097628471, 0.04254693060275435, 0.036439342850399604, 0.029637411586921195, 0.022891668088580716, 0.016791211928589855, 0.011696450294316233, 0.007737373288764629, 0.0048607183156681895, 0.0028998450454134615] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1263542320644209185_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5117489313559423934_i": {
            "samples": [0.002865820691614407, 0.0047071095929761666, 0.0073745460484814385, 0.011020263018688789, 0.015708123750690386, 0.02135661183854497, 0.027695938152648772, 0.03425906399134473, 0.04042132931542719, 0.0454905697855672, 0.048832375039166126, 0.05, 0.048832375039166126, 0.0454905697855672, 0.04042132931542719, 0.03425906399134473, 0.027695938152648772, 0.02135661183854497, 0.015708123750690386, 0.011020263018688789, 0.0073745460484814385, 0.0047071095929761666, 0.002865820691614407, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5117489313559423934_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8709403317967044306_i": {
            "samples": [0.002834921720190051, 0.0045696877678023645, 0.007053138240012856, 0.010423862595733963, 0.014751132808722145, 0.019988144541558575, 0.025934029627344382, 0.03221943624125977, 0.03832801119018458, 0.043658121514372, 0.04761723999475882] + [0.049729467169738945] * 2 + [0.04761723999475882, 0.043658121514372, 0.03832801119018458, 0.03221943624125977, 0.025934029627344382, 0.019988144541558575, 0.014751132808722145, 0.010423862595733963, 0.007053138240012856, 0.0045696877678023645, 0.002834921720190051],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8709403317967044306_q": {
            "samples": [0.0] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1155711426557672926_i": {
            "samples": [0.0028067381417066863, 0.004446080872969317, 0.0067667641618306355, 0.009894934954180734, 0.013901865022659707, 0.01876555494256998, 0.024337612797998585, 0.030326532985631673, 0.03630745185368455, 0.0417635105705636, 0.04615581731933179, 0.04900993366533776, 0.05, 0.04900993366533776, 0.04615581731933179, 0.0417635105705636, 0.03630745185368455, 0.030326532985631673, 0.024337612797998585, 0.01876555494256998, 0.013901865022659707, 0.009894934954180734, 0.0067667641618306355, 0.004446080872969317, 0.0028067381417066863] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1155711426557672926_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7536743060761306045_i": {
            "samples": [0.0027809284304838883, 0.004334350716624308, 0.006510241522248106, 0.009423429055037943, 0.013144971336512882, 0.017670512074329035, 0.022891668088580716, 0.028578837505011535, 0.03438353235519167, 0.03986531841436178, 0.04454293158439271, 0.04796242902846769] + [0.0497693943770712] * 2 + [0.04796242902846769, 0.04454293158439271, 0.03986531841436178, 0.03438353235519167, 0.028578837505011535, 0.022891668088580716, 0.017670512074329035, 0.013144971336512882, 0.009423429055037943, 0.006510241522248106, 0.004334350716624308, 0.0027809284304838883] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7536743060761306045_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6388921243584437272_i": {
            "samples": [0.0027572058474173962, 0.004232899431126499, 0.006279328577150272, 0.009001087153051165, 0.012467610438864815, 0.01668698902458154, 0.021581381200937142, 0.026970375361881335, 0.03256876158151036, 0.03800336023035619, 0.04284984457176395, 0.04668560624918924, 0.049149969646391525, 0.05, 0.049149969646391525, 0.04668560624918924, 0.04284984457176395, 0.03800336023035619, 0.03256876158151036, 0.026970375361881335, 0.021581381200937142, 0.01668698902458154, 0.012467610438864815, 0.009001087153051165, 0.006279328577150272, 0.004232899431126499, 0.0027572058474173962, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6388921243584437272_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1278433812937113097_i": {
            "samples": [0.002735327907539154, 0.00414039890922729, 0.0060705256497609345, 0.008621081194687644, 0.0118590116629278, 0.015801073051313504, 0.0203927591289532, 0.025492752061941737, 0.03086802040111313, 0.03620363343834905, 0.04112887811993324, 0.04525774296401605, 0.048238105580975396] + [0.04980109820219597] * 2 + [0.048238105580975396, 0.04525774296401605, 0.04112887811993324, 0.03620363343834905, 0.03086802040111313, 0.025492752061941737, 0.0203927591289532, 0.015801073051313504, 0.0118590116629278, 0.008621081194687644, 0.0060705256497609345, 0.00414039890922729, 0.002735327907539154],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1278433812937113097_q": {
            "samples": [0.0] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4285857220696316067_i": {
            "samples": [0.0027150881816862906, 0.004055736906838736, 0.005880923748526811, 0.008277730066572073, 0.01131011211301379, 0.015000733581042909, 0.019312923664813176, 0.02413645521624202, 0.02928120130671888, 0.03448214158408967, 0.03941753929454081, 0.0437395918177791, 0.047113989472523654, 0.04926233274822752, 0.05, 0.04926233274822752, 0.047113989472523654, 0.0437395918177791, 0.03941753929454081, 0.03448214158408967, 0.02928120130671888, 0.02413645521624202, 0.019312923664813176, 0.015000733581042909, 0.01131011211301379, 0.008277730066572073, 0.005880923748526811, 0.004055736906838736, 0.0027150881816862906] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4285857220696316067_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8808174990786319383_i": {
            "samples": [0.002696309851531143, 0.003977975435911384, 0.005708088000484348, 0.007966278536960766, 0.010813258341494367, 0.014275585681915955, 0.01833021485368369, 0.022891668088580716, 0.027805044188660435, 0.032847778482463424, 0.03774198009945037, 0.04217738245321173, 0.04584276778660145, 0.04846166172381721] + [0.04982668994851846] * 2 + [0.04846166172381721, 0.04584276778660145, 0.04217738245321173, 0.03774198009945037, 0.032847778482463424, 0.027805044188660435, 0.022891668088580716, 0.01833021485368369, 0.014275585681915955, 0.010813258341494367, 0.007966278536960766, 0.005708088000484348, 0.003977975435911384, 0.002696309851531143] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8808174990786319383_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1140819934264769014_i": {
            "samples": [0.0026788405963976483, 0.00390631832647667, 0.005549967079187939, 0.007682723433531037, 0.010361962318306845, 0.01361666755014075, 0.01743418606418866, 0.021748761738846677, 0.026434397179580627, 0.031304466235011576, 0.03611978959808223, 0.040605619167156784, 0.0444763438397427, 0.047465060364983394, 0.049353847252378576, 0.05, 0.049353847252378576, 0.047465060364983394, 0.0444763438397427, 0.040605619167156784, 0.03611978959808223, 0.031304466235011576, 0.026434397179580627, 0.021748761738846677, 0.01743418606418866, 0.01361666755014075, 0.010361962318306845, 0.007682723433531037, 0.005549967079187939, 0.00390631832647667, 0.0026788405963976483, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1140819934264769014_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6995355519178226904_i": {
            "samples": [0.0026625485020862942, 0.003840085704057873, 0.005404822227200863, 0.007423676150889755, 0.00995070221065691, 0.013016240019842008, 0.016615540549723397, 0.020698577903878936, 0.02516307136256083, 0.029852719317876128, 0.034562190004558964, 0.03904952149711631, 0.04305536616140598, 0.04632719066581175, 0.04864539678371839] + [0.04984764470335167] * 2 + [0.04864539678371839, 0.04632719066581175, 0.04305536616140598, 0.03904952149711631, 0.034562190004558964, 0.029852719317876128, 0.02516307136256083, 0.020698577903878936, 0.016615540549723397, 0.013016240019842008, 0.00995070221065691, 0.007423676150889755, 0.005404822227200863, 0.003840085704057873, 0.0026625485020862942],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6995355519178226904_q": {
            "samples": [0.0] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4670797437091390451_i": {
            "samples": [0.002647318761494564, 0.0037786937356530438, 0.0052711711835988885, 0.007186253242839668, 0.009574759750733157, 0.012467610438864815, 0.015866039563750777, 0.019732577286671354, 0.023984411272303417, 0.02849077633519044, 0.03307573278246874, 0.037527068197661065, 0.04161115483183768, 0.04509255793226413, 0.047756220139797384, 0.04942936025833958, 0.05, 0.04942936025833958, 0.047756220139797384, 0.04509255793226413, 0.04161115483183768, 0.037527068197661065, 0.03307573278246874, 0.02849077633519044, 0.023984411272303417, 0.019732577286671354, 0.015866039563750777, 0.012467610438864815, 0.009574759750733157, 0.007186253242839668, 0.0052711711835988885, 0.0037786937356530438, 0.002647318761494564] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4670797437091390451_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9193115207181393767_i": {
            "samples": [0.0026330509941431624, 0.00372163842775093, 0.00514774354755709, 0.006967988844909425, 0.009230087303692295, 0.011964980338316566, 0.015178399800876406, 0.018842902677797573, 0.022891668088580716, 0.027215410790795848, 0.03166359091122766, 0.03605066299559501, 0.04016744101475299, 0.043796851566868016, 0.04673254539564545, 0.048798199693554] + [0.049865018169666556] * 2 + [0.048798199693554, 0.04673254539564545, 0.043796851566868016, 0.04016744101475299, 0.03605066299559501, 0.03166359091122766, 0.027215410790795848, 0.022891668088580716, 0.018842902677797573, 0.015178399800876406, 0.011964980338316566, 0.009230087303692295, 0.006967988844909425, 0.00514774354755709, 0.00372163842775093, 0.0026330509941431624] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9193115207181393767_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9032134807329442601_i": {
            "samples": [0.002619657053491279, 0.0036684825684191453, 0.005033444988644889, 0.0067667641618306355, 0.008913198979252397, 0.011503314949690454, 0.01454619035230741, 0.01802238942989105, 0.02187823688501346, 0.026022506051035107, 0.030326532985631673, 0.03462846621025988, 0.03874187144416247, 0.04246829082841563, 0.045612703841427266, 0.04800027206427389, 0.049492390168936695, 0.05, 0.049492390168936695, 0.04800027206427389, 0.045612703841427266, 0.04246829082841563, 0.03874187144416247, 0.03462846621025988, 0.030326532985631673, 0.026022506051035107, 0.02187823688501346, 0.01802238942989105, 0.01454619035230741, 0.011503314949690454, 0.008913198979252397, 0.0067667641618306355, 0.005033444988644889, 0.0036684825684191453, 0.002619657053491279, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9032134807329442601_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6219423770532406003_i": {
            "samples": [0.0026070592216907973, 0.003618845129261924, 0.004927328354199723, 0.006580750371340995, 0.008621081194687642, 0.011078232094900766, 0.013963734722897546, 0.017264544538571694, 0.020937800975694126, 0.024907458469635976, 0.029063650893670724, 0.03326544423074864, 0.0373472726742971, 0.04112887811993324, 0.044428048779768615, 0.04707496681601854, 0.048926619603661396] + [0.04987958196666021] * 2 + [0.048926619603661396, 0.04707496681601854, 0.044428048779768615, 0.04112887811993324, 0.0373472726742971, 0.03326544423074864, 0.029063650893670724, 0.024907458469635976, 0.020937800975694126, 0.017264544538571694, 0.013963734722897546, 0.011078232094900766, 0.008621081194687642, 0.006580750371340995, 0.004927328354199723, 0.003618845129261924, 0.0026070592216907973],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6219423770532406003_q": {
            "samples": [0.0] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4185110239725598276_i": {
            "samples": [0.002595188714316214, 0.0035723926069823626, 0.004828570193672211, 0.00640836213600811, 0.008351118985510775, 0.01068590789442151, 0.013426020649958657, 0.016563508097770987, 0.02006441339444917, 0.023865456128386947, 0.02787289896516111, 0.03196418761612999, 0.03599269207614192, 0.03979551414757587, 0.04320390857559339, 0.04605545592934736, 0.04820679546798823, 0.04954554031808842, 0.05, 0.04954554031808842, 0.04820679546798823, 0.04605545592934736, 0.04320390857559339, 0.03979551414757587, 0.03599269207614192, 0.03196418761612999, 0.02787289896516111, 0.023865456128386947, 0.02006441339444917, 0.016563508097770987, 0.013426020649958657, 0.01068590789442151, 0.008351118985510775, 0.00640836213600811, 0.004828570193672211, 0.0035723926069823626, 0.002595188714316214] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4185110239725598276_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4018826075551204738_i": {
            "samples": [0.0025839844347918545, 0.0035288319055661616, 0.004736451567412025, 0.006248219549812199, 0.00810103508668073, 0.010322996882226687, 0.012928618797500867, 0.015914005940229233, 0.01925253636976, 0.022891668088580716, 0.026751490193092954, 0.030725543211001523, 0.03468424227854721, 0.03848096052466252, 0.04196049935090567, 0.044969332689644585, 0.04736671750996184, 0.04903556536550464] + [0.049891910630579066] * 2 + [0.04903556536550464, 0.04736671750996184, 0.044969332689644585, 0.04196049935090567, 0.03848096052466252, 0.03468424227854721, 0.030725543211001523, 0.026751490193092954, 0.022891668088580716, 0.01925253636976, 0.015914005940229233, 0.012928618797500867, 0.010322996882226687, 0.00810103508668073, 0.006248219549812199, 0.004736451567412025, 0.0035288319055661616, 0.0025839844347918545] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4018826075551204738_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1601165302299511392_i": {
            "samples": [0.0025733919312547356, 0.0034879044506540796, 0.004650342266798705, 0.006099116828426824, 0.007868839394088365, 0.009986564358125815, 0.012467610438864815, 0.015311299002902122, 0.018497053221884698, 0.021981369650497184, 0.025696184865166883, 0.02954909888167482, 0.03342577839164012, 0.037194653106882324, 0.04071375797867211, 0.04383929521644875, 0.04643523325096258, 0.0483830669271807, 0.04959077001361501, 0.05, 0.04959077001361501, 0.0483830669271807, 0.04643523325096258, 0.04383929521644875, 0.04071375797867211, 0.037194653106882324, 0.03342577839164012, 0.02954909888167482, 0.025696184865166883, 0.021981369650497184, 0.018497053221884698, 0.015311299002902122, 0.012467610438864815, 0.009986564358125815, 0.007868839394088365, 0.006099116828426824, 0.004650342266798705, 0.0034879044506540796, 0.0025733919312547356, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1601165302299511392_q": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8030401897711621082_i": {
            "samples": [0.0025538525355706942, 0.003413059032581848, 0.004493998388012063, 0.005829927496599249, 0.007451342466791033, 0.009383114668586039, 0.011641277780761964, 0.01422968905446275, 0.01713686189403215, 0.02033332079828439, 0.0237698508919818, 0.027376992143041297, 0.03106605696782864, 0.03473182997641245, 0.03825694859923382, 0.041517779458262974, 0.04439141992821902, 0.046763292912681415, 0.048534690269203956, 0.049629576452366694, 0.05, 0.049629576452366694, 0.048534690269203956, 0.046763292912681415, 0.04439141992821902, 0.041517779458262974, 0.03825694859923382, 0.03473182997641245, 0.03106605696782864, 0.027376992143041297, 0.0237698508919818, 0.02033332079828439, 0.01713686189403215, 0.01422968905446275, 0.011641277780761964, 0.009383114668586039, 0.007451342466791033, 0.005829927496599249, 0.004493998388012063, 0.003413059032581848, 0.0025538525355706942] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8030401897711621082_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1755771283058638749_i": {
            "samples": [0.002544822714565668, 0.0033787563544115623, 0.004422840230134619, 0.005708088000484348, 0.007263151472393362, 0.009111808333139739, 0.011270134083719225, 0.013743540388445672, 0.016523924271883917, 0.019587220020940474, 0.022891668088580716, 0.02637710400819787, 0.029965519835388223, 0.03356306030992498, 0.037063491031181915, 0.04035302776569314, 0.04331626101013014, 0.04584276778660145, 0.04783389347182214, 0.04920912766202454] + [0.04991150131520572] * 2 + [0.04920912766202454, 0.04783389347182214, 0.04584276778660145, 0.04331626101013014, 0.04035302776569314, 0.037063491031181915, 0.03356306030992498, 0.029965519835388223, 0.02637710400819787, 0.022891668088580716, 0.019587220020940474, 0.016523924271883917, 0.013743540388445672, 0.011270134083719225, 0.009111808333139739, 0.007263151472393362, 0.005708088000484348, 0.004422840230134619, 0.0033787563544115623, 0.002544822714565668] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1755771283058638749_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9023617734129362498_i": {
            "samples": [0.0025362376427132847, 0.003346311157893433, 0.004355827581814801, 0.005593749595561242, 0.0070870148619200865, 0.008858325763205081, 0.01092365392653933, 0.013289608884202246, 0.015950872674240942, 0.01888794365518279, 0.022065455155220307, 0.02543133060094481, 0.02891700156978686, 0.0324388474295308, 0.035900917950228976, 0.039198881304570214, 0.04222501127025566, 0.04487390425974968, 0.04704851513012878, 0.048666035379217654, 0.04966311945686184, 0.05, 0.04966311945686184, 0.048666035379217654, 0.04704851513012878, 0.04487390425974968, 0.04222501127025566, 0.039198881304570214, 0.035900917950228976, 0.0324388474295308, 0.02891700156978686, 0.02543133060094481, 0.022065455155220307, 0.01888794365518279, 0.015950872674240942, 0.013289608884202246, 0.01092365392653933, 0.008858325763205081, 0.0070870148619200865, 0.005593749595561242, 0.004355827581814801, 0.003346311157893433, 0.0025362376427132847, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9023617734129362498_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3477438533968125597_i": {
            "samples": [0.002528065301096756, 0.003315578084938566, 0.004292616508838816, 0.005486264996632666, 0.006921868253627256, 0.008621081194687642, 0.010599661595717305, 0.01286512835538612, 0.015414452552352569, 0.0182319846055169, 0.02128784229029823, 0.024536985213698223, 0.02791917730239037, 0.03135998820850191, 0.03477290893057051, 0.0380625617037418, 0.04112887811993324, 0.04387201394036187, 0.046197676919354946, 0.04802247752716405, 0.0492788818578542] + [0.049919357457577904] * 2 + [0.0492788818578542, 0.04802247752716405, 0.046197676919354946, 0.04387201394036187, 0.04112887811993324, 0.0380625617037418, 0.03477290893057051, 0.03135998820850191, 0.02791917730239037, 0.024536985213698223, 0.02128784229029823, 0.0182319846055169, 0.015414452552352569, 0.01286512835538612, 0.010599661595717305, 0.008621081194687642, 0.006921868253627256, 0.005486264996632666, 0.004292616508838816, 0.003315578084938566, 0.002528065301096756],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3477438533968125597_q": {
            "samples": [0.0] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4189916522553424772_i": {
            "samples": [0.0025202766681376824, 0.003286426430826524, 0.004232899431126499, 0.005385057259501606, 0.0067667641618306355, 0.008398661837876681, 0.010296212321709937, 0.012467610438864811, 0.014911704809071079, 0.017616097749774847, 0.020555614525359374, 0.023691336319768205, 0.026970375361881335, 0.030326532985631673, 0.03368192276723634, 0.03694956481401544, 0.040036870145840404, 0.04284984457176395, 0.045297759555475485, 0.04729797344533827, 0.0487805490032423, 0.049692308666322065, 0.05, 0.049692308666322065, 0.0487805490032423, 0.04729797344533827, 0.045297759555475485, 0.04284984457176395, 0.040036870145840404, 0.03694956481401544, 0.03368192276723634, 0.030326532985631673, 0.026970375361881335, 0.023691336319768205, 0.020555614525359374, 0.017616097749774847, 0.014911704809071079, 0.012467610438864811, 0.010296212321709937, 0.008398661837876681, 0.0067667641618306355, 0.005385057259501606, 0.004232899431126499, 0.003286426430826524, 0.0025202766681376824] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4189916522553424772_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5675198221971292460_i": {
            "samples": [0.0025128453773136197, 0.0032587383562236866, 0.004176400511928773, 0.005289610692387379, 0.006620856890794367, 0.008189805979818993, 0.010011564444950933, 0.012094814247438324, 0.01443993970885866, 0.017037288538126784, 0.01986572863262788, 0.022891668088580716, 0.026068695758330287, 0.029337971899910803, 0.03262945308885559, 0.03586397493223743, 0.0389561448151963, 0.041817921443122526, 0.04436268616053358, 0.04650955119382207, 0.048187609703781206, 0.04933981775935761] + [0.04992621234479659] * 2 + [0.04933981775935761, 0.048187609703781206, 0.04650955119382207, 0.04436268616053358, 0.041817921443122526, 0.0389561448151963, 0.03586397493223743, 0.03262945308885559, 0.029337971899910803, 0.026068695758330287, 0.022891668088580716, 0.01986572863262788, 0.017037288538126784, 0.01443993970885866, 0.012094814247438324, 0.010011564444950933, 0.008189805979818993, 0.006620856890794367, 0.005289610692387379, 0.004176400511928773, 0.0032587383562236866, 0.0025128453773136197] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5675198221971292460_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5896692281170007708_i": {
            "samples": [0.002505747420680767, 0.003232407353173493, 0.004122871722965482, 0.005199463114343012, 0.006483389646379692, 0.007993384189019955, 0.009744155223568687, 0.011744719328074062, 0.01399671224223789, 0.01649279906832163, 0.019215321022246976, 0.022135322986878217, 0.025212100217203166, 0.028393382212441223, 0.031616236750950315, 0.03480872884620627, 0.03789231118721658, 0.040784859363710665, 0.04340420294214317, 0.04567194891451151, 0.047517353620476, 0.04888097830587432, 0.04971786555152947, 0.05, 0.04971786555152947, 0.04888097830587432, 0.047517353620476, 0.04567194891451151, 0.04340420294214317, 0.040784859363710665, 0.03789231118721658, 0.03480872884620627, 0.031616236750950315, 0.028393382212441223, 0.025212100217203166, 0.022135322986878217, 0.019215321022246976, 0.01649279906832163, 0.01399671224223789, 0.011744719328074062, 0.009744155223568687, 0.007993384189019955, 0.006483389646379692, 0.005199463114343012, 0.004122871722965482, 0.003232407353173493, 0.002505747420680767, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5896692281170007708_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7538336034711494810_i": {
            "samples": [0.0024989608912136954, 0.0032073369241662993, 0.004072089473848755, 0.005114199237242183, 0.006353683504536693, 0.007808383144148403, 0.009492579789532414, 0.011415501634023637, 0.013579799196179876, 0.015980092869922236, 0.018601709296872628, 0.021419730900866366, 0.02439848000030468, 0.02749154421167759, 0.030642422915499373, 0.03378583624377857, 0.03684969066555055, 0.03975764244109334, 0.0424321467043333, 0.044797831049628416, 0.04678499360112465, 0.048333001358751716, 0.04939335861570002] + [0.049932229130174324] * 2 + [0.04939335861570002, 0.048333001358751716, 0.04678499360112465, 0.044797831049628416, 0.0424321467043333, 0.03975764244109334, 0.03684969066555055, 0.03378583624377857, 0.030642422915499373, 0.02749154421167759, 0.02439848000030468, 0.021419730900866366, 0.018601709296872628, 0.015980092869922236, 0.013579799196179876, 0.011415501634023637, 0.009492579789532414, 0.007808383144148403, 0.006353683504536693, 0.005114199237242183, 0.004072089473848755, 0.0032073369241662993, 0.0024989608912136954],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7538336034711494810_q": {
            "samples": [0.0] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2918484592528411434_i": {
            "samples": [0.0024924657581652256, 0.003183439440717145, 0.0040238517145384095, 0.005033444988644893, 0.006231127939626965, 0.007633891686687384, 0.009255572824076668, 0.011105512215226277, 0.01318717803150054, 0.015496839242815317, 0.018022389429891057, 0.020742428174248848, 0.023625706442813293, 0.026631031924742005, 0.0297077096292436, 0.032796562677026964, 0.035831539713412984, 0.03874187144416247, 0.0414546930816414, 0.0438980062341342, 0.046003817393241046, 0.047711264761893184, 0.04896953397043469, 0.04974036822432454, 0.05, 0.04974036822432454, 0.04896953397043469, 0.047711264761893184, 0.046003817393241046, 0.0438980062341342, 0.0414546930816414, 0.03874187144416247, 0.035831539713412984, 0.032796562677026964, 0.0297077096292436, 0.026631031924742005, 0.023625706442813293, 0.020742428174248848, 0.018022389429891057, 0.015496839242815317, 0.01318717803150054, 0.011105512215226277, 0.009255572824076668, 0.007633891686687384, 0.006231127939626965, 0.005033444988644893, 0.0040238517145384095, 0.003183439440717145, 0.0024924657581652256] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2918484592528411434_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1759314727475078776_i": {
            "samples": [0.0024862436706174803, 0.0031606351537644428, 0.003977975435911384, 0.0049568626255373695, 0.006115172667345031, 0.007469088762520901, 0.0090319925809447, 0.010813258341494367, 0.01281700757075368, 0.015040897717863778, 0.017475030009987826, 0.020101069154732743, 0.022891668088580716, 0.025810283697274818, 0.028811453683589994, 0.03184158071858716, 0.03484023877480174, 0.03774198009945037, 0.04047858243339435, 0.04298163818012712, 0.0451853538936598, 0.047029403168217104, 0.04846166172381721, 0.049440652230561655] + [0.04993753904622905] * 2 + [0.049440652230561655, 0.04846166172381721, 0.047029403168217104, 0.0451853538936598, 0.04298163818012712, 0.04047858243339435, 0.03774198009945037, 0.03484023877480174, 0.03184158071858716, 0.028811453683589994, 0.025810283697274818, 0.022891668088580716, 0.020101069154732743, 0.017475030009987826, 0.015040897717863778, 0.01281700757075368, 0.010813258341494367, 0.0090319925809447, 0.007469088762520901, 0.006115172667345031, 0.0049568626255373695, 0.003977975435911384, 0.0031606351537644428, 0.0024862436706174803] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1759314727475078776_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5119082287509612699_i": {
            "samples": [0.002480277785184948, 0.003138851332956246, 0.003934294506670615, 0.004884146515280716, 0.006005320599092863, 0.00731323297148999, 0.008820806937035332, 0.010537386790920361, 0.012467610438864815, 0.01461030300988035, 0.016957464604601662, 0.019493432224073286, 0.02219429747269594, 0.025027656738345366, 0.027952758610452468, 0.030921094311865033, 0.0338774516165966, 0.03676142256396496, 0.03950932239356749, 0.04205644416788042, 0.044339543459319584, 0.04629942319064234, 0.04788347284235835, 0.049048010758336626, 0.04976028428422183, 0.05, 0.04976028428422183, 0.049048010758336626, 0.04788347284235835, 0.04629942319064234, 0.044339543459319584, 0.04205644416788042, 0.03950932239356749, 0.03676142256396496, 0.0338774516165966, 0.030921094311865033, 0.027952758610452468, 0.025027656738345366, 0.02219429747269594, 0.019493432224073286, 0.016957464604601662, 0.01461030300988035, 0.012467610438864815, 0.010537386790920361, 0.008820806937035332, 0.00731323297148999, 0.006005320599092863, 0.004884146515280716, 0.003934294506670615, 0.003138851332956246, 0.002480277785184948, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5119082287509612699_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4897588228310897451_i": {
            "samples": [0.0024745526144779677, 0.0031180215157491573, 0.0038926577954437624, 0.0048150194814180584, 0.005901121738979186, 0.007165653488865205, 0.008621081194687642, 0.01027666905775511, 0.012137457162314097, 0.01420325069309823, 0.016467683004473817, 0.01891742181236899, 0.021531589940250125, 0.024281468931423338, 0.0271305448545296, 0.030034940671922673, 0.03294425907324257, 0.03580283475869078, 0.03855136741231789, 0.04112887811993324, 0.04347490513629988, 0.04553183214190747, 0.047247225724038715, 0.048576050616129796, 0.049482632431129325] + [0.04994224861461563] * 2 + [0.049482632431129325, 0.048576050616129796, 0.047247225724038715, 0.04553183214190747, 0.04347490513629988, 0.04112887811993324, 0.03855136741231789, 0.03580283475869078, 0.03294425907324257, 0.030034940671922673, 0.0271305448545296, 0.024281468931423338, 0.021531589940250125, 0.01891742181236899, 0.016467683004473817, 0.01420325069309823, 0.012137457162314097, 0.01027666905775511, 0.008621081194687642, 0.007165653488865205, 0.005901121738979186, 0.0048150194814180584, 0.0038926577954437624, 0.0031180215157491573, 0.0024745526144779677],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4897588228310897451_q": {
            "samples": [0.0] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2533544376133337050_i": {
            "samples": [0.002469053893468293, 0.0030980848503909817, 0.0038529275355500612, 0.004749229629311066, 0.005802167882686558, 0.007025742160038183, 0.008431967398583791, 0.010029988257169727, 0.011825151813009735, 0.013818083730990761, 0.016003821895914795, 0.018371067533487658, 0.020901616369087942, 0.023570030562486313, 0.026343605463193056, 0.02918267348098945, 0.032041270834799136, 0.034868172390365236, 0.03760827645372948, 0.04020429688601301, 0.04259869615963446, 0.0447357720176497, 0.04656379418017178, 0.04803707773957508, 0.04911787770764392, 0.049777995215018286, 0.05, 0.049777995215018286, 0.04911787770764392, 0.04803707773957508, 0.04656379418017178, 0.0447357720176497, 0.04259869615963446, 0.04020429688601301, 0.03760827645372948, 0.034868172390365236, 0.032041270834799136, 0.02918267348098945, 0.026343605463193056, 0.023570030562486313, 0.020901616369087942, 0.018371067533487658, 0.016003821895914795, 0.013818083730990761, 0.011825151813009735, 0.010029988257169727, 0.008431967398583791, 0.007025742160038183, 0.005802167882686558, 0.004749229629311066, 0.0038529275355500612, 0.0030980848503909817, 0.002469053893468293] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2533544376133337050_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3030746657500092114_i": {
            "samples": [0.0024637684613389565, 0.0030789855194342714, 0.003814977896949741, 0.004686547580708139, 0.0057080880004843505, 0.006892946600839856, 0.008252694963685723, 0.009796327527285029, 0.011529419074498436, 0.013453279924025428, 0.015564155347705725, 0.01785252129982155, 0.02030253125392538, 0.022891668088580716, 0.02559065004276659, 0.028363630563060033, 0.03116871853280928, 0.03395882844516559, 0.03668285048442406, 0.039287109487906785, 0.04171706090895607, 0.04391915286411141, 0.04584276778660145, 0.04744214661345651, 0.04867819396531215, 0.04952006513485812] + [0.04994644502558085] * 2 + [0.04952006513485812, 0.04867819396531215, 0.04744214661345651, 0.04584276778660145, 0.04391915286411141, 0.04171706090895607, 0.039287109487906785, 0.03668285048442406, 0.03395882844516559, 0.03116871853280928, 0.028363630563060033, 0.02559065004276659, 0.022891668088580716, 0.02030253125392538, 0.01785252129982155, 0.015564155347705725, 0.013453279924025428, 0.011529419074498436, 0.009796327527285029, 0.008252694963685723, 0.006892946600839856, 0.0057080880004843505, 0.004686547580708139, 0.003814977896949741, 0.0030789855194342714, 0.0024637684613389565] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3030746657500092114_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4636608399021458255_i": {
            "samples": [0.0024586841567666735, 0.0030606722325465796, 0.0037786937356530403, 0.0046267640579210996, 0.005618544205628365, 0.0067667641618306355, 0.008082562439363497, 0.009574759750733151, 0.011249092606956727, 0.013107440292288157, 0.015147085381610621, 0.017360053061381487, 0.019732577286671354, 0.022244741643582158, 0.024870339233461276, 0.027576988724858215, 0.030326532985631673, 0.03307573278246873, 0.03577725161283505, 0.03838090980604428, 0.0408351678230042, 0.043088781570857826, 0.04509255793226413, 0.04680112789477074, 0.0481746487324534, 0.049180346376956396, 0.049793814725774925, 0.05, 0.049793814725774925, 0.049180346376956396, 0.0481746487324534, 0.04680112789477074, 0.04509255793226413, 0.043088781570857826, 0.0408351678230042, 0.03838090980604428, 0.03577725161283505, 0.03307573278246873, 0.030326532985631673, 0.027576988724858215, 0.024870339233461276, 0.022244741643582158, 0.019732577286671354, 0.017360053061381487, 0.015147085381610621, 0.013107440292288157, 0.011249092606956727, 0.009574759750733151, 0.008082562439363497, 0.0067667641618306355, 0.005618544205628365, 0.0046267640579210996, 0.0037786937356530403, 0.0030606722325465796, 0.0024586841567666735, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4636608399021458255_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-114290628931454939_i": {
            "samples": [0.0024537897248895976, 0.0030430977791321644, 0.00374396949560364, 0.0045696877678023645, 0.00553322822504619, 0.006646736636571679, 0.00792093025951564, 0.009364438438319222, 0.010983104590816887, 0.012779278378754054, 0.014751132808722145, 0.01689204565136944, 0.01919008731470583, 0.021627657634343687, 0.024181311542401607, 0.026821808016929113, 0.02951440808865742, 0.03221943624125977, 0.034893105801257755, 0.03748859364207801, 0.039957333701476555, 0.042250483553692236, 0.044320504763776566, 0.04612278711236404, 0.04761723999475882, 0.04876977209991802, 0.04955358326495435] + [0.049950200199334105] * 2 + [0.04955358326495435, 0.04876977209991802, 0.04761723999475882, 0.04612278711236404, 0.044320504763776566, 0.042250483553692236, 0.039957333701476555, 0.03748859364207801, 0.034893105801257755, 0.03221943624125977, 0.02951440808865742, 0.026821808016929113, 0.024181311542401607, 0.021627657634343687, 0.01919008731470583, 0.01689204565136944, 0.014751132808722145, 0.012779278378754054, 0.010983104590816887, 0.009364438438319222, 0.00792093025951564, 0.006646736636571679, 0.00553322822504619, 0.0045696877678023645, 0.00374396949560364, 0.0030430977791321644, 0.0024537897248895976],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-114290628931454939_q": {
            "samples": [0.0] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "107203430267260309_i": {
            "samples": [0.002449074734468069, 0.003026218632729593, 0.0037107082419621826, 0.00451514354356592, 0.00545185830217733, 0.0065324456120135314, 0.0077672143495752495, 0.009164589635859368, 0.010730476335068845, 0.012467610438864811, 0.014374928450381512, 0.016446989096126696, 0.01867348436054603, 0.021038877504485697, 0.023522204033027672, 0.026097067295826448, 0.02873185348777371, 0.031390181430008074, 0.034031591030898804, 0.03661246134614739, 0.03908713545344811, 0.04140921584263013, 0.0435329816781146, 0.045414869087599175, 0.04701494844438925, 0.048298329138143484, 0.049236423018361175, 0.04980800269394257, 0.05, 0.04980800269394257, 0.049236423018361175, 0.048298329138143484, 0.04701494844438925, 0.045414869087599175, 0.0435329816781146, 0.04140921584263013, 0.03908713545344811, 0.03661246134614739, 0.034031591030898804, 0.031390181430008074, 0.02873185348777371, 0.026097067295826448, 0.023522204033027672, 0.021038877504485697, 0.01867348436054603, 0.016446989096126696, 0.014374928450381512, 0.012467610438864811, 0.010730476335068845, 0.009164589635859368, 0.0077672143495752495, 0.0065324456120135314, 0.00545185830217733, 0.00451514354356592, 0.0037107082419621826, 0.003026218632729593, 0.002449074734468069] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "107203430267260309_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7985027911179528293_i": {
            "samples": [0.002444529503959828, 0.0030099946003556487, 0.003678820807955497, 0.004462970708996382, 0.005374176472612954, 0.006423508374335231, 0.007620880479333864, 0.008974504731932459, 0.010490309843998432, 0.012171346469777309, 0.01401720481627395, 0.016023474652747317, 0.018181280231104057, 0.020476923521937335, 0.02289166808858072, 0.02540169265110044, 0.02797823786233076, 0.030587962124624377, 0.03319351269519628, 0.03575430731481765, 0.03822750976446968, 0.04056917084761368, 0.04273549512668324, 0.044684184138528184, 0.04637579954635434, 0.0477750854025085, 0.04885218785845216, 0.049583713491734606] + [0.04995357388586044] * 2 + [0.049583713491734606, 0.04885218785845216, 0.0477750854025085, 0.04637579954635434, 0.044684184138528184, 0.04273549512668324, 0.04056917084761368, 0.03822750976446968, 0.03575430731481765, 0.03319351269519628, 0.030587962124624377, 0.02797823786233076, 0.02540169265110044, 0.02289166808858072, 0.020476923521937335, 0.018181280231104057, 0.016023474652747317, 0.01401720481627395, 0.012171346469777309, 0.010490309843998432, 0.008974504731932459, 0.007620880479333864, 0.006423508374335231, 0.005374176472612954, 0.004462970708996382, 0.003678820807955497, 0.0030099946003556487, 0.002444529503959828] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7985027911179528293_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7763533851980813045_i": {
            "samples": [0.0024401450354109566, 0.002994388510972589, 0.0036482250401508065, 0.004413021634991416, 0.005299946162158934, 0.006319574296332377, 0.0074814392659343365, 0.008793534059145854, 0.01026178024453872, 0.011889482025838508, 0.013676788279067962, 0.015620188765761498, 0.017712073123370822, 0.019940382269409286, 0.02228838123747092, 0.02473457999293026, 0.02725282436825054, 0.029812572961748746, 0.03237936785702951, 0.03491549769066371, 0.037380841408871684, 0.03973387060876707, 0.0419327783299803, 0.04393669324900831, 0.045706931104567, 0.047208230436611834, 0.048409917806535155, 0.04928694885197926, 0.04982077587508655, 0.05, 0.04982077587508655, 0.04928694885197926, 0.048409917806535155, 0.047208230436611834, 0.045706931104567, 0.04393669324900831, 0.0419327783299803, 0.03973387060876707, 0.037380841408871684, 0.03491549769066371, 0.03237936785702951, 0.029812572961748746, 0.02725282436825054, 0.02473457999293026, 0.02228838123747092, 0.019940382269409286, 0.017712073123370822, 0.015620188765761498, 0.013676788279067962, 0.011889482025838508, 0.01026178024453872, 0.008793534059145854, 0.0074814392659343365, 0.006319574296332377, 0.005299946162158934, 0.004413021634991416, 0.0036482250401508065, 0.002994388510972589, 0.0024401450354109566, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7763533851980813045_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7316678876098476270_i": {
            "samples": [0.002435912955215962, 0.0029793659380993043, 0.003618845129261924, 0.004365160462885511, 0.005228950064450073, 0.006220321643198391, 0.007348441744565965, 0.008621081194687642, 0.010044128984978123, 0.011621090763833554, 0.013352591761317168, 0.015235907079823315, 0.017264544538571694, 0.01942790637561821, 0.021711055840484977, 0.024094612871482846, 0.02655479955176726, 0.029063650893670724, 0.031589399850201996, 0.03409703755951741, 0.03654904107496654, 0.038906251703063124, 0.04112887811993324, 0.043177590254165926, 0.04501466309304222, 0.04660512461797638, 0.047917859432597715, 0.048926619603661396, 0.04961089691301218] + [0.049956616054783784] * 2 + [0.04961089691301218, 0.048926619603661396, 0.047917859432597715, 0.04660512461797638, 0.04501466309304222, 0.043177590254165926, 0.04112887811993324, 0.038906251703063124, 0.03654904107496654, 0.03409703755951741, 0.031589399850201996, 0.029063650893670724, 0.02655479955176726, 0.024094612871482846, 0.021711055840484977, 0.01942790637561821, 0.017264544538571694, 0.015235907079823315, 0.013352591761317168, 0.011621090763833554, 0.010044128984978123, 0.008621081194687642, 0.007348441744565965, 0.006220321643198391, 0.005228950064450073, 0.004365160462885511, 0.003618845129261924, 0.0029793659380993043, 0.002435912955215962],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7316678876098476270_q": {
            "samples": [0.0] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7538172935297191518_i": {
            "samples": [0.002431825460928962, 0.002964894952295667, 0.003590611015475533, 0.004319261972767974, 0.005160988261532103, 0.006125454742606967, 0.007221475435667583, 0.00845659787755376, 0.009836657724136656, 0.011365317661131394, 0.013043607933790552, 0.01486948860420408, 0.016837455742893862, 0.01893821491227217, 0.021158445286670047, 0.02348067641138794, 0.025883296837165577, 0.028340709670415954, 0.03082364454728654, 0.03329962886960136, 0.03573361363275896, 0.038088741218395256, 0.04032723457465495, 0.04241137976010234, 0.04430456738436634, 0.04597235350761083, 0.047383497459668834, 0.04851093310148842, 0.04933263143749993, 0.04983231620813549, 0.05, 0.04983231620813549, 0.04933263143749993, 0.04851093310148842, 0.047383497459668834, 0.04597235350761083, 0.04430456738436634, 0.04241137976010234, 0.04032723457465495, 0.038088741218395256, 0.03573361363275896, 0.03329962886960136, 0.03082364454728654, 0.028340709670415954, 0.025883296837165577, 0.02348067641138794, 0.021158445286670047, 0.01893821491227217, 0.016837455742893862, 0.01486948860420408, 0.013043607933790552, 0.011365317661131394, 0.009836657724136656, 0.00845659787755376, 0.007221475435667583, 0.006125454742606967, 0.005160988261532103, 0.004319261972767974, 0.003590611015475533, 0.002964894952295667, 0.002431825460928962] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7538172935297191518_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7101399232169736447_i": {
            "samples": [0.0024278752734174583, 0.00295094589984705, 0.0035634578588658616, 0.00427521057816669, 0.0050958765561137116, 0.006034701472665832, 0.007100160847091294, 0.008299579470046963, 0.009638722838079402, 0.011121372851145478, 0.012748902913080404, 0.014519870093967808, 0.016429643955280793, 0.018470092791889704, 0.0206293482201413, 0.022891668088580716, 0.025237415514640274, 0.027643168435256577, 0.030081969462450522, 0.032523720204316243, 0.03493571778167314, 0.0372833243527405, 0.0395307534268863, 0.04164195001851245, 0.04358153569152915, 0.045315784684656586, 0.04681359395070428, 0.04804740837396265, 0.04899406283097626, 0.04963550519216617] + [0.049959368755182615] * 2 + [0.04963550519216617, 0.04899406283097626, 0.04804740837396265, 0.04681359395070428, 0.045315784684656586, 0.04358153569152915, 0.04164195001851245, 0.0395307534268863, 0.0372833243527405, 0.03493571778167314, 0.032523720204316243, 0.030081969462450522, 0.027643168435256577, 0.025237415514640274, 0.022891668088580716, 0.0206293482201413, 0.018470092791889704, 0.016429643955280793, 0.014519870093967808, 0.012748902913080404, 0.011121372851145478, 0.009638722838079402, 0.008299579470046963, 0.007100160847091294, 0.006034701472665832, 0.0050958765561137116, 0.00427521057816669, 0.0035634578588658616, 0.00295094589984705, 0.0024278752734174583] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7101399232169736447_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7378593635585738661_i": {
            "samples": [0.0024240555937433345, 0.0029374912044815306, 0.0035373255667968647, 0.004232899431126501, 0.005033444988644893, 0.00594781102780247, 0.006984148357941575, 0.008149560900092277, 0.009449730478863508, 0.010888526022913963, 0.012467610438864817, 0.014186060689585282, 0.016040018397985235, 0.018022389429891057, 0.020122611218834442, 0.022326505947265, 0.024616236003660266, 0.02697037536188134, 0.029364106713896294, 0.031769549438440174, 0.0341562179881798, 0.036491604276097406, 0.03874187144416247, 0.040872640349731676, 0.04284984457176395, 0.04464062507811166, 0.046214232233282214, 0.04754290083264267, 0.04860266351433041, 0.049374069317750915, 0.049842777313575226, 0.05, 0.049842777313575226, 0.049374069317750915, 0.04860266351433041, 0.04754290083264267, 0.046214232233282214, 0.04464062507811166, 0.04284984457176395, 0.040872640349731676, 0.03874187144416247, 0.036491604276097406, 0.0341562179881798, 0.031769549438440174, 0.029364106713896294, 0.02697037536188134, 0.024616236003660266, 0.022326505947265, 0.020122611218834442, 0.018022389429891057, 0.016040018397985235, 0.014186060689585282, 0.012467610438864817, 0.010888526022913963, 0.009449730478863508, 0.008149560900092277, 0.006984148357941575, 0.00594781102780247, 0.005033444988644893, 0.004232899431126501, 0.0035373255667968647, 0.0029374912044815306, 0.0024240555937433345, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7378593635585738661_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2985209571553696033_i": {
            "samples": [0.0024203600642353114, 0.0029245051893809332, 0.003512158371335674, 0.00419222962395352, 0.0049735365161414635, 0.005864551928152404, 0.006873115437888062, 0.008006113028742408, 0.00926913212665601, 0.010666101334644774, 0.012198926506533684, 0.013867136839583492, 0.015667556310793418, 0.017594016877396354, 0.01963713026408038, 0.02178413474760476, 0.024018832039639535, 0.026321627123554223, 0.028669680738527593, 0.03103718020337501, 0.033395729573420456, 0.03571485492571769, 0.03796261512062647, 0.04010630297872012, 0.04211321674999914, 0.043951477347772244, 0.04559086336308615, 0.047003633617155295, 0.04816530613845629, 0.049055363081174, 0.0496578532580101] + [0.04996186757555894] * 2 + [0.0496578532580101, 0.049055363081174, 0.04816530613845629, 0.047003633617155295, 0.04559086336308615, 0.043951477347772244, 0.04211321674999914, 0.04010630297872012, 0.03796261512062647, 0.03571485492571769, 0.033395729573420456, 0.03103718020337501, 0.028669680738527593, 0.026321627123554223, 0.024018832039639535, 0.02178413474760476, 0.01963713026408038, 0.017594016877396354, 0.015667556310793418, 0.013867136839583492, 0.012198926506533684, 0.010666101334644774, 0.00926913212665601, 0.008006113028742408, 0.006873115437888062, 0.005864551928152404, 0.0049735365161414635, 0.00419222962395352, 0.003512158371335674, 0.0029245051893809332, 0.0024203600642353114],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2985209571553696033_q": {
            "samples": [0.0] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3477601633382428889_i": {
            "samples": [0.002416782733285445, 0.0029119639171118136, 0.0034879044506540783, 0.00415310947579437, 0.004916005832864119, 0.005784710242708293, 0.0067667641618306355, 0.007868839394088363, 0.0090964205827995, 0.010453472794458255, 0.01194210442824829, 0.013562237518211834, 0.015311299002902118, 0.017183947585848427, 0.01917185127328757, 0.02126353044627351, 0.023444280324158583, 0.02569618486516688, 0.027998231532400004, 0.030326532985631673, 0.032654657748492105, 0.03495406740548105, 0.037194653106882324, 0.03934535934058818, 0.04137487832891846, 0.04325239429324332, 0.04494835345640833, 0.04643523325096258, 0.04768828295300995, 0.04868620799024986, 0.049411771530654326, 0.049852289620141044, 0.05, 0.049852289620141044, 0.049411771530654326, 0.04868620799024986, 0.04768828295300995, 0.04643523325096258, 0.04494835345640833, 0.04325239429324332, 0.04137487832891846, 0.03934535934058818, 0.037194653106882324, 0.03495406740548105, 0.032654657748492105, 0.030326532985631673, 0.027998231532400004, 0.02569618486516688, 0.023444280324158583, 0.02126353044627351, 0.01917185127328757, 0.017183947585848427, 0.015311299002902118, 0.013562237518211834, 0.01194210442824829, 0.010453472794458255, 0.0090964205827995, 0.007868839394088363, 0.0067667641618306355, 0.005784710242708293, 0.004916005832864119, 0.00415310947579437, 0.0034879044506540783, 0.0029119639171118136, 0.002416782733285445] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3477601633382428889_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5829967302144723109_i": {
            "samples": [0.0024133180234607392, 0.0028998450454134628, 0.00346451558920456, 0.004115453893829434, 0.004860718315668192, 0.0057080880004843505, 0.006664818985020722, 0.007737373288764629, 0.008931126357051284, 0.010250060065080184, 0.011696450294316233, 0.013270559740947228, 0.014970347995637963, 0.016791211928589855, 0.018725769914081158, 0.02076370333904112, 0.02289166808858072, 0.025093287246301433, 0.027349234084497978, 0.029637411586921195, 0.03193323132661429, 0.03420999063895378, 0.036439342850399604, 0.038591851043963565, 0.04063761168275637, 0.04254693060275435, 0.04429103065045601, 0.04584276778660145, 0.04717733097628471, 0.04827290076478668, 0.0491112421665986, 0.049678209377909864] + [0.049964142799259675] * 2 + [0.049678209377909864, 0.0491112421665986, 0.04827290076478668, 0.04717733097628471, 0.04584276778660145, 0.04429103065045601, 0.04254693060275435, 0.04063761168275637, 0.038591851043963565, 0.036439342850399604, 0.03420999063895378, 0.03193323132661429, 0.029637411586921195, 0.027349234084497978, 0.025093287246301433, 0.02289166808858072, 0.02076370333904112, 0.018725769914081158, 0.016791211928589855, 0.014970347995637963, 0.013270559740947228, 0.011696450294316233, 0.010250060065080184, 0.008931126357051284, 0.007737373288764629, 0.006664818985020722, 0.0057080880004843505, 0.004860718315668192, 0.004115453893829434, 0.00346451558920456, 0.0028998450454134628, 0.0024133180234607392] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5829967302144723109_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6609007170341003591_i": {
            "samples": [0.002409960702571528, 0.0028881276970462895, 0.0034419468721474987, 0.004079183800229198, 0.004807549079145888, 0.005634501767364641, 0.006567024748239613, 0.007611375133453423, 0.008772814407308023, 0.010055324652747746, 0.011461318806597346, 0.012991354374124001, 0.01464386129321684, 0.016414895575980307, 0.018297930874598085, 0.02028370013450789, 0.02236009894512199, 0.024512161035382552, 0.026722114577887302, 0.028969525585645972, 0.03123153177148329, 0.033483166890683175, 0.03569777193628933, 0.037847485766526294, 0.03990380399967908, 0.04183819150978624, 0.043622730793235705, 0.04523078603633418, 0.046637661057344, 0.047821228547837324, 0.04876250827672761, 0.049446173172996724, 0.049860964440973855, 0.05, 0.049860964440973855, 0.049446173172996724, 0.04876250827672761, 0.047821228547837324, 0.046637661057344, 0.04523078603633418, 0.043622730793235705, 0.04183819150978624, 0.03990380399967908, 0.037847485766526294, 0.03569777193628933, 0.033483166890683175, 0.03123153177148329, 0.028969525585645972, 0.026722114577887302, 0.024512161035382552, 0.02236009894512199, 0.02028370013450789, 0.018297930874598085, 0.016414895575980307, 0.01464386129321684, 0.012991354374124001, 0.011461318806597346, 0.010055324652747746, 0.008772814407308023, 0.007611375133453423, 0.006567024748239613, 0.005634501767364641, 0.004807549079145888, 0.004079183800229198, 0.0034419468721474987, 0.0028881276970462895, 0.002409960702571528, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6609007170341003591_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3632207614141556246_i": {
            "samples": [0.0024067058573818425, 0.002876792342132161, 0.0034201564100956984, 0.004044225617191438, 0.004756382127650614, 0.005563781369226778, 0.006473144886509911, 0.007490530113344597, 0.008621081194687644, 0.009868766443995265, 0.011236109456194202, 0.012723922230419727, 0.014331049806499624, 0.016054136798034593, 0.01788742672933987, 0.019822605178684748, 0.021848697336027387, 0.02395202965988791, 0.026116263850466306, 0.02832250935902005, 0.030549518172714146, 0.03277396272735183, 0.03497079461551554, 0.037113678408998575, 0.03917549155671987, 0.04112887811993324, 0.0429468412361583, 0.044603356825750756, 0.046073989317072656, 0.0473364891874168, 0.04837135198105608, 0.049162319214457566, 0.04969680320656619] + [0.04996622032584039] * 2 + [0.04969680320656619, 0.049162319214457566, 0.04837135198105608, 0.0473364891874168, 0.046073989317072656, 0.044603356825750756, 0.0429468412361583, 0.04112887811993324, 0.03917549155671987, 0.037113678408998575, 0.03497079461551554, 0.03277396272735183, 0.030549518172714146, 0.02832250935902005, 0.026116263850466306, 0.02395202965988791, 0.021848697336027387, 0.019822605178684748, 0.01788742672933987, 0.016054136798034593, 0.014331049806499624, 0.012723922230419727, 0.011236109456194202, 0.009868766443995265, 0.008621081194687644, 0.007490530113344597, 0.006473144886509911, 0.005563781369226778, 0.004756382127650614, 0.004044225617191438, 0.0034201564100956984, 0.002876792342132161, 0.0024067058573818425],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3632207614141556246_q": {
            "samples": [0.0] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2078495740119386424_i": {
            "samples": [0.002403548869684607, 0.002865820691614407, 0.0033991050907472642, 0.0040105108033760715, 0.0047071095929761666, 0.005495768744439523, 0.006382959818160457, 0.0073745460484814385, 0.008475552020915043, 0.00968992055722552, 0.011020263018688789, 0.012467610438864815, 0.01403117394538493, 0.015708123750690386, 0.017493396511464265, 0.019379541009510785, 0.02135661183854497, 0.023412120053710055, 0.02553104853635789, 0.027695938152648772, 0.02988704867426442, 0.032082595943622026, 0.03425906399134473, 0.036391587860823076, 0.03845439989291418, 0.04042132931542719, 0.042266342314659915, 0.04396410748451649, 0.0454905697855672, 0.04682351501448994, 0.047943106368403154, 0.048832375039166126, 0.04947764790163084, 0.049868897238146144, 0.05, 0.049868897238146144, 0.04947764790163084, 0.048832375039166126, 0.047943106368403154, 0.04682351501448994, 0.0454905697855672, 0.04396410748451649, 0.042266342314659915, 0.04042132931542719, 0.03845439989291418, 0.036391587860823076, 0.03425906399134473, 0.032082595943622026, 0.02988704867426442, 0.027695938152648772, 0.02553104853635789, 0.023412120053710055, 0.02135661183854497, 0.019379541009510785, 0.017493396511464265, 0.015708123750690386, 0.01403117394538493, 0.012467610438864815, 0.011020263018688789, 0.00968992055722552, 0.008475552020915043, 0.0073745460484814385, 0.006382959818160457, 0.005495768744439523, 0.0047071095929761666, 0.0040105108033760715, 0.0033991050907472642, 0.002865820691614407, 0.002403548869684607] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2078495740119386424_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1601002202885208100_i": {
            "samples": [0.002400485394497352, 0.002855195600634447, 0.003378756354411561, 0.003977975435911384, 0.004659631047907215, 0.005430316910988311, 0.006296265493955797, 0.00726315147239336, 0.008335878618591175, 0.009518354479012657, 0.010813258341494367, 0.012221809076095859, 0.013743540388445672, 0.015376091787717117, 0.017115024079373757, 0.018953668387053993, 0.020883017539213667, 0.022891668088580716, 0.02496582024736544, 0.02708934161995265, 0.029243898821220887, 0.031409158929666676, 0.03356306030992498, 0.03568214973968598, 0.03774198009945037, 0.03971756025067383, 0.04158384626586692, 0.04331626101013014, 0.04489122732685822, 0.04628669885554552, 0.04748267188974292, 0.04846166172381721, 0.04920912766202454, 0.049713832261944445] + [0.04996812241102594] * 2 + [0.049713832261944445, 0.04920912766202454, 0.04846166172381721, 0.04748267188974292, 0.04628669885554552, 0.04489122732685822, 0.04331626101013014, 0.04158384626586692, 0.03971756025067383, 0.03774198009945037, 0.03568214973968598, 0.03356306030992498, 0.031409158929666676, 0.029243898821220887, 0.02708934161995265, 0.02496582024736544, 0.022891668088580716, 0.020883017539213667, 0.018953668387053993, 0.017115024079373757, 0.015376091787717117, 0.013743540388445672, 0.012221809076095859, 0.010813258341494367, 0.009518354479012657, 0.008335878618591175, 0.00726315147239336, 0.006296265493955797, 0.005430316910988311, 0.004659631047907215, 0.003977975435911384, 0.003378756354411561, 0.002855195600634447, 0.002400485394497352] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1601002202885208100_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "119263947883780439_i": {
            "samples": [0.0023975113401624457, 0.0028449009807679673, 0.0033590759908060266, 0.003946559832881187, 0.0046138528870977216, 0.005367289035338639, 0.0062128720885030585, 0.007156093896448765, 0.008201736968157385, 0.009353665457905674, 0.010614609399372732, 0.011985948044452004, 0.013467499033156036, 0.015057320829185861, 0.016751536346890437, 0.018544185917778053, 0.020427117654172263, 0.02238992283060589, 0.024419923100782986, 0.02650221519687987, 0.028619777234860047, 0.030753638910412964, 0.032883115770880496, 0.03498610546329214, 0.03703944147740068, 0.039019297527471145, 0.04090163345687087, 0.04266267151625229, 0.04427939016591169, 0.045730021281727276, 0.0469945358813685, 0.04805510329088511, 0.04889650907303556, 0.049506518040757966, 0.04987617025505978, 0.05, 0.04987617025505978, 0.049506518040757966, 0.04889650907303556, 0.04805510329088511, 0.0469945358813685, 0.045730021281727276, 0.04427939016591169, 0.04266267151625229, 0.04090163345687087, 0.039019297527471145, 0.03703944147740068, 0.03498610546329214, 0.032883115770880496, 0.030753638910412964, 0.028619777234860047, 0.02650221519687987, 0.024419923100782986, 0.02238992283060589, 0.020427117654172263, 0.018544185917778053, 0.016751536346890437, 0.015057320829185861, 0.013467499033156036, 0.011985948044452004, 0.010614609399372732, 0.009353665457905674, 0.008201736968157385, 0.007156093896448765, 0.0062128720885030585, 0.005367289035338639, 0.0046138528870977216, 0.003946559832881187, 0.0033590759908060266, 0.0028449009807679673, 0.0023975113401624457, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "119263947883780439_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7215441445934793223_i": {
            "samples": [0.0023946228501606362, 0.0028349217201900498, 0.00334003195482363, 0.003916208211836444, 0.004569687767802362, 0.005306557591749217, 0.006132602818318216, 0.007053138240012854, 0.008072825318239813, 0.009195478131102977, 0.010423862595733961, 0.011759494182001253, 0.013202440126173151, 0.014751132808722143, 0.01640220143134939, 0.01815032936882021, 0.01998814454155857, 0.021906149824206973, 0.023892699854184553, 0.025934029627344375, 0.028014338975640676, 0.030115935441649956, 0.03221943624125977, 0.03430402799942942, 0.03634778082948979, 0.03832801119018458, 0.04022168589028565, 0.04200585771482498, 0.043658121514372, 0.0451570783166006, 0.0464827941624143, 0.04761723999475882, 0.0485446990735277, 0.04925212906734522, 0.049729467169738945] + [0.049969868264962615] * 2 + [0.049729467169738945, 0.04925212906734522, 0.0485446990735277, 0.04761723999475882, 0.0464827941624143, 0.0451570783166006, 0.043658121514372, 0.04200585771482498, 0.04022168589028565, 0.03832801119018458, 0.03634778082948979, 0.03430402799942942, 0.03221943624125977, 0.030115935441649956, 0.028014338975640676, 0.025934029627344375, 0.023892699854184553, 0.021906149824206973, 0.01998814454155857, 0.01815032936882021, 0.01640220143134939, 0.014751132808722143, 0.013202440126173151, 0.011759494182001253, 0.010423862595733961, 0.009195478131102977, 0.008072825318239813, 0.007053138240012854, 0.006132602818318216, 0.005306557591749217, 0.004569687767802362, 0.003916208211836444, 0.00334003195482363, 0.0028349217201900498, 0.0023946228501606362],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7215441445934793223_q": {
            "samples": [0.0] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4020255950087090211_i": {
            "samples": [0.002391816286468386, 0.002825243610948521, 0.0033215941992491907, 0.0038868683804221408, 0.004527054103908085, 0.0052480036021318325, 0.006055292872816925, 0.0069540654088154534, 0.007948862388609255, 0.009043442361751145, 0.010240594288924036, 0.01154194858951179, 0.012947791570322002, 0.014456889214970445, 0.01606632676191024, 0.017771370749839012, 0.019565360226583672, 0.02143963357306465, 0.023383496868672304, 0.02538423891112007, 0.02742719690867722, 0.029495875506114155, 0.03157212022288823, 0.033636344622404654, 0.03566780865673102, 0.03764494371458435, 0.03954571802189338, 0.04134803428770198, 0.043030149937163614, 0.04457110900660239, 0.045951173862560896, 0.04715224440352183, 0.04815825234873114, 0.048955518632689946, 0.04953306280435922, 0.04988285465277764, 0.05, 0.04988285465277764, 0.04953306280435922, 0.048955518632689946, 0.04815825234873114, 0.04715224440352183, 0.045951173862560896, 0.04457110900660239, 0.043030149937163614, 0.04134803428770198, 0.03954571802189338, 0.03764494371458435, 0.03566780865673102, 0.033636344622404654, 0.03157212022288823, 0.029495875506114155, 0.02742719690867722, 0.02538423891112007, 0.023383496868672304, 0.02143963357306465, 0.019565360226583672, 0.017771370749839012, 0.01606632676191024, 0.014456889214970445, 0.012947791570322002, 0.01154194858951179, 0.010240594288924036, 0.009043442361751145, 0.007948862388609255, 0.0069540654088154534, 0.006055292872816925, 0.0052480036021318325, 0.004527054103908085, 0.0038868683804221408, 0.0033215941992491907, 0.002825243610948521, 0.002391816286468386] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4020255950087090211_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8474418866615923455_i": {
            "samples": [0.0023890882143082406, 0.002815853282620022, 0.0033037345226438275, 0.0038584914556833196, 0.004485875607510272, 0.005191515947754341, 0.005980788446132368, 0.006858671005965548, 0.007829585737254945, 0.008897231266792356, 0.010064408524271744, 0.01133284415962482, 0.01270301640293852, 0.014173988737419369, 0.015743257180722108, 0.017406617224934955, 0.019158056538685103, 0.020989679360104194, 0.022891668088580716, 0.024852286907872882, 0.026857931346046467, 0.028893226513865777, 0.030941175390385614, 0.03298335698263938, 0.03500017252695872, 0.03697113618372704, 0.038875204973662064, 0.04069114108470412, 0.042397898217736124, 0.043975022407256356, 0.045403056813649464, 0.04666393939043146, 0.04774138212280154, 0.048621220736860225, 0.04929172439775786, 0.049743855936678634] + [0.04997147453894671] * 2 + [0.049743855936678634, 0.04929172439775786, 0.048621220736860225, 0.04774138212280154, 0.04666393939043146, 0.045403056813649464, 0.043975022407256356, 0.042397898217736124, 0.04069114108470412, 0.038875204973662064, 0.03697113618372704, 0.03500017252695872, 0.03298335698263938, 0.030941175390385614, 0.028893226513865777, 0.026857931346046467, 0.024852286907872882, 0.022891668088580716, 0.020989679360104194, 0.019158056538685103, 0.017406617224934955, 0.015743257180722108, 0.014173988737419369, 0.01270301640293852, 0.01133284415962482, 0.010064408524271744, 0.008897231266792356, 0.007829585737254945, 0.006858671005965548, 0.005980788446132368, 0.005191515947754341, 0.004485875607510272, 0.0038584914556833196, 0.0033037345226438275, 0.002815853282620022, 0.0023890882143082406] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8474418866615923455_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7550233452913711648_i": {
            "samples": [0.002386435388158208, 0.0028067381417066863, 0.003286426430826524, 0.003831031609024675, 0.004446080872969317, 0.005136990745124717, 0.005908945859089028, 0.0067667641618306355, 0.007714750275078417, 0.008756539417257549, 0.009894934954180734, 0.011131743293944549, 0.012467610438864811, 0.013901865022659707, 0.01543237306183095, 0.0170554099048296, 0.01876555494256998, 0.020555614525359374, 0.022416578197047152, 0.024337612797998585, 0.026306098204672824, 0.02830770747585988, 0.030326532985631673, 0.03234525877321762, 0.03434537787286939, 0.03630745185368455, 0.038211408258574525, 0.040036870145840404, 0.0417635105705636, 0.043371423659170544, 0.04484150298734344, 0.04615581731933179, 0.04729797344533827, 0.04825345588948402, 0.04900993366533776, 0.049557525024414247, 0.04988901225428032, 0.05, 0.04988901225428032, 0.049557525024414247, 0.04900993366533776, 0.04825345588948402, 0.04729797344533827, 0.04615581731933179, 0.04484150298734344, 0.043371423659170544, 0.0417635105705636, 0.040036870145840404, 0.038211408258574525, 0.03630745185368455, 0.03434537787286939, 0.03234525877321762, 0.030326532985631673, 0.02830770747585988, 0.026306098204672824, 0.024337612797998585, 0.022416578197047152, 0.020555614525359374, 0.01876555494256998, 0.0170554099048296, 0.01543237306183095, 0.013901865022659707, 0.012467610438864811, 0.011131743293944549, 0.009894934954180734, 0.008756539417257549, 0.007714750275078417, 0.0067667641618306355, 0.005908945859089028, 0.005136990745124717, 0.004446080872969317, 0.003831031609024675, 0.003286426430826524, 0.0028067381417066863, 0.002386435388158208, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7550233452913711648_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7771727512112426896_i": {
            "samples": [0.0023838547389005323, 0.0027978863162037033, 0.0032696450105638808, 0.003804445834154376, 0.004407602998983276, 0.005084330779299037, 0.005839630761904705, 0.00667816647056171, 0.0076041269134938545, 0.008621081194687642, 0.009731826929995772, 0.010938235794364525, 0.012241100070511211, 0.013639984544023426, 0.01513308846652301, 0.016717122559419654, 0.018387206130354505, 0.02013678930103379, 0.021957605082488073, 0.023839655572363803, 0.025771235887146762, 0.027738998587590755, 0.029728060324811796, 0.03172215125364979, 0.03370380646408998, 0.03565459731383328, 0.03755539915504877, 0.03938669059000439, 0.04112887811993324, 0.04276263892503575, 0.044269273583694285, 0.045631059852667466, 0.0468315982256859, 0.04785613989325341, 0.04869188795686513, 0.0493282633079167, 0.049757127452727035] + [0.04997295572376939] * 2 + [0.049757127452727035, 0.0493282633079167, 0.04869188795686513, 0.04785613989325341, 0.0468315982256859, 0.045631059852667466, 0.044269273583694285, 0.04276263892503575, 0.04112887811993324, 0.03938669059000439, 0.03755539915504877, 0.03565459731383328, 0.03370380646408998, 0.03172215125364979, 0.029728060324811796, 0.027738998587590755, 0.025771235887146762, 0.023839655572363803, 0.021957605082488073, 0.02013678930103379, 0.018387206130354505, 0.016717122559419654, 0.01513308846652301, 0.013639984544023426, 0.012241100070511211, 0.010938235794364525, 0.009731826929995772, 0.008621081194687642, 0.0076041269134938545, 0.00667816647056171, 0.005839630761904705, 0.005084330779299037, 0.004407602998983276, 0.003804445834154376, 0.0032696450105638808, 0.0027978863162037033, 0.0023838547389005323],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7771727512112426896_q": {
            "samples": [0.0] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4405196166482164595_i": {
            "samples": [0.002381343362003121, 0.0027892866048317543, 0.0032533668142381844, 0.0037786937356530425, 0.004370379244734646, 0.0050334449886448905, 0.0057727174092799365, 0.006592711022417429, 0.007497501331800719, 0.008490589288978839, 0.009574759750733155, 0.010751936915644368, 0.012023040216887354, 0.013387844585182461, 0.014844849348858226, 0.016391160282601274, 0.018022389429891057, 0.019732577286671354, 0.021514141730269384, 0.023357857698380058, 0.02525287106526743, 0.027186749430930964, 0.029145571646634085, 0.031114056867874947, 0.03307573278246873, 0.03501314144295258, 0.0369080798810717, 0.03874187144416247, 0.04049566261786312, 0.04215073903618566, 0.04368885347606519, 0.04509255793226413, 0.04634553140659614, 0.04743289485090372, 0.04834150479385936, 0.04906021756373722, 0.049580116686908246, 0.04989469697675056, 0.05, 0.04989469697675056, 0.049580116686908246, 0.04906021756373722, 0.04834150479385936, 0.04743289485090372, 0.04634553140659614, 0.04509255793226413, 0.04368885347606519, 0.04215073903618566, 0.04049566261786312, 0.03874187144416247, 0.0369080798810717, 0.03501314144295258, 0.03307573278246873, 0.031114056867874947, 0.029145571646634085, 0.027186749430930964, 0.02525287106526743, 0.023357857698380058, 0.021514141730269384, 0.019732577286671354, 0.018022389429891057, 0.016391160282601274, 0.014844849348858226, 0.013387844585182461, 0.012023040216887354, 0.010751936915644368, 0.009574759750733155, 0.008490589288978839, 0.007497501331800719, 0.006592711022417429, 0.0057727174092799365, 0.0050334449886448905, 0.004370379244734646, 0.0037786937356530425, 0.0032533668142381844, 0.0027892866048317543, 0.002381343362003121] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4405196166482164595_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4626690225680879843_i": {
            "samples": [0.0023788985066381502, 0.0027809284304838883, 0.0032375697544028154, 0.003753737336079348, 0.004334350716624311, 0.004984247995779588, 0.0057080880004843505, 0.006510241522248109, 0.007394672852595283, 0.008364813324402726, 0.009423429055037947, 0.010572485566995856, 0.011813012413266466, 0.013144971336512885, 0.014567131821221753, 0.01607695813455482, 0.01767051207432904, 0.01934237563356426, 0.021085597636209694, 0.022891668088580716, 0.02475052352197671, 0.02665058597661253, 0.028578837505011542, 0.03052093117111936, 0.03246133851330052, 0.03438353235519167, 0.0362702027237503, 0.0381035025086781, 0.03986531841436178, 0.04153756175813872, 0.043102472799610075, 0.04454293158439271, 0.04584276778660145, 0.04698706176511043, 0.04796242902846769, 0.04875728054180862, 0.049362051805404844, 0.0497693943770712] + [0.04997432447755395] * 2 + [0.0497693943770712, 0.049362051805404844, 0.04875728054180862, 0.04796242902846769, 0.04698706176511043, 0.04584276778660145, 0.04454293158439271, 0.043102472799610075, 0.04153756175813872, 0.03986531841436178, 0.0381035025086781, 0.0362702027237503, 0.03438353235519167, 0.03246133851330052, 0.03052093117111936, 0.028578837505011542, 0.02665058597661253, 0.02475052352197671, 0.022891668088580716, 0.021085597636209694, 0.01934237563356426, 0.01767051207432904, 0.01607695813455482, 0.014567131821221753, 0.013144971336512885, 0.011813012413266466, 0.010572485566995856, 0.009423429055037947, 0.008364813324402726, 0.007394672852595283, 0.006510241522248109, 0.0057080880004843505, 0.004984247995779588, 0.004334350716624311, 0.003753737336079348, 0.0032375697544028154, 0.0027809284304838883, 0.0023788985066381502] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4626690225680879843_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1775636094303868161_i": {
            "samples": [0.0023765175656522927, 0.00277280179748533, 0.003222233007255454, 0.003729540899760031, 0.0042994620825031644, 0.004936659680003747, 0.005645632077882292, 0.006430611485562499, 0.007295453414731069, 0.008243518601862293, 0.009277549343912747, 0.010399542651203787, 0.011610623033113523, 0.012910918101726147, 0.014299440486615508, 0.015773979781220488, 0.017331008369633794, 0.01896560499595428, 0.020671399823556116, 0.022440544479577298, 0.024263710186295383, 0.026130116546987422, 0.02802759288646575, 0.02994267325901653, 0.031860725348329115, 0.03376611252030916, 0.03564238728058127, 0.03747251336822416, 0.03923911272284779, 0.04092473263182789, 0.04251212753632145, 0.043984549284493316, 0.04532603910028947, 0.04652171421278589, 0.04755804198445521, 0.04842309449844854, 0.04910677691816965, 0.049601023510753364, 0.04989995601404226, 0.05, 0.04989995601404226, 0.049601023510753364, 0.04910677691816965, 0.04842309449844854, 0.04755804198445521, 0.04652171421278589, 0.04532603910028947, 0.043984549284493316, 0.04251212753632145, 0.04092473263182789, 0.03923911272284779, 0.03747251336822416, 0.03564238728058127, 0.03376611252030916, 0.031860725348329115, 0.02994267325901653, 0.02802759288646575, 0.026130116546987422, 0.024263710186295383, 0.022440544479577298, 0.020671399823556116, 0.01896560499595428, 0.017331008369633794, 0.015773979781220488, 0.014299440486615508, 0.012910918101726147, 0.011610623033113523, 0.010399542651203787, 0.009277549343912747, 0.008243518601862293, 0.007295453414731069, 0.006430611485562499, 0.005645632077882292, 0.004936659680003747, 0.0042994620825031644, 0.003729540899760031, 0.003222233007255454, 0.00277280179748533, 0.0023765175656522927, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1775636094303868161_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1154310326417174617_i": {
            "samples": [0.0023741980663118723, 0.0027648972523077447, 0.0032073369241662967, 0.0037060707716190452, 0.004265661310659706, 0.004890604787077224, 0.005585245978070846, 0.006353683504536691, 0.007199666634441962, 0.00812648494662392, 0.009136852622855698, 0.010232789530572876, 0.011415501634023632, 0.012685263611333798, 0.014041306841966548, 0.015481716146257238, 0.017003338789898063, 0.01860170929687262, 0.02027099353233575, 0.022003955313550594, 0.02379194847753636, 0.025624936878516826, 0.02749154421167759, 0.029379134872581925, 0.03127392627966391, 0.033161132231419775, 0.035025135965740424, 0.03684969066555054, 0.038618144244593276, 0.0403136843834164, 0.041919599002129805, 0.04341954668575614, 0.04479783104962841, 0.046039672671701934, 0.0471314720457076, 0.04806105703700783, 0.048817908557594714, 0.04939335861570002, 0.0497807555286759] + [0.04997559189699447] * 2 + [0.0497807555286759, 0.04939335861570002, 0.048817908557594714, 0.04806105703700783, 0.0471314720457076, 0.046039672671701934, 0.04479783104962841, 0.04341954668575614, 0.041919599002129805, 0.0403136843834164, 0.038618144244593276, 0.03684969066555054, 0.035025135965740424, 0.033161132231419775, 0.03127392627966391, 0.029379134872581925, 0.02749154421167759, 0.025624936878516826, 0.02379194847753636, 0.022003955313550594, 0.02027099353233575, 0.01860170929687262, 0.017003338789898063, 0.015481716146257238, 0.014041306841966548, 0.012685263611333798, 0.011415501634023632, 0.010232789530572876, 0.009136852622855698, 0.00812648494662392, 0.007199666634441962, 0.006353683504536691, 0.005585245978070846, 0.004890604787077224, 0.004265661310659706, 0.0037060707716190452, 0.0032073369241662967, 0.0027648972523077447, 0.0023741980663118723],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1154310326417174617_q": {
            "samples": [0.0] * 80,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1375804385615889865_i": {
            "samples": [0.0023719376617539777, 0.0027572058474173954, 0.003192862950491985, 0.0036832952295819906, 0.004232899431126499, 0.004846012572645961, 0.005526832330445386, 0.006279328577150269, 0.007107146946222248, 0.008013505651825247, 0.009001087153051162, 0.010071926609742871, 0.011227299419639394, 0.012467610438864811, 0.013792287754816857, 0.015199684087177015, 0.01668698902458154, 0.018250155348319173, 0.019883842639177397, 0.02158138120093714, 0.023334759059131748, 0.025134634405631767, 0.026970375361881335, 0.028830128334327694, 0.03070091554758425, 0.032568761581510355, 0.03441884792917923, 0.03623569375865828, 0.03800336023035619, 0.03970567492278966, 0.04132647218290696, 0.04284984457176395, 0.044260400049559875, 0.04554351915970706, 0.04668560624918924, 0.04767432871595663, 0.04849883841124281, 0.049149969646391525, 0.049620408753911195, 0.04990483081790261, 0.05, 0.04990483081790261, 0.049620408753911195, 0.049149969646391525, 0.04849883841124281, 0.04767432871595663, 0.04668560624918924, 0.04554351915970706, 0.044260400049559875, 0.04284984457176395, 0.04132647218290696, 0.03970567492278966, 0.03800336023035619, 0.03623569375865828, 0.03441884792917923, 0.032568761581510355, 0.03070091554758425, 0.028830128334327694, 0.026970375361881335, 0.025134634405631767, 0.023334759059131748, 0.02158138120093714, 0.019883842639177397, 0.018250155348319173, 0.01668698902458154, 0.015199684087177015, 0.013792287754816857, 0.012467610438864811, 0.011227299419639394, 0.010071926609742871, 0.009001087153051162, 0.008013505651825247, 0.007107146946222248, 0.006279328577150269, 0.005526832330445386, 0.004846012572645961, 0.004232899431126499, 0.0036832952295819906, 0.003192862950491985, 0.0027572058474173954, 0.0023719376617539777] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1375804385615889865_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6389084342998740564_i": {
            "samples": [0.0023697341230815502, 0.0027497191079700937, 0.003178793550988529, 0.003661184349251405, 0.004201130317136066, 0.004802816476033676, 0.005470299598572874, 0.006207425493364534, 0.007017738815929368, 0.007904386509011268, 0.008870016302179503, 0.009916672026138945, 0.011045687809812412, 0.012257583515331636, 0.01355196401427587, 0.01492742510443359, 0.01638146899710487, 0.017910432358655807, 0.019509429856531403, 0.021172316031397853, 0.02289166808858072, 0.024658791871943433, 0.026463752854039426, 0.02829543345402747, 0.030141617389831035, 0.031989101097731676, 0.03382383152912155, 0.035631068881849984, 0.03739557206640686, 0.03910180397075797, 0.04073415289842753, 0.04227716593857408, 0.043715789509102224, 0.0450356119165765, 0.04622310251860319, 0.04726584196970143, 0.04815273808954074, 0.04887422211602598, 0.04942242049219364, 0.04979129787620506] + [0.04997676774289315] * 2 + [0.04979129787620506, 0.04942242049219364, 0.04887422211602598, 0.04815273808954074, 0.04726584196970143, 0.04622310251860319, 0.0450356119165765, 0.043715789509102224, 0.04227716593857408, 0.04073415289842753, 0.03910180397075797, 0.03739557206640686, 0.035631068881849984, 0.03382383152912155, 0.031989101097731676, 0.030141617389831035, 0.02829543345402747, 0.026463752854039426, 0.024658791871943433, 0.02289166808858072, 0.021172316031397853, 0.019509429856531403, 0.017910432358655807, 0.01638146899710487, 0.01492742510443359, 0.01355196401427587, 0.012257583515331636, 0.011045687809812412, 0.009916672026138945, 0.008870016302179503, 0.007904386509011268, 0.007017738815929368, 0.006207425493364534, 0.005470299598572874, 0.004802816476033676, 0.004201130317136066, 0.003661184349251405, 0.003178793550988529, 0.0027497191079700937, 0.0023697341230815502] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6389084342998740564_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3573564073619056728_i": {
            "samples": [0.002367585332046556, 0.002742429001095446, 0.0031651121412089953, 0.003639709879688648, 0.0041703104847918586, 0.004760953821469017, 0.0054155616602510085, 0.006137860272902416, 0.0069312960193502, 0.007798944917806579, 0.008743417486256922, 0.009766760439516934, 0.010870357111619398, 0.01205482873719094, 0.013319938955978312, 0.014664504089895237, 0.016086311870337322, 0.017582051354369247, 0.019147256752444986, 0.020776267790237824, 0.022462209038039648, 0.024196990361033722, 0.02597133027379668, 0.027774803527376324, 0.02959591372555346, 0.03142219117030988, 0.033240315490314754, 0.03503626192859949, 0.03679546947713834, 0.038503028369162424, 0.0401438837980271, 0.041703052147697824, 0.043165845516891024, 0.04451809991721775, 0.04574640224315968, 0.04683831096255842, 0.047782565470367404, 0.0485692791906385, 0.04919011180175932, 0.04963841639207437, 0.049909357916148325, 0.05, 0.049909357916148325, 0.04963841639207437, 0.04919011180175932, 0.0485692791906385, 0.047782565470367404, 0.04683831096255842, 0.04574640224315968, 0.04451809991721775, 0.043165845516891024, 0.041703052147697824, 0.0401438837980271, 0.038503028369162424, 0.03679546947713834, 0.03503626192859949, 0.033240315490314754, 0.03142219117030988, 0.02959591372555346, 0.027774803527376324, 0.02597133027379668, 0.024196990361033722, 0.022462209038039648, 0.020776267790237824, 0.019147256752444986, 0.017582051354369247, 0.016086311870337322, 0.014664504089895237, 0.013319938955978312, 0.01205482873719094, 0.010870357111619398, 0.009766760439516934, 0.008743417486256922, 0.007798944917806579, 0.0069312960193502, 0.006137860272902416, 0.0054155616602510085, 0.004760953821469017, 0.0041703104847918586, 0.003639709879688648, 0.0031651121412089953, 0.002742429001095446, 0.002367585332046556, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3573564073619056728_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9018644415177036998_i": {
            "samples": [0.0023654892742708774, 0.0027353279075391515, 0.003151803024336082, 0.003618845129261924, 0.004140398909227288, 0.0047203655441330665, 0.005362537422570768, 0.0060705256497609345, 0.0068476809801616524, 0.007697009067600198, 0.008621081194687642, 0.009621941912718581, 0.010701015284218336, 0.011859011662927799, 0.013095837159927582, 0.014410508119241997, 0.015801073051313504, 0.017264544538571694, 0.018796843625467123, 0.0203927591289532, 0.022045924149701537, 0.023748811827015427, 0.025492752061941737, 0.02726797053697746, 0.029063650893670724, 0.030868020401113125, 0.03266845887158564, 0.03445162996993254, 0.03620363343834905, 0.03791017613764978, 0.039556759210257725, 0.04112887811993324, 0.04261223183894916, 0.04399293705396253, 0.04525774296401605, 0.04639424206178008, 0.047391072232571156, 0.048238105580975396, 0.048926619603661396, 0.04944944666606251, 0.04980109820219597] + [0.04997786062858862] * 2 + [0.04980109820219597, 0.04944944666606251, 0.048926619603661396, 0.048238105580975396, 0.047391072232571156, 0.04639424206178008, 0.04525774296401605, 0.04399293705396253, 0.04261223183894916, 0.04112887811993324, 0.039556759210257725, 0.03791017613764978, 0.03620363343834905, 0.03445162996993254, 0.03266845887158564, 0.030868020401113125, 0.029063650893670724, 0.02726797053697746, 0.025492752061941737, 0.023748811827015427, 0.022045924149701537, 0.0203927591289532, 0.018796843625467123, 0.017264544538571694, 0.015801073051313504, 0.014410508119241997, 0.013095837159927582, 0.011859011662927799, 0.010701015284218336, 0.009621941912718581, 0.008621081194687642, 0.007697009067600198, 0.0068476809801616524, 0.0060705256497609345, 0.005362537422570768, 0.0047203655441330665, 0.004140398909227288, 0.003618845129261924, 0.003151803024336082, 0.0027353279075391515, 0.0023654892742708774],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-9018644415177036998_q": {
            "samples": [0.0] * 84,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1760744602010964249_i": {
            "samples": [0.0023634440329593502, 0.0027284085954552796, 0.003138851332956245, 0.0035985648606288896, 0.0041113568557084494, 0.004680995938689247, 0.005311150468688069, 0.00600532059909286, 0.0067667641618306355, 0.007598417184809545, 0.008502810091413515, 0.009481980876368503, 0.010537386790920358, 0.011669816293375147, 0.012879303219463201, 0.014165045291316809, 0.01552532920487773, 0.01695746460460166, 0.018457729263681805, 0.020021327731311947, 0.021642365581140174, 0.023313841194520603, 0.025027656738345366, 0.026774649652645865, 0.028544645553053374, 0.030326532985631673, 0.032108359957239506, 0.0338774516165966, 0.035620547894877584, 0.03732395934686225, 0.03897373888245319, 0.040555866562226706, 0.04205644416788042, 0.04346189586630725, 0.04475917098022608, 0.04593594467215388, 0.046980812252376526, 0.04788347284235835, 0.04863489826575815, 0.049227483298830255, 0.04965517378525212, 0.04991356959803134, 0.05, 0.04991356959803134, 0.04965517378525212, 0.049227483298830255, 0.04863489826575815, 0.04788347284235835, 0.046980812252376526, 0.04593594467215388, 0.04475917098022608, 0.04346189586630725, 0.04205644416788042, 0.040555866562226706, 0.03897373888245319, 0.03732395934686225, 0.035620547894877584, 0.0338774516165966, 0.032108359957239506, 0.030326532985631673, 0.028544645553053374, 0.026774649652645865, 0.025027656738345366, 0.023313841194520603, 0.021642365581140174, 0.020021327731311947, 0.018457729263681805, 0.01695746460460166, 0.01552532920487773, 0.014165045291316809, 0.012879303219463201, 0.011669816293375147, 0.010537386790920358, 0.009481980876368503, 0.008502810091413515, 0.007598417184809545, 0.0067667641618306355, 0.00600532059909286, 0.005311150468688069, 0.004680995938689247, 0.0041113568557084494, 0.0035985648606288896, 0.003138851332956245, 0.0027284085954552796, 0.0023634440329593502] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1760744602010964249_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5117652412973727226_i": {
            "samples": [0.0023614477830638096, 0.0027216641961612113, 0.0031262429753324637, 0.003578845194019041, 0.0040831477242977785, 0.004642792428202869, 0.0052613287333539305, 0.0059421499025434435, 0.006688423508546294, 0.007503016839910196, 0.008388418185686591, 0.009346655170821307, 0.010379211532248009, 0.011486943930939034, 0.012670000579125477, 0.013927743616257138, 0.015258677283788763, 0.016660384019739603, 0.018129470612149777, 0.019661526510158164, 0.021251096288042743, 0.022891668088580713, 0.02457567963695314, 0.02629454311685732, 0.028038689840620853, 0.029797635231494826, 0.03156006417787868, 0.03331393632715323, 0.03504661037417321, 0.036744985880981476, 0.038395660655756815, 0.03998510123679154, 0.04149982358780436, 0.04292658072989966, 0.0442525537275051, 0.04546554222331691, 0.04655415059090276, 0.047507965750505046, 0.048317722777824534, 0.04897545462768124, 0.049474622591320176, 0.04981022450099476] + [0.04997887817809232] * 2 + [0.04981022450099476, 0.049474622591320176, 0.04897545462768124, 0.048317722777824534, 0.047507965750505046, 0.04655415059090276, 0.04546554222331691, 0.0442525537275051, 0.04292658072989966, 0.04149982358780436, 0.03998510123679154, 0.038395660655756815, 0.036744985880981476, 0.03504661037417321, 0.03331393632715323, 0.03156006417787868, 0.029797635231494826, 0.028038689840620853, 0.02629454311685732, 0.02457567963695314, 0.022891668088580713, 0.021251096288042743, 0.019661526510158164, 0.018129470612149777, 0.016660384019739603, 0.015258677283788763, 0.013927743616257138, 0.012670000579125477, 0.011486943930939034, 0.010379211532248009, 0.009346655170821307, 0.008388418185686591, 0.007503016839910196, 0.006688423508546294, 0.0059421499025434435, 0.0052613287333539305, 0.004642792428202869, 0.0040831477242977785, 0.003578845194019041, 0.0031262429753324637, 0.0027216641961612113, 0.0023614477830638096] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5117652412973727226_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5661736604214274021_i": {
            "samples": [0.0023594987858608523, 0.0027150881816862893, 0.0031139645857773107, 0.0035596635180664376, 0.004055736906838736, 0.004605705351574352, 0.005213004204556965, 0.005880923748526811, 0.006612543930766052, 0.007410664308975208, 0.00827773006657207, 0.009215755159204355, 0.010226243854141788, 0.01131011211301379, 0.012467610438864815, 0.013698249953282927, 0.015000733581042905, 0.016372894291256584, 0.017811642369046546, 0.019312923664813172, 0.020871690685061783, 0.022481888246841455, 0.024136455216242015, 0.025827343591189503, 0.027545555873158847, 0.02928120130671888, 0.031023571157490146, 0.03276123275757919, 0.03448214158408967, 0.03617377016362694, 0.03782325212764544, 0.03941753929454081, 0.04094356923922737, 0.04238844044386423, 0.0437395918177791, 0.044984983142411124, 0.04611327284821754, 0.047113989472523654, 0.0479776931850282, 0.04869612390285605, 0.04926233274822752, 0.049670793924314345, 0.04991749449086604, 0.05, 0.04991749449086604, 0.049670793924314345, 0.04926233274822752, 0.04869612390285605, 0.0479776931850282, 0.047113989472523654, 0.04611327284821754, 0.044984983142411124, 0.0437395918177791, 0.04238844044386423, 0.04094356923922737, 0.03941753929454081, 0.03782325212764544, 0.03617377016362694, 0.03448214158408967, 0.03276123275757919, 0.031023571157490146, 0.02928120130671888, 0.027545555873158847, 0.025827343591189503, 0.024136455216242015, 0.022481888246841455, 0.020871690685061783, 0.019312923664813172, 0.017811642369046546, 0.016372894291256584, 0.015000733581042905, 0.013698249953282927, 0.012467610438864815, 0.01131011211301379, 0.010226243854141788, 0.009215755159204355, 0.00827773006657207, 0.007410664308975208, 0.006612543930766052, 0.005880923748526811, 0.005213004204556965, 0.004605705351574352, 0.004055736906838736, 0.0035596635180664376, 0.0031139645857773107, 0.0027150881816862893, 0.0023594987858608523, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5661736604214274021_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4179998349212846360_i": {
            "samples": [0.0023575953839095015, 0.002708674343961557, 0.003102003478767531, 0.0035409984075191283, 0.00402909165514829, 0.0045696877678023645, 0.005166112648902035, 0.005821557364281266, 0.006539016831393066, 0.007321223984968252, 0.00817058019581819, 0.009089082905899914, 0.010078251625859302, 0.01113905361502447, 0.012271830721827588, 0.013476228998271037, 0.014751132808722145, 0.01609460522468131, 0.017503836527409104, 0.018975102624404182, 0.020503735119741663, 0.0220841046595669, 0.023709619001476934, 0.02537273703070116, 0.027064999669333657, 0.02877707830168332, 0.030498840975286517, 0.03221943624125977, 0.03392739407907832, 0.03561074292056631, 0.03725714135797283, 0.03885402270429286, 0.04038875018356396, 0.0418487801776481, 0.04322183065625878, 0.04449605167986177, 0.04566019470012907, 0.046703777297440935, 0.04761723999475882, 0.04839209187467782, 0.04902104190148081, 0.04949811310957606, 0.0498187371580125] + [0.04997982715937286] * 2 + [0.0498187371580125, 0.04949811310957606, 0.04902104190148081, 0.04839209187467782, 0.04761723999475882, 0.046703777297440935, 0.04566019470012907, 0.04449605167986177, 0.04322183065625878, 0.0418487801776481, 0.04038875018356396, 0.03885402270429286, 0.03725714135797283, 0.03561074292056631, 0.03392739407907832, 0.03221943624125977, 0.030498840975286517, 0.02877707830168332, 0.027064999669333657, 0.02537273703070116, 0.023709619001476934, 0.0220841046595669, 0.020503735119741663, 0.018975102624404182, 0.017503836527409104, 0.01609460522468131, 0.014751132808722145, 0.013476228998271037, 0.012271830721827588, 0.01113905361502447, 0.010078251625859302, 0.009089082905899914, 0.00817058019581819, 0.007321223984968252, 0.006539016831393066, 0.005821557364281266, 0.005166112648902035, 0.0045696877678023645, 0.00402909165514829, 0.0035409984075191283, 0.003102003478767531, 0.002708674343961557, 0.0023575953839095015],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4179998349212846360_q": {
            "samples": [0.0] * 88,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1366180850948390541_i": {
            "samples": [0.0023557359963581035, 0.002702416775512681, 0.0030903476064767566, 0.003522829547219092, 0.004003180959416371, 0.004534695275563765, 0.005120593358589029, 0.005763970676858676, 0.006467739668992819, 0.007234567834485123, 0.008066812254210081, 0.00896645141527161, 0.009935015382480405, 0.0109735155187145, 0.012082375102822195, 0.013261362320668355, 0.014509527206492262, 0.015825144182227458, 0.01720566187655127, 0.01864766189857047, 0.020146828189494592, 0.021697928476803786, 0.023294809208003968, 0.024930405145275957, 0.02659676455996392, 0.028285090680370613, 0.02998579972286272, 0.03168859548158114, 0.0333825600743261, 0.03505626005097021, 0.036697866676605594, 0.038295288815846165, 0.03983631647894344, 0.041308772756270824, 0.04270067157648922, 0.044000378485671676, 0.04519677146892932, 0.046279398730104206, 0.04723863031438423, 0.04806580050654053, 0.048753338064773985, 0.04929488155526912, 0.04968537733136282, 0.04992115804719207, 0.05, 0.04992115804719207, 0.04968537733136282, 0.04929488155526912, 0.048753338064773985, 0.04806580050654053, 0.04723863031438423, 0.046279398730104206, 0.04519677146892932, 0.044000378485671676, 0.04270067157648922, 0.041308772756270824, 0.03983631647894344, 0.038295288815846165, 0.036697866676605594, 0.03505626005097021, 0.0333825600743261, 0.03168859548158114, 0.02998579972286272, 0.028285090680370613, 0.02659676455996392, 0.024930405145275957, 0.023294809208003968, 0.021697928476803786, 0.020146828189494592, 0.01864766189857047, 0.01720566187655127, 0.015825144182227458, 0.014509527206492262, 0.013261362320668355, 0.012082375102822195, 0.0109735155187145, 0.009935015382480405, 0.00896645141527161, 0.008066812254210081, 0.007234567834485123, 0.006467739668992819, 0.005763970676858676, 0.005120593358589029, 0.004534695275563765, 0.004003180959416371, 0.003522829547219092, 0.0030903476064767566, 0.002702416775512681, 0.0023557359963581035] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1366180850948390541_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1108773240470778536_i": {
            "samples": [0.002353919114572558, 0.002696309851531143, 0.00307898551943427, 0.0035051376618063196, 0.003977975435911384, 0.004500685846748754, 0.005076388918068964, 0.005708088000484348, 0.006398615554804989, 0.007150574896042875, 0.007966278536960766, 0.00884768392586556, 0.009796327527285027, 0.010813258341494367, 0.011898972094507545, 0.013053347448852982, 0.014275585681915955, 0.015564155347705725, 0.01691674347479884, 0.01833021485368369, 0.019800580927307347, 0.021322979716784412, 0.022891668088580716, 0.0245000274999269, 0.026140584147037346, 0.027805044188660435, 0.029484344429800732, 0.03116871853280928, 0.032847778482463424, 0.03451061067637399, 0.036145885651279325, 0.03774198009945037, 0.039287109487906785, 0.040769469276886745, 0.04217738245321173, 0.04349945085839971, 0.04472470760917139, 0.04584276778660145, 0.04684397451519882, 0.04771953756838331, 0.04846166172381721, 0.04906366225031764, 0.04952006513485812, 0.04982668994851846] + [0.04998071359715336] * 2 + [0.04982668994851846, 0.04952006513485812, 0.04906366225031764, 0.04846166172381721, 0.04771953756838331, 0.04684397451519882, 0.04584276778660145, 0.04472470760917139, 0.04349945085839971, 0.04217738245321173, 0.040769469276886745, 0.039287109487906785, 0.03774198009945037, 0.036145885651279325, 0.03451061067637399, 0.032847778482463424, 0.03116871853280928, 0.029484344429800732, 0.027805044188660435, 0.026140584147037346, 0.0245000274999269, 0.022891668088580716, 0.021322979716784412, 0.019800580927307347, 0.01833021485368369, 0.01691674347479884, 0.015564155347705725, 0.014275585681915955, 0.013053347448852982, 0.011898972094507545, 0.010813258341494367, 0.009796327527285027, 0.00884768392586556, 0.007966278536960766, 0.007150574896042875, 0.006398615554804989, 0.005708088000484348, 0.005076388918068964, 0.004500685846748754, 0.003977975435911384, 0.0035051376618063196, 0.00307898551943427, 0.002696309851531143, 0.002353919114572558] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1108773240470778536_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4511218137379937594_i": {
            "samples": [0.0023521432980605113, 0.0026903482132105095, 0.0030679063300458726, 0.0034879044506540766, 0.003953447223179746, 0.004467619672724645, 0.005033444988644889, 0.005653837747975059, 0.006331552880619031, 0.007069130816380236, 0.00786883939408836, 0.008732613255708736, 0.009661991589606147, 0.010658055222875662, 0.011721364188337703, 0.012851897002720597, 0.0140489929839709, 0.015311299002902116, 0.016636722103163252, 0.01802238942989105, 0.019464616878161044, 0.0209588878050457, 0.022499843042273794, 0.024081283299824993, 0.02569618486516688, 0.02733672928041425, 0.028994347423940886, 0.030659778138672513, 0.03232314124242926, 0.03397402443335853, 0.03560158327372894, 0.037194653106882324, 0.03874187144416247, 0.040231809060531525, 0.04165310776858627, 0.042994622609584025, 0.04424556601489621, 0.04539565135896793, 0.04643523325096258, 0.04735544190081372, 0.0481483089486141, 0.04880688226446461, 0.049325327407432035, 0.049699013673513974, 0.04992458295798774, 0.05, 0.04992458295798774, 0.049699013673513974, 0.049325327407432035, 0.04880688226446461, 0.0481483089486141, 0.04735544190081372, 0.04643523325096258, 0.04539565135896793, 0.04424556601489621, 0.042994622609584025, 0.04165310776858627, 0.040231809060531525, 0.03874187144416247, 0.037194653106882324, 0.03560158327372894, 0.03397402443335853, 0.03232314124242926, 0.030659778138672513, 0.028994347423940886, 0.02733672928041425, 0.02569618486516688, 0.024081283299824993, 0.022499843042273794, 0.0209588878050457, 0.019464616878161044, 0.01802238942989105, 0.016636722103163252, 0.015311299002902116, 0.0140489929839709, 0.012851897002720597, 0.011721364188337703, 0.010658055222875662, 0.009661991589606147, 0.008732613255708736, 0.00786883939408836, 0.007069130816380236, 0.006331552880619031, 0.005653837747975059, 0.005033444988644889, 0.004467619672724645, 0.003953447223179746, 0.0034879044506540766, 0.0030679063300458726, 0.0026903482132105095, 0.0023521432980605113, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4511218137379937594_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6835776219466774047_i": {
            "samples": [0.0023504071706684183, 0.002684526752245091, 0.003057099678737945, 0.0034711125275900465, 0.003929569886006754, 0.004435459022221865, 0.004991710109454501, 0.005601152164127267, 0.006266464974861447, 0.006990127421560913, 0.007774362712087754, 0.008621081194687642, 0.009531821534077656, 0.010507691164227685, 0.011549307047327269, 0.012656737872029408, 0.013829448910539591, 0.015066250819290425, 0.016365253707858633, 0.01772382781187781, 0.019138572084960222, 0.020605291969744585, 0.022118987517657437, 0.023673852900300094, 0.025263288193100687, 0.026879924115683254, 0.028515660186145615, 0.03016171649210398, 0.03180869900505531, 0.033446678072439624, 0.0350652794207335, 0.036653786700647804, 0.0382012543101879, 0.03969662895135058, 0.04112887811993324, 0.04248712350336351, 0.04376077707607792, 0.044939677542379666, 0.04601422468837087, 0.04697550917162547, 0.04781543530237421, 0.048526834454084955, 0.049103566883684835, 0.04954060993977659, 0.049834130886838246] + [0.04998154286874318] * 2 + [0.049834130886838246, 0.04954060993977659, 0.049103566883684835, 0.048526834454084955, 0.04781543530237421, 0.04697550917162547, 0.04601422468837087, 0.044939677542379666, 0.04376077707607792, 0.04248712350336351, 0.04112887811993324, 0.03969662895135058, 0.0382012543101879, 0.036653786700647804, 0.0350652794207335, 0.033446678072439624, 0.03180869900505531, 0.03016171649210398, 0.028515660186145615, 0.026879924115683254, 0.025263288193100687, 0.023673852900300094, 0.022118987517657437, 0.020605291969744585, 0.019138572084960222, 0.01772382781187781, 0.016365253707858633, 0.015066250819290425, 0.013829448910539591, 0.012656737872029408, 0.011549307047327269, 0.010507691164227685, 0.009531821534077656, 0.008621081194687642, 0.007774362712087754, 0.006990127421560913, 0.006266464974861447, 0.005601152164127267, 0.004991710109454501, 0.004435459022221865, 0.003929569886006754, 0.0034711125275900465, 0.003057099678737945, 0.002684526752245091, 0.0023504071706684183],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6835776219466774047_q": {
            "samples": [0.0] * 92,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2313458449376770731_i": {
            "samples": [0.0023487094170303773, 0.0026788405963976483, 0.0030465557025082116, 0.0034547453650004786, 0.00390631832647667, 0.004404168109843033, 0.004951135513422761, 0.005549967079187939, 0.00620326978449356, 0.00691346231996685, 0.007682723433531037, 0.008512937940321689, 0.009405641117495178, 0.010361962318306845, 0.011382568747762917, 0.012467610438864811, 0.01361666755014075, 0.014828701168026055, 0.016102008838123887, 0.01743418606418866, 0.018822095000024644, 0.02026184151517824, 0.021748761738846677, 0.02327741907718648, 0.024841612557469243, 0.026434397179580627, 0.028048116753501297, 0.029674449473986737, 0.031304466235011576, 0.03292870142192064, 0.03453723564470059, 0.03611978959808223, 0.03766582796051853, 0.039164671981945176, 0.040605619167156784, 0.04197806824496479, 0.04327164742994413, 0.0444763438397427, 0.04558263183192654, 0.04658159797435142, 0.047465060364983394, 0.04822568007240598, 0.04885706257690151, 0.049353847252378576, 0.04971178313839497, 0.04992778950448698, 0.05, 0.04992778950448698, 0.04971178313839497, 0.049353847252378576, 0.04885706257690151, 0.04822568007240598, 0.047465060364983394, 0.04658159797435142, 0.04558263183192654, 0.0444763438397427, 0.04327164742994413, 0.04197806824496479, 0.040605619167156784, 0.039164671981945176, 0.03766582796051853, 0.03611978959808223, 0.03453723564470059, 0.03292870142192064, 0.031304466235011576, 0.029674449473986737, 0.028048116753501297, 0.026434397179580627, 0.024841612557469243, 0.02327741907718648, 0.021748761738846677, 0.02026184151517824, 0.018822095000024644, 0.01743418606418866, 0.016102008838123887, 0.014828701168026055, 0.01361666755014075, 0.012467610438864811, 0.011382568747762917, 0.010361962318306845, 0.009405641117495178, 0.008512937940321689, 0.007682723433531037, 0.00691346231996685, 0.00620326978449356, 0.005549967079187939, 0.004951135513422761, 0.004404168109843033, 0.00390631832647667, 0.0034547453650004786, 0.0030465557025082116, 0.0026788405963976483, 0.0023487094170303773] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-2313458449376770731_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7762103977444927572_i": {
            "samples": [0.002347048779249552, 0.002673285096051335, 0.0030362650056868575, 0.0034387872419526506, 0.003883668701533285, 0.004373712974291932, 0.0049116749569081235, 0.005500221680700284, 0.006141889580543693, 0.006839038534534935, 0.007593803111526728, 0.008408041573549649, 0.009283283289787775, 0.010220675325219643, 0.011220929067069556, 0.012284267842470251, 0.013410376557778703, 0.014598354450409277, 0.01584667208459727, 0.01715313374019508, 0.018514846335837026, 0.019928195992504606, 0.021388833279221975, 0.022891668088580716, 0.024430874966110842, 0.02599990956513435, 0.027591536719521245, 0.029197870423497665, 0.030810425784009523, 0.03242018277163988, 0.0340176613459811, 0.03559300727656994, 0.03713608772737931, 0.03863659542810152, 0.04008416002583862, 0.041468465003015625, 0.04277936836771416, 0.04400702517701141, 0.045142009847387025, 0.04617543614298125, 0.04709907271550833, 0.04790545210078051, 0.048587971156587625, 0.04914098105423956, 0.049559865109167794, 0.04984110295101274] + [0.04998231978575862] * 2 + [0.04984110295101274, 0.049559865109167794, 0.04914098105423956, 0.048587971156587625, 0.04790545210078051, 0.04709907271550833, 0.04617543614298125, 0.045142009847387025, 0.04400702517701141, 0.04277936836771416, 0.041468465003015625, 0.04008416002583862, 0.03863659542810152, 0.03713608772737931, 0.03559300727656994, 0.0340176613459811, 0.03242018277163988, 0.030810425784009523, 0.029197870423497665, 0.027591536719521245, 0.02599990956513435, 0.024430874966110842, 0.022891668088580716, 0.021388833279221975, 0.019928195992504606, 0.018514846335837026, 0.01715313374019508, 0.01584667208459727, 0.014598354450409277, 0.013410376557778703, 0.012284267842470251, 0.011220929067069556, 0.010220675325219643, 0.009283283289787775, 0.008408041573549649, 0.007593803111526728, 0.006839038534534935, 0.006141889580543693, 0.005500221680700284, 0.0049116749569081235, 0.004373712974291932, 0.003883668701533285, 0.0034387872419526506, 0.0030362650056868575, 0.002673285096051335, 0.002347048779249552] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7762103977444927572_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3954932071202303921_i": {
            "samples": [0.0023454240537945543, 0.00266785581166854, 0.0030262186327295916, 0.003423223196004869, 0.003861598346498577, 0.004344061365504695, 0.0048732845618869895, 0.005451858302177329, 0.006082250685299729, 0.0067667641618306355, 0.007507489496236231, 0.008306257571426221, 0.009164589635859368, 0.01008364669168461, 0.011064178815137814, 0.012106475284621122, 0.013210316464479142, 0.014374928450381508, 0.015598941522470409, 0.016880353472302736, 0.0182164988667091, 0.0196040252840437, 0.021038877504485697, 0.022516290555281746, 0.024030792404005234, 0.025576216958733813, 0.027145727875001597, 0.02873185348777371, 0.030326532985631673, 0.031921173727724704, 0.03350671937640114, 0.03507372828494667, 0.03661246134614739, 0.03811297827941045, 0.039565241118007945, 0.04095922345972151, 0.04228502386959872, 0.04353298167811459, 0.044693793306593524, 0.04575862717834858, 0.04671923524177146, 0.04756805914264066, 0.048298329138143484, 0.04890415394425274, 0.0493805998496571, 0.04972375761069428, 0.049930795858806304, 0.05, 0.049930795858806304, 0.04972375761069428, 0.0493805998496571, 0.04890415394425274, 0.048298329138143484, 0.04756805914264066, 0.04671923524177146, 0.04575862717834858, 0.044693793306593524, 0.04353298167811459, 0.04228502386959872, 0.04095922345972151, 0.039565241118007945, 0.03811297827941045, 0.03661246134614739, 0.03507372828494667, 0.03350671937640114, 0.031921173727724704, 0.030326532985631673, 0.02873185348777371, 0.027145727875001597, 0.025576216958733813, 0.024030792404005234, 0.022516290555281746, 0.021038877504485697, 0.0196040252840437, 0.0182164988667091, 0.016880353472302736, 0.015598941522470409, 0.014374928450381508, 0.013210316464479142, 0.012106475284621122, 0.011064178815137814, 0.01008364669168461, 0.009164589635859368, 0.008306257571426221, 0.007507489496236231, 0.0067667641618306355, 0.006082250685299729, 0.005451858302177329, 0.0048732845618869895, 0.004344061365504695, 0.003861598346498577, 0.003423223196004869, 0.0030262186327295916, 0.00266785581166854, 0.0023454240537945543, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-3954932071202303921_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8484042401283422779_i": {
            "samples": [0.0023438340885947664, 0.002662548502086295, 0.003016408042880571, 0.003408038978403922, 0.003840085704057874, 0.004315182639942583, 0.004835922669629573, 0.005404822227200863, 0.006024283219370086, 0.006696552055769085, 0.007423676150889755, 0.008207458353881215, 0.009049409855302368, 0.009950702210656914, 0.010912119206528896, 0.011934009373685717, 0.01301624001984201, 0.014158153710107577, 0.015358528162793315, 0.016615540549723397, 0.017926737191282762, 0.019289009615272894, 0.020698577903878936, 0.022150982183836033, 0.02364108302101215, 0.025163071362560838, 0.026710488528717453, 0.028276256594121682, 0.029852719317876128, 0.0314316935857174, 0.03300453112063725, 0.03456219000455897, 0.03609531533820894, 0.03759432815440884, 0.03904952149711631, 0.040451162390149786, 0.04178959825099127, 0.04305536616140598, 0.04423930329240693, 0.04533265670024928, 0.04632719066581175, 0.04721528974415928, 0.047990055725537405, 0.04864539678371839, 0.049176107201602724, 0.04957793621528276, 0.04984764470335167] + [0.04998304866405808] * 2 + [0.04984764470335167, 0.04957793621528276, 0.049176107201602724, 0.04864539678371839, 0.047990055725537405, 0.04721528974415928, 0.04632719066581175, 0.04533265670024928, 0.04423930329240693, 0.04305536616140598, 0.04178959825099127, 0.040451162390149786, 0.03904952149711631, 0.03759432815440884, 0.03609531533820894, 0.03456219000455897, 0.03300453112063725, 0.0314316935857174, 0.029852719317876128, 0.028276256594121682, 0.026710488528717453, 0.025163071362560838, 0.02364108302101215, 0.022150982183836033, 0.020698577903878936, 0.019289009615272894, 0.017926737191282762, 0.016615540549723397, 0.015358528162793315, 0.014158153710107577, 0.01301624001984201, 0.011934009373685717, 0.010912119206528896, 0.009950702210656914, 0.009049409855302368, 0.008207458353881215, 0.007423676150889755, 0.006696552055769085, 0.006024283219370086, 0.005404822227200863, 0.004835922669629573, 0.004315182639942583, 0.003840085704057874, 0.003408038978403922, 0.003016408042880571, 0.002662548502086295, 0.0023438340885947664],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8484042401283422779_q": {
            "samples": [0.0] * 96,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1757172383199137058_i": {
            "samples": [0.0023422777803198446, 0.0026573591135838955, 0.003006825086557508, 0.0033932210123972066, 0.003819110258265289, 0.004287047663374263, 0.00479954970491761, 0.00535906150767277, 0.005967920866984466, 0.006628319533989669, 0.00734226209496504, 0.00811152286192766, 0.008937601277212043, 0.00982167641856898, 0.010764561271088567, 0.01176665750551206, 0.012827911566761958, 0.013947772929280167, 0.015125155414584882, 0.016358402489055148, 0.017645257464282145, 0.01898283950666276, 0.02036762632592945, 0.021795444353162226, 0.023261467137206407, 0.024760222584608464, 0.026285609543097933, 0.02783092408385142, 0.029388895675488788, 0.030951733265812565, 0.03251118109913282, 0.034058583901559664, 0.03558496086826492, 0.03708108769010378, 0.03853758566704166, 0.03994501677750795, 0.04129398341097818, 0.0425752313304191, 0.04377975431599434, 0.044898898855378545, 0.04592446719227338, 0.0468488170256052, 0.04766495616889826, 0.048366630533019005, 0.04894840388546867, 0.049405727964275475, 0.04973500168195559, 0.04993361834171834, 0.05, 0.04993361834171834, 0.04973500168195559, 0.049405727964275475, 0.04894840388546867, 0.048366630533019005, 0.04766495616889826, 0.0468488170256052, 0.04592446719227338, 0.044898898855378545, 0.04377975431599434, 0.0425752313304191, 0.04129398341097818, 0.03994501677750795, 0.03853758566704166, 0.03708108769010378, 0.03558496086826492, 0.034058583901559664, 0.03251118109913282, 0.030951733265812565, 0.029388895675488788, 0.02783092408385142, 0.026285609543097933, 0.024760222584608464, 0.023261467137206407, 0.021795444353162226, 0.02036762632592945, 0.01898283950666276, 0.017645257464282145, 0.016358402489055148, 0.015125155414584882, 0.013947772929280167, 0.012827911566761958, 0.01176665750551206, 0.010764561271088567, 0.00982167641856898, 0.008937601277212043, 0.00811152286192766, 0.00734226209496504, 0.006628319533989669, 0.005967920866984466, 0.00535906150767277, 0.00479954970491761, 0.004287047663374263, 0.003819110258265289, 0.0033932210123972066, 0.003006825086557508, 0.0026573591135838955, 0.0023422777803198446] + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1757172383199137058_q": {
            "samples": [0.0] * 100,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7377163761049853188_i": {
            "samples": [0.0023407540718299795, 0.002652283769664158, 0.00299746198332459, 0.0033787563544115645, 0.0037986524731640687, 0.004259628720537644, 0.004764128049941792, 0.005314526795062467, 0.005913100658053454, 0.006561988105067251, 0.007263151472393365, 0.008018336164919445, 0.008829028407540337, 0.009696412087621814, 0.010621325300621516, 0.011604217279296836, 0.012645106447333757, 0.013743540388445675, 0.01489855855980506, 0.01610865860199775, 0.017371767104643564, 0.018685215675796316, 0.020045723132955003, 0.021449384583134792, 0.022891668088580716, 0.024367419523501705, 0.025870876116356845, 0.02739568904301677, 0.02893495529041042, 0.030481258850476114, 0.03202672113332439, 0.03356306030992498, 0.035081659112196295, 0.036573640436263995, 0.03802994991724154, 0.0394414444756411, 0.040798985680890736, 0.04209353664069587, 0.04331626101013014, 0.04445862262494371, 0.04551248420266807, 0.04647020352505927, 0.04732472551790415, 0.04806966868005799, 0.04869940438277257, 0.04920912766202454, 0.049594918258907945, 0.049853790823621756] + [0.0499837333837949] * 2 + [0.049853790823621756, 0.049594918258907945, 0.04920912766202454, 0.04869940438277257, 0.04806966868005799, 0.04732472551790415, 0.04647020352505927, 0.04551248420266807, 0.04445862262494371, 0.04331626101013014, 0.04209353664069587, 0.040798985680890736, 0.0394414444756411, 0.03802994991724154, 0.036573640436263995, 0.035081659112196295, 0.03356306030992498, 0.03202672113332439, 0.030481258850476114, 0.02893495529041042, 0.02739568904301677, 0.025870876116356845, 0.024367419523501705, 0.022891668088580716, 0.021449384583134792, 0.020045723132955003, 0.018685215675796316, 0.017371767104643564, 0.01610865860199775, 0.01489855855980506, 0.013743540388445675, 0.012645106447333757, 0.011604217279296836, 0.010621325300621516, 0.009696412087621814, 0.008829028407540337, 0.008018336164919445, 0.007263151472393365, 0.006561988105067251, 0.005913100658053454, 0.005314526795062467, 0.004764128049941792, 0.004259628720537644, 0.0037986524731640687, 0.0033787563544115645, 0.00299746198332459, 0.002652283769664158, 0.0023407540718299795] + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7377163761049853188_q": {
            "samples": [0.0] * 100,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4902209669630684111_i": {
            "samples": [0.0023392619497844816, 0.002647318761494563, 0.0029883113013304528, 0.003364632657872833, 0.0037786937356530425, 0.004232899431126499, 0.004729621927095248, 0.0052711711835988885, 0.005859762765638613, 0.006497483214903075, 0.007186253242839665, 0.007927789094654854, 0.008723562506622177, 0.009574759750733155, 0.010482240329397893, 0.011446495946626277, 0.012467610438864811, 0.013545221396378827, 0.014678484242745097, 0.015866039563750774, 0.017105984486043, 0.018395848898737684, 0.019732577286671354, 0.021112516901222664, 0.022531412933208747, 0.023984411272303413, 0.025466069339249494, 0.026970375361881335, 0.02849077633519044, 0.03002021476142527, 0.03155117411106762, 0.03307573278246873, 0.03458562617033715, 0.03607231628483439, 0.03752706819766106, 0.038941032433230265, 0.04030533227586364, 0.04161115483183768, 0.04284984457176395, 0.04401299798757799, 0.04509255793226413, 0.04608090617173868, 0.04697095266880169, 0.047756220139797384, 0.04843092247589471, 0.04899003570223589, 0.04942936025833958, 0.04974557352006636, 0.0499362716444125, 0.05, 0.0499362716444125, 0.04974557352006636, 0.04942936025833958, 0.04899003570223589, 0.04843092247589471, 0.047756220139797384, 0.04697095266880169, 0.04608090617173868, 0.04509255793226413, 0.04401299798757799, 0.04284984457176395, 0.04161115483183768, 0.04030533227586364, 0.038941032433230265, 0.03752706819766106, 0.03607231628483439, 0.03458562617033715, 0.03307573278246873, 0.03155117411106762, 0.03002021476142527, 0.02849077633519044, 0.026970375361881335, 0.025466069339249494, 0.023984411272303413, 0.022531412933208747, 0.021112516901222664, 0.019732577286671354, 0.018395848898737684, 0.017105984486043, 0.015866039563750774, 0.014678484242745097, 0.013545221396378827, 0.012467610438864811, 0.011446495946626277, 0.010482240329397893, 0.009574759750733155, 0.008723562506622177, 0.007927789094654854, 0.007186253242839665, 0.006497483214903075, 0.005859762765638613, 0.0052711711835988885, 0.004729621927095248, 0.004232899431126499, 0.0037786937356530425, 0.003364632657872833, 0.0029883113013304528, 0.002647318761494563, 0.0023392619497844816, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4902209669630684111_q": {
            "samples": [0.0] * 100,
            "type": "arbitrary",
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
        "cosine_weights_D1/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_D1/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "D1/acquisition_mixer_8f5": [{'intermediate_frequency': -312363546.0, 'lo_frequency': 7450000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "D1/drive_mixer_b94": [{'intermediate_frequency': -141729925.0, 'lo_frequency': 5100000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

