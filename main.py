from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

KV = """
BoxLayout:
    orientation: "vertical"
    AnchorLayout:
        size: 10, root.width * .14
        size_hint: 1, None
        AnchorLayout:
            size: 10, root.width * .14
            size_hint: 1, None
            canvas:
                Color:
                    rgb: .65, 0, 0
                Rectangle:
                    size: self.size
                    pos: self.pos
        GridLayout:
            cols: 7
            padding: root.width * .02, 0, root.width * .02, 0
            size: root.width, root.width * .1
            size_hint: None, None
            height: self.minimum_height
            Button:
                on_press: app.options_pressing(OPTIONS_img, ONE_img, TWO_img, THREE_img, SM)
                background_color: 1, 1, 1, 0
                Image:
                    id: OPTIONS_img
                    source: "options_icon.png"
                    size: root.width * .1, self.height
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
            Image:
                source: "separation.png"
                size: self.parent.width, self.parent.height
            Button:
                on_press: app.one_pressing(OPTIONS_img, ONE_img, TWO_img, THREE_img, SM)
                background_color: 1, 1, 1, 0
                Image:
                    id: ONE_img
                    source: "one_icon_click.png"
                    size: root.width * .1, self.height
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
            Image:
                source: "separation.png"
            Button:
                on_press: app.two_pressing(OPTIONS_img, ONE_img, TWO_img, THREE_img, SM)
                background_color: 1, 1, 1, 0
                Image:
                    id: TWO_img
                    source: "two_icon.png"
                    size: root.width * .1, self.height
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
            Image:
                source: "separation.png"
            Button:
                on_press: app.calculate(AI_input, TOT_input, FR_input, FRONT_img, DIRECTION1_img, DIRECTION2_img, RESULT_img, SIGHT_text, DIRECTION_text, NUMBER_text, DATA_text, MOVETHE_text, UNIT1_text)
                on_press: app.three_pressing(OPTIONS_img, ONE_img, TWO_img, THREE_img, SM)
                background_color: 1, 1, 1, 0
                Image:
                    id: THREE_img
                    source: "three_icon.png"
                    size: root.width * .1, self.height
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
    ScreenManager:
        id: SM
        size: root.width, root.height

# ------------------- STEP 1 ----------------------

        Screen:
            name: "step1_screen"
            AnchorLayout:
                canvas:
                    Color:
                        rgb: 1, .99, .93
                    Rectangle:
                        size: self.size
                        pos: self.pos
                ScrollView:
                    bar_margin: 5
                    bar_width: 10
                    do_scroll_x: False
                    
                    GridLayout:
                        cols: 1
                        size_hint: 1, None
                        height: self.minimum_height
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .05, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Image:
                                id: GUNSIGHTS_img
                                source: "gun_back_adjustment.png"
                                size: root.width * .6, root.width * .44
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            GridLayout:
                                cols: 2
                                size: root.width * .7, root.width * .19
                                size_hint: None, None
                                spacing: [root.width * .03, 0]
                                Button:
                                    background_color: 1, 1, 1, 0
                                    on_press: app.back_pressing(FRONT_img, BACK_img, GUNSIGHTS_img)
                                    Image:
                                        id: BACK_img
                                        source: "back_active.png"
                                        size: self.parent.width, self.parent.height
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                Button:
                                    background_color: 1, 1, 1, 0
                                    on_press: app.front_pressing(FRONT_img, BACK_img, GUNSIGHTS_img)
                                    Image:
                                        id: FRONT_img
                                        source: "front_notactive.png"
                                        size: self.parent.width, self.parent.height
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .05, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Image:
                                id: TARGET_img
                                source: "horizontal_correction.png"
                                padding: 0, 10, 0, 10
                                size: root.width * .6, root.width * .6
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            GridLayout:
                                cols: 2
                                size: root.width * .7, root.width * .19
                                size_hint: None, None
                                spacing: [root.width * .03, 0]
                                Button:
                                    background_color: 1, 1, 1, 0
                                    on_press: app.horizontal_pressing(HORIZONTAL_img, VERTICAL_img, TARGET_img, DIRECTION1_img, DIRECTION2_img, DIRECTION_img)
                                    Image:
                                        id: HORIZONTAL_img
                                        source: "horizontal_active.png"
                                        size: self.parent.width, self.parent.height
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                Button:
                                    background_color: 1, 1, 1, 0
                                    on_press: app.vertical_pressing(HORIZONTAL_img, VERTICAL_img, TARGET_img, DIRECTION1_img, DIRECTION2_img, DIRECTION_img)
                                    Image:
                                        id: VERTICAL_img
                                        source: "vertical_notactive.png"
                                        size: self.parent.width, self.parent.height
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                            Widget
                                

# ------------------- OPTIONS ----------------------

        Screen:
            name: "options_screen"
            AnchorLayout:
                canvas:
                    Color:
                        rgb: 1, .99, .93
                    Rectangle:
                        size: self.size
                        pos: self.pos
                BoxLayout:
                    orientation: "horizontal"
                    size: root.width * .7, root.width * .19
                    size_hint: None, None
                    Button:
                        background_color: 1, 1, 1, 0
                        on_press: app.cm_pressing(CM_img, INCH_img, UNIT1_text, UNIT2_text, UNIT3_text)
                        Image:
                            id: CM_img
                            source: "cm_active.png"
                            size: self.parent.width, self.parent.height
                            center_x: self.parent.center_x
                            center_y: self.parent.center_y
                    Widget:
                        size: 10, 90
                        size_hint: None, None
                    Button:
                        background_color: 1, 1, 1, 0
                        on_press: app.inch_pressing(CM_img, INCH_img, UNIT1_text, UNIT2_text, UNIT3_text)
                        Image:
                            id: INCH_img
                            source: "inch_notactive.png"
                            size: self.parent.width, self.parent.height
                            center_x: self.parent.center_x
                            center_y: self.parent.center_y
            
            
            

# ------------------- STEP 2 ----------------------

        Screen:
            name: "step2_screen"
            AnchorLayout:
                canvas:
                    Color:
                        rgb: 1, .99, .93
                    Rectangle:
                        size: self.size
                        pos: self.pos

                ScrollView:
                    bar_margin: 5
                    bar_width: 10
                    do_scroll_x: False

                    GridLayout:
                        cols: 1
                        size_hint: 1, None
                        height: self.minimum_height
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .05, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Image:
                                id: DIRECTION_img
                                source: "left_correction.png"
                                size: root.width * .6, root.width * .6
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            GridLayout:
                                cols: 2
                                size: root.width * .7, root.width * .19
                                size_hint: None, None
                                spacing: [root.width * .03, 0]
                                Button:
                                    background_color: 1, 0, 0, 0
                                    on_press: app.direction1_pressing(DIRECTION1_img, DIRECTION2_img, DIRECTION_img)
                                    Image:
                                        id: DIRECTION1_img
                                        source: "left_active.png"
                                        size: self.parent.width, self.parent.height
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                Button:
                                    background_color: 0, 1, 0, 0
                                    on_press: app.direction2_pressing(DIRECTION1_img, DIRECTION2_img, DIRECTION_img)
                                    Image:
                                        id: DIRECTION2_img
                                        source: "right_notactive.png"
                                        size: self.parent.width, self.parent.height
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .05, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget: 
                            Image:
                                source: "d_to_target.png"
                                padding: 0, 10, 0, 10
                                size: root.width * .6, root.width * .25
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Label:
                                text: "Distance between point of aim and point of impact"
                                color: 1, 0, 0
                                halign: "center"
                                text_size: root.width * .7, None
                                size: self.texture_size
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            BoxLayout:
                                orientation: "horizontal"
                                size: root.width * .7, root.width * .12
                                size_hint: None, None
                                TextInput:
                                    id: AI_input
                                    multiline: False
                                    text: ""
                                    size: root.width * .45, root.width * .12
                                    size_hint: None, None
                                Label:
                                    id: UNIT1_text
                                    bold: True
                                    text: "cm"
                                    color: 1, 0, 0
                                    halign: "right"
                                    valign: "center"
                                    text_size: root.width * .25, None
                                    size: self.texture_size
                                    size_hint: None, None
                            Widget:
                            
                            
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .05, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Image:
                                source: "gun_to_target.png"
                                padding: 0, 10, 0, 10
                                size: root.width * .6, root.width * .25
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Label:
                                text: "Distance between front sight and target"
                                color: 1, 0, 0
                                halign: "center"
                                text_size: root.width * .7, None
                                size: self.texture_size
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            BoxLayout:
                                orientation: "horizontal"
                                size: root.width * .7, root.width * .12
                                size_hint: None, None
                                TextInput:
                                    id: TOT_input
                                    multiline: False
                                    text: ""
                                    size: root.width * .45, root.width * .12
                                    size_hint: None, None
                                Label:
                                    id: UNIT2_text
                                    bold: True
                                    text: "m"
                                    color: 1, 0, 0
                                    halign: "right"
                                    valign: "center"
                                    text_size: root.width * .25, None
                                    size: self.texture_size
                                    size_hint: None, None
                            Widget:  
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .05, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Image:
                                source: "f_to_b.png"
                                padding: 0, 10, 0, 10
                                size: root.width * .6, root.width * .25
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Label:
                                text: "Distance between front and rear sights"
                                color: 1, 0, 0
                                halign: "center"
                                text_size: root.width * .7, None
                                size: self.texture_size
                                size_hint: None, None
                            Widget:
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            BoxLayout:
                                orientation: "horizontal"
                                size: root.width * .7, root.width * .12
                                size_hint: None, None
                                TextInput:
                                    id: FR_input
                                    multiline: False
                                    text: ""
                                    size: root.width * .45, root.width * .12
                                    size_hint: None, None
                                Label:
                                    id: UNIT3_text
                                    bold: True
                                    text: "cm"
                                    color: 1, 0, 0
                                    halign: "right"
                                    valign: "center"
                                    text_size: root.width * .25, None
                                    size: self.texture_size
                                    size_hint: None, None
                            Widget:
                            
                            
                        GridLayout:
                            cols: 3
                            padding: 0, root.width * .02, 0, 0
                            size_hint: 1, None
                            height: self.minimum_height
                            Widget:
                            Widget:
                                size: root.width * .7, root.width * 1.2
                                size_hint: None, None
                            Widget:
                            
# ------------------- STEP 3 ----------------------

        Screen:
            name: "step3_screen"
            AnchorLayout:
                canvas:
                    Color:
                        rgb: 1, .99, .93
                    Rectangle:
                        size: self.size
                        pos: self.pos
                
                GridLayout:
                    cols: 1
                    size_hint: 1, None
                    height: self.minimum_height
                    GridLayout:
                        cols: 3
                        size_hint: 1, None
                        height: self.minimum_height
                        Widget:
                        Image:
                            id: RESULT_img
                            source: "b_r.png"
                            padding: 0, 10, 0, 10
                            size: root.width * .8, root.width * .6
                            size_hint: None, None
                        Widget:
                    GridLayout:
                        cols: 3
                        padding: 0, root.width * .03, 0, 0
                        size_hint: 1, None
                        height: self.minimum_height
                        Widget:
                        Label:
                            id: DATA_text
                            bold: True
                            underline: True
                            text: ""
                            color: 1, 0, 0
                            halign: "center"
                            text_size: root.width * .7, None
                            size: self.texture_size
                            size_hint: None, None
                        Widget:
                    GridLayout:
                        cols: 3
                        size_hint: 1, None
                        height: self.minimum_height
                        Widget:
                        Label:
                            id: MOVETHE_text
                            text: ""
                            color: 1, 0, 0
                            halign: "center"
                            text_size: root.width * .7, None
                            size: self.texture_size
                            size_hint: None, None
                        Widget:
                    GridLayout:
                        cols: 3
                        size_hint: 1, None
                        height: self.minimum_height
                        Widget:
                        Label:
                            id: SIGHT_text
                            text: ""
                            color: 1, 0, 0
                            halign: "center"
                            text_size: root.width * .7, None
                            size: self.texture_size
                            size_hint: None, None
                        Widget:
                    GridLayout:
                        cols: 3
                        size_hint: 1, None
                        height: self.minimum_height
                        Widget:
                        Label:
                            id: DIRECTION_text
                            bold: True
                            text: ""
                            color: 1, 0, 0
                            halign: "center"
                            text_size: root.width * .7, None
                            size: self.texture_size
                            size_hint: None, None
                        Widget:
                    GridLayout:
                        cols: 3
                        size_hint: 1, None
                        height: self.minimum_height
                        Widget:
                        Label:
                            id: NUMBER_text
                            bold: True
                            text: ""
                            color: 1, 0, 0
                            halign: "center"
                            text_size: root.width * .7, None
                            size: self.texture_size
                            size_hint: None, None
                        Widget:
"""

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)
    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen

    global directionoption
    directionoption = "LEFTRIGHT"

    def options_pressing(self, OPTIONS_img, ONE_img, TWO_img, THREE_img, SM):
        OPTIONS_img.source = "options_icon_click.png"
        ONE_img.source = "one_icon.png"
        TWO_img.source = "two_icon.png"
        THREE_img.source = "three_icon.png"
        SM.transition.direction = "right"
        SM.current = "options_screen"

    def one_pressing(self, OPTIONS_img, ONE_img, TWO_img, THREE_img, SM):
        OPTIONS_img.source = "options_icon.png"
        ONE_img.source = "one_icon_click.png"
        TWO_img.source = "two_icon.png"
        THREE_img.source = "three_icon.png"
        if SM.current == "options_screen":
            SM.transition.direction = "left"
        else:
            SM.transition.direction = "right"
        SM.current = "step1_screen"

    def two_pressing(self, OPTIONS_img, ONE_img, TWO_img, THREE_img, SM):
        OPTIONS_img.source = "options_icon.png"
        ONE_img.source = "one_icon.png"
        TWO_img.source = "two_icon_click.png"
        THREE_img.source = "three_icon.png"
        if SM.current == "step3_screen":
            SM.transition.direction = "right"
        else:
            SM.transition.direction = "left"
        SM.current = "step2_screen"

    def three_pressing(self, OPTIONS_img, ONE_img, TWO_img, THREE_img, SM):
        OPTIONS_img.source = "options_icon.png"
        ONE_img.source = "one_icon.png"
        TWO_img.source = "two_icon.png"
        THREE_img.source = "three_icon_click.png"
        SM.transition.direction = "left"
        SM.current = "step3_screen"

    def cm_pressing(self, CM_img, INCH_img, UNIT1_text, UNIT2_text, UNIT3_text):
        CM_img.source = "cm_active.png"
        INCH_img.source = "inch_notactive.png"
        UNIT1_text.text = "cm"
        UNIT2_text.text = "m"
        UNIT3_text.text = "cm"

    def inch_pressing(self, CM_img, INCH_img, UNIT1_text, UNIT2_text, UNIT3_text):
        CM_img.source = "cm_notactive.png"
        INCH_img.source = "inch_active.png"
        UNIT1_text.text = "inch"
        UNIT2_text.text = "yard"
        UNIT3_text.text = "inch"

    def front_pressing(self, FRONT_img, BACK_img, GUNSIGHTS_img):
        FRONT_img.source = "front_active.png"
        BACK_img.source = "back_notactive.png"
        GUNSIGHTS_img.source = "gun_front_adjustment.png"

    def back_pressing(self, FRONT_img, BACK_img, GUNSIGHTS_img):
        FRONT_img.source = "front_notactive.png"
        BACK_img.source = "back_active.png"
        GUNSIGHTS_img.source = "gun_back_adjustment.png"

    def horizontal_pressing(self, HORIZONTAL_img, VERTICAL_img, TARGET_img, DIRECTION1_img, DIRECTION2_img,
                            DIRECTION_img):
        global directionoption
        HORIZONTAL_img.source = "horizontal_active.png"
        VERTICAL_img.source = "vertical_notactive.png"
        TARGET_img.source = "horizontal_correction.png"
        if directionoption == "UPDOWN":
            DIRECTION1_img.source = "left_active.png"
            DIRECTION2_img.source = "right_notactive.png"
            DIRECTION_img.source = "left_correction.png"
        directionoption = "LEFTRIGHT"

    def vertical_pressing(self, HORIZONTAL_img, VERTICAL_img, TARGET_img, DIRECTION1_img, DIRECTION2_img,
                          DIRECTION_img):
        global directionoption
        HORIZONTAL_img.source = "horizontal_notactive.png"
        VERTICAL_img.source = "vertical_active.png"
        TARGET_img.source = "vertical_correction.png"
        if directionoption == "LEFTRIGHT":
            DIRECTION1_img.source = "up_active.png"
            DIRECTION2_img.source = "down_notactive.png"
            DIRECTION_img.source = "vertical_correction.png"
        directionoption = "UPDOWN"

    def direction1_pressing(self, DIRECTION1_img, DIRECTION2_img, DIRECTION_img):
        global directionoption
        if directionoption == "LEFTRIGHT":
            DIRECTION1_img.source = "left_active.png"
            DIRECTION2_img.source = "right_notactive.png"
            DIRECTION_img.source = "left_correction.png"
        if directionoption == "UPDOWN":
            DIRECTION1_img.source = "up_active.png"
            DIRECTION2_img.source = "down_notactive.png"
            DIRECTION_img.source = "vertical_correction.png"

    def direction2_pressing(self, DIRECTION1_img, DIRECTION2_img, DIRECTION_img):
        global directionoption
        if directionoption == "LEFTRIGHT":
            DIRECTION1_img.source = "left_notactive.png"
            DIRECTION2_img.source = "right_active.png"
            DIRECTION_img.source = "horizontal_correction.png"
        if directionoption == "UPDOWN":
            DIRECTION1_img.source = "up_notactive.png"
            DIRECTION2_img.source = "down_active.png"
            DIRECTION_img.source = "down_correction.png"

    def calculate(self, AI_input, TOT_input, FR_input, FRONT_img, DIRECTION1_img, DIRECTION2_img, RESULT_img,
                  SIGHT_text, DIRECTION_text, NUMBER_text, DATA_text, MOVETHE_text, UNIT1_text):
        if UNIT1_text.text == "cm":
            ucor1 = 10
            ucor2 = 1000
            uresult = "mm"
            roundresult = 2
        else:
            ucor1 = 1
            ucor2 = 36
            uresult = "inch"
            roundresult = 3
        AIdot = ""
        TOTdot = ""
        FRdot = ""
        if "," in AI_input.text:
            AIdot = AI_input.text.replace(",", ".")
        if "," in TOT_input.text:
            TOTdot = TOT_input.text.replace(",", ".")
        if "," in FR_input.text:
            FRdot = FR_input.text.replace(",", ".")
        try:
            if AIdot == "":
                float(AI_input.text)
            else:
                float(AIdot)
            if FRdot == "":
                float(FR_input.text)
            else:
                float(FRdot)
            if TOTdot == "":
                float(TOT_input.text)
            else:
                float(TOTdot)
        except:
            RESULT_img.source = "no_data.png"
            DATA_text.text = "Missing data"
            MOVETHE_text.text = ""
            SIGHT_text.text = ""
            DIRECTION_text.text = ""
            NUMBER_text.text = ""
        else:
            DATA_text.text = "Correction"
            MOVETHE_text.text = "Move the"
            if AIdot == "":
                AI = float(AI_input.text) * ucor1
            else:
                AI = float(AIdot) * ucor1
            if FRdot == "":
                FR = float(FR_input.text) * ucor1
            else:
                FR = float(FRdot) * ucor1

            if TOTdot == "":
                if FRONT_img.source == "front_active.png":
                    TOT = (float(TOT_input.text) * ucor2) + (float(FR_input.text) * ucor1)
                else:
                    TOT = float(TOT_input.text) * ucor2
            else:
                if FRONT_img.source == "front_active.png":
                    TOT = (float(TOTdot) * ucor2) + FR
                else:
                    TOT = float(TOTdot) * ucor2

            result = (AI / TOT) * FR
            sight = ""
            direction = ""
            if DIRECTION1_img.source == "left_active.png":
                if FRONT_img.source == "front_active.png":
                    RESULT_img.source = "f_r.png"
                    sight = "front sight"
                    direction = "to the right"
                else:
                    RESULT_img.source = "b_l.png"
                    sight = "rear sight"
                    direction = "to the left"
            if DIRECTION1_img.source == "up_active.png":
                if FRONT_img.source == "front_active.png":
                    RESULT_img.source = "f_d.png"
                    sight = "front sight"
                    direction = "down"
                else:
                    RESULT_img.source = "b_u.png"
                    sight = "rear sight"
                    direction = "up"
            if DIRECTION2_img.source == "right_active.png":
                if FRONT_img.source == "front_active.png":
                    RESULT_img.source = "f_l.png"
                    sight = "front sight"
                    direction = "to the left"
                else:
                    RESULT_img.source = "b_r.png"
                    sight = "rear sight"
                    direction = "to the right"
            if DIRECTION2_img.source == "down_active.png":
                if FRONT_img.source == "front_active.png":
                    RESULT_img.source = "f_u.png"
                    sight = "front sight"
                    direction = "up"
                else:
                    RESULT_img.source = "b_d.png"
                    sight = "rear sight"
                    direction = "down"
            SIGHT_text.text = sight
            DIRECTION_text.text = direction
            NUMBER_text.text = "by " + str(round(result, roundresult)) + uresult

ma = MainApp()
ma.run()