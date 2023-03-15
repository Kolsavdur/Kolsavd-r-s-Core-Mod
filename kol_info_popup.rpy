#THIS CODE DOES NOT BELONG TO ME.
#ALL CREDIT GOES TO THE ALMIGHTY EvilChaosKnight!
#I REPEAT, I DO *NOT* OWN THIS CODE NOR THE IMAGES ASSOCIATED WITH IT.
screen kol_extrainfo:
    
    if kolextradisplay == 1:
        add "image/ui/kolextras2.png" at zoom_fade_in
        
    elif kolextradisplay == 2:
        add "image/ui/kolextras2.png" at zoom_fade_in
    
    elif kolextradisplay == 3:
        add "image/ui/kolextras3.png" at zoom_fade_in
        
    elif kolextradisplay == 4:
        add "image/ui/kolextras4.png" at zoom_fade_in
    
    elif kolextradisplay == 5:
        add "image/ui/kolextras5.png" at zoom_fade_in
        
    elif kolextradisplay == 6:
        add "image/ui/kolextras6.png" at zoom_fade_in
        
    elif kolextradisplay == 7:
        add "image/ui/kolextras7.png" at zoom_fade_in
        
    elif kolextradisplay == 8:
        add "image/ui/kolextras8.png" at zoom_fade_in
        
    elif kolextradisplay == 11:
        add "image/ui/kolextras5.png" at zoom_fade_in
        
    else:
        pass

    hbox at zoom_fade_in:
        xalign 0.03
        yalign 0.0

        if kolextradisplay == 1:
#           add "image/ui/kolextras2.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]") style "status_text"
            
        elif kolextradisplay == 2:
#           add "image/ui/kolextras2.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]\n[koldisplayvar2name] {b}[koldisplayvar2]{/b}[koldisplayvar2unit]") style "status_text"
        
        elif kolextradisplay == 3:
#           add "image/ui/kolextras3.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]\n[koldisplayvar2name] {b}[koldisplayvar2]{/b}[koldisplayvar2unit]\n[koldisplayvar3name] {b}[koldisplayvar3]{/b}[koldisplayvar3unit]") style "status_text"
            
        elif kolextradisplay == 4:
#           add "image/ui/kolextras4.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]\n[koldisplayvar2name] {b}[koldisplayvar2]{/b}[koldisplayvar2unit]\n[koldisplayvar3name] {b}[koldisplayvar3]{/b}[koldisplayvar3unit]\n[koldisplayvar4name] {b}[koldisplayvar4]{/b}[koldisplayvar4unit]") style "status_text"
        
        elif kolextradisplay == 5:
#           add "image/ui/kolextras5.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]\n[koldisplayvar2name] {b}[koldisplayvar2]{/b}[koldisplayvar2unit]\n[koldisplayvar3name] {b}[koldisplayvar3]{/b}[koldisplayvar3unit]\n[koldisplayvar4name] {b}[koldisplayvar4]{/b}[koldisplayvar4unit]\n[koldisplayvar5name] {b}[koldisplayvar5]{/b}[koldisplayvar5unit]") style "status_text"
            
        elif kolextradisplay == 6:
#           add "image/ui/kolextras6.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]\n[koldisplayvar2name] {b}[koldisplayvar2]{/b}[koldisplayvar2unit]\n[koldisplayvar3name] {b}[koldisplayvar3]{/b}[koldisplayvar3unit]\n[koldisplayvar4name] {b}[koldisplayvar4]{/b}[koldisplayvar4unit]\n[koldisplayvar5name] {b}[koldisplayvar5]{/b}[koldisplayvar5unit]\n[koldisplayvar6name] {b}[koldisplayvar6]{/b}[koldisplayvar6unit]") style "status_text"
            
        elif kolextradisplay == 7:
#           add "image/ui/kolextras7.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]\n[koldisplayvar2name] {b}[koldisplayvar2]{/b}[koldisplayvar2unit]\n[koldisplayvar3name] {b}[koldisplayvar3]{/b}[koldisplayvar3unit]\n[koldisplayvar4name] {b}[koldisplayvar4]{/b}[koldisplayvar4unit]\n[koldisplayvar5name] {b}[koldisplayvar5]{/b}[koldisplayvar5unit]\n[koldisplayvar6name] {b}[koldisplayvar6]{/b}[koldisplayvar6unit]\n[koldisplayvar7name] {b}[koldisplayvar7]{/b}[koldisplayvar7unit]") style "status_text"
            
        elif kolextradisplay == 8:
#           add "image/ui/kolextras8.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1]{/b}[koldisplayvar1unit]\n[koldisplayvar2name] {b}[koldisplayvar2]{/b}[koldisplayvar2unit]\n[koldisplayvar3name] {b}[koldisplayvar3]{/b}[koldisplayvar3unit]\n[koldisplayvar4name] {b}[koldisplayvar4]{/b}[koldisplayvar4unit]\n[koldisplayvar5name] {b}[koldisplayvar5]{/b}[koldisplayvar5unit]\n[koldisplayvar6name] {b}[koldisplayvar6]{/b}[koldisplayvar6unit]\n[koldisplayvar7name] {b}[koldisplayvar7]{/b}[koldisplayvar7unit]\n[koldisplayvar8name] {b}[koldisplayvar8]{/b}[koldisplayvar8unit]") style "status_text"
            
        if kolextradisplay == 11:
#           add "image/ui/kolextras5.png"
            text _("[koldisplayvar1name]{b} [koldisplayvar1][koldisplayvar1unit][koldisplayvar1sec]{/b}\n[koldisplayvar2name] {b}[koldisplayvar2][koldisplayvar2unit]{/b}\n[koldisplayvar3name] {b}[koldisplayvar3]{/b}[koldisplayvar3unit]\n[koldisplayvar4name] {b}[koldisplayvar4]{/b}[koldisplayvar4unit]") style "status_text"
            
        else:
            pass
 