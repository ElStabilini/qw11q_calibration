
# Single QUA script generated at 2025-01-15 11:39:29.220008
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(int, )
    set_dc_offset("B1/flux", "single", 0.0)
    set_dc_offset("D1/flux", "single", 0.21674190528643072)
    set_dc_offset("B2/flux", "single", -0.2819)
    set_dc_offset("D2/flux", "single", -0.4253086474672965)
    set_dc_offset("B3/flux", "single", 0.0307)
    set_dc_offset("D3/flux", "single", -0.21477959018116385)
    set_dc_offset("B4/flux", "single", -0.215)
    set_dc_offset("D4/flux", "single", 0.0)
    set_dc_offset("B5/flux", "single", 0.074)
    set_dc_offset("D5/flux", "single", -0.04)
    wait((4+(0*((Cast.to_int(v2)+Cast.to_int(v3))+Cast.to_int(v4)))), "B2/acquisition")
    with for_(v1,0,(v1<2048),(v1+1)):
        align()
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-164126628865188911", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        r1 = declare_stream()
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25553, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-7009042038113738942", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25553, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("8016682567654673542", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25552, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("52491366316988517", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25552, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("2814767558931722162", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25552, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("5076625473023077071", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25552, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("8956581005421886658", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25551, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-7873301612554006437", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25551, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("717081487210833740", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25551, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("1889309654779964293", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25551, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("359623134795485717", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25550, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-4988625125260856487", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25550, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-5550191170562876634", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25550, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-6111588085425425586", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25550, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("266652478318346996", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25549, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-7638066444208317632", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25549, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("2914809268673952775", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25549, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("3822908648087794801", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25549, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("5514632396013246107", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25548, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-4275738695597305651", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25548, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("1921827109723645217", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25548, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("7236245621965069123", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25548, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("1729256648351813092", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25547, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-5666600396346030177", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25547, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-4972177436948756488", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25547, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-7309571846804030613", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25547, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-722003858977088807", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25546, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-1112872323470008628", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25546, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-4946484525243574253", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25546, "B2/flux")
        wait(25501, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(11, "B2/flux")
        play("-7694144158965913873", "B2/flux")
        wait(51, "B2/drive")
        play("-6585968513791844179", "B2/drive")
        wait(71, "B2/acquisition")
        measure("-1741302944044372701", "B2/acquisition", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        assign(v4, Cast.to_int((((v2*0.6205520709401277)-(v3*0.7841652423130719))>0.0026125142084282697)))
        save(v4, r1)
        wait(25001, "B2/acquisition")
        wait(25546, "B2/flux")
        wait(25501, "B2/drive")
        wait(25000, )
    with stream_processing():
        r1.buffer(30).average().save("-1741302944044372701_B2|acquisition_shots")


config = {
    "version": 1,
    "controllers": {
        "con4": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": -0.2819,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
                    "offset": 0.21674190528643072,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
            },
            "digital_outputs": {
                "1": {},
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
    },
    "octaves": {
        "octave2": {
            "connectivity": "con2",
            "RF_outputs": {
                "1": {
                    "LO_frequency": 7370000000.0,
                    "gain": -10.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "4": {
                    "LO_frequency": 5900000000.0,
                    "gain": 0.0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
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
            "operations": {
                "-164126628865188911": "-164126628865188911",
                "-7009042038113738942": "-7009042038113738942",
                "8016682567654673542": "8016682567654673542",
                "52491366316988517": "52491366316988517",
                "2814767558931722162": "2814767558931722162",
                "5076625473023077071": "5076625473023077071",
                "8956581005421886658": "8956581005421886658",
                "-7873301612554006437": "-7873301612554006437",
                "717081487210833740": "717081487210833740",
                "1889309654779964293": "1889309654779964293",
                "359623134795485717": "359623134795485717",
                "-4988625125260856487": "-4988625125260856487",
                "-5550191170562876634": "-5550191170562876634",
                "-6111588085425425586": "-6111588085425425586",
                "266652478318346996": "266652478318346996",
                "-7638066444208317632": "-7638066444208317632",
                "2914809268673952775": "2914809268673952775",
                "3822908648087794801": "3822908648087794801",
                "5514632396013246107": "5514632396013246107",
                "-4275738695597305651": "-4275738695597305651",
                "1921827109723645217": "1921827109723645217",
                "7236245621965069123": "7236245621965069123",
                "1729256648351813092": "1729256648351813092",
                "-5666600396346030177": "-5666600396346030177",
                "-4972177436948756488": "-4972177436948756488",
                "-7309571846804030613": "-7309571846804030613",
                "-722003858977088807": "-722003858977088807",
                "-1112872323470008628": "-1112872323470008628",
                "-4946484525243574253": "-4946484525243574253",
                "-7694144158965913873": "-7694144158965913873",
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
            "intermediate_frequency": 10073341.0,
            "time_of_flight": 224.0,
            "smearing": 0.0,
            "operations": {
                "-1741302944044372701": "-1741302944044372701_B2/acquisition",
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
            "intermediate_frequency": 63692382.0,
            "operations": {
                "-6585968513791844179": "-6585968513791844179",
            },
        },
    },
    "pulses": {
        "-6585968513791844179": {
            "length": 40,
            "waveforms": {
                "I": "-6585968513791844179_i",
                "Q": "-6585968513791844179_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9050700954715220040": {
            "length": 16,
            "waveforms": {
                "single": "9050700954715220040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1741302944044372701_B2/acquisition": {
            "length": 2000.0,
            "waveforms": {
                "I": "-8174328342881317996_i",
                "Q": "-8174328342881317996_q",
            },
            "digital_marker": "ON",
            "operation": "measurement",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
        },
        "-9131541413759145051": {
            "length": 16,
            "waveforms": {
                "single": "-9131541413759145051",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7205224739123158010": {
            "length": 16,
            "waveforms": {
                "single": "7205224739123158010",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5458220889669468116": {
            "length": 16,
            "waveforms": {
                "single": "5458220889669468116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5923434123016257132": {
            "length": 16,
            "waveforms": {
                "single": "-5923434123016257132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4288629829290113043": {
            "length": 16,
            "waveforms": {
                "single": "-4288629829290113043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "224862136626242013": {
            "length": 16,
            "waveforms": {
                "single": "224862136626242013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2895681670847542446": {
            "length": 16,
            "waveforms": {
                "single": "2895681670847542446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7261980149505854049": {
            "length": 16,
            "waveforms": {
                "single": "-7261980149505854049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7822458837988356290": {
            "length": 16,
            "waveforms": {
                "single": "-7822458837988356290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8568533287076536978": {
            "length": 16,
            "waveforms": {
                "single": "8568533287076536978",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4674794086681186088": {
            "length": 16,
            "waveforms": {
                "single": "4674794086681186088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1704045741485071543": {
            "length": 16,
            "waveforms": {
                "single": "-1704045741485071543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "44904476768858220": {
            "length": 16,
            "waveforms": {
                "single": "44904476768858220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5662695876224425042": {
            "length": 16,
            "waveforms": {
                "single": "5662695876224425042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6372099158211672012": {
            "length": 16,
            "waveforms": {
                "single": "-6372099158211672012",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1546814767260175217": {
            "length": 20,
            "waveforms": {
                "single": "-1546814767260175217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7374115000206132047": {
            "length": 20,
            "waveforms": {
                "single": "-7374115000206132047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3216353019215632699": {
            "length": 20,
            "waveforms": {
                "single": "3216353019215632699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8909729046407383099": {
            "length": 20,
            "waveforms": {
                "single": "-8909729046407383099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1123609973053160968": {
            "length": 24,
            "waveforms": {
                "single": "-1123609973053160968",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8892532386715499652": {
            "length": 24,
            "waveforms": {
                "single": "8892532386715499652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4137328351939705565": {
            "length": 24,
            "waveforms": {
                "single": "-4137328351939705565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5702951140420113872": {
            "length": 24,
            "waveforms": {
                "single": "-5702951140420113872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2084736329512452582": {
            "length": 28,
            "waveforms": {
                "single": "2084736329512452582",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1435931450565773040": {
            "length": 28,
            "waveforms": {
                "single": "1435931450565773040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4943342252037150343": {
            "length": 28,
            "waveforms": {
                "single": "4943342252037150343",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-118065782231584018": {
            "length": 28,
            "waveforms": {
                "single": "-118065782231584018",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1035565734676778513": {
            "length": 32,
            "waveforms": {
                "single": "-1035565734676778513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6430260038676449908": {
            "length": 32,
            "waveforms": {
                "single": "6430260038676449908",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-164126628865188911": {
            "length": 32,
            "waveforms": {
                "single": "-164126628865188911",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7009042038113738942": {
            "length": 32,
            "waveforms": {
                "single": "-7009042038113738942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8016682567654673542": {
            "length": 36,
            "waveforms": {
                "single": "8016682567654673542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "52491366316988517": {
            "length": 36,
            "waveforms": {
                "single": "52491366316988517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2814767558931722162": {
            "length": 36,
            "waveforms": {
                "single": "2814767558931722162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5076625473023077071": {
            "length": 36,
            "waveforms": {
                "single": "5076625473023077071",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8956581005421886658": {
            "length": 40,
            "waveforms": {
                "single": "8956581005421886658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7873301612554006437": {
            "length": 40,
            "waveforms": {
                "single": "-7873301612554006437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "717081487210833740": {
            "length": 40,
            "waveforms": {
                "single": "717081487210833740",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1889309654779964293": {
            "length": 40,
            "waveforms": {
                "single": "1889309654779964293",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "359623134795485717": {
            "length": 44,
            "waveforms": {
                "single": "359623134795485717",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4988625125260856487": {
            "length": 44,
            "waveforms": {
                "single": "-4988625125260856487",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5550191170562876634": {
            "length": 44,
            "waveforms": {
                "single": "-5550191170562876634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6111588085425425586": {
            "length": 44,
            "waveforms": {
                "single": "-6111588085425425586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "266652478318346996": {
            "length": 48,
            "waveforms": {
                "single": "266652478318346996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7638066444208317632": {
            "length": 48,
            "waveforms": {
                "single": "-7638066444208317632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2914809268673952775": {
            "length": 48,
            "waveforms": {
                "single": "2914809268673952775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3822908648087794801": {
            "length": 48,
            "waveforms": {
                "single": "3822908648087794801",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5514632396013246107": {
            "length": 52,
            "waveforms": {
                "single": "5514632396013246107",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4275738695597305651": {
            "length": 52,
            "waveforms": {
                "single": "-4275738695597305651",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1921827109723645217": {
            "length": 52,
            "waveforms": {
                "single": "1921827109723645217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7236245621965069123": {
            "length": 52,
            "waveforms": {
                "single": "7236245621965069123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1729256648351813092": {
            "length": 56,
            "waveforms": {
                "single": "1729256648351813092",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5666600396346030177": {
            "length": 56,
            "waveforms": {
                "single": "-5666600396346030177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4972177436948756488": {
            "length": 56,
            "waveforms": {
                "single": "-4972177436948756488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7309571846804030613": {
            "length": 56,
            "waveforms": {
                "single": "-7309571846804030613",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-722003858977088807": {
            "length": 60,
            "waveforms": {
                "single": "-722003858977088807",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1112872323470008628": {
            "length": 60,
            "waveforms": {
                "single": "-1112872323470008628",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4946484525243574253": {
            "length": 60,
            "waveforms": {
                "single": "-4946484525243574253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7694144158965913873": {
            "length": 60,
            "waveforms": {
                "single": "-7694144158965913873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6585968513791844179_i": {
            "samples": [0.00020272710178481995, 0.0002588094340347883, 0.0003243334534286107, 0.0003988385361872125, 0.00048108131352079836, 0.0005689086817884582, 0.0006591894461085467, 0.0007478294374550071, 0.0008298901297564485, 0.0008998216167203549, 0.00095180775985842, 0.0009802056987941597, 0.0009800457981846084, 0.0009475440813943577, 0.0008805699560155827, 0.0007790098417747416, 0.0006449735133424266, 0.00048280459894422726, 0.00029887827724257344, 0.00010119497508516105, -0.00010119497508515806, -0.0002988782772425705, -0.00048280459894422444, -0.000644973513342424, -0.000779009841774739, -0.0008805699560155803, -0.0009475440813943555, -0.0009800457981846067, -0.000980205698794158, -0.0009518077598584185, -0.0008998216167203536, -0.0008298901297564475, -0.0007478294374550062, -0.0006591894461085461, -0.0005689086817884575, -0.00048108131352079793, -0.0003988385361872122, -0.00032433345342861036, -0.00025880943403478807, -0.0002027271017848198],
            "type": "arbitrary",
        },
        "-6585968513791844179_q": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
        },
        "9050700954715220040": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-8174328342881317996_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-8174328342881317996_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-9131541413759145051": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "7205224739123158010": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "5458220889669468116": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-5923434123016257132": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-4288629829290113043": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "224862136626242013": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "2895681670847542446": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-7261980149505854049": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "-7822458837988356290": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
        },
        "8568533287076536978": {
            "samples": [0.0] * 10 + [0.25] + [0.0] * 5,
            "type": "arbitrary",
        },
        "4674794086681186088": {
            "samples": [0.0] * 10 + [0.25] * 2 + [0.0] * 4,
            "type": "arbitrary",
        },
        "-1704045741485071543": {
            "samples": [0.0] * 10 + [0.25] * 3 + [0.0] * 3,
            "type": "arbitrary",
        },
        "44904476768858220": {
            "samples": [0.0] * 10 + [0.25] * 4 + [0.0] * 2,
            "type": "arbitrary",
        },
        "5662695876224425042": {
            "samples": [0.0] * 10 + [0.25] * 5 + [0.0],
            "type": "arbitrary",
        },
        "-6372099158211672012": {
            "samples": [0.0] * 10 + [0.25] * 6,
            "type": "arbitrary",
        },
        "-1546814767260175217": {
            "samples": [0.0] * 10 + [0.25] * 7 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7374115000206132047": {
            "samples": [0.0] * 10 + [0.25] * 8 + [0.0] * 2,
            "type": "arbitrary",
        },
        "3216353019215632699": {
            "samples": [0.0] * 10 + [0.25] * 9 + [0.0],
            "type": "arbitrary",
        },
        "-8909729046407383099": {
            "samples": [0.0] * 10 + [0.25] * 10,
            "type": "arbitrary",
        },
        "-1123609973053160968": {
            "samples": [0.0] * 10 + [0.25] * 11 + [0.0] * 3,
            "type": "arbitrary",
        },
        "8892532386715499652": {
            "samples": [0.0] * 10 + [0.25] * 12 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4137328351939705565": {
            "samples": [0.0] * 10 + [0.25] * 13 + [0.0],
            "type": "arbitrary",
        },
        "-5702951140420113872": {
            "samples": [0.0] * 10 + [0.25] * 14,
            "type": "arbitrary",
        },
        "2084736329512452582": {
            "samples": [0.0] * 10 + [0.25] * 15 + [0.0] * 3,
            "type": "arbitrary",
        },
        "1435931450565773040": {
            "samples": [0.0] * 10 + [0.25] * 16 + [0.0] * 2,
            "type": "arbitrary",
        },
        "4943342252037150343": {
            "samples": [0.0] * 10 + [0.25] * 17 + [0.0],
            "type": "arbitrary",
        },
        "-118065782231584018": {
            "samples": [0.0] * 10 + [0.25] * 18,
            "type": "arbitrary",
        },
        "-1035565734676778513": {
            "samples": [0.0] * 10 + [0.25] * 19 + [0.0] * 3,
            "type": "arbitrary",
        },
        "6430260038676449908": {
            "samples": [0.0] * 10 + [0.25] * 20 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-164126628865188911": {
            "samples": [0.0] * 10 + [0.25] * 21 + [0.0],
            "type": "arbitrary",
        },
        "-7009042038113738942": {
            "samples": [0.0] * 10 + [0.25] * 22,
            "type": "arbitrary",
        },
        "8016682567654673542": {
            "samples": [0.0] * 10 + [0.25] * 23 + [0.0] * 3,
            "type": "arbitrary",
        },
        "52491366316988517": {
            "samples": [0.0] * 10 + [0.25] * 24 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2814767558931722162": {
            "samples": [0.0] * 10 + [0.25] * 25 + [0.0],
            "type": "arbitrary",
        },
        "5076625473023077071": {
            "samples": [0.0] * 10 + [0.25] * 26,
            "type": "arbitrary",
        },
        "8956581005421886658": {
            "samples": [0.0] * 10 + [0.25] * 27 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7873301612554006437": {
            "samples": [0.0] * 10 + [0.25] * 28 + [0.0] * 2,
            "type": "arbitrary",
        },
        "717081487210833740": {
            "samples": [0.0] * 10 + [0.25] * 29 + [0.0],
            "type": "arbitrary",
        },
        "1889309654779964293": {
            "samples": [0.0] * 10 + [0.25] * 30,
            "type": "arbitrary",
        },
        "359623134795485717": {
            "samples": [0.0] * 10 + [0.25] * 31 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4988625125260856487": {
            "samples": [0.0] * 10 + [0.25] * 32 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-5550191170562876634": {
            "samples": [0.0] * 10 + [0.25] * 33 + [0.0],
            "type": "arbitrary",
        },
        "-6111588085425425586": {
            "samples": [0.0] * 10 + [0.25] * 34,
            "type": "arbitrary",
        },
        "266652478318346996": {
            "samples": [0.0] * 10 + [0.25] * 35 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-7638066444208317632": {
            "samples": [0.0] * 10 + [0.25] * 36 + [0.0] * 2,
            "type": "arbitrary",
        },
        "2914809268673952775": {
            "samples": [0.0] * 10 + [0.25] * 37 + [0.0],
            "type": "arbitrary",
        },
        "3822908648087794801": {
            "samples": [0.0] * 10 + [0.25] * 38,
            "type": "arbitrary",
        },
        "5514632396013246107": {
            "samples": [0.0] * 10 + [0.25] * 39 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-4275738695597305651": {
            "samples": [0.0] * 10 + [0.25] * 40 + [0.0] * 2,
            "type": "arbitrary",
        },
        "1921827109723645217": {
            "samples": [0.0] * 10 + [0.25] * 41 + [0.0],
            "type": "arbitrary",
        },
        "7236245621965069123": {
            "samples": [0.0] * 10 + [0.25] * 42,
            "type": "arbitrary",
        },
        "1729256648351813092": {
            "samples": [0.0] * 10 + [0.25] * 43 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-5666600396346030177": {
            "samples": [0.0] * 10 + [0.25] * 44 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4972177436948756488": {
            "samples": [0.0] * 10 + [0.25] * 45 + [0.0],
            "type": "arbitrary",
        },
        "-7309571846804030613": {
            "samples": [0.0] * 10 + [0.25] * 46,
            "type": "arbitrary",
        },
        "-722003858977088807": {
            "samples": [0.0] * 10 + [0.25] * 47 + [0.0] * 3,
            "type": "arbitrary",
        },
        "-1112872323470008628": {
            "samples": [0.0] * 10 + [0.25] * 48 + [0.0] * 2,
            "type": "arbitrary",
        },
        "-4946484525243574253": {
            "samples": [0.0] * 10 + [0.25] * 49 + [0.0],
            "type": "arbitrary",
        },
        "-7694144158965913873": {
            "samples": [0.0] * 10 + [0.25] * 50,
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
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "2": {
                    "offset": -0.2819,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "3": {
                    "offset": 0.0307,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": -0.215,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "5": {
                    "offset": 0.074,
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
        "con9": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.21674190528643072,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
                    },
                },
                "4": {
                    "offset": -0.4253086474672965,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.0891790415038731, -1.024484298837039],
                        "feedback": [0.935305257333166],
                    },
                },
                "5": {
                    "offset": -0.21477959018116385,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [1.1298143371682787, -0.9007185757251136],
                        "feedback": [0.7709042385568349],
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
                "7": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "8": {
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
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "B1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 1),
            },
        },
        "D1/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con9', 3),
            },
        },
        "B2/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "operations": {
                "-164126628865188911": "-164126628865188911",
                "-7009042038113738942": "-7009042038113738942",
                "8016682567654673542": "8016682567654673542",
                "52491366316988517": "52491366316988517",
                "2814767558931722162": "2814767558931722162",
                "5076625473023077071": "5076625473023077071",
                "8956581005421886658": "8956581005421886658",
                "-7873301612554006437": "-7873301612554006437",
                "717081487210833740": "717081487210833740",
                "1889309654779964293": "1889309654779964293",
                "359623134795485717": "359623134795485717",
                "-4988625125260856487": "-4988625125260856487",
                "-5550191170562876634": "-5550191170562876634",
                "-6111588085425425586": "-6111588085425425586",
                "266652478318346996": "266652478318346996",
                "-7638066444208317632": "-7638066444208317632",
                "2914809268673952775": "2914809268673952775",
                "3822908648087794801": "3822908648087794801",
                "5514632396013246107": "5514632396013246107",
                "-4275738695597305651": "-4275738695597305651",
                "1921827109723645217": "1921827109723645217",
                "7236245621965069123": "7236245621965069123",
                "1729256648351813092": "1729256648351813092",
                "-5666600396346030177": "-5666600396346030177",
                "-4972177436948756488": "-4972177436948756488",
                "-7309571846804030613": "-7309571846804030613",
                "-722003858977088807": "-722003858977088807",
                "-1112872323470008628": "-1112872323470008628",
                "-4946484525243574253": "-4946484525243574253",
                "-7694144158965913873": "-7694144158965913873",
            },
            "singleInput": {
                "port": ('con4', 2),
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
        "B3/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 3),
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
        "B4/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 4),
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
        "B5/flux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 0,
            "singleInput": {
                "port": ('con4', 5),
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
        "B2/acquisition": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con2', 1),
                "out2": ('con2', 2),
            },
            "time_of_flight": 224,
            "smearing": 0,
            "intermediate_frequency": 10073341.0,
            "operations": {
                "-1741302944044372701": "-1741302944044372701_B2/acquisition",
            },
            "mixInputs": {
                "I": ('con2', 1),
                "Q": ('con2', 2),
                "mixer": "B2/acquisition_mixer_3a8",
                "lo_frequency": 7370000000.0,
            },
        },
        "B2/drive": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 57,
                    "buffer": 18,
                    "port": ('con2', 7),
                },
            },
            "digitalOutputs": {},
            "intermediate_frequency": 63692382.0,
            "operations": {
                "-6585968513791844179": "-6585968513791844179",
            },
            "mixInputs": {
                "I": ('con2', 7),
                "Q": ('con2', 8),
                "mixer": "B2/drive_mixer_d9d",
                "lo_frequency": 5900000000.0,
            },
        },
    },
    "pulses": {
        "-6585968513791844179": {
            "length": 40,
            "waveforms": {
                "I": "-6585968513791844179_i",
                "Q": "-6585968513791844179_q",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "9050700954715220040": {
            "length": 16,
            "waveforms": {
                "single": "9050700954715220040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1741302944044372701_B2/acquisition": {
            "length": 2000,
            "waveforms": {
                "I": "-8174328342881317996_i",
                "Q": "-8174328342881317996_q",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights_B2/acquisition",
                "sin": "sine_weights_B2/acquisition",
                "minus_sin": "minus_sine_weights_B2/acquisition",
            },
            "operation": "measurement",
        },
        "-9131541413759145051": {
            "length": 16,
            "waveforms": {
                "single": "-9131541413759145051",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7205224739123158010": {
            "length": 16,
            "waveforms": {
                "single": "7205224739123158010",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5458220889669468116": {
            "length": 16,
            "waveforms": {
                "single": "5458220889669468116",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5923434123016257132": {
            "length": 16,
            "waveforms": {
                "single": "-5923434123016257132",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4288629829290113043": {
            "length": 16,
            "waveforms": {
                "single": "-4288629829290113043",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "224862136626242013": {
            "length": 16,
            "waveforms": {
                "single": "224862136626242013",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2895681670847542446": {
            "length": 16,
            "waveforms": {
                "single": "2895681670847542446",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7261980149505854049": {
            "length": 16,
            "waveforms": {
                "single": "-7261980149505854049",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7822458837988356290": {
            "length": 16,
            "waveforms": {
                "single": "-7822458837988356290",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8568533287076536978": {
            "length": 16,
            "waveforms": {
                "single": "8568533287076536978",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4674794086681186088": {
            "length": 16,
            "waveforms": {
                "single": "4674794086681186088",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1704045741485071543": {
            "length": 16,
            "waveforms": {
                "single": "-1704045741485071543",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "44904476768858220": {
            "length": 16,
            "waveforms": {
                "single": "44904476768858220",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5662695876224425042": {
            "length": 16,
            "waveforms": {
                "single": "5662695876224425042",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6372099158211672012": {
            "length": 16,
            "waveforms": {
                "single": "-6372099158211672012",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1546814767260175217": {
            "length": 20,
            "waveforms": {
                "single": "-1546814767260175217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7374115000206132047": {
            "length": 20,
            "waveforms": {
                "single": "-7374115000206132047",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3216353019215632699": {
            "length": 20,
            "waveforms": {
                "single": "3216353019215632699",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-8909729046407383099": {
            "length": 20,
            "waveforms": {
                "single": "-8909729046407383099",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1123609973053160968": {
            "length": 24,
            "waveforms": {
                "single": "-1123609973053160968",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8892532386715499652": {
            "length": 24,
            "waveforms": {
                "single": "8892532386715499652",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4137328351939705565": {
            "length": 24,
            "waveforms": {
                "single": "-4137328351939705565",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5702951140420113872": {
            "length": 24,
            "waveforms": {
                "single": "-5702951140420113872",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2084736329512452582": {
            "length": 28,
            "waveforms": {
                "single": "2084736329512452582",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1435931450565773040": {
            "length": 28,
            "waveforms": {
                "single": "1435931450565773040",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "4943342252037150343": {
            "length": 28,
            "waveforms": {
                "single": "4943342252037150343",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-118065782231584018": {
            "length": 28,
            "waveforms": {
                "single": "-118065782231584018",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1035565734676778513": {
            "length": 32,
            "waveforms": {
                "single": "-1035565734676778513",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "6430260038676449908": {
            "length": 32,
            "waveforms": {
                "single": "6430260038676449908",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-164126628865188911": {
            "length": 32,
            "waveforms": {
                "single": "-164126628865188911",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7009042038113738942": {
            "length": 32,
            "waveforms": {
                "single": "-7009042038113738942",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8016682567654673542": {
            "length": 36,
            "waveforms": {
                "single": "8016682567654673542",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "52491366316988517": {
            "length": 36,
            "waveforms": {
                "single": "52491366316988517",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2814767558931722162": {
            "length": 36,
            "waveforms": {
                "single": "2814767558931722162",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5076625473023077071": {
            "length": 36,
            "waveforms": {
                "single": "5076625473023077071",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "8956581005421886658": {
            "length": 40,
            "waveforms": {
                "single": "8956581005421886658",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7873301612554006437": {
            "length": 40,
            "waveforms": {
                "single": "-7873301612554006437",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "717081487210833740": {
            "length": 40,
            "waveforms": {
                "single": "717081487210833740",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1889309654779964293": {
            "length": 40,
            "waveforms": {
                "single": "1889309654779964293",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "359623134795485717": {
            "length": 44,
            "waveforms": {
                "single": "359623134795485717",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4988625125260856487": {
            "length": 44,
            "waveforms": {
                "single": "-4988625125260856487",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5550191170562876634": {
            "length": 44,
            "waveforms": {
                "single": "-5550191170562876634",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-6111588085425425586": {
            "length": 44,
            "waveforms": {
                "single": "-6111588085425425586",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "266652478318346996": {
            "length": 48,
            "waveforms": {
                "single": "266652478318346996",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7638066444208317632": {
            "length": 48,
            "waveforms": {
                "single": "-7638066444208317632",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "2914809268673952775": {
            "length": 48,
            "waveforms": {
                "single": "2914809268673952775",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "3822908648087794801": {
            "length": 48,
            "waveforms": {
                "single": "3822908648087794801",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "5514632396013246107": {
            "length": 52,
            "waveforms": {
                "single": "5514632396013246107",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4275738695597305651": {
            "length": 52,
            "waveforms": {
                "single": "-4275738695597305651",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1921827109723645217": {
            "length": 52,
            "waveforms": {
                "single": "1921827109723645217",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "7236245621965069123": {
            "length": 52,
            "waveforms": {
                "single": "7236245621965069123",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "1729256648351813092": {
            "length": 56,
            "waveforms": {
                "single": "1729256648351813092",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-5666600396346030177": {
            "length": 56,
            "waveforms": {
                "single": "-5666600396346030177",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4972177436948756488": {
            "length": 56,
            "waveforms": {
                "single": "-4972177436948756488",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7309571846804030613": {
            "length": 56,
            "waveforms": {
                "single": "-7309571846804030613",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-722003858977088807": {
            "length": 60,
            "waveforms": {
                "single": "-722003858977088807",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-1112872323470008628": {
            "length": 60,
            "waveforms": {
                "single": "-1112872323470008628",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-4946484525243574253": {
            "length": 60,
            "waveforms": {
                "single": "-4946484525243574253",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
        "-7694144158965913873": {
            "length": 60,
            "waveforms": {
                "single": "-7694144158965913873",
            },
            "digital_marker": "ON",
            "operation": "control",
        },
    },
    "waveforms": {
        "-6585968513791844179_i": {
            "samples": [0.00020272710178481995, 0.0002588094340347883, 0.0003243334534286107, 0.0003988385361872125, 0.00048108131352079836, 0.0005689086817884582, 0.0006591894461085467, 0.0007478294374550071, 0.0008298901297564485, 0.0008998216167203549, 0.00095180775985842, 0.0009802056987941597, 0.0009800457981846084, 0.0009475440813943577, 0.0008805699560155827, 0.0007790098417747416, 0.0006449735133424266, 0.00048280459894422726, 0.00029887827724257344, 0.00010119497508516105, -0.00010119497508515806, -0.0002988782772425705, -0.00048280459894422444, -0.000644973513342424, -0.000779009841774739, -0.0008805699560155803, -0.0009475440813943555, -0.0009800457981846067, -0.000980205698794158, -0.0009518077598584185, -0.0008998216167203536, -0.0008298901297564475, -0.0007478294374550062, -0.0006591894461085461, -0.0005689086817884575, -0.00048108131352079793, -0.0003988385361872122, -0.00032433345342861036, -0.00025880943403478807, -0.0002027271017848198],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6585968513791844179_q": {
            "samples": [0.0012460382379137248, 0.0016767277202166312, 0.0022213033282811904, 0.0028971257025183664, 0.0037199830373729112, 0.00470249918287307, 0.005852354789839167, 0.007170454978303785, 0.008649219696941287, 0.010271202528091139, 0.012008252339934198, 0.013821413721335572, 0.01566171357752801, 0.017471904059173184, 0.019189132601073893, 0.020748399443086044, 0.022086556238579497, 0.023146512203565634, 0.02388126137262637] + [0.024257336517404967] * 2 + [0.02388126137262637, 0.023146512203565634, 0.022086556238579497, 0.020748399443086044, 0.019189132601073893, 0.017471904059173184, 0.01566171357752801, 0.013821413721335572, 0.012008252339934198, 0.010271202528091139, 0.008649219696941287, 0.007170454978303785, 0.005852354789839167, 0.00470249918287307, 0.0037199830373729112, 0.0028971257025183664, 0.0022213033282811904, 0.0016767277202166312, 0.0012460382379137248],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "9050700954715220040": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8174328342881317996_i": {
            "sample": 0.0021,
            "type": "constant",
        },
        "-8174328342881317996_q": {
            "sample": 0.0,
            "type": "constant",
        },
        "-9131541413759145051": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7205224739123158010": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5458220889669468116": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5923434123016257132": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4288629829290113043": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "224862136626242013": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2895681670847542446": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7261980149505854049": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7822458837988356290": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8568533287076536978": {
            "samples": [0.0] * 10 + [0.25] + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4674794086681186088": {
            "samples": [0.0] * 10 + [0.25] * 2 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1704045741485071543": {
            "samples": [0.0] * 10 + [0.25] * 3 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "44904476768858220": {
            "samples": [0.0] * 10 + [0.25] * 4 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5662695876224425042": {
            "samples": [0.0] * 10 + [0.25] * 5 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6372099158211672012": {
            "samples": [0.0] * 10 + [0.25] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1546814767260175217": {
            "samples": [0.0] * 10 + [0.25] * 7 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7374115000206132047": {
            "samples": [0.0] * 10 + [0.25] * 8 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3216353019215632699": {
            "samples": [0.0] * 10 + [0.25] * 9 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-8909729046407383099": {
            "samples": [0.0] * 10 + [0.25] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1123609973053160968": {
            "samples": [0.0] * 10 + [0.25] * 11 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8892532386715499652": {
            "samples": [0.0] * 10 + [0.25] * 12 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4137328351939705565": {
            "samples": [0.0] * 10 + [0.25] * 13 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5702951140420113872": {
            "samples": [0.0] * 10 + [0.25] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2084736329512452582": {
            "samples": [0.0] * 10 + [0.25] * 15 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1435931450565773040": {
            "samples": [0.0] * 10 + [0.25] * 16 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "4943342252037150343": {
            "samples": [0.0] * 10 + [0.25] * 17 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-118065782231584018": {
            "samples": [0.0] * 10 + [0.25] * 18,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1035565734676778513": {
            "samples": [0.0] * 10 + [0.25] * 19 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "6430260038676449908": {
            "samples": [0.0] * 10 + [0.25] * 20 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-164126628865188911": {
            "samples": [0.0] * 10 + [0.25] * 21 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7009042038113738942": {
            "samples": [0.0] * 10 + [0.25] * 22,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8016682567654673542": {
            "samples": [0.0] * 10 + [0.25] * 23 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "52491366316988517": {
            "samples": [0.0] * 10 + [0.25] * 24 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2814767558931722162": {
            "samples": [0.0] * 10 + [0.25] * 25 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5076625473023077071": {
            "samples": [0.0] * 10 + [0.25] * 26,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "8956581005421886658": {
            "samples": [0.0] * 10 + [0.25] * 27 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7873301612554006437": {
            "samples": [0.0] * 10 + [0.25] * 28 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "717081487210833740": {
            "samples": [0.0] * 10 + [0.25] * 29 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1889309654779964293": {
            "samples": [0.0] * 10 + [0.25] * 30,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "359623134795485717": {
            "samples": [0.0] * 10 + [0.25] * 31 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4988625125260856487": {
            "samples": [0.0] * 10 + [0.25] * 32 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5550191170562876634": {
            "samples": [0.0] * 10 + [0.25] * 33 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-6111588085425425586": {
            "samples": [0.0] * 10 + [0.25] * 34,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "266652478318346996": {
            "samples": [0.0] * 10 + [0.25] * 35 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7638066444208317632": {
            "samples": [0.0] * 10 + [0.25] * 36 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "2914809268673952775": {
            "samples": [0.0] * 10 + [0.25] * 37 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "3822908648087794801": {
            "samples": [0.0] * 10 + [0.25] * 38,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "5514632396013246107": {
            "samples": [0.0] * 10 + [0.25] * 39 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4275738695597305651": {
            "samples": [0.0] * 10 + [0.25] * 40 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1921827109723645217": {
            "samples": [0.0] * 10 + [0.25] * 41 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "7236245621965069123": {
            "samples": [0.0] * 10 + [0.25] * 42,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "1729256648351813092": {
            "samples": [0.0] * 10 + [0.25] * 43 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-5666600396346030177": {
            "samples": [0.0] * 10 + [0.25] * 44 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4972177436948756488": {
            "samples": [0.0] * 10 + [0.25] * 45 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7309571846804030613": {
            "samples": [0.0] * 10 + [0.25] * 46,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-722003858977088807": {
            "samples": [0.0] * 10 + [0.25] * 47 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-1112872323470008628": {
            "samples": [0.0] * 10 + [0.25] * 48 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-4946484525243574253": {
            "samples": [0.0] * 10 + [0.25] * 49 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "-7694144158965913873": {
            "samples": [0.0] * 10 + [0.25] * 50,
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
        "cosine_weights_B2/acquisition": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights_B2/acquisition": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "B2/acquisition_mixer_3a8": [{'intermediate_frequency': 10073341.0, 'lo_frequency': 7370000000.0, 'correction': [1, 0.0, 0.0, 1]}],
        "B2/drive_mixer_d9d": [{'intermediate_frequency': 63692382.0, 'lo_frequency': 5900000000.0, 'correction': [1, 0.0, 0.0, 1]}],
    },
}

