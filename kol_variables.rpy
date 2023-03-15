init python:
    #defining variables for The Last Dragon
    
    kol_tld_remysleep1 = False #Day 1
    kol_tld_remyvideogames = False #Day 2
    kol_tld_martinaccepted = False #Day 3
    kol_tld_remysleep2 = False #Day 3
    kol_tld_remytherapy = False #Day 4
    kol_tld_remytherapycounter = 0 #Day 4

    #Videogame Variables
    kol_tld_mckick = 6
    kol_tld_mckickcrit = 12
    kol_tld_mckickfail = 4
    kol_tld_mcpunch = 5
    kol_tld_mcpunchcrit = 10
    kol_tld_mcpunchfail = 2
    kol_tld_mcspecial = 8
    kol_tld_mcspecialfail = 3
    kol_tld_mcspecialcrit = 15

    kol_tld_remykick = 9
    kol_tld_remykickfail = 5
    kol_tld_remypunch = 6
    kol_tld_remypunchfail = 4
    kol_tld_remyspecialfail = 4
    kol_tld_remyspecial = 12

    kol_tld_mchealth = 100
    kol_tld_remyhealth = 100



    #Ending Variables
    if not persistent.kol_tld_endinga:
        persistent.kol_tld_endinga = False 

    if not persistent.kol_tld_endingb:
        persistent.kol_tld_endingb = False

    if not persistent.kol_tld_endingc:
        persistent.kol_tld_endingc = False

    if not persistent.kol_tld_endingd:
        persistent.kol_tld_endingd = False

    if not persistent.kol_tld_endinge:
        persistent.kol_tld_endinge = False

    if not persistent.kol_tld_ending_achieved:
        persistent.kol_tld_ending_achieved = False

    if not persistent.kol_tld_secretending:
        persistent.kol_tld_secretending = False
    
    kol_tld_secretending = False

    #Route Selection Variables
    kol_tld_wtpchosen = False

    #Other Variables
    kol_tld_fruitsnackstaken = False
    kol_tld_fruitsnackskept = False

    #=======================================================================

    #defining variables for The Last Hope

    #=======================================================================

    kol_tlh_chapter1B_done = False
    kol_tlh_chapter1B_mood = 0
    kol_tlh_chapter1B_food = "None"
    kol_tlh_chapter1B_drink = "None"
    kol_tlh_mcpaid = False
    kol_tlh_letter_read = False

    kol_tlh_chapter2B_mood = 0
    kol_tlh_2Bplayed = False

    kol_tlh_read_stories = False
    kol_tlh_drinkingwithlogan = False
    kol_tlh_seb_ask_nobooze = False
    kol_tlh_preventbooze = False
    kol_tlh_drinkchoice = ""
    kol_tlh_noextrabeer = False
    kol_tlh_chapter3B_mood = 0
    kol_tlh_3B_played = False
    kol_tlh_carrying_amely = False
    kol_tlh_3B_remyasked = False

    kol_tlh_question1asked = False
    kol_tlh_question2asked = False
    kol_tlh_question3asked = False

    kol_tlh_mav_trial_counter = 0
    kol_tlh_mavstillofficer = False

    kol_tlh_remytherapycounter = 0
    kol_tlh_remytherapywin = False
    kol_tlh_4B_played = False

    kol_tlh_logan_apartment = False

    kol_tlh_snack_with_logan = False
    
    
    if not persistent.kol_tlh_chapter1A_skip:
        persistent.kol_tlh_chapter1A_skip = False

    if not persistent.kol_tlh_chapter1B_skip:
        persistent.kol_tlh_chapter1B_skip = False
    
    kol_tlh_bryce_escort = False

    if not persistent.kol_tlh_chapter2A_skip:
        persistent.kol_tlh_chapter2A_skip = False

    if not persistent.kol_tlh_chapter2B_skip:
        persistent.kol_tlh_chapter2B_skip = False

    if not persistent.kol_tlh_chapter3A_skip:
        persistent.kol_tlh_chapter3A_skip = False

    if not persistent.kol_tlh_chapter3A_5_skip:
        persistent.kol_tlh_chapter3A_5_skip = False

    if not persistent.kol_tlh_chapter3B_skip:
        persistent.kol_tlh_chapter3B_skip = False

    if not persistent.kol_tlh_chapter4A_skip:
        persistent.kol_tlh_chapter4A_skip = False
    
    if not persistent.kol_tlh_chapter4A_5_skip:
        persistent.kol_tlh_chapter4A_5_skip = False    

    if not persistent.kol_tlh_chapter4B_skip:
        persistent.kol_tlh_chapter4B_skip = False




    # Ending variables

    kol_tlh_endingA_route = False
    kol_tlh_tld_crossover = False
    kol_tlh_tld_crossover2 = False

    kol_tlh_tld_crossover2_skip = False

    kol_tlh_endingA_variation = False

    kol_tlh_false_endingA_1 = False
    kol_tlh_false_endingA_2 = False
    kol_tlh_false_endingA_3 = False
    
    if not persistent.kol_tlh_EndingA_done == "A":
        persistent.kol_tlh_EndingA_done = "..."

    if not persistent.kol_tlh_alternate_EndingA_done == "A (The Last Dragon Route)":
        persistent.kol_tlh_alternate_EndingA_done = "..."

    if not persistent.kol_tlh_EndingB_done == "B":
        persistent.kol_tlh_EndingB_done = "..."

    if not persistent.kol_tlh_EndingC_done == "C":
        persistent.kol_tlh_EndingC_done = "..."

    if not persistent.kol_tlh_EndingD_done == "D":
        persistent.kol_tlh_EndingD_done = "..."

    if not persistent.kol_tlh_EndingE_done == "E":
        persistent.kol_tlh_EndingE_done = "..."


    if not persistent.kol_tlh_goodendingcheck:
        persistent.kol_tlh_goodendingcheck = False

    if not persistent.kol_tlh_badendingcheck:
        persistent.kol_tlh_badendingcheck = False


    if persistent.kol_tlh_EndingB_done == "B" or persistent.kol_tlh_EndingC_done == "C":
        persistent.kol_tlh_goodendingcheck = True

    if persistent.kol_tlh_EndingD_done == "D" or persistent.kol_tlh_EndingE_done == "E":
        persistent.kol_tlh_badendingcheck = True





    #Ending Routing variables
    kol_tlh_1B_success = False
    kol_tlh_2B_success = False
    kol_tlh_3B_success = False
    kol_tlh_4B_success = False

    kol_tlh_datecounter = 0

    kol_tlh_endingA = False
    kol_tlh_endingA_alternate = False
    kol_tlh_endingB = False
    kol_tlh_endingC = False
    kol_tlh_endingD = False
    kol_tlh_endingE = False



    #TLH minigame 1 variables

    kol_tlh_flouramount = 0
    kol_tlh_bakingsodaamount = 0
    kol_tlh_saltamount = 0
    kol_tlh_cocoapowderamount = 0
    kol_tlh_bakingpowderamount = 0
    kol_tlh_sugaramount = 0

    kol_tlh_eggamount = 0
    kol_tlh_oilamount = 0
    kol_tlh_milkamount = 0
    kol_tlh_wateramount = 0
    kol_tlh_vanillaamount = 0

    kol_tlh_askremyamount = 0
    kol_tlh_strikes = 0

    kol_tlh_mixdry = False
    kol_tlh_mixwet = False
    kol_tlh_mixfinal = False
    #Yes, I know that I probably won't need these variables, but I'm paranoid as hecc, alright?
    kol_tlh_flourfail = False
    kol_tlh_bakingsodafail = False
    kol_tlh_saltfail = False
    kol_tlh_cocoapowderfail = False
    kol_tlh_bakingpowderfail = False
    kol_tlh_sugarfail = False
    kol_tlh_eggfail = False
    kol_tlh_oilfail = False
    kol_tlh_milkfail = False
    kol_tlh_waterfail = False
    kol_tlh_vanillafail = False



    #Minigame 2 variables

    kol_tlh_stability = ""
    kol_tlh_temperature = ""
    kol_tlh_electrical_output = ""
    kol_tlh_spark_risk = ""

    kol_tlh_stability_value = 40
    kol_tlh_temperature_value = 35
    kol_tlh_electrical_output_value = 45
    kol_tlh_spark_risk_value = 30

    kol_tlh_turn_count = 0
    kol_tlh_critical_count = 0

    kol_tlh_random_dialogue = 0

    kol_tlh_chapter4_minigame_win = False






#----------------------------------------------------------------
#Variables for the menu popup (Original source: EvilChaosKnight)
#----------------------------------------------------------------

$ kol_extradisplay = 0

$ koldisplayvar1name = ""
$ koldisplayvar1 = 0
$ koldisplayvar1unit = ""
$ koldisplayvar1sec = 0
    
$ koldisplayvar2name = ""
$ koldisplayvar2 = 0
$ koldisplayvar2unit = ""
$ koldisplayvar3name = ""
$ koldisplayvar3 = 0
$ koldisplayvar3unit = ""
$ koldisplayvar4name = ""
$ koldisplayvar4 = 0
$ koldisplayvar4unit = ""
$ koldisplayvar5name = ""
$ koldisplayvar5 = 0
$ koldisplayvar5unit = ""
$ koldisplayvar6name = ""
$ koldisplayvar6 = 0
$ koldisplayvar6unit = ""
$ koldisplayvar7name = ""
$ koldisplayvar7 = 0
$ koldisplayvar7unit = ""
$ koldisplayvar8name = ""
$ koldisplayvar8 = 0
$ koldisplayvar8unit = ""